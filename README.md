# Business Fast API

## EndPoints disponibles

### Empresas

**Creación de empresas**

Permite crear una empresa

`Type: POST -> /companies`

* Body

```json
    {
        "name": "Company Name",
        "link": "Link",
        "city": "City",
        "date_added": "2022-01-01",
        "contact_first_name": "First Namd",
        "contact_last_name": "Last Name",
        "contact_phone_number": "Phone Number",
        "contact_email": "Contact Email",
        "company_id": 1,
        "country": "Country"
    }
```

* Return

```json
    {
        "name": "Company Name",
        "link": "Link",
        "city": "City",
        "date_added": "2022-01-01",
        "contact_first_name": "First Namd",
        "contact_last_name": "Last Name",
        "contact_phone_number": "Phone Number",
        "contact_email": "Contact Email",
        "company_id": 1,
        "country": "Country"
    }
```

**Obtención de empresas**

Obtiene la información de todas las empresas existentes

`Type: GET -> /companies`

* Return

```json
    [
      {
          "name": "Company Name 7",
          "link": "Link 3",
          "city": "City 3",
          "date_added": "2014-01-01",
          "contact_first_name": "First name",
          "contact_last_name": "Last name",
          "contact_phone_number": "Phone number",
          "contact_email": "Email",
          "company_id": 7,
          "country": "Country 1"
      },
      {
          "name": "Company Name 4",
          "link": "Link 3",
          "city": "City 3",
          "date_added": "2014-01-01",
          "contact_first_name": "First name",
          "contact_last_name": "Last name",
          "contact_phone_number": "Phone number",
          "contact_email": "Email",
          "company_id": 1,
          "country": "Country 1"
      }
    ]
```

**Obtención de empresa según ID**

Obtiene la información de una empresa con el ID recibido por parámetro

`Type: GET -> /companies/{company_id}`

* Return

```json
    {
        "name": "Company Name",
        "link": "Link",
        "city": "City",
        "date_added": "2022-01-01",
        "contact_first_name": "First Namd",
        "contact_last_name": "Last Name",
        "contact_phone_number": "Phone Number",
        "contact_email": "Contact Email",
        "company_id": 1,
        "country": "Country"
    }
```

**Actualización de datos de empresa según ID**

Actualiza la información de una empresa con el ID recibido por parámetro

`Type: PUT -> /companies/{company_id}`

* Body

```json
    {
        "name": "Company Name",
        "link": "Link",
        "city": "City",
        "date_added": "2022-01-01",
        "contact_first_name": "First Namd",
        "contact_last_name": "Last Name",
        "contact_phone_number": "Phone Number",
        "contact_email": "Contact Email",
        "company_id": 1,
        "country": "Country"
    }
```

**Borrado de empresa según ID**

Se borra empresa según ID recibido por parámetro

`Type: DELETE -> /companies/{company_id}`

* Return

```json
    {
        "name": "Company Name",
        "link": "Link",
        "city": "City",
        "date_added": "2022-01-01",
        "contact_first_name": "First Namd",
        "contact_last_name": "Last Name",
        "contact_phone_number": "Phone Number",
        "contact_email": "Contact Email",
        "company_id": 1,
        "country": "Country"
    }
```

### Vacantes

**Creación de vacante**

Permite crear una vacante

`Type: POST -> /vacancies`

* Body

```json
    {
        "position_name": "Position name",
        "company_id": 1,
        "salary": 3000,
        "max_experience": 5,
        "vacancy_id": 1,
        "vacancy_link": "Vacancy link",
        "min_experience": 1,
        "skills": "Skills"
    }
```

* Return

```json
    {
        "position_name": "Position name",
        "company_id": 1,
        "salary": 3000,
        "max_experience": 5,
        "vacancy_id": 1,
        "vacancy_link": "Vacancy link",
        "min_experience": 1,
        "skills": "Skills"
    }
```

**Obtención de vacantes**

Obtiene la información de todas las vacantes existentes

`Type: GET -> /vacancies`

* Return

```json
    [
      {
          "position_name": "Position name",
          "company_id": 1,
          "salary": 3000,
          "max_experience": 5,
          "vacancy_id": 1,
          "vacancy_link": "Vacancy link",
          "min_experience": 1,
          "skills": "Skills"
      },
      {
          "position_name": "Position name",
          "company_id": 2,
          "salary": 3500,
          "max_experience": 3,
          "vacancy_id": 2,
          "vacancy_link": "Vacancy link",
          "min_experience": 1,
          "skills": "Skills"
      }
    ]
```

**Obtención de vacantes según ID de empresa**

Obtiene la información de todas las vacantes existentes según ID recibido por parámetro

`Type: GET -> /vacancies/company/{company_id}`

* Return

```json
    [
      {
          "position_name": "Position name",
          "company_id": 1,
          "salary": 3000,
          "max_experience": 5,
          "vacancy_id": 1,
          "vacancy_link": "Vacancy link",
          "min_experience": 1,
          "skills": "Skills"
      },
      {
          "position_name": "Position name",
          "company_id": 1,
          "salary": 3500,
          "max_experience": 3,
          "vacancy_id": 2,
          "vacancy_link": "Vacancy link",
          "min_experience": 1,
          "skills": "Skills"
      }
    ]
```

**Obtención de vacante según ID**

Obtiene la información de una vacante con el ID recibido por parámetro

`Type: GET -> /vacancies/{vacancy_id}`

* Return

```json
    {
        "position_name": "Position name",
        "company_id": 1,
        "salary": 3000,
        "max_experience": 5,
        "vacancy_id": 1,
        "vacancy_link": "Vacancy link",
        "min_experience": 1,
        "skills": "Skills"
    }
```

**Actualización de datos de vacante según ID**

Actualiza la información de una vacante con el ID recibido por parámetro

`Type: PUT -> /vacancies/{vacancy_id}`

* Body

```json
    {
          "position_name": "Position name",
          "company_id": 1,
          "salary": 3000,
          "max_experience": 5,
          "vacancy_id": 1,
          "vacancy_link": "Vacancy link",
          "min_experience": 1,
          "skills": "Skills"
    }
```

**Borrado de vacante según ID**

Se borra vacante según ID recibido por parámetro

`Type: DELETE -> /vacancies/{vacancy_id}`

* Return

```json
    {
        "position_name": "Position name",
        "company_id": 1,
        "salary": 3000,
        "max_experience": 5,
        "vacancy_id": 1,
        "vacancy_link": "Vacancy link",
        "min_experience": 1,
        "skills": "Skills"
    }
```
