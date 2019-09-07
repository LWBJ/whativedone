from django import forms
from django.utils import timezone
from django.forms import ModelForm, inlineformset_factory, modelformset_factory
from thingsdone.models import Day, ThingDone, Month, Week
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import date, timedelta


class DayForm(forms.Form):
  day = forms.DateField(required=True, initial=timezone.now)
  #user value is set using the view
  user = ''
  
  DIFFICULTY = [
    ('', ''),
    ('Trivial', 'Trivial'),
    ('Normal', 'Normal'),
    ('Challenging', 'Challenging'),
    ('Tough', 'Tough'),
  ]
  
  saikang1 = forms.CharField(required=False)
  difficulty1 = forms.ChoiceField(choices=DIFFICULTY, required=False)
  saikang2 = forms.CharField(required=False)
  difficulty2 = forms.ChoiceField(choices=DIFFICULTY, required=False)
  saikang3 = forms.CharField(required=False)
  difficulty3 = forms.ChoiceField(choices=DIFFICULTY, required=False)
  
  def clean(self):
        data = super().clean()
        
        if (data['saikang1'] and not(data['difficulty1'])) or (not(data['saikang1']) and data['difficulty1']):
            raise ValidationError(_('Make sure each item has a name and difficulty!'))
        
        if (data['saikang2'] and not(data['difficulty2'])) or (not(data['saikang2']) and data['difficulty2']):
            raise ValidationError(_('Make sure each item has a name and difficulty!'))
        
        if (data['saikang3'] and not(data['difficulty3'])) or (not(data['saikang3']) and data['difficulty3']):
            raise ValidationError(_('Make sure each item has a name and difficulty!'))
        
        return data
        
  def clean_day(self):
    data = self.cleaned_data['day']
    if Day.objects.filter(user=self.user).filter(day=data):
      raise ValidationError(_('Day already exists!'))
    return data   
   
class ThingDoneForm(ModelForm):
  class Meta:
    model = ThingDone
    fields = ['name', 'difficulty']

def createThingDoneFormSet(model):
  return inlineformset_factory(model, ThingDone, fields=('name', 'difficulty'), extra=0)

class MonthForm(forms.Form):
  MONTHS = [
    (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), 
    (7, 'July'), (8, 'August'), (9, 'September'),(10, 'October'),(11, 'November'),(12, 'December'),
  ]

  year = forms.IntegerField(min_value=0, max_value=9999)
  month = forms.ChoiceField(choices=MONTHS)
  #user value is set using the view
  user = ''
  
  DIFFICULTY = [
    ('', ''),
    ('Trivial', 'Trivial'),
    ('Normal', 'Normal'),
    ('Challenging', 'Challenging'),
    ('Tough', 'Tough'),
  ]
  
  saikang1 = forms.CharField(required=False)
  difficulty1 = forms.ChoiceField(choices=DIFFICULTY, required=False)
  saikang2 = forms.CharField(required=False)
  difficulty2 = forms.ChoiceField(choices=DIFFICULTY, required=False)
  saikang3 = forms.CharField(required=False)
  difficulty3 = forms.ChoiceField(choices=DIFFICULTY, required=False)

  def clean(self):
    data = super().clean()
        
    if (data['saikang1'] and not(data['difficulty1'])) or (not(data['saikang1']) and data['difficulty1']):
      raise ValidationError(_('Make sure each item has a name and difficulty!'))
        
    if (data['saikang2'] and not(data['difficulty2'])) or (not(data['saikang2']) and data['difficulty2']):
      raise ValidationError(_('Make sure each item has a name and difficulty!'))
        
    if (data['saikang3'] and not(data['difficulty3'])) or (not(data['saikang3']) and data['difficulty3']):
      raise ValidationError(_('Make sure each item has a name and difficulty!'))
        
    start_day = date(year=data['year'], month=int(data['month']), day=1)
    if Month.objects.filter(user=self.user).filter(start_day=start_day):
      raise ValidationError(_('Month already exists!'))
        
    return data

def get_prev_weekday_start(today):
  c1 = 0
  while c1 < 7:
    test_date = (today - timedelta(days=c1))
    if test_date.weekday() == 6:
      return test_date
    c1 +=1

class WeekForm(forms.Form):
  initial = get_prev_weekday_start(timezone.now())
  start_day = forms.DateField(initial=initial)

  #user value is set using the view
  user = ''
  
  DIFFICULTY = [
    ('', ''),
    ('Trivial', 'Trivial'),
    ('Normal', 'Normal'),
    ('Challenging', 'Challenging'),
    ('Tough', 'Tough'),
  ]
  
  saikang1 = forms.CharField(required=False)
  difficulty1 = forms.ChoiceField(choices=DIFFICULTY, required=False)
  saikang2 = forms.CharField(required=False)
  difficulty2 = forms.ChoiceField(choices=DIFFICULTY, required=False)
  saikang3 = forms.CharField(required=False)
  difficulty3 = forms.ChoiceField(choices=DIFFICULTY, required=False)
  
  def clean(self):
    data = super().clean()
        
    if (data['saikang1'] and not(data['difficulty1'])) or (not(data['saikang1']) and data['difficulty1']):
      raise ValidationError(_('Make sure each item has a name and difficulty!'))
        
    if (data['saikang2'] and not(data['difficulty2'])) or (not(data['saikang2']) and data['difficulty2']):
      raise ValidationError(_('Make sure each item has a name and difficulty!'))
        
    if (data['saikang3'] and not(data['difficulty3'])) or (not(data['saikang3']) and data['difficulty3']):
      raise ValidationError(_('Make sure each item has a name and difficulty!'))
        
    return data
    
  def clean_start_day(self):
    data = self.cleaned_data['start_day']

    if not(data.weekday()==6):
      raise ValidationError(_('Choose a date that falls on a Sunday!'))    
    
    if Week.objects.filter(user=self.user).filter(start_day=data):
      raise ValidationError(_('That week already exists!'))
    
    return data
    
