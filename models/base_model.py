#!/usr/bin/python3
import uuid
import datetime
import models
class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        frmat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) > 0:
            print(kwargs)
            for key in kwargs:
                value = kwargs[key]
                if key == "created_at":
                    self.created_at = datetime.datetime.strptime(value, frmat)
                elif key == "updated_at":
                    self.updated_at = datetime.datetime.strptime(value, frmat)
                elif key == "id":
                    self.id = value
            if not kwargs:
                models.storage.new(self)  # New instance, register with storage
        else:
            # Also call storage.new for new instances without arguments
            models.storage.new(self)


    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.datetime.now()
        models.storage.save()


    def to_dict(self):
        """
        Returns a dictionary containing all keys and values of the instance's __dict__,
        including the class name and ISO formatted timestamps.
        """
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict



    def __str__(self):
        """ print: [<class name>] (<self.id>) <self.__dict__>"""
        # return f"{self.__class__.__name__}('{self.id}', '{self.created_at}', '{self.updated_at}')"

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
