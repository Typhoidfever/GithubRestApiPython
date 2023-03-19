from api.api_requests import Apirequests
from api.api_responses import Apiresponses
from utilities.config_reader_helper import *

auth = (read_login(), read_auth_token())


def test_get_all_repos():
    global repos
    api = Apirequests(read_base_url())
    response = api.send_get(read_user_repos_endpoint(), auth=auth)
    repos_list_response = Apiresponses(response)
    if repos_list_response.get_status_code() == 200:
        repos = repos_list_response.get_json()

        for repo in repos:
            print(repo['name'])
    else:
        print("Oops, something went wrong")

    assert len(repos) > 0, "This account not contains any repos"
