from django.db import models


class College(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    objects = models.manager


class Room(models.Model):
    College = models.OneToOneField(College, on_delete=models.CASCADE, primary_key=True,)
    Total_Rooms = models.CharField(max_length=50)
    Persons = models.CharField(max_length=50)
    objects = models.manager

class Student(models.Model):
    Room = models.ForeignKey(Room, on_delete=models.CASCADE)
    email_id = models.EmailField(max_length=50)
    roll_no = models.CharField(max_length=50)
    objects = models.manager





