from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
import csv
# Create your views here.

def insert_data(self):
    with open('C:\\Users\\USER\\OneDrive\\Desktop\\django projects\\Akhil\\Scripts\\project39\\app\\Business-employment-data-september-2022-quarter-csv.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            sr=i[0]
            p=i[1]
            dv=i[2]
            su=i[3]
            st=i[4]
            u=i[5]
            m=i[6]
            s=i[7]
            g=i[8]
            s1=i[9]
            s2=i[10]
            s3=i[11]
            EDO=EmploymentData(Series_reference=sr,Period=p, Data_value=dv,Suppressed=su,Status=st,Units=u,Magnitude=m,Subject=s,Group=g,Series_title_1=s1,Series_title_2=s2,Series_title_3=s3)
            EDO.save()
    return HttpResponse('Data is Uploaded successfully')
