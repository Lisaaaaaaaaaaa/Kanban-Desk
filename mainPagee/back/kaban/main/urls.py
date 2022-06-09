"""kaban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from . import views


urlpatterns = [
    path('', views.user_login, name='home'),
    path('kaban', views.index, name='kaban'),
    path('reg', views.register, name='reg'),
    path('update/<int:pk>', views.update.as_view(), name='update'),
    path('<int:pk>', views.detailView.as_view(), name='detail'),
    path('delete/<int:pk>', views.delete.as_view(), name='delete')
]
