from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from account.forms import UserRegisterForm


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
            # new_user = st_form.save()
            if new_user:
                return redirect("todo:home")
        return render(request, self.template,
                      {"form": self.form, "message": "یوزرنیم یا پسورد اشتباه یا تکراری است"}
                      )
