from django.shortcuts import render
from django.contrib.auth.models import User
from myapp.forms.AddUserForm import AddUserForm

# Create your views here.
def IndexPage(request):
    status = 200
    form = AddUserForm()

    # if request.method =='POST':
    # #     form = AddUserForm(request.POST)
    if request.method =='POST':
        form = AddUserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            status = 201
        else:
            status = 400
    else:
        form = AddUserForm()
    context = {
       'user_list':User.objects.all(),
       'form': form
    }

    return render(request, "myapp/index.html", context,status=status)



        # if request.method =='POST':
    #     form = AddUserForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = AddUserForm()