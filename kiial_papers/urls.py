"""
kiial_papers URL Configuration
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.contrib import admin
from django.urls import path,include
from django_filters.views import FilterView
from papers.filters import PapersFilter
from papers.views import SignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('papers.urls', namespace="papers")),
    url(r'^search/$', FilterView.as_view(filterset_class=PapersFilter,
        template_name='papers/search.html'), name='search'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('password-reset-done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path("convert/", include("guest_user.urls")),
]
