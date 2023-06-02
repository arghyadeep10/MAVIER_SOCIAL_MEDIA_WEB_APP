from django.shortcuts import render, get_object_or_404
from mavier.models import Post, Like, Comment, SharedPost, Like_for_SharedPost, Comment_forSharedPost, Notifications
from users.models import UserProfile, UserFollowing, UserFollowers
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.paginator import Paginator

#function based view
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('app-home'))
    
    return render(request, "mavier/index.html")

#class based view (superior than function based view. Has lots of built in functionality)
# @login_required
@method_decorator(login_required, name='dispatch')
class PostListView(ListView):
    template_name='mavier/home.html' #this tells the ListView which template to refer to
    context_object_name = 'posts' #this is the variable that will be passed to the template, over which the template can loop over.
    ordering = ['-date_posted']
    paginate_by = 7

    def get_queryset(self):
        current_user = self.request.user
        pop = UserFollowers.objects.filter(followers=current_user).values('userprofile')

        array = []
        lister = []

        for i in pop:
            array.append(i['userprofile'])

        userprofiles = UserProfile.objects.filter(pk__in=array).values('user')

        for j in userprofiles:
            lister.append(j['user'])

        users = User.objects.filter(pk__in=lister)

        posts_of_interest = Post.objects.filter(author__in=users).order_by('-date_posted')

        current_user = self.request.user

        for current_post in posts_of_interest:
            important_likes = Like.objects.filter(liker=current_user, post=current_post)
            counter = len(important_likes)

            if counter == 0:
                # liked = False
                current_post.temp_like_flag = 0
            elif counter == 1:
                # liked = True  
                current_post.temp_like_flag = 1

        return posts_of_interest

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)   

        current_user = self.request.user
        pop = UserFollowers.objects.filter(followers=current_user).values('userprofile')

        array = []
        lister = []

        for i in pop:
            array.append(i['userprofile'])

        userprofiles = UserProfile.objects.filter(pk__in=array).values('user')

        for j in userprofiles:
            lister.append(j['user'])

        users = User.objects.filter(pk__in=lister)

        posts_of_interest = Post.objects.filter(author__in=users).order_by('-date_posted')

        my_p_counter = posts_of_interest.count()
        context.update({
            'my_p_counter': my_p_counter,
        })
        return context

@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model=Post
    #here since we are not specifically mentioning the template that we wish to load, hence here Django will look for it at its default location: <mavier>/<model>_<viewtype>.html

    #Here model = post and viewtype = detail

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)

        liked = False
        current_post = self.get_object()
        current_user = self.request.user

        important_likes = Like.objects.filter(liker=current_user, post=current_post)
        counter = len(important_likes)

        if counter == 0:
            liked = False
        elif counter == 1:
            liked = True    

        context.update({
            'comments': Comment.objects.filter(post=self.get_object()),
            'comment_count': self.get_object().comment_counter,
            'liked': liked,
        })
        return context

@method_decorator(login_required, name='dispatch')
class SharedPostDetailView(DetailView):
    model=SharedPost
    #here since we are not specifically mentioning the template that we wish to load, hence here Django will look for it at its default location: <mavier>/<model>_<viewtype>.html

    #Here model = sharedpost and viewtype = detail

    def get_context_data(self, **kwargs):
        context = super(SharedPostDetailView, self).get_context_data(**kwargs)

        liked = False
        current_post = self.get_object()
        current_user = self.request.user

        important_likes = Like_for_SharedPost.objects.filter(liker=current_user, post=current_post)
        counter = len(important_likes)

        if counter == 0:
            liked = False
        elif counter == 1:
            liked = True    

        context.update({
            'comments': Comment_forSharedPost.objects.filter(post=self.get_object()),
            'comment_count': self.get_object().comment_counter,
            'liked': liked,
        })
        return context


