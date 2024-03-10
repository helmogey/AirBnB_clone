import unittest
from datetime import datetime
from unittest.mock import patch

from models import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_new_instance(self):
        """Tests creating a new BaseModel instance."""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    @patch('models.storage.new')
    def test_new_instance_storage(self, mock_new):
        """Tests registering a new instance with storage (using mock)."""
        model = BaseModel()
        self.assertTrue(mock_new.called)
        mock_new.assert_called_once_with(model)

    def test_save(self):
        """Tests updating updated_at and calling storage.save (using mock)."""
        model = BaseModel()
        with patch.object(model, 'save') as mock_save:
            model.save()
            self.assertTrue(mock_save.called)
            self.assertEqual(model.updated_at, datetime.now())

    def test_to_dict(self):
        """Tests to_dict method."""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], model.__class__.__name__)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()