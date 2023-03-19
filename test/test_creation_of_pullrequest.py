import json
from api.api_requests import Apirequests
from api.api_responses import Apiresponses
from utilities.config_reader_helper import *

auth = (read_login(), read_auth_token())
pulls = f'{read_repos_endpoint()}/{read_login()}/{read_repository()}/{read_pulls_endpoint()}'
with open('data/pullrequest.json', 'r') as f:
    params = json.load(f)


def test_create_new_pr():
    api = Apirequests(read_base_url())
    response = api.send_post(pulls, auth=auth, json=params)
    pr_create_response = Apiresponses(response)
    assert pr_create_response.get_status_code() == 201
    pr_json = pr_create_response.get_json()
    assert pr_json['title'] == 'Add new'
    print(pr_json)