@method_decorator(login_required, name='dispatch')
class SharedPostListView(ListView):
    # model=SharedPost
    template_name='mavier/shome.html' #this tells the ListView which template to refer to
    context_object_name = 'shared_posts' #this is the variable that will be passed to the template, over which the template can loop over.
    ordering = ['-date_posted']
    paginate_by = 7

    def get_queryset(self):
        current_user = self.request.user
        pop = UserFollowers.objects.filter(followers=current_user).values('userprofile')

        array = []
        lister = []

        for i in pop:
            array.append(i['userprofile'])

        userprofiles = UserProfile.objects.filter(pk__in=array).values('user')

        for j in userprofiles:
            lister.append(j['user'])

        users = User.objects.filter(pk__in=lister)

        sharedposts_of_interest = SharedPost.objects.filter(author__in=users).order_by('-date_posted')

        current_user = self.request.user

        for current_post in sharedposts_of_interest:
            important_likes = Like_for_SharedPost.objects.filter(liker=current_user, post=current_post)
            counter = len(important_likes)

            if counter == 0:
                # liked = False
                current_post.temp_like_flag = 0
            elif counter == 1:
                # liked = True  
                current_post.temp_like_flag = 1

        return sharedposts_of_interest

    def get_context_data(self, **kwargs):
        context = super(SharedPostListView, self).get_context_data(**kwargs)   

        current_user = self.request.user
        pop = UserFollowers.objects.filter(followers=current_user).values('userprofile')

        array = []
        lister = []

        for i in pop:
            array.append(i['userprofile'])

        userprofiles = UserProfile.objects.filter(pk__in=array).values('user')

        for j in userprofiles:
            lister.append(j['user'])

        users = User.objects.filter(pk__in=lister)

        sharedposts_of_interest = SharedPost.objects.filter(author__in=users).order_by('-date_posted')

        my_p_counter = sharedposts_of_interest.count()

        context.update({
        'my_p_counter': my_p_counter,
        })
        return context




# @method_decorator(login_required, name='dispatch')
# class MyNewPostListView(ListView):
#     model=Post
#     template_name='mavier/mnewhome.html' #this tells the ListView which template to refer to
#     context_object_name = 'posts' #this is the variable that will be passed to the template, over which the template can loop over.
#     ordering = ['-date_posted']
    

@login_required
def MyNewPostListView(request):
    
    po = Post.objects.filter(author = request.user).order_by('-date_posted')
    mypost_counter = len(po)

    current_user = request.user

    for current_post in po:
        important_likes = Like.objects.filter(liker=current_user, post=current_post)
        counter = len(important_likes)

        if counter == 0:
            # liked = False
            current_post.temp_like_flag = 0
        elif counter == 1:
            # liked = True  
            current_post.temp_like_flag = 1

    paginator = Paginator(po, 7) # Show 7 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'posts' : po,
        'counter' : mypost_counter,
        'page_obj': page_obj
    }

    return render(request, "mavier/mnewhome.html", context)

@login_required
def MySharePostListView(request):
    
    sh_po = SharedPost.objects.filter(author = request.user).order_by('-date_posted')
    myshpost_counter = len(sh_po)

    current_user = request.user

    for current_post in sh_po:
        important_likes = Like_for_SharedPost.objects.filter(liker=current_user, post=current_post)
        counter = len(important_likes)

        if counter == 0:
            # liked = False
            current_post.temp_like_flag = 0
        elif counter == 1:
            # liked = True  
            current_post.temp_like_flag = 1

    paginator = Paginator(sh_po, 7) # Show 7 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'shared_posts' : sh_po,
        'counter' : myshpost_counter,
        'page_obj': page_obj
    }

    return render(request, "mavier/msharehome.html", context)

@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.comment_counter = 0
        form.instance.like_counter = 0
        form.instance.share_counter = 0
        return super().form_valid(form)



@method_decorator(login_required, name='dispatch')        
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name='mavier/post_update_form.html' #this tells the ListView which template to refer to
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

@method_decorator(login_required, name='dispatch')
class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False

    success_url = '/home'


