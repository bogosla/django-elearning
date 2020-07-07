from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from accounts.forms import LoginForm, PassChangeForm, PassResetForm, PassSetForm

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #changing
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html', form_class=PassChangeForm), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_change.html'), name='password_change_done'),
    
    #resetting
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html', form_class=PassResetForm, email_template_name='password_reset_email.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=PassSetForm), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('', views.dash, name='dash')
]