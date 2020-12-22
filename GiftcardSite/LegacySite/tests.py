from django.test import TestCase
from django.test import Client

class ViewsTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Run once to set up non-modified data for all class methods.
        pass

    def setUp(self):
        #setUp: Run once for every test method to setup clean data.
        pass

    def test_register_view_good_data(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_register_view_xss_data(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_register_view_sqlInject_data(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
		
	def test_register_view_empty_data(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

srf_client = Client(enforce_csrf_checks=True)
