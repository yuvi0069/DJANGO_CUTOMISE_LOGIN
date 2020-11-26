from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
urlpatterns = [
    path('',views.customer),

    path('card/',views.contact),
    path('home/',views.home),
    path('logout/',views.out),
    path('reset/',auth_views.PasswordResetView.as_view(template_name='accounts/reset.html'),name='reset_password'),
    path('reset_send/',auth_views.PasswordResetDoneView.as_view(template_name='accounts/done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='accounts/confirm.html'),name='password_reset_confirm'),
    path('reset_done/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/comp.html'),name='password_reset_complete'),
    path('sign/',views.sign),
]
