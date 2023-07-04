from rest_framework import serializers
from .models import Book



        
        
class BookSerializer(serializers.ModelSerializer):
    class Meta :
        model= Book
        fields =  ('id', 'title', 'auther_name', 'release_date', 'description','img_url', 'user')