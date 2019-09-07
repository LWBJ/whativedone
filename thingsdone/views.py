from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import DeleteView
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from datetime import timedelta, date, datetime

from thingsdone.models import Day, Month, Week, ThingDone
from thingsdone.forms import DayForm, ThingDoneForm,  createThingDoneFormSet, MonthForm, WeekForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def mainView(request):
  return render(request, 'base_generic.html')
  
class DayList(LoginRequiredMixin, generic.ListView):
  model = Day
  
  def get_queryset(self):
    return Day.objects.filter(user=self.request.user)
  
@login_required
def DayDetail(request, pk):
  day = Day.objects.filter(user=request.user).get(pk=pk)
  
  if request.method == "POST":
    form = ThingDoneForm(request.POST)
    if form.is_valid():
      fs = form.save(commit=False)
      fs.owner = request.user
      fs.day = day
      fs.save()
      
      return HttpResponseRedirect(reverse('days-detail', kwargs={'pk': pk}))
  else:
    form = ThingDoneForm

  context = {'day': day, 'form': form}
  return render(request, 'thingsdone/day_detail.html', context)

  
class MonthList(LoginRequiredMixin, generic.ListView):
  model = Month
  
  def get_queryset(self):
    return Month.objects.filter(user=self.request.user)

@login_required
def MonthDetail(request, pk):
    
  month = Month.objects.filter(user=request.user).get(pk=pk)
  days = month.day_set.filter(user=request.user).all()
  
  if request.method == "POST":
    form = ThingDoneForm(request.POST)
    if form.is_valid():
      fs = form.save(commit=False)
      fs.owner = request.user
      fs.month = month
      fs.save()
      
      return HttpResponseRedirect(reverse('months-detail', kwargs={'pk': pk}))
  else:
    form = ThingDoneForm
  
  context = {
    'month': month,
    'days' : days,
    'form' : form,
  }
  return render(request, 'thingsdone/month_detail.html', context)
  
class WeekList(LoginRequiredMixin, generic.ListView):
  model = Week
  
  def get_queryset(self):
    return Week.objects.filter(user=self.request.user)

@login_required
def WeekDetail(request, pk):
    
  week = Week.objects.filter(user=request.user).get(pk=pk)
  days = week.day_set.filter(user=request.user).all()
  
  if request.method == "POST":
    form = ThingDoneForm(request.POST)
    if form.is_valid():
      fs = form.save(commit=False)
      fs.owner = request.user
      fs.week = week
      fs.save()
      
      return HttpResponseRedirect(reverse('weeks-detail', kwargs={'pk':pk}))
  else:
    form = ThingDoneForm
  
  context = {
    'week': week,
    'days' : days,
    'form' : form
  }
  return render(request, 'thingsdone/week_detail.html', context)
  
@login_required
def DayCreate(request):
  if request.method == "POST":
#<---------------------------------------Form validation part---------------------------------------------->  
    form = DayForm(request.POST)
    form.user = request.user

    if form.is_valid():
  
#<----------------------------Check if the month and week exist, creates if it doesnt--------------------------->#  
      day = form.cleaned_data['day']
    
      allowed_week_start_days = []
      c1 = 0
      while c1 < 7:
       allowed_week_start_days.append(day - timedelta(days=c1))
       c1 +=1
     
      week = Week.objects.filter(user=request.user).filter(start_day__in=allowed_week_start_days).first()
      month = Month.objects.filter(user=request.user).filter(start_day__year=day.year).filter(start_day__month=day.month).first()
    
      if week:
        newweek = week
      else: 
        newweekstartday = ''
        for day_count in allowed_week_start_days:
          if day_count.weekday() == 6:
            newweekstartday = day_count
       
        newweek = Week(start_day=newweekstartday, user=request.user)
        newweek.save()
      
      if month:
        newmonth = month
      else:
        newmonth = Month(start_day=date(year=day.year, month=day.month, day=1), user=request.user)
        newmonth.save()
#<--------------------------------------------------Creates the day--------------------------------------------->       
      
      newday = Day(day=day, user=request.user, month=newmonth, week=newweek)
      newday.save()
#<-------------------------------------------Creates the saikang and adds it----------------------------------------->    
      for i in range(1,4):
        name = form.cleaned_data['saikang%s'%(i)]
        difficulty = form.cleaned_data['difficulty%s'%(i)]
        if name and difficulty:
          newthingdone = ThingDone(owner=request.user, name=name, difficulty=difficulty, day=newday)
          newthingdone.save()

      return HttpResponseRedirect(reverse('days-detail', kwargs={'pk': newday.pk})) 
