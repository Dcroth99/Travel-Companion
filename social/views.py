from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import TravelDiary, Review


@login_required
def travel_diary(request, username):
    user = get_object_or_404(User, username=username)
    diary = get_object_or_404(TravelDiary, user=user)
    reviews = Review.objects.filter(user=user).order_by('-created_at')
    
    return render(request, 'travel_diary.html', {
        'diary': diary,
        'reviews': reviews,
    })

