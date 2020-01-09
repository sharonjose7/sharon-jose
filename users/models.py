from django.db import models
from datetime import date

# Create your models here.
#signup table

class signup(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.IntegerField()
    password = models.CharField(max_length=50)  

    class Meta:
        db_table = 'sign_up'

# faculty table

class faculties(models.Model):
    f_name = models.CharField(max_length=50)
    f_address = models.CharField(max_length=100)
    f_gender = models.CharField(max_length=10)
    f_mobile = models.IntegerField()
    f_email = models.CharField(max_length=50, null=True, blank=True)
    f_batch = models.CharField(max_length=10)
    f_qualfication = models.CharField(max_length=10)
    f_password = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'faculty_details'

#batch table

class batches(models.Model):
    b_batch = models.CharField(max_length=10)
    b_nostudents = models.IntegerField()
    b_incharge = models.CharField(max_length=40)
    
    class Meta:
        db_table = 'batch_details'

#students table
class students(models.Model):
    s_addno = models.IntegerField(primary_key=True)
    s_adddate = models.DateField()
    s_name = models.CharField(max_length=50)
    s_address = models.CharField(max_length=200)
    s_gender = models.CharField(max_length=10)
    s_dob = models.DateField()
    s_guardian = models.CharField(max_length=50)
    s_mobile = models.IntegerField()
    s_email = models.EmailField(max_length=50)
    b_batch = models.CharField(max_length=50) 
    s_qualfication = models.CharField(max_length=10)
    s_password = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'students_details'


#faculty leave table
class facultyleave(models.Model):
    f_id = models.IntegerField()
    f_name = models.CharField(max_length=50)
    l_fromdate = models.CharField(max_length=50)
    l_todate = models.CharField(max_length=50)
    l_reason = models.CharField(max_length=500)
    l_status = models.CharField(max_length=500, default='Pending')
    
    class Meta:
        db_table = 'faculty_leave_details'

 # student leave table
class studentleave(models.Model):
    s_id = models.IntegerField()
    s_name = models.CharField(max_length=50)
    l_fromdate = models.CharField(max_length=50)
    l_todate = models.CharField(max_length=50)
    l_reason = models.CharField(max_length=500)
    l_status = models.CharField(max_length=500, default='Pending')
    
    class Meta:
        db_table = 'student_leave_details'   

#assesment table
class assesment(models.Model):
    s_name = models.CharField(max_length=100)
    a_subject = models.CharField(max_length=100)
    a_no = models.IntegerField()
    t_total = models.IntegerField()
    t_mark = models.IntegerField()
    b_batch = models.CharField(max_length=500)
    
    class Meta:
       db_table = 'assesments'


#attendence table
class attendence(models.Model):
    s_addno = models.IntegerField()
    a_date = models.CharField(max_length=100)
    s_name = models.CharField(max_length=100)
    a_h1 = models.CharField(max_length=10)
    a_h2 = models.CharField(max_length=10)
    a_h3 = models.CharField(max_length=10)
    a_h4 = models.CharField(max_length=10)
    b_batch = models.CharField(max_length=100)
    
    class Meta:
       db_table = 'attendance_table'