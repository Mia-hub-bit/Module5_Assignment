import unittest
import contact_manager
from contact_manager import DuplicateContactError, contacts 

class TestContactManager(unittest.TestCase):

    def setUp(self):
        # Clear state before test
        contacts.clear()
        
    def test_add_new_contact(self):
        # Test for successful addition
        name = "Cara"
        phone = "123-4567"
        contact_manager.add_contact(name, phone)
        self.assertIn(name, contacts)
        self.assertEqual(contacts[name], phone)

    def test_add_duplicate_contact_raises_error(self):
        # Test for duplicates exception
        name = "Sarah"
        contacts[name] = "999-0000"
        with self.assertRaises(DuplicateContactError):
            contact_manager.add_contact(name, "111-2233")
        
    def test_find_existing_contact(self):
        # Test successful lookup
        name = "Harry"
        phone = "222-3333"
        contacts[name] = phone
        found_phone = contact_manager.find_contact(name)
        self.assertEqual(found_phone, phone)

    def test_find_non_existent_contact_raises_keyerror(self):
        # Test KeyError for absent contact
        with self.assertRaises(KeyError):
            contact_manager.find_contact("NonExistentName")

    def test_delete_existing_contact(self):
        # Test successful deletion
        name = "Moe"
        contacts[name] = "1515-2323"
        contact_manager.delete_contact(name)
        self.assertNotIn(name, contacts)

    def test_delete_non_existent_contact_raises_keyerror(self):
        # Test KeyError for absent deletion
        with self.assertRaises(KeyError):
            contact_manager.delete_contact("UnknownContact")

if __name__ == '__main__':
    unittest.main()
