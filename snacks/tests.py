from django.test import TestCase
from django.urls import reverse


class ThingsTest(TestCase):
    def test_home_page_status_code(self):
        url = reverse('home')
        print(f'The url is: {url}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, 'base.html')