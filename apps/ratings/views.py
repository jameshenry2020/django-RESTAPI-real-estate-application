from django.contrib.auth import get_user_model
from rest_framework import permissions ,status
from rest_framework.decorators import api_view, permission_classes
from apps.profiles.models import HostAgent
from rest_framework.response import Response

from apps.ratings.models import Rating


User = get_user_model()


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_agent_review(request, agent_id):
    agent_profile=HostAgent.objects.get(id=agent_id)
    #check if the agent is also the person trying to rate himself
    user=agent_profile.profile.user
    if request.user == user:
        msg_response={'message':"you can't rate yourself"}
        return Response(msg_response, status=status.HTTP_403_FORBIDDEN)
    alreadyRated = Rating.objects.filter(agent=agent_profile, client=request.user)
    if alreadyRated.exists():
        msg_response['message']="you have already rated this agent, you can't rate an agent twice"
        return Response(msg_response, status=status.HTTP_400_BAD_REQUEST)
    elif request.data['rating'] == 0:
        msg_response['message'] = "please select a rating from 1 to 5"
        return Response(msg_response, status=status.HTTP_400_BAD_REQUEST)
    else:
        review= Rating.objects.create(
            client=request.user,
            agent=agent_profile,
            rating=request.data['rating'],
            comment=request.data['comment']
        )
        agent_reviews = agent_profile.agent_reviewed.all()
        agent_profile.num_of_reviews=agent_reviews.count()
        agent_profile.save()
        return Response({'message':'Review added successfully'}, status=status.HTTP_200_OK)

    
    
