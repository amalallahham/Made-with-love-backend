from django.shortcuts import render
# Create your views here.
import json as JSON
from rest_framework import status, exceptions
from django.http import HttpResponse

import jwt,json
from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render
from accounts.models import Item
from accounts.models import Seller
from django.core.serializers import json
# import jwt,json
#importinf models of tables 


from rest_framework_simplejwt.backends import TokenBackend
from accounts.models import Item
from accounts.models import Seller
from accounts.models import Buyer
from accounts.models import Category
from accounts.models import Order
class getCategoryStore (APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, cat):
        # data = self.request.data 
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
             return Response ({"jhh":"hjghjgh"})
        #  tole = jwt.decode(token, "SECRET_KEY") 
        
        #  print(tole['email'],'hijuhuyu')
        #  email = tole['email']
        #  if Seller.objects.get( email = email):
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    print(tole['email'],'hijuhuyu')
                    email = tole['email']
                    if Seller.objects.get( email = email): 
                        print(cat)
                        obj = Seller.objects.filter(category = 'food')
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(obj)
                        data= JSON.loads(json_serialized)
                        # print(data)
                        return Response (data)
                except jwt.DecodeError:
                    return HttpResponse({'Errorrrrrr': "Internalll server error"}, status="500")
class addItem(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    print(tole['email'],'hijuhuyu')
                    email = tole['email']
                    if Seller.objects.get( email = email): 
                        data = self.request.data 
                        print(data)
                        productName = data['product'] 
                        description = data['description'] 
                        price = data['price']
                        category = data['category']
                        image = data['url'] 
                        if category == "clothes":
                            gender = data['gender'] 
                            size = data['size'] 
                            category_id = Category.objects.get(category_id =200)
                            item = Item.objects.create (productname = productName, description=description, price=price, gender=gender, size=size, image=image, category_id=200)
                            return Response ({'success': 'Add Item'})
                        if(category == 'food'):
                            types = data['type'] 
                            category_id = Category.objects.get(category_id =100) 
                            item = Item.objects.create (productname = productName, description=description, price=price,types=types, image=image, category_id=100)
                            return Response ({'success': 'Add Item'})
                        if category == 'accessories':
                            material = data['material'] 
                            print(material,"materiaaal")
                            category_id = Category.objects.get(category_id =300)
                            item = Item.objects.create (productname = productName, description=description, price=price, image=image, material=material, category_id=300)
                            return Response ({'success': 'Add Item'})
                        if category == 'babyproducts':
                            gender = data['gender']
                            category_id = Category.objects.get(category_id =400)
                            item = Item.objects.create (productname = productName, description=description, price=price, gender=gender, image=image, category_id=400)
                            return Response ({'success': 'Add Item'})
                            item = Item.objects.create (productname = productName, description=description, price=price, gender=gender,types=types, size=size, image=image, material=material)
                            item.save()
                            return Response ({'success': 'Add Item'})

                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")

class getItems(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    print(tole['email'],'hijuhuyu')
                    email = tole['email']
                    if Seller.objects.get( email = email): 
                        obj = Item.objects.filter(store_id=pk)
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(obj)
                        print(json_serialized,"iteeeeeems" )
                        return Response(json_serialized)
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")

class getItemsVisit(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    print(tole['email'],'hijuhuyu')
                    email = tole['email']
                    if Seller.objects.get( email = email): 
                        obj = Item.objects.filter(store_id=pk)
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(obj)
                        print(json_serialized,"iteeeeeems" )
                        return Response(json_serialized)
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")

class sellerVisit(APIView):
    permission_classes = (permissions.AllowAny,)         
    def get(self, request,pk, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    print(tole['email'],'hijuhuyu')
                    email = tole['email']
                    print(pk)
                    if Seller.objects.get( email = email):
                        obj1 = Seller.objects.filter(pk=pk)
                        json_serializer = json.Serializer()
                        json_serialized1 = json_serializer.serialize(obj1)
                        # print(json_serialized )
                        myData = []
                        print(pk,">>>>11111111111111")
                        obj = Item.objects.filter(store_id=pk)
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(obj)
                        # print(json_serialized )
                        myData.append(json_serialized1)
                        myData.append(json_serialized)
                        print("mydataaa",myData,"dataaend")
                        # dat =   JSON.dumps(myData)
                        return Response(json_serialized1)    
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")     
class SnippetDetailSeller(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    print(tole['email'],'hijuhuyu')
                    email = tole['email']
                    print(pk)
                    if Seller.objects.get( email = email): 

                        obj1 = Seller.objects.filter(pk=pk)
                        json_serializer = json.Serializer()
                        json_serialized1 = json_serializer.serialize(obj1)
                        # print(json_serialized)
                        myData = []
                        print(pk,">>>>11111111111111")
                        obj = Item.objects.filter(store_id=pk)
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(obj)
                        # print(json_serialized )
                        myData.append(json_serialized1)
                        myData.append(json_serialized)
                        print("mydataaa",myData,"dataaend")
                        # dat =   JSON.dumps(myData)
                        return Response(json_serialized1)
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")

            
class getListOrder (APIView):
     permission_classes = (permissions.AllowAny,)
     
        # try:
        #     valid_data = TokenBackend(algorithm='HS256').decode(token,verify=False)
        #     user = valid_data['user']
        #     request.user = user
        # except ValidationError as v:
        #     print("validation error", v)
     def get(self, request, pk):
         token = request.META.get('HTTP_AUTHORIZATION')
         print(token)
         if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
         elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    print(tole['email'],'hijuhuyu')
                    email = tole['email']
                    if Seller.objects.get( email = email):
                        
                        obj = Order.objects.filter(store_id=pk)
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(obj)
                        data= JSON.loads(json_serialized)
                        for x in data:
                                # print(x['fields']['buyer'])
                            obj1 = Buyer.objects.get(buyer_id = x['fields']['buyer'])
                                # print(obj1.username)
                            x['fields']['buyer'] = obj1.username
                        for x in data:
                                # print(x['fields']['item'])
                            obj1 = Item.objects.get(item_id = x['fields']['item'])
                            print(obj1.productname)
                                
                            x['fields']['item'] = obj1.productname  
                        return Response (data)
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")

class editItem (APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, pk):
        data = self.request.data 
        if not data:
            return HttpResponse({"Error":"please enter your information"} ,status="401")
        elif data:
            try:
                gender = data['gender'] 
                size = data['size'] 
                productName = data['product'] 
                description = data['description'] 
                price = data['price']
                image = data['url'] 
                material = data['material'] 
                types = data['type'] 

                Item.objects.filter(item_id= pk).update(productname = productName, description=description, price=price, gender=gender,types=types, size=size, image=image, material=material)    
                return HttpResponse({"success":"updated"} ,status="200")
            except Item.DoesNotExist:
                return HttpResponse({"Error":"ERROR"} ,status="401")
              
        

