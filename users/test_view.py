from django.test import TestCase
from store.models import Order
class TestViews(TestCase):

    def test_my_login_view(self):
        response = self.client.post("login/",{'username':'test','password':'test'})
        self.assertRedirect =(response,"shop")
        self.assertRedirect =(response,"profile")
    
    def test_my_register_view(self):
        response = self.client.post("register/",{'first_name':'test','last_name':'test','username':'test','email':'test','password1':'test','password2':'test'})
        self.assertRedirect =(response,"login")
          
       
    def test_my_profile_view(self):
        response = self.client.post("profile/",{'firstname':'test','last_name':'test','username':'test','email':'test',})
        self.assertRedirect =(response,"profile")   

    def test_my_pas_change_view(self):
        response = self.client.post("password/")
        self.assertRedirect =(response,"profile")       

    def test_order_history_view(self):    
        order = Order.objects.create(transaction_id="7777")
        response = self.client.get(f"/order_history/{order.transaction_id}")
        self.assertEqual =(response.status_code,200)
        self.assertTemplateUsed(response,'store/checkout_success.html')        