"""star_wars_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# wiew imports from my application
from pages.views import homepage_view
from pages.views import  ep1_view, ep2_view, ep3_view, ep4_view, ep5_view, ep6_view, ep7_view
from pages.views import more_info1, more_info2, more_info3, more_info4, more_info5, more_info6, more_info7

urlpatterns = [
    path('admin/', admin.site.urls),

    # oath for homepage view
    path('', homepage_view, name='home'),

    # path for each movie view and its additional info view
    path('episode1/', ep1_view, name='ep1'),
        path('episode1/info/', more_info1, name='ep1_info'),
    path('episode2/', ep2_view, name='ep2'),
        path('episode2/info/', more_info2, name='ep2_info'),
    path('episode3/', ep3_view, name='ep3'),
        path('episode3/info/', more_info3, name='ep3_info'),
    path('episode4/', ep4_view, name='ep4'),
        path('episode4/info/', more_info4, name='ep4_info'),
    path('episode5/', ep5_view, name='ep5'),
        path('episode5/info/', more_info5, name='ep5_info'),
    path('episode6/', ep6_view, name='ep6'),
        path('episode6/info/', more_info6, name='ep6_info'),
    path('episode7/', ep7_view, name='ep7'),
        path('episode7/info/', more_info7, name='ep7_info'),
    ]
