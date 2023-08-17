from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url, echo=False)
        self.session = None

    def create_session(self):
        if self.session == None:
            self.session = sessionmaker(bind=self.engine)

        return self.session()

    def close_session(self):
        if self.session != None:
            self.session.close()
        self.session = None