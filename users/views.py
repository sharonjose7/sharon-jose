from django.shortcuts import render
from users.models import signup, faculties, batches, students, facultyleave
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import logout
from faculties import urls
from students import urls

#user registration
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email= request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')

        a=signup(name=name, email=email, mobile=mobile, password=password)
        a.save()
    return render(request,'login.html')

#login
def login_request(request):
   
     if request.method=='POST':
        email= request.POST.get('email')
        password = request.POST.get('password')
        email=str(email)
        password=str(password)
        u=signup.objects.filter(password=password)
        p=signup.objects.filter(email=email)
        if u.count()==1 and p.count()==1:
            QuerySet = signup.objects.all().filter( email = email )
            return render(request,'admin_home.html',{'data':QuerySet})
        else: 
            c = faculties.objects.filter(f_password = password)
            d = faculties.objects.filter(f_email = email)
            if c.count()==1 and d.count()==1:
                request.session['fac']=email
                QuerySet = faculties.objects.all().filter( f_email = email )
                return render(request,'faculties_home.html',{'data':QuerySet})
            else:
                u=students.objects.filter(s_password=password)
                p=students.objects.filter(s_email=email)
                if u.count()==1 and p.count()==1:
                    request.session['stud'] =  email
                    QuerySet = students.objects.get( s_email = email )
                    return render(request,'students_home.html',{'data':QuerySet})
                else:
                    return HttpResponse("login unsuccessfull")
                
        
#admin faculty details table views
def admin_faculty_table(request):
    facultyview = faculties.objects.all()
    return render (request,'admin_faculties.html',{'faculty':facultyview} )

#admin each faculty details
def admin_faculty_detail(request):
    ab = request.GET.get('id')
    faculty = faculties.objects.get(id=ab)
    return render (request,'admin_faculties_details.html',{'facultyview':faculty})
        

#faculty registration by admin
def facultyadd(request):
    if request.method == 'POST':

        fname = request.POST.get('fname')
        faddress= request.POST.get('faddress')
        fgender= request.POST.get('fgender')
        fmobile = request.POST.get('fmobile')
        femail = request.POST.get('femail')
        fqualification = request.POST.get('fqualification')
        fpassword = request.POST.get('fpassword')
        fbatch = request.POST.get('fbatch')

        a=faculties(f_name=fname, f_address=faddress, f_gender = fgender, f_mobile=fmobile, f_email=femail, f_qualfication=fqualification, f_password=fpassword, f_batch=fbatch)
        a.save()
    return render(request,'admin_faculties.html')

"""#display corresponding faculty details
def admin_faculty_details(request):
    facultydetails=faculties.objects.all.filter()
    return render (request,'admin_faculties.html',{'faculty':facultydetails} )"""

 #get batch details
def admin_batch_table(request):
    batchview = batches.objects.all()
    return render (request,'admin_batch.html',{'batches':batchview} )

#batch addition
def batch_add(request):
    if request.method == 'POST':
        bname = request.POST.get('bname')
        b_nos = request.POST.get('b_nos')
        bcharge = request.POST.get('bcharge')

        a = batches(b_batch= bname,b_nostudents = b_nos, b_incharge=bcharge)
        a.save()
        return render(request,'admin_batch.html')

#batch student list
def admin_batch_students_table(request):
    s = request.GET.get('batch')
    studentstable = students.objects.all().filter(b_batch=s)
    return render (request,'admin_batch_students_table.html',{'studenttable':studentstable} )

#get students table in admin
def admin_students_table(request):
    studentsview = students.objects.all()
    return render (request,'admin_student.html',{'students':studentsview} )

#admin student details
def admin_students_details(request):
    ab = request.GET.get('id')
    student = students.objects.get(s_email=ab)
    return render (request,'admin_student_details.html',{'studentsview':student})

#admin logout
def admin_logout(request):
    logout(request)
    return render(request,'login.html')

#admin new leave applications
def admin_new_leave(request):
    leaveview = facultyleave.objects.all().filter(l_status="Pending")
    return render (request,'admin_leave_new.html',{'leaveview':leaveview} )
#admin new leave to approve

def admin_leave_approve(request):
    if request.method == 'POST':
        aid = request.POST.get('approveid')
        facultyleave.objects.all().filter( id = aid ).update(l_status="Approved")

#admin approved leave applications list
def admin_approved_leave(request):
    leaveview = facultyleave.objects.all().filter(l_status="Approved")
    return render (request,'admin_leave_approved.html',{'leaveview':leaveview} )
       
#admin student registration
def admin_student_add(request):
    if request.method == 'POST':
        saddno = request.POST.get('addno')
        sadddate = request.POST.get('adddate')
        sbatch = request.POST.get('batch')
        sname = request.POST.get('name')
        saddress= request.POST.get('address')
        sgender= request.POST.get('gender')
        sdob= request.POST.get('dob')
        smobile = request.POST.get('mobile')
        sguardian = request.POST.get('guardian')
        semail = request.POST.get('email')
        squalification = request.POST.get('squalification')
        spassword = request.POST.get('password')

        a = students(s_addno=saddno,s_adddate = sadddate, s_name=sname, s_address=saddress,s_gender = sgender, s_dob=sdob, s_guardian = sguardian, s_mobile=smobile, s_email=semail, s_qualfication=squalification, s_password=spassword, b_batch=sbatch)
        a.save()
        return render(request,'admin_student.html')

