# -*- coding: utf-8 -*-
from flask import Blueprint
import csv
import traceback

data= Blueprint('register', __name__)
from index import *
from const import *

"""
CACHE PATH
"""
HOSPITAL_PATH = os.path.join(path_home, "HOSPITAL.csv")
HOTEL_PATH = os.path.join(path_home, "HOTEL.csv")
LOGISITICAL_PATH = os.path.join(path_home, "LOGISITICAL.csv")
NEWS_PATH = os.path.join(path_home, "NEWS.csv")


@data.before_request
def before(*args,**kwargs):
    pass


@data.route('/index')
def index():
    return "hello world"


@data.route('/hospital_list')
def hospital_list():
    try:
        data = csv.reader(open(HOSPITAL_PATH, 'r'))
        next(data)
        hospitals= []
        for hospital in data:
            item = {}
            item["province"]=hospital[0]
            item["name"] = hospital[1]
            item["address"] = hospital[2]
            item["people"] = hospital[3]
            item["need"] = hospital[4]
            item["link"] = hospital[5]
            item["phone"] = hospital[6]
            item["extra"] = hospital[7]
            hospitals.append(item)
        response={
            "success": True,
            "data": hospitals
        }
    except Exception as e:
        response = {
            "success":False,
            "msg":e.message
        }
    return json.dumps(response,ensure_ascii=False)


@data.route('/hotel_list')
def hotel_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        csv_data = csv.reader(open(HOTEL_PATH, 'r'))
        next(csv_data)
        resp_data = []
        resp_data.append(dict(zip(HOTEL_HEADERS, csv_data))
        resp['success'] = True
    except Exception as e:
        resp['msg'] = str(e)
        traceback.print_exec()
    return json.dumps(resp, ensure_ascii=False)


@data.route('/logistical_list')
def logistical_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        csv_data = csv.reader(open(LOGISITICAL_PATH, 'r'))
        next(csv_data)
        resp_data = []
        resp_data.append(dict(zip(LOGISTICS_HEADERS, csv_data))
        resp['success'] = True
    except Exception as e:
        resp['msg'] = str(e)
        traceback.print_exec()
    return json.dumps(resp, ensure_ascii=False)


@data.route('/news_list')
def hotel_list():
    resp = {
        'success': False,
        'data': [],
        'msg': '',
    }
    try:
        csv_data = csv.reader(open(NEWS_PATH, 'r'))
        next(csv_data)
        resp_data = []
        resp_data.append(dict(zip(NEWS_HEADERS, csv_data))
        resp['success'] = True
    except Exception as e:
        resp['msg'] = str(e)
        traceback.print_exec()
    return json.dumps(resp, ensure_ascii=False)
