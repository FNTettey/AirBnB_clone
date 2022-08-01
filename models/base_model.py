#!/usr/bin/python3
"""
Contains the "BaseModel" class
"""
from uuid import uuid4
from datetime import datetime
 
class BaseModel:
    """ defines all common attributes/methods for other classes:"""
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
 
    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
 
    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
 
    def _str_(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
 
 
 
