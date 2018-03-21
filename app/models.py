from sqlalchemy import Column, String, Integer, Date, Sequence
from config import Config

try:
    class FeatureRequestApp(Config.base):
        """Simple database model to track event attendees."""    
        __tablename__ = 'FeatureRequestApp'
        id = Column('id', Integer, Sequence('feature_id_seq'),unique=True,primary_key=True)
        title = Column(String(250),unique=True)
        description = Column(String(1000))
        client = Column(String(100)) 
        clientPriority = Column(Integer())
        targetDate = Column(Date())
        productArea = Column(String(100))

        def __init__(self, title, description, client, clientpriority, targetdate, productarea):
            self.title = title
            self.description = description
            self.client = client
            self.clientPriority = clientpriority
            self.targetDate = targetdate
            self.productArea = productarea

    Config.base.metadata.create_all(Config.db)
except ArgumentError as argexp:
    print('missing connection string or primary key', argexp)

except UnboundExecutionError as unexp:
    print('SQL was attempted without a database connection to execute it on', unexp)

except IndexError as indexerror:
    print('Missing Table Name', indexerror)

except TypeError as typeerror:
    print('Check Params', typeerror)

except TimeoutError as timeout:
    print('Connection TimedOut', timeout)