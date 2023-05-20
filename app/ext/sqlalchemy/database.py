# More on this stuff
# https://flask.palletsprojects.com/en/2.1.x/patterns/sqlalchemy/
# https://docs.sqlalchemy.org/en/14/orm/session_basics.html#session-getting

from sqlalchemy.orm import scoped_session
from app.app import db

db_session : scoped_session = db.session
db_select = db.select
