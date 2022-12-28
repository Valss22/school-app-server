from rest_framework.decorators import api_view
from rest_framework.request import Request
from . import services


def request_validator(schema: dict):
    def inner(func):
        def wrapper(request: Request):
            for (schema_key, schema_type_key), (data_key, data_value) in zip(
                schema.items(), request.data.items()
            ):
                if schema_key != data_key or schema_type_key is not type(data_value):
                    raise TypeError
            return func(request)

        return wrapper

    return inner


@api_view(["POST"])
@request_validator(
    {
        "name": str,
        "age": int,
    }
)
def register(request: Request):
    return services.create_user(request)
