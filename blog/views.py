from django.shortcuts import render
from django.http import Http404
from datetime import date

blogs = [
    {
        "title": "Mountain Hiking",
        "slug": "moutain-hiking",
        "excerpt" : "Mountain hiking offers more than just breathtaking views — it’s a journey of endurance, discovery, and connection with nature. From preparing the right gear to conquering challenging trails, every step brings both physical rewards and mental clarity",
        "image_url": "mountain_hiking.jpg",
        "description": "Mountain hiking is an outdoor activity that combines physical endurance with the beauty of nature. It involves trekking along trails that ascend into mountainous terrain, often leading to breathtaking views, fresh air, and unique ecosystems. Hikers prepare with proper gear, navigation tools, and safety measures to tackle varying elevations, weather conditions, and trail difficulties. Beyond fitness, mountain hiking offers mental rejuvenation, a sense of adventure, and an opportunity to connect deeply with the natural world.",
        "author" : "Vivek Dhengale",
        "updated_at": date.today(),
    },
    {
        "title": "Nature at its Best",
        "slug": "nature-at-its-best",
        "excerpt" : "Experience nature at its finest — from towering peaks and lush forests to tranquil lakes and endless skies, every moment outdoors brings peace, beauty, and inspiration",
        "image_url": "nature_at_its_best.jpg",
        "description": "Nature at its best reveals the harmony and beauty of the natural world. From majestic mountains and dense forests to serene rivers and open meadows, it offers a sanctuary away from the pace of modern life. Experiencing nature in its purest form awakens the senses, restores balance, and inspires appreciation for the environment. Whether through hiking, camping, or simply pausing to admire a sunset, these moments remind us of the simplicity and grandeur that only nature can provide.",
        "author" : "Vivek Dhengale",
        "updated_at": date.today(),
    },
    {
        "title": "Programming is Great",
        "slug": "programming-is-great",
        "excerpt" : "Programming is great because it transforms ideas into reality — from building apps to solving everyday problems with code.",
        "image_url": "programming_great.jpg",
        "description": "Mountain hiking is an outdoor activity that combines physical endurance with the beauty of nature. It involves trekking along trails that ascend into mountainous terrain, often leading to breathtaking views, fresh air, and unique ecosystems. Hikers prepare with proper gear, navigation tools, and safety measures to tackle varying elevations, weather conditions, and trail difficulties. Beyond fitness, mountain hiking offers mental rejuvenation, a sense of adventure, and an opportunity to connect deeply with the natural world.",
        "author" : "Vivek Dhengale",
        "updated_at": date.today(),
    }
]

def index(request):
    recent_blogs = blogs
    return render(request,"blog/index.html",{
        "recent_blogs" : recent_blogs
    })

def posts_list(request):
    return render(request,"blog/all_posts.html")

def individual_post(request,slug):
    for slugs in blogs:
        if slugs["slug"] == slug:
            return render(request,"blog/detail_post.html",{
                "title":slugs["title"],
                "description":slugs["description"],
                "author_name":slugs["author"],
            })
    else:
        raise Http404()