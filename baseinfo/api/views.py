from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles.models import Business
from offers.models import Offer
from reviews.models import Review
from baseinfo.api.utils import get_rating_avg
class BaseInfoview(APIView):
    def get(self, request, *args, **kwargs):
        """
        Returns base information about the plattform.
        """
        business_profiles_count = Business.objects.count()
        offers_count = Offer.objects.count()
        review_count = Review.objects.count()
        rating_average = get_rating_avg()

        base_info = {
            'review_count': review_count,
            'average_rating': rating_average,
            'business_profile_count': business_profiles_count,
            'offer_count': offers_count,
        }
        
        return Response(base_info ,status=status.HTTP_200_OK)