from django.test import TestCase
from .models import Product,Order

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
        self.assertRedirect =(response,"store/checkout_success.html")       

    def test_checkout_success(self):
        
        order = Order.objects.create(transaction_id="1223344556677",full_name="test",
        email="@test",phone_number="0000",country="test",postcode="test",street_address1="test",street_address2="test",total="90",grand_total="90")
        response = self.client.get(f"/checkout_success/{order.transaction_id}")
        self.assertEqual =(response.status_code,200)
        self.assertTemplateUsed(response,'store/checkout_success.html')     

