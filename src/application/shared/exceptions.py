class ApplicationError(Exception):
    status_code = 400
    expose_message = True
