from django.shortcuts import render
from django.contrib.auth.models import User


def camera_input(request):
    # Your view logic goes here
    return render(request, 'camera.html')
def home(request):
    # Add any context data if needed
    return render(request, 'base.html')
# def login(request):
#     if request.method == "POST":
#         uname = request.POST.get('name')
#         uemail = request.POSt.get('email')
#         upassword1 = request.POST.get('password1')
#         upassword2 = request.POST.get('password2')
#         my_user = User.objects.create_user(uname, uemail, upassword1)
#         my_user.save()
#         print(uname, uemail, upassword2)
#     return render(request, 'index.html')