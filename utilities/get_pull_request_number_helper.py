from api.api_requests import Apirequests
from api.api_responses import Apiresponses
from utilities.config_reader_helper import *

auth = (read_login(), read_auth_token())

pulls = f'{read_repos_endpoint()}/{read_login()}/{read_repository()}/{read_pulls_endpoint()}'


def get_pull_request_number():
    api = Apirequests(read_base_url())
    get_response = api.send_get(pulls, auth=auth)
    get_pr_number = Apiresponses(get_response)
    if get_pr_number.get_status_code() == 200:
        pull_request_number = get_pr_number.get_json()[0]['number']
        return pull_request_number
