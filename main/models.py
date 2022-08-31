"""
from django.db import models

# Create your models here.
class ToDoList(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text
"""
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # <--- added
    name = models.CharField(max_length=200)

    def __str__(self):
	return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
	return self.text
"""

from django.db import models

# Create your models here.
class ToDoList(models.Model):
	date = models.DateTimeField("date published")
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Item(models.Model):
	text = models.CharField(max_length=500)
	toDoList = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	complete = models.BooleanField()

	def __str__(self):
		return self.text