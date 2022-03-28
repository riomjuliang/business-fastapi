from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_vacancy():
    response = client.post(
        "/vacancies",
        json={
            "position_name": "Position name 1",
            "company_id": 1,
            "salary": 3000,
            "max_experience": 5,
            "vacancy_id": 1,
            "vacancy_link": "Vacancy link",
            "min_experience": 1,
            "skills": "Skills"
        }
    )
    data = response.json()
    bool(data)


def test_create_vacancy_id_already_exists():
    response = client.post(
        "/vacancies",
        json={
            "position_name": "Position name 1",
            "company_id": 1,
            "salary": 3000,
            "max_experience": 5,
            "vacancy_id": 1,
            "vacancy_link": "Vacancy link",
            "min_experience": 1,
            "skills": "Skills"
        }
    )
    data = response.json()
    assert data['detail'] == "Vacancy already exists with id 1"


def test_update_vacancy():
    response = client.put(
        "/vacancies/1",
        json={
            "position_name": "Position name 5",
            "company_id": 1,
            "salary": 3000,
            "max_experience": 5,
            "vacancy_link": "Vacancy link",
            "min_experience": 1,
            "skills": "Skills"
        }
    )
    data = response.json()
    assert data["position_name"] == "Position name 5"


def test_get_vacancies():
    response = client.get(
        "/vacancies"
    )
    data = response.json()
    assert bool(data)


def test_get_vacancy_by_id():
    response = client.get(
        "/vacancies/1"
    )
    data = response.json()
    assert bool(data)


def test_get_vacancy_not_found():
    response = client.get(
        "/vacancies/5"
    )
    data = response.json()
    assert data['detail'] == "Vacancy with vacancy id 5 not found"


def test_delete_vacancy():
    response = client.delete(
        "/vacancies/1"
    )
    data = response.json()
    assert bool(data)
