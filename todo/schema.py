from graphene_django import DjangoObjectType
import graphene

from .models import User_Model, Task_Model

class User(DjangoObjectType):
    class Meta:
        model = User_Model

class Task(DjangoObjectType):
    class Meta:
        model = Task_Model


class Query(graphene.ObjectType):
    users = graphene.List(User)
    tasks = graphene.List(Task)

    @graphene.resolve_only_args
    def resolve_users(self):
        return User_Model.objects.all()

    @graphene.resolve_only_args
    def resolve_tasks(self):
        return Task_Model.objects.all()

schema = graphene.Schema(query=Query)