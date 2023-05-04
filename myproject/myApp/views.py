from django.shortcuts import render, HttpResponse
import pandas as pd
import calendar
import datetime


def index(request):
    filepath = 'C:/Users/jkhong/Desktop/크루플랜(2023)_v01.xlsx'
    sheetname = 'C_도적'
    data = pd.read_excel(filepath, sheet_name=sheetname)
    # columns_to_select = ['CV']
    selected_data = data.iloc[49, 12]
    return HttpResponse(selected_data)


def cal(request):
    today = datetime.datetime.today()
    current_month = today.month
    current_year = today.year
    cal = calendar.monthcalendar(current_year, current_month)
    # for week in cal:
    #     print(week)
    return HttpResponse(cal)


