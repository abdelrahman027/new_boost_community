from hashlib import blake2b
from pydoc import cli
from time import timezone
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from trainers.models import Trainer
from venues.models import Halls

# Create your models here.

# class ClientStatus(models.TextChoices):
#     regesitered="Registered"
#     rfp="request for proposal"
#     propsal="Proposal"
#     Media_Production="Media Production"
#     Digital_Marketing="Digital Marketing"


class Invoice_status(models.TextChoices):
    accepted="accepted"
    issued="issued"
    paid="paid"
    waiting_papers="waiting papers"

class Proposal_status(models.TextChoices):
    waiting="waiting"
    working="working"
    accepted="accepted"
    returned="returned"


class Task_Status(models.TextChoices):
    done="Done"
    stuck="Stuck"
    in_progress="In Progress"
    missed="Missed"

class Design_type(models.TextChoices):
    materials="Materials"
    persentation="Persentation"
    proposal="Proposal"
    ui="Ui"
    banner="banner"
    other="other"


class company_branch(models.TextChoices):
    dubai="Dubai"
    abu_dhabi="Abu Dhabi"
    egypt="Egypt"
    ksa="KSA"




class Course_type(models.TextChoices):
    public_course="Public"
    private_course="Private"

class Course_status(models.TextChoices):
    not_confirmed="not confirmed"
    confirmed="confirmed"
    running="running"
    finished="finished"
    canceled="canceled"
    merged="merged"


class Certificate_status(models.TextChoices):
    no_action="no action"
    name_ready="Names sheet recieved"
    ready_for_design="Ready for Design"
    ready_for_print="Ready to Print"
    ready_for_delivery="printed and Ready for Delivery"
    certificate_delivered="delivered"

class Material_status(models.TextChoices):
    not_recieved="not Receieved"
    received_material="Receieved"
    ready_for_design="Ready for Design"
    ready_for_print="Ready to Print"
    ready_for_delivery="printed and Ready for Delivery"
    delivered="Delivred"

class Course_category(models.TextChoices):
    online="online"
    physical="physical"


class Department(models.Model):
    department_id=models.AutoField(primary_key=True)
    department_name=models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.department_id}  {self.department_name}"
    
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)
    manager_role = models.BooleanField(default=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, default=None)
    employee_photo = models.ImageField(
        upload_to='employee_photos/', default='employee_photos/sara.jpg', null=True, blank=True)
    location = models.CharField(max_length=50, null=True)
    comilative_points=models.CharField(max_length=20,null=True)
    points=models.CharField(max_length=20,default="0")


    def __str__(self):
        return f"{self.employee_id} {self.firstname} {self.lastname}"
    




class Client(models.Model):
    client_id=models.AutoField(primary_key=True)
    client_name=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    contact_person=models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50 ,default="example@email.com")
    status=models.BooleanField(default=False)
    sales_person = models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,related_name="clients")
    client_logo= models.ImageField(upload_to='clients/', default='clients/default.png', null=True, blank=True)
    registred_date =models.DateField(default=date.today)

    def __str__(self):
        return self.client_name




# class Hotel_of_course(models.Model):
#     hotel_id=models.AutoField(primary_key=True)
#     hotel_name=models.CharField(max_length=255)
#     hotel_location=models.CharField(max_length=255)
#     course_name=models.CharField(max_length=255)
#     review=models.CharField(max_length=255,default="0")
#     contact_person=models.CharField(max_length=255,null=True,blank=True)
#     email=models.EmailField(max_length=255,null=True,blank=True)
#     phone=models.CharField(max_length=255,null=True,blank=True)
#     comments=models.TextField(null=True,blank=True)
    
#     def __str__(self):
#         return self.hotel_name
    

class Facilitator(models.Model):
    facilitator_id=models.AutoField(primary_key=True)
    employee=models.OneToOneField(Employee,on_delete=models.CASCADE,null=True,blank=True)
    # course=models.ForeignKey(Course,on_delete=)

    def __str__(self):
        return self.employee.firstname



    



class Design_Request(models.Model):
    design_request_id=models.AutoField(primary_key=True)
    design_type=models.CharField(max_length=255,choices=Design_type.choices)
    requested_from=models.ForeignKey(Employee,on_delete=models.CASCADE)
    design_file= models.FileField(null=True,blank=True,upload_to='pdf')
    comments=models.TextField(null=True,blank=True)

    def __str__(self):
        return f"{self.design_type} from :{self.requested_from} id: {self.design_request_id}"




    
