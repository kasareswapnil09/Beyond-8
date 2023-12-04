from django.db import models

class Nurse(models.Model):
    name = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=20, choices=[('Novice', 'Novice'), ('Competent', 'Competent'), ('Expert', 'Expert')])

class Shift(models.Model):
    name = models.CharField(max_length=20, unique=True)

class Schedule(models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    day = models.DateField()
