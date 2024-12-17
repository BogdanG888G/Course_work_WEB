# main_app/tests.py

from django.test import TestCase
from main_app.models import Stand
import time

class StandTestCase(TestCase):
    def setUp(self):
        Stand.objects.create(stand_user='Jotaro Kujo', stand_name='Star Platinum')

    def test_stand_query(self):
        stands = Stand.objects.filter(stand_user='Jotaro Kujo')
        self.assertEqual(stands.count(), 1)

class PerformanceTestCase(TestCase):
    def setUp(self):
        # Создаем большое количество объектов для тестирования производительности
        for i in range(1000):
            Stand.objects.create(stand_user=f'User {i}', stand_name=f'Stand {i}')

    def test_query_performance(self):
        start_time = time.time()
        stands = Stand.objects.filter(stand_user='User 500')
        end_time = time.time()
        self.assertEqual(stands.count(), 1)
        print(f"Query time: {end_time - start_time} seconds")
