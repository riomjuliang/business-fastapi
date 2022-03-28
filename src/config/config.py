import os


def get_url():
    user = os.getenv("POSTGRES_USER", "jriom")
    password = os.getenv("POSTGRES_PASSWORD", "55141055")
    server = os.getenv("POSTGRES_SERVER", "localhost:5432")
    db = os.getenv("POSTGRES_DB", "fastapi_db")
    return f"postgresql://{user}:{password}@{server}/{db}"
