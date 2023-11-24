from django.contrib import admin
from django.urls import path
from mathapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('areaofsqprism/',views.sqprismarea,name="areaofsqprism"),
    path('',views.sqprismarea,name="areaofsqprismroot")
]
