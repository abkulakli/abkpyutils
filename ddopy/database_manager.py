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

    def add(self, obj):
        self._open_session().add(obj)
        self._commit_session()

    def get(self, obj):
        return self._open_session().query(obj).first()

    def _open_session(self):
        if self._active_session is None:
            self._active_session = self._session_maker()
        return self._active_session

    def _commit_session(self):
        if self._active_session is not None:
            self._active_session.commit()

