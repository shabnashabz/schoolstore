
from django.shortcuts import render, redirect
from storeapp.models import Department, Course, User, Order
from storeapp.forms import RegisterForm

def home(request):
    # return HttpResponse("hello world")
    newvrbl=Department.objects.all()
    newvrbls=Course.objects.all()
    return render(request,"home.html",{'result':newvrbl,'results':newvrbls})


def login_view(request):
    if request.method == 'POST':
        # Handle login logic here
        return redirect('new_page')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Handle registration logic here
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def new_page(request):
    if request.method == 'POST':
        # Handle form submission logic here
            return render(request, 'new_page.html', {'message': 'Order Confirmed'})
    return render(request, 'new_page.html')

def hom(request):
    return render(request, 'home.html')
def submit_order(request):
    # if request.method == 'POST':
        p=Order()
        p.user_id = request.POST.get('user_id')
        p.name = request.POST.get('name')
        p.dob = request.POST.get('dob')
        p.age = request.POST.get('age')
        p.gender = request.POST.get('gender')
        p.phn = request.POST.get('phone')
        p.email = request.POST.get('email')
        p.add = request.POST.get('address')
        p.depart = request.POST.get('department')
        p.course = request.POST.get('course')
        p.purpose = request.POST.get('purpose')
        p.material= ', '.join(request.POST.getlist('materials'))
        p.save()
    
        return render(request, 'new_page.html')
        # Redirect to a success page or display a success message
        # return redirect('success')
      

    # Render the form template if the request is GET
    # return render(request, 'new_page.html')
def view_order(request):
    p=Order.objects.all()
    return render(request,'view_order.html',{'data':p})
def del_order(request,id):
    p=Order.objects.get(id=id)
    p.delete()
    return redirect("/view_order/")