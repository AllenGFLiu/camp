from sqlalchemy import Column, Integer, String, Float
# from flask_sqlalchemy import SQLAlchemy

# from app import db
import sys
sys.path.append('..')
from database import Base

class Comment(Base):
    __tablename__ = 'zhihu_comment'

    id = Column(String, primary_key=True)
    user_name = Column(String(1000))
    comment = Column(String(100000))
