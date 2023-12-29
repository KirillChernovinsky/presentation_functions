from django.urls import path
from .views import GetNews, CreatePerson, CreateNews, UpdateNews, DeletePost

urlpatterns = [
    path('', GetNews.as_view(), name='home'),
    path('create/', CreateNews.as_view(), name='create'),
    path('update/<int:pk>', UpdateNews.as_view(), name='update'),
    path('delete/<int:pk>', DeletePost.as_view(), name="delete"),
    #path('popular_posts', popular_posts, name='popular_posts'),
    #path('popular/<int:id>', popular, name='popular'),
    #path('lastpost/', lastpost, name='lastpost'),

    #path('vhod/', vhod, name='vhod'),
    path('registr/', CreatePerson.as_view(), name='registr'),
]