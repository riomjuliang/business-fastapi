from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_company():
    response = client.post(
        "/companies",
        json={"name": "Company Name 1",
              "link": "Link 3",
              "city": "City 3",
              "date_added": "2014-01-01",
              "contact_first_name": "First name",
              "contact_last_name": "Last name",
              "contact_phone_number": "Phone number",
              "contact_email": "Email",
              "company_id": 1,
              "country": "Country 1"}
    )
    data = response.json()
    assert data["name"] == "Company Name 1"


def test_create_company_name_already_exists():
    response = client.post(
        "/companies",
        json={"name": "Company Name 1",
              "link": "Link 3",
              "city": "City 3",
              "date_added": "2014-01-01",
              "contact_first_name": "First name",
              "contact_last_name": "Last name",
              "contact_phone_number": "Phone number",
              "contact_email": "Email",
              "company_id": 5,
              "country": "Country 1"}
    )
    data = response.json()
    assert data['detail'] == "Company already exists with name Company Name 1"


def test_create_company_id_already_exists():
    response = client.post(
        "/companies",
        json={"name": "Company Name 1",
              "link": "Link 3",
              "city": "City 3",
              "date_added": "2014-01-01",
              "contact_first_name": "First name",
              "contact_last_name": "Last name",
              "contact_phone_number": "Phone number",
              "contact_email": "Email",
              "company_id": 1,
              "country": "Country 1"}
    )
    data = response.json()
    assert data['detail'] == "Company already exists with id 1"


def test_update_company():
    response = client.put(
        "/companies/1",
        json={"name": "Company Name 2",
              "link": "Link 3",
              "city": "City 3",
              "date_added": "2014-01-01",
              "contact_first_name": "First name",
              "contact_last_name": "Last name",
              "contact_phone_number": "Phone number",
              "contact_email": "Email",
              "country": "Country 1"}
    )
    data = response.json()
    assert data["name"] == "Company Name 2"


def test_get_companies():
    response = client.get(
        "/companies"
    )
    data = response.json()
    assert bool(data)


def test_get_company_by_id():
    response = client.get(
        "/companies/1"
    )
    data = response.json()
    assert bool(data)


def test_get_company_not_found():
    response = client.get(
        "/companies/5"
    )
    data = response.json()
    assert data['detail'] == "Company with company id 5 not found"


def test_delete_company():
    response = client.delete(
        "/companies/1"
    )
    data = response.json()
    assert bool(data)
