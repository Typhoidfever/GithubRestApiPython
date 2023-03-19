# This class store basic methods for response validation
class Apiresponses:

    def __init__(self, response):
        self.response = response

    def get_status_code(self):
        return self.response.status_code

    def get_header(self):
        return self.response.header

    def get_content(self):
        return self.response.content

    def get_json(self):
        return self.response.json()

    def is_request_success(self):
        return self.response.ok

    def is_request_was_redirected(self):
        return self.response.is_redirect