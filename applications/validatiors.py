def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    from django.conf import settings
    (_, ext) = os.path.splitext(value.name)

    valid_extensions = settings.SUPPORTED_RESUME_EXTENSIONS
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
