from rest_framework import permissions, status
from .models import EnquiryRequest
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from apps.properties.models import Property
from django.conf import settings
from django.core.mail import send_mail


DEFAULT_FROM_EMAIL = settings.DEFAULT_FROM_EMAIL




@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def send_enquiry_message(request, property_id):
    data= request.data
    property = Property.objects.get(id=property_id)
    
    try:
        email_subject=f"Enquiry for {property.title} at {property.city}"
        sender_name = data['names']
        sender_email = data['email']
        sender_phone = data['phone']
        message = data['message']
        recipient_list = [DEFAULT_FROM_EMAIL]

        send_mail(subject=email_subject, message=message, from_email=sender_email, recipient_list=recipient_list, fail_silently=True)
        enquiry = EnquiryRequest.objects.create(property=property, names=sender_name, email=sender_email, phone=sender_phone, message=message)
        return Response({'success':'your enquiry was submitted sucessfully an agent will reachout to you soon'}, status=status.HTTP_200_OK)

    except:
        return Response({'fail':'enquiry was not sent please try again'})





