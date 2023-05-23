from celery import shared_task
from django.core.mail import send_mail
from .models import Orders


@shared_task
def order_created(order_id):
    order = Orders.objects.get(id=order_id)
    subject = f'Order nr. {order_id}'
    message = f'Dear {order.first_name}, \n\n You have successfully placed an order. Your order id is {order.id}'
    mail_sent = send_mail(subject, message, 'admin@gmail.com', [order.email])
    return mail_sent
