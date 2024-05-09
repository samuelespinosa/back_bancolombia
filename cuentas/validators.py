from django.core.exceptions import ValidationError

def validate_number(value):
    if len(value) != 10:
        raise ValidationError('Debe de ser de 10 digitos')
    try:
        int(value)
    except ValueError:
        raise ValidationError('Debe de ser un numero valido')
