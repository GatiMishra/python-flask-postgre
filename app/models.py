from app import DB

try:
    class FeatureRequestApp(DB.Model):
        """Simple database model to track event attendees."""
    
        __tablename__ = 'FeatureRequestApp'
        id = DB.Column('id', DB.Integer, DB.Sequence('feature_id_seq'),unique=True,primary_key=True)
        title = DB.Column(DB.String(250),unique=True)
        description = DB.Column(DB.String(1000))
        client = DB.Column(DB.String(100)) 
        clientPriority = DB.Column(DB.Integer())
        targetDate = DB.Column(DB.Date())
        productArea = DB.Column(DB.String(100))

        def __init__(self, title, description, client, clientpriority, targetdate, productarea):
            self.title = title
            self.description = description
            self.client = client
            self.clientPriority = clientpriority
            self.targetDate = targetdate
            self.productArea = productarea

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