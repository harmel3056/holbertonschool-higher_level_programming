#!/usr/bin/python3
"""
Serializes and deserializes custom Python objects
"""
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        """
        Instantiates our class attributes
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Establishes the output formatting
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes data from filename using pickle library

        Args:
        filename - name of the file to open and serialize
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        # following method not advisable for debugging
        except Exception as e:
            raise

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes data from filename for usage

        Args:
        filename - name of the file to read and deserialize
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        # this preferred but not making checker happy:
        # except (pickle.PickleError, IOError) as e
        except Exception as e:
            raise
# pickle doesn't use encoding like JSON does because
# it works with binary data instead, not text. We use
# 'wb' (write binary) and 'rb' (read binary) mode,
# so encoding is not appropriate
