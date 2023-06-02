from django.urls import path
from django.conf.urls import url
from .views import PostListView, SharedPostListView, MyNewPostListView, MySharePostListView, PostDetailView, SharedPostDetailView, PostCreateView, PostUpdateView, PostDeleteView, SharedPostCreateView, SharedPostUpdateView, SharedPostDeleteView, LikePost, LikeSharedPost, CommentView, CommentViewSharedPost, UserListView, UserDetailView, AddToFollowing, MyFollowing, MyFollowers, CommentDetailView, CommentUpdateView, CommentDeleteView, SharedCommentDetailView, SharedCommentUpdateView, SharedCommentDeleteView, Notification_View, PostSharesList, LikedUsersList, LikedUsersList_forSharedPosts
from . import views

urlpatterns = [
    path('', views.index, name = "app-index"),        
    path('users/', UserListView.as_view(), name='app-users'),
    path('home/', PostListView.as_view(), name='app-home'),
    path('notifications/', Notification_View.as_view(), name='app-notifications'),
    path('shome/', SharedPostListView.as_view(), name='app-shome'),
    path('mnewhome/', views.MyNewPostListView, name='app-mnewhome'),
    path('msharehome/', views.MySharePostListView, name='app-msharehome'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='app-user-detail'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='app-post-detail'),
    path('sharedpost/<int:pk>/', SharedPostDetailView.as_view(), name='app-sharedpost-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    url(r'^sharedpost/new/(?P<post>\d+)/$', SharedPostCreateView.as_view(), name='sharedpost-create'),
    path('sharedpost/<int:pk>/update/', SharedPostUpdateView.as_view(), name='sharedpost-update'),
    path('sharedpost/<int:pk>/delete/', SharedPostDeleteView.as_view(), name='sharedpost-delete'),
    path('post/<int:pk>/like/', LikePost.as_view(), name='post-like'),
    path('sharedpost/<int:pk>/like/', LikeSharedPost.as_view(), name='sharedpost-like'),
    path('comment/<int:pk>/', CommentView, name='comment-post'),
    path('comment/sharedpost/<int:pk>/', CommentViewSharedPost, name='comment-sharedpost'),
    path('userfollowing/add/<int:pk>/', AddToFollowing, name='add-to-following'),
    path('myfollowing/', MyFollowing, name='my-following'),
    path('myfollowers/', MyFollowers, name='my-followers'),
    path('comment_detail/<int:pk>/', CommentDetailView.as_view(), name='app-comment-detail'),
    path('comment_detail/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment_detail/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('sharedcomment_detail/<int:pk>/', SharedCommentDetailView.as_view(), name='app-sharedcomment-detail'),
    path('sharedcomment_detail/<int:pk>/update/', SharedCommentUpdateView.as_view(), name='app-sharedcomment-update'),
    path('sharedcomment_detail/<int:pk>/delete/', SharedCommentDeleteView.as_view(), name='app-sharedcomment-delete'),
    path('post_shares_list/', PostSharesList, name='post-shares-list'),
    path('liked_users_list/', LikedUsersList, name='liked-users-list'),
    path('liked_users_list_sharedposts/', LikedUsersList_forSharedPosts, name='liked-users-list-sharedposts'),
]
