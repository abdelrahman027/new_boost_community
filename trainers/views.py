from django.shortcuts import render
from base.models import  Trainer ,Employee
from django.shortcuts import redirect ,get_object_or_404
# from django.contrib.auth import authenticate, login, logout
import json
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def trainers(request):
    employee = get_object_or_404(Employee, user=request.user)
    trainers=Trainer.objects.all()


    context={
        "employee":employee,
        'trainers_json': json.dumps(list(Trainer.objects.values()), sort_keys=True, default=str),
        "trainers":trainers,
    }
    
    return render(request,"pages/trainers.html",context)

@login_required
def trainer_detail(request, id):
    #   employee = get_object_or_404(Employee, user=request.user)
    selected_trainer=Trainer.objects.get(pk=id)
    employee = get_object_or_404(Employee, user=request.user)

    # client_projects=Project.objects.filter(client__client_id=id)
    

    # if 'qe' in request.GET:
    #     qe = request.GET['qe']
    #     employee_list = Employee.objects.filter(
    #         Q(FirstName__icontains=qe) | Q(LastName__icontains=qe))
    # else:
    #     employee_list = Employee.objects.all()

    #     # print(selected_employee.Task_set.all())
    context = {
        # 'employee': employee,
        'selected_trainer': selected_trainer,
        # "client_projects":client_projects,

        "employee":employee
            }
    return render(request, 'pages/trainer_detail.html', context)
