
<h1>AIRBNB_CLONE</h1>


<h3>The goal of the project is to deploy on your server a simple copy of the AirBnB website.</h3>


<h2>Attributes</h2>

# BaseModel Class

The `BaseModel` class is a foundational class that provides common attributes and methods for other classes in your program. It's designed to simplify the creation and management of objects.

## Attributes

- `id` (string): A unique identifier assigned to each instance of the class. It's generated using the `uuid.uuid4()` method and converted to a string for uniqueness.
- `created_at` (datetime): The timestamp indicating when the instance was created.
- `updated_at` (datetime): The timestamp indicating when the instance was last updated.

## Methods

### `__str__`

This method returns a user-friendly string representation of the object. It displays the class name, ID, and attributes.

### `save`

The `save` method updates the `updated_at` timestamp to the current datetime whenever changes are made to the object.

### `to_dict`

The `to_dict` method converts the object into a dictionary. This dictionary includes the object's attributes, class name, and timestamps. It's a crucial part of the serialization/deserialization process for storing or transferring data.

## Usage

You can use the `BaseModel` class as a foundation for other classes in your program. By inheriting from it, you inherit its common attributes and methods, making it easier to work with objects consistently.


AirBnB_clone/
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── engine/
│   │   ├── __init__.py
│   │   └── file_storage.py
├── tests/
|   ├── __init__.py
|   ├──
