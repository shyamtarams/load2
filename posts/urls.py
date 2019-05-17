from django.urls import path

from .views import HomePageView, CreatePostView ,CreateCommentView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'),
    path('comment/',CreateCommentView.as_view(), name='add_comment')
]
