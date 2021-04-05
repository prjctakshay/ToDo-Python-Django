# it is logic part
# Create your views here.

from django.shortcuts import render, redirect

from core.forms import TodoForm
from core.models import Todo


def home(request):
    print("***********at home")
    
    form = TodoForm
    todos = Todo.objects.all() #to get all objects or data in db

    # if request.method == 'POST': #if any forms submited or POST is clicked
    #     form = TodoForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
    print("feilds =",form.Meta.fields)

    return render(request, 'home.html', {'form': form, 'todos': todos})

def save(request):
    # form = TodoForm 
    # print("111111111111form",form)
    if request.method == 'POST': #if any forms submited or POST is clicked
        form = TodoForm(request.POST) #gets that form if duplicate entry post with 
                                    #error are passing
        if form.is_valid(): #means no duplicate 
            form.save()
            return redirect('home')
    # return redirect('home')
    todos = Todo.objects.all() #to get all objects or data in db
    return render(request, 'home.html',{'form': form,'todos': todos  })
    


def update(request, todo_id):
    todo=Todo.objects.get(id=todo_id)
    # print('to do: ', todo)
    form = TodoForm(instance=todo)
    # print('to form: ', form)

    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        # TodoForm(request.POST, instance=todo) koduthillal updatene pakaram new instance save aavaum
        # print(f"\n in update TodoForm(request.POST)={TodoForm(request.POST)} \n ************* TodoForm(request.POST, instance=todo)={TodoForm(request.POST, instance=todo)}")
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'update.html', {'form': form})


def delete(request, todo_id):
    if request.method == 'POST':
        Todo.objects.get(id=todo_id).delete()
    return redirect('home')


def test(request):
    # return HttpResponse("Home")
    return render(request, '../core/templates/applications.html')

#
# from myapp.models import Dreamreal
# from django.http import HttpResponse
#
#
# def crudops(request):
#     # Creating an entry
#
#     dreamreal = Dreamreal(
#         website="www.polo.com", mail="sorex@polo.com",
#         name="sorex", phonenumber="002376970"
#     )
#
#     dreamreal.save()
#
#     # Read ALL entries
#     objects = Dreamreal.objects.all()
#     res = 'Printing all Dreamreal entries in the DB : <br>'
#
#     for elt in objects:
#         res += elt.name + "<br>"
#
#     # Read a specific entry:
#     sorex = Dreamreal.objects.get(name="sorex")
#     res += 'Printing One entry <br>'
#     res += sorex.name
#
#     # Delete an entry
#     res += '<br> Deleting an entry <br>'
#     sorex.delete()
#
#     # Update
#     dreamreal = Dreamreal(
#         website="www.polo.com", mail="sorex@polo.com",
#         name="sorex", phonenumber="002376970"
#     )
#
#     dreamreal.save()
#     res += 'Updating entry<br>'
#
#     dreamreal = Dreamreal.objects.get(name='sorex')
#     dreamreal.name = 'thierry'
#     dreamreal.save()
#
#     return HttpResponse(res)
