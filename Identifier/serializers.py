from rest_framework import serializers
from .models import HashIdentifier,ContentHash

class ContentHashSerializer(serializers.ModelSerializer):
	class Meta:
		model = ContentHash
		fields = ['id','contentHashString','hashIdentifierKey']

class HashIdentifierSerializer(serializers.ModelSerializer):
	class Meta:
		model = HashIdentifier
		fields = ['id','hashIdentifierString','activeStatus']