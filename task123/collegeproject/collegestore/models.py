from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Material(models.Model):
    debit_notebook=models.BooleanField(default=False)
    pen=models.BooleanField(default=False)
    exam_papers=models.BooleanField(default=False)


    def __str__(self):
        return self.name




class Purpose(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Realform(models.Model):
    name=models.CharField(max_length=30)
    Dob=models.DateField(max_length=40)
    AGE=models.IntegerField()
    GENDER=models.CharField(max_length=13)
    PHONE_NUMBER=models.CharField(max_length=12)
    EMAIL=models.EmailField()
    ADDRESS=models.TextField(max_length=200)
    department=models.ForeignKey(Department, on_delete=models.SET_NULL,blank=True,null=True)
    course=models.ForeignKey(Course, on_delete=models.SET_NULL,blank=True,null=True)
    purpose=models.ForeignKey(Purpose, on_delete=models.CASCADE)
    debit_notebook = models.BooleanField(default=False)
    pen = models.BooleanField(default=False)
    exam_papers = models.BooleanField(default=False)

    def __str__(self):
        return self.name
