class APIError(Exception):
    def __init__(self, response):
        super(APIError, self).__init__(response.text)
        self.response = response


class AuthenticationError(APIError):
    def __init__(self, response):
        super(AuthenticationError, self).__init__(response)
        self.errors = response.json()


class ValidationError(APIError):
    def __init__(self, response):
        super(ValidationError, self).__init__(response)
        self.errors = response.json()