@method_decorator(login_required, name='dispatch')
class SharedPostCreateView(CreateView):
    model = SharedPost
    fields = ['title', 'content']
    template_name='mavier/sharedpost_create.html' #this tells the ListView which template to refer to

    def get_context_data(self, **kwargs):
        context = super(SharedPostCreateView, self).get_context_data(**kwargs)
        context.update({
            'PostToBeShared': Post.objects.get(pk=self.kwargs['post']),
        })
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = Post.objects.get(pk=self.kwargs['post'])
        post.share_counter += 1
        post.save()
        #now lets add a notification for the user whose post got shared
        user_to_be_notified = post.author
        postid = post.id
        noti = Notifications(user=user_to_be_notified, notification_type='Post_Shared', notification_message=f"'{self.request.user}' shared your post '{post.title}'", link="url 'app-post-detail'", link_variable=postid)
        noti.save()
        form.instance.shared_post = post
        form.instance.comment_counter = 0
        form.instance.like_counter = 0
        return super().form_valid(form)

    success_url = '/home'


@method_decorator(login_required, name='dispatch')
class SharedPostUpdateView(UserPassesTestMixin, UpdateView):
    model = SharedPost
    fields = ['title', 'content']
    template_name='mavier/sharedpost_update.html' #this tells the ListView which template to refer to

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            return True
        return False    


@method_decorator(login_required, name='dispatch')
class SharedPostDeleteView(UserPassesTestMixin, DeleteView):
    model = SharedPost

    def test_func(self):
        post = self.get_object()

        if self.request.user == post.author:
            if self.request.method == 'POST': #this prevents the below chunk of code to run twice during the GET and POST requests
                post.shared_post.share_counter -= 1
                post.shared_post.save()
            return True
        return False

    success_url = '/home'


# @method_decorator(login_required, name='dispatch')
# class LikePost(CreateView):
#     model = Like
#     fields = []
#     template_name='mavier/like.html' #this tells the ListView which template to refer to

#     def form_valid(self, form):
#         form.instance.liker = self.request.user
#         post_extract = self.get_object()
#         form.instance.post = post_extract
#         if self.request.method == 'POST': #this prevents the below chunk of code to run twice during the GET and POST requests
#             post_extract.like_counter += 1 
#             post_extract.save()
#         return super().form_valid(form)

#     success_url = '/home'


@method_decorator(login_required, name='dispatch')
class LikePost(UpdateView):
    model = Post
    fields = []
    template_name='mavier/like.html' #this tells the ListView which template to refer to

    def form_valid(self, form):
        post_extract = self.get_object()
        existing_likes = Like.objects.filter(liker=self.request.user, post=post_extract)
        count_existing_likes = len(existing_likes)
        if self.request.method == 'POST' and count_existing_likes == 0: #the first criteria prevents the below chunk of code to run twice during the GET and POST requests and the second criteria prevents the same user from clicking the like button again and again. Now if the user clicks the like button more than once, nothing happens.
            form.instance.like_counter += 1 
            form.instance.save()
            like_ob = Like(liker=self.request.user,post=post_extract)
            like_ob.save() 
            messages.success(self.request, f"Post Liked Successfully !")   

            #now lets add a notification for the user whose post got liked
            user_to_be_notified = post_extract.author
            postid = post_extract.id
            noti = Notifications(user=user_to_be_notified, notification_type='Post_Like', notification_message=f"'{self.request.user}' liked your post '{post_extract.title}'", link="url 'app-post-detail'", link_variable = postid)
            noti.save()
        elif self.request.method == 'POST' and count_existing_likes != 0:    
            form.instance.like_counter -= 1
            form.instance.save()
            like_ob = Like.objects.get(liker=self.request.user,post=post_extract) 
            like_ob.delete()        
            messages.success(self.request, f"Post Unliked Successfully")   

        return super().form_valid(form)

    # success_url = '/home'
        return HttpResponseRedirect(reverse('app-post-detail', args=[str(pk)]))


