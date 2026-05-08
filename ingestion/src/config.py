import os
from sqlalchemy import create_engine

def get_engine():
    # Credentials are read from enviornment variables at call time,
    # not at import time. Prevents failure if env variables aren't set 
    # when module is first imported. 
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST", "postgres")
    db = os.getenv("POSTGRES_DB")
    
    # Psycopg2 is underlying driver. SQLAlchemy uses it to
    # communicate with Postgres but abstracts the low level connection handling. 
    return create_engine(
        f"postgresql+psycopg2://{user}:{password}@{host}/{db}"
    )