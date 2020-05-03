from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import ContentHash,HashIdentifier
from .serializers import ContentHashSerializer,HashIdentifierSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# list all content hashes
@csrf_exempt
def listContentHash(request):
	if request.method == 'GET':
		content_hash = ContentHash.objects.all()
		serializer = ContentHashSerializer(content_hash, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ContentHashSerializer(data=data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.errors,status=400)


# content hash details
def detailContentHash(request,arg_hash):
	try:
		content_hash = ContentHash.objects.get(contentHashString=arg_hash)

	except ContentHash.DoesNotExist:
		return HttpResponse(status = 404)
	
	if request.method == 'GET':
		serializer = ContentHashSerializer(content_hash)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ContentHashSerializer(content_hash , data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors,status=400)

# list all identifier
@csrf_exempt
def listIdentifierHash(request):
	if request.method == 'GET':
		identifier_hash = HashIdentifier.objects.all()
		serializer = HashIdentifierSerializer(identifier_hash, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = HashIdentifierSerializer(data=data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data,status=201)
		return JsonResponse(serializer.errors,status=400)

# identifier hash details
@csrf_exempt
def detailIdentifierHash(request,arg_identifierhash):
	try:
		identifier_hash = HashIdentifier.objects.get(hashIdentifierString=arg_identifierhash)

	except HashIdentifier.DoesNotExist:
		return HttpResponse(status = 404)
		# return JsonResponse(data={'found':False})
	
	if request.method == 'GET':
		serializer = HashIdentifierSerializer(identifier_hash)
		return JsonResponse(serializer.data)
		# return JsonResponse(data={'found':True})

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = HashIdentifierSerializer(identifier_hash , data = data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def processHash(request,arg_identifierhash,arg_contenthash):
	# print(arg_contenthash)
	# print(arg_identifierhash)
	try:
		identifier_hash = HashIdentifier.objects.get(hashIdentifierString = arg_identifierhash)
		# a=identifier_hash.id
		# print(a)
		
	except HashIdentifier.DoesNotExist:
		return HttpResponse(status = 404)
	# if request.method == 'GET':
	# 	serializer = HashIdentifierSerializer(identifier_hash)
	# 	return JsonResponse(serializer.data)
	if request.method == 'GET':
		if identifier_hash is not None :
			try:
				content_hash = ContentHash.objects.get(hashIdentifierKey=identifier_hash)
				# print(content_hash)
			except ContentHash.DoesNotExist:
				return HttpResponse(status = 404)
			# serializer = ContentHashSerializer(content_hash)
			# return JsonResponse(serializer.data)
			if str(content_hash) == arg_contenthash :
				print(type(str(content_hash)))
				print(type(arg_contenthash))
				# return JsonResponse(data = {
				# 	'arg_identifierhash':arg_identifierhash,
				# 	'db_identifierhash':identifier_hash,
				# 	'arg_contenthash':arg_contenthash,
				# 	'db_contenthash':content_hash

				# })
				return JsonResponse(data={'found':True})
			else :
				print(type(content_hash))
				print(type(arg_contenthash))
				print('failed')
				return HttpResponse(status = 404)
			
