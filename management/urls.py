"""
URL configuration for management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1.views import qr_code_view
from app1.views import new_registration, update_register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qr/', qr_code_view, name='qr_page'),
    path('register/', new_registration, name='register_page'),
    path('update1/<int:id>/', update_register, name='update_reg'),
]

