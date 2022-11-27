from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class EmployeeGetPostAPIView(APIView):
    def get(self, request):
        try:
            employee = Employee.objects.all()
        except Employee.DoesNotExist:
            return Response(data={'msg': 'Employee not found', 'success': 'false', 'employee': []},
                            status=status.HTTP_404_NOT_FOUND)
        if not employee:
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        serializer = EmployeeModelSerializer(employee, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            serializer = EmployeeModelSerializer(data=request.data)
        except:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={'msg': 'Employee created successfully',
                      'success': 'true', 'empid': request.data.get('regid')},
                status=status.HTTP_201_CREATED)
        else:
            if Employee.objects.filter(email=request.data.get('email')):
                return Response(data={'msg': 'Employee Already Exist', 'success': 'false'}, status=status.HTTP_200_OK)
            else:
                return Response(data={'msg': 'Invalid Body Request', 'success': 'false'},
                                status=status.HTTP_404_NOT_FOUND)


class EmployeeGetPutDeleteAPIView(APIView):
    def get(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(data={'msg': 'Employee Not Found', 'success': 'false', 'employee': []},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeModelSerializer(employee)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk=None):
        if pk != '':
            try:
                employee = Employee.objects.get(
                    pk=pk)
            except:
                return Response(data={'msg': 'Employee with this regid Not Found', 'success': 'false'},
                                status=status.HTTP_404_NOT_FOUND)
            employee.delete()
            return Response(data={'msg': 'Employee deleted successfully!', 'success': 'true'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'msg': 'Employee deletion failed!', 'success': 'false'}, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        try:
            employee = Employee.objects.get(
                pk=pk)
        except Employee.DoesNotExist:
            return Response(data={'msg': 'no Employee found with this regid'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeModelSerializer(
            data=request.data, instance=employee)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msg': 'Employee details updated successfully', 'success': 'true'},
                            status=status.HTTP_200_OK)
        else:
            if Employee.objects.filter(email=request.data.get('email')):
                return Response(data={'msg': 'Employee details updation failed', 'success': 'false'},
                                status=status.HTTP_200_OK)
            else:
                return Response(data={'msg': 'invalid body request', 'success': 'false'},
                                status=status.HTTP_404_NOT_FOUND)
