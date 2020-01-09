from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
        path('students-home', TemplateView.as_view(template_name='students_home.html'), name='students_home'),
        path('students-profile', TemplateView.as_view(template_name='student_profile.html'), name='student_profile'),
        path('student_attendence', TemplateView.as_view(template_name='student_attendence.html'), name='student_attendence'),
        path('student-assesment', TemplateView.as_view(template_name='student_assesment.html'), name='student_assesment'),
        path('student_new_leave', TemplateView.as_view(template_name='student_new_leave.html'), name='student_new_leave'),
        path('student-leave-table', TemplateView.as_view(template_name='student_leave_table.html'), name='student_leave_table'),




        path('student-profile',views.students_profile, name='student_profile'),
        path('students-logout',views.students_logout, name='students_logout'),
        path('leave-name-field',views.leave_name_field, name='leave_name_field'),
        path('student-leave-submission',views.student_leave_submission, name='student_leave_submission'),
        path('attendence-table',views.attendence_table, name='attendence_table'),
        path('assesment-table',views.assesment_table, name='assesment_table'),



]