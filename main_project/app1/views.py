# Python Core Imports
import json
from math import trunc
import random
import requests
from datetime import datetime

# Django Core Imports
from django.shortcuts import render
from django.http import HttpResponse

# Django Auth Imports

# REST API
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Database Imports
from .models import ErrorLogApi, UsageLogApi

# Variable Imports
#from .floww_variables import SERVICE_LIST, RENTAL_PLANS_AVAILABLE, PRODUCT_LIST

# Contant Imports
#from main_project.constants import TASK_DETAILS_BASE_URL









# Edit Order Details

class EditOrderInstructions(APIView):
    authentication_classes = []#[TokenAuthentication,]
    permission_classes = []#[IsAuthenticated,]

    def get(self, request):
        pass
 
    def post(self, request):
        # Get user_id from Token auth. Django DB (user_id/uid) -> Company Detail DB (uid) -> user_id

        #user_uid = request.user.username
        user_id = 'testing'#CompanyDetails.objects.get(user_uid=user_uid).user_id

        # try:

        # Sample POST data: { “vendorCode”:”VEN88762”, ”productDescription”:”Bottles”, ”companyName”:”Myntra”, ”deliveryDate”:”13/12/2021”, “orderType”:”perOrder”, ”orderList” : [ {“pickup”:”F-205”, “pickupPincode”: “400076”, “pickupNo”:”9999999999”, “drop”:”F-205”, “dropPincode”: “400076”, “dropNo”:”99999”, “weight”:”small”, “instruction”:”Delivery to watchman”}, {} ], “rentalPlan”: ”plan1”, “serviceList”:[“same_day”,”otp”]}
        # To check, if the orderId parameter is sent correctly
        try:
            order_id = str(request.data.get('orderId'))
        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps({'status': 400, 'error': 'order_id_not_found', 'message': 'Either orderId is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)

        try:
            instructions = str(request.data.get('instruction'))
        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps({'status': 400, 'error': 'instruction_not_found', 'message': 'Either instruction is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)


        # To check, if the order (via orderId) is present in the database
        try:            
            # From the vendor_code, take out vendor charge data 
            #order_query = OrderDetails.objects.get(order_id=order_id)

            order_query = {
                'instructions':'xyz'
            }

        except Exception as e:
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            
            response = json.dumps({'status': 400, 'error': 'order_not_found', 'message': 'orderId not found in database, please check'})                # [EDIT]
            return Response(response, status=400)

        try:
            #order_query.instructions = str(instructions)
            #order_query.save()

            order_query['instructions'] = instructions
            status = 'success'

            # ----------------Logging
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=True, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps(
            {'status': status})
            return Response(response, status=201)
        
        except Exception as e:
            status = 'failure'
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='EditOrderInstructions', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='EditOrderInstructions', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps(
            {'status': status})
            return Response(response, status=400)

    def delete(self, request):
        pass

    def put(self, request):
        pass










# Get Order Details

class GetOrderDetails(APIView):
    authentication_classes = []#[TokenAuthentication,]
    permission_classes = []#[IsAuthenticated,]

    def get(self, request):
        # Get user_id from Token auth. Django DB (user_id/uid) -> Company Detail DB (uid) -> user_id

        #user_uid = request.user.username
        user_id = 'testing'#CompanyDetails.objects.get(user_uid=user_uid).user_id

        # To check, if the orderId parameter is sent correctly
        try:
            order_id = str(request.query_params.get('orderId'))
        except Exception as e:

            # ----------------Logging
            ErrorLogApi.objects.create(api_name='GetOrderDetails', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='GetOrderDetails', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps({'status': 400, 'error': 'order_id_not_found', 'message': 'Either orderId is not sent or parameter name is misspelt'})                # [EDIT]
            return Response(response, status=400)
        
        # To check, if the order (via orderId) is present in the database
        try:
            #order_query = OrderDetails.objects.get(order_id=order_id)
            order_query = {
                'pickup_address':'xyz',
                'drop_address':'xyz',
                'pickup_pincode':'xyz',
                'drop_pincode':'xyz',
                'pickup_contact_no':'xyz',
                'drop_contact_no':'xyz',
                'weight':'xyz',
                'status':'xyz',
                'instructions':'xyz',
            }
            pickup_address = order_query.pickup_address
            drop_address = order_query.drop_address  
            pickup_pincode = order_query.pickup_pincode 
            drop_pincode = order_query.drop_pincode 
            pickup_contact_no = order_query.pickup_contact_no 
            drop_contact_no = order_query.drop_contact_no 
            weight = order_query.weight
            status = order_query.status                         # It is a list containing an object
            instructions = order_query.instructions 

            # Get Task Id also
            #task_query = TaskDetails.objects.get(orders_list={'order_id':order_id})
            task_id = 'xyz'#task_query.task_id
            

            data = {'orderId': order_id, 'pickup': pickup_address, 'drop': drop_address, 'pickupPincode': int(pickup_pincode), 
            'dropPincode': int(drop_pincode), 'pickupNo': pickup_contact_no, 'dropNo': drop_contact_no, 'weight': float(weight), 
            'instruction': instructions, 'orderStatusList':status, 'taskId':task_id}

            # ----------------Logging
            UsageLogApi.objects.create(api_name='GetOrderDetails', api_success=True, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps(data)
            return Response(response, status=200)

        except Exception as e:
            
            # ----------------Logging
            ErrorLogApi.objects.create(api_name='GetOrderDetails', error_val=e, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)
            UsageLogApi.objects.create(api_name='GetOrderDetails', api_success=False, timestamp=str(int(datetime.now().timestamp())), user_id=user_id)

            response = json.dumps({'status': 400, 'error': 'order_not_found', 'message': 'orderId not found in database, please check'})                # [EDIT]
            return Response(response, status=400)

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass