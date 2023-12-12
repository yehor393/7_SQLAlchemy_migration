from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configparser


# file_config = pathlib.Path(__file__).parent.parent.joinpath('config.ini')
config = configparser.ConfigParser()
config.read('config.ini')

print("Config contents:", dict(config.items('DB')))

username = config.get('DB', 'USER')
password = config.get('DB', 'PASSWORD')
db_name = config.get('DB', 'DB_NAME')
domain = config.get('DB', 'DOMAIN')

url = f'postgresql://{username}:{password}@{domain}:5432/{db_name}'
Base = declarative_base()
engine = create_engine(url, echo=True, pool_size=5)

DBSession = sessionmaker(bind=engine)
session = DBSession()
