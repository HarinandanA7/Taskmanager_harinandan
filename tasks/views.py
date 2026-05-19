from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer

from users.models import User

from notifications.utils import send_task_email

class TaskCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        if not request.user.can_create_task:

            return Response({
                'error': 'Task creation disabled'
            })

        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():

            task = serializer.save(
                created_by=request.user
            )

            assigned_users = request.data.get(
                'assigned_users',
                []
            )

            for user_id in assigned_users:

                user = User.objects.get(id=user_id)

                task.assigned_users.add(user)

                send_task_email(
                    user.email,
                    task.title
                )

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)