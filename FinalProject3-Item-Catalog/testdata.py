from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Users, Base, SaleItem, Category

engine = create_engine('sqlite:///salesite.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()
# Menu for UrbanBurger


user1 = Users(name="George Smith", social_id="23786543")
session.add(user1)
session.commit()

category1 = Category(name="Electronics", description="Electronic items, PCs HiFis etc")
session.add(category1)
session.commit()

