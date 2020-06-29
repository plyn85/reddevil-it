from django.test import TestCase
from .forms import OrderForm

class TestOrderForm(TestCase):

    def test_order_fullname(self):
        form = OrderForm({'full_name':'test'})
        self.assertFalse(form.is_valid())

    def test_order_name_is_req(self):
        form = OrderForm({'full_name':' '})
        self.assertFalse(form.is_valid())
    
    
    def test_order_email(self):
        form =OrderForm({'email':'test'})
        self.assertFalse(form.is_valid())

    def test_order_phone_num(self):
        form = OrderForm({'phone_number':'test'})
        self.assertFalse(form.is_valid())

    def test_order_postcode(self):
        form =OrderForm({'postcode':'test'})
        self.assertFalse(form.is_valid())    
    
    def test_order_addr_one(self):
        form =OrderForm({'street_address1':'test'})
        self.assertFalse(form.is_valid())       
    
    
    def test_order_street_addr_is_req(self):
        form = OrderForm({'street_address1':' '})
        self.assertFalse(form.is_valid())
    
    
    def test_order_addr_two(self):
        form =OrderForm({'street_address2':'test'})
        self.assertFalse(form.is_valid())        

    def test_order_county(self):
        form = OrderForm({'county':'test'})
        self.assertFalse(form.is_valid())            

    def test_order_location(self):
        form = OrderForm({'State or Locality':'test'})
        self.assertFalse(form.is_valid())        

    def test_order_country(self):
        form = OrderForm({'country':'test'})
        self.assertFalse(form.is_valid())                 

    def test_country_req(self):
        form = OrderForm({'country':' '})
        self.assertFalse(form.is_valid())    