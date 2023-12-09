from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import *

# Create your views here.
def html_index(request):
    return render(request, 'index.html')
def html_date(request):
    return render(request, 'dates.html')

#using variables
def html_person(request):
    var =    'NSP'
    msg = 'Thank you for your service to the nation.'
    tasks = ['Registration', 'Appointment', 'Report']
    num1, num2 = 12, 5
    ans = num1 > num2
    print(ans)
    dic = {
        'var' : var,
        'msg' : msg,
        'tasks' : tasks,
        'num1' : num1,
        'num2' : num2,
        'ans' : ans,
    }
    return render(request, 'persons.html', context = dic)

#adding images from the static folder
def html_image(request):
    return render(request, 'image.html')
def html_image2(request, imgvar):
    imgvar = str(imgvar);
    imgvar = imgvar.lower()
    print(imgvar)
    if imgvar == 'residence':
        var = False
    elif imgvar == 'django':
        var = True
    dic = {
        'var' : var,
    }
    return render(request, 'image2.html', context = dic)

#adding forms and backends
def html_forms(request):
    return render(request, 'form.html')
def html_forms_get(request):
    dic = {
        'Email' : request.POST['email'],
        'password' : request.POST['password'],
        'checkbox' : request.POST['check'],
        'Grid Radios' : request.POST['gridRadios'],
        'method' : request.method,
    }
    return JsonResponse(dic)

#adding django forms
def django_forms(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            dic = {
                'form' : FeedbackForm(),
            }
            error = False
            errorbox = []
            if title != title.upper():
                error = True
                errormsg = 'Title must in CAPITALIZED'
                errorbox.append(errormsg)
                
            import re
            regex = '^\w+([\.-]?\w+)*@\w([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex,email):
                error = True
                errormsg = 'Incorrect Email'
                errorbox.append(errormsg)            
                            
            if error != True:
                dic['success'] = True
                dic['successmsg'] = 'Form Submitted'
                
            dic['error'] = error
            dic['errorbox'] = errorbox
            
            return render(request, 'djangoforms.html', context=dic)
        
    elif request.method == 'GET':
        form = FeedbackForm() 
        dict = {
            'form': form,
        }
        return render(request, 'djangoforms.html', context=dict)