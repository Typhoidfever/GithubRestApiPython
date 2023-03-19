import configparser

config = configparser.ConfigParser()
config.read('config.ini')


def read_base_url():
    return config.get('API', 'base_url')


def read_login():
    return config.get('Authentication', 'user')


def read_auth_token():
    return config.get('Authentication', 'token')


def read_repository():
    return config.get('Authentication', 'repository')


def read_user_endpoint():
    return config.get('API', 'user_endpoint')


def read_user_repos_endpoint():
    return config.get('API', 'user_repos_endpoint')


def read_repos_endpoint():
    return config.get('API', 'repos_endpoint')


def read_branches_endpoint():
    return config.get('API', 'branches_endpoint')


def read_pulls_endpoint():
    return config.get('API', 'pulls_endpoint')

def read_reviews_endpoint():
    return config.get('API', 'reviews_endpoint')
