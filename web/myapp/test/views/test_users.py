from django.test import TestCase
from django.urls import reverse
from myapp.forms.AddUserForm import AddUserForm
from django.contrib.auth.models import User

# Create your tests here.
class IndexViewTest(TestCase):

    fixtures = ['auth-user.json',]

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_view_users_GET_status_is_200(self):
        
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/index.html')

    def test_view_users_GET_list_is_3item(self):
        
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['user_list']), 3)     

    def test_view_users_GET_have_AddUserForm(self):
        response = self.client.get(reverse('index'))
        self.assertTrue(isinstance(response.context['form'], AddUserForm))

    def test_view_users_POST_can_create_user(self):
        response = self.client.post(reverse('index'),{
            'username': 'name_test'
        })
        self.assertEqual(response.status_code, 201)

        # have name_test
        user_list = User.objects.all().filter(username='name_test')
        self.assertEqual(len(user_list), 1)

    def test_view_users_POST_is_not_valid_username_is_null(self):
        response = self.client.post(reverse('index'),{
            #'username': 'name_test'
        })
        self.assertEqual(response.status_code, 400)
        self.assertFormError(response, 'form', 'username',['This field is required.'])