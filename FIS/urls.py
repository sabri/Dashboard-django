from django.conf.urls import url
from rest_framework import routers
from . import views
from .views import *
from django.urls import path,include

r=routers.DefaultRouter()
r.register('',views.laptop_list)

r2=routers.DefaultRouter()
r2.register('',views.user_list)

urlpatterns=[
    url(r'^$',index,name='index'),

    url(r'^display_laptop$', display_laptops, name='display_laptops'),
    url(r'^display_desktop$', display_desktops, name='display_desktops'),


    url(r'^add_laptop$', add_laptot, name='add_laptop'),
    url(r'^add_desktop$', add_desktop, name='add_desktop'),


    url(r'^edit_laptop/(?P<pk>\d+)$', edit_laptop, name='edit_laptop'),
    url(r'^edit_desktop/(?P<pk>\d+)$', edit_desktop, name='edit_desktop'),


    url(r'^delet_laptop/(?P<pk>\d+)$', delet_laptop, name='delet_laptop'),
    url(r'^delet_desktop/(?P<pk>\d+)$', delet_desktop, name='delet_desktop'),

    path('desktopjson/',views.desktop_list.as_view()),
    path('laptopjson/',include(r.urls)),
    path('userjson/',include(r2.urls)),

    path('register/', register, name='register'),
    path('register_backend/', register_backend, name='register_backend'),

    path('login/', log, name='log'),
    path('login_backend/', log_backend, name='log_backend'),
    path('logout_backend/', logout_backend, name='logout_backend'),

    path('flexmonster/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),

    path("products/", views.products, name="products"),
    path('panda', main_view, name='panda'),
    path("model_name/", views.model_name, name="model_name"),

    path("pie/", views.pie, name="model_Usb_Headset"),
    path("piel/", views.piel, name="model_Brand_name"),
    path("Dell_HP_desk/", views.Dell_HP_desk, name="Dell_HP_desk"),
    path("programming/", views.programming, name="programming"),
    path("principal_chart/", views.principal_chart, name="principal_chart"),
    path("nav/", views.navbar, name="navbar"),

]