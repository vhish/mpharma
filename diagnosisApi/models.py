from django.db import models


# Create your models here.

class Category(models.Model):
    category_code = models.CharField(max_length=10 , primary_key=True)
    category_title =  models.TextField()
    created_at  =  models.DateTimeField(auto_now_add=True)
    updated_at  =  models.DateTimeField(auto_now=True)

    class Meta :
        def __str__(self):
            return "{} , {}".format(self.category_code, self.category_title)




class Diagnosis(models.Model):
    diagnosis_code  = models.CharField(max_length=7)
    code_type = models.CharField(max_length=7, default='icd-10')
    abbreviated_description  =  models.CharField(max_length=200)
    full_description  =  models.TextField()
    category =  models.ForeignKey(Category,  on_delete=models.CASCADE)
    created_at  =  models.DateTimeField(auto_now_add=True)
    updated_at  =  models.DateTimeField(auto_now=True)




    class Meta :

        def __str__(self):
            return "{} , {} , {} ".format(self.diagnosis_code ,  self.abbreviated_description , self.full_description )
