from rest_framework.exceptions import APIException


class NotAnAgent(APIException):
    status_code = 403
    default_detail = "you are not an agent, please register as an agent"


class PropertyNotFound(APIException):
    status_code = 404
    default_detail = "this property does not exist"
