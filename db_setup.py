from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base



# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy


# class Config(object):
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///planner.db?check_same_thread=False'


# db = SQLAlchemy()


# def create_app():
#     app.config.from_object(Config)
#     app = Flask(__name__)
#     db.init_app(app)

# engine = create_engine('sqlite:///planner.db?check_same_thread=False')

engine = create_engine('sqlite:///planner.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    import models
    Base.metadata.create_all(bind=engine)



