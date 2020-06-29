from django.test import TestCase
from . models import Comment,Post
from django.contrib.auth.models import User

class TestViews(TestCase):

    def test_home(self):
        response = self.client.get("/")
        self.assertEqual =(response.status_code,200)
        self.assertTemplateUsed(response,'fourm/home.html')

    def test_post_list_view(self):    
        response = self.client.get("/")
        self.assertEqual =(response.status_code,200)
        self.assertTemplateUsed(response,'fourm/home.html')       

    def test_user_post_list_view(self):    
        user = User.objects.create(username="plyn85")
        response = self.client.get(f"/user/{user.username}")
        self.assertEqual =(response.status_code,200)
        self.assertTemplateUsed(response,'fourm/user_posts.html')       
    
    
    def test_add_comment_to_post(self):
        response = self.client.post({'text':'test'})     
        self.assertRedirect =(response,"post/<int:pk>/comment/")
    
    def test_post_create_view(self):
        response = self.client.post("post/",{'title':'test','content':'test'})
        self.assertRedirect =(response,"post/new")
        
    def test_post_update_view(self):
        response = self.client.post("post/",{'title':'test','content':'test'})
        self.assertRedirect =(response,"post/<int:pk>/update/")
   
    def test_post_delete_view(self):
        response = self.client.post("post/",{'title':'test','content':'test'})
        self.assertRedirect =(response,"post/<int:pk>/delete")
    
     