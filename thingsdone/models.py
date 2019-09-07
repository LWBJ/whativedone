from django.db import models
from datetime import date, timedelta
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Week(models.Model):
  start_day = models.DateField(default=timezone.now)
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null = True)
  
  class Meta:
    ordering = ['-start_day']
    unique_together =[['start_day','user']]
  
  def get_absolute_url(self):
    return reverse('weeks-detail', args=[str(self.id)])
  
  def __str__(self):
    return "%s's %s --- %s"%(self.user, self.start_day.strftime('%d %b %y'), (self.start_day + timedelta(days=6)).strftime('%d %b %y'))
  
class Month(models.Model):
  start_day = models.DateField(default=timezone.now)
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null = True)
  
  class Meta:
    ordering = ['-start_day']
    unique_together =[['start_day','user']]
  
  def get_absolute_url(self):
    return reverse('months-detail', args=[str(self.id)])
  
  def __str__(self):
    return "%s's "%(self.user) + str(self.start_day.strftime('%B %Y')) 

class Day (models.Model):
  day = models.DateField(default=timezone.now)
  month = models.ForeignKey(Month, on_delete=models.CASCADE, null=True)
  week = models.ForeignKey(Week, on_delete=models.CASCADE, null=True)
  
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null = True)
  
  class Meta:
    ordering = ['-day']
    unique_together =[['day','user']]
  
  def __str__(self):
    return self.day.strftime('%d-%m-%Y')
    
  def get_absolute_url(self):
    return reverse('days-detail', args=[str(self.id)])

class ThingDone(models.Model):
  DIFFICULTY = [
    ('Trivial', 'Trivial'),
    ('Normal', 'Normal'),
    ('Challenging', 'Challenging'),
    ('Tough', 'Tough'),
  ]
  name = models.CharField(max_length=200, help_text="What did you do?", default="Saikang")
  difficulty = models.CharField(max_length=200, choices=DIFFICULTY, default='Normal', help_text="How challenging was the task?")
  
  day = models.ForeignKey(Day, blank=True, on_delete=models.CASCADE, null=True)
  week = models.ForeignKey(Week, blank=True, on_delete=models.CASCADE, null=True)
  month = models.ForeignKey(Month, blank=True, on_delete=models.CASCADE, null=True)
  
  owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, null = True)
  
  class Meta:
    ordering = ['name']
    verbose_name_plural = 'Things done'
  
  def __str__(self):
    return self.name