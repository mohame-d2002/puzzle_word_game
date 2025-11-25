from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import CustomUser
from .forms import SignupMenForm, SignupWomenForm, SignupKidsForm


# Create your views here.

class HomePageView(TemplateView):
    template_name = '_base.html'

class SelectCategoryView(TemplateView):
    template_name = 'select_category.html'

class BaseSignupView(CreateView):
    model = CustomUser
    template_name = 'signup.html'
    success_url = reverse_lazy('custom_login')
    category_value = None

    def form_valid(self, form):
        signup = form.save(commit=False)
        signup.category = self.category_value
        if not signup.username:
          signup.username = f"user_{CustomUser.objects.count() + 1}"
        signup.save()
        return super().form_valid(form)
    
class SignupMenView(BaseSignupView):
    form_class = SignupMenForm
    category_value = 'Man'

class SignupWomenView(BaseSignupView):
    form_class = SignupWomenForm
    category_value = 'Woman'

class SignupKidsView(BaseSignupView):
    form_class = SignupKidsForm
    category_value = 'kid'


# LOGIN
from django.contrib.auth import login
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import NameLoginForm

class NameLoginView(FormView):
    template_name = 'login.html'
    form_class = NameLoginForm
    success_url = reverse_lazy('home')  # redirect after successful login

    def form_valid(self, form):
        user = form.cleaned_data['user']
        login(self.request, user)
        return super().form_valid(form)

class CustomLogoutView(ListView):
    model = CustomUser
    template_name = 'logout.html'
