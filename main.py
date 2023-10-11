from sqlalchemy import create_engine
engine = create_engine('sqlite:///identifier.sqlite', echo=True)
from sqlalchemy.orm import Session
session = Session(engine)
from models import Claims
from sqlalchemy import select
stmt = select(Claims)
for t_claims in session.scalars(stmt):
    print(t_claims)
