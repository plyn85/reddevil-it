from django.test import TestCase
from .forms import UserRegisterForm,UserUpdateForm,UserLoginForm,ProfileForm,UserPasswordChangeForm,UserPasswordResetForm,UserSetPasswordForm

class TestUserRegisterForm(TestCase):

    def test_user_f_name(self):
        form = UserRegisterForm({'first_name':'test'})
        self.assertFalse(form.is_valid())
    

    def test_user_last_name(self):
        form =UserRegisterForm({'last_name':'test'})
        self.assertFalse(form.is_valid())
    
    def test_user_username(self):
        form =UserRegisterForm({'username':'test'})
        self.assertFalse(form.is_valid())

    def test_email(self):
        form = UserRegisterForm({'email':'@test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'][0],'Enter a valid email address.')

    def user_pass_one(self):
        form = UserRegisterForm({'password1':'test'})
        self.assertFalse(form.is_valid())
        self.assertIn('password1',form.errors.keys())
        self.assertEqual(form.errors['password1'][0],'This Field is required.')
    
    def test_user_pass_two(self):
        form = UserRegisterForm({'password2':'test'})
        self.assertFalse(form.is_valid()) 
        self.assertIn('password2',form.errors.keys())
        self.assertEqual(form.errors['password2'][0],'This password is too short. It must contain at least 8 characters.')  


class TestUserUpdateForm(TestCase):

    def test_user_f_name(self):
        form =UserUpdateForm({'first_name':'test'})
        self.assertFalse(form.is_valid())
    
    def test_user_last_name(self):
        form =UserUpdateForm({'last_name':'test'})
        self.assertFalse(form.is_valid())
    
    def test_user_username(self):
        form =UserUpdateForm({'username':'test'})
        self.assertTrue(form.is_valid())

    def test_email_update(self):
        form = UserUpdateForm({'email':' '})
        self.assertFalse(form.is_valid())


class TestUserLoginForm(TestCase):

    def test_username(self):
        form =UserLoginForm({'username':'test'})
        self.assertFalse(form.is_valid())
    
    def test_user_password(self):
        form =UserLoginForm({'password':'test'})
        self.assertFalse(form.is_valid())



class TestUserProfileForm(TestCase):

    def test_default_phone_num(self):
        form =ProfileForm({'phone_number':'000000'})
        self.assertTrue(form.is_valid())
    
    def test_default_postcode(self):
        form =ProfileForm({'default_postcode':'test'})
        self.assertTrue(form.is_valid())

    def test_default_town_or_city(self):
        form =ProfileForm({'default_town_or_city':'test'})
        self.assertTrue(form.is_valid())
    
    def test_default_addr_one(self):
        form =ProfileForm({'default_street_address1':'test'})
        self.assertTrue(form.is_valid())    

    def test_default_addr_two(self):
        form =ProfileForm({'default_street_address2':'test'})
        self.assertTrue(form.is_valid())
    
    def test_default_country(self):
        form =ProfileForm({'default_county':'test'})
        self.assertTrue(form.is_valid())    

class TestUserPasswordChangeForm(TestCase):

    def test_pass_change_pass_old(self):
        form =UserPasswordChangeForm({'old_password':'test'})
        self.assertFalse(form.is_valid())
    
    def test_pass_change_pass_one(self):
        form =UserPasswordChangeForm({'new_password1':'test'})
        self.assertFalse(form.is_valid())

    def test_pass_change_pass_two(self):
        form =UserPasswordChangeForm({'new_password2':'test'})
        self.assertFalse(form.is_valid())

class TestUserPasswordResetForm(TestCase):

    def test_pass_rest_form(self):
        form =UserPasswordResetForm({'email ':'@test'})
        self.assertFalse(form.is_valid())


class TestUserSetPasswordForm(TestCase):

    def test_change_new_pass_one(self):
        form =UserSetPasswordForm({'new_password1':'test'})
        self.assertFalse(form.is_valid())
    
    def test_pass_change_pass_two(self):
        form =UserSetPasswordForm({'new_password2':'test'})
        self.assertFalse(form.is_valid())