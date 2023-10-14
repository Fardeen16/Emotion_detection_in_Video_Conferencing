from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserTable
from django.http import JsonResponse



# Create your views here.
def home(request):
    return render(request, 'base.html')

def register_old(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user) 
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)

#def loginPage(request):
def register(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user) 
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_old(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('camera_input')
        else:
            messages.info(request, "Username or password is incorrect")
            
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = user.username
            return redirect('camera_input')
        else:
            messages.info(request, "Username or password is incorrect")
            
    context = {}
    return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def stats(request):
    # if request.method == "POST":
    #     return JsonResponse({'message': 'Statistics updated successfully.'})
    return render(request, 'stats.html')

@login_required
def results_saved(request):
    if request.method == 'POST':
        # Get the logged-in user
        username = request.session.get('username')

        # Get the updated statistics from the POST data
        happy_percentage = request.POST.get('happy_percentage')
        sad_percentage = request.POST.get('sad_percentage')
        neutral_percentage = request.POST.get('neutral_percentage')
        angry_percentage = request.POST.get('angry_percentage')
        disgusted_percentage = request.POST.get('disgusted_percentage')
        fearful_percentage = request.POST.get('fearful_percentage')
        surprised_percentage = request.POST.get('surprised_percentage')
        # Get other percentages in a similar way

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None
        
        #user = User.objects.get(username=username)
        #Update the UserTable entry
        if user:
        #user_table, created = UserTable.objects.get_or_create(username=user)
        # user_table.happy = happy_percentage or 0.0
        # user_table.sad = sad_percentage or 0.0
        # user_table.angry = angry_percentage or 0.0
        # user_table.disgusted = disgusted_percentage or 0.0
        # user_table.neutral = neutral_percentage or 0.0
        # user_table.surprised = surprised_percentage or 0.0
        # user_table.fearful = fearful_percentage or 0.0
        # # Update other percentages here
        # user_table.save()
            user_table = UserTable.objects.create(
                username=user,
                happy=happy_percentage or 0.0,
                sad=sad_percentage or 0.0,
                angry=angry_percentage or 0.0,
                disgusted=disgusted_percentage or 0.0,
                neutral=neutral_percentage or 0.0,
                surprised=surprised_percentage or 0.0,
                fearful=fearful_percentage or 0.0
                # Set default values for other percentages here
            )
            user_table.save()

        return JsonResponse({'message': 'Statistics updated successfully.'})

    return JsonResponse({'message': 'Invalid request.'}, status=400)

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