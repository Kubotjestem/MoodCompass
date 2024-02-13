from django.shortcuts import render
# Create your views here.


dairies = [
    {'id':1, 'name':'My thougts'},
     {'id':2, 'name':'New ideas'},
]


def home(request):
    return render(request, 'home.html')



def dairy(request):
    return render(request, 'dairy.html')



def signin(request):
    return render(request, 'signin.html')


