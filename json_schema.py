# https://chat.openai.com/share/14e8dc0a-a202-4868-8eb1-dc5f030ff3b1
# pointless change so i can notify colaborator
from jsonschema import Draft7Validator, exceptions
from jsonschema.validators import extend

def is_valid_employee(validator, employee_id, instance, schema):
    if not validator.is_type(instance, "integer"):
        yield exceptions.ValidationError(f"{instance} is not a valid integer")
    else:
        with Session(engine) as session:
            result = session.execute(select(Employee).filter_by(employee_id=instance)).scalar()
            if not result:
                yield exceptions.ValidationError(f"Employee ID {instance} does not exist in the database")

# Extend the default validator with a new 'employee_id' check
CustomValidator = extend(
    Draft7Validator,
    validators={
        "employee_id": is_valid_employee,
    }
)

schema = {
    "type": "object",
    "properties": {
        "employee_id": {"type": "integer", "employee_id": True}
    },
    "required": ["employee_id"]
}

def validate_json(data):
    validator = CustomValidator(schema)
    for error in validator.iter_errors(data):
        print(error.message)

# Test the custom validator
validate_json({"employee_id": 3})  # Should raise an error
validate_json({"employee_id": 1})  # Should pass
