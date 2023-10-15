from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def make_email():
    file_path = "C:/Users/farde/Downloads/_myfile5.pdf"   
    subject = "Testing Reports"
    message = "This is just a mail from ur friend, u can chill. ~Fardeen"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["fardeen.mk@somaiay.edu"]#, "khushi.kenia@somaiay.edu", "p.sangoi@gmail.com", "gaurav.chawla@somaiya.edu"]
    mail = EmailMessage(subject=subject, body=message, from_email=from_email, to=recipient_list)
    mail.attach_file(file_path)
    mail.send()
