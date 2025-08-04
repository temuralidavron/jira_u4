from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
    #
    # def has_permission(self, request, view):
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #     return request.user.is_superuser


class IsOwnerProjectOrAssign(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(obj),print(request.user.id),print(obj.project.owner.id),print(obj.assign_to.id)
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        return obj.project.owner == request.user or obj.assign_to == request.user


class TaskMemberPermission(permissions.BasePermission):


    def has_object_permission(self, request, view, obj):
        print(request.user.id,obj.project.members.filter(id=request.user.id).exists())
        if request.method in permissions.SAFE_METHODS:
            return obj.project.members.filter(id=request.user.id).exists()

        return False