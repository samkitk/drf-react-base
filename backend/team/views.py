from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Member
from .serializers import MemberSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the team index.")


@api_view(["GET"])
def teamListView(request):
    if request.method == "GET":
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data)

# class teamListView(APIView):
#     serializer_class = MemberSerializer
#     queryset = Member.objects.all()

# Create your views here.