#<------------------------------------------------------------------------------------------------------------------>
  else:
    form = DayForm
    
  context = {'form': form}
  return render(request, 'thingsdone/day_form.html', context)

@login_required
def DayEdit(request, pk):
  day = Day.objects.filter(user=request.user).get(pk=pk)
  ThingDoneFormSet = createThingDoneFormSet(Day)
  
  if request.method == "POST":
    formset = ThingDoneFormSet(request.POST, request.FILES, instance=day)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect(reverse('days-detail', kwargs={'pk': pk}))
  else:
    formset = ThingDoneFormSet(instance=day)
  
  if day.thingdone_set.count() == 0:
    return HttpResponseRedirect(reverse('days-detail', kwargs={'pk': pk}))
  
  context = {'formset':formset, 'title':day}
  return render(request, 'thingsdone/generic_edit.html', context)

class DayDelete(LoginRequiredMixin, DeleteView):
  model = Day
  success_url = reverse_lazy('days-list')

@login_required
def MonthCreate(request):
  if request.method == "POST":
#<---------------------------------------Form validation part---------------------------------------------->  
    form = MonthForm(request.POST)
    form.user = request.user

    if form.is_valid():
      start_day = date(year=form.cleaned_data['year'], month=int(form.cleaned_data['month']), day=1)
      newmonth = Month(start_day=start_day, user=request.user)
      newmonth.save()
#<-------------------------------------------Creates the saikang and adds it----------------------------------------->    
      for i in range(1,4):
        name = form.cleaned_data['saikang%s'%(i)]
        difficulty = form.cleaned_data['difficulty%s'%(i)]
        if name and difficulty:
          newthingdone = ThingDone(owner=request.user, name=name, difficulty=difficulty, month=newmonth)
          newthingdone.save()

      return HttpResponseRedirect(reverse('months-detail', kwargs={'pk': newmonth.pk})) 
#<------------------------------------------------------------------------------------------------------------------>
  else:
    form = MonthForm
    
  context = {'form': form}
  return render(request, 'thingsdone/month_form.html', context)
  
@login_required
def MonthEdit(request, pk):
  month = Month.objects.filter(user=request.user).get(pk=pk)
  ThingDoneFormSet = createThingDoneFormSet(Month)
  
  if request.method == "POST":
    formset = ThingDoneFormSet(request.POST, request.FILES ,instance=month)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect(reverse('months-detail', kwargs={'pk':pk}))
  else:
    formset = ThingDoneFormSet(instance=month)
  
  if month.thingdone_set.count() == 0:
    return HttpResponseRedirect(reverse('months-detail', kwargs={'pk': pk}))
  
  context = {'formset': formset, 'title':month}
  return render(request, 'thingsdone/generic_edit.html', context)
  
@login_required
def WeekCreate(request):
  if request.method == "POST":
    form = WeekForm(request.POST)
    form.user = request.user
    
    if form.is_valid():
      start_day = form.cleaned_data['start_day']
      newweek = Week(start_day=start_day, user=request.user)
      newweek.save()
      
      for i in range(1,4):
        name = form.cleaned_data['saikang%s'%(i)]
        difficulty = form.cleaned_data['difficulty%s'%(i)]
        if name and difficulty:
          newthingdone = ThingDone(owner=request.user, name=name, difficulty=difficulty, week=newweek)
          newthingdone.save()
        
      return HttpResponseRedirect(reverse('weeks-detail', kwargs={'pk':newweek.pk}))
  else:
    form = WeekForm
    
  context = {'form': form}
  return render(request, 'thingsdone/week_form.html', context)
  
@login_required
def WeekEdit(request, pk):
  week = Week.objects.filter(user=request.user).get(pk=pk)
  ThingDoneFormSet = createThingDoneFormSet(Week)
  
  if request.method == "POST":
    formset = ThingDoneFormSet(request.POST, request.FILES ,instance=week)
    if formset.is_valid():
      formset.save()
      return HttpResponseRedirect(reverse('weeks-detail', kwargs={'pk':pk}))
  else:
    formset = ThingDoneFormSet(instance=week)
  
  if week.thingdone_set.count() == 0:
    return HttpResponseRedirect(reverse('weeks-detail', kwargs={'pk': pk}))
  
  context = {'formset': formset, 'title':week}
  return render(request, 'thingsdone/generic_edit.html', context)
  
  
  
  
  
  
  
  
  