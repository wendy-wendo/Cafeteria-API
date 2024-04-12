from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ItemSerializer, CategorySerializer
from .models import Item, Category

# Create your views here.
@api_view(['GET'])
def index(request):
    api_urls = {
        'Items': '/items/',
        'Item': '/items/<int:pk>/',
        'Create': '/item-create/',
        'Update': '/item-update/<int:pk>/',
        'Delete': '/item-delete/<int:pk>/',
        'Categories': '/categories/',
        'CategoryAdd': '/category_create/',
        'CategoryDelete': '/category_delete/<int:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def item(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def item_create(request):
    serializer = ItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def item_update(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(instance=item, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def item_delete(request, pk):
    item = Item.objects.get(id=pk)

    item.delete()

    return Response("Item successfully deleted.")


@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def category_create(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def category_delete(request, pk):
    category = Category.objects.get(id=pk)

    category.delete()

    return Response("Category successfully deleted.")