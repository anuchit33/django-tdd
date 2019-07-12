from django.shortcuts import render
from django.contrib.auth.models import User
from myapp.forms.AddUserForm import AddUserForm

# Create your views here.
def IndexPage(request):
    form = None
    form = AddUserForm()

    # if request.method =='POST':
    # #     form = AddUserForm(request.POST)

    context = {
       'user_list':User.objects.all(),
       'form': form
    }

    return render(request, "myapp/index.html", context)



        # if request.method =='POST':
    #     form = AddUserForm(request.POST)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = AddUserForm()