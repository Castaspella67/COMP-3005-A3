#This file makes sessions with postgres
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Get password from env
load_dotenv()
postgres_user = "postgres"
postgres_pw = os.getenv("POSTGRES_PW")
port = "5432"
# db_name="comp3005a3"
db_name="postgres"
#Use psycopg to connect to postgresql, connecting on the specified port and opening the specified db
db_url = f"postgresql+psycopg://{postgres_user}:{postgres_pw}@localhost:{port}/{db_name}"

#Start POSTGRES session
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)