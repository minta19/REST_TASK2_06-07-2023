from django.db import models

class Student(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    age=models.IntegerField()
    grade=models.CharField(max_length=10)
    place=models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.first_name
    
