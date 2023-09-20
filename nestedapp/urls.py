from django.urls import path
from .views import * 


urlpatterns = [
    path('',userView.as_view(),name='user'),
    path('user/',userOnlyView.as_view(),name='user_only'),
    path('doctor/',DoctorView.as_view(),name='doctor'),
    path('doctor_only/',DoctorOnlyView.as_view(),name='doctor_only'),
]