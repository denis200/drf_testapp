
from django.forms import model_to_dict
from rest_framework import generics,viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAdminUser

from women.permissions import IsAdminOrReadOnlyPermission, IsOwnerOrReadOnly

from .models import Category, Women
from .serializers import WomenSerializer


# class WomenViewSet(viewsets.ModelViewSet):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

#     def get_queryset(self):
#         return super().get_queryset()

#     @action(methods=['get'],detail = True)
#     def category(self,request,pk = None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats':cats.name})
    

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsOwnerOrReadOnly]


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = [IsAdminOrReadOnlyPermission]
