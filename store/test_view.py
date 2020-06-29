from django.test import TestCase
from .models import Product

class TestViews(TestCase):
    
    def test_product_detail(self):
        product = Product.objects.create(
            name="A product", description="test", price="10"
        )
        response = self.client.get(f"/{product.id}")
        self.assertEqual =(response.status_code,200)
       
    
    def test_product_list_view(self):    
        response = self.client.get("/shop/")
        self.assertEqual =(response.status_code,200)
        self.assertTemplateUsed(response,'store/shop.html')     
    
    def test_shop(self):
        product = Product.objects.create(
            name="A product", description="test", price="10"
        )
        response = self.client.get(f"shop/{product.id}")
        self.assertEqual =(response.status_code,200)

    def test_cart(self):
        response = self.client.get("/cart/")
        self.assertEqual =(response.status_code,200)
        self.assertTemplateUsed(response,'store/cart.html')   

    def test_checkout(self):
        response = self.client.post("checkout/",{'full_name':"test",'email':'test','phone_number':'test','country':'test','postcode':'test','town_or_city':'test', 'street_address1':'test','street_address2':'test','county':'test',})
        self.assertRedirect =(response,"checkout_success")       

        response = self.client.get("/checkout/")
        self.assertEqual =(response.status_code,200)
        self.assertTemplateUsed(response,'store/checkout.html')   