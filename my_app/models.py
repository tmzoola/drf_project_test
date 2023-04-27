from django.db import models

class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=19, decimal_places=1)

    def __str__(self):
        return  self.name
    
