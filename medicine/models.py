from unicodedata import category
from django.db import models

# Create your models here.
class MedicineType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name.upper()

class Medicine(models.Model):
    name = models.CharField(max_length=150)
    salt = models.TextField()
    category = models.ForeignKey(MedicineType,on_delete=models.CASCADE)
    mrp = models.IntegerField()
    pack = models.CharField(max_length=150)
    image = models.ImageField(default=None,upload_to='static/medicine')  
    date = models.DateField()

    def __str__(self):
        return self.name.upper()
    
    @staticmethod
    def allMedicines():
        return Medicine.objects.all()

    @staticmethod
    def getMedicines(medicine_id):
        if medicine_id:
            return Medicine.objects.filter(category=medicine_id)
        else:
            return Medicine.allMedicines()
        

    