class AsessmentBank(models.Model):
    asessement_id=models.AutoField(primary_key=True)
    asessment_name=models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)
    assessment_file= models.FileField(null=True,blank=True,upload_to='pdf')
    
    def __str__(self):
        return self.asessment_name



class Compitency(models.Model):
    compitency_id=models.AutoField(primary_key=True)
    compitency_name=models.CharField(max_length=255)
    compitency_description=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.compitency_name

class Simulation(models.Model):
    simulation_id=models.AutoField(primary_key=True)
    Simulation_name=models.CharField(max_length=255)
    compitency=models.ManyToManyField(Compitency)
    simulation_photo= models.ImageField(upload_to='employee_photos/', default='employee_photos/default-employee.webp', null=True, blank=True)
    learning_guide= models.FileField(null=True,blank=True,upload_to='pdf')


    def __str__(self):
        return self.Simulation_name
    


class Inventory(models.Model):
    inventory_id=models.AutoField(primary_key=True)
    inventory_name=models.CharField(max_length=100,default="item")
    descripttion=models.TextField(null=True,blank=True)
    quantity=models.CharField(max_length=100)
    branch=models.CharField(max_length=100,choices=company_branch.choices)

    def __str__(self):
        return self.inventory_name

class Logestics(models.Model):
    logestic_id=models.AutoField(primary_key=True)
    driver_name=models.CharField(max_length=255)
    driver_phone=models.CharField(max_length=255)
    city=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.driver_name}  city:{self.city}"

class Manager(models.Model):
    manger_id=models.AutoField(primary_key=True)
    deparment= models.ForeignKey(Department,on_delete=models.CASCADE)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.manger_id} {self.employee.firstname}"

class Task(models.Model):
    task_id=models.AutoField(primary_key=True)
    task_name=models.CharField(max_length=500)
    description=models.TextField()
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    manager=models.ForeignKey(Manager,on_delete=models.SET_NULL,null=True)
    created_at= models.DateField(auto_now_add=True)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,choices=Task_Status.choices)
    deadline=models.DateField()
    points=models.CharField(max_length=20,default="0")

    def __str__(self):
        return self.task_name

    


class Badge(models.Model):
    badge_id=models.AutoField(primary_key=True)
    issue_date=models.DateField()
    badge_name=models.CharField(max_length=255)
    description=models.CharField(max_length=500,null=True,blank=True)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    badge_img= models.ImageField(upload_to='employee_photos/', default='employee_photos/default-employee.webp', null=True, blank=True)


class Idea(models.Model):
    idea_id=models.AutoField(primary_key=True)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    description=models.TextField(null=True,blank=True)
    points=models.CharField(max_length=20,null=True,blank=True)



class Project(models.Model):
    project_id=models.AutoField(primary_key=True)
    project_name=models.CharField(max_length=255)
    feedback= models.FileField(null=True,blank=True,upload_to='pdf')
    invoice= models.FileField(null=True,blank=True,upload_to='pdf')
    dead_line=models.DateField()
    starting_Date=models.DateField(auto_now_add=True)
    client=models.ForeignKey(Client,on_delete=models.SET_NULL,null=True)
    invoice_document= models.FileField(null=True,blank=True,upload_to='pdf')
    invoice_number=models.CharField(max_length=255,null=True,blank=True)
    invoice_status=models.CharField(max_length=20,choices=Invoice_status.choices ,default=Invoice_status.accepted)
    rfp_name=models.CharField(max_length=255,null=True,blank=True,default=project_name)
    proposal_name=models.CharField(max_length=255,null=True,blank=True,default=project_name)
    proposal_dead_line=models.DateField(default=date.today(),null=True,blank=True)
    proposal_document = models.FileField(null=True,blank=True,upload_to='pdf')
    proposal_status = models.CharField(max_length=20,choices=Proposal_status.choices,default=Proposal_status.waiting)
    # project=models.ForeignKey(Project,on_delete=models.CASCADE)
    rfp_document = models.FileField(null=True,blank=True,upload_to='pdf')

    def __str__(self):
        return self.project_name

