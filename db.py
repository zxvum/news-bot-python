from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем подключение к базе данных
engine = create_engine("sqlite:///news.db")  # Здесь можно указать ваше подключение к базе данных

# Создаем базовый класс моделей с помощью declarative_base
Base = declarative_base()


# Определяем модель User
class User(Base):
    __tablename__ = "users"  # Название таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Поле с идентификатором пользователя (первичный ключ)
    chat_id = Column(String, nullable=False, unique=True)


# Создаем таблицу в базе данных, если она еще не существует
Base.metadata.create_all(engine)

# Создаем сессию для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()
