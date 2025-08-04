from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from account.serializers import CustomUserSerializer
from task.models import Project, Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    memebers = serializers.SerializerMethodField()
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'assign_to',
            'project',
            'owner',
            'memebers',
            'created_at',
            'updated_at',
        ]

    def get_owner(self, obj):
        project = obj.project
        if project:
            owner = project.owner
            if owner:
                username=owner.username
                return username

        return None


    def get_memebers(self, obj):
        project = obj.project
        if project:
            usernames = project.members.values_list('username', flat=True)
            return list(usernames)
        return None

class TaskProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'assign_to',
            'project',
        ]

    def create(self, validated_data):
        return Task.objects.create(**validated_data)


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'status',
            'assign_to',
            'project',

        ]






class BaseProjectSerializer(ModelSerializer):
    # tasks = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'owner',
            'members',
            # 'tasks',
            'created_at',
            'updated_at',
        ]
        extra_kwargs = {
            'created_at': {'read_only': True},
        }

    # def get_tasks(self, obj):
    #     tasks = obj.task_project.all()
    #     return TaskProjectSerializer(tasks, many=True).data

class ProjectCreateSerializer(BaseProjectSerializer):
    # owner=serializers.HiddenField(default='user',source='owner')
    class Meta(BaseProjectSerializer.Meta):
        extra_kwargs = {
            'created_at': {'read_only': True},
            'id': {'read_only': True},

        }


# for query opt

class TaskQuerySerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.only('name'))

# project= BaseProjectSerializer(read_only=True)
#     project_n=serializers.CharField()
    project_nn=serializers.CharField(source='project.name', read_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'assign_to',
            'project',
            # 'project_n',
            'project_nn',
        ]




    # def get_project_n(self, obj):
    #     project = obj.project
    #     if project:
    #         name=project.name
    #         return name

    # def get_project_n(self, obj):
    #     name=Task.objects.select_related('project')
    #     serializer=Project(name, many=True)
    #     return serializer.data
class TaskQSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
        ]

class ProjectQuerySerializer(BaseProjectSerializer):
    # task=serializers.ListField(child=serializers.CharField())
    # tasks = TaskSerializer(many=True, read_only=True)
    # tasks = TaskQSerializers(source='task_project', many=True, read_only=True)
    # tasks=serializers.CharField(source="task_project.title", read_only=True)
    tasks = serializers.ListField(child=serializers.CharField(), source='task_titles')



    class Meta:
        model = Project
        fields = [
            'id',
            'name',
            'description',
            'owner',
            'members',
            'tasks',
        ]