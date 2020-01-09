from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
        path('faculties-home', TemplateView.as_view(template_name='faculties_home.html'), name='faculties_home'),
        path('faculties-student-table', TemplateView.as_view(template_name='faculties_students_table.html'), name='faculties_students_table'),
        path('faculties-student-registration', TemplateView.as_view(template_name='faculties_student_registration.html'), name='faculties_students_registration'),
        path('faculties-students-details', TemplateView.as_view(template_name='faculties_student_details.html'), name='faculties_student_details'),
        path('students-assesment-details', TemplateView.as_view(template_name='faculty_assesment_form.html'), name='faculties_assesment_details'),
        path('faculty-attendence-insertion', TemplateView.as_view(template_name='faculty_attendence_insertion.html'), name='faculty_attendence_insertion'),
        path('faculty-attendence-form', TemplateView.as_view(template_name='faculty_attendence_form.html'), name='faculty_attendence_form'),
        path('faculty-attendence-add', TemplateView.as_view(template_name='faculty_attendence_add_form.html'), name='faculty_attendence_add'),
        path('faculties-new-leave', TemplateView.as_view(template_name='faculties_new_leave.html'), name='faculties_new_leave'),
        path('faculty-leave-application', TemplateView.as_view(template_name='faculty_leave_application.html'), name='faculty_leave_application'),
        path('faculty-leave-approved', TemplateView.as_view(template_name='faculty_leave_approved.html'), name='faculty_leave_approved'),
        path('faculty-leave-pending', TemplateView.as_view(template_name='faculty_leave_pending.html'), name='faculty_leave_pending'),
        path('faculty-student-assesment-add', TemplateView.as_view(template_name='faculty_student_assesment_add.html'), name='faculty_student_assesment_add'),


        path('faculty-profile',views.faculty_profile, name='faculty_profile'),
        path('faculties-students-table',views.faculty_student_table, name='faculty_students_table'),
        path('students-registration',views.studentsadd, name='students_adds'),
        path('faculties-student-details',views.studentdetails, name='faculties_student_details'),
        path('faculties-student-assesments',views.assesmentdetails, name='student_assesment_form'),
        path('faculties-assesments_adds',views.assesmentadd, name='assesment_adds'),
        path('faculty-assesment-table',views.faculty_assesment_table, name='faculty_assesment_table'),
        #path('attendence-date',views.attendence_date, name='attendence_date'),
        #path('attendence-student-profile',views.attendence_student_profile, name='attendence_student_profile'),
        path('student-attendence-form',views.attendencedetails, name='student_attendence_form'),
        path('attendence-adds',views.attendenceadds, name='attendence_adds'),
        path('faculty-attendence-table',views.faculty_attendence_table, name='faculty_attendence_table'),
        path('attendence-table-add',views.attendence_table_add, name='attendence_table_add'),
        path('faculty-leave-application',views.faculty_leave_application, name='faculty_leave_application'),
        path('faculty-new-leave',views.faculty_new_leave, name='faculty_new_leave'),
        path('faculty-leave-approve',views.faculty_leave_approve, name='faculty_leave_approve'),
        path('faculty-approved-leave',views.faculty_approved_leave, name='faculty_approved_leave'),
        path('faculty_leave_personal',views.faculty_leave_personal, name='faculty_leave_personal'),



]