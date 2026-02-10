# Architecture Overview

The platform is a **single Django monorepo** with modular domain apps under `apps/`, DRF-based versioned APIs under `/api/v1`, JWT authentication, async processing via Celery, PostgreSQL persistence, and Redis-backed event/task delivery.

## Domain Model Diagram (textual)

- `accounts.User` owns auth identity + role + KYC status.
- `profiles.CompanyProfile` anchors legal entity data.
  - `BuyerProfile` -> `User`, `CompanyProfile`
  - `SupplierProfile` -> `User`, `CompanyProfile`
- `catalog.Product` belongs to `SupplierProfile` and `Category`.
- `marketplace.Listing` wraps `Product` discoverability.
- `rfq.RFQ` links `BuyerProfile` and `Product` with lifecycle state.
  - `RFQResponse` and `NegotiationMessage` capture bidding and negotiation.
- `orders.PurchaseOrder` is generated from a finalized `RFQ`.
  - `OrderMilestone` tracks contractual and operational checkpoints.
- `payments.Payment` belongs to `PurchaseOrder` and drives escrow lifecycle.
- `operations.ProcurementTask` and `InspectionReport` bind internal workflows to orders.
- `logistics.Shipment` and `WarehouseEntry` capture transportation and intake.
- `customs.CustomsClearance` + `ComplianceDocument` model border compliance.
- `reviews.SupplierReview` closes transaction trust loop.
- `notifications.Notification` stores omnichannel delivery intent.
- `audit.AuditLog` stores compliance-grade immutable trails.

## App-by-App Breakdown

### 1) accounts
- Custom user model (`accounts.User`) with role + KYC state.
- JWT issue/refresh endpoints.
- Admin-only user listing.

### 2) profiles
- Company, buyer, supplier profiles.
- Document verification artifacts.

### 3) catalog
- Product + category + pricing baselines + MOQ.

### 4) suppliers
- Supplier onboarding and KPI metrics.

### 5) marketplace
- Searchable listings + supplier discovery bookmarks.

### 6) rfq
- RFQ request, supplier response, negotiation threads.
- Service-layer lifecycle transition.

### 7) messaging
- Conversation and message persistence tied to RFQ/order context.

### 8) orders
- Purchase order + milestone entities.
- State-machine transition logic in service layer.

### 9) payments
- Escrow-centric payment model and invoice linkage.

### 10) operations
- Internal procurement tasks and QC reports.

### 11) logistics
- Shipment and warehouse entry lifecycle tracking.

### 12) customs
- Customs clearance status and compliance docs.

### 13) reviews
- Structured buyer feedback for supplier trust scoring.

### 14) notifications
- Event-driven user notifications (email/SMS/in-app).

### 15) audit
- Compliance logs for actor/entity/action tracing.

## API Design

Base URL: `/api/v1/`

- Auth
  - `POST /api/v1/auth/token/`
  - `POST /api/v1/auth/token/refresh/`
- Users
  - `GET /api/v1/users/`
  - `GET /api/v1/users/{id}/`
- Catalog
  - `GET/POST /api/v1/products/`
  - `GET/PATCH/DELETE /api/v1/products/{id}/`
- Marketplace
  - `GET /api/v1/listings/?search=<name>&is_active=true`
- RFQ
  - `GET/POST /api/v1/rfqs/`
  - `POST /api/v1/rfqs/{id}/open/`
- Orders
  - `GET/POST /api/v1/orders/`
  - `POST /api/v1/orders/{id}/transition/`
- Payments
  - `GET/POST /api/v1/payments/`
  - `POST /api/v1/payments/{id}/hold_escrow/`

## Workflow Diagrams (textual)

### Search to Delivery
1. Buyer searches active `marketplace.Listing`.
2. Buyer creates `rfq.RFQ`.
3. Suppliers submit `RFQResponse`; negotiation converges.
4. Approved RFQ materializes `orders.PurchaseOrder`.
5. Deposit and escrow states move in `payments.Payment`.
6. `operations` handles inspections and task execution.
7. `logistics.Shipment` created and tracked.
8. `customs.CustomsClearance` completed.
9. Order transitions to `delivered/closed`.
10. Buyer submits `reviews.SupplierReview`.

## State Machines

### RFQ lifecycle
`draft -> open -> negotiation -> agreed -> (order created)`

Terminal alternative: `draft/open/negotiation -> cancelled`

### Order lifecycle
`created -> contract_signed -> deposit_paid -> in_production -> qc_passed -> in_transit -> customs_clearance -> delivered -> closed`

### Payment lifecycle
`initiated -> escrow_held -> released`

Alternative terminal branches: `failed`, `refunded`

## Async Flows

- `common.services.events.emit(...)` publishes domain events via Celery task (`publish_event`).
- Notifications and heavy integrations run asynchronously (`notifications.tasks.send_notification`).
- Recommended future: use outbox table + Kafka for at-least-once event delivery.

## Security Model

- JWT Bearer auth (`rest_framework_simplejwt`).
- Role-based authorization at viewset + service policy layers.
- KYC status included in JWT claims for downstream gateways.
- Secure production settings: HSTS, secure cookies, SSL redirect.
- Audit app stores actor/action/entity for compliance traceability.

## Deployment Architecture

- `web`: Gunicorn/Django API
- `worker`: Celery worker
- `beat` (optional): Celery beat scheduler
- `db`: PostgreSQL
- `redis`: broker/result backend/cache
- Reverse proxy + WAF in production (Nginx/Cloud LB)

## Scalability Strategy

- Horizontal scale DRF API and Celery workers independently.
- Use read replicas for analytics-heavy queries.
- Partition high-volume tables (`audit_log`, `message`, `notification`).
- Add distributed tracing + central log aggregation.
- Shift event bus from Redis to Kafka/RabbitMQ under high throughput.

## Sample Code Sections

Implemented in repository:
- Model samples: `apps/orders/models.py`, `apps/rfq/models.py`, `apps/payments/models.py`
- Serializer samples: `apps/catalog/serializers.py`, `apps/rfq/serializers.py`
- Service samples: `apps/orders/services.py`, `apps/rfq/services.py`, `apps/payments/services.py`
- ViewSet samples: `apps/orders/views.py`, `apps/rfq/views.py`, `apps/payments/views.py`
- Settings split: `config/settings/base.py`, `dev.py`, `prod.py`
