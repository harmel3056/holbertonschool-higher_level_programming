#!/usr/bin/env python3
import os
import json
from task_00_basic_serialization import serialize_and_save_to_file, load_and_deserialize

def test_basic_serialization():
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    filename = 'data.json'

    # Ensure any existing file is removed before test
    if os.path.exists(filename):
        os.remove(filename)

    # Serialize and save
    serialize_and_save_to_file(data_to_serialize, filename)
    print("Data serialized and saved to 'data.json'.")

    # Check file existence
    assert os.path.exists(filename), "File was not created."

    # Load and deserialize
    deserialized_data = load_and_deserialize(filename)
    print("Deserialized Data:")
    print(deserialized_data)

    # Check data integrity
    assert isinstance(deserialized_data, dict), "Deserialized data is not a dictionary."
    assert deserialized_data == data_to_serialize, "Deserialized data does not match original."

if __name__ == "__main__":
    test_basic_serialization()