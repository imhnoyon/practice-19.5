
from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout




def Register(request):
    if request.method=='POST':
        register_form=forms.RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('signin')
    else:
        register_form=forms.RegisterForm()
    return render(request,'register_form.html',{'form':register_form,'type':'Signin'})


class users_login(LoginView):
    template_name='register_form.html'
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        # messages.success(self.request,'Loggin in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # messages.success(self.request,'Loggin Information is Incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs) 
        context["type"] = 'Login'
        return context

def Profile(request):
    return render(request,'profile.html')


# class User_logout(LogoutView):
#     success_url=reverse_lazy('login')

def Logoutviews(request):
    logout(request)
    return redirect('login')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')



def UserPass_change(request):
    if request.method=='POST':
        form=PasswordChangeForm(request=request.user,data=request.POST)
        if form.is_valid():
            update_session_auth_hash(request,form.user)
            form.save()
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'register_form.html',{'form':form,'type':'Change Password'})






