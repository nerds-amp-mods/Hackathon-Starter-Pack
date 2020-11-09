def test_base_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'{"response":"Welcome to Landing Page"}' in response.data
