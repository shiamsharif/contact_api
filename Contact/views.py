from rest_framework.viewsets import ModelViewSet

from Contact.models import Contact
from Contact.serializers import ContactSerializer

# Create your views here.
class ContactViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    
