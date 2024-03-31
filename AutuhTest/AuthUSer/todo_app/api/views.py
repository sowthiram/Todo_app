from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view

from todo_app.models import Task
from todo_app.api.serializers import TaskSerializer
# from todo_app.api.permissions import  UserOnlyAccess


class TaskListAV(APIView):
    # permission_classes = [IsAuthenticated]
    
    def get(self , request):
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class TaskItemAV(APIView):
    
    # permission_classes = [IsAuthenticated]


    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data)
        except:
            return Response({'error': 'Object not found'})
    
    
    def put(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request,pk):
        task = Task.objects.get(pk=pk)
        task.delete()
        return Response({'success': 'Task deleted successfully'})