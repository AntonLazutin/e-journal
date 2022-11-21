from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('signup', views.SignUpView.as_view(), name='signup'),

    path('students', views.StudentsView.as_view(), name='index'),
    path('students/add', views.AddStudent.as_view(), name="add_student"),
    path('students/<int:pk>/update/', views.UpdateStudent.as_view(), name="update_student"),
    path('students/<int:pk>/delete/', views.DeleteStudent.as_view(), name="delete_student"),

    path('students/<int:pk>/grades/', views.GradesView.as_view(), name="grades_view"),
    path('students/<int:pk>/grades/add', views.AddGrade.as_view(), name="add_grade"),
    path('students/<int:pk>/grades/update', views.UpdateGrade.as_view(), name="update_grade"),
    path('students/<int:pk>/grades/delete', views.DeleteGrade.as_view(), name="delete_grade"),

    path('subjects/', views.SubjectView.as_view(), name="subjects"),
    path('subjects/add', views.AddSubject.as_view(), name="add_subject"),
    path('subjects/<int:pk>/update/', views.UpdateSubject.as_view(), name="update_subject"),
    path('subjects/<int:pk>/delete/', views.DeleteSubject.as_view(), name="delete_subject"),

    path('groups/', views.GroupView.as_view(), name="groups"),
    path('groups/<int:pk>/update/', views.UpdateGroup.as_view(), name="update_group"),
    path('groups/<int:pk>/delete/', views.DeleteGroup.as_view(), name="delete_group"),
    path('groups/add', views.AddGroup.as_view(), name="add_group"),
    
    path('teachers/', views.TeacherView.as_view(), name="teachers"),
    path('teachers/<int:pk>/update/', views.UpdateTeacher.as_view(), name="update_teacher"),
    path('teachers/<int:pk>/delete/', views.DeleteTeacher.as_view(), name="delete_teacher"),
    path('teachers/add', views.AddTeacher.as_view(), name="add_teacher"),
]
