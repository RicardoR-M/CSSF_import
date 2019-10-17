from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class ATF(base):
    __tablename__ = 'ATF'