@method_decorator(login_required, name='dispatch')
class LikeSharedPost(UpdateView):
    model = SharedPost
    fields = []
    template_name='mavier/like_sharedpost.html' #this tells the ListView which template to refer to

    def form_valid(self, form):
        post_extract = self.get_object()
        existing_likes = Like_for_SharedPost.objects.filter(liker=self.request.user, post=post_extract)
        count_existing_likes = len(existing_likes)
        if self.request.method == 'POST' and count_existing_likes == 0: #the first criteria prevents the below chunk of code to run twice during the GET and POST requests and the second criteria prevents the same user from clicking the like button again and again. Now if the user clicks the like button more than once, nothing happens.
            form.instance.like_counter += 1 
            form.instance.save()
            like_ob = Like_for_SharedPost(liker=self.request.user,post=post_extract)
            like_ob.save()   
            messages.success(self.request, f"Post Liked Successfully !")   
            #now lets add a notification for the user whose post got liked
            user_to_be_notified = post_extract.author
            postid = post_extract.id
            noti = Notifications(user=user_to_be_notified, notification_type='SharedPost_Like', notification_message=f"'{self.request.user}' liked your post '{post_extract.title}'", link="url 'app-sharedpost-detail'", link_variable = postid)
            noti.save()
        elif self.request.method == 'POST' and count_existing_likes != 0:             
            form.instance.like_counter -= 1
            form.instance.save()
            like_ob = Like_for_SharedPost.objects.get(liker=self.request.user,post=post_extract) 
            like_ob.delete()        
            messages.success(self.request, f"Post Unliked Successfully")   

        return super().form_valid(form)

    # success_url = '/home'
        return HttpResponseRedirect(reverse('app-sharedpost-detail', args=[str(pk)]))


def CommentView(request, pk):
    post_obt = get_object_or_404(Post, id=request.POST.get('post_id'))
    post_obt.comment_counter += 1
    post_obt.save()

    comment_content_obtained = request.POST.get('content')

    our_comment = Comment(post=post_obt, commenter=request.user, comment_content=comment_content_obtained)
    our_comment.save()

    #now lets add a notification for the user whose post got commented
    user_to_be_notified = post_obt.author
    postid = post_obt.id
    noti = Notifications(user=user_to_be_notified, notification_type='Post_Comment', notification_message=f"'{request.user}' commented on your post '{post_obt.title}'", link="url 'app-post-detail'", link_variable = postid)
    noti.save()

    return HttpResponseRedirect(reverse('app-post-detail', args=[str(pk)]))


def CommentViewSharedPost(request, pk):
    post_obt = get_object_or_404(SharedPost, id=request.POST.get('post_id'))
    post_obt.comment_counter += 1
    post_obt.save()

    comment_content_obtained = request.POST.get('content')

    our_comment = Comment_forSharedPost(post=post_obt, commenter=request.user, comment_content=comment_content_obtained)
    our_comment.save()

    #now lets add a notification for the user whose post got commented
    user_to_be_notified = post_obt.author
    postid = post_obt.id
    noti = Notifications(user=user_to_be_notified, notification_type='SharedPost_Comment', notification_message=f"'{request.user}' commented on your post '{post_obt.title}'", link="url 'app-sharedpost-detail'", link_variable = postid)
    noti.save()

    return HttpResponseRedirect(reverse('app-sharedpost-detail', args=[str(pk)]))


@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model=User
    template_name='mavier/users.html' #this tells the ListView which template to refer to
    context_object_name = 'users' #this is the variable that will be passed to the template, over which the template can loop over.
    ordering = ['username']


