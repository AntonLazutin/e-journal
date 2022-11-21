from django.db import models

GRADE_CHOICES = (
    ('5', 'пять'),
    ('4', 'четыре'),
    ('3', 'три'),
    ('2', 'два'),
    ('1', 'один'),
)

class Teacher(models.Model):
   first_name = models.CharField(max_length=30)
   last_name = models.CharField(max_length=30)

   def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
        
class Subject(models.Model):
    name = models.CharField(max_length=30, unique=True)
    teacher = models.ForeignKey(Teacher, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    

class Group(models.Model):
    code = models.CharField(max_length=6, unique=True)

    def __str__(self) -> str:
        return self.code


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    group = models.ForeignKey(Group, related_name='students', on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Grade(models.Model):
    student = models.ForeignKey(Student, related_name='grades', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='grades', on_delete=models.CASCADE)
    digit = models.CharField(max_length=6, choices=GRADE_CHOICES)

    def __str__(self):
        return self.digit
    
