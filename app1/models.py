from django.db import models
class foods(models.Model):
    name=models.CharField(max_length=100,default='')
    iamge=models.ImageField(upload_to='media/',default='')
    def __str__(self):
        return self.name
    
class foodcategory_items(models.Model):
    foodcategory_name=models.CharField(max_length=100)
    foodcategory_image=models.ImageField(upload_to='media/')
    foodcategory_price=models.IntegerField(max_length=100)
    foodcategory_description=models.TextField(max_length=700,default='')
    foodcategory_items=models.ForeignKey(foods,on_delete=models.CASCADE)
    def __str__(self):
        return self.foodcategory_name

class chefs(models.Model):
    chefs_image=models.ImageField(upload_to='media/')
    chefs_name=models.CharField(max_length=100)
    chefs_post=models.CharField(max_length=100)
    chefs_socialmedia=models.URLField()

    def __str__(self):
        return self.chefs_name
    
class Weeklyoffer(models.Model):
    name=models.ForeignKey(foodcategory_items,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.description
    
class Dailyoffer(models.Model):
    name=models.ForeignKey(foodcategory_items,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.description
                      

    
    
# Create your models here.
