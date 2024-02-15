from django.db import models

# Create your models here.
class EmploymentData(models.Model):
    Series_reference=models.CharField(max_length=100)
    Period=models.FloatField()
    Data_value=models.CharField(max_length=100)
    Suppressed=models.CharField(max_length=50)
    Status=models.CharField(max_length=50)
    Units=models.CharField(max_length=100)
    Magnitude=models.CharField(max_length=100)
    Subject=models.CharField(max_length=100)
    Group=models.CharField(max_length=100)
    Series_title_1=models.CharField(max_length=100)
    Series_title_2=models.CharField(max_length=100)
    Series_title_3=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Series_reference