
import pytest
import app as task_app


@pytest.fixture
def client():
    task_app.app.config["TESTING"] = True

    # Start each test with a fresh task list
    task_app.tasks.clear()
    task_app.tasks.extend([
        {"id": 1, "name": "Study Python", "completed": False},
        {"id": 2, "name": "Practice Testing", "completed": False}
    ])
    task_app.next_id = 3

    with task_app.app.test_client() as client:
        yield client


def test_login_page_opens(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Login" in response.data


def test_valid_login(client):
    response = client.post(
        "/",
        data={"username": "admin", "password": "1234"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"My Dashboard" in response.data


def test_invalid_login(client):
    response = client.post(
        "/",
        data={"username": "admin", "password": "5143"}
    )

    assert response.status_code == 200
    assert b"Invalid username or password" in response.data


def test_dashboard_displays_tasks(client):
    response = client.get("/dashboard")

    assert response.status_code == 200
    assert b"Study Python" in response.data
    assert b"Practice Testing" in response.data


def test_add_task(client):
    response = client.post(
        "/add_task",
        data={"task": "Complete lab record"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Complete lab record" in response.data


def test_empty_task_is_not_added(client):
    client.post("/add_task", data={"task": "   "})

    assert len(task_app.tasks) == 2


def test_complete_task(client):
    client.post("/complete_task/1")

    task = next(t for t in task_app.tasks if t["id"] == 1)
    assert task["completed"] is True


def test_mark_task_incomplete(client):
    task_app.tasks[0]["completed"] = True

    client.post("/complete_task/1")

    task = next(t for t in task_app.tasks if t["id"] == 1)
    assert task["completed"] is False


def test_delete_task(client):
    client.post("/delete_task/1")

    assert all(t["id"] != 1 for t in task_app.tasks)
    assert len(task_app.tasks) == 1


def test_password_below_minimum(client):
    response = client.post(
        "/",
        data={"username": "admin", "password": "123"}
    )

    assert response.status_code == 200
    assert b"at least 4 characters" in response.data


def test_password_at_minimum(client):
    response = client.post(
        "/",
        data={"username": "admin", "password": "1234"}
    )

    assert response.status_code == 302


def test_password_above_minimum_wrong_password(client):
    response = client.post(
        "/",
        data={"username": "admin", "password": "12345"}
    )

    assert response.status_code == 200
    assert b"Invalid username or password" in response.data

