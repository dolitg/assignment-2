from django.test import TestCase

def test_user_registration():
    client = app.test_client()
    response = client.post('/register', data={
        'username': 'test_user',
        'email': 'test_user@example.com',
        'password': 'test_password',
        'confirm_password': 'test_password'
    })
    assert response.status_code == 200
    assert b'Thank you for registering. Please log in.' in response.data

    def test_user_login():
        client = app.test_client()
        response = client.post('/login', data={
            'username': 'test_user',
            'password': 'test_password'
        })
        assert response.status_code == 200
        assert b'You have been logged in.' in response.data

        def test_chatbot_interaction():
            client = app.test_client()
            response = client.post('/chat', data={
                'input_text': 'Hello'
            })
            assert response.status_code == 200
            assert b'Hi there!' in response.data
