from django.db import models,connection

# Create your models here.
def selfcont(self,params):
    cursor = connection.cursor()
    cursor.execute(self, params)
    rows = cursor.fetchall()

    columns_name = list(name[0] for name in cursor.description)
    p = {}
    i = 0
    for item in rows:
        #p = ToJSON.toJSON(list(item))
        p[i] = dict(zip(columns_name, tupleToJSON(item)))
        i = i + 1
    return p


def tupleToJSON(self):
    import datetime, decimal
    d = []
    for attr in self:
            d.append(str(attr))

    return d

def toJSON(self):
    import datetime, decimal
    d = {}
    for attr in self:
        if isinstance(attr, datetime.datetime):
            #d.append(str(attr))
            d[attr] = datetime.datetime(self[attr])
        elif isinstance(attr, decimal.Decimal):
            d[attr] = float(self[attr])
        else:
            d[attr] = str(self[attr])

    return d

