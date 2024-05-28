from typing import List, Dict

from user.user import User

users_db = [
    {
        'username': 'testUser01',
        'password': 'testPassword01'
    },
    {
        'username': 'sky',
        'password': 'flying_Cat1'
    },
    {
        'username': 'hero',
        'password': 'flying_Cat2'
    }
]


def authenticate(credentials: dict) -> list[dict[str, str] | User]:
    '''Authenticate the user. Create user object if success.'''
    response = {
        'status': 'Failed!',
        'message': ''
    }
    user_found = None

    if not validate_credentials(credentials):
        response['message'] = 'Invalid credentials!'
        return [response, user_found]

    for user in users_db:
        if (
                user['username'].lower() == credentials['username'].lower()
                and user['password'] == credentials['password']
        ):
            response['status'] = 'Success!'
            user_found = User(
                username=credentials['username'],
                password=credentials['password']
            )

    if not user_found:
        response['message'] = 'Wrong username or password!'

    return [response, user_found]


def validate_credentials(credentials: dict) -> bool:
    '''Validate the login credentials struct'''
    if 'username' not in credentials or 'password' not in credentials:
        return False

    # TODO - validate strong password

    return True
