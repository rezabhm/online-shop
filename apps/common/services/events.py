from dataclasses import dataclass
from typing import Any

from celery import shared_task


@dataclass
class DomainEvent:
    name: str
    payload: dict[str, Any]


@shared_task
def publish_event(name: str, payload: dict[str, Any]) -> None:
    # In production this would write to Kafka/RabbitMQ for downstream processing.
    pass


def emit(event: DomainEvent) -> None:
    publish_event.delay(event.name, event.payload)
