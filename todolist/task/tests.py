from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Task
from django.utils import timezone
import datetime

class TaskTests(APITestCase):
    def setUp(self):
        time = timezone.now() + datetime.timedelta(days=30)
        self.task_data = {
            'title': 'tarefa teste',
            'description': 'tarefa para testes',
            'deadline': timezone.now(),
            'completion_date': time,
            'state': 'nova'
        }
    
    def create_task(self):
        url = reverse('task-list')
        response = self.client.post(url,self.task_data, format = 'json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_get_task_list(self):
        Task.objects.create(**self.task_data)
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)