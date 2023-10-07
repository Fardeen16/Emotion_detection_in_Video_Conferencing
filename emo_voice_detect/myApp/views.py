from django.shortcuts import render, HttpResponse
import base64
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from google.cloud import vision_v1p3beta1 as vision
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

# Create your views here.
def home(request):
    return render(request, 'base.html')

def login(request):
    return render(request, 'index.html')

def camera_input(request):
    return render(request, 'camera.html')

def analyze_emotion(request):
    return render(request, 'analyze_emotion.html')


class CustomLoginView(LoginView):
    template_name = 'index.html'

class CustomSignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'index.html'
    success_url = '/login/'

@csrf_exempt
def detect_emotion(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')

        # Initialize the Google Cloud Vision API client
        client = vision.ImageAnnotatorClient()

        # Convert the base64 image data to bytes
        image_bytes = base64.b64decode(image_data.split(',')[1])

        # Create an image object
        image = vision.Image(content=image_bytes)

        # Detect faces in the image
        response = client.face_detection(image=image)

        # Get emotion data (e.g., happiness score)
        face = response.face_annotations[0]  # Assuming only one face is detected
        emotions = {
            "joy": face.joy_likelihood,
            "sorrow": face.sorrow_likelihood,
            "anger": face.anger_likelihood,
            "surprise": face.surprise_likelihood,
            "under_exposed": face.under_exposed_likelihood,
            "blurred": face.blurred_likelihood,
            "headwear": face.headwear_likelihood,
        }

        # Determine the detected emotion
        detected_emotion = max(emotions, key=emotions.get)

        return JsonResponse({'emotion': detected_emotion})
    return JsonResponse({'error': 'Invalid request method'})