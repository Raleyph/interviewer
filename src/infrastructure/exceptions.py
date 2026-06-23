class InfrastructureError(Exception):
    status_code = 500
    expose_message = False
