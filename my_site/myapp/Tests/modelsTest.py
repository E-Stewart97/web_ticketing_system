import unittest
from model import User

class UserTests(unittest.TestCase):
    def test_user_creation(self):
        user = User(username="Maxi")
        self.assertEqual(user.username, "Maxi")

    def test_user_str_representation(self):
        user = User(username="John")
        self.assertEqual(str(user), "John")

    def test_user_update(self):
        user = User(username="Tom")
        user.username = "Tom"
        self.assertEqual(user.username, "Tom")

if __name__ == '__main__':
    unittest.main()