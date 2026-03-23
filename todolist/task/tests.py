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
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'tarefa teste')
    
    def test_get_task_list(self):
        Task.objects.create(**self.task_data)
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_update_task(self):
        task = Task.objects.create(**self.task_data)
        url = reverse('task-detail', args=[task.id])
        response = self.client.patch(url,{'title': 'tarefa atualizada'}, format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(Task.objects.get().title, 'tarefa atualizada')
