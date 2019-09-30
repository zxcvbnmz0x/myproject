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


class Stuffrepository(models.Model):
    autoid = models.AutoField(primary_key=True)
    ciid = models.IntegerField(db_column='ciID')  # Field name made lowercase.
    pltype = models.IntegerField(db_column='plType')  # Field name made lowercase.
    stuffid = models.CharField(db_column='StuffID', max_length=10)  # Field name made lowercase.
    stuffname = models.CharField(db_column='StuffName', max_length=30)  # Field name made lowercase.
    stufftype = models.IntegerField(db_column='StuffType')  # Field name made lowercase.
    stuffkind = models.CharField(db_column='StuffKind', max_length=100)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=60)  # Field name made lowercase.
    package = models.CharField(db_column='Package', max_length=30)  # Field name made lowercase.
    bpunit = models.CharField(db_column='bpUnit', max_length=20)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=20)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.PositiveIntegerField(db_column='spAmount')  # Field name made lowercase.
    mpamount = models.PositiveIntegerField(db_column='mpAmount')  # Field name made lowercase.
    basicunit = models.CharField(db_column='BasicUnit', max_length=20)  # Field name made lowercase.
    producer = models.CharField(db_column='Producer', max_length=100)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=100)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=100)  # Field name made lowercase.
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    expireddate = models.DateField(db_column='ExpiredDate')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=8, decimal_places=6)  # Field name made lowercase.
    position = models.CharField(max_length=60)
    basicamount = models.DecimalField(db_column='BasicAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    checkintime = models.DateTimeField(db_column='CheckInTime')  # Field name made lowercase.
    putintime = models.DateTimeField(db_column='PutinTime')  # Field name made lowercase.
    piamount = models.DecimalField(db_column='piAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.
    water = models.DecimalField(db_column='Water', max_digits=8, decimal_places=2)  # Field name made lowercase.
    content = models.DecimalField(db_column='Content', max_digits=8, decimal_places=2)  # Field name made lowercase.
    lrid = models.IntegerField(db_column='lrID')  # Field name made lowercase.
    checkdate = models.DateField(db_column='CheckDate')  # Field name made lowercase.
    status = models.IntegerField()
    chargerid = models.CharField(db_column='ChargerID', max_length=10)  # Field name made lowercase.
    chargername = models.CharField(db_column='ChargerName', max_length=30)  # Field name made lowercase.
    cunit = models.CharField(db_column='cUnit', max_length=20)  # Field name made lowercase.
    ceffect = models.DecimalField(db_column='cEffect', max_digits=14, decimal_places=4)  # Field name made lowercase.
    cstandard = models.DecimalField(db_column='cStandard', max_digits=14, decimal_places=3)  # Field name made lowercase.
    content1 = models.DecimalField(db_column='Content1', max_digits=14, decimal_places=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stuffrepository'

