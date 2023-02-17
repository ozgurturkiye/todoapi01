from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import TodoOutputSerializer
from .serializers import TodoInputSerializer

from todos.models import Todo


@api_view(["GET"])
def todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoOutputSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def todo_detail(request, pk):
    todo = get_object_or_404(Todo.objects.all(), pk=pk)
    serializer = TodoOutputSerializer(todo)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def todo_add(request):
    serializer = TodoInputSerializer(data=request.data)

    if serializer.is_valid():
        serializer.validated_data["owner"] = request.user
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def todo_change(request, pk):
    todo = get_object_or_404(Todo.objects.all(), pk=pk)

    if todo.owner == request.user:
        serializer = TodoInputSerializer(todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(
        {"message": "You can only update your todo"}, status=status.HTTP_403_FORBIDDEN
    )


@api_view(["DELETE"])
def todo_delete(request, pk):
    # More restrictive query
    todo = get_object_or_404(Todo.objects.filter(owner=request.user), pk=pk)

    if todo.owner == request.user:
        todo.delete()
        return Response(
            {"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT
        )

    return Response(
        {"message": "You can only delete your todo"}, status=status.HTTP_403_FORBIDDEN
    )
