from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm, ProfileForm
from .models import Profile


# Create your views here.

def user_login(request):

    if request.method == 'POST':

        user_login_form = UserLoginForm(data = request.POST)

        if user_login_form.is_valid():

            data = user_login_form.cleaned_data

            user = authenticate(username = data['username'], password = data['password'])

            if user:

                login(request, user)

                return redirect("edu:article_list")

            else:

                return HttpResponse("username and password didn't match")


    elif request.method == 'GET':

        user_login_form = UserLoginForm()

        context = {'form': user_login_form}

        return render(request, 'userprofile/login.html', context)

    else:

        return HttpResponse('WAT...')

def user_logout(request):

    logout(request)

    return redirect("edu:article_list")

def user_register(request):

    if request.method == 'POST':

        user_register_form = UserRegisterForm(data = request.POST)

        if user_register_form.is_valid():

            new_user = user_register_form.save(commit = False)

            new_user.set_password(user_register_form.cleaned_data['password'])

            new_user.save()

            login(request, new_user)

            return redirect("edu:article_list")

        else:

            return HttpResponse('SOMETHING WRONG WITH THE REGISTRATION, PLZ TRY AGAIN')

    elif request.method == 'GET':

        user_register_form = UserRegisterForm()

        context = {'form': user_register_form}

        return render(request, 'userprofile/register.html', context)

    else:

        return HttpResponse("WAT...")

# @login_required(login_url = '/userprofile/login/')
# def user_delete(request, id):
#     user = User.objects.get(id=id)
#
#     if request.method == 'POST':
#
#         return HttpResponse(str(id) + str(user))

    #     print(user)
    #
    #     if request.user == user:
    #
    #         logout(request)
    #
    #         user.delete()
    #
    #         # return redirect('edu:article_list')
    #
    #         return HttpResponse('deleted')
    #
    #     else:
    #
    #         return HttpResponse('PLZ ASK ADMINISTRATORS FOR MORE INFORMATION')
    # else:
    #
    #     return HttpResponse('WAT...')

@login_required(login_url = '/userprofile/login/')
def profile_edit(request, id):

    user = User.objects.get(id = id)

    profile = Profile.objects.get(user_id = id)

    # if Profile.objects.filter(user_id = id).exists():
    #
    #     profile = Profile.objects.get(user_id = id)
    #
    # else:
    #
    #     profile = Profile.objects.create(user = user)

    if request.method == 'POST':

        if request.user != user:

            return HttpResponse('PLZ ASK ADMINISTRATORS FOR MORE INFORMATION')

        profile_form = ProfileForm(data = request.POST)

        if profile_form.is_valid():

            profile_cd = profile_form.cleaned_data
            profile.phone = profile_cd['phone']
            profile.email = profile_cd['email']
            profile.school = profile_cd['school']
            profile.major = profile_cd['major']
            profile.bio = profile_cd['bio']

            profile.save()

            return redirect("userprofile:edit", id = id)

        else:

            return HttpResponse('PLZ TRY AGAIN')

    elif request.method == 'GET':

        profile_form = ProfileForm()

        context = {'proile_form': profile_form, 'profile': profile, 'user': user}

        return render(request, 'userprofile/edit.html', context)

    else:

        return HttpResponse('WAT...')

@login_required(login_url = '/userprofile/login/')
def profile_upload(request, id):

    user = User.objects.get(id=id)

    profile = Profile.objects.get(user_id=id)

    # if Profile.objects.filter(user_id = id).exists():
    #
    #     profile = Profile.objects.get(user_id = id)
    #
    # else:
    #
    #     profile = Profile.objects.create(user = user)

    if request.method == 'POST':

        if request.user != user:
            return HttpResponse('PLZ ASK ADMINISTRATORS FOR MORE INFORMATION')

        profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid() and 'resume' in request.FILES:

            profile_cd = profile_form.cleaned_data

            profile.resume = profile_cd['resume']

            profile.save()

            return redirect("userprofile:upload", id = id)

        else:

            return HttpResponse('PLZ TRY AGAIN')

    elif request.method == 'GET':

        profile_form = ProfileForm()

        context = {'proile_form': profile_form, 'profile': profile, 'user': user}

        return render(request, 'userprofile/upload.html', context)

    else:

        return HttpResponse('WAT...')





