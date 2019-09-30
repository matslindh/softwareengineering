class Request:
    def __init__(self):
        self.form = {}


def abort(c, msg):
    pass


class User:
    @staticmethod
    def sign_in(email, password):
        return False


request = Request()


valid_user = User.sign_in(
    request.form.get('email'),
    request.form.get('password_field'),
)

if not valid_user:
    abort(403, 'Invalid user given')

