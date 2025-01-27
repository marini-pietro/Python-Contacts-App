# This file should contain all the necessary tests to ensure that the application fully works before pushing to production.

import unittest, utils

class TestMyFunction(unittest.TestCase):
    
    def run_all_tests(self):
        # Run all tests
        self.test_database_setup()
        self.test_add_contact(name=input("Enter name: "), phone=input("Enter phone: "), email=input("Enter email: "), phone_prefix=input("Enter phone prefix: "))
        self.test_delete_contact(phone_number=input("Enter phone number to delete: "))
        self.test_search_contacts(name=input("Enter name: "), phone=input("Enter phone: "), email=input("Enter email: "), phone_prefix=input("Enter phone prefix: "))
        self.test_get_all_contacts()
        self.test_connection_close()

    def test_database_setup(self):
        # Test case 1: Check if the database is correctly created
        result = utils.setup_db()
        self.assertEqual(result, 0) # 0 means the database was successfully set up
    
    def test_connection_close(self):
        # Test case 2: Check if the connection to the database is correctly closed
        result = utils.close_connection()
        self.assertNotEqual(result, 0) # 0 means the database was successfully set up
    
    def test_add_contact(self, name:str, phone:str, email:str, phone_prefix:str):
        # Test case 3: Check if a contact is successfully added to the database
        result = utils.add_contact(name, phone, email, phone_prefix)
        self.assertNotEqual(result, 0) # 0 means the contact was successfully added to the database
    
    def test_delete_contact(self, phone_number:str):
        # Test case 4: Check if a contact is successfully deleted from the database
        result = utils.delete_contact(phone_number)
        self.assertNotEqual(result, 0) # 0 means the contact was successfully deleted from the database
    
    def test_search_contacts(self, name:str, phone:str, email:str, phone_prefix:str):
        # Test case 5: Check if the search function returns a list of contacts and not an int
        result = utils.search_contacts(name, phone, email, phone_prefix)
        self.assertIsInstance(result, list) # Ensure the result is a list
        self.assertNotIsInstance(result, int) # Ensure the result is not an int
    
    def test_get_all_contacts(self):
        # Test case 6: Check if the get_all_contacts function returns a list of contacts and not an int
        result = utils.get_all_contacts()
        self.assertIsInstance(result, list) # Ensure the result is a list
        self.assertNotIsInstance(result, int) # Ensure the result is not an int

if __name__ == '__main__':
    TestMyFunction().run_all_tests()