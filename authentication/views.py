import jwt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class LoginView(APIView):
    def post(self,request):
        credential = request.data['credential']
        hj = '232416043202-814erfoumpuobmt513rehc42ruijelb7.apps.googleusercontent.com'
        decoded_token = jwt.decode(credential, hj, algorithms=['HS256'])
        print(decoded_token)
        
        return Response("hi")