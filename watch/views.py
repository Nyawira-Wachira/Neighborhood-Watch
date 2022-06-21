from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm,NewPostForm,NewHoodForm,HoodUpdateForm,CreateBusinessForm,BizUpdateForm
from .models import Profile,Post,Neighborhood,Business,HealthCentre,PoliceAuthority
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
                return redirect('hood')

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

@login_required
def Home(request):
    from .models import Post
    user=request.user

    posts = Post.objects.all().order_by('-posted')


    return render(request, 'home.html',{'posts':posts} )

@login_required
def CreateHood(request):
    from .models import Neighborhood
    user = request.user.id

    if request.method == 'POST':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            picture = form.cleaned_data.get('picture')
            location = form.cleaned_data.get('location')
            occupants_count = form.cleaned_data.get('occupants_count')

            h, created = Neighborhood.objects.get_or_create(name=name,picture=picture, location=location,occupants_count=occupants_count, user_id=user)
            h.save()
            return redirect('hood')
        
    else:
        form = NewHoodForm()
   
    
    return render(request, 'create_hood.html',  {'form': form})


def Hood(request):
    from .models import Neighborhood
    user=request.user

    hoods = Neighborhood.objects.all()


    return render(request, 'hood.html',{'hoods':hoods} )

@login_required
def HoodUpdate(request):
    if request.method == 'POST':
            q_form = HoodUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user)
            if q_form.is_valid():
                q_form.save()
                messages.success(request, f'Neighborhood details updated!')
                return redirect('hood')

    else:
        q_form = HoodUpdateForm(instance=request.user)

    context = {
        'q_form': q_form
    }
    return render(request, 'update_hood.html', context)

@login_required
def CreateBusiness(request):
    from .models import Business
    user = request.user.id

    if request.method == 'POST':
        form = CreateBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            picture = form.cleaned_data.get('picture')
            email = form.cleaned_data.get('email')
            
            b, created = Business.objects.get_or_create(name=name,picture=picture, email=email, user_id=user)
            b.save()
            return redirect('businesslist')
        
    else:
        form = CreateBusinessForm()
   
    
    return render(request, 'create_business.html',  {'form': form})

def NewBusiness(request):
    from .models import Business
    user=request.user

    projects = Business.objects.all()


    return render(request, 'business.html',{'projects':projects} )


@login_required
def BizUpdate(request):
    if request.method == 'POST':
            a_form = BizUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user)
            if a_form.is_valid():
                a_form.save()
                messages.success(request, f'Business details updated!')
                return redirect('hood')

    else:
        a_form = BizUpdateForm(instance=request.user)

    context = {
        'a_form': a_form
    }
    return render(request, 'update_business.html', context)

def Hospital(request):
    from .models import HealthCentre
    user=request.user

    centres = HealthCentre.objects.all()


    return render(request, 'hospital.html',{'centres':centres} )

def Security(request):
    from .models import PoliceAuthority
    user=request.user

    services = PoliceAuthority.objects.all()


    return render(request, 'police.html',{'services':services} )

def search_results(request):
    from .models import Business

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"businesses": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

