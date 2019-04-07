from django.db import models
from  multiselectfield import MultiSelectField

class ContactData(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.BigIntegerField()

    COURSE_CHOICES=(
        ('python','Python'),
        ('django','Django'),
        ('ui','UI'),
        ('rest api','REST API')
    )
    courses=MultiSelectField(max_length=200,choices=COURSE_CHOICES)

    LOCATION_CHOICES=(
        ('hyderabad','Hyderabad'),
        ('bangelure','Bangelure'),
        ('chennai','Chennai')
    )
    location=MultiSelectField(max_length=200,choices=LOCATION_CHOICES)

    SHIFT_CHOICES=(
        ('morning','Morning'),
        ('afternoon','Afternoon'),
        ('evening','Evening'),
        ('night','Night')

    )
    shift=MultiSelectField(max_length=200 ,choices=SHIFT_CHOICES)

class FeedbackData(models.Model):
    name=models.CharField(max_length=50)
    rating=models.IntegerField()
    date=models.DateField()
    feedback=models.TextField(max_length=500)