@method_decorator(login_required, name='dispatch')
class UserDetailView(DetailView):
    model=User
    template_name="mavier/user_detail.html"

    #Here model = post and viewtype = detail
    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)

        followed = False
        display_user = self.get_object()
        current_user = self.request.user

        # important_follow = Like.objects.filter(liker=current_user, post=current_post)

        pop = UserFollowers.objects.filter(followers=current_user).values('userprofile')

        array = []

        for i in pop:
            array.append(i['userprofile'])

        userprofiles = UserProfile.objects.filter(pk__in=array).values('user')

        lister = []

        for j in userprofiles:
            lister.append(j['user'])

        users = User.objects.filter(pk__in=lister)
        #at this point we have the entire following of current_user inside users. We just now need to check if display_user is in that or not

        important_follow = users.filter(id=display_user.id)

        counter = len(important_follow)

        if counter == 0:
            followed = False
        elif counter == 1:
            followed = True 

        context.update({
            'posts': Post.objects.filter(author=self.get_object()),
            'shared_posts': SharedPost.objects.filter(author=self.get_object()),
            'followed': followed,
        })
        return context


def AddToFollowing(request, pk):
    user_to_be_followed = User.objects.get(id=pk)

    followed = False
    display_user = user_to_be_followed
    current_user = request.user

    # important_follow = Like.objects.filter(liker=current_user, post=current_post)

    pop = UserFollowers.objects.filter(followers=current_user).values('userprofile')

    array = []

    for i in pop:
        array.append(i['userprofile'])

    userprofiles = UserProfile.objects.filter(pk__in=array).values('user')

    lister = []

    for j in userprofiles:
        lister.append(j['user'])

    users = User.objects.filter(pk__in=lister)
    #at this point we have the entire following of current_user inside users. We just now need to check if display_user is in that or not

    important_follow = users.filter(id=display_user.id)

    counter = len(important_follow)

    if counter == 0:
        followed = False
    elif counter == 1:
        followed = True 

    if followed == False:
        user_following = UserFollowing.objects.get(userprofile = request.user.userprofile)
        user_following.following.add(user_to_be_followed)
        user_following.save()

        user_follower = UserFollowers.objects.get(userprofile = user_to_be_followed.userprofile)
        user_follower.followers.add(request.user)
        user_follower.save()

        #now lets add a notification for the user whose post got commented
        user_to_be_notified = user_to_be_followed
        userid = request.user.id
        noti = Notifications(user=user_to_be_notified, notification_type='New_Follower', notification_message=f"'{request.user.username}' followed you", link="url 'app-user-detail'", link_variable = userid)
        noti.save()

        messages.success(request, f"You are now following {user_to_be_followed.username}")

    elif followed == True:
        user_following = UserFollowing.objects.get(userprofile = request.user.userprofile)
        user_following.following.remove(user_to_be_followed)
        user_following.save()

        user_follower = UserFollowers.objects.get(userprofile = user_to_be_followed.userprofile)
        user_follower.followers.remove(request.user)
        user_follower.save()

        messages.success(request, f"User {user_to_be_followed.username} unfollowed successfully")

    return HttpResponseRedirect(reverse('app-user-detail', args=[str(pk)]))


def MyFollowing(request):
    
    pop = UserFollowers.objects.filter(followers=request.user).values('userprofile')

    array = []

    for i in pop:
        array.append(i['userprofile'])

    userprofiles = UserProfile.objects.filter(pk__in=array).values('user')

    lister = []

    for j in userprofiles:
        lister.append(j['user'])

    users = User.objects.filter(pk__in=lister)

    counter = len(users)

    context = {
        'users' : users,
        'counter' : counter
    }

    return render(request, "mavier/myfollowing.html", context)


def MyFollowers(request):
    
    pop = UserFollowing.objects.filter(following=request.user).values('userprofile')

    array = []

    for i in pop:
        array.append(i['userprofile'])

    userprofiles = UserProfile.objects.filter(pk__in=array).values('user')

    lister = []

    for j in userprofiles:
        lister.append(j['user'])

    users = User.objects.filter(pk__in=lister)

    counter = len(users)

    context = {
        'users' : users,
        'counter' : counter
    }

    return render(request, "mavier/myfollowers.html", context)


@method_decorator(login_required, name='dispatch')
class CommentDetailView(DetailView):
    model=Comment
    template_name = 'mavier/comment_detail.html'