class Portfolio(models.Model):
    portfolio_id=models.AutoField(primary_key=True)
    template_name=models.CharField(max_length=255)
    description_of_template=models.TextField(null=True,blank=True)
    Template_file= models.FileField(null=True,blank=True,upload_to='pdf')
    project=models.ForeignKey(Project,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return f"{self.template_name} id :{self.portfolio_id}"


    
    
class Repository(models.Model):
    repository_id=models.AutoField(primary_key=True)
    document_name=models.CharField(max_length=255)
    project=models.ForeignKey(Project,on_delete=models.CASCADE)
    repo_file= models.FileField(null=True,blank=True,upload_to='pdf')

    def __str__(self):
        return f"{self.document_name} id :{self.project}"
class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=255,default="New Course")
    field=models.CharField(max_length=255,null=True)
    location=models.CharField(max_length=255,null=True)
    course_type = models.CharField(max_length=40,choices=Course_type.choices,null=True)
    course_confirmation= models.BooleanField(default=False)
    course_Date=models.DateField(default=date.today,null=True)
    course_duration = models.CharField(max_length=2,default="1")
    course_category = models.CharField(max_length=40,choices=Course_category.choices,null=True)
    feedback= models.FileField(null=True,blank=True,upload_to='pdf')
    # certificate = models.ForeignKey(Certificate,on_delete=models.CASCADE,null=True,blank=True)
    gift_items_description=models.TextField(null=True,blank=True)
    pre_post_files= models.FileField(null=True,blank=True,upload_to='pdf')
    place_of_course = models.ForeignKey(Halls,on_delete=models.SET_NULL,null=True,blank=True)
    facilitator=models.ForeignKey(Facilitator,on_delete=models.SET_NULL,null=True)
    Sales_man=models.ForeignKey(Employee,on_delete=models.SET_NULL,null=True,related_name="courses")
    trainer=models.ForeignKey(Trainer,on_delete=models.SET_NULL,null=True,blank=True,related_name="courses")
    project=models.ForeignKey(Project,on_delete=models.CASCADE,null=True,blank=True)
    contract = models.FileField(null=True,blank=True,upload_to='pdf')
    invoice= models.FileField(null=True,blank=True,upload_to='pdf')
    trainer_visa_valid=models.BooleanField(default=False,null=True,blank=True)
    number_of_attendees=models.CharField(max_length=2,default="1",null=True,blank=True)
    number_of_gift=models.CharField(max_length=2,default="1",null=True,blank=True)
    status=models.CharField(max_length=50,choices=Course_status.choices,default=Course_status.not_confirmed)
    certificate_status=models.CharField(max_length=40,choices=Certificate_status.choices,null=True,blank=True,default=Certificate_status.no_action)
    certificates_file= models.FileField(null=True,blank=True,upload_to='pdf')
    material_status=models.CharField(max_length=40,choices=Material_status.choices,null=True,blank=True,default=Material_status.not_recieved)
    material_file= models.FileField(null=True,blank=True,upload_to='pdf')
    attendance_file= models.FileField(null=True,blank=True,upload_to='pdf')


    

    def __str__(self):
        return self.course_name
    



class Notification(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.title} - {self.employee.firstname} {self.employee.lastname}"





class Comments(models.Model):
    comment_id=models.AutoField(primary_key=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE,related_name="comments")
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE)
    comment=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"{self.employee} comment: {self.comment}"



class Contract(models.Model):
    contract_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=128,blank=True,null=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE,blank=True,null=True)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    client=models.ForeignKey(Client,on_delete=models.CASCADE,blank=True,null=True)
    contract=models.FileField(null=True,blank=True,upload_to='pdf')
    comments=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # add contract 
    def __str__(self):
        return f"trainer: {self.trainer} client: {self.client} contract: {self.contract}"

class Invoice(models.Model):
    invoice_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=128,blank=True,null=True)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE,blank=True,null=True)
    employee=models.ForeignKey(Employee,on_delete=models.CASCADE,blank=True,null=True)
    client=models.ForeignKey(Client,on_delete=models.CASCADE,blank=True,null=True)
    invoice=models.FileField(null=True,blank=True,upload_to='pdf')
    comments=models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    def __str__(self):
        return f"trainer: {self.trainer} client: {self.client} invoice: {self.invoice}"