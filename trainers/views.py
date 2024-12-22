from django.shortcuts import render
from base.models import Employee,Comments,Notification
from django.shortcuts import redirect ,get_object_or_404
# from django.contrib.auth import authenticate, login, logout
import json
from django.contrib.auth.decorators import login_required
from .models import Flight, Visa,Trainer

# Create your views here.

@login_required
def trainers(request):
    employee = get_object_or_404(Employee, user=request.user)
    trainers=Trainer.objects.all()
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')


    context={
        "employee":employee,
        'trainers_json': json.dumps(list(Trainer.objects.values()), sort_keys=True, default=str),
        "trainers":trainers,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    
    return render(request,"pages/trainers.html",context)

@login_required
def trainer_detail(request, id):
    #   employee = get_object_or_404(Employee, user=request.user)
    selected_trainer=Trainer.objects.get(pk=id)
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')                    
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    comments = selected_trainer.comments.all()


    if request.method == 'POST':
        comment = request.POST.get('comment')
        new_comment = Comments(comment=comment, trainer=selected_trainer, employee=employee)
        new_comment.save()
        return redirect('trainers-detail', id=id)
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

        "employee":employee,
        "comments":comments,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
            }
    return render(request, 'pages/trainer_detail.html', context)



@login_required
def delete_Commeent(request,id,trainer_id):
    Comments.objects.filter(pk=id).delete()
    return redirect('trainers-detail', id=trainer_id)



@login_required
def trainer_visas(request):
    employee = get_object_or_404(Employee, user=request.user)
    Visas=Visa.objects.all()
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')


    context={
        "employee":employee,
        'trainers_json': json.dumps(list(Trainer.objects.values()), sort_keys=True, default=str),
        "trainers":trainers,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications,
        "Visas":Visas,
    }
    
    return render(request,"pages/trainer_visas.html",context)



@login_required
def trainer_flights(request):
    employee = get_object_or_404(Employee, user=request.user)
    flights=Flight.objects.all()
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')


    context={
        "employee":employee,
        'trainers_json': json.dumps(list(Trainer.objects.values()), sort_keys=True, default=str),
        "trainers":trainers,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications,
        "flights":flights,
    }
    
    return render(request,"pages/trainer_flight.html",context)