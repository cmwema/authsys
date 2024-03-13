import random
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from django.conf import settings

def generate_otp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))

    return otp


def send_code_to_user(email):
    subject = "One time passcode"
    otp_code = generate_otp()
    print(otp_code)
    user = User.object.get(email=email)
    current_site = "authsys"

    email_body = f"""Hi {user.first_name},
Thanks for signing up on {current_site}.
Please verify your email with one time passcode : {otp_code}
    """

    from_email = settings.DEFAULT_FROM_EMAIL

    OneTimePassword.objects.create(user=user, code=otp_code)

    send_email = EmailMessage(subject=subject, body=email_body, from_email=from_email, to=[email])
    send_email.send(fail_silently=True)
