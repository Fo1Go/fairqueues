from bot.utils.db import Base, engine


def create_all_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_all_tables()
