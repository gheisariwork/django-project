from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from account.forms import *
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
from student.models import Profile
from django.shortcuts import get_object_or_404
from django.contrib import messages

class RegisterView(View):
    form = UserRegisterForm()
    template = "account/register.html"

    def get(self, request):
        return render(request, self.template, {"form": self.form})

    def post(self, request):
        st_form = UserRegisterForm(request.POST)
        if st_form.is_valid():
            new_user = User.objects.create_user(
                username=request.POST["username"],
                email="",
                password=request.POST["password"]
            )
            if new_user:
                return redirect("todo:home")
        return render(request, self.template,
                      {"form": self.form, "message": "یوزرنیم یا پسورد اشتباه یا تکراری است"}
                      )


class LoginView(View):
    form = UserLoginForm()
    template = "account/login.html"

    def get(self, request):
        return render(request, self.template, {"form": self.form})

    def post(self, request):
        form_data = UserLoginForm(request.POST)

        # if form_data.is_valid():
        user = authenticate(username=request.POST["username"],
                            password=request.POST["password"])

        if user and user.is_authenticated:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'successfuly Loged in ')
            return redirect("account:user-profile")
        return render(request, self.template, {"form": self.form, "message": "یوزر یا پسورد اشتباه است"})


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect("account:user-login")

class DeleteView(View):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                user = User.objects.get(id=request.user.id)
                user.delete()
                return redirect("todo:home")
            except:
                return redirect("student:add_course")
            

class ProfileView(View):
    html_file = "account/profile.html"
    def get(self, request):
        if request.user.is_authenticated:
            profile = get_object_or_404(Profile, user_id=request.user.id)
            if profile.is_student:
                extended_data = profile.student
            else:
                extended_data = profile.teacher

            return render(request, self.html_file, {"profile": profile, "extended_data": extended_data,
                                                    "message": "با موفقیت وارد شدید"})
        else:
            return redirect("accounts:user-login")