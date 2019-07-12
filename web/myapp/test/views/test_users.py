from django.test import TestCase
from django.urls import reverse
from myapp.forms.AddUserForm import AddUserForm

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
        #self.assertEqual(response.context['form'], AddUserForm())