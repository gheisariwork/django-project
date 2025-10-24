from django.views import View
from student.models import *
from student.forms import StudentForm
from django.shortcuts import render, redirect


class AllStudentsView(View):
    html_file = "student/all_student.html"
    form = StudentForm()

    def get(self, request):
        all_students = Student.objects.all()
        context = {"students": all_students, "form": self.form}
        return render(request, self.html_file, context)

    def post(self, request):
        st_form = StudentForm(request.POST)
        if st_form.is_valid():
            saved_obj = st_form.save()
            if saved_obj:
                return redirect("todo:home")
        return render(request, self.html_file, {"form": self.form})
