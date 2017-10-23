from django.test import TestCase

from .models import Item
# Create your tests here.

class TestItemListView(TestCase):
    def setUp(self):
        chili = Item(name='chili')
        chili.save()
        cheese = Item(name='cheese')
        cheese.save()
        sour_cream = Item(name='sour cream')
        sour_cream.save()

    def test_slug_is_correct(self):
        response = self.client.get('/items/sour-cream/')
        self.assertEqual(200, response.status_code)

    def test_all_items_posted(self):
        response = self.client.get('/items/')
        self.assertEqual(3, len(response.context['items']))