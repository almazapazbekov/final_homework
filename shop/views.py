from django.shortcuts import render
from rest_framework import viewsets, authentication
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Profile, Item, Order, Category
from .permissions import IsAuthorPermission, IsSenderOrReadOnly, IsBuyerOrReadOnly, ReadOnlyPermission, \
    OrderOrReadOnly
from .serializers import CategorySerializer, ItemSerializer, OrderSerializer


class CategoryCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication, SessionAuthentication]

    permission_classes = [IsSenderOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorPermission, ]


class ItemCreateListApiView(ListCreateAPIView):
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]

    permission_classes = [IsSenderOrReadOnly, ]

    def get_queryset(self):
        category = self.kwargs['pk']
        return Item.objects.filter(category=category)

    def perform_create(self, serializer):
        category = Category.objects.filter(pk=self.kwargs['pk']).first()
        serializer.save(category=category)
        serializer.save(profile=self.request.user)


class ItemRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    # queryset = Item.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsAuthorPermission, ]


# ===================================== СПРОСИТЬ
    def get_queryset(self):
        print(self.kwargs)
        print(Item.objects.filter(id=self.kwargs['id']))
        return Item.objects.filter(id=self.kwargs['id'])


class OrderCreateApiView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsBuyerOrReadOnly, ]


class OrderRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    permission_classes = [IsBuyerOrReadOnly, ]
    # permission_classes = [IsAuthorPermission, ]
