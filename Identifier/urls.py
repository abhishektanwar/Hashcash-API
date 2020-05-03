from django.urls import path
from .views import listContentHash,detailContentHash,listIdentifierHash,detailIdentifierHash,processHash

urlpatterns = [
    path('listcontenthash/',listContentHash),
    path('detailcontenthash/<slug:arg_hash>',detailContentHash),
    path('listidentifierhash/',listIdentifierHash),
    path('detailidentifierhash/<slug:arg_identifierhash>',detailIdentifierHash),
    path('processHash/<slug:arg_identifierhash>/<slug:arg_contenthash>',processHash)
]

