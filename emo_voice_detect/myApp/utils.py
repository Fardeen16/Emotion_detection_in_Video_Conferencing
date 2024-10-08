from django.core.mail import send_mail, EmailMessage
from django.conf import settings
import os
import magic

def make_email(recipient_list):
    file_path = "C:/Users/Khushi/Downloads/myfile5.pdf"
    subject = "PDF Reports"
    message = "PFA your analytics for this session"
    from_email = settings.EMAIL_HOST_USER
    #recipient_list = ["khushi.kenia@somaiya.edu"]#, "khushi.kenia@somaiya.edu", "psangoi@somaiya.edu", "gaurav.chawla@somaiay.edu"]
    
    with open(file_path, 'rb') as file:
        file_content = file.read()

    mime_type = magic.from_buffer(file_content, mime=True)
    # Extract the filename from the attachment_path
    file_name = os.path.basename(file_path)


    mail = EmailMessage(subject=subject, body=message, from_email=from_email, to=recipient_list)
    mail.attach(file_name, file_content, mime_type)
    mail.send()
