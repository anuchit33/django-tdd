from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class UsersViewTest(TestCase):

    fixtures = ['auth-user.json',]

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_view_users_status_is_200(self):
        
        response = self.client.get(reverse('users'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/users.html')

    def test_view_users_list_is_3item(self):
        
        response = self.client.get(reverse('users'))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['user_list']), 3)       