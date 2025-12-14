from django.db import models

class Employee(models.Model):

    
    class DepartmentChoices(models.TextChoices): #ENUM
        HR = "HR", "Human Resources"
        IT = "IT", "Information Technology"
        SALES = "SALES", "Sales"
        FINANCE = "FIN", "Finance"
        MARKETING = "MKT", "Marketing"
    

    class PositionChoices(models.TextChoices):
        INTERN = "INTERN", "Intern"
        JUNIOR = "JR", "Junior Developer"
        SENIOR = "SR", "Senior Developer"
        MANAGER = "MGR", "Manager"
        DIRECTOR = "DIR", "Director"

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    
    department = models.CharField(
        max_length=20,
        choices=DepartmentChoices.choices)
    
    position = models.CharField(
        max_length=20,
        choices=PositionChoices.choices)
    
    joining_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
class AwardCategory(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
class Award(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE , related_name= 'awards')       #we used forign key here because 
    category = models.ForeignKey(AwardCategory, on_delete=models.CASCADE , related_name= 'awards')
    date_given = models.DateField(auto_now_add=True)     #will automatically set the of date time when award was created in db.

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.category.title}"
