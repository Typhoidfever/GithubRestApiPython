import json
import pytest
from api.api_requests import Apirequests
from api.api_responses import Apiresponses
from utilities.config_reader_helper import *
from utilities.get_pull_request_number_helper import get_pull_request_number

api = Apirequests(read_base_url())
auth = (read_login(), read_auth_token())
branches_content = f'{read_repos_endpoint()}/{read_login()}/{read_repository()}{read_branches_endpoint()}'
pulls = f'{read_repos_endpoint()}/{read_login()}/{read_repository()}/{read_pulls_endpoint()}'
new_review = f'{read_repos_endpoint()}/{read_login()}/{read_repository()}/{read_pulls_endpoint()}/{get_pull_request_number()}/{read_reviews_endpoint()}'
pull_request = f'{read_repos_endpoint()}/{read_login()}/{read_repository()}/{read_pulls_endpoint()}/{get_pull_request_number()}'

with open('data/pullrequest.json', 'r') as f:
    params = json.load(f)

with open('data/pullrequestreview.json', 'r') as f:
    review_data = json.load(f)

with open('data/closepullrequest.json', 'r') as f:
    close_data = json.load(f)


@pytest.mark.tryfirst
def test_perform_authorization_on_github():
    response = api.send_get(read_user_endpoint(), auth=auth)
    authorization_response = Apiresponses(response)
    print(authorization_response.get_status_code())
    print(authorization_response.get_content())

    assert "login" in authorization_response.get_json(), "Authorization failed: User is not found"



def test_get_all_repos():
    global repos
    response = api.send_get(read_user_repos_endpoint(), auth=auth)
    repos_list_response = Apiresponses(response)
    if repos_list_response.get_status_code() == 200:
        repos = repos_list_response.get_json()

        for repo in repos:
            print(repo['name'])
    else:
        print("Oops, something went wrong")

    assert len(repos) > 0, "This account not contains any repos"



def test_get_all_branches_in_repos():
    response = api.send_get(branches_content, auth=auth)
    get_repository_branches_response = Apiresponses(response)
    branches = get_repository_branches_response.get_json()
    for branch in branches:
        print(branch['name'])
    assert len(branches) > 0, "No branches in this repo"



def test_create_new_pr():
    response = api.send_post(pulls, auth=auth, json=params)
    pr_create_response = Apiresponses(response)
    assert pr_create_response.get_status_code() == 201
    pr_json = pr_create_response.get_json()
    assert pr_json['title'] == 'Add new'
    print(pr_json)



def test_get_all_pullrequests():
    response = api.send_get(pulls, auth=auth)
    get_prs_response = Apiresponses(response)
    if get_prs_response.get_status_code() != 200:
        print(f"Failed to get PRs from repository: {get_prs_response.get_status_code()}")

    pull_requests = json.loads(get_prs_response.get_content())
    print(pull_requests)

    assert len(pull_requests) > 0
    if len(pull_requests) == 0:
        print("There is no open PRs in repository")



def test_approve_pullrequest():
    response = api.send_post(new_review, auth=auth, json=review_data)
    approve_response = Apiresponses(response)
    print(approve_response.get_status_code())
    print(approve_response.get_json())


@pytest.mark.trylast
def test_delete_pull_request():
    response = api.send_patch(pull_request, auth=auth, data=json.dumps(close_data))
    delete_response = Apiresponses(response)
    print(delete_response.get_status_code())
    if (delete_response.get_status_code()) == 200:
        print(f"Pull request {get_pull_request_number()} has been deleted")
    delete_response_json = json.loads(response.text)
    assert delete_response_json['state'] == 'closed'
