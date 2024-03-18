from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text

# Define SQLAlchemy base
class Base(DeclarativeBase):
    pass

# Define Reminder model
class Reminders(Base):
    __tablename__ = "reminders"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)
    date: Mapped[str] = mapped_column(String(50))
    message: Mapped[str] = mapped_column(Text)
