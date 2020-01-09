from django.shortcuts import render
from users.models import signup, faculties, batches, students, assesment, attendence, facultyleave, studentleave
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import logout
from users import views
from students import views

#faculty logout
def faculty_logout(request):
    logout(request)
    return render(request,'login.html')

def faculty_profile(request):
    QuerySet = faculties.objects.all().filter( f_email = request.session['fac'] )[0]
    request.session['abatch'] = QuerySet.f_batch
    #request.session['bbatch'] = QuerySet.f_batch
    return render(request,'faculties_profile.html',{'data':QuerySet})

#faculty student details table 
def faculty_student_table(request):
    studentsview = students.objects.all()
    return render (request,'faculties_students_table.html',{'students1':studentsview} )

#students registration by faculty
def studentsadd(request):
    if request.method == 'POST':
        saddno = request.POST.get('addno')
        sadddate = request.POST.get('adddate')
        sname = request.POST.get('name')
        saddress= request.POST.get('address')
        sgender= request.POST.get('gender')
        sdob= request.POST.get('dob')
        smobile = request.POST.get('mobile')
        sguardian = request.POST.get('guardian')
        semail = request.POST.get('email')
        squalification = request.POST.get('squalification')
        spassword = request.POST.get('password')

        a = students(s_addno=saddno,s_adddate = sadddate, s_name=sname, s_address=saddress,s_gender = sgender, s_dob=sdob, s_guardian = sguardian, s_mobile=smobile, s_email=semail, s_qualfication=squalification, s_password=spassword, b_batch=request.session['abatch'])
        a.save()
        return render(request,'faculties_students_table.html')


#student details in facalty
def studentdetails(request):
    ab = request.GET.get('id')
    student = students.objects.get(s_email=ab)
    return render (request,'faculties_students_details.html',{'studentview':student})

#get particular student details in assesment form
def assesmentdetails(request):
    ab = request.GET.get('id')
    student = students.objects.get(s_email=ab)
    return render (request,'faculty_assesment_form.html',{'studentview':student})

#student assesment data insertion
def assesmentadd(request):
    if request.method == 'POST':
        sname = request.POST.get('name')
        sbatch = request.POST.get('batch')
        ssubject = request.POST.get('subject')
        sa_no= request.POST.get('a_no')
        st_mark= request.POST.get('t_mark')
        ss_mark= request.POST.get('s_mark')

        a = assesment(s_name=sname, a_subject=ssubject,a_no = sa_no, t_total=st_mark, t_mark = ss_mark, b_batch=sbatch)
        a.save()
        return render(request,'faculties_students_table.html')

#faculty student assesment details table 
def faculty_assesment_table(request):
    assesmentsview = assesment.objects.all()
    return render (request,'faculty_assesment_table.html',{'assesments':assesmentsview} )

        #faculty student assesment details table 
"""def faculty_assesment_table(request):
    assesmentsview = assesment.objects.get( b_batch =  request.session['abatch'] )
    return render (request,'faculty_assesment_table.html',{'assesments':assesmentsview} )"""



#attendence management

#get date from attendence insertion page
#def attendence_date(request):
 #   if request.method == 'POST':
  #      a_date = request.POST.get('a_date')
   #     request.session['adate'] = a_date
    #    return render(request,'faculty_attendence_insertion.html')

#display student details in the table
#def attendence_student_profile(request):
 #   QuerySet = students.objects.all()
  #  return render(request,'faculty_attendence_insertion.html',{'studentdata':QuerySet})

#get student details for attendence form 
def attendencedetails(request):
    bd = request.GET.get('id')
    studentattendence = students.objects.get(s_email=bd)
    return render (request,'faculty_attendence_form.html',{'studentattendence':studentattendence})

#add attendence from students details tables
def attendenceadds(request):
    if request.method == 'POST':
        sname = request.POST.get('name')
        sbatch = request.POST.get('batch')
        date = request.POST.get('date')
        h1 = request.POST.get('h1')
        h2= request.POST.get('h2')
        h3= request.POST.get('h3')
        h4= request.POST.get('h4')

        a = attendence(s_name=sname, b_batch=sbatch, a_date = date, a_h1=h1, a_h2=h2, a_h3=h3, a_h4=h4)
        a.save()
        return render(request,'faculties_students_table.html')

#faculty attendence table
def faculty_attendence_table(request):
    attendenceview = attendence.objects.all()
    return render (request,'faculty_attendence_table.html',{'attendencetable':attendenceview} )


#student attendence insertion on attendence table by faculty
def attendence_table_add(request):
    if request.method == 'POST':
        sname = request.POST.get('name')
        sbatch = request.POST.get('batch')
        date = request.POST.get('date')
        h1 = request.POST.get('h1')
        h2= request.POST.get('h2')
        h3= request.POST.get('h3')
        h4= request.POST.get('h4')

        a = attendence(s_name=sname, b_batch=sbatch, a_date = date, a_h1=h1, a_h2=h2, a_h3=h3, a_h4=h4)
        a.save()
        return render(request,'faculty_attendence_table.html')

#faculty new leave name field
def faculty_leave_personal(request):
    bd = request.GET.get('id')
    facultypersonal = faculties.objects.get(f_name=bd)
    return render (request,'faculty_leave_application.html',{'facultypersonal':facultypersonal})

#faculty application for leave
def faculty_leave_application(request):
    if request.method == 'POST':
        
        fname = request.POST.get('name')
        fdate = request.POST.get('fdate')
        tdate = request.POST.get('tdate')
        reason = request.POST.get('reason')

        a = facultyleave(f_name=fname, l_fromdate=fdate, l_todate = tdate, l_reason=reason)
        a.save()
        return render(request,'faculties_home.html')

#faculty new leave applications
def faculty_new_leave(request):
    leaveview = studentleave.objects.all().filter(l_status="Pending")
    return render (request,'faculties_new_leave.html',{'leaveview':leaveview} )

#faculty new leave to approve
def faculty_leave_approve(request):
    if request.method == 'POST':
        aid = request.POST.get('approveid')
        studentleave.objects.all().filter( id = aid ).update(l_status="Approved")

#faculty approved leave applications list
def faculty_approved_leave(request):
    leaveview = studentleave.objects.all().filter(l_status="Approved")
    return render (request,'faculty_leave_approved.html',{'leaveview':leaveview} )

