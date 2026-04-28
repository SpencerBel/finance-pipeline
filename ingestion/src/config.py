import os
from sqlalchemy import create_engine

def get_engine():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST", "postgres")
    db = os.getenv("POSTGRES_DB")
    
    return create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}/{db}"
    )