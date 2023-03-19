import json
from api.api_requests import Apirequests
from api.api_responses import Apiresponses
from utilities.config_reader_helper import *
from utilities.get_pull_request_number_helper import get_pull_request_number

auth = (read_login(), read_auth_token())

pull_request = f'{read_repos_endpoint()}/{read_login()}/{read_repository()}/{read_pulls_endpoint()}/{get_pull_request_number()}'

with open('data/closepullrequest.json', 'r') as f:
    close_data = json.load(f)


def test_delete_pull_request():
    api = Apirequests(read_base_url())
    response = api.send_patch(pull_request, auth=auth, data=json.dumps(close_data))
    delete_response = Apiresponses(response)
    print(delete_response.get_status_code())
    if (delete_response.get_status_code()) == 200:
        print(f"Pull request {get_pull_request_number()} has been deleted")
    delete_response_json = json.loads(response.text)
    assert delete_response_json['state'] == 'closed'
