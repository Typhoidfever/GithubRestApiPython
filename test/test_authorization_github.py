from api.api_requests import Apirequests
from api.api_responses import Apiresponses
from utilities.config_reader_helper import *

auth = (read_login(), read_auth_token())


def test_perform_authorization_on_github():
    api = Apirequests(read_base_url())
    response = api.send_get(read_user_endpoint(), auth=auth)
    authorization_response = Apiresponses(response)
    print(authorization_response.get_status_code())
    print(authorization_response.get_content())

    assert "login" in authorization_response.get_json(), "Authorization failed: User is not found"
