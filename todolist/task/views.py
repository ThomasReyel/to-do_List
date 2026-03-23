from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer
from django.db import models

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all().order_by('-id')

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.query_params.get('search', None)

        if search_term:
            queryset = queryset.filter(
                models.Q(title__icontains=search_term) |
                models.Q(description__icontains=search_term)
            )
        return queryset


    
