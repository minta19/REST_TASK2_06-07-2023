from django.urls import path
from .views import StudentViewcreate,StudentDetails

urlpatterns=[
    path('listcreate/',StudentViewcreate.as_view(),name='list_create'),
    path('details/<int:pk>/',StudentDetails.as_view(),name='details')
]

