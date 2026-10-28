from sqlalchemy import Column, BigInteger, String, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key= True, nullable = False)
    f_name: Mapped[str | None] = mapped_column(String(60))
    l_name: Mapped[str | None] = mapped_column(String(60))
    age: Mapped[int| None] = mapped_column(Integer)
    gender: Mapped[str | None] = mapped_column(String(10))
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(str(100), unique=True, nullable = False)
    hashed_password: Mapped[str] = mapped_column(Text, nullable=False)
    bio: Mapped[str | None] = mapped_column(Text)
    location: Mapped[str | None] = mapped_column(Text)
    instruments: Mapped[list[str] | None] = mapped_column(ARRAY(Text))
    