# -*- coding:utf-8 -*-
from django.db import connections
import MySQLdb
from django.shortcuts import render, redirect
from django.conf import settings
from django.template import loader, Context
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, StreamingHttpResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Q, Max
from django.db.models.aggregates import Count
from django.core import serializers
from django.core.paginator import Paginator
from django.utils import timezone
from td import models
from requests_oauthlib import OAuth2Session
from datetime import datetime, timedelta
import hashlib, os, logging, time, base64, json, requests, uuid


logger = logging.getLogger('log')


def td_req(request):
    res = request.POST  # PTD接口请求： <QueryDict: {'ptd_name': ['发红包'], 'PhoneNum': ['11111'], 'code': ['上海']}>
    logger.info(res)

    return JsonResponse(data={"code": 0, "data": ["恭喜你，拯救了世界！"]}, json_dumps_params={'ensure_ascii': False})
    # return JsonResponse(data={"code": 0, "data": [{'aaa':'111'},{'bbb':'222'}]}, json_dumps_params={'ensure_ascii': False})



