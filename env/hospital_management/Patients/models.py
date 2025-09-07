from django.db import models


class Patient(models.Model):
    GENDER_CHOICE =[
        ('Male','Male'),
        ('Female','Female'),
        ('other','other')
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICE)
    contact= models.CharField(max_length=100)
    address=models.CharField(blank=True,null=True)

    def __str__(self):
        return self.name
    
