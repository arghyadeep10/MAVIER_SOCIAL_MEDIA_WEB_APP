# About Mavier
Mavier is a fully functional, feature rich social media web app, that allows its users to connect with one another in this ever so growing fast pace of the world.

Mavier is new, fresh and funky with beautiful backgrounds, designs and colorful UI.

# Usage

## Overall Directory structure of the Repo
- `MAVIER_SOCIAL_MEDIA_APP` [dir] (repo name)
    - `social_media` [dir]
        - `social_media` [dir]
        - `mavier` [dir]
        - `users` [dir]
        - `media` [dir]
        - `manage.py`
    - `requirements.txt`
    - `README.md`

## Steps to run the application


### Step 1:
#### **For Windows**
Create a virtual environment as follows:

In the dir `MAVIER_SOCIAL_MEDIA_APP` open cmd and execute:

```shell
python -m venv social_media_env
```

Activate the venv as follows: 

In that same directory open terminal and execute:
```shell
social_media_env\Scripts\activate
```

#### **For Linux**
Create a virtual environment as follows:

If this is your first time creating a virtual environment in your Linux machine, then run the following command:

```shell
sudo apt install -y python3-venv
```

In the dir `MAVIER_SOCIAL_MEDIA_APP` open terminal and execute:

```shell
python -m venv social_media_env
```

Activate the venv as follows:

In that same directory open terminal and execute:
```shell
source social_media_env/bin/activate
```


Step 2:

Install the necessary dependencies using pip and the `requirements.txt` file
```shell
pip install -r requirements.txt
```

Step 3:
Create a `.env` file to store your `SECRET_KEY` and `DEBUG` status

Create a new file name `.env` inside your `MAVIER_SOCIAL_MEDIA_APP/social_media` dir (Thus .env file will be alongside the manage.py file)

Inside the file write:
```txt
SECRET_KEY=<any_alphanumeric_combination>
DEBUG=1 [for DEBUG properties to be on]
DEBUG=0 [for DEBUG properties to be off]
```

Example:
```txt
SECRET_KEY=aipel280494nk3h2o802j4v4hf4
DEBUG=1
```

Step 4:

Apply all the migrations

Open cmd or terminal in the `MAVIER_SOCIAL_MEDIA_APP/social_media` dir which contains the `manage.py` file and execute the command as follows:

```shell
python manage.py migrate 
```


Step 5:

Start the server

Open cmd or terminal in the `MAVIER_SOCIAL_MEDIA_APP/social_media` dir which contains the `manage.py` file and execute the command as follows:

```
python manage.py runserver
```

#### Optional Task:
To visualize the backend and database you may create a superuser as follows:

Open cmd or terminal in the `MAVIER_SOCIAL_MEDIA_APP/social_media` dir which contains the `manage.py` file and execute the command as follows:

```shell
python manage.py createsuperuser
```

Follow the prompts
Then you can visit the `/admin` route and enter super user credentials and view the admin page.


# Functionality
1. Create Account
2. Login / Logout to and from your account
3. Create Posts
4. Edit Posts
5. Delete Posts 
6. Like Posts (also Unlike Posts)
7. Comment on Posts 
8. Edit Comments
9. Delete Comments
10. Share Posts (with your added input)
11. Edit your userprofile info
12. Upload Profile Picture
13. View other users and their profile and posts on Mavier
14. Follow other users to be able to view their posts
15. Receive detailed notifications (with clickable link to the source) when:

	i. Someone likes your Post
	
	ii. Someone comments on your Post
	
	iii. Someone Shares your Post
	
	iv. Someone Follows you on Mavier

16. View how many likes you have on your posts (alongwith the people who liked your posts)
17. View the comments on your posts
18. View how many shares you have on your posts (alongwith the people who shared your post and their shared post additional content)

Mavier also boasts of many features that are available in leading industry standard social media apps like:
1. Dynamic Like Button (that changes color and text when you like a post, indicating whether you have liked that post or not and thereby enabling you to unlike that post if already liked)
2. Dynamic Follow Button (that changes text when you follow someone indicating, whether you are already following that person or not)
3. Sharing posts with your own additional context and data/info. These shared posts are displayed as per industry standard with the original post embedded inside the shared post)
4. User Following and Follower features (These features put a user first focus on Mavier reminding that Mavier is not a blog which is static for all its users. Instead Mavier is personalized and dynamic with a user centric interface, crafted and tailored to the needs of an individual and his/her preference) (these features required substantial model chaining)
5. Displaying only the posts and shared posts of the people you are following on Mavier and not all the posts available on Mavier. (This again puts emphasis on the fact that Maver is user centric and tailored to an individual's needs.) (this feature required extensive Django Model Querying because of the substantial Model Chaining and Model Interaction between the User, Post, UserProfile, UserFollowing, UserFollower models)
6. Interactive Notifications (Notifications on Mavier are not static, instead they are dynamic and interactive providing users a highly improved user experience. For example, when someone likes your post, the notification you receive doesn't only tell you that someone has liked your post but displays the user who liked your post and the title of your post that was liked alongwith the most important piece, a button link to that post, so that you can quickly refer which post of yours got liked in just one click and don't have to manually rummage around to find that post of yours. Similarly when someone follows you on Mavier the notification tells in detail who followed you along with date and time stamps but most importantly allows you to view their profile in an instant by clicking the "View Profile" button right by the notification itself.)
7. Providing data that is useful to you (For each of the posts on Mavier you are able to view all the users (and their short description) who have liked your post. You also are able to view all the shared posts that others have created while sharing your post to see how exactly the community is reacting and responding to your work. And you can obviously view all the comments on your posts)
8. Mavier also provides clickable links to a User's profile. These links are embedded inside the username of the user displayed in various places throughout the website like on posts, shared posts and even comments. This allows you to view the person whose content you were just reading in an instant, allowing people to connect with each other more easily.
9. Mavier also uses Pagination to enable webpages to load faster, so that the user can enjoy a seamless experience. 

## Disclaimer
The app has been created by Arghyadeep Acharya as a Computer Science Web Development Project. It is solely for a personal educational purposes only and is meant to be a Portfolio project and not a commercial entity. All the details, info, names, logos e.t.c (if any) displayed in the app, or any of its documentation on its About Section or anywhere else in the website (Mavier), or in Github, or any of its video demonstrations are completely fictional and used solely for sake of explanation and demonstration. 

Mavier uses various dependencies like:

1. Django
2. Bootstrap 
3. Pillow (Python Package)	

And more.

Mavier is written using HTML, CSS, and Javascript for the frontend and uses Django for the backend. The backend database currently in use is SQLite database.