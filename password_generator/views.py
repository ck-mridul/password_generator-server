import random
import string
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class GeneratePassword(APIView):
    def post(self,request):
        attributes = request.data['attributes']
        length = request.data['length']
        char_set = '' 
        
        if attributes['upperCase']:
            char_set += string.ascii_uppercase
        if attributes['lowerCase']:
            char_set += string.ascii_lowercase
        if attributes['number']:
            char_set += string.digits
        if attributes['symbol']:
            char_set += string.punctuation
            
        char_list = list(char_set)
        random.shuffle(char_list)
        password = ''.join(random.sample(char_list, int(length)))
        response = {
            'password':password
        }
        print(password)
        return Response(response)


        
