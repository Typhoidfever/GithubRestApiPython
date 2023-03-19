import json
from api.api_requests import Apirequests
from api.api_responses import Apiresponses
from utilities.config_reader_helper import *

auth = (read_login(), read_auth_token())
pulls = f'{read_repos_endpoint()}/{read_login()}/{read_repository()}/{read_pulls_endpoint()}'


def test_get_all_pullrequests():
    api = Apirequests(read_base_url())
    response = api.send_get(pulls, auth=auth)
    get_prs_response = Apiresponses(response)
    if get_prs_response.get_status_code() != 200:
        print(f"Failed to get PRs from repository: {get_prs_response.get_status_code()}")

    pull_requests = json.loads(get_prs_response.get_content())
    print(pull_requests)

    assert len(pull_requests) > 0
    if len(pull_requests) == 0:
        print("There is no open PRs in repository")
