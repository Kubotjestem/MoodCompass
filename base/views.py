from django.shortcuts import render
# Create your views here.


dairies = [
    {'id':1, 'name':'My thougts'},
     {'id':2, 'name':'New ideas'},
]


def home(request):
    return render(request, 'base/home.html')



def dairy(request):
    context = {'dairies': dairies}
    return render(request, 'base/dairy.html', context)



def signin(request):
    return render(request, 'signin.html')



