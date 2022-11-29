from django.shortcuts import render
from django.views.generic import View, ListView, FormView, UpdateView, DeleteView, DetailView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import *
from .models import *


class LoginView(View):
    form_class = LoginForm
    template_name = 'login_page.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse('Invalid account')
        return render(request, self.template_name, {'form': form})
    

class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


class StudentsView(ListView):
    model = Student
    template_name = 'student_list.html'


class SubjectView(ListView):
    model = Subject
    template_name = 'subject_list.html'


class GroupView(ListView):
    model = Group
    template_name = 'group_list.html'


class TeacherView(ListView):
    model = Teacher
    template_name = 'teacher_list.html'


class AddStudent(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'add_student'
    template_name = 'add_page.html'
    form_class = StudentForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddGrade(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'add_grade'
    template_name = 'add_page.html'
    form_class = GradeForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'

    def form_valid(self, form):
        grade = form.save(commit=False)
        grade.student = Student.objects.get(id=self.kwargs['pk'])
        grade.save()
        return super().form_valid(form)


class AddGroup(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'add_group'
    template_name = 'add_page.html'
    form_class = GroupForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddSubject(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'add_subject'
    template_name = 'add_page.html'
    form_class = SubjectForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AddTeacher(LoginRequiredMixin, PermissionRequiredMixin, FormView):
    permission_required = 'add_teacher'
    template_name = 'add_page.html'
    form_class = TeacherForm
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UpdateStudent(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'change_student'
    model = Student
    template_name: str = 'update_page.html'
    fields = [
        'first_name', 'last_name', 'group', 'age'
    ]
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'


class UpdateGrade(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'change_grade'
    model = Grade
    template_name: str = 'update_page.html'
    fields = [
        'digit'
    ]
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'


class UpdateSubject(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'change_subject'
    model = Subject
    template_name: str = 'update_page.html'
    fields = [
        'name', 'teacher'
    ]
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'



class UpdateGroup(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'change_group'
    model = Group
    template_name: str = 'update_page.html'
    fields = [
        'code'
    ]
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'



class UpdateTeacher(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'change_teacher'
    model = Teacher
    template_name: str = 'update_page.html'
    fields = [
        'first_name', 'last_name'
    ]
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'


class DeleteStudent(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_student'
    model = Student
    template_name: str = 'delete_page.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'


class DeleteGrade(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_grade'
    model = Grade
    template_name: str = 'delete_page.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'


class DeleteGroup(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_group'
    model = Group
    template_name: str = 'delete_page.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'


class DeleteSubject(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_subject'
    model = Subject
    template_name: str = 'delete_page.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'

class DeleteTeacher(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'delete_teacher'
    model = Teacher
    template_name: str = 'delete_page.html'
    success_url = reverse_lazy('index')
    login_url = reverse_lazy('login')
    redirect_field_name = 'index'


class GradesView(DetailView):
    model = Student
    template_name = 'grades.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        print(Student.objects.get(id=self.kwargs['pk']).grades.all())
        context['grades'] = Student.objects.get(id=self.kwargs['pk']).grades.all()  
        return context