from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm,NewPostForm
from .models import Profile,Post
# Create your views here.

def Register(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, "Account Created Successfully! You are now able to log in")

                return redirect('login')


        return render(request, 'authenticate/register.html',{'form':form} )

def Login(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('profile')

            else:
                messages.error (request, 'Check username or password and try again')

        return render(request, 'authenticate/login.html' )

def Logout(request):
    logout(request)

    return redirect('login')

@login_required
def UserProfile(request):
    user=request.user
    posts= Post.objects.filter(user=user).order_by('-posted')


    return render(request, 'profile.html',{'posts':posts})

@login_required
def ProfileUpdate(request):
    if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f'Your account has been updated successfully!')
                return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'update_profile.html', context)

@login_required
def CreatePost(request):
    from .models import Post
    user = request.user.id

    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.cleaned_data.get('picture')
            caption = form.cleaned_data.get('caption')

            p, created = Post.objects.get_or_create(picture=picture, caption=caption, user_id=user)
            p.save()
            return redirect('home')
        
    else:
        form = NewPostForm()
   
    
    return render(request, 'post.html',  {'form': form})

def Home(request):
    from .models import Post
    user=request.user

    posts = Post.objects.all().order_by('-posted')


    return render(request, 'home.html',{'posts':posts} )