from django.shortcuts import render
from users.models import signup, faculties, batches, students, facultyleave, studentleave, assesment, attendence
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.contrib.auth import logout
from users import views

#student logout
def students_logout(request):
    logout(request)
    return render(request,'login.html')

#view students profile
def students_profile(request):
    #ab = request.GET.get('id')
    #student = students.objects.get(s_email = ab)
    #return render(request,'student_profile.html',{'studentdata':student})
    QuerySet = students.objects.all().filter( s_email = request.session['stud'] )[0]
    #request.session['sbatch'] =  QuerySet.b_batch
    #request.session['sname'] =  QuerySet.s_name #for attendence table
    return render(request,'student_profile.html',{'studentdata':QuerySet})

#student leave application name
def leave_name_field(request):
    bd = request.GET.get('id')
    studentdetail = students.objects.get(s_email=bd)
    return render (request,'student_new_leave.html',{'studentname':studentdetail})
#students leave submission
def student_leave_submission(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        fdate = request.POST.get('fdate')
        tdate = request.POST.get('tdate')
        reason = request.POST.get('reason')

        a = studentleave(s_name=name, l_fromdate=fdate, l_todate = tdate, l_reason=reason)
        a.save()
        return render(request,'students_home.html')


#student attendence table
def attendence_table(request):
    ab = request.GET.get('id')
    attendenceSet = attendence.objects.all().filter(s_name = ab)
    return render(request,'student_attendence.html',{'attendencetable':attendenceSet})
    #attendenceSet = attendence.objects.get( s_name = request.session['sname'])
    

#student assesment table
def assesment_table(request):
    cd = request.GET.get('sname')
    assesmentSet = assesment.objects.all().filter(s_name=cd)
    #assesmentSet = assesment.objects.all()
    return render(request,'student_assesment.html',{'assesmenttable':assesmentSet})