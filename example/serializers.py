from rest_framework import serializers
from example.models import TestClass

class TestClassSerializer(serializers.ModelSerializer):
	class Meta:
		model = TestClass
		fields = ('id','num')