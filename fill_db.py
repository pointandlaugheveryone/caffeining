from models import Store, Drink
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()


albert = Store(name='Albert', logo_url='src/static/images/albert.svg')
billa = Store(name='Billa', logo_url='src/static/images/billa.svg')
globus = Store(name='Globus', logo_url='src/static/images/globus.svg')
kaufland = Store(name='Kaufland', logo_url='src/static/images/kaufland.svg')
lidl = Store(name='Lidl', logo_url='src/static/images/lidl.svg')
norma = Store(name='Norma', logo_url='src/static/images/norma.svg')
penny = Store(name='Penny', logo_url='src/static/images/penny.svg')
tesco = Store(name='Tesco', logo_url='src/static/images/tesco.svg')
#session.add_all([])

#TODO: add urls to fetch api 4 drinks
drink1 = Drink(name='Drink 1', normal_cost=1.0, discount_cost=1.0, image_url='src/static/images/', is_zero=False)
drink2 = Drink(name='Drink 2', normal_cost=1.0, discount_cost=1.0, image_url='src/static/images/', is_zero=True)
#session.add_all([])


session.commit()