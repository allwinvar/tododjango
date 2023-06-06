from django.urls import path
from . import views
app_name='TODOapp'
urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
]