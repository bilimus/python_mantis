import time


def test_login(app):

    app.session.login("administrator", "root")
    time.sleep(2)
    assert app.session.is_logged_in_as("administrator")