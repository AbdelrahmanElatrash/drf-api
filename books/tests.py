from django.test import TestCase
from .models import Book
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
# from rest_framework.test import APIRequestFactory
# Create your tests here.

# factory = APIRequestFactory()

class TestBook(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        cls.testuser1.save()

        cls.test_book = Book.objects.create(title='title',auther_name='auther', release_date="1990-01-01",
                                        img_url='https://img',description='description',user=cls.testuser1)
        cls.test_book.save()

    def test_get_single_book(self):
        
        url = reverse('book_detail', kwargs={'pk': 1})  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'title')
        self.assertEqual(response.data['auther_name'], 'auther')
       
        
    def test_get_book(self):
        url = reverse('book_list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
        
    # def test_create_book(self):
        
        
    #     data = {'title':'title', 'auther_name':'auther', 'release_date':"1990-01-01",
    #             'img_url':'https://img', 'description':'description' } 
        
        
    #     url = reverse('book_list')                                 
    #     response = self.client.post(url, data)
    #     print(response)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    
    # def test_update_book(self):
    #     obj = Book.objects.first()
    #     url = reverse('book_detail', kwargs={'pk': obj.pk})  
        
    #     data = {'title':'title1', 'auther_name':'auther', 'release_date':"1990-01-01",
    #             'img_url':'https://img', 'description':'description', 'user':self.testuser1 }
        
    #     response = self.client.put(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    #     obj.refresh_from_db()
    #     self.assertEqual(obj.title, 'title1')
        
        
        
    def test_delete_book(self):
        obj = Book.objects.first()
        url = reverse('book_detail', kwargs={'pk': obj.pk})  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=obj.pk).exists())