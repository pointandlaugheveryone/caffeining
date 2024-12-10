from models import Store, Drink
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Create and add stores
store1 = Store(name='Store 1', logo_url='http://example.com/logo1.png')
store2 = Store(name='Store 2', logo_url='http://example.com/logo2.png')
session.add_all([store1, store2])

# Create and add drinks
drink1 = Drink(name='Drink 1', normal_cost=10.0, discount_cost=8.0, image_url='http://example.com/drink1.png', is_zero=False)
drink2 = Drink(name='Drink 2', normal_cost=12.0, discount_cost=10.0, image_url='http://example.com/drink2.png', is_zero=True)
session.add_all([drink1, drink2])

# Commit the session
session.commit()