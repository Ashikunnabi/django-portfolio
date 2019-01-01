from django.core.validators import validate_email

def email_validator(value):
    try:
        validate_email(value)
    except:
        raise ValueError("fghghfg")