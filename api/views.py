from rest_framework import generics
from . import serializers
from .models import *
import pandas as pd
from django.http import JsonResponse
from django.conf import settings
from django.shortcuts import render


"""Staff"""

class StaffList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = serializers.StaffSerializer

class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = serializers.StaffDetailSerializer

"""Record"""

class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = serializers.RecordSerializer

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = serializers.RecordDetailSerializer

"""Department"""

class DepartmentList(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentDetailSerializer


def export_staff_to_excel(request):
    objs = Staff.objects.all()
    data = []

    for obj in objs:
        data.append({
            "Full Name": obj.name,
            "Card ID": obj.card_id,
            "Phone Number": obj.phone_number,
            "Email": obj.email,
            "Gender": obj.gender,
            "Department": obj.department,
            "User": obj.user
        })


    pd.DataFrame(data).to_excel('Staff.xlsx')
    return JsonResponse({'status': 200})


def export_record_to_excel(request):
    objs = Record.objects.all()
    data = []

    for obj in objs:
        data.append({
            "Full Name": obj.name,
            "Card ID": obj.card_id,
            "Datetime": (obj.datetime).strftime('%x %X'),
            "Department": obj.department,
            "Action": obj.action
        })


    pd.DataFrame(data).to_excel('Record.xlsx')
    return JsonResponse({'status': 200})


def import_data_to_db(request):
    if request.method == 'POST':
        file = request.FILES['files']
        obj = ExcelFile.objects.create(file = file)
        path = str(obj.file)
        print(f'{settings.BASE_DIR}/{path}')
        df = pd.read_excel(path)
        for d in df.values:
            print(d)

    return render(request, 'excel.html')
