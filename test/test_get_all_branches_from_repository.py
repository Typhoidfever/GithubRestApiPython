import pytest
from api.api_requests import Apirequests
from api.api_responses import Apiresponses
from utilities.config_reader_helper import *

auth = (read_login(), read_auth_token())
branches_content = f'{read_repos_endpoint()}/{read_login()}/{read_repository()}{read_branches_endpoint()}'


def test_get_all_branches_in_repos():
    api = Apirequests(read_base_url())
    response = api.send_get(branches_content, auth=auth)
    get_repository_branches_response = Apiresponses(response)
    branches = get_repository_branches_response.get_json()
    for branch in branches:
        print(branch['name'])
    assert len(branches) > 0, "No branches in this repo"
