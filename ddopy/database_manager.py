from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DatabaseManager:
    def __init__(self, db_url):
        self._engine = create_engine(db_url, echo=False)
        self._session_maker = sessionmaker(bind=self._engine)
        self._active_session = None

        Base.metadata.create_all(self._engine)

    def get_base(self):
        return self._base

    def open_session(self):
        if self._active_session is None:
            self._active_session = self._session_maker()
        return self._active_session

    def close_session(self):
        if self._active_session is not None:
            self._active_session.close()
            self._active_session = None
