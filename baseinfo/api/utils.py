from reviews.models import Review
from statistics import mean

def get_rating_avg():
    """
    Returns the average rating of all reviews
    """
    rating_list = []
    reviews = Review.objects.all()
    
    for review in reviews:
        rating_list.append(review.rating)
    
    return round(mean(rating_list), 1)