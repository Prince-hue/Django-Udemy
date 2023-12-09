loading an image
-------------------------------------
{% load static %}
<img src="{% static 'django.png' %}" alt="django">

getting data from forms using the GET method
-----------------------------------------------
#create one html form but two different paths
#one path uses render
#the other uses JsonResponse

getting data from forms using the POST method
-----------------------------------------------
#follows the same method as the GET with only two exceptions
<form method='POST' ...>
{% csrf_token %}
#view.py
'Email' : request.POST['email']


Building a form in Django
-----------------------------------------------
#visit django website
https://docs.djangoproject.com/en/4.2/topics/forms/
forms.py  #create in apps
"""
from django import forms

class Feedback(forms.Form):
    title = forms.CharField(label="Title", max_length=50, widget = forms.TextInput)
"""
#the initial form was html, this is python
path('djangoforms/', views.django_forms) #in url
from .forms import * #in views.py
def django_forms(request): #create function
#create a html page
insert ' {{form.as_p}} ' into the form tag
#boostrap codes can be added to the attribute of the TextInput
TextInput(attrs = {'class': 'form-control'})
#class: form-control is a class in Bootstrap that can be used to style textual form controls like <input> and <textarea> elements. 
#add the POST method to the form and also add {% csrf_token %}
#modify django_forms(request) with the POST method
from django.http import JsonResponse, HttpResponse #in view.py
""""
def django_forms(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            print(title)
            print(subject)
            var = str('Form Submitted '+ str(request.method))
            return HttpResponse(var)
        else:
            dic = {
                'form' : form,
            }
            return render(request, 'djangoforms.html', context=dic)
        
    elif request.method == 'GET':
        form = FeedbackForm() 
        dict = {
            'form': form,
        }
        return render(request, 'djangoforms.html', context=dict)
""""

Adding Alerts to forms
---------------------------------------------------
https://getbootstrap.com/docs/4.0/components/alerts/

Standard 404 error page
----------------------------------------------------
#in settings.py, change DEBUG = False
#in settings.py, change ALLOWED_HOSTS = ['*']
https://getbootstrap.com/docs/4.0/components/jumbotron/
#create a 404.html file in templates
#let the href in the a tag be
href = "{% url 'index' %}"
#to render it, we move into urls.py of project
handler404 = 'app.views.error_404_view'
#in views.py
'''
def error_404_view(request, exception):
    return render(request, '404.html')

'''

