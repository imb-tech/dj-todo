from django.urls import path


from . import views



employee_lc = views.EmployeeViewSet.as_view({'get': 'list', 'post': 'create'})
employee_udd = views.EmployeeViewSet.as_view({'get': 'retrieve', 'delete': 'destroy', 'patch': 'partial_update'})

urlpatterns = [
    path('employees/', employee_lc, name='employee_lc'),
    path('employees/<int:pk>/', employee_lc, name='employee_udd'),
]


