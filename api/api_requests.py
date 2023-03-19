import requests

# This class store basic requests methods that used in test

class Apirequests:

    def __init__(self, base_url):
        self.base_url = base_url

    def send_get(self, endpoint, headers=None, params=None, auth=None):
        url = self.base_url + endpoint
        response = requests.get(url, headers=headers, params=params,  auth=auth)
        return response

    def send_post(self, endpoint, headers=None, data=None, json=None, auth=None):
        url = self.base_url + endpoint
        response = requests.post(url, headers=headers, data=data, json=json, auth=auth)
        return response

    def send_put(self, endpoint, headers=None, data=None, json=None,auth=None):
        url = self.base_url + endpoint
        response = requests.put(url, headers=headers, data=data, json=json, auth=auth)
        return response

    def send_delete(self, endpoint, headers=None, auth=None):
        url = self.base_url + endpoint
        response = requests.delete(url, headers=headers, auth=auth)
        return response

    def send_patch(self, endpoint, headers=None, auth=None, data=None):
        url = self.base_url + endpoint
        response = requests.patch(url, headers=headers, auth=auth, data=data)
        return response

