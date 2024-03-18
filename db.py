from sqlalchemy.orm import Session
from sqlalchemy import create_engine

#connecting to databse
engine = create_engine('mysql://root:@localhost/')

def db_session():
    """
    Function to create and return a database session using SQLAlchemy engine.
    
    Returns:
    Session: SQLAlchemy Session object for interacting with the database.
    """
    conn = Session(engine)
    return conn