@method_decorator(login_required, name='dispatch')        
class CommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['comment_content']
    template_name='mavier/comment_update_form.html' #this tells the ListView which template to refer to
    

    def form_valid(self, form):
        form.instance.commenter = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()

        if self.request.user == comment.commenter:
            return True
        return False


@method_decorator(login_required, name='dispatch')
class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        comment = self.get_object()

        if self.request.user == comment.commenter:
            if self.request.method == 'POST':
                post_affected = comment.post
                post_affected.comment_counter -= 1
                post_affected.save()
            return True
        return False

    success_url = '/home'


@method_decorator(login_required, name='dispatch')
class SharedCommentDetailView(DetailView):
    model=Comment_forSharedPost
    template_name = 'mavier/sharedcomment_detail.html'

@method_decorator(login_required, name='dispatch')        
class SharedCommentUpdateView(UserPassesTestMixin, UpdateView):
    model = Comment_forSharedPost
    fields = ['comment_content']
    template_name='mavier/sharedcomment_update_form.html' #this tells the ListView which template to refer to
    

    def form_valid(self, form):
        form.instance.commenter = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()

        if self.request.user == comment.commenter:
            return True
        return False


@method_decorator(login_required, name='dispatch')
class SharedCommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment_forSharedPost
    template_name='mavier/sharedcomment_confirm_delete.html' #this tells the ListView which template to refer to


    def test_func(self):
        comment = self.get_object()

        if self.request.user == comment.commenter:
            if self.request.method == 'POST':
                post_affected = comment.post
                post_affected.comment_counter -= 1
                post_affected.save()
            return True
        return False

    success_url = '/shome'

@method_decorator(login_required, name='dispatch')
class Notification_View(ListView):
    # model=Notifications
    template_name='mavier/notifications.html'
    context_object_name = 'notifications'
    # ordering = ['-notification_date']

    def get_queryset(self):
        current_user = self.request.user
        notifications = Notifications.objects.filter(user = current_user).order_by('-notification_date')
        return notifications    



@login_required
def PostSharesList(request):    
    post_obt = get_object_or_404(Post, id=request.POST.get('post_id'))

    sh_po = SharedPost.objects.filter(shared_post = post_obt).order_by('-date_posted')
    myshpost_counter = len(sh_po)

    current_user = request.user

    for current_post in sh_po:
        important_likes = Like_for_SharedPost.objects.filter(liker=current_user, post=current_post)
        counter = len(important_likes)

        if counter == 0:
            # liked = False
            current_post.temp_like_flag = 0
        elif counter == 1:
            # liked = True  
            current_post.temp_like_flag = 1

    context = {
        'shared_posts' : sh_po,
        'counter' : myshpost_counter
    }

    return render(request, "mavier/post_share_list.html", context)


@login_required
def LikedUsersList(request):    
    post_obt = get_object_or_404(Post, id=request.POST.get('post_id'))

    likes = Like.objects.filter(post = post_obt).values('liker')
    array = []
    for like in likes:
        array.append(like['liker'])
    users_of_importance = User.objects.filter(pk__in = array) 
    counter = users_of_importance.count()

    context = {
        'users' : users_of_importance,
        'counter' : counter
    }

    return render(request, "mavier/liked_users_list.html", context)


@login_required
def LikedUsersList_forSharedPosts(request):    
    post_obt = get_object_or_404(SharedPost, id=request.POST.get('sharedpost_id'))

    likes = Like_for_SharedPost.objects.filter(post = post_obt).values('liker')
    array = []
    for like in likes:
        array.append(like['liker'])
    users_of_importance = User.objects.filter(pk__in = array) 
    counter = users_of_importance.count()

    context = {
        'users' : users_of_importance,
        'counter' : counter
    }

    return render(request, "mavier/liked_users_list_forsharedposts.html", context)


#function based view
def about(request):
    return render(request, 'mavier/about.html')

#class based view (superior than function based view. Has lots of built in functionality)

