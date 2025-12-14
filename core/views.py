from django.shortcuts import render,redirect
from .models import Employee, Award, AwardCategory
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def add_employee(request):
    if request.method == "POST":
        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        email = request.POST.get("email")
        department = request.POST.get("department")
        position = request.POST.get("position")
        joining_date = request.POST.get("joining_date")

        if not (first and last and email and department and position and joining_date):
            messages.error(request, "Please fill all fields.")
            return redirect("add_employee")

        Employee.objects.create(
            first_name=first,
            last_name=last,
            email=email,
            department=department,
            position=position,
            joining_date=joining_date
        )

        messages.success(request, "Employee added successfully!")
        return redirect("employees")

    return render(request, "core/add_employee.html")

def employees_list(request):
    employees = Employee.objects.all()
    return render(request, 'core/employees.html', {'employees': employees})


def awards_list(request):
    awards = Award.objects.all()
    return render(request, 'core/awards.html', {'awards': awards})

def give_award(request):
    employees = Employee.objects.all()
    categories = AwardCategory.objects.all()

    if request.method  == "POST":
        employee_id = request.POST.get("employee")
        category_id = request.POST.get("category")

        if not employee_id or not category_id:
            messages.error(request, "Please select both Employee and Award Category.")
        else:
            employee = Employee.objects.get(id=employee_id)
            category = AwardCategory.objects.get(id=category_id)

            Award.objects.create(employee=employee, category=category)
            messages.success(request, f"Award given to {employee.first_name} successfully!")

            return redirect('awards')   #after giving award we redirect to awards page to see the list of awards.
    
    return render(request, "core/give_award.html", {
        "employees": employees,
        "categories": categories
    })










    

