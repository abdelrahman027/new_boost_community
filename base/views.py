from audioop import reverse
from email import message
from math import log
from django.core.mail import send_mail, send_mass_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Contract, Employee,Client,Course_status, Invoice,Project,Course,Course_type,Repository,AsessmentBank,Simulation,Trainer,Task,Manager,Design_Request,Portfolio,Notification
from django.db.models import Count ,Q
from django.contrib import messages
from django.shortcuts import redirect ,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
import json
from .forms import TaskForm
import openai
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


openai.api_key = settings.OPENAI_API_KEY





# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # SENDING EMAIL LOGIC @@@@@@@
            # subject = f'Welcome {username}'
            # message = f"you logged in to Boost community as {username}"
            # send_mail(
            #     subject,
            #     message,
            #     settings.EMAIL_HOST_USER,
            #     ['abdelrahmansaad027@gmail.com'],
            #     fail_silently=False
            # )
            messages.success(request, "Your logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'pages/login.html')

@login_required
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    return render(request, 'pages/logout.html')


def chat_gpt(request):
    if request.method == "POST":
        user_input = request.POST.get('user_input')
        
        if user_input:
            try:
                # Call the OpenAI API with the user input
                response = openai.Completion.create(
                    model="gpt-3.5-turbo-0613",  # You can replace with "gpt-4" if you have access
                    prompt=user_input,
                    max_tokens=150  # Customize the length of the response
                )

                return render(request, 'chat.html', {
                    'user_input': user_input,
                    'response': response.choices[0].text.strip()
                })
            except Exception as e:
                return render(request, 'pages/chat.html', {
                    'error': str(e)
                })
        else:
            return render(request, 'chat.html', {
                'error': "Please provide some input."
            })
    
    return render(request, 'pages/chat.html')
@login_required
def index(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    task_manger=Task.objects.get(task_id=20).manager
    print(task_manger)
    context={
        "employee":employee,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    
    return render(request,"pages/index.html",context)

@login_required
def projects(request):
    all_projects = Project.objects.all()
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')

    context={
        'all_projects':all_projects,
        "employee":employee,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    return render(request,"pages/projects.html",context)



@login_required
def projects_detail(request, id):
    selected_project=Project.objects.get(pk=id)
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    project_courses =Course.objects.filter(project__project_id=id)
    if request.method == 'POST':
        proposal_status = request.POST.get('proposal_status')
        invoice_status = request.POST.get('invoice_status')

        # Get files
        rfp_document = request.FILES.get('rfp_document')
        proposal_document = request.FILES.get('proposal_document')
        invoice_document = request.FILES.get('invoice_document')


        # Update Course object fields
        selected_project.proposal_status = proposal_status
        selected_project.invoice_status = invoice_status


        # Update files if they are uploaded
        if rfp_document or None:
            selected_project.rfp_document = rfp_document
        if proposal_document or None:
            selected_project.proposal_document = proposal_document
        if invoice_document or None:
            selected_project.invoice_document = invoice_document

        # Save the course instance
        selected_project.save()
        return redirect('project-detail',id=id)

 
    context = {
        # 'employee': employee,
        'selected_project': selected_project,
        # "client_projects":client_projects,
        'projects_courses_json': json.dumps(list(Course.objects.filter(project__project_id=id).values()), sort_keys=True, default=str),
        "employee":employee,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
            }
    return render(request, 'pages/project_detail.html', context)
# def login(request):
#     return render(request,"pages/login.html")

@login_required
def courses(request):
    all_courses = Course.objects.all()
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')

    context={
        'all_courses':all_courses,
        "employee":employee,
        'course_json': json.dumps(list(Course.objects.values()), sort_keys=True, default=str),
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
            }
    return render(request,"pages/courses.html",context)

@login_required
def public_courses(request):
    public_courses = Course.objects.filter(course_type=Course_type.public_course)
    sales_id =request.GET.get('sales_id')
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    all_sales=Employee.objects.filter(department__department_name="Sales")

    if sales_id :
        active_employee=Employee.objects.get(employee_id=sales_id)
        sales_courses=Course.objects.filter(Sales_man__employee_id=sales_id)
    else:
        sales_clients =None
        active_employee = None
        sales_id =None

    context={
        'public_courses':public_courses,
        "employee":employee,
        "all_sales":all_sales,
        "sales_id":sales_id,
        "sales_courses":sales_courses,
        'course_json': json.dumps(list(Course.objects.filter(Sales_man__employee_id=sales_id).values()), sort_keys=True, default=str),
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications

    }
    return render(request,"pages/public_courses.html",context)

@login_required
def courses_detail(request,id):
    selected_course = Course.objects.get(pk=id)
    course_sales=selected_course.Sales_man
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    if request.method == 'POST':
        material_status = request.POST.get('material_status')
        number_of_attendees = request.POST.get('number_of_attendees')
        certificate_status = request.POST.get('certificate_status')
        feedback = request.FILES.get('feedback')  # Treat feedback as a file field
        number_of_gift = request.POST.get('number_of_gift')

        # Get files
        material_file = request.FILES.get('material_file')
        attendance_file = request.FILES.get('attendance_file')
        certificates_file = request.FILES.get('certificates_file')
        pre_post_files = request.FILES.get('pre_post_files')

        # Update Course object fields
        selected_course.material_status = material_status
        selected_course.number_of_attendees = number_of_attendees
        selected_course.certificate_status = certificate_status
        selected_course.feedback = feedback
        selected_course.number_of_gift = number_of_gift

        # Update files if they are uploaded
        if material_file:
            selected_course.material_file = material_file
        if attendance_file:
            selected_course.attendance_file = attendance_file
        if certificates_file:
            selected_course.certificates_file = certificates_file
        if pre_post_files:
            selected_course.pre_post_files = pre_post_files

        # Save the course instance
        selected_course.save()
        return redirect('courses-detail',id=id)


    context={
        'selected_course':selected_course,
        "employee":employee,
        "course_sales":course_sales,
        'course_json': json.dumps(list(Course.objects.values()), sort_keys=True, default=str),
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications

    }
    return render(request,"pages/course_detail.html",context)


@login_required
def profile(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    context={
        "employee":employee,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    
    return render(request,"pages/profile.html",context)
@login_required
def clients(request):
    all_clients=Client.objects.all()
    sales_id =request.GET.get('sales_id')
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')

    all_sales=Employee.objects.filter(department__department_name="Sales")
    if sales_id :
        active_employee=Employee.objects.get(employee_id=sales_id)
        sales_clients=Client.objects.filter(sales_person__employee_id=sales_id)
    else:
        sales_clients =None
        active_employee = None
        sales_id =None

    context ={
        "all_clients":all_clients,
        "all_sales":all_sales,
        "request":request,
        "sales_clients":sales_clients,
        "active_employee":active_employee,
        "sales_id":sales_id,
        "employee":employee,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    return render(request,"pages/clients.html",context)
@login_required
def clients_detail(request, id):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    selected_client=Client.objects.get(pk=id)
    client_projects=Project.objects.filter(client__client_id=id)
    

    # if 'qe' in request.GET:
    #     qe = request.GET['qe']
    #     employee_list = Employee.objects.filter(
    #         Q(FirstName__icontains=qe) | Q(LastName__icontains=qe))
    # else:
    #     employee_list = Employee.objects.all()

    #     # print(selected_employee.Task_set.all())
    context = {
        # 'employee': employee,
        'selected_client': selected_client,
        "client_projects":client_projects,
        'course_json': json.dumps(list(Course.objects.values()), sort_keys=True, default=str),
        "employee":employee,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
            }
    return render(request, 'pages/client_detail.html', context)


@login_required
def sales(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')

    sales_men= Employee.objects.filter(department__department_name="Sales").annotate(
        active_client_count=Count('clients', filter=Q(clients__status=True)),
        running_courses_count=Count('courses', filter=Q(courses__status="running"))

    )

    #     sales_men=Employee.objects.filter(department=1).annotate(
    #     active_client_count=Count('clients',filter=Q(clients__status=True))
    # )

    
    sarah_active_clients=Client.objects.filter(status=True,sales_person=2)
    active_clients=Client.objects.filter(status=True)


    context={
        "sales_men":sales_men,
        "active_clients":sarah_active_clients,
        "active_clients":active_clients,
        "employee":employee,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }

    return render(request,"pages/sales.html",context)


@login_required
def learning_developers(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    l_d_men=Employee.objects.filter(department__department_name="L&D")
    projects = Project.objects.all()
    repository =Repository.objects.all()
    asessmentBank=AsessmentBank.objects.all()
    simulation=Simulation.objects.all()

    context={
        "employee":employee,
        "l_d_men":l_d_men,
        "projects":projects,
        "repository":repository,
        "asessmentBank":asessmentBank,
        "simulation":simulation,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
            }
    
    return render(request,"pages/l&d.html",context)

@login_required
def repository(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    l_d_men=Employee.objects.filter(department__department_name="L&D")
    projects = Project.objects.all()
    repository =Repository.objects.all()
    asessmentBank=AsessmentBank.objects.all()
    simulation=Simulation.objects.all()

    context={
        "employee":employee,
        "l_d_men":l_d_men,
        "projects":projects,
        "repository":repository,
        "asessmentBank":asessmentBank,
        "simulation":simulation,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
            }
    
    return render(request,"pages/repository.html",context)


@login_required
def assesment_bank(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    l_d_men=Employee.objects.filter(department__department_name="L&D")
    projects = Project.objects.all()
    repository =Repository.objects.all()
    asessmentBank=AsessmentBank.objects.all()
    simulation=Simulation.objects.all()

    context={
        "employee":employee,
        "l_d_men":l_d_men,
        "projects":projects,
        "repository":repository,
        "asessmentBank":asessmentBank,
        "simulation":simulation,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    
    return render(request,"pages/assesment-bank.html",context)
@login_required
def simulation(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    l_d_men=Employee.objects.filter(department__department_name="L&D")
    projects = Project.objects.all()
    repository =Repository.objects.all()
    asessmentBank=AsessmentBank.objects.all()
    simulation=Simulation.objects.all()

    context={
        "employee":employee,
        "l_d_men":l_d_men,
        "projects":projects,
        "repository":repository,
        "asessmentBank":asessmentBank,
        "simulation":simulation,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    
    return render(request,"pages/simulation.html",context)



# def tasks(request):
#     employee = get_object_or_404(Employee, user=request.user)
#     employee_tasks=Task.objects.filter(employee=employee.employee_id)
#     employee_done=Task.objects.filter(employee=employee.employee_id,status="Done")
#     employee_stuck=Task.objects.filter(employee=employee.employee_id,status="Stuck")
#     employee_inprogress=Task.objects.filter(employee=employee.employee_id,status="In Progress")
#     employee_missed=Task.objects.filter(employee=employee.employee_id,status="Missed")
    
#     manager = Manager.objects.get(employee__employee_id=employee.employee_id)
#     # print(employee)
#     # print(manager)


#     context={
#         "employee":employee,
#         "employee_tasks":employee_tasks,
#         "employee_done":employee_done,
#         "employee_stuck":employee_stuck,
#         "employee_inprogress":employee_inprogress,
#         "employee_missed":employee_missed

#     }
    
#     return render(request,"pages/tasks.html",context)


@login_required
def create_own_Task(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    employee_tasks=Task.objects.filter(employee=employee.employee_id)
    employee_done=Task.objects.filter(employee=employee.employee_id,status="Done")
    employee_stuck=Task.objects.filter(employee=employee.employee_id,status="Stuck")
    employee_inprogress=Task.objects.filter(employee=employee.employee_id,status="In Progress")
    employee_missed=Task.objects.filter(employee=employee.employee_id,status="Missed")
    
    manager = Manager.objects.get(employee__employee_id=employee.employee_id)
    stage=request.GET.get('stage')
    if stage == "done":
                employee_tasks=Task.objects.filter(employee=employee.employee_id,status="Done")
    elif stage == "stuck":
                employee_tasks=Task.objects.filter(employee=employee.employee_id,status="Stuck")
    elif stage == "inprogress":
                employee_tasks=Task.objects.filter(employee=employee.employee_id,status="In Progress")
    elif stage == "missed":
                employee_tasks=Task.objects.filter(employee=employee.employee_id,status="Missed")
    if request.method == 'POST':
        if len(request.POST['task_name']) > 0:
            task_name = request.POST['task_name']
            task_desc = request.POST['description']
            task_status = request.POST['task_status']
            task_deadline = request.POST['deadline']
            print("name",task_name)
            # print(task_desc)
            # print(task_status)
            # print(task_deadline)

            Task.objects.create(task_name=task_name,description=task_desc,status=task_status,deadline=task_deadline,employee=employee,manager=manager,department=employee.department,points=0)
            # Task.save()
            return redirect('tasks')
        else:
         return redirect('login')

    

    context={
        "employee":employee,
        "employee_tasks":employee_tasks,
        "employee_done":employee_done,
        "employee_stuck":employee_stuck,
        "employee_inprogress":employee_inprogress,
        "employee_missed":employee_missed,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    return render(request,'pages/tasks.html',context)


@login_required
def update_Task(request,id):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    employee_tasks=Task.objects.filter(employee=employee.employee_id)
    employee_done=Task.objects.filter(employee=employee.employee_id,status="Done")
    employee_stuck=Task.objects.filter(employee=employee.employee_id,status="Stuck")
    employee_inprogress=Task.objects.filter(employee=employee.employee_id,status="In Progress")
    employee_missed=Task.objects.filter(employee=employee.employee_id,status="Missed")
    
    task_manager = Task.objects.get(task_id=id).manager
    selected_task = Task.objects.get(pk=id)
    # task_name = request.POST['task_name']
    selected_employee = employee
    employee_user = selected_employee

    print("email: ",task_manager.employee.email)

    if request.method == 'POST':
        if len(request.POST['task_name']) > 0:
           task_name = request.POST['task_name']
           task_desc = request.POST['description']
           task_status = request.POST['task_status']
           task_deadline = request.POST['deadline']
           Task.objects.filter(pk=id).update(task_name=task_name,description=task_desc,status=task_status,deadline=task_deadline,employee=employee,manager=task_manager,department=employee.department,points=0)
           Notification.objects.create(title=f"{employee_user.firstname} {employee_user.lastname} Updated Task {task_name}",message=f"{employee_user.firstname} {employee_user.lastname} marked status as {task_status}",employee=task_manager.employee)
           email_mesaage=f"{employee_user.firstname} {employee_user.lastname} Updated Task {task_name} as {task_status} Please confirm"
           send_mail(
                f"New Task {task_name}",
                email_mesaage,
                "boostuae2001@gmail.com",
                [task_manager.employee.email,],
                fail_silently=False
            )

        return redirect('tasks')
    context ={
        "employee":employee,
        'selected_task':selected_task,
        "update":True,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    return render(request,'pages/update-task.html',context)

@login_required
def assign_tasks(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    all_employees = Employee.objects.all()
    


    manager = Manager.objects.get(employee__employee_id=employee.employee_id)


    if request.method == 'POST':
        selected_employee = get_object_or_404(Employee, pk=request.POST['employee'])
        print(selected_employee)
        if len(request.POST['task_name']) > 0:
           task_name = request.POST['task_name']
           task_desc = request.POST['description']
           task_status = request.POST['task_status']
           task_deadline = request.POST['deadline']
           employee_user = selected_employee
           print("email",employee_user.email)
           Task.objects.create(task_name=task_name,description=task_desc,status=task_status,deadline=task_deadline,employee=employee_user,manager=manager,department=employee.department,points=0,)
           Notification.objects.create(title=f"New Task {task_name}",message=task_desc,employee=employee_user)
           email_mesaage=f"New Task {task_name} is assigned you from {manager.employee.firstname} {manager.employee.lastname}\n {task_desc}\n  don't reply this email \n Thank you."
           send_mail(
                f"New Task {task_name}",
                email_mesaage,
                "boostuae2001@gmail.com",
                [employee_user.email,],
                fail_silently=False
            )
        return redirect('tasks')
    context ={
        "employee":employee,
        "all_employees":all_employees,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    return render(request,'pages/assign_tasks.html',context)

@login_required
def delete_task(request,id):
    Task.objects.filter(pk=id).delete()
    return redirect('tasks')

# def task_create_view(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task_name = request.POST['task_name']
#             task_desc = request.POST['description']
#             task_status = request.POST['task_status']
#             print("SUCCESS")
#             form.save()
#             return redirect('home')  # Define a success URL
#         else:
#             print(form.errors)  # Debugging: Print errors in the console
#     else:
#         form = TaskForm()
#     return render(request, 'pages/add_task.html', {'form': form})




@login_required
def operations(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    l_d_men=Employee.objects.filter(department__department_name="L&D")
    projects = Project.objects.all()
    repository =Repository.objects.all()
    asessmentBank=AsessmentBank.objects.all()
    simulation=Simulation.objects.all()

    context={
        "employee":employee,
        "l_d_men":l_d_men,
        "projects":projects,
        "repository":repository,
        "asessmentBank":asessmentBank,
        "simulation":simulation,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    
    return render(request,"pages/operations.html",context)

@login_required
def designers(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    l_d_men=Employee.objects.filter(department__department_name="L&D")
    projects = Project.objects.all()
    repository =Repository.objects.all()
    asessmentBank=AsessmentBank.objects.all()
    simulation=Simulation.objects.all()

    context={
        "employee":employee,
        "l_d_men":l_d_men,
        "projects":projects,
        "repository":repository,
        "asessmentBank":asessmentBank,
        "simulation":simulation,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    
    return render(request,"pages/designers.html",context)


@login_required
def designer_requests(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    requests=Design_Request.objects.all()

    context={
        "employee":employee,
        "requests":requests,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications

    }
    
    return render(request,"pages/design_requests.html",context)

@login_required
def portoflio(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    portfolio=Portfolio.objects.all()
    

    context={
        "employee":employee,
        "portfolio":portfolio,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications

    }
    
    return render(request,"pages/portfolio.html",context)
@login_required
def employees_list(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_employees=Employee.objects.all()
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')

    context={
        "employee":employee,
        "all_employees":all_employees,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications

    }
    
    return render(request,"pages/employees.html",context)
@login_required
def employees_detail(request,id):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    selected_employee=get_object_or_404(Employee, employee_id=id)
    employee_tasks=Task.objects.filter(employee=selected_employee.employee_id)
    employee_done=Task.objects.filter(employee=selected_employee.employee_id,status="Done")
    employee_stuck=Task.objects.filter(employee=selected_employee.employee_id,status="Stuck")
    employee_inprogress=Task.objects.filter(employee=selected_employee.employee_id,status="In Progress")
    employee_missed=Task.objects.filter(employee=selected_employee.employee_id,status="Missed")
    
    

    context={
        "employee":employee,
        "selected_employee":selected_employee,
        "employee_tasks":employee_tasks,
        "employee_done":employee_done,
        "employee_stuck":employee_stuck,
        "employee_inprogress":employee_inprogress,
        "employee_missed":employee_missed,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications


    }
    
    return render(request,"pages/employee_detail.html",context)




@login_required
def care(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    context={
        "employee":employee,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    
    return render(request,"pages/care.html",context)



@login_required
def AllTasks(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    tasks = Task.objects.all()
    stage=request.GET.get('stage')
    if stage == "done":
                tasks=Task.objects.filter(status="Done")
    elif stage == "stuck":
                tasks=Task.objects.filter(status="Stuck")
    elif stage == "inprogress":
                tasks=Task.objects.filter(status="In Progress")
    elif stage == "missed":
                tasks=Task.objects.filter(status="Missed")
    context={
        "employee":employee,
        "tasks":tasks,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    
    return render(request,"pages/all_tasks.html",context)

@login_required
def all_Notifications(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    tasks = Task.objects.all()
    context={
        "employee":employee,
        "tasks":tasks,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications
    }
    
    return render(request,"pages/all_notifications.html",context)

@login_required
def mark_notifications_read(request):
    if request.method == 'POST':
        employee = get_object_or_404(Employee, user=request.user)
        Notification.objects.filter(employee=employee, is_read=False).update(is_read=True)
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)



@login_required
def invoices(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    invoices=Invoice.objects.all()
    context={
        "employee":employee,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications,
        "invoices":invoices
    }
    
    return render(request,"pages/invoices.html",context)


@login_required
def contracts(request):
    employee = get_object_or_404(Employee, user=request.user)
    all_notifications=employee.notifications.all().order_by('-created_at')
    not_read_notifications=employee.notifications.filter(is_read=False).order_by('-created_at')
    contracts=Contract.objects.all()

    
    context={
        "employee":employee,
        "all_notifications":all_notifications,
        "not_read_notifications":not_read_notifications,
        "contracts":contracts

    }
    
    return render(request,"pages/contracts.html",context)
