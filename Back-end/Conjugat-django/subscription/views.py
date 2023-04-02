from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RetrieveStatusSerializer, NewStripeCustomerSerializer, \
    NewCoinbaseCustomerSerializer, NewPaypalCustomerSerializer, SuccessSerializer
from .validations import *



''' Routes '''
class GetRoutes(APIView):
    def get(self, request):
        routes = [
            {
                'Endpoint': '/process/',
                'method': 'POST',
                'body': {'body': ""},
                'description': 'Post data and retrieve payment details'
            },
            {
                'Endpoint': '/success/',
                'method': 'POST',
                'body': {'body': ""},
                'description': 'Unsubscribes to the newsletter'
            },
        ]
        return Response(routes)


''' Process '''
class RetrieveStatus(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_return_urls = validate_return_urls(data)
        if validated_return_urls[0] == False:
            return Response(data=validated_return_urls[1], status=validated_return_urls[2])

        context = {'user': request.user}
        serializer = RetrieveStatusSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.retrieve_status(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])

class NewStripeCustomer(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_customer_id = validate_customer_id(data)
        if validated_customer_id[0] == False:
            return Response(data=validated_customer_id[1], status=validated_customer_id[2])

        context = {'user': request.user}
        serializer = NewStripeCustomerSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.create_stripe_customer(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])

class NewPaypalCustomer(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_subscriber_id = validate_subscriber_id(data)
        if validated_subscriber_id[0] == False:
            return Response(data=validated_subscriber_id[1], status=validated_subscriber_id[2])

        context = {'user': request.user}
        serializer = NewPaypalCustomerSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.create_paypal_customer(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])

class NewCoinbaseCustomer(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        validated_charge_url = validate_charge_url(data)
        if validated_charge_url[0] == False:
            return Response(data=validated_charge_url[1], status=validated_charge_url[2])

        context = {'user': request.user}
        serializer = NewCoinbaseCustomerSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.create_coinbase_customer(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])


'''Success'''
class Success(APIView):
    permission_classes = (permissions.AllowAny,)
    # authentication_classes = (SessionAuthentication,)
    def post(self, request):
        data = request.data
        context = {'user': request.user}
        serializer = SuccessSerializer(data=data, context=context)
        if serializer.is_valid(raise_exception=True):
            response = serializer.return_premium_status(data)
            if response[1] == True:
                return Response(data=response[0], status=status.HTTP_200_OK)
            return Response({'error':response[0]}, status=response[2])