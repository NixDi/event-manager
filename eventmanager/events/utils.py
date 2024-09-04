from django.core.mail import send_mail
from django.conf import settings

def send_registration_email(user, event):
    subject = 'Підтвердження реєстрації на подію'
    message = f'Вітаю, {user.username},\n\nВи успішно зареєструвалися на подію: {event.title}.\n\nДякую!'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, from_email, recipient_list)
