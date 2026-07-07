from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.mutable import Mutable
from sqlalchemy.dialects.postgresql import JSONB
from database import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    icon_name = Column(String(40), nullable=False)
    name = Column(String(40), nullable=False)
    tagline = Column(String(240), nullable=False)
    features = Column(Mutable.as_mutable(JSONB), default=list)
