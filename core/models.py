from django.db import models

# Create your models here.
#it is database part 

class Todo(models.Model):
    title = models.CharField(max_length=50, unique=True)
    title2 = models.CharField(max_length=50, unique=False, default="aaa")

    # class Meta: if we want to name the table or collection use it othervise django automatically name it
    #     db_table = "dreamreal"
