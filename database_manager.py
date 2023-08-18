from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseManager:
    def __init__(self, db_url):
        self._engine = create_engine(db_url, echo=False)
        self._session_maker = sessionmaker(bind=self._engine)
        self._active_session = None

    def create_session(self):
        if self._active_session is None:
            self._active_session = self._session_maker()
        return self._active_session

    def close_session(self):
        if self._active_session is not None:
            self._active_session.close()
            self._active_session = None
