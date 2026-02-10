from celery import shared_task


@shared_task
def send_notification(notification_id: int) -> None:
    # provider integration (email/SMS/push) should run here
    pass
