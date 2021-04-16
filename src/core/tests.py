from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from core.models import Resource


class ResourceTest(APITestCase):
    def setUp(self):
        Resource.objects.create(title='Test 1', amount=5, unit='KG', price=2, date='2022-01-01')
        Resource.objects.create(title='Test 2', amount=5, unit='KG', price=2, date='2022-01-01')

    def test_retrieve_all_resources(self):
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data['resources']), Resource.objects.count())
        self.assertEqual(response.data['total_count'], Resource.objects.count())
        self.assertEqual(response.data['resources'][0]['cost'], 10)
        self.assertEqual(response.data['resources'][1]['cost'], 10)

    def test_create_resource(self):
        data = {
            'title': 'Test 3',
            'amount': 3,
            'unit': 'KG',
            'price': 5,
            'date': '2020-01-01'
        }
        response = self.client.post(reverse('resources'), data=data, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Resource.objects.count(), 3)
        response = self.client.get(reverse('resources'))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data['resources']), Resource.objects.count())
        self.assertEqual(response.data['total_count'], Resource.objects.count())
        self.assertEqual(response.data['resources'][2]['cost'], 15)

    def test_put_resource(self):
        data = {
            'title': 'Test 2',
            'amount': 10,
            'unit': 'KG',
            'price': 5,
            'date': '2020-01-01'
        }
        response = self.client.put(reverse('resources-pk', kwargs={'pk': 2}), data=data, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(Resource.objects.get(pk=2).amount, 10)

    def test_patch_resource(self):
        data = {
            'price': 50
        }
        response = self.client.patch(reverse('resources-pk', kwargs={'pk': 2}), data=data, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(Resource.objects.get(pk=2).price, 50)

    def test_delete_resource(self):
        response = self.client.delete(reverse('resources-pk', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(Resource.objects.count(), 1)

    def test_total_count(self):
        response = self.client.get(reverse('total-cost'))
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['total_cost'], 20)



