import json
from api.api_requests import Apirequests
from api.api_responses import Apiresponses
from utilities.config_reader_helper import *
from utilities.get_pull_request_number_helper import get_pull_request_number

auth = (read_login(), read_auth_token())

new_review = f'{read_repos_endpoint()}/{read_login()}/{read_repository()}/{read_pulls_endpoint()}/{get_pull_request_number()}/{read_reviews_endpoint()}'

with open('data/pullrequestreview.json', 'r') as f:
    review_data = json.load(f)


def test_approve_pullrequest():
    api = Apirequests(read_base_url())
    response = api.send_post(new_review, auth=auth, json=review_data)
    approve_response = Apiresponses(response)
    print(approve_response.get_status_code())
    print(approve_response.get_json())
