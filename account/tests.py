from django.test import TestCase

from account.serializers import CustomUserSerializer


class CustomUserTests(TestCase):
    def setUp(self):
        self.validate_data={
            'username':'test',
            'email':'test@gmail.com',
            'password':'1995',
        }

    def test_serializer(self):
        serializer = CustomUserSerializer(data=self.validate_data)
        self.assertTrue(serializer.is_valid())


    def test_create_user(self):
        serializer = CustomUserSerializer(data=self.validate_data)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        user=serializer.save()
        self.assertEqual(user.username,"test")
        self.assertTrue(user.check_password("1995"))



