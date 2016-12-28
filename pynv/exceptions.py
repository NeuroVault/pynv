class APIError(Exception):
    def __init__(self, response):

        super(APIError, self).__init__(self._extract_text(response))
        self.response = response

    def _extract_text(self, response):
        return self._text_from_detail(response) or response.text

    def _text_from_detail(self, response):
        try:
            errors = response.json()
            return errors['detail']
        except (AttributeError, KeyError, ValueError):
            return None


class AuthenticationError(APIError):
    def __init__(self, response):
        super(AuthenticationError, self).__init__(response)
        self.errors = response.json()


class ValidationError(APIError):
    def __init__(self, response):
        super(ValidationError, self).__init__(response)
        self.errors = response.json()
