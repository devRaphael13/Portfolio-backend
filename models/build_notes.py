from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Paragraph(Base):
    __tablename__ = "paragraphs"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    order = Column(Integer, nullable=False)
    build_note_id = Column(Integer, ForeignKey("build_notes.id"), nullable=False)
    build_note = relationship("BuildNote", back_populates="paragraphs")

class BuildNote(Base):
    __tablename__ = "build_notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(240), nullable=False)
    tagline = Column(String(240), nullable=False)
    read_time = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    paragraphs = relationship("Paragraph", back_populates="build_note", cascade="all, delete-orphan")
