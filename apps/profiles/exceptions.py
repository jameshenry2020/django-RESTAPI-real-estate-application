from rest_framework.exceptions import APIException



class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "the requested profile does not exist"



class NotYourProfile(APIException):
    status_code = 403
    default_detail = "this profile is not yours, you have no permission here"


    