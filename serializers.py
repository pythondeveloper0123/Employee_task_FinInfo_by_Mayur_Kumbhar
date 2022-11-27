from rest_framework import serializers
from .models import EmployeeQualification, EmployeeWorkExperience, EmployeeProjects, Employee, EmployeeAddress
from drf_writable_nested import WritableNestedModelSerializer


class EmployeeAddressModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeAddress
        fields = ('hno', 'street', 'city', 'state', )

    def create(self, validated_data):
        return EmployeeAddress.objects.create(**validated_data)


class EmployeeWorkExperienceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeWorkExperience
        fields = ('companyName', 'fromDate', 'toDate', 'address', )

    def create(self, validated_data):
        return EmployeeWorkExperience.objects.create(**validated_data)


class EmployeeQualificationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeQualification
        fields = ('qualificationName', 'percentage', )

    def create(self, validated_data):
        return EmployeeQualification.objects.create(**validated_data)


class EmployeeProjectsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProjects
        fields = ('title', 'description', )

    def create(self, validated_data):
        return EmployeeProjects.objects.create(**validated_data)


class EmployeeModelSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    EmployeeAddress = EmployeeAddressModelSerializer()
    EmployeeWorkExperience = EmployeeWorkExperienceModelSerializer(many=True)
    EmployeeQualification = EmployeeQualificationModelSerializer(many=True)
    EmployeeProjects = EmployeeProjectsModelSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('regid', 'name', 'email', 'age', 'gender', 'phoneNo',
                  'EmployeeAddress', 'EmployeeWorkExperience', 'EmployeeQualification', 'EmployeeProjects', 'photo')
