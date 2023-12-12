from django.urls import path
from .views import *

urlpatterns = [
    path('staffs/', StaffList.as_view()),
    path('staffs/<int:pk>/', StaffDetail.as_view()),
    
	path('records/', RecordList.as_view()),
    path('records/<int:pk>/', RecordDetail.as_view()),
    
	path('departments/', DepartmentList.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),

    path('export_staff_to_excel/', export_staff_to_excel),
    path('export_record_to_excel/', export_record_to_excel),
    path('import_data_to_db/', import_data_to_db),

]