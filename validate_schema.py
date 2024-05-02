import jsonschema

def validate_schema(data, schema):
    """
    Validate the json request against the given json schema.

    Args:
        json_request: Dictionary representing the JSON request.
        json_schema: Dictionary representing the JSON schema.

    Returns:
        bool: True if the data is valid according to the schema, False otherwise.
        str: If validation fails, returns the error message.
    """
    try:
        jsonschema.validate(instance=data, schema=schema)
        return True, None  # Validation successful
    except jsonschema.exceptions.ValidationError as e:
        return False, str(e)  # Validation failed, return error message

if __name__ == "__main__":
    # Example usage
    json_request = {
        "name": "John Doe",
        "age": 30,
        "email": "john.doe@example.com"
    }

    json_schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "age": {"type": "integer"},
            "email": {"type": "string", "format": "email"}
        },
        "required": ["name", "age", "email"]
    }

    is_valid, error_message = validate_schema(json_request, json_schema)
    if is_valid:
        print("Request is valid according to the schema.")
    else:
        print("Validation failed with error:", error_message)
