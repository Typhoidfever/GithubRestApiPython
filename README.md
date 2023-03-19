# GithubRestApiPython

1. Summary:
This repository represent realization of minimal testing framework, based on requests and pytest libraries to perform testing of basic actions, present on github.com
using GitHub REST API v3

2. Framework structure:

2.1 api frolder:

2.1.1 api_requests.py: Store class Apirequests that consists of methods that represent major REST API requests

2.1.2 api_responce.py: Store class Apiresponce that consists of  basic methods for response validation

2.2 test folder:

2.2.1 data folder:

2.2.1.1 closepullrequest.json : Store test-data to perform pull-request close operation

2.2.1.2 pullrequest.json: Store test-data to perform pull-request creation operation

2.2.1.3 pullrequestreview.json: Store test-data to perform pull-request approve operation

2.2.2 Report folder: Store Allure reports for test runs

2.2.3 config.ini: Store information about basic configurations (base url, endpoints, authorization information)

2.2.4 run_tests_with_allure_report.sh: Bash script that ensures the launch of hole test scope and generate allure test execution report

2.2.5 test_alltogether.py : Represent test script that contain all test cases

2.2.6 test_approve_pull_request.py : Represent test script that tests an ability to approve pull request using GitHub REST API

2.2.7 test_authorization_github.py : Represent test script that tests an ability to performe authorization with access token GitHub REST API

2.2.8 test_creation_of_pullrequest.py : Represent test script that tests an ability to create pull request using GitHub REST API

2.2.9 test_delete_pull_request.py : Represent test script that tests an ability to close pull request using GitHub REST API

2.2.10 test_get_all_branches_from_repository.py : Represent test script that tests an ability to get all branches from repository using GitHub REST API

2.2.11 test_get_all_pullrequests.py : Represent test script that tests an ability to get all existing pull requests in repository using GitHub REST API

2.2.12 test_get_all_repositories.py : Represent test script that tests an ability to get all existing  repositories on account using GitHub REST API 

2.3 utilities folder:

2.3.1 config_reader_helper.py : Helper that store methods for reading parametrs from config.ini file

2.3.2 get_pull_request_number_helper.py : Helper that store method that do get() call to 'pulls' endpoint and return number of last opened pull request

3. Framework use:

3.1 Clone repository GithubRestApiPython to local machine

3.2 Open project with IDE (Pycharm, VsCode) and navigate to config.ini file

3.3 Replase placeholders near 'user', 'token' and 'repository' values with custom information

3.4 Open and run all necessary tests

3.5 To run all tests with allure report perform next operation:

3.5.1 Navigate to /pass/to/project/folder/test with command line (For Windows machine Git Bush installation and use pre-required)

3.5.2 Make sure that run_tests_with_allure_report.sh is present 

3.5.3 Make run_tests_with_allure_report.sh executable (use chmod +x run_tests_with_allure_report.sh command)

3.5.4 Run run_tests_with_allure_report.sh (use ./run_tests_with_allure_report.sh command) 
