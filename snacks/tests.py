from django.test import TestCase, SimpleTestCase
from django.urls import reverse
# Create your tests here.

class test_status_code(SimpleTestCase):
    def test_all_status_codes(self):
        self.assertEqual(self.client.get(reverse('home')).status_code, 200)
        self.assertEqual(self.client.get(reverse('about')).status_code, 200)

    def test_all_template_use(self):
        self.assertEqual(self.client.get(reverse('home')).templates[0].name, "home.html")
        self.assertEqual(self.client.get(reverse('about')).templates[0].name, "about.html")
        self.assertEqual(self.client.get(reverse('about')).templates[1].name, "base.html")