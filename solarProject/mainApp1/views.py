from typing import Any
from urllib import request
from django.db.models import Sum, F, Subquery
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, UserInputForm, UserInputForm1, ElectronicDetailsForm
from .models import UserInput2, UserInput, ElectronicDetail
from django.forms import formset_factory


# Create your views here.

def dashboard(request):
  return render(request,'registration/dashboard.html',{'section':'dashboard'})

def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        #profile_form = UserInputForm1(request.POST)
        if user_form.is_valid():
            #Create a new user object but avoid saving it yet
             user=user_form.save()

            # profile = profile_form.save(commit=False)
             #profile.user = user
             #profile.save()

             #Set the choosen password
             user.set_password(
                 user_form.cleaned_data['password'])
             #Save the user object
             user.save()
             return render(request, 'registration/register_done.html',{'user':user})
    else:
        user_form=UserRegistrationForm()
        #profile_form= UserInputForm1()

    context= {'user_form': user_form} 

    return render(request, 'registration/register.html',context )

''''This code below allows a User to update their Electronic inputs after they have signed up'''

def userInput(request):
          profile_form = UserInputForm()
          if request.method == "POST":
                 user_form = UserRegistrationForm(request.POST, instance=request.user)
                 profile_form = UserInputForm(request.POST, instance=request.user.userinput2)
                 if profile_form.is_valid():
                      profile_form.save()
                      messages.success(request,'Your Data has been Updated!!')
                      return redirect('/userInput')
          else:
             user_form = UserRegistrationForm(instance=request.user)
             profile_form = UserInputForm(instance=request.user.userinput2) 
          return render(request,'registration/userInput.html',{'profile_form': profile_form})

class ElectronicList(LoginRequiredMixin, ListView):
     model=  ElectronicDetail
     context_object_name = 'electroList'

     def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          #context['electroList'] = ElectronicDetail.objects.annotate(totalPower=(F('no_Of_Load') * F('power_Of_Load')), totalEnergy=(F('totalPower') * F('operating_Hours'))).filter(userF=self.request.user)
          # Annotate the queryset
          annotated_queryset = ElectronicDetail.objects.filter(userF=self.request.user).annotate(totalPower=F('no_Of_Load') * F('power_Of_Load'),totalEnergy=F('no_Of_Load') * F('power_Of_Load') * F('operating_Hours'))

           # Aggregate the totalEnergy field
          total_energy_aggregated = annotated_queryset.aggregate(totEnergy=Sum('totalEnergy'))
          total_power_aggregated = annotated_queryset.aggregate(totPower=Sum('totalPower'))

          # Add both to the context dictionary
          context = {
                      'electroList': annotated_queryset,
                      'totalEnergyAggregated': total_energy_aggregated['totEnergy'],  # Access the aggregated value
                      'totalPowerAggregated': total_power_aggregated['totPower']
                     }
          return context
    
     
class ElectronicsDetail(LoginRequiredMixin, DetailView):
     model= ElectronicDetail
     context_object_name= 'electroList'
     template_name= 'mainApp1/appliance.html'
     

class AddElectronicApp(LoginRequiredMixin, CreateView): 
     model= ElectronicDetail
     fields = ['electronicName','power_Of_Load','operating_Hours','no_Of_Load','effective_Sunlight']
     success_url = reverse_lazy('electronicdetails') 
     #This function will make sure the logged in user creates the electronic app.
     def form_valid(self, form):
          form.instance.userF = self.request.user
          return super(AddElectronicApp, self).form_valid(form)

class ElectronicUpdate(LoginRequiredMixin, UpdateView):
     model= ElectronicDetail
     fields = ['electronicName','power_Of_Load','operating_Hours','no_Of_Load','effective_Sunlight']
     success_url= reverse_lazy('electronicdetails')
    
class ElectronicDelete(LoginRequiredMixin, DeleteView):
     model= ElectronicDetail
     success_url= reverse_lazy('electronicdetails')

def calculate(request):
      
     all_Values= ElectronicDetail.objects.all
     return render(request,'registration/calculate.html',{'all':all_Values})
     
      
  

'''def dashboard(request):
     all_Values= ElectronicDetail.objects.all
     return render(request,'registration/dashboard.html',{'all':all_Values})'''

