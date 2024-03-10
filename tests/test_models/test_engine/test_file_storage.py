import unittest
import os
from unittest.mock import patch
from models import FileStorage
from models.base_model import BaseModel
import json
class TestFileStorage(unittest.TestCase):

    def setUp(self):
        # Cleanup file before each test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Tests if all returns the __objects dictionary."""
        storage = FileStorage()
        self.assertEqual(storage.all(), {})  # Initially empty

    def test_new(self):
        """Tests adding a new object to __objects."""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        self.assertEqual(storage.all(), {model.__class__.__name__ + "." + model.id: model})

    def test_save(self):
        """Tests serializing objects to JSON file."""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.save()
        with open("file.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data, model.to_dict())

    def test_reload(self):
        """Tests deserializing objects from JSON file."""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.save()
        storage = FileStorage()  # New instance to test reloading
        storage.reload()
        self.assertEqual(storage.all(), {model.__class__.__name__ + "." + model.id: model})

    @patch('builtins.open')
    def test_reload_file_not_found(self, mock_open):
        """Tests reload behavior when file doesn't exist."""
        mock_open.side_effect = FileNotFoundError
        storage = FileStorage()
        storage.reload()  # Should not raise an exception

if __name__ == '__main__':
    unittest.main()
