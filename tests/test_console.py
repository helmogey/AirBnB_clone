import unittest
import unittest.mock
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()
        self.console.stdout = StringIO()  # Capture console output
        storage.reload()  # Ensure a clean storage state

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Tests creating a new instance."""
        self.console.onecmd("create BaseModel")
        self.assertIn("BaseModel.", mock_stdout.getvalue())  # Check for ID
        self.assertEqual(len(storage.all()), 1)  # Ensure one object

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Tests showing an instance."""
        model = BaseModel()
        storage.new(model)
        storage.save()
        self.console.onecmd(f"show BaseModel {model.id}")
        self.assertIn(str(model), mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Tests destroying an instance."""
        model = BaseModel()
        storage.new(model)
        storage.save()
        self.console.onecmd(f"destroy BaseModel {model.id}")
        self.assertEqual(storage.all(), {})  # Ensure object is deleted

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Tests showing all instances."""
        model1 = BaseModel()
        model2 = BaseModel()
        storage.new(model1)
        storage.new(model2)
        storage.save()
        self.console.onecmd("all")
        self.assertIn(str(model1), mock_stdout.getvalue())
        self.assertIn(str(model2), mock_stdout.getvalue())