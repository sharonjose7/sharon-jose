from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('', TemplateView.as_view(template_name='login.html'), name='index'),
    path('signup', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('faculty-home', TemplateView.as_view(template_name='faculty_home.html'), name='faculty_home'),
    path('admin-home', TemplateView.as_view(template_name='admin_home.html'), name='admin_home'),
     path('admin-faculties-details', TemplateView.as_view(template_name='admin_faculties_details.html'), name='admin_faculties_details'),
    path('faculty-registration', TemplateView.as_view(template_name='faculty_registration.html'), name='faculty_registration'),
    #path('students', TemplateView.as_view(template_name='admin_student.html'), name='admin_student'),
    path('leave-new', TemplateView.as_view(template_name='admin_leave_new.html'), name='admin_leave_new'),
    path('admin-student-registration', TemplateView.as_view(template_name='admin_student_registration.html'), name='admin_student_registration'),
    path('admin-leave-approved', TemplateView.as_view(template_name='admin_leave_approved.html'), name='admin_leave_approved'),
    path('admin-leave-pending', TemplateView.as_view(template_name='admin_leave_pending.html'), name='admin_leave_pending'),
    path('admin_batch_registration', TemplateView.as_view(template_name='admin_batch_registration.html'), name='admin_batch_registration'),
    path('admin-batch-students-table', TemplateView.as_view(template_name='admin_batch_students_table.html'), name='admin_batch_students_table'),


    path('admin-logout',views.admin_logout, name='admin_logout'),
    path('submit',views.register, name='submit'),
    path('log',views.login_request, name='logins'),
    path('admin-faculties',views.admin_faculty_table, name='admin_faculties'),
    path('faculty-details',views.admin_faculty_detail, name='admin_faculties_details'),
    path('faculty-register',views.facultyadd, name='faculty-add'),
    path('admin-batch',views.admin_batch_table, name='admin_batch'),
    path('students',views.admin_students_table, name='admin_student'),
    path('students-details',views.admin_students_details, name='admin_student_details'),
    path('admin-new-leave',views.admin_new_leave, name='admin_new_leave'),
    path('admin-leave-approve',views.admin_leave_approve, name='admin_leave_approve'),
    path('admin-student-add',views.admin_student_add, name='admin_student_add'),
    path('batch-add',views.batch_add, name='batch_add'),
    path('admin-batch-students-table',views.admin_batch_students_table, name='admin_batch_students_table'),
    path('admin_approved_leave',views.admin_approved_leave, name='admin_approved_leave'),



]