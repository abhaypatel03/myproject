from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Tweet
from .forms import TweetForm


# Home Page
def index(request):
    return render(request, "myapp/index.html")


# Tweet List
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, "myapp/tweet_list.html", {"tweets": tweets})


# Create Tweet
@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
        else:
            print(form.errors)   # 👈 ADD THIS
    else:
        form = TweetForm()

    return render(request, 'myapp/tweet_form.html', {'form': form})

# Tweet Detail
def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, "myapp/tweet_detail.html", {"tweet": tweet})


# Edit Tweet
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)

    return render(request, 'myapp/tweet_form.html', {'form': form})


# Delete Tweet
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)

    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')

    return render(request, 'myapp/tweet_confirm_delete.html', {'tweet': tweet})


# Register User
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()   # ✅ correct
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
    