from django.shortcuts import render

def camera_input(request):
    # Your view logic goes here
    return render(request, 'camera.html')
def home(request):
    # Add any context data if needed
    return render(request, 'base.html')
def login(request):
    return render(request, 'index.html')