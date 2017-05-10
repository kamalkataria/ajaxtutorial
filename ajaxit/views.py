from django.shortcuts import render
from ajaxit.forms import EmployeeForm
# Create your views here.
from ajaxit.models import Employees
from django.shortcuts import HttpResponse
import json
import time,datetime
def index(request):
    emp_list=Employees.objects.all()

    if request.method == 'POST':
        if 'emp_name' in request.POST and 'emp_email' in request.POST and 'emp_dob' in request.POST and 'emp_pass' in request.POST:
            form = EmployeeForm(request.POST)
            if form.is_valid():
                form.save()
                form = EmployeeForm()
                if not emp_list:
                    return render(request, 'ajaxit/index.html', {'form': form, 'msg': 'Employee Added'})
                else:
                    return render(request, 'ajaxit/index.html', {'form': form,'empx':emp_list, 'msg': 'Employee Added'})

            if not emp_list:
                return render(request, 'ajaxit/index.html',
                          {'form': form, 'msg': 'Invalid Data'})
            else:
                return render(request, 'ajaxit/index.html',
                              {'form': form,'empx':emp_list,'msg': 'Invalid Data'})
        form = EmployeeForm()
        if not emp_list:
            return render(request, 'ajaxit/index.html',{'form':form})
        else:
            return render(request, 'ajaxit/index.html',{'form':form,'empx':emp_list})

    form = EmployeeForm()
    if not emp_list:
        return render(request, 'ajaxit/index.html', {'form': form})
    else:
        return render(request, 'ajaxit/index.html', {'form': form,'empx':emp_list})


def addemployee(request):

    employee_name = request.POST.get('employee_name', 'root')
    employee_email= request.POST.get('employee_email', 'root@mail.com')
    employee_dob = request.POST.get('employee_dob', '08-01-1993')
    employee_pass = request.POST.get('employee_pass', 'toor')

    emp_obj = Employees(emp_name=str(employee_name),emp_email=str(employee_email),emp_dob=str(employee_dob),emp_pass=str(employee_pass))
    emp_obj.save()
    myemps=Employees.objects.all()
    strx=''
    strx+='<h3 class="text-success text-center page-header">List of Employees</h3>'

    strx+='<table class="table table-striped table-hover table-bordered table-condensed">'

    strx+="<tr><th class='info'>S.N.</th><th class='info'>Name</th><th class='info'>Email</th><th class='info'>D.O.B.</th><th class='info' colspan='2'>Actions</th></tr>"

    for i in range(len(myemps)):
        strx+='<tr>'
        strx+='<td>'+str(i+1)+'</td>'
        strx+='<td>'+myemps[i].emp_name+'</td>'
        strx+='<td>'+myemps[i].emp_email+'</td>'
        strx+='<td>'+str(myemps[i].emp_dob)+'</td>'
        strx+='<td>'+'<button onclick=del("'+str(myemps[i].id)+'")>Delete</button>'
        strx+='<td>'+'<button onclick=edit("'+str(myemps[i].id)+'")>Edit</button>'

        strx+='</tr>'
    strx+='</table>'
    # print(strx)

    return HttpResponse(strx)

def delemployee(request):

    employee_id = request.POST.get('employee_id', '-1')
    Employees.objects.filter(id=employee_id).delete()
    strx=''
    strx+='<h3 class="text-success text-center page-header">List of Employees</h3>'

    strx+='<table class="table table-striped table-hover table-bordered table-condensed">'
    strx+="<tr><th class='info'>S.N.</th><th class='info'>Name</th><th class='info'>Email</th><th class='info'>D.O.B.</th><th class='info' colspan='2'>Actions</th></tr>"
    myemps=Employees.objects.all()
    for i in range(len(myemps)):
        strx+='<tr>'
        strx+='<td>'+str(i+1)+'</td>'

        strx+='<td>'+myemps[i].emp_name+'</td>'
        strx+='<td>'+myemps[i].emp_email+'</td>'
        strx+='<td>'+str(myemps[i].emp_dob)+'</td>'
        strx+='<td>'+'<button onclick=del("'+str(myemps[i].id)+'")>Delete</button>'
        strx+='<td>'+'<button onclick=edit("'+str(myemps[i].id)+'")>Edit</button>'

        strx+='</tr>'
    strx+='</table>'
    return HttpResponse(strx)

def editemployee(request):

    employee_id = request.POST.get('employee_id', '-1')
    # empk=Employees.objects.filter(id=employee_id)
    myemps=Employees.objects.filter(id=employee_id)
    empdict={}
    for i in myemps:
        empdict['emp_id']=i.id
        empdict['emp_name']=i.emp_name
        empdict['emp_email']=i.emp_email
        empdict['emp_dob']=str(i.emp_dob)
        empdict['emp_pass']=str(i.emp_pass)

    return HttpResponse(json.dumps(empdict))


def editemployeefull(request):
    employee_name = request.POST.get('employee_name', 'root')
    employee_email = request.POST.get('employee_email', 'root@mail.com')
    employee_dob = request.POST.get('employee_dob', '08-01-1993')
    employee_pass = request.POST.get('employee_pass', 'toor')
    employee_id=request.POST.get('employee_id', 'root')
    myemps=Employees.objects.filter(id=employee_id)
    myemps.update(emp_name=employee_name,emp_email=employee_email,emp_dob=employee_dob,emp_pass=employee_pass)
    myemps = Employees.objects.all()
    strx=''
    strx+='<h3 class="text-success text-center page-header">List of Employees</h3>'
    strx += '<table class="table table-striped table-hover table-bordered table-condensed">'
    strx += "<tr><th class='info'>S.N.</th><th class='info'>Name</th><th class='info'>Email</th><th class='info'>D.O.B.</th><th class='info' colspan='2'>Actions</th></tr>"

    for i in range(len(myemps)):
        strx += '<tr>'
        strx += '<td>' + str(i + 1) + '</td>'

        strx += '<td>' + myemps[i].emp_name + '</td>'
        strx += '<td>' + myemps[i].emp_email + '</td>'
        strx += '<td>' + str(myemps[i].emp_dob) + '</td>'
        strx += '<td>' + '<button onclick=del("' + str(myemps[i].id) + '")>Delete</button>'
        strx += '<td>' + '<button onclick=edit("' + str(myemps[i].id) + '")>Edit</button>'

        strx += '</tr>'
    strx += '</table>'
    return HttpResponse(strx)




