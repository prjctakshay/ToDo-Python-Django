from django.urls import path
# from django.http import HttpResponse
# from first.first.views import home, test
from core.views import home, test, update, delete,save

# from django.shortcuts import render

# def home(request):
#     # return HttpResponse("Home")
#     return render(request,'home.html')
# from first.core.views import home, save, test, update, delete

urlpatterns = [
    # path('con/', admin.site.urls),
    path('', home, name='home'),
    path('save', save, name='save'),
    path('test', test),
    path('update/<int:todo_id>/', update, name='update'),
    path('delete/<int:todo_id>/', delete, name= 'delete'),
]