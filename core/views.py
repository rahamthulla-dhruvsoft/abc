from rest_framework.views import APIView
from rest_framework.response import Response
#from rest_framework.permissions import IsAuthenticated
#from rest_framework.permissions import AllowAny
#from rest_framework import permissions
from rest_framework.response import Response
import json
from rest_framework_simplejwt import authentication
from django.contrib.auth import authenticate
from django.db import connection
from django.contrib.auth.models import User
import requests

class Helloview(APIView):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (authentication.JWTAuthentication,)
    def get(self,request):
        print(request)
        content = {'message': 'Hello from hello'}
        return Response(content)

class AccesToken(APIView):
    #permission_classes = (AllowAny,)
    def post(self,request):
        a=json.loads(request.body.decode('utf-8'))
        r = requests.post('http://127.0.0.1:8000/api/token/', data={'username':a['username'], 'password':a['password']})
        response = r.json()
        token = response['access']
        print(token)
        content = {'message': 'Authenticated user','token':token}
        return Response(content)

class LoginView(APIView):
    #permission_classes = (IsAuthenticated,)
    #authentication_classes = (authentication.JWTAuthentication,)
    def post(self, request):
        a=json.loads(request.body.decode('utf-8'))
        print(a["username"])
        print(a["password"])
        cursor = connection.cursor()
        orgs_list1 = list()
        username=a["username"]
        cursor.execute("select keyword from hhh1_keywords where org_id_id IN(select org_id_id from hhh1_members where user_id_id IN (select id from auth_user where username='"+username+"'))")
        for row in cursor.fetchall():
            orgs_list1.append(row[0])
        user = authenticate(username=a["username"], password=a["password"])
        if user is not None:
            print('Authenticated user')
            content = {'message': 'Authenticated user','keywords':orgs_list1}
        else:
            print('Not Authenticated user')
            content = {'message': 'Unauthenticated user'}
        return Response(content)
class SignUpView(APIView):
    def post(selfself,request):
        content = {'message': 'user created'}
        print(json.loads(request.body.decode('utf-8')))
        a=json.loads(request.body.decode('utf-8'))
        user=User.objects.create_user(username=a["email"],email=a["email"],password=a["password"])
        print(user)
        return Response(content)



