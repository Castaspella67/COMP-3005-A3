#Use the session created
from datetime import date
from database_sessions import engine
from sqlalchemy import Date
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import create_engine, Column, Integer, String, Date

#https://docs.sqlalchemy.org/en/21/orm/quickstart.html

class Base(DeclarativeBase):
    pass
class Student(Base):
    __tablename__ = "students"
    student_id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    enrollment_date: Mapped[date] = mapped_column(Date)

#https://docs.sqlalchemy.org/en/21/orm/quickstart.html#emit-create-table-ddl
Base.metadata.create_all(engine)
print("Setup table 'students'!")