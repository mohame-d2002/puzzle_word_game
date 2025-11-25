from django.urls import path
from .views import HomePageView, SelectCategoryView, SignupMenView, SignupWomenView, SignupKidsView, NameLoginView, CustomLogoutView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('select_category', SelectCategoryView.as_view(), name='select_category'),
    path('select_category/mansignup', SignupMenView.as_view(), name='men_signup'),
    path('select_category/womensignup', SignupWomenView.as_view(), name='women_signup'),
    path('select_category/kidssignup', SignupKidsView.as_view(), name='kids_signup'),
    path('login', NameLoginView.as_view(), name='custom_login'),
    path('logout', CustomLogoutView.as_view(), name='custom_logout')
]