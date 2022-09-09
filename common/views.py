from rest_framework import status
from rest_framework.generics import get_object_or_404

from common.models import Task
from rest_framework.views import APIView
from rest_framework.response import Response

from common.serializers import TaskSerializer


class TasksListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response({'tasks': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        task = request.data.get('task')
        serializer = TaskSerializer(data=task)
        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
            return Response({'success': 'Task "{}" created successfully.'.format(task_saved)}, status=status.HTTP_200_OK)


class TaskDetailView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task.objects.all(), pk=pk)
        serializer = TaskSerializer(instance=task)
        return Response({'task': serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = get_object_or_404(Task.objects.all(), pk=pk)
        data = request.data.get('task')
        serializer = TaskSerializer(instance=task, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            task_saved = serializer.save()
            return Response({'success': 'Task "{}" created successfully.'.format(task_saved)}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        task = get_object_or_404(Task.objects.all(), pk=pk)
        task.delete()
        return Response({"message": "Task with id '{}' has been deleted.".format(pk)}, status=status.HTTP_200_OK)

