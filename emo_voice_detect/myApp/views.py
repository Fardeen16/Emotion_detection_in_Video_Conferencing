from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .forms import CreateUserForm


# Create your views here.
def home(request):
    return render(request, 'base.html')

def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'index.html', context)

def login(request):
    if request.method == "POST":
        uname = request.POST.get('name')
        uemail = request.POSt.get('email')
        upassword1 = request.POST.get('password1')
        upassword2 = request.POST.get('password2')
        my_user = User.objects.create_user(uname, uemail, upassword1)
        my_user.save()
        print(uname, uemail, upassword2)
    
    
    return render(request, 'index.html')



def camera_input(request):
    return render(request, 'camera.html')

def analyze_emotion(request):
    return render(request, 'analyze_emotion.html')

class CustomSignupView(CreateView):
    form_class = UserCreationForm()
    template_name = 'index.html'
    success_url = '/login/'

class CustomLoginView(LoginView):
    template_name = 'index.html'


# <input type="email" name="email" id="signEmail" placeholder="Email">
#                         <input type="text" name="name" id="signName" placeholder="Username">
#                         <input type="password" name="password" id="signPassword" placeholder="Password"><br>
#                         <input type="submit" value="SignUp">
# @csrf_exempt
# def detect_emotion(request):
#     if request.method == 'POST':
#         image_data = request.POST.get('image_data')

#         # Initialize the Google Cloud Vision API client
#         client = vision.ImageAnnotatorClient()

#         # Convert the base64 image data to bytes
#         image_bytes = base64.b64decode(image_data.split(',')[1])

#         # Create an image object
#         image = vision.Image(content=image_bytes)

#         # Detect faces in the image
#         response = client.face_detection(image=image)

#         # Get emotion data (e.g., happiness score)
#         face = response.face_annotations[0]  # Assuming only one face is detected
#         emotions = {
#             "joy": face.joy_likelihood,
#             "sorrow": face.sorrow_likelihood,
#             "anger": face.anger_likelihood,
#             "surprise": face.surprise_likelihood,
#             "under_exposed": face.under_exposed_likelihood,
#             "blurred": face.blurred_likelihood,
#             "headwear": face.headwear_likelihood,
#         }

#         # Determine the detected emotion
#         detected_emotion  = max(emotions, key=emotions.get)

#         return JsonResponse({'emotion': detected_emotion})
#     return JsonResponse({'error': 'Invalid request method'})