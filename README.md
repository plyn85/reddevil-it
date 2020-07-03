# Patrick Lynch RedevilIt Website

Milestone 4
Project:Full Stack Development - Code Institute

## Demo
A live demo can be found [here](https://redevilit.herokuapp.com/)

![Desktop Demo](https://res.cloudinary.com/plyn85/image/upload/v1593789703/reademe%20final/Screenshot_52_usk9gs.png "Desktop Demo")

This project was built with two purposes in mind. To provide a forum where fans could discuss Issues and events the effect the football club Manchester United and to sell vintage jerseys to those fans at a profit. 
The Idea for this project came from being a lifelong Manchester United fan. I wanted to build something that other fans could use and enjoy as well as meeting the requirements for the code institute final milestone.In the building the project, [Python](https://docs.python.org/3/), the framework [Django](https://docs.djangoproject.com/en/3.0/) and [postgrateSQL](https://www.postgresql.org/) atlas as the cloud based storage for the data and backend functionality. For the front-end, [Html](https://developer.mozilla.org/en-US/docs/Web/HTML), [Css](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) and [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) where used. Static files as well all Images for the products are stored in [AWS s3](https://developer.mozilla.org/en-US/docs/Web/HTML) bucket.
 


## UX
## The app is split Into three distinct sections. 

- The store app which includes shop page, cart and checkout pages which is available to any user who wants to make a purchase.

-  The forum app which Is only available to logged and registered users and includes the forum page, where a user can create, update and delete a post for other fans to see, as well as comment on or like other users posts.

- The users app which provides login, logout register password change, forgot password functionality for the user.

- Profile page  Although the profile page is in the profile app, it is intended to connect all the apps together. It is the first thing a user will see if he logs into the site with an empty shopping cart.There are links to both the fans forum and shopping pages. As well as the ability to update or add delivery information and personal user Information. A user can change their password or also view their entire order history.

 

## User  stories
" as a user I would like to ____________    "

- be able to view the website from all devices

- to be able to purchase a vintage jersey without the signing up process

-  To be able to search for a vintage jersey by its size, condition, which players name it contains, by highest or lowest price or by the year it was worn.

- to be able to clearly view a larger image of a jersey and gain more Information

- to be able to add it to my cart and be sure It has been added to my cart


- to be able increase the quantity after seeing the free delivery threshold

- to be able to go to a secure checkout, make a payment and receive confirmation email with the order details as well as confirmation of the order by email.

- to return to the shopping page after purchase

- to then decide to create an account by registering to view the fans forum
- to be brought to my profile page where I can clearly see all the information I just entered as well as options to add delivery Information, a pl;ace where my order history will be stored and an option to update my password.

- see clear links to the fans forum

- create update or delete a post

- to filter the posts by username, by the post content or by most recent or most popular posts.

- to add view all posts by a certain user

- to see how many comments a post has

- to view the comments 
- to comment on a post 

- to like or dislike a post

## Design 
- Layout - The design for this website was done using bootstrap for layout. 
- Colors -  There were four main colors used for the website. 
- off white  - an off white color #f8f8ff was used for background
- red - a shade of red #c70101 was used throughout the website. It being a manchester united fans forum, red being the color most closest associated with that team was the reason for this.
- black - black #000000 was used to complement the red color throughout the website
- green - a shade of green #28a745 was used for certain buttons, post, reset and most buttons regarding payments. I didn't want all buttons to be red, as red Is more of a warning color green portraits trust as is generally a better choice when it comes to purchases


- Fonts - The where two fonts used In the website taken from [Google fonts](https://fonts.google.com/)
.
- Bebas Neue - A font called for [Bebas Neue ](https://fonts.google.com/specimen/Bebas+Neue?query=bebas+) was used for all larger text on the website
- Montserrat - A font called for [Montserrat](https://fonts.google.com/specimen/Montserrat?query=montse) was used for all smaller text on the website
 

## Wireframe mockups
  Wireframing for this project was done the same as I like to do all my projects with a pencil and paper. Some of the forms pages would be near Identical on both mobile and larger devices so this was written on the sketch rather than sketching It out twice.

<details>
<summary>Home page</summary>
<br>
<table>
   <tr>
    <td>Mobile version<img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593802089/reademe%20final/IMG_20200703_193835_mjarmq.jpg" alt="wireframe mockup" style="width: 375px;"/> </td>
    </tr>
</table>
</details>
<br>
<details>
<summary>Register page</summary>
<br>
<table>
   <tr>
    <td> For all devices <img src="https://res.cloudinary.com/plyn85/image/upload/v1585983630/bookmarks-app/bookmarks%20wireframes%20pics/IMG_20200403_180614_se9vwj.jpg" alt="wireframe mockup" style="width:375px;"/> </td>
</table>
</details>

<br>
<details>
<summary>Login page</summary>
<table>
   <tr>
   For all devices
    <td> <img src="https://res.cloudinary.com/plyn85/image/upload/v1585983626/bookmarks-app/bookmarks%20wireframes%20pics/IMG_20200403_180628_avi2pa.jpg" alt="wireframe mockup" style="width: 250px;"/> </td>
</table>
</details>

<br>
<details>
<summary>Forum Page</summary>
<br>
<table>
   <tr>
    <td>Mobile version<img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593802085/reademe%20final/IMG_20200703_193842_hcbm8e.jpg" alt="wireframe mockup" style="width:375px;"/> </td>
    </tr>
</table>
</details>


<br>
<details>
<summary>Shop page</summary>
<table>
   <tr>
    <td>For mobile devices<img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593802092/reademe%20final/IMG_20200703_193824_ydj23g.jpg" alt="wireframe mockup" style="width: 375px;"/> </td>
</table>
</details>

<br>
<details>
<summary>Profile page</summary>
<br>
<table>
   <tr>
     For all devices
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593802095/reademe%20final/IMG_20200703_193904_xw23ba.jpg" style="width: 375px;"/> </td>
    </tr>
</table>
</details>

<br>
<details>
<summary>Shopping cart an checkout pages</summary>
<br>
<table>
   <tr>
    <td>For all devices <img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593802081/reademe%20final/IMG_20200703_193856_2_g6tyil.jpg" style="width: 250px;"/> </td>
    </tr>
</table>
</details>
<br>


## Technologies used 
- [Vs code](https://code.visualstudio.com/) - used as my IDE for coding
-  [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) - markup text language used  
-  [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) - used for  cascading style sheets
- [JQuery](https://jquery.com/) - Used for Javascript
- [Python](https://docs.python.org/3/) - Used as the back end programming language 
-  [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/)- to make the website responsive and used for layout.
- [Django](https://www.djangoproject.com/) -The framework used to build the website
- [Cloudinary](https://cloudinary.com/home-03-20-20?utm_expid=.VHiV_aImSdyLqXD_FUrhEg.1&utm_referrer=https%3A%2F%2Fwww.google.com%2F) - All images were deployed using the cloudinary caching server.
-  [postgrateSQL](https://www.postgresql.org/) Used as the database to store the various data

- [Heroku](www.heroku.com)  -Used to host the app 
- [Git and Github](https://github.com/) used for version control. GitHub used as a remote repository and the hosting of this site.

- [AWS s3](https://developer.mozilla.org/en-US/docs/Web/HTML) Used to store Images for products and static files

## Features

### Home/landing page top
<table>
   <tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593789703/reademe%20final/Screenshot_52_usk9gs.png" alt="wireframe mockup" style="width: 375px;"/> </td>
    </tr>
    <tr>
    <td> The non logged In user sees this when accessing the website. Two photos displayed in a carousel move across the screen telling the user and providing links to the two main sections of the website. Fans forum and shop. </td>
    </tr>
</table>

### Home/landing page bottom
<table>
   <tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593790133/reademe%20final/Screenshot_49_zayoeo.png" alt="wireframe mockup" style="width: 375px;"/> </td>
    </tr>
    <tr>
    <td> The non logged In user sees this when accessing the website. It displays the products in a card which can be viewed by clicking a button which will bring the user to the product detail page.  </td>
    </tr>
</table>

### Navbar logged In
<table>
   <tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593790527/reademe%20final/Screenshot_54_kln5wa.png" alt="wireframe mockup" style="width: 375px;"/> </td>
    </tr>
    <tr>
    <td> The navbar for a logged In user contains links for Forum, shop ,account which contains a dropdown which allows the user to logout and view their profile page as well as a shopping cart which displays the amount as the user adds Items to their cart.
  </td>
    </tr>
</table>

### Navbar not logged In
<table>
   <tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593790780/reademe%20final/Screenshot_57_u2xrja.png" alt="wireframe mockup" style="width: 375px;"/> </td>
    </tr>
    <tr>
    <td> The navbar for a non logged In user contains links for home, shop , register and login as well as a shopping cart which displays the amount as the user adds Items to their cart.
 </td>
    </tr>
</table>

### Footer
<table>
   <tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593791143/reademe%20final/Screenshot_59_olcnk5.png" style="width: 375px;"/> </td>
    </tr>
    <tr>
    <td> 
    The footer contains social media links, a copyright register and logged in buttons only on view for a non logged In user as well as a phone number and contact email address.

 </td>
    </tr>
</table>

### Register  
<table>
   <tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593783738/reademe%20final/Screenshot_30_ximlgz.png" alt="wireframe mockup" style="width: 375px;"/> </td>
    </tr>
    <tr>
    <td> Anyone can sign up, have an account and make use of the app. All passwords encrypted. Infomation Is then stored for user In there Profile Page. </td>
    </tr>
</table>

### Login 
 <table>
 <tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593784021/reademe%20final/Screenshot_32_r3w6rx.png" style="width: 375px;"/> </td>
    </tr>
    <tr>
    <td> Registered users can login In using username and password </td>
    </tr>
</table>

### Profile page
 <table>
<tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593784275/reademe%20final/Screenshot_33_iilfvh.png" style="width: 375px;"/> </td>
    </tr>
    <tr>
    <td>Registered users can view there profile page. 
    Which gives the user the ability to view all of the personal and delivery Information. Change or update it. Update their password. View all of the order history and view Individual orders by clicking on the order number
</td>
    </tr>
 </table>

### Forum page
 <table>
<tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593784680/reademe%20final/Screenshot_35_rruqqp.png" style="width: 375px;"/> </td>
    </tr>
    <tr>
    <td>
    Registered users can view the fans forum page gives a user the ability to create, update and delete their own posts.Interact with other users, comment,like or dislike other users' posts. Search posts by username, post content or by newer or most popular posts. The move through the posts by using pagination buttons located at the top and bottom of posts


</td>
    </tr>
 </table>

### Shop page
 <table>
<tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593785812/reademe%20final/Screenshot_39_fuceek.png" style="width: 375px;"/> </td>
    </tr>
    <tr>
<td>
Gives a user the ability to alter the quantity of the item they have in their cart. To continue shopping, go to a secure checkout and will alert the user to the fact that they could avail of free delivery if necessary

</td>
    </tr>
</table>

### Shopping cart
 <table>
<tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593794302/reademe%20final/Screenshot_99_yixrax.png" 
    style="width: 250px;"/> </td>
    </tr>
    <tr>
<td>
The cart is displayed on the corner on the navbar and will update the amount displayed in euros as the user adds Items to the cart. It Is handled using cookies. This was used instead of sessions as even if the user was to leave the website and come back another day the cart Items are still there encouraging  the user to make a purchase. If the user decides to login in or register while items are in the cart they will be directed to the shopping page and a pop up alert will tell the user there are items in there cart, again encouraging  the user to make a purchase.


</td>
    </tr>
</table>

### Check out page
 <table>
<tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593787657/reademe%20final/Screenshot_41_xzub45.png" style="width: 375px;"/> </td>
    </tr>
    <tr>
<td>
Gives the user the ability to purchase their order and complete the payment. User can also go back to cart page by adjusting the cart again alerted to the free delivery threshold If necessary


</td>
    </tr>
</table>

### Check out page
 <table>
<tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593788652/reademe%20final/Screenshot_43_rutkks.png" style="width: 375px;"/> </td>
    </tr>
    <tr>
<td>
Gives the user full details of the order tells them they ll be sent a confirmation email and gives them option to continue shopping

</td>
    </tr>
</table>

### Confirmation Email
 <table>
<tr>
    <td><img src="https://res.cloudinary.com/plyn85/image/upload/c_scale,w_375/v1593789076/reademe%20final/Screenshot_45_geuxjn.png" style="width: 375px;"/> </td>
    </tr>
    <tr>
<td>
The user will be sent a confirmation email with all the order details confirming that there order has been placed

</td>
    </tr>
</table>

## Features left to Implement

- I would like to add a members discount feature which gives the user an extra 15% discount after registration. I had the discount working On the website but couldn't get it saved to the database so decided to remove it.

- I Would like to handle the comments and posts by a  user using  ajax, maybe in a modal to give a better user experience by avoiding having the user being dragged around the website when commenting on a post or submitting their own post.
  
- A profile Image for each user which I originally had but was removed as It requires a lambda function for resize functionally to work with aws which I felt i wouldn't have time to implement
 
## Testing 
I used [WSC CSS](https://jigsaw.w3.org/css-validator/) Validation and [HTML Markup](https://validator.w3.org/) Validation to validate the html and css. The only errors occurring was with the django templating language which the HTML validator does not recognise   I used [PEP8](https://www.python.org/dev/peps/pep-0008/) to validate python.

Testing information can be found in every app In the folders 
test_view.py an test_forms.py

Most of the testing was done In as I developed the app  
I used the Django built In debugger through the whole development phase. I had It set debug=True in setings.py. This was a valuable resource. If there were any errors they were shown here and I used this to solve many Issues through the development process. 
As you become accustomed to the debugger you're able to quickly Identify what causes the app to crash. 

### Creating an account
I have created my own account along with 5 fake ones.The authentication for 
creating an account Is working as expected. I could register login, logout an then log back In Seamlessly.I was able to reset forgotten passwords for each user.
 I also updated user and delivery Information, updated passwords and made purchases using the fake user accounts.


### CRUD TESTING
As well as my own posts an comments I added posts and comments for 
the five fake users testing purposes


### Defensive design 
A login and registration system was used access the fourm section of the website.


 The defensive design was implemented throughout this project. Mainly my using the django templating language on the front end. Making use of 
      
      {% if user.is_authenticated %}    
      {% if user.is_authenticated %}
This was used to prevent users from having access to certain elements on the page 
Such as the access to delete or edit buttons on other users posts.



My app is fully responsive across a range of devices. This was achieved using the bootstrap grid. 
The responsiveness and correct displaying of all elements has been tested on a number of devices, browsers, and resolutions. Chrome, Firefox, Opera, Safari, Edge, and IE all display without issue.

Chrome dev tools were used to simulate multiple devices and widths, and no issues were encountered.

The following physical devices where 
tested with no issues found.

 - Lenovo ideapad 320s
 - Apple iphone 8
 - Apple ipad 3 
 - Samsung galaxy A3
 - Huawei p20 lite  

 ## Bugs 


###  Internet Explorer Issue 
 
When veiwing the callout section In both edge and Internet explorer the  callout section text was barely visible. This was a problem I enconterd In milestone one and I used the same fix I used then In my current application. Its a problem  In which the col class from bootstrap was causing the text to condense. It was resolved by adding 

    .internet-exploer-fix {
    -webkit-box-flex: 0;
     flex: none;
    -ms-flex: none;
    -moz-box-flex: none;
    }
      
## fixes 

## Deployment 
I deployed this application by:
 
1. I created an app on heroku 
2. Selected the free Hobby level.
3. updated the env.py file in my local enviroment with the DATABASE_URL details, and the settings.py to connect to the database using the dj_database_url package.
4. Ran the heroku run  python manage.py migrate command to migrate the models into Heroku Postgres and created a new super user in the new PostgreSQL database.
5. Copied and paste all of the default variables from env.py in to Heroku's Config Vars section.
6. Went to the Developers section in Stripe and clicked on API Keys.
7. Copied and pasted the Publishable Key and Secret Key and set them as the STRIPE_PUBLISHABLE and STRIPE_SECRET environment variables in the env.py file  within my local enviroment.
8. Updated the settings.py with the new Stripe environment variables.
9. Went to the S3 section of AWS and created a new S3 bucket.
10. Updated the settings.py file in my local workspace with the relevant S3 bucket detail
    
          AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
        }

        AWS_ACCESS_KEY_ID = <AWS_ACCESS_KEY_ID>
        AWS_SECRET_ACCESS_KEY = <AWS_SECRET_ACCESS_KEY>
        AWS_STORAGE_BUCKET_NAME = '<bucket_name>'
        AWS_S3_REGION_NAME = <region>
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
  
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'


        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOM{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

11. Created a custom_storages.py file with classes to route to the relevant location settings for static and media files.

12. Ran the python manage .py collectstatic command to push the static files to my S3 bucket.

13. Created a requirements .txt file using the following command in the terminal window:
        
        pip freeze --local > requirements.txt
14. Created a Procfile using the following command in the terminal window:
        
        web: gunicorn config.wsgi:application> Procfile

15. Ran the git add ., git commit -m "<commit-message>" and git push commands to push all changes to my GitHub repository.
16. Ran git push heroku master

17.Then the app was now deployed   

### Live app Link

- [https://redevilit.herokuapp.com/](https://redevilit.herokuapp.com/)

### Repository Link 

- [https://github.com/plyn85/reddevil-it](https://github.com/plyn85/reddevil-it) 



Should you wish to clone this:

   1. On GitHub, navigate to the main page of the repository.
   2. Under the repository name, click Clone or download.
   3. In the Clone with HTTPs section, click the copy icon to copy the clone URL for the repository.
   4. Open terminal.
   5. Change the current working directory to the location where you want the cloned directory to be made.
   6. Type git clone, and then paste`[https://github.com/plyn85/reddevil-it](https://github.com/plyn85/reddevil-it)
   7. Press Enter. Your local clone will be created.
   8. Enter and save your own credentials in the 
 .env,py file  and import this into the settings .py file
   9. Install the requirements.txt file by running the below command in your CLI Terminal:
        
           pip3 install -r requirements.txt

 10. Run the following commands in your Terminal to launch the Django project:
           
         python3 manage.py runserver

11. Run the following commands to migrate the database models and create a super user:

        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser
 
12. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
 
13. Set the following config vars in heroku :

        AWS_ACCESS_KEY_ID <YOUR_ACCESS_KEY>
        AWS_SECRET_ACCESS_KEY <YOUR_SECRET_ACCESS_KEY>
        AWS_STORAGE_BUCKET_NAME <YOUR_BUCKET_NAME>
        DATABASE_URL <YOUR_DATABASE_URL>
        DEFAULT_FROM_EMAIL <YOUR_DEFAULT_FORM_EMAIL>
        EMAIL_HOST_PASSWORD <YOUR_EMAIL_HOST_PASSWORD>  
        SECRET_KEY <YOUR_SECRET_KEY> 
        STRIPE_PUBLIC_KEY <YOUR_STRIPE_PUBLIC_KEY>
        STRIPE_SECRET_KEY <YOUR_STRIPE_PUBILC_KEY>
           

## Credits
  The following tutorials where used In the building of the app:
  - For the set up of the fourm an user apps [Corey Schafer](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
  - For the set up of cookie cart functionality [Denis Ivy](https://www.youtube.com/watch?v=woORrr3QNh8&t=3732s)
  - For the set up like/unlike buttons [CodingEntrepreneurs](https://www.youtube.com/watch?v=pkPRtQf6oQ8&t=1044s)
  - For stripe payments an checkout the [Code Institute](https://codeinstitute.net/contact/) course material was used

 Inspiration was taken from the following websites:
 - [classicfootballshirts](https://www.classicfootballshirts.co.uk/premiership-clubs/manchester-united.html)
 - [manutd.com](https://www.manutd.com/en/fans/fans-forum) 

### Content
 - The content for the products was taken from [classicfootballshirts](https://www.classicfootballshirts.co.uk/premiership-clubs/manchester-united.html)

### Media
- The Images of the products was taken from [classicfootballshirts](https://www.classicfootballshirts.co.uk/premiership-clubs/manchester-united.html)

### Acknowledgements
 - Rahul Patil my Code Institute mentor, for his invaluable advice and guidance.


  #### Disclaimer

   The content of this Website is for educational purposes only.

