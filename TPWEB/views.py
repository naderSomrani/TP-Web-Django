from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from .serializers import *
# Create your views here.


class CustomersAPI(APIView):
    parser_class = (FileUploadParser,)

    def get(self, request):
        try:
            id = request.query_params['id']
        except:
            id = None
        if id is None:
            serializer = CustomerSerializer(Customer.objects.all(),
                                      many=True)
        else:
            serializer = CustomerSerializer(Customer.objects.filter(pk=id),
                                            many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print(request.data)
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        pk = request.query_params['id']
        customer = Customer.objects.get(pk=pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.query_params['id']
        customer = Customer.objects.get(pk=pk)
        customer.delete()
        return Response("Customer deleted", status=status.HTTP_204_NO_CONTENT)
