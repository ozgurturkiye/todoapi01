from rest_framework import serializers

from todos.models import Todo


class TodoOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "body", "photo", "owner"]


class TodoInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["title", "body", "photo"]
