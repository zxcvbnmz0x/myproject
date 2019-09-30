from django.db import models
from datetime import datetime
# Create your models here.

class Menu(models.Model):
    autoid              = models.IntegerField(primary_key=True)
    article             = models.CharField(max_length=30)
    parent_article_id   = models.IntegerField(default=0)
    url                 = models.CharField(max_length=40)
    def __str__(self):
        return self.article

    class Meta:
        managed = False
        db_table = 'menu'

'''
class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
'''


class Auxilliaryrecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    kind = models.IntegerField(db_column='Kind')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=30)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=30)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=120)  # Field name made lowercase.
    classtitle = models.CharField(db_column='ClassTitle', max_length=60)  # Field name made lowercase.
    ar = models.TextField()

    class Meta:
        managed = False
        db_table = 'auxilliaryrecords'


class Checkitems(models.Model):
    autoid = models.AutoField(primary_key=True)
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=60)  # Field name made lowercase.
    stuffid = models.CharField(db_column='StuffID', max_length=20)  # Field name made lowercase.
    itemtype = models.IntegerField(db_column='ItemType')  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=30)  # Field name made lowercase.
    restype = models.IntegerField(db_column='ResType')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=30)  # Field name made lowercase.
    referencevalue = models.CharField(db_column='ReferenceValue', max_length=200)  # Field name made lowercase.
    expr = models.CharField(db_column='Expr', max_length=100)  # Field name made lowercase.
    exprremark = models.CharField(db_column='ExprRemark', max_length=200)  # Field name made lowercase.
    fp = models.IntegerField()
    remark = models.CharField(db_column='Remark', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'checkitems'


class Cleanconfirmity(models.Model):
    autoid = models.AutoField(primary_key=True)
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    lpid = models.IntegerField(db_column='lpID')  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=30)  # Field name made lowercase.
    linepostname = models.CharField(db_column='LinePostName', max_length=30)  # Field name made lowercase.
    lastprodid = models.CharField(db_column='LastProdID', max_length=10)  # Field name made lowercase.
    lastprodname = models.CharField(db_column='LastProdName', max_length=30)  # Field name made lowercase.
    lastbatchno = models.CharField(db_column='LastBatchNo', max_length=60)  # Field name made lowercase.
    prodid = models.CharField(db_column='ProdID', max_length=10)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=60)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=30)  # Field name made lowercase.
    cleanerid = models.CharField(db_column='CleanerID', max_length=10)  # Field name made lowercase.
    cleanername = models.CharField(db_column='CleanerName', max_length=30)  # Field name made lowercase.
    cleandate = models.DateField(db_column='CleanDate')  # Field name made lowercase.
    checkerid = models.CharField(db_column='CheckerID', max_length=10)  # Field name made lowercase.
    checkername = models.CharField(db_column='CheckerName', max_length=30)  # Field name made lowercase.
    checkdate = models.DateField(db_column='CheckDate')  # Field name made lowercase.
    validdate = models.DateField(db_column='ValidDate')  # Field name made lowercase.
    seccleanerid = models.CharField(db_column='secCleanerID', max_length=10)  # Field name made lowercase.
    seccleanername = models.CharField(db_column='secCleanerName', max_length=30)  # Field name made lowercase.
    seccleandate = models.DateField(db_column='secCleanDate')  # Field name made lowercase.
    seccheckerid = models.CharField(db_column='secCheckerID', max_length=10)  # Field name made lowercase.
    seccheckername = models.CharField(db_column='secCheckerName', max_length=30)  # Field name made lowercase.
    seccheckdate = models.DateField(db_column='secCheckDate')  # Field name made lowercase.
    iscopy = models.IntegerField(db_column='IsCopy')  # Field name made lowercase.
    origid = models.IntegerField(db_column='OrigID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cleanconfirmity'


class Clerkdept(models.Model):
    clerkid = models.CharField(db_column='ClerkID', primary_key=True, max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=30)  # Field name made lowercase.
    defaultdept = models.IntegerField(db_column='DefaultDept')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clerkdept'
        unique_together = (('clerkid', 'deptid'),)


class Clerkexperience(models.Model):
    autoid = models.AutoField(primary_key=True)
    clerkid = models.CharField(db_column='ClerkID', max_length=30)  # Field name made lowercase.
    fromdate = models.DateField(db_column='FromDate')  # Field name made lowercase.
    todate = models.DateField(db_column='ToDate')  # Field name made lowercase.
    experience = models.CharField(max_length=200)
    position = models.CharField(max_length=30)
    exptype = models.IntegerField(db_column='ExpType')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clerkexperience'


class Clerks(models.Model):
    clerkname = models.CharField(db_column='ClerkName', max_length=60)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=2)  # Field name made lowercase.
    birthday = models.DateField(db_column='Birthday',default='0000-00-00',blank=True)  # Field name made lowercase.
    entranceday = models.DateField(db_column='EntranceDay',default='0000-00-00',blank=True)  # Field name made lowercase.
    edudegree = models.CharField(db_column='EduDegree', max_length=40)  # Field name made lowercase.
    special = models.CharField(db_column='Special', max_length=60)  # Field name made lowercase.
    schoolname = models.CharField(db_column='SchoolName', max_length=100)  # Field name made lowercase.
    marrystatus = models.CharField(db_column='MarryStatus', max_length=20)  # Field name made lowercase.
    idno = models.CharField(db_column='IDNo', max_length=30)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=230)  # Field name made lowercase.
    telno = models.CharField(db_column='TelNo', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=60)  # Field name made lowercase.
    rank = models.IntegerField(db_column='Rank')  # Field name made lowercase.
    techtitle = models.CharField(db_column='TechTitle', max_length=30)  # Field name made lowercase.
    inputcode = models.CharField(db_column='InputCode', max_length=30)  # Field name made lowercase.
    lastupdatepassword = models.DateTimeField(db_column='LastUpdatePassword',default=datetime.now,blank=True)  # Field name made lowercase.
    lastlogin = models.DateTimeField(db_column='LastLogin',default='0000-00-00 00:00:00',blank=True)  # Field name made lowercase.
    useroption = models.PositiveIntegerField(db_column='UserOption')  # Field name made lowercase.
    healthstatus = models.CharField(db_column='HealthStatus', max_length=30)  # Field name made lowercase.
    policystatus = models.CharField(db_column='PolicyStatus', max_length=30)  # Field name made lowercase.
    native = models.CharField(db_column='Native', max_length=200)  # Field name made lowercase.
    nation = models.CharField(db_column='Nation', max_length=30)  # Field name made lowercase.
    strongsuit = models.CharField(db_column='StrongSuit', max_length=200)  # Field name made lowercase.
    portraitid = models.IntegerField(db_column='PortraitID')  # Field name made lowercase.
    icsn = models.CharField(db_column='ICSN', max_length=50)  # Field name made lowercase.
    pid = models.CharField(db_column='pID', unique=True, max_length=20)  # Field name made lowercase.
    clerkid = models.AutoField(db_column='ClerkID', primary_key=True)  # Field name made lowercase.
    disabled = models.IntegerField(db_column='Disabled')  # Field name made lowercase.
    dismissdate = models.DateField(db_column='DismissDate',default='0000-00-00',blank=True)  # Field name made lowercase.

    def  __str__(self):
        return self.clerkname

    class Meta:
        managed = False
        db_table = 'clerks'


class Clerkthbatchrecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    kind = models.IntegerField()
    creatorid = models.CharField(db_column='CreatorID', max_length=30)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=30)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=200)  # Field name made lowercase.
    fromdate = models.DateField(db_column='FromDate')  # Field name made lowercase.
    todate = models.DateField(db_column='ToDate')  # Field name made lowercase.
    dotime = models.CharField(db_column='DoTime', max_length=40)  # Field name made lowercase.
    teacher = models.CharField(db_column='Teacher', max_length=30)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=60)  # Field name made lowercase.
    score = models.CharField(db_column='Score', max_length=30)  # Field name made lowercase.
    position = models.CharField(max_length=30)
    remark = models.CharField(db_column='Remark', max_length=200)  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clerkthbatchrecords'


class Clerktrainingrecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    clerkid = models.CharField(db_column='ClerkID', max_length=30)  # Field name made lowercase.
    fromdate = models.DateField(db_column='FromDate')  # Field name made lowercase.
    todate = models.DateField(db_column='ToDate')  # Field name made lowercase.
    training = models.CharField(db_column='Training', max_length=200)  # Field name made lowercase.
    teachingtime = models.CharField(db_column='TeachingTime', max_length=20)  # Field name made lowercase.
    teacher = models.CharField(db_column='Teacher', max_length=30, blank=True, null=True)  # Field name made lowercase.
    score = models.CharField(db_column='Score', max_length=10)  # Field name made lowercase.
    position = models.CharField(max_length=20)
    thbrid = models.IntegerField(db_column='thbrID')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clerktrainingrecords'


class Client(models.Model):
    clientid = models.CharField(db_column='ClientID', unique=True, max_length=30)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=60)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    postzip = models.CharField(db_column='PostZip', max_length=10)  # Field name made lowercase.
    telno = models.CharField(db_column='TelNo', max_length=100)  # Field name made lowercase.
    faxno = models.CharField(db_column='FaxNo', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=60)  # Field name made lowercase.
    homepage = models.CharField(db_column='HomePage', max_length=100)  # Field name made lowercase.
    charger = models.CharField(db_column='Charger', max_length=30)  # Field name made lowercase.
    linkman = models.CharField(db_column='Linkman', max_length=30)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=30)  # Field name made lowercase.
    bankaccount = models.CharField(db_column='BankAccount', max_length=100)  # Field name made lowercase.
    chargertitle = models.CharField(db_column='ChargerTitle', max_length=20)  # Field name made lowercase.
    chargertelno = models.CharField(db_column='ChargerTelNo', max_length=100)  # Field name made lowercase.
    taxno = models.CharField(db_column='TaxNo', max_length=100)  # Field name made lowercase.
    salerid = models.CharField(db_column='SalerID', max_length=10)  # Field name made lowercase.
    salername = models.CharField(db_column='SalerName', max_length=30)  # Field name made lowercase.
    inputcode = models.CharField(db_column='InputCode', max_length=60)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200)  # Field name made lowercase.
    totalmoney = models.DecimalField(db_column='TotalMoney', max_digits=16, decimal_places=2)  # Field name made lowercase.
    dues = models.DecimalField(db_column='Dues', max_digits=12, decimal_places=2)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=40)  # Field name made lowercase.
    autoid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'client'


class Clientcomplainnotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    clientid = models.CharField(db_column='ClientID', max_length=30)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    prodid = models.CharField(db_column='ProdID', max_length=10)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=10)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=30, blank=True, null=True)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=30)  # Field name made lowercase.
    complainer = models.CharField(db_column='Complainer', max_length=20)  # Field name made lowercase.
    telno = models.CharField(db_column='TelNo', max_length=30)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    zip = models.CharField(max_length=20)
    comp = models.TextField()
    receiverid = models.CharField(db_column='ReceiverID', max_length=10)  # Field name made lowercase.
    receivername = models.CharField(db_column='ReceiverName', max_length=30)  # Field name made lowercase.
    receivedate = models.DateField(db_column='ReceiveDate')  # Field name made lowercase.
    investigation = models.TextField(db_column='Investigation')  # Field name made lowercase.
    qcid = models.CharField(db_column='QCID', max_length=10)  # Field name made lowercase.
    qcname = models.CharField(db_column='QCName', max_length=30)  # Field name made lowercase.
    qcdate = models.DateField(db_column='qcDate')  # Field name made lowercase.
    leadercomment = models.TextField(db_column='LeaderComment')  # Field name made lowercase.
    leaderid = models.CharField(db_column='LeaderID', max_length=10)  # Field name made lowercase.
    leadername = models.CharField(db_column='LeaderName', max_length=30)  # Field name made lowercase.
    ldate = models.DateField(db_column='lDate')  # Field name made lowercase.
    localadmincomment = models.TextField(db_column='LocalAdminComment', blank=True, null=True)  # Field name made lowercase.
    lacdate = models.DateField(db_column='lacDate')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clientcomplainnotes'


class Complainsupplyer(models.Model):
    autoid = models.AutoField(primary_key=True)
    supid = models.CharField(db_column='SupID', max_length=20)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    compdate = models.DateField(db_column='CompDate')  # Field name made lowercase.
    cause = models.TextField()
    reply = models.TextField()
    replyer = models.CharField(db_column='Replyer', max_length=30)  # Field name made lowercase.
    replyresult = models.CharField(db_column='ReplyResult', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'complainsupplyer'


class Department(models.Model):
    deptid = models.CharField(db_column='DeptID', primary_key=True, max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=60)  # Field name made lowercase.
    depttype = models.CharField(db_column='DeptType', max_length=30)  # Field name made lowercase.
    inputcode = models.CharField(db_column='InputCode', max_length=60)  # Field name made lowercase.
    sectiontype = models.IntegerField(db_column='SectionType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'department'


class Deptselfcheckitems(models.Model):
    autoid = models.AutoField(primary_key=True)
    dscrid = models.IntegerField(db_column='dscrID')  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=40)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=200)  # Field name made lowercase.
    cdeptid = models.CharField(db_column='cDeptID', max_length=20)  # Field name made lowercase.
    cdeptname = models.CharField(db_column='cDeptName', max_length=30)  # Field name made lowercase.
    rdate = models.DateField(db_column='rDate')  # Field name made lowercase.
    cdate = models.DateField(db_column='cDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deptselfcheckitems'


class Deptselfcheckrecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    scrid = models.IntegerField(db_column='scrID')  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=20)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=20)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    kind = models.CharField(max_length=40)
    checkdate = models.DateField(db_column='CheckDate')  # Field name made lowercase.
    checkers = models.CharField(db_column='Checkers', max_length=20)  # Field name made lowercase.
    measure = models.TextField(db_column='Measure')  # Field name made lowercase.
    evaluation = models.TextField()
    conclusion = models.TextField(db_column='Conclusion')  # Field name made lowercase.
    chdate = models.DateField(db_column='chDate')  # Field name made lowercase.
    chargerid = models.CharField(db_column='ChargerID', max_length=30)  # Field name made lowercase.
    chargername = models.CharField(db_column='ChargerName', max_length=30)  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deptselfcheckrecords'
        unique_together = (('deptid', 'kind', 'scrid'),)


class Dictionary(models.Model):
    dictid = models.CharField(db_column='DictID', max_length=2)  # Field name made lowercase.
    dicttype = models.CharField(db_column='DictType', primary_key=True, max_length=16)  # Field name made lowercase.
    subid = models.CharField(db_column='SubID', max_length=2)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dictionary'
        unique_together = (('dicttype', 'dictid', 'subid'),)


class Dismissionrecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    clerkid = models.IntegerField(db_column='ClerkID', unique=True)  # Field name made lowercase.
    clerkname = models.CharField(db_column='ClerkName', max_length=30)  # Field name made lowercase.
    pid = models.CharField(db_column='pID', max_length=20)  # Field name made lowercase.
    position = models.CharField(max_length=30)
    applyform = models.TextField(db_column='ApplyForm')  # Field name made lowercase.
    applydate = models.DateField(db_column='ApplyDate')  # Field name made lowercase.
    deptadvice = models.TextField(db_column='DeptAdvice')  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    chargerid = models.CharField(db_column='ChargerID', max_length=10)  # Field name made lowercase.
    chargername = models.CharField(db_column='ChargerName', max_length=30)  # Field name made lowercase.
    chargerdate = models.DateField(db_column='ChargerDate')  # Field name made lowercase.
    adminadvice = models.TextField(db_column='AdminAdvice')  # Field name made lowercase.
    adminid = models.CharField(db_column='AdminID', max_length=10)  # Field name made lowercase.
    adminname = models.CharField(db_column='AdminName', max_length=30)  # Field name made lowercase.
    admindate = models.DateField(db_column='AdminDate')  # Field name made lowercase.
    finacialadvice = models.TextField(db_column='FinacialAdvice')  # Field name made lowercase.
    finacialid = models.CharField(db_column='FinacialID', max_length=10)  # Field name made lowercase.
    finacialname = models.CharField(db_column='FinacialName', max_length=30)  # Field name made lowercase.
    finacialdate = models.DateField(db_column='FinacialDate')  # Field name made lowercase.
    ceoadvice = models.TextField(db_column='CEOAdvice')  # Field name made lowercase.
    ceoid = models.CharField(db_column='CEOID', max_length=10)  # Field name made lowercase.
    ceoname = models.CharField(db_column='CEOName', max_length=30)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200)  # Field name made lowercase.
    status = models.IntegerField()
    ceodate = models.DateField(db_column='CEODate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dismissionrecords'

'''
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

'''



class Docdepartment(models.Model):
    docid = models.IntegerField(db_column='DocID', primary_key=True)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'docdepartment'
        unique_together = (('docid', 'deptid'),)


class Documents(models.Model):
    autoid = models.AutoField(primary_key=True)
    docno = models.CharField(db_column='DocNo', max_length=20)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=120)  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=30)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createdate = models.DateField(db_column='CreateDate')  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    auditorid = models.CharField(db_column='AuditorID', max_length=10)  # Field name made lowercase.
    auditorname = models.CharField(db_column='AuditorName', max_length=30)  # Field name made lowercase.
    auditdate = models.DateField(db_column='AuditDate')  # Field name made lowercase.
    approverid = models.CharField(db_column='ApproverID', max_length=10)  # Field name made lowercase.
    approvername = models.CharField(db_column='ApproverName', max_length=30)  # Field name made lowercase.
    approvedate = models.DateField(db_column='ApproveDate')  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate')  # Field name made lowercase.
    doc = models.TextField(db_column='Doc')  # Field name made lowercase.
    ext = models.CharField(max_length=10)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'documents'


class Drawstufflist(models.Model):
    autoid = models.AutoField(primary_key=True)
    srid = models.IntegerField(db_column='srID')  # Field name made lowercase.
    sdpid = models.IntegerField(db_column='sdpID')  # Field name made lowercase.
    stuffid = models.CharField(db_column='StuffID', max_length=20)  # Field name made lowercase.
    stuffname = models.CharField(db_column='StuffName', max_length=60)  # Field name made lowercase.
    stufftype = models.IntegerField(db_column='StuffType')  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=100)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=30)  # Field name made lowercase.
    package = models.CharField(db_column='Package', max_length=30)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=40)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=8, decimal_places=3)  # Field name made lowercase.
    producer = models.CharField(db_column='Producer', max_length=60)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=30)  # Field name made lowercase.
    lrid = models.IntegerField(db_column='lrID')  # Field name made lowercase.
    content = models.DecimalField(db_column='Content', max_digits=6, decimal_places=3)  # Field name made lowercase.
    water = models.DecimalField(db_column='Water', max_digits=6, decimal_places=3)  # Field name made lowercase.
    presamount = models.DecimalField(db_column='PresAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    checkamount = models.DecimalField(db_column='CheckAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    realamount = models.DecimalField(db_column='RealAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    drawamount = models.DecimalField(db_column='DrawAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    restamount = models.DecimalField(db_column='RestAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    backamount = models.DecimalField(db_column='BackAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    backtime = models.DateTimeField(db_column='BackTime')  # Field name made lowercase.
    remark = models.CharField(max_length=100)
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    destroyamount = models.DecimalField(db_column='DestroyAmount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    destroymethod = models.CharField(db_column='DestroyMethod', max_length=30)  # Field name made lowercase.
    destroydate = models.DateField(db_column='DestroyDate')  # Field name made lowercase.
    destroyerid = models.CharField(db_column='DestroyerID', max_length=10)  # Field name made lowercase.
    destroyername = models.CharField(db_column='DestroyerName', max_length=30)  # Field name made lowercase.
    supervisorid = models.CharField(db_column='SupervisorID', max_length=10)  # Field name made lowercase.
    supervisorname = models.CharField(db_column='SupervisorName', max_length=30)  # Field name made lowercase.
    ismainaux = models.IntegerField(db_column='IsMainAux')  # Field name made lowercase.
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'drawstufflist'


class Eqaccidentnotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    eqno = models.CharField(db_column='EqNo', max_length=30)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=30)  # Field name made lowercase.
    occurdate = models.DateTimeField(db_column='OccurDate')  # Field name made lowercase.
    factormen = models.CharField(db_column='FactorMen', max_length=50)  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=100)  # Field name made lowercase.
    injury = models.CharField(db_column='Injury', max_length=50)  # Field name made lowercase.
    brief = models.CharField(max_length=200)
    reason = models.CharField(max_length=200)
    prodloss = models.DecimalField(db_column='ProdLoss', max_digits=10, decimal_places=2)  # Field name made lowercase.
    stoploss = models.DecimalField(db_column='StopLoss', max_digits=10, decimal_places=2)  # Field name made lowercase.
    repairfee = models.DecimalField(db_column='RepairFee', max_digits=10, decimal_places=2)  # Field name made lowercase.
    otherloss = models.DecimalField(db_column='OtherLoss', max_digits=10, decimal_places=2)  # Field name made lowercase.
    treatadvice = models.CharField(db_column='TreatAdvice', max_length=200)  # Field name made lowercase.
    chargeradvice = models.CharField(db_column='ChargerAdvice', max_length=200)  # Field name made lowercase.
    directorid = models.CharField(db_column='DirectorID', max_length=10)  # Field name made lowercase.
    directorname = models.CharField(db_column='DirectorName', max_length=30)  # Field name made lowercase.
    managerid = models.CharField(db_column='ManagerID', max_length=10)  # Field name made lowercase.
    managername = models.CharField(db_column='ManagerName', max_length=30)  # Field name made lowercase.
    fillerid = models.CharField(db_column='FillerID', max_length=10)  # Field name made lowercase.
    fillername = models.CharField(db_column='FillerName', max_length=30)  # Field name made lowercase.
    filldate = models.DateField(db_column='FillDate')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eqaccidentnotes'


class Eqeventsdef(models.Model):
    autoid = models.AutoField(primary_key=True)
    eqno = models.CharField(db_column='EqNo', max_length=30)  # Field name made lowercase.
    evttype = models.IntegerField(db_column='EvtType')  # Field name made lowercase.
    alertmsg = models.CharField(db_column='AlertMsg', max_length=100)  # Field name made lowercase.
    intervals = models.IntegerField(db_column='Intervals')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eqeventsdef'


class Eqlubricantnotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    eqno = models.CharField(db_column='EqNo', max_length=30)  # Field name made lowercase.
    fillerid = models.CharField(db_column='FillerID', max_length=10)  # Field name made lowercase.
    fillername = models.CharField(db_column='FillerName', max_length=30)  # Field name made lowercase.
    ludate = models.DateField(db_column='luDate')  # Field name made lowercase.
    lupart = models.CharField(db_column='LuPart', max_length=30)  # Field name made lowercase.
    lubricant = models.CharField(db_column='Lubricant', max_length=100)  # Field name made lowercase.
    ration = models.DecimalField(max_digits=6, decimal_places=2)
    remark = models.CharField(max_length=60)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eqlubricantnotes'


class Eqnormaldocuments(models.Model):
    autoid = models.AutoField(db_column='AUTOID', primary_key=True)  # Field name made lowercase.
    eqno = models.CharField(db_column='EqNo', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=20)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=50)  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=30)  # Field name made lowercase.
    subkind = models.CharField(db_column='SubKind', max_length=20)  # Field name made lowercase.
    format = models.TextField(db_column='Format')  # Field name made lowercase.
    orientation = models.IntegerField(db_column='Orientation')  # Field name made lowercase.
    flag = models.IntegerField()
    formtype = models.PositiveIntegerField(db_column='FormType')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eqnormaldocuments'


class Eqrepairnotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    eqno = models.CharField(db_column='EqNo', max_length=30)  # Field name made lowercase.
    partrepairing = models.CharField(db_column='PartRepairing', max_length=30)  # Field name made lowercase.
    partreplacing = models.CharField(db_column='PartReplacing', max_length=30)  # Field name made lowercase.
    mainpoint = models.CharField(db_column='MainPoint', max_length=100)  # Field name made lowercase.
    testrunning = models.CharField(db_column='TestRunning', max_length=100)  # Field name made lowercase.
    wseqid = models.CharField(db_column='wsEqID', max_length=10)  # Field name made lowercase.
    wseqname = models.CharField(db_column='wsEqName', max_length=30)  # Field name made lowercase.
    operatorid = models.CharField(db_column='OperatorID', max_length=10)  # Field name made lowercase.
    operatorname = models.CharField(db_column='OperatorName', max_length=30)  # Field name made lowercase.
    repairerid = models.CharField(db_column='RepairerID', max_length=10)  # Field name made lowercase.
    repairername = models.CharField(db_column='RepairerName', max_length=30)  # Field name made lowercase.
    finishdate = models.DateField(db_column='FinishDate')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eqrepairnotes'


class Eqrunnotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    eqno = models.CharField(db_column='EqNo', max_length=30)  # Field name made lowercase.
    fillerid = models.CharField(db_column='FillerID', max_length=10)  # Field name made lowercase.
    fillername = models.CharField(db_column='FillerName', max_length=30)  # Field name made lowercase.
    filltime = models.DateTimeField(db_column='FillTime')  # Field name made lowercase.
    runstarttime = models.DateTimeField(db_column='RunStartTime')  # Field name made lowercase.
    runtime = models.IntegerField(db_column='RunTime')  # Field name made lowercase.
    runstatus = models.IntegerField(db_column='RunStatus')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=60)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=20)  # Field name made lowercase.
    dictid = models.CharField(db_column='DictID', max_length=20)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=20)  # Field name made lowercase.
    pid = models.IntegerField(db_column='pID')  # Field name made lowercase.
    rtype = models.IntegerField(db_column='rType')  # Field name made lowercase.
    postname = models.CharField(db_column='PostName', max_length=30)  # Field name made lowercase.
    maintenance = models.IntegerField(db_column='Maintenance')  # Field name made lowercase.
    startstatus = models.IntegerField(db_column='StartStatus')  # Field name made lowercase.
    stopstatus = models.IntegerField(db_column='StopStatus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eqrunnotes'


class Equipments(models.Model):
    eqno = models.CharField(db_column='EqNo', unique=True, max_length=30)  # Field name made lowercase.
    eqname = models.CharField(db_column='EqName', max_length=100)  # Field name made lowercase.
    eqtype = models.IntegerField(db_column='EqType')  # Field name made lowercase.
    serialno = models.CharField(db_column='SerialNo', max_length=30)  # Field name made lowercase.
    blueprint = models.CharField(db_column='BluePrint', max_length=30)  # Field name made lowercase.
    stuff = models.CharField(db_column='Stuff', max_length=100)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=50)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    manufacturer = models.CharField(db_column='Manufacturer', max_length=100)  # Field name made lowercase.
    indate = models.DateField(db_column='InDate')  # Field name made lowercase.
    maintainerid = models.CharField(db_column='MaintainerID', max_length=10)  # Field name made lowercase.
    maintainername = models.CharField(db_column='MaintainerName', max_length=30)  # Field name made lowercase.
    dimension = models.CharField(db_column='Dimension', max_length=30)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=30)  # Field name made lowercase.
    attachments = models.CharField(db_column='Attachments', max_length=100)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    instposition = models.CharField(db_column='InstPosition', max_length=50)  # Field name made lowercase.
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    scale = models.CharField(db_column='Scale', max_length=30)  # Field name made lowercase.
    presicion = models.CharField(db_column='Presicion', max_length=30)  # Field name made lowercase.
    validdate = models.DateField(db_column='ValidDate')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100)  # Field name made lowercase.
    status = models.IntegerField()
    verifydate = models.DateField(db_column='VerifyDate')  # Field name made lowercase.
    verifyunit = models.CharField(db_column='VerifyUnit', max_length=50)  # Field name made lowercase.
    verifyresult = models.CharField(db_column='VerifyResult', max_length=60)  # Field name made lowercase.
    autoid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'equipments'

class Forms(models.Model):
    autoid = models.AutoField(db_column='AUTOID', primary_key=True)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=7)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=20)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=50)  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=30)  # Field name made lowercase.
    subkind = models.CharField(db_column='SubKind', max_length=20)  # Field name made lowercase.
    format = models.TextField(db_column='Format')  # Field name made lowercase.
    orientation = models.IntegerField(db_column='Orientation')  # Field name made lowercase.
    flag = models.IntegerField()
    formtype = models.PositiveIntegerField(db_column='FormType')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    sdfid = models.IntegerField(db_column='sdfID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forms'


class Healthrecord(models.Model):
    autoid = models.AutoField(primary_key=True)
    clerkid = models.CharField(db_column='ClerkID', max_length=30)  # Field name made lowercase.
    checkdate = models.DateField(db_column='CheckDate')  # Field name made lowercase.
    checkitem = models.CharField(db_column='CheckItem', max_length=100)  # Field name made lowercase.
    hospital = models.CharField(db_column='Hospital', max_length=80)  # Field name made lowercase.
    healthstatus = models.CharField(db_column='HealthStatus', max_length=20)  # Field name made lowercase.
    remark = models.CharField(max_length=200)
    thbrid = models.IntegerField(db_column='thbrID')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'healthrecord'


class Imagelib(models.Model):
    autoid = models.AutoField(db_column='AUTOID', primary_key=True)  # Field name made lowercase.
    ext = models.CharField(db_column='Ext', max_length=10)  # Field name made lowercase.
    img = models.TextField()

    class Meta:
        managed = False
        db_table = 'imagelib'


class Labrecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    paperno = models.CharField(db_column='PaperNo', max_length=20)  # Field name made lowercase.
    labtype = models.IntegerField(db_column='LabType')  # Field name made lowercase.
    chkid = models.CharField(db_column='chkID', max_length=10)  # Field name made lowercase.
    chkname = models.CharField(db_column='chkName', max_length=30)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    package = models.CharField(db_column='Package', max_length=100)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=50)  # Field name made lowercase.
    ciid = models.IntegerField(db_column='ciID')  # Field name made lowercase.
    samplerid = models.CharField(db_column='SamplerID', max_length=10)  # Field name made lowercase.
    samplername = models.CharField(db_column='SamplerName', max_length=30)  # Field name made lowercase.
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.
    samplecount = models.DecimalField(db_column='SampleCount', max_digits=10, decimal_places=4)  # Field name made lowercase.
    sampleunit = models.CharField(db_column='SampleUnit', max_length=20)  # Field name made lowercase.
    checkamount = models.DecimalField(db_column='CheckAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    caunit = models.CharField(db_column='CAUnit', max_length=20)  # Field name made lowercase.
    applytime = models.DateTimeField(db_column='ApplyTime')  # Field name made lowercase.
    applyerid = models.CharField(db_column='ApplyerID', max_length=10)  # Field name made lowercase.
    applyername = models.CharField(db_column='ApplyerName', max_length=30)  # Field name made lowercase.
    applydeptid = models.CharField(db_column='ApplyDeptID', max_length=10)  # Field name made lowercase.
    applydeptname = models.CharField(db_column='ApplyDeptName', max_length=30)  # Field name made lowercase.
    applyremark = models.CharField(db_column='ApplyRemark', max_length=100)  # Field name made lowercase.
    checkgist = models.CharField(db_column='CheckGist', max_length=250)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    sampletime = models.DateTimeField(db_column='SampleTime')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=250)  # Field name made lowercase.
    reporttime = models.DateTimeField(db_column='ReportTime')  # Field name made lowercase.
    samplesource = models.CharField(db_column='SampleSource', max_length=50)  # Field name made lowercase.
    reporterid = models.CharField(db_column='ReporterID', max_length=10)  # Field name made lowercase.
    reportername = models.CharField(db_column='ReporterName', max_length=30)  # Field name made lowercase.
    reportdeptid = models.CharField(db_column='ReportDeptID', max_length=10)  # Field name made lowercase.
    reportdeptname = models.CharField(db_column='ReportDeptName', max_length=30)  # Field name made lowercase.
    expireddate = models.DateField(db_column='ExpiredDate')  # Field name made lowercase.
    status = models.IntegerField()
    papertype = models.IntegerField(db_column='PaperType')  # Field name made lowercase.
    checkerid = models.CharField(db_column='CheckerID', max_length=10)  # Field name made lowercase.
    checkername = models.CharField(db_column='CheckerName', max_length=30)  # Field name made lowercase.
    warrantorid = models.CharField(db_column='WarrantorID', max_length=10)  # Field name made lowercase.
    warrantorname = models.CharField(db_column='WarrantorName', max_length=30)  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    nosub = models.IntegerField(db_column='NoSub')  # Field name made lowercase.
    ittype = models.IntegerField(db_column='itType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'labrecords'


class Labrecordsdetail(models.Model):
    autoid = models.AutoField(primary_key=True)
    lrid = models.IntegerField(db_column='lrID')  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=30)  # Field name made lowercase.
    itemname = models.CharField(db_column='ItemName', max_length=60)  # Field name made lowercase.
    labvalue = models.CharField(db_column='LabValue', max_length=240)  # Field name made lowercase.
    restype = models.IntegerField(db_column='ResType')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=30)  # Field name made lowercase.
    referencevalue = models.CharField(db_column='ReferenceValue', max_length=200)  # Field name made lowercase.
    expr = models.CharField(db_column='Expr', max_length=100)  # Field name made lowercase.
    exprremark = models.CharField(db_column='ExprRemark', max_length=200)  # Field name made lowercase.
    result = models.CharField(db_column='Result', max_length=50)  # Field name made lowercase.
    checked = models.IntegerField(db_column='Checked')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'labrecordsdetail'


class Linepost(models.Model):
    autoid = models.AutoField(primary_key=True)
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    postname = models.CharField(db_column='PostName', max_length=100)  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=30)  # Field name made lowercase.
    options = models.PositiveIntegerField(db_column='Options')  # Field name made lowercase.
    workerid = models.CharField(db_column='WorkerID', max_length=10)  # Field name made lowercase.
    workername = models.CharField(db_column='WorkerName', max_length=30)  # Field name made lowercase.
    temp = models.DecimalField(db_column='Temp', max_digits=6, decimal_places=1)  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    humidity = models.DecimalField(db_column='Humidity', max_digits=6, decimal_places=2)  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'linepost'


class Linepostdocument(models.Model):
    autoid = models.AutoField(primary_key=True)
    lpid = models.IntegerField(db_column='lpID')  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    docid = models.IntegerField(db_column='DocID')  # Field name made lowercase.
    aid = models.IntegerField()
    rdid = models.IntegerField(db_column='rdID')  # Field name made lowercase.
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'linepostdocument'


class Logins(models.Model):
    autoid = models.AutoField(primary_key=True)
    authentype = models.IntegerField(db_column='AuthenType')  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=10)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=30)  # Field name made lowercase.
    ip = models.IntegerField(db_column='IP')  # Field name made lowercase.
    machinename = models.CharField(db_column='MachineName', max_length=60)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    icsn = models.IntegerField(db_column='ICSN')  # Field name made lowercase.
    logintime = models.DateTimeField(db_column='LoginTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'logins'


class Mail(models.Model):
    orderno = models.AutoField(primary_key=True)
    flag = models.IntegerField()
    senderid = models.CharField(db_column='SenderID', max_length=7)  # Field name made lowercase.
    sendername = models.CharField(db_column='senderName', max_length=20)  # Field name made lowercase.
    receiverid = models.CharField(db_column='ReceiverID', max_length=7)  # Field name made lowercase.
    receivername = models.CharField(db_column='ReceiverName', max_length=20)  # Field name made lowercase.
    sendtime = models.DateTimeField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail'


class Midproddrawnotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    container = models.IntegerField(db_column='Container')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=12)  # Field name made lowercase.
    workerid = models.CharField(db_column='WorkerID', max_length=10)  # Field name made lowercase.
    workername = models.CharField(db_column='WorkerName', max_length=30)  # Field name made lowercase.
    registrarid = models.CharField(db_column='RegistrarID', max_length=10)  # Field name made lowercase.
    registrarname = models.CharField(db_column='RegistrarName', max_length=30)  # Field name made lowercase.
    regtime = models.DateTimeField(db_column='RegTime')  # Field name made lowercase.
    drawerid = models.CharField(db_column='DrawerID', max_length=10)  # Field name made lowercase.
    drawername = models.CharField(db_column='DrawerName', max_length=30)  # Field name made lowercase.
    providerid = models.CharField(db_column='ProviderID', max_length=10)  # Field name made lowercase.
    providername = models.CharField(db_column='ProviderName', max_length=30)  # Field name made lowercase.
    drawtime = models.DateTimeField(db_column='DrawTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'midproddrawnotes'


class Modifyevents(models.Model):
    autoid = models.AutoField(primary_key=True)
    tableid = models.IntegerField(db_column='TableID')  # Field name made lowercase.
    paperno = models.CharField(db_column='PaperNo', max_length=40)  # Field name made lowercase.
    keyid = models.IntegerField(db_column='KeyID')  # Field name made lowercase.
    flag = models.IntegerField()
    msg = models.CharField(max_length=200)
    status = models.IntegerField()
    tabletype = models.IntegerField(db_column='tableType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modifyevents'


class Modifytracenotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    frmid = models.IntegerField(db_column='frmID')  # Field name made lowercase.
    tabid = models.IntegerField(db_column='TabID')  # Field name made lowercase.
    beforemodify = models.TextField(db_column='BeforeModify')  # Field name made lowercase.
    aftermodify = models.TextField(db_column='AfterModify')  # Field name made lowercase.
    modifierid = models.CharField(db_column='ModifierID', max_length=10)  # Field name made lowercase.
    modifiername = models.CharField(db_column='ModifierName', max_length=30)  # Field name made lowercase.
    modifiedtime = models.DateTimeField(db_column='ModifiedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modifytracenotes'


class Nonproductiveapply(models.Model):
    autoid = models.AutoField(primary_key=True)
    applydate = models.DateField(db_column='ApplyDate')  # Field name made lowercase.
    applyerid = models.CharField(db_column='ApplyerID', max_length=10)  # Field name made lowercase.
    applyername = models.CharField(db_column='ApplyerName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    approverid = models.CharField(db_column='ApproverID', max_length=10)  # Field name made lowercase.
    approvername = models.CharField(db_column='ApproverName', max_length=30)  # Field name made lowercase.
    approvedate = models.DateField(db_column='ApproveDate')  # Field name made lowercase.
    remark = models.CharField(max_length=200)
    status = models.IntegerField()
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nonproductiveapply'


class Nonproductivedictionary(models.Model):
    dictid = models.CharField(db_column='DictID', max_length=10)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=30)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=60)  # Field name made lowercase.
    dicttype = models.IntegerField(db_column='DictType')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    inputcode = models.CharField(db_column='InputCode', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nonproductivedictionary'


class Nonproductivedrawnotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    drawerid = models.CharField(db_column='DrawerID', max_length=10)  # Field name made lowercase.
    drawername = models.CharField(db_column='DrawerName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    approverid = models.CharField(db_column='ApproverID', max_length=10)  # Field name made lowercase.
    approvername = models.CharField(db_column='ApproverName', max_length=30)  # Field name made lowercase.
    applydate = models.DateField(db_column='ApplyDate')  # Field name made lowercase.
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.
    drawdate = models.DateField(db_column='DrawDate')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nonproductivedrawnotes'


class Nonproductiveio(models.Model):
    autoid = models.AutoField(primary_key=True)
    indate = models.DateField(db_column='InDate')  # Field name made lowercase.
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    checkerid = models.CharField(db_column='CheckerID', max_length=10)  # Field name made lowercase.
    checkername = models.CharField(db_column='CheckerName', max_length=30)  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=30)  # Field name made lowercase.
    papertype = models.IntegerField(db_column='PaperType')  # Field name made lowercase.
    status = models.IntegerField()
    remark = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'nonproductiveio'


class Npalist(models.Model):
    autoid = models.AutoField(primary_key=True)
    npaid = models.IntegerField(db_column='npaID')  # Field name made lowercase.
    dictid = models.CharField(db_column='DictID', max_length=10)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=30)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=60)  # Field name made lowercase.
    dicttype = models.IntegerField(db_column='DictType')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'npalist'


class Npapdnlist(models.Model):
    autoid = models.AutoField(primary_key=True)
    npdnid = models.IntegerField(db_column='npdnID')  # Field name made lowercase.
    dictid = models.CharField(db_column='DictID', max_length=10)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=30)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=60)  # Field name made lowercase.
    dicttype = models.IntegerField(db_column='DictType')  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'npapdnlist'


class Npdnlist(models.Model):
    autoid = models.AutoField(primary_key=True)
    npdnid = models.IntegerField(db_column='npdnID')  # Field name made lowercase.
    dictid = models.CharField(db_column='DictID', max_length=10)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=30)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=60)  # Field name made lowercase.
    dicttype = models.IntegerField(db_column='DictType')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'npdnlist'


class Npiolist(models.Model):
    autoid = models.AutoField(primary_key=True)
    npioid = models.IntegerField(db_column='npioID')  # Field name made lowercase.
    nprid = models.IntegerField(db_column='nprID')  # Field name made lowercase.
    dictid = models.CharField(db_column='DictID', max_length=10)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=30)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=60)  # Field name made lowercase.
    dicttype = models.IntegerField(db_column='DictType')  # Field name made lowercase.
    source = models.CharField(db_column='Source', max_length=30)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount')  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'npiolist'


class Observationrecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    srid = models.IntegerField(db_column='srID')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=20)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    obsdate = models.DateField(db_column='ObsDate')  # Field name made lowercase.
    obsperiod = models.CharField(db_column='ObsPeriod', max_length=20)  # Field name made lowercase.
    labdate = models.DateField(db_column='LabDate')  # Field name made lowercase.
    samplequantity = models.DecimalField(db_column='SampleQuantity', max_digits=10, decimal_places=4)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=30)  # Field name made lowercase.
    labid = models.CharField(db_column='LabID', max_length=20)  # Field name made lowercase.
    labname = models.CharField(db_column='LabName', max_length=30)  # Field name made lowercase.
    checkerid = models.CharField(db_column='CheckerID', max_length=20)  # Field name made lowercase.
    checkername = models.CharField(db_column='CheckerName', max_length=30)  # Field name made lowercase.
    conclusion = models.CharField(db_column='Conclusion', max_length=200)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200)  # Field name made lowercase.
    labstatus = models.IntegerField(db_column='LabStatus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'observationrecords'


class Oddmentdrawnotes(models.Model):
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    prid = models.IntegerField(db_column='prID')  # Field name made lowercase.
    drawerid = models.CharField(db_column='DrawerID', max_length=10)  # Field name made lowercase.
    drawername = models.CharField(db_column='DrawerName', max_length=30)  # Field name made lowercase.
    chargerid = models.CharField(db_column='ChargerID', max_length=10)  # Field name made lowercase.
    chargername = models.CharField(db_column='ChargerName', max_length=30)  # Field name made lowercase.
    qaid = models.CharField(db_column='QAID', max_length=10)  # Field name made lowercase.
    qaname = models.CharField(db_column='QAName', max_length=30)  # Field name made lowercase.
    amount = models.DecimalField(max_digits=14, decimal_places=4)
    drawdate = models.DateField(db_column='DrawDate')  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=60)  # Field name made lowercase.
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    status = models.IntegerField()
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.
    flag = models.IntegerField()
    dppid = models.IntegerField(db_column='dppID')  # Field name made lowercase.
    autoid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'oddmentdrawnotes'


class Ordergoods(models.Model):
    autoid = models.AutoField(primary_key=True)
    prodid = models.CharField(db_column='ProdID', max_length=10)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=30)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=60)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    bpunit = models.CharField(db_column='bpUnit', max_length=20)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=20)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.PositiveIntegerField(db_column='spAmount')  # Field name made lowercase.
    mpamount = models.PositiveIntegerField(db_column='mpAmount')  # Field name made lowercase.
    orderamount = models.DecimalField(db_column='OrderAmount', max_digits=12, decimal_places=3)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=12, decimal_places=2)  # Field name made lowercase.
    soid = models.IntegerField(db_column='soID')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=30)  # Field name made lowercase.
    hpunit = models.CharField(db_column='hpUnit', max_length=20)  # Field name made lowercase.
    bpamount = models.IntegerField(db_column='bpAmount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordergoods'


class Originalcheckpaper(models.Model):
    autoid = models.AutoField(primary_key=True)
    lrid = models.IntegerField(db_column='lrID')  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=100)  # Field name made lowercase.
    formcontent = models.TextField(db_column='FormContent')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=30)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'originalcheckpaper'


class Originalcheckpapersetting(models.Model):
    autoid = models.AutoField(primary_key=True)
    dictid = models.CharField(db_column='DictID', max_length=30)  # Field name made lowercase.
    itemtype = models.IntegerField(db_column='ItemType')  # Field name made lowercase.
    sdfid = models.IntegerField(db_column='sdfID')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=30)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'originalcheckpapersetting'


class Packstuffdestroynotes(models.Model):
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    chargerid = models.CharField(db_column='ChargerID', max_length=10)  # Field name made lowercase.
    chargername = models.CharField(db_column='ChargerName', max_length=30)  # Field name made lowercase.
    checkdate = models.DateField(db_column='CheckDate')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200)  # Field name made lowercase.
    kind = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'packstuffdestroynotes'
        unique_together = (('ppid', 'kind'),)


class Passnotes(models.Model):
    ppid = models.IntegerField(db_column='ppID', primary_key=True)  # Field name made lowercase.
    qapass = models.IntegerField(db_column='QAPass')  # Field name made lowercase.
    qaid = models.CharField(db_column='QAID', max_length=10)  # Field name made lowercase.
    qaname = models.CharField(db_column='QAName', max_length=30)  # Field name made lowercase.
    qadate = models.DateField(db_column='QADate')  # Field name made lowercase.
    qcid = models.CharField(db_column='QCID', max_length=10)  # Field name made lowercase.
    qcname = models.CharField(db_column='QCName', max_length=30)  # Field name made lowercase.
    qcdate = models.DateField(db_column='QCDate')  # Field name made lowercase.
    qcpass = models.IntegerField(db_column='QCPass')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=230)  # Field name made lowercase.
    passform = models.TextField(db_column='PassForm')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'passnotes'


class Planprescription(models.Model):
    autoid = models.AutoField(primary_key=True)
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    prodid = models.CharField(db_column='ProdID', max_length=20)  # Field name made lowercase.
    stuffkind = models.CharField(db_column='StuffKind', max_length=100)  # Field name made lowercase.
    stufftype = models.IntegerField(db_column='StuffType')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=12, decimal_places=3)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=30)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.IntegerField(db_column='spAmount')  # Field name made lowercase.
    ismainaux = models.IntegerField(db_column='IsMainAux')  # Field name made lowercase.
    flag = models.IntegerField()
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    hflag = models.IntegerField()
    samount = models.DecimalField(db_column='sAmount', max_digits=12, decimal_places=3)  # Field name made lowercase.
    extraamount = models.DecimalField(db_column='ExtraAmount', max_digits=8, decimal_places=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'planprescription'


class Postdocument(models.Model):
    autoid = models.AutoField(primary_key=True)
    wfid = models.IntegerField(db_column='wfID')  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    docid = models.IntegerField(db_column='DocID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'postdocument'


class Postequipments(models.Model):
    eqno = models.CharField(db_column='EqNo', max_length=10)  # Field name made lowercase.
    plid = models.IntegerField(db_column='plID')  # Field name made lowercase.
    postname = models.CharField(db_column='PostName', max_length=30)  # Field name made lowercase.
    rtype = models.IntegerField(db_column='rType')  # Field name made lowercase.
    autoid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'postequipments'
        unique_together = (('eqno', 'plid', 'postname', 'rtype'),)


class Postgmpfile(models.Model):
    autoid = models.AutoField(primary_key=True)
    wfid = models.IntegerField(db_column='wfID')  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    docid = models.IntegerField(db_column='DocID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'postgmpfile'


class Pplist(models.Model):
    autoid = models.AutoField(primary_key=True)
    paperno = models.CharField(db_column='PaperNo', max_length=20)  # Field name made lowercase.
    stuffid = models.CharField(db_column='StuffID', max_length=10)  # Field name made lowercase.
    stuffname = models.CharField(db_column='StuffName', max_length=30)  # Field name made lowercase.
    stufftype = models.IntegerField(db_column='StuffType')  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=60)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    producer = models.CharField(db_column='Producer', max_length=100)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=8, decimal_places=2)  # Field name made lowercase.
    arrivedamount = models.DecimalField(db_column='ArrivedAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    iposid = models.IntegerField(db_column='iPosID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pplist'


class Ppopqrcode(models.Model):
    autoid = models.AutoField(primary_key=True)
    ppodid = models.IntegerField(db_column='ppodID')  # Field name made lowercase.
    qr0 = models.CharField(max_length=60)
    flag = models.IntegerField()
    kind = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ppopqrcode'


class Prodqrcode(models.Model):
    autoid = models.AutoField(primary_key=True)
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    qrcode0 = models.CharField(db_column='QRCode0', max_length=200)  # Field name made lowercase.
    qrcode1 = models.CharField(db_column='QRCode1', max_length=200)  # Field name made lowercase.
    qrcode2 = models.CharField(db_column='QRCode2', max_length=200)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=200)  # Field name made lowercase.
    used = models.IntegerField(db_column='Used')  # Field name made lowercase.
    flag = models.IntegerField()
    qrcode3 = models.CharField(db_column='QRCode3', max_length=200)  # Field name made lowercase.
    bflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prodqrcode'


class Producingplan(models.Model):
    autoid = models.AutoField(primary_key=True)
    batchno = models.CharField(db_column='BatchNo', max_length=20)  # Field name made lowercase.
    prodid = models.CharField(db_column='ProdID', max_length=10)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=60)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=60)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    medkind = models.CharField(db_column='MedKind', max_length=100)  # Field name made lowercase.
    package = models.CharField(db_column='Package', max_length=100)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=30)  # Field name made lowercase.
    bpunit = models.CharField(db_column='bpUnit', max_length=20)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=20)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.PositiveIntegerField(db_column='spAmount')  # Field name made lowercase.
    mpamount = models.PositiveIntegerField(db_column='mpAmount')  # Field name made lowercase.
    basicamount = models.DecimalField(db_column='BasicAmount', max_digits=8, decimal_places=4)  # Field name made lowercase.
    basicunit = models.CharField(db_column='BasicUnit', max_length=20)  # Field name made lowercase.
    spprice = models.DecimalField(db_column='spPrice', max_digits=8, decimal_places=3)  # Field name made lowercase.
    productgist = models.CharField(db_column='ProductGist', max_length=60)  # Field name made lowercase.
    planamount = models.DecimalField(db_column='PlanAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    plantime = models.DateTimeField(db_column='PlanTime')  # Field name made lowercase.
    realamount = models.DecimalField(db_column='RealAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    labelimgid = models.IntegerField(db_column='LabelImgID')  # Field name made lowercase.
    instructorid = models.CharField(db_column='InstructorID', max_length=10)  # Field name made lowercase.
    instructorname = models.CharField(db_column='InstructorName', max_length=30)  # Field name made lowercase.
    qaauditorid = models.CharField(db_column='QAAuditorID', max_length=10)  # Field name made lowercase.
    qaauditorname = models.CharField(db_column='QAAuditorName', max_length=30)  # Field name made lowercase.
    qadate = models.DateField(db_column='QADate')  # Field name made lowercase.
    warrantorid = models.CharField(db_column='WarrantorID', max_length=10)  # Field name made lowercase.
    warrantorname = models.CharField(db_column='WarrantorName', max_length=30)  # Field name made lowercase.
    warrantdate = models.DateField(db_column='WarrantDate')  # Field name made lowercase.
    linename = models.CharField(db_column='LineName', max_length=60)  # Field name made lowercase.
    lineid = models.IntegerField(db_column='LineID')  # Field name made lowercase.
    workshopid = models.CharField(db_column='WorkshopID', max_length=10)  # Field name made lowercase.
    workshopname = models.CharField(db_column='WorkshopName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100)  # Field name made lowercase.
    statustime = models.DateTimeField(db_column='StatusTime')  # Field name made lowercase.
    status = models.IntegerField()
    midstatus = models.IntegerField(db_column='MidStatus')  # Field name made lowercase.
    prodstatus = models.IntegerField(db_column='ProdStatus')  # Field name made lowercase.
    executorid = models.CharField(db_column='ExecutorID', max_length=10)  # Field name made lowercase.
    executorname = models.CharField(db_column='ExecutorName', max_length=30)  # Field name made lowercase.
    executetime = models.DateTimeField(db_column='ExecuteTime')  # Field name made lowercase.
    expireddates = models.IntegerField(db_column='ExpiredDates')  # Field name made lowercase.
    bpconstitutorid = models.CharField(db_column='bpConstitutorID', max_length=10)  # Field name made lowercase.
    bpconstitutorname = models.CharField(db_column='bpConstitutorName', max_length=30)  # Field name made lowercase.
    bpconsdate = models.DateField(db_column='bpCOnsDate')  # Field name made lowercase.
    bpqaid = models.CharField(db_column='bpQAID', max_length=10)  # Field name made lowercase.
    bpqaname = models.CharField(db_column='bpQAName', max_length=30)  # Field name made lowercase.
    bpqadate = models.DateField(db_column='bpQADate')  # Field name made lowercase.
    bpwarrantorid = models.CharField(db_column='bpWarrantorID', max_length=10)  # Field name made lowercase.
    bpwarrantorname = models.CharField(db_column='bpWarrantorName', max_length=30)  # Field name made lowercase.
    bpwarrantdate = models.DateField(db_column='bpWarrantDate')  # Field name made lowercase.
    bpdate = models.DateField(db_column='bpDate')  # Field name made lowercase.
    pltype = models.IntegerField(db_column='plType')  # Field name made lowercase.
    bpexecutorid = models.CharField(db_column='bpExecutorID', max_length=10)  # Field name made lowercase.
    bpexecutorname = models.CharField(db_column='bpExecutorName', max_length=30)  # Field name made lowercase.
    bpexecutetime = models.DateTimeField(db_column='bpExecuteTime')  # Field name made lowercase.
    hpunit = models.CharField(db_column='hpUnit', max_length=20)  # Field name made lowercase.
    bpamount = models.IntegerField(db_column='bpAmount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producingplan'


class Productcheckindata(models.Model):
    autoid = models.AutoField(primary_key=True)
    pcipid = models.IntegerField(db_column='pcipID')  # Field name made lowercase.
    prid = models.IntegerField(db_column='prID')  # Field name made lowercase.
    dictid = models.CharField(db_column='DictID', max_length=20)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=60)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=60)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=30)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    spamount = models.DecimalField(db_column='spAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=30)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=30)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30)  # Field name made lowercase.
    flag = models.IntegerField()
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    package = models.CharField(db_column='Package', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productcheckindata'


class Productcheckinpaper(models.Model):
    autoid = models.AutoField(primary_key=True)
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    pikind = models.CharField(db_column='piKind', max_length=30)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=20)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=20)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    putintime = models.DateTimeField(db_column='PutInTime')  # Field name made lowercase.
    status = models.IntegerField()
    remark = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'productcheckinpaper'


class Productcheckreport(models.Model):
    autoid = models.AutoField(primary_key=True)
    dictid = models.CharField(db_column='DictID', max_length=20)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=30)  # Field name made lowercase.
    supid = models.CharField(db_column='SupID', max_length=20)  # Field name made lowercase.
    ppno = models.CharField(db_column='ppNo', max_length=20)  # Field name made lowercase.
    supname = models.CharField(db_column='SupName', max_length=60)  # Field name made lowercase.
    pidid = models.IntegerField(db_column='pidID')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=10, decimal_places=2)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    samplequantity = models.DecimalField(db_column='SampleQuantity', max_digits=10, decimal_places=2)  # Field name made lowercase.
    sendtime = models.DateField(db_column='SendTime')  # Field name made lowercase.
    senderid = models.CharField(db_column='SenderID', max_length=20)  # Field name made lowercase.
    sendername = models.CharField(db_column='SenderName', max_length=30)  # Field name made lowercase.
    checktime = models.DateField(db_column='CheckTime')  # Field name made lowercase.
    checkstandard = models.CharField(db_column='CheckStandard', max_length=100)  # Field name made lowercase.
    checkresult = models.CharField(db_column='CheckResult', max_length=200)  # Field name made lowercase.
    remark = models.TextField(db_column='Remark')  # Field name made lowercase.
    conclusion = models.IntegerField(db_column='Conclusion')  # Field name made lowercase.
    dealadvice = models.TextField(db_column='DealAdvice')  # Field name made lowercase.
    checkerid = models.CharField(db_column='CheckerID', max_length=20)  # Field name made lowercase.
    checkername = models.CharField(db_column='CheckerName', max_length=30)  # Field name made lowercase.
    auditorid = models.CharField(db_column='AuditorID', max_length=20)  # Field name made lowercase.
    auditorname = models.CharField(db_column='AuditorName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=20)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'productcheckreport'


class Productdictionary(models.Model):
    prodid = models.CharField(db_column='ProdID', unique=True, max_length=20)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=60)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    medkind = models.CharField(db_column='MedKind', max_length=30)  # Field name made lowercase.
    bpunit = models.CharField(db_column='bpUnit', max_length=20)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=20)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.PositiveIntegerField(db_column='spAmount')  # Field name made lowercase.
    mpamount = models.PositiveIntegerField(db_column='mpAmount')  # Field name made lowercase.
    basicamount = models.DecimalField(db_column='BasicAmount', max_digits=8, decimal_places=4)  # Field name made lowercase.
    basicunit = models.CharField(db_column='BasicUnit', max_length=20)  # Field name made lowercase.
    spprice = models.DecimalField(db_column='spPrice', max_digits=8, decimal_places=3)  # Field name made lowercase.
    expireddates = models.IntegerField(db_column='ExpiredDates')  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=30)  # Field name made lowercase.
    inputcode = models.CharField(db_column='InputCode', max_length=60)  # Field name made lowercase.
    midprodcheck = models.TextField(db_column='MidProdCheck')  # Field name made lowercase.
    plid = models.IntegerField(db_column='plID')  # Field name made lowercase.
    lowlimit = models.DecimalField(db_column='LowLimit', max_digits=8, decimal_places=4)  # Field name made lowercase.
    upperlimit = models.DecimalField(db_column='UpperLimit', max_digits=8, decimal_places=4)  # Field name made lowercase.
    package = models.CharField(db_column='Package', max_length=30)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=60)  # Field name made lowercase.
    qrtype = models.IntegerField(db_column='QRType')  # Field name made lowercase.
    externalno = models.CharField(db_column='ExternalNo', max_length=40)  # Field name made lowercase.
    hpunit = models.CharField(db_column='hpUnit', max_length=20)  # Field name made lowercase.
    bpamount = models.IntegerField(db_column='bpAmount')  # Field name made lowercase.
    wplid = models.IntegerField(db_column='wplID')  # Field name made lowercase.
    autoid = models.AutoField(primary_key=True)
    storage = models.CharField(db_column='Storage', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productdictionary'


class Productlabel(models.Model):
    autoid = models.AutoField(primary_key=True)
    prodid = models.CharField(db_column='ProdID', max_length=20)  # Field name made lowercase.
    modifytime = models.DateTimeField(db_column='ModifyTime')  # Field name made lowercase.
    modifierid = models.CharField(db_column='ModifierID', max_length=10)  # Field name made lowercase.
    modifiername = models.CharField(db_column='ModifierName', max_length=30)  # Field name made lowercase.
    imgid = models.IntegerField(db_column='imgID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productlabel'


class Productline(models.Model):
    autoid = models.AutoField(primary_key=True)
    linename = models.CharField(db_column='LineName', max_length=100)  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=40)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    passform = models.TextField(db_column='PassForm')  # Field name made lowercase.
    pltype = models.IntegerField(db_column='plType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productline'


class Productprescription(models.Model):
    autoid = models.AutoField(primary_key=True)
    prodid = models.CharField(db_column='ProdID', max_length=20)  # Field name made lowercase.
    stuffkind = models.CharField(db_column='StuffKind', max_length=100)  # Field name made lowercase.
    stufftype = models.IntegerField(db_column='StuffType')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=8, decimal_places=3)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=30)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=30)  # Field name made lowercase.
    spamount = models.IntegerField(db_column='spAmount')  # Field name made lowercase.
    pltype = models.IntegerField(db_column='plType')  # Field name made lowercase.
    ismainaux = models.IntegerField(db_column='IsMainAux')  # Field name made lowercase.
    flag = models.IntegerField()
    extraamount = models.DecimalField(db_column='ExtraAmount', max_digits=8, decimal_places=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productprescription'
        unique_together = (('prodid', 'stuffkind'),)


class Productputinnotes(models.Model):
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    piamount = models.DecimalField(db_column='piAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    packamount = models.IntegerField(db_column='PackAmount')  # Field name made lowercase.
    unittype = models.IntegerField(db_column='UnitType')  # Field name made lowercase.
    oddment = models.DecimalField(db_column='Oddment', max_digits=10, decimal_places=3)  # Field name made lowercase.
    pidate = models.DateField(db_column='piDate')  # Field name made lowercase.
    hxflag = models.IntegerField()
    hxbatchno = models.CharField(db_column='hxBatchNo', max_length=60)  # Field name made lowercase.
    hxamount = models.DecimalField(db_column='hxAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    piapplyerid = models.CharField(db_column='piApplyerID', max_length=10)  # Field name made lowercase.
    piapplyername = models.CharField(db_column='piApplyerName', max_length=30)  # Field name made lowercase.
    hxworkerid = models.CharField(db_column='hxWorkerID', max_length=10)  # Field name made lowercase.
    hxworkername = models.CharField(db_column='hxWorkerName', max_length=30)  # Field name made lowercase.
    hxmakedate = models.DateField(db_column='hxMakeDate')  # Field name made lowercase.
    piqaid = models.CharField(db_column='piQAID', max_length=10)  # Field name made lowercase.
    piqaname = models.CharField(db_column='piQAName', max_length=30)  # Field name made lowercase.
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.
    pistatus = models.IntegerField(db_column='piStatus')  # Field name made lowercase.
    piremark = models.CharField(db_column='piRemark', max_length=100)  # Field name made lowercase.
    pltype = models.IntegerField(db_column='plType')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=30)  # Field name made lowercase.
    dpdepositorid = models.CharField(db_column='dpDepositorID', max_length=10)  # Field name made lowercase.
    dpdepositorname = models.CharField(db_column='dpDepositorName', max_length=30)  # Field name made lowercase.
    dpwarehousemanid = models.CharField(db_column='dpWarehousemanID', max_length=10)  # Field name made lowercase.
    dpwarehousemanname = models.CharField(db_column='dpWarehousemanName', max_length=30)  # Field name made lowercase.
    dpdate = models.DateField(db_column='dpDate')  # Field name made lowercase.
    dpposition = models.CharField(db_column='dpPosition', max_length=30)  # Field name made lowercase.
    dpamount = models.IntegerField(db_column='dpAmount')  # Field name made lowercase.
    dpremark = models.CharField(db_column='dpRemark', max_length=200)  # Field name made lowercase.
    dpstatus = models.IntegerField(db_column='dpStatus')  # Field name made lowercase.
    chargerid = models.CharField(db_column='ChargerID', max_length=10)  # Field name made lowercase.
    chargername = models.CharField(db_column='ChargerName', max_length=30)  # Field name made lowercase.
    qrflag = models.IntegerField()
    autoid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'productputinnotes'


class Productputoutdata(models.Model):
    autoid = models.AutoField(primary_key=True)
    ppopid = models.IntegerField(db_column='ppopID')  # Field name made lowercase.
    prid = models.IntegerField(db_column='prID')  # Field name made lowercase.
    dictid = models.CharField(db_column='DictID', max_length=20)  # Field name made lowercase.
    dictname = models.CharField(db_column='DictName', max_length=60)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=60)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=30)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    mpamount = models.DecimalField(db_column='mpAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    bpunit = models.CharField(db_column='bpUnit', max_length=30)  # Field name made lowercase.
    spamount = models.DecimalField(db_column='spAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    basicamount = models.DecimalField(db_column='BasicAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=30)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=40)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', max_length=30)  # Field name made lowercase.
    flag = models.IntegerField()
    basicunit = models.CharField(db_column='BasicUnit', max_length=30)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=60)  # Field name made lowercase.
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    hpunit = models.CharField(db_column='hpUnit', max_length=20)  # Field name made lowercase.
    bpamount = models.IntegerField(db_column='bpAmount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productputoutdata'


class Productputoutpaper(models.Model):
    autoid = models.AutoField(primary_key=True)
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    pokind = models.CharField(db_column='poKind', max_length=30)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=20)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=30)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    auditorid = models.CharField(db_column='AuditorID', max_length=30)  # Field name made lowercase.
    auditorname = models.CharField(db_column='AuditorName', max_length=30)  # Field name made lowercase.
    clientid = models.CharField(db_column='ClientID', max_length=30)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    putouttime = models.DateTimeField(db_column='PutOutTime')  # Field name made lowercase.
    exectime = models.DateTimeField(db_column='ExecTime')  # Field name made lowercase.
    status = models.IntegerField()
    remark = models.CharField(max_length=100)
    qrflag = models.IntegerField(db_column='QRFLAG')  # Field name made lowercase.
    snid = models.IntegerField(db_column='snID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productputoutpaper'


class Productrepository(models.Model):
    autoid = models.AutoField(primary_key=True)
    prodid = models.CharField(db_column='ProdID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=60)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=60)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=30)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=30)  # Field name made lowercase.
    bpunit = models.CharField(db_column='bpUnit', max_length=20)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=20)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.PositiveIntegerField(db_column='spAmount')  # Field name made lowercase.
    mpamount = models.PositiveIntegerField(db_column='mpAmount')  # Field name made lowercase.
    basicamount = models.DecimalField(db_column='BasicAmount', max_digits=8, decimal_places=4)  # Field name made lowercase.
    basicunit = models.CharField(db_column='BasicUnit', max_length=20)  # Field name made lowercase.
    spprice = models.DecimalField(db_column='spPrice', max_digits=8, decimal_places=3)  # Field name made lowercase.
    stockamount = models.DecimalField(db_column='StockAmount', max_digits=12, decimal_places=3)  # Field name made lowercase.
    piamount = models.DecimalField(db_column='piAmount', max_digits=12, decimal_places=3)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=100)  # Field name made lowercase.
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    workshopid = models.CharField(db_column='WorkShopID', max_length=10)  # Field name made lowercase.
    workshopname = models.CharField(db_column='WorkShopName', max_length=30)  # Field name made lowercase.
    expireddays = models.IntegerField(db_column='ExpiredDays')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=60)  # Field name made lowercase.
    indate = models.DateField(db_column='InDate', blank=True, null=True)  # Field name made lowercase.
    inputcode = models.CharField(db_column='InputCode', max_length=60)  # Field name made lowercase.
    pisource = models.IntegerField(db_column='piSource')  # Field name made lowercase.
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    chkpaperno = models.CharField(db_column='chkPaperNo', max_length=30)  # Field name made lowercase.
    flag = models.IntegerField()
    hxamount = models.DecimalField(db_column='hxAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    hxstockamount = models.DecimalField(db_column='hxStockAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    hxbatchno = models.CharField(db_column='hxBatchNo', max_length=30)  # Field name made lowercase.
    hxmakedate = models.DateField(db_column='hxMakeDate')  # Field name made lowercase.
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.
    hxbpstockamount = models.DecimalField(db_column='hxbpStockAmount', max_digits=10, decimal_places=3)  # Field name made lowercase
    deptid = models.CharField(db_column='DeptID', max_length=30)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    hpunit = models.CharField(db_column='hpUnit', max_length=20)  # Field name made lowercase.
    bpamount = models.IntegerField(db_column='bpAmount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productrepository'
        unique_together = (('prodid', 'batchno', 'deptid', 'flag'),)

class Productstuff(models.Model):
    autoid = models.AutoField(primary_key=True)
    srid = models.IntegerField(db_column='srID')  # Field name made lowercase.
    sdpid = models.IntegerField(db_column='sdpID')  # Field name made lowercase.
    stuffid = models.CharField(db_column='StuffID', max_length=20)  # Field name made lowercase.
    stuffname = models.CharField(db_column='StuffName', max_length=60)  # Field name made lowercase.
    stufftype = models.IntegerField(db_column='StuffType')  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=100)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=30)  # Field name made lowercase.
    package = models.CharField(db_column='Package', max_length=30)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=40)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=8, decimal_places=3)  # Field name made lowercase.
    producer = models.CharField(db_column='Producer', max_length=60)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=30)  # Field name made lowercase.
    lrid = models.IntegerField(db_column='lrID')  # Field name made lowercase.
    content = models.DecimalField(db_column='Content', max_digits=6, decimal_places=3)  # Field name made lowercase.
    water = models.DecimalField(db_column='Water', max_digits=6, decimal_places=3)  # Field name made lowercase.
    presamount = models.DecimalField(db_column='PresAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    checkamount = models.DecimalField(db_column='CheckAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    realamount = models.DecimalField(db_column='RealAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    drawamount = models.DecimalField(db_column='DrawAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    restamount = models.DecimalField(db_column='RestAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    backamount = models.DecimalField(db_column='BackAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    backtime = models.DateTimeField(db_column='BackTime')  # Field name made lowercase.
    remark = models.CharField(max_length=100)
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    destroyamount = models.DecimalField(db_column='DestroyAmount', max_digits=14, decimal_places=3)  # Field name made lowercase.
    destroymethod = models.CharField(db_column='DestroyMethod', max_length=30)  # Field name made lowercase.
    destroydate = models.DateField(db_column='DestroyDate')  # Field name made lowercase.
    destroyerid = models.CharField(db_column='DestroyerID', max_length=10)  # Field name made lowercase.
    destroyername = models.CharField(db_column='DestroyerName', max_length=30)  # Field name made lowercase.
    supervisorid = models.CharField(db_column='SupervisorID', max_length=10)  # Field name made lowercase.
    supervisorname = models.CharField(db_column='SupervisorName', max_length=30)  # Field name made lowercase.
    ismainaux = models.IntegerField(db_column='IsMainAux')  # Field name made lowercase.
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'productstuff'


class Productwithdrawnotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    clientid = models.CharField(db_column='ClientID', max_length=30)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    qaid = models.CharField(db_column='QAID', max_length=10)  # Field name made lowercase.
    qaname = models.CharField(db_column='QAName', max_length=30)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=100)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100)  # Field name made lowercase.
    status = models.IntegerField()
    wdate = models.DateField(db_column='wDate')  # Field name made lowercase.
    qrstatus = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'productwithdrawnotes'


class Purchasingplan(models.Model):
    paperno = models.CharField(db_column='PaperNo', unique=True, max_length=20)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    supid = models.CharField(db_column='SupID', max_length=10)  # Field name made lowercase.
    supname = models.CharField(db_column='SupName', max_length=100)  # Field name made lowercase.
    invaliddate = models.DateField(db_column='InvalidDate')  # Field name made lowercase.
    remark = models.CharField(max_length=200)
    warrantorid = models.CharField(db_column='WarrantorID', max_length=10)  # Field name made lowercase.
    warrantorname = models.CharField(db_column='WarrantorName', max_length=30)  # Field name made lowercase.
    status = models.IntegerField()
    autoid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'purchasingplan'


class Pwngoods(models.Model):
    autoid = models.AutoField(primary_key=True)
    pwnid = models.IntegerField(db_column='pwnID')  # Field name made lowercase.
    sgid = models.IntegerField(db_column='sgID')  # Field name made lowercase.
    prodid = models.CharField(db_column='ProdID', max_length=10)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=30)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=60)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    bpunit = models.CharField(db_column='bpUnit', max_length=20)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=20)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.PositiveIntegerField(db_column='spAmount')  # Field name made lowercase.
    mpamount = models.PositiveIntegerField(db_column='mpAmount')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=12, decimal_places=3)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=12, decimal_places=2)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=30)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=60)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=60)  # Field name made lowercase.
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    indate = models.DateField(db_column='InDate')  # Field name made lowercase.
    chkpaperno = models.CharField(db_column='chkPaperNo', max_length=30)  # Field name made lowercase.
    expireddate = models.DateField(db_column='ExpiredDate')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=30)  # Field name made lowercase.
    saledate = models.DateField(db_column='SaleDate')  # Field name made lowercase.
    salerid = models.CharField(db_column='SalerID', max_length=10)  # Field name made lowercase.
    salername = models.CharField(db_column='SalerName', max_length=30)  # Field name made lowercase.
    status = models.IntegerField()
    piapplyerid = models.CharField(db_column='piApplyerID', max_length=10)  # Field name made lowercase.
    piapplyername = models.CharField(db_column='piApplyerName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    piamount = models.DecimalField(db_column='piAmount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    pidate = models.DateField(db_column='piDate')  # Field name made lowercase.
    warehouseid = models.CharField(db_column='WarehouseID', max_length=10)  # Field name made lowercase.
    warehousename = models.CharField(db_column='WarehouseName', max_length=30)  # Field name made lowercase.
    qaid = models.CharField(db_column='QAID', max_length=10)  # Field name made lowercase.
    qaname = models.CharField(db_column='QAName', max_length=30)  # Field name made lowercase.
    piremark = models.CharField(db_column='piRemark', max_length=100)  # Field name made lowercase.
    pistatus = models.IntegerField(db_column='piStatus')  # Field name made lowercase.
    pideptid = models.CharField(max_length=30)
    pideptname = models.CharField(max_length=30)
    hpunit = models.CharField(db_column='hpUnit', max_length=20)  # Field name made lowercase.
    bpamount = models.IntegerField(db_column='bpAmount')  # Field name made lowercase.
    bflag = models.IntegerField()
    drawerid = models.CharField(db_column='DrawerID', max_length=30)  # Field name made lowercase.
    drawername = models.CharField(db_column='DrawerName', max_length=30)  # Field name made lowercase.
    drawtime = models.DateTimeField(db_column='DrawTime')  # Field name made lowercase.
    ppid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pwngoods'


class Pwqrcode(models.Model):
    autoid = models.AutoField(primary_key=True)
    pwdid = models.IntegerField(db_column='pwdID')  # Field name made lowercase.
    qr0 = models.CharField(db_column='QR0', unique=True, max_length=200)  # Field name made lowercase.
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pwqrcode'


class Qrcoderepository(models.Model):
    autoid = models.AutoField(primary_key=True)
    qrcode = models.CharField(db_column='QRCode', unique=True, max_length=200)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=200)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=200)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=200)  # Field name made lowercase.
    telno = models.CharField(db_column='TelNo', max_length=60)  # Field name made lowercase.
    used = models.IntegerField(db_column='Used')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    usedtime = models.DateTimeField(db_column='UsedTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'qrcoderepository'


class Rectificationnotice(models.Model):
    autoid = models.AutoField(primary_key=True)
    deptid = models.CharField(db_column='DeptID', max_length=30)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    scrid = models.IntegerField(db_column='scrID')  # Field name made lowercase.
    accordance = models.CharField(db_column='Accordance', max_length=200)  # Field name made lowercase.
    descrip = models.TextField(db_column='Descrip')  # Field name made lowercase.
    qaid = models.CharField(db_column='qaID', max_length=30)  # Field name made lowercase.
    qaname = models.CharField(db_column='qaName', max_length=30)  # Field name made lowercase.
    qachargerid = models.CharField(db_column='qaChargerID', max_length=30)  # Field name made lowercase.
    qachargername = models.CharField(db_column='qaChargerName', max_length=30)  # Field name made lowercase.
    qadate = models.DateField(db_column='qaDate')  # Field name made lowercase.
    measure = models.TextField(db_column='Measure')  # Field name made lowercase.
    dchargerid = models.CharField(db_column='dChargerID', max_length=30)  # Field name made lowercase.
    dchargername = models.CharField(db_column='dChargerName', max_length=30)  # Field name made lowercase.
    groupid = models.CharField(db_column='GroupID', max_length=30)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=30)  # Field name made lowercase.
    done = models.TextField(db_column='Done')  # Field name made lowercase.
    dnchargerid = models.CharField(db_column='dnChargerID', max_length=30)  # Field name made lowercase.
    dnchargername = models.CharField(db_column='dnChargerName', max_length=30)  # Field name made lowercase.
    checkdone = models.TextField(db_column='CheckDone')  # Field name made lowercase.
    cdid = models.CharField(db_column='cdID', max_length=30)  # Field name made lowercase.
    cdname = models.CharField(db_column='cdName', max_length=30)  # Field name made lowercase.
    leaderid = models.CharField(db_column='LeaderID', max_length=30)  # Field name made lowercase.
    leadername = models.CharField(db_column='LeaderName', max_length=30)  # Field name made lowercase.
    gpid = models.CharField(db_column='gpID', max_length=30)  # Field name made lowercase.
    gpname = models.CharField(db_column='gpName', max_length=30)  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rectificationnotice'


class Rejectdisposal(models.Model):
    autoid = models.AutoField(primary_key=True)
    ciid = models.IntegerField(db_column='ciID')  # Field name made lowercase.
    rejecttype = models.IntegerField(db_column='RejectType')  # Field name made lowercase.
    stuffid = models.CharField(db_column='StuffID', max_length=10)  # Field name made lowercase.
    stuffname = models.CharField(db_column='StuffName', max_length=10)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    batchno = models.CharField(db_column='BatchNo', max_length=40)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=12, decimal_places=2)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=30)  # Field name made lowercase.
    rdtype = models.IntegerField(db_column='rdType')  # Field name made lowercase.
    producer = models.CharField(db_column='Producer', max_length=60)  # Field name made lowercase.
    buyerid = models.CharField(db_column='BuyerID', max_length=10)  # Field name made lowercase.
    buyername = models.CharField(db_column='BuyerName', max_length=30)  # Field name made lowercase.
    rejectcause = models.CharField(db_column='RejectCause', max_length=250)  # Field name made lowercase.
    applydate = models.DateField(db_column='ApplyDate')  # Field name made lowercase.
    applyerid = models.CharField(db_column='ApplyerID', max_length=10)  # Field name made lowercase.
    applyername = models.CharField(db_column='ApplyerName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    qccomment = models.CharField(db_column='QCComment', max_length=250)  # Field name made lowercase.
    qcid = models.CharField(db_column='QCID', max_length=10)  # Field name made lowercase.
    qcname = models.CharField(db_column='QCName', max_length=30)  # Field name made lowercase.
    qcdate = models.DateField(db_column='QCDate')  # Field name made lowercase.
    gmapprove = models.CharField(db_column='GMApprove', max_length=250)  # Field name made lowercase.
    gmid = models.CharField(db_column='GMID', max_length=10)  # Field name made lowercase.
    gmname = models.CharField(db_column='GMName', max_length=30)  # Field name made lowercase.
    approvedate = models.DateField(db_column='ApproveDate')  # Field name made lowercase.
    checkpaperno = models.CharField(db_column='CheckPaperNo', max_length=20)  # Field name made lowercase.
    status = models.IntegerField()
    flag = models.IntegerField()
    qmcomment = models.CharField(db_column='QMComment', max_length=250)  # Field name made lowercase.
    qmid = models.CharField(db_column='QMID', max_length=10)  # Field name made lowercase.
    qmname = models.CharField(db_column='QMName', max_length=30)  # Field name made lowercase.
    qmdate = models.DateField(db_column='QMDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rejectdisposal'
        unique_together = (('ciid', 'rejecttype'),)


class Relativepictures(models.Model):
    autoid = models.AutoField(primary_key=True)
    kind = models.IntegerField()
    scid = models.CharField(db_column='scID', max_length=20)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=100)  # Field name made lowercase.
    imageid = models.IntegerField(db_column='ImageID')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relativepictures'


class Returnmoneynotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    clientid = models.CharField(db_column='ClientID', max_length=30)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    salerid = models.CharField(db_column='SalerID', max_length=10)  # Field name made lowercase.
    salername = models.CharField(db_column='SalerName', max_length=30)  # Field name made lowercase.
    paydate = models.DateField(db_column='PayDate')  # Field name made lowercase.
    money = models.DecimalField(db_column='Money', max_digits=12, decimal_places=2)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    auditorid = models.CharField(db_column='AuditorID', max_length=10)  # Field name made lowercase.
    auditorname = models.CharField(db_column='AuditorName', max_length=30)  # Field name made lowercase.
    paymethod = models.CharField(db_column='PayMethod', max_length=30)  # Field name made lowercase.
    remark = models.CharField(max_length=200)
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'returnmoneynotes'


class Saleorders(models.Model):
    autoid = models.AutoField(primary_key=True)
    clientid = models.CharField(db_column='ClientID', max_length=30)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    salerid = models.CharField(db_column='SalerID', max_length=10)  # Field name made lowercase.
    salername = models.CharField(db_column='SalerName', max_length=30)  # Field name made lowercase.
    qaid = models.CharField(db_column='QAID', max_length=10)  # Field name made lowercase.
    qaname = models.CharField(db_column='QAName', max_length=30)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100)  # Field name made lowercase.
    orderdate = models.DateField(db_column='OrderDate')  # Field name made lowercase.
    deliverydate = models.DateField(db_column='DeliveryDate')  # Field name made lowercase.
    deliveryplace = models.CharField(db_column='DeliveryPlace', max_length=60)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saleorders'


class Salesgoods(models.Model):
    autoid = models.AutoField(primary_key=True)
    prodid = models.CharField(db_column='ProdID', max_length=10)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=30)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=60)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    bpunit = models.CharField(db_column='bpUnit', max_length=20)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=20)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.PositiveIntegerField(db_column='spAmount')  # Field name made lowercase.
    mpamount = models.PositiveIntegerField(db_column='mpAmount')  # Field name made lowercase.
    saleamount = models.DecimalField(db_column='SaleAmount', max_digits=12, decimal_places=3)  # Field name made lowercase.
    wdamount = models.DecimalField(db_column='wdAmount', max_digits=13, decimal_places=3)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=12, decimal_places=2)  # Field name made lowercase.
    snid = models.IntegerField(db_column='snID')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=30)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=60)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=60)  # Field name made lowercase.
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    indate = models.DateField(db_column='InDate')  # Field name made lowercase.
    chkpaperno = models.CharField(db_column='chkPaperNo', max_length=30)  # Field name made lowercase.
    expireddate = models.DateField(db_column='ExpiredDate')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=30)  # Field name made lowercase.
    flag = models.IntegerField()
    saledate = models.DateField(db_column='SaleDate')  # Field name made lowercase.
    hpunit = models.CharField(db_column='hpUnit', max_length=20)  # Field name made lowercase.
    bpamount = models.IntegerField(db_column='bpAmount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesgoods'


class Salesnotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    clientid = models.CharField(db_column='ClientID', max_length=30)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    saledate = models.DateField(db_column='SaleDate')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    salerid = models.CharField(db_column='SalerID', max_length=10)  # Field name made lowercase.
    salername = models.CharField(db_column='SalerName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    auditorid = models.CharField(db_column='AuditorID', max_length=10)  # Field name made lowercase.
    auditorname = models.CharField(db_column='AuditorName', max_length=30)  # Field name made lowercase.
    consignmentid = models.CharField(db_column='ConsignmentID', max_length=10)  # Field name made lowercase.
    consignmentname = models.CharField(db_column='ConsignmentName', max_length=30)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=100)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    deliverydate = models.DateField(db_column='DeliveryDate')  # Field name made lowercase.
    deliveryplace = models.CharField(db_column='DeliveryPlace', max_length=60)  # Field name made lowercase.
    conveyance = models.CharField(db_column='Conveyance', max_length=20)  # Field name made lowercase.
    paymethod = models.CharField(db_column='PayMethod', max_length=20)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    consignmentdate = models.DateField(db_column='ConsignmentDate')  # Field name made lowercase.
    deliverid = models.CharField(db_column='DeliverID', max_length=10)  # Field name made lowercase.
    delivername = models.CharField(db_column='DeliverName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesnotes'


class Salesnotesgoods(models.Model):
    autoid = models.AutoField(primary_key=True)
    prodid = models.CharField(db_column='ProdID', max_length=10)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=30)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=60)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    bpunit = models.CharField(db_column='bpUnit', max_length=20)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=20)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.PositiveIntegerField(db_column='spAmount')  # Field name made lowercase.
    mpamount = models.PositiveIntegerField(db_column='mpAmount')  # Field name made lowercase.
    saleamount = models.DecimalField(db_column='SaleAmount', max_digits=12, decimal_places=3)  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=12, decimal_places=2)  # Field name made lowercase.
    snid = models.IntegerField(db_column='snID')  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=30)  # Field name made lowercase.
    hpunit = models.CharField(db_column='hpUnit', max_length=20)  # Field name made lowercase.
    bpamount = models.IntegerField(db_column='bpAmount')  # Field name made lowercase.
    inmethod = models.IntegerField(db_column='InMethod')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'salesnotesgoods'


class Samplerecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    samplename = models.CharField(db_column='SampleName', max_length=40)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=30)  # Field name made lowercase.
    sampledate = models.DateField(db_column='SampleDate')  # Field name made lowercase.
    prodid = models.CharField(db_column='ProdID', max_length=20)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=40)  # Field name made lowercase.
    spec = models.CharField(max_length=200)
    samplequantity = models.DecimalField(db_column='SampleQuantity', max_digits=10, decimal_places=4)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    kind = models.IntegerField()
    creatorid = models.CharField(db_column='CreatorID', max_length=20)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    status = models.IntegerField()
    commonname = models.CharField(db_column='CommonName', max_length=40)  # Field name made lowercase.
    expdays = models.IntegerField(db_column='ExpDays')  # Field name made lowercase.
    expiredtime = models.DateTimeField(db_column='ExpiredTime')  # Field name made lowercase.
    etid = models.CharField(db_column='etID', max_length=30)  # Field name made lowercase.
    etname = models.CharField(db_column='etName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'samplerecords'


class Sectionsettings(models.Model):
    sectionid = models.CharField(db_column='SectionID', primary_key=True, max_length=10)  # Field name made lowercase.
    varname = models.CharField(db_column='VarName', max_length=30)  # Field name made lowercase.
    varvalue = models.CharField(db_column='VarValue', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sectionsettings'
        unique_together = (('sectionid', 'varname'),)


class Selfcheckitems(models.Model):
    autoid = models.AutoField(primary_key=True)
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    kind = models.CharField(max_length=30)
    itemname = models.CharField(db_column='ItemName', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'selfcheckitems'
        unique_together = (('kind', 'itemname'),)


class Selfcheckrecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    creatorid = models.CharField(db_column='CreatorID', max_length=30)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=30)  # Field name made lowercase.
    cdate = models.DateField(db_column='cDate')  # Field name made lowercase.
    summary = models.TextField(db_column='Summary')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'selfcheckrecords'


class Selfdefinedformat(models.Model):
    autoid = models.AutoField(db_column='AUTOID', primary_key=True)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=7)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=20)  # Field name made lowercase.
    formatname = models.CharField(db_column='FormatName', max_length=50)  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=30)  # Field name made lowercase.
    subkind = models.CharField(db_column='SubKind', max_length=20)  # Field name made lowercase.
    format = models.TextField(db_column='Format')  # Field name made lowercase.
    orientation = models.IntegerField(db_column='Orientation')  # Field name made lowercase.
    flag = models.IntegerField()
    formtype = models.PositiveIntegerField(db_column='FormType')  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'selfdefinedformat'


class Stuffcheckin(models.Model):
    paperno = models.CharField(db_column='PaperNo', max_length=20)  # Field name made lowercase.
    pppaperno = models.CharField(db_column='ppPaperNo', max_length=20)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    supid = models.CharField(db_column='SupID', max_length=10)  # Field name made lowercase.
    supname = models.CharField(db_column='SupName', max_length=100)  # Field name made lowercase.
    remark = models.CharField(max_length=200)
    buyerid = models.CharField(db_column='BuyerID', max_length=10)  # Field name made lowercase.
    buyername = models.CharField(db_column='BuyerName', max_length=30)  # Field name made lowercase.
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.
    auditorid = models.CharField(db_column='AuditorID', max_length=10)  # Field name made lowercase.
    auditorname = models.CharField(db_column='AuditorName', max_length=30)  # Field name made lowercase.
    buydate = models.DateField(db_column='BuyDate')  # Field name made lowercase.
    pikind = models.CharField(db_column='piKind', max_length=20)  # Field name made lowercase.
    papertype = models.IntegerField(db_column='PaperType')  # Field name made lowercase.
    status = models.IntegerField()
    eflag = models.IntegerField()
    autoid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'stuffcheckin'


class StuffcheckinCopy(models.Model):
    paperno = models.CharField(db_column='PaperNo', primary_key=True, max_length=20)  # Field name made lowercase.
    pppaperno = models.CharField(db_column='ppPaperNo', max_length=20)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    supid = models.CharField(db_column='SupID', max_length=10)  # Field name made lowercase.
    supname = models.CharField(db_column='SupName', max_length=100)  # Field name made lowercase.
    remark = models.CharField(max_length=200)
    buyerid = models.CharField(db_column='BuyerID', max_length=10)  # Field name made lowercase.
    buyername = models.CharField(db_column='BuyerName', max_length=30)  # Field name made lowercase.
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.
    auditorid = models.CharField(db_column='AuditorID', max_length=10)  # Field name made lowercase.
    auditorname = models.CharField(db_column='AuditorName', max_length=30)  # Field name made lowercase.
    buydate = models.DateField(db_column='BuyDate')  # Field name made lowercase.
    pikind = models.CharField(db_column='piKind', max_length=20)  # Field name made lowercase.
    papertype = models.IntegerField(db_column='PaperType')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stuffcheckin_copy'
        unique_together = (('paperno', 'papertype'),)


class Stuffcheckinlist(models.Model):
    autoid = models.AutoField(primary_key=True)
    paperno = models.CharField(db_column='PaperNo', max_length=20)  # Field name made lowercase.
    papertype = models.IntegerField(db_column='PaperType')  # Field name made lowercase.
    stuffid = models.CharField(db_column='StuffID', max_length=10)  # Field name made lowercase.
    stuffname = models.CharField(db_column='StuffName', max_length=30)  # Field name made lowercase.
    stufftype = models.IntegerField(db_column='StuffType')  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=60)  # Field name made lowercase.
    package = models.CharField(db_column='Package', max_length=30)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    producer = models.CharField(db_column='Producer', max_length=100)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=100)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=100)  # Field name made lowercase.
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    expireddate = models.DateField(db_column='ExpiredDate')  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    piamount = models.DecimalField(db_column='piAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    basicunit = models.CharField(db_column='BasicUnit', max_length=10)  # Field name made lowercase.
    basicamount = models.DecimalField(db_column='BasicAmount', max_digits=10, decimal_places=4)  # Field name made lowercase.
    pitime = models.DateTimeField(db_column='piTime')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=8, decimal_places=2)  # Field name made lowercase.
    position = models.CharField(max_length=60)
    water = models.DecimalField(max_digits=8, decimal_places=2)
    content = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.IntegerField()
    checkintime = models.DateTimeField(db_column='CheckInTime')  # Field name made lowercase.
    srid = models.IntegerField(db_column='srID')  # Field name made lowercase.
    pplid = models.IntegerField(db_column='pplID')  # Field name made lowercase.
    lrid = models.IntegerField(db_column='lrID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stuffcheckinlist'


class Stuffdictionary(models.Model):
    stuffid = models.CharField(db_column='StuffID', unique=True, max_length=20)  # Field name made lowercase.
    stuffname = models.CharField(db_column='StuffName', max_length=60)  # Field name made lowercase.
    stufftype = models.IntegerField(db_column='StuffType')  # Field name made lowercase.
    kind = models.CharField(db_column='Kind', max_length=100)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=30)  # Field name made lowercase.
    package = models.CharField(db_column='Package', max_length=30)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=40)  # Field name made lowercase.
    bpunit = models.CharField(db_column='bpUnit', max_length=20)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=20)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.PositiveIntegerField(db_column='spAmount')  # Field name made lowercase.
    mpamount = models.PositiveIntegerField(db_column='mpAmount')  # Field name made lowercase.
    basicamount = models.DecimalField(db_column='BasicAmount', max_digits=12, decimal_places=4)  # Field name made lowercase.
    spprice = models.DecimalField(db_column='spPrice', max_digits=12, decimal_places=4)  # Field name made lowercase.
    basicunit = models.CharField(db_column='BasicUnit', max_length=20)  # Field name made lowercase.
    producer = models.CharField(db_column='Producer', max_length=60)  # Field name made lowercase.
    inputcode = models.CharField(db_column='InputCode', max_length=60)  # Field name made lowercase.
    checkitems = models.TextField(db_column='CheckItems')  # Field name made lowercase.
    lowlimit = models.DecimalField(db_column='LowLimit', max_digits=10, decimal_places=4)  # Field name made lowercase.
    upperlimit = models.DecimalField(db_column='UpperLimit', max_digits=10, decimal_places=4)  # Field name made lowercase.
    plid = models.IntegerField(db_column='plID')  # Field name made lowercase.
    countercheckdays = models.IntegerField(db_column='CountercheckDays')  # Field name made lowercase.
    kindinputcode = models.CharField(db_column='KindInputCode', max_length=100)  # Field name made lowercase.
    expireddays = models.IntegerField(db_column='ExpiredDays')  # Field name made lowercase.
    externalno = models.CharField(db_column='ExternalNo', max_length=40)  # Field name made lowercase.
    cunit = models.CharField(db_column='cUnit', max_length=20)  # Field name made lowercase.
    ceffect = models.DecimalField(db_column='cEffect', max_digits=14, decimal_places=4)  # Field name made lowercase.
    cstandard = models.DecimalField(db_column='cStandard', max_digits=14, decimal_places=3)  # Field name made lowercase.
    autoid = models.AutoField(primary_key=True)
    storage = models.CharField(db_column='Storage', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stuffdictionary'


class Stuffdrawpaper(models.Model):
    autoid = models.AutoField(primary_key=True)
    papertype = models.IntegerField(db_column='PaperType')  # Field name made lowercase.
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    applytime = models.DateTimeField(db_column='ApplyTime')  # Field name made lowercase.
    drawtime = models.DateTimeField(db_column='DrawTime')  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    chargerid = models.CharField(db_column='ChargerID', max_length=10)  # Field name made lowercase.
    chargername = models.CharField(db_column='ChargerName', max_length=30)  # Field name made lowercase.
    providerid = models.CharField(db_column='ProviderID', max_length=10)  # Field name made lowercase.
    providername = models.CharField(db_column='ProviderName', max_length=30)  # Field name made lowercase.
    drawerid = models.CharField(db_column='DrawerID', max_length=10)  # Field name made lowercase.
    drawername = models.CharField(db_column='DrawerName', max_length=30)  # Field name made lowercase.
    workshopid = models.CharField(db_column='WorkShopID', max_length=10)  # Field name made lowercase.
    workshopname = models.CharField(db_column='WorkShopName', max_length=30)  # Field name made lowercase.
    remark = models.CharField(max_length=200)
    status = models.IntegerField()
    wdqaid = models.CharField(db_column='wdQAID', max_length=10)  # Field name made lowercase.
    wdqaname = models.CharField(db_column='wdQAName', max_length=30)  # Field name made lowercase.
    wdwarehousemanid = models.CharField(db_column='wdWarehousemanID', max_length=10)  # Field name made lowercase.
    wdwarehousemanname = models.CharField(db_column='wdWarehousemanName', max_length=30)  # Field name made lowercase.
    wdchargerid = models.CharField(db_column='wdChargerID', max_length=10)  # Field name made lowercase.
    wdchargername = models.CharField(db_column='wdChargerName', max_length=30)  # Field name made lowercase.
    wddate = models.DateField(db_column='wdDate')  # Field name made lowercase.
    wdremark = models.CharField(db_column='wdRemark', max_length=100)  # Field name made lowercase.
    wdstatus = models.IntegerField()
    wddrawerid = models.CharField(db_column='wdDrawerID', max_length=10)  # Field name made lowercase.
    wddrawername = models.CharField(db_column='wdDrawerName', max_length=30)  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stuffdrawpaper'


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
    def __unicode__(self):
        return '%s' % (self.catname)

    def toJSON(self):
        import json,datetime,decimal
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr), datetime.datetime):
                d[attr] = str(getattr(self, attr))
            elif isinstance(getattr(self,attr),decimal.Decimal):
                d[attr] = float(getattr(self,attr))
            else:
                d[attr] = str(getattr(self, attr))


        return json.dumps(d)


class Stuffsupplyers(models.Model):
    autoid = models.AutoField(primary_key=True)
    sdid = models.IntegerField(db_column='sdID')  # Field name made lowercase.
    spid = models.IntegerField(db_column='spID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stuffsupplyers'
        unique_together = (('sdid', 'spid'),)


class Superhistory(models.Model):
    autoid = models.AutoField(primary_key=True)
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    moditime = models.DateTimeField(db_column='ModiTime', blank=True, null=True)  # Field name made lowercase.
    tabname = models.CharField(max_length=40, blank=True, null=True)
    action = models.CharField(max_length=8, blank=True, null=True)
    editorid = models.CharField(db_column='EditorID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    editorname = models.CharField(db_column='EditorName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    origtext = models.TextField(db_column='OrigText', blank=True, null=True)  # Field name made lowercase.
    moditext = models.TextField(db_column='ModiText', blank=True, null=True)  # Field name made lowercase.
    caseid = models.CharField(db_column='CaseID', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'superhistory'


class Supplyer(models.Model):
    supid = models.CharField(db_column='SupID', unique=True, max_length=20)  # Field name made lowercase.
    supname = models.CharField(db_column='SupName', max_length=60)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    postzip = models.CharField(db_column='PostZip', max_length=10)  # Field name made lowercase.
    telno = models.CharField(db_column='TelNo', max_length=100)  # Field name made lowercase.
    faxno = models.CharField(db_column='FaxNo', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=60)  # Field name made lowercase.
    homepage = models.CharField(db_column='HomePage', max_length=100)  # Field name made lowercase.
    charger = models.CharField(db_column='Charger', max_length=30)  # Field name made lowercase.
    bankname = models.CharField(db_column='BankName', max_length=30)  # Field name made lowercase.
    bankaccount = models.CharField(db_column='BankAccount', max_length=100)  # Field name made lowercase.
    chargertitle = models.CharField(db_column='ChargerTitle', max_length=20)  # Field name made lowercase.
    inputcode = models.CharField(db_column='InputCode', max_length=60)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200)  # Field name made lowercase.
    taxno = models.CharField(db_column='TaxNo', max_length=100)  # Field name made lowercase.
    evaluation = models.TextField(db_column='Evaluation')  # Field name made lowercase.
    tstkind = models.IntegerField(db_column='tstKind')  # Field name made lowercase.
    validdate = models.DateField(db_column='ValidDate')  # Field name made lowercase.
    validtime = models.DateField(db_column='ValidTime')  # Field name made lowercase.
    externalcode = models.CharField(db_column='ExternalCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    autoid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'supplyer'


class Supplyerevaluation(models.Model):
    autoid = models.AutoField(primary_key=True)
    supid = models.CharField(db_column='SupID', max_length=20)  # Field name made lowercase.
    property = models.CharField(max_length=30)
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=20)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    producingscale = models.CharField(db_column='ProducingScale', max_length=200)  # Field name made lowercase.
    management = models.CharField(db_column='Management', max_length=220)  # Field name made lowercase.
    transportation = models.CharField(db_column='Transportation', max_length=100)  # Field name made lowercase.
    usedinvestigation = models.CharField(db_column='UsedInvestigation', max_length=200)  # Field name made lowercase.
    attachments = models.CharField(db_column='Attachments', max_length=100)  # Field name made lowercase.
    remark = models.CharField(db_column='Remark', max_length=200)  # Field name made lowercase.
    conclusion = models.TextField(db_column='Conclusion')  # Field name made lowercase.
    investigatorid = models.CharField(db_column='InvestigatorID', max_length=10)  # Field name made lowercase.
    investigatorname = models.CharField(db_column='InvestigatorName', max_length=30)  # Field name made lowercase.
    invdate = models.DateField(db_column='InvDate')  # Field name made lowercase.
    qccomment = models.CharField(db_column='QCComment', max_length=220)  # Field name made lowercase.
    qcid = models.CharField(db_column='QCID', max_length=10)  # Field name made lowercase.
    qcname = models.CharField(db_column='QCName', max_length=30)  # Field name made lowercase.
    qcdate = models.DateField(db_column='QCDate')  # Field name made lowercase.
    warrantcomment = models.CharField(db_column='WarrantComment', max_length=200)  # Field name made lowercase.
    managerid = models.CharField(db_column='ManagerID', max_length=10)  # Field name made lowercase.
    managername = models.CharField(db_column='ManagerName', max_length=30)  # Field name made lowercase.
    mandate = models.DateField(db_column='ManDate')  # Field name made lowercase.
    flag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'supplyerevaluation'


class Sysoperator(models.Model):
    autoid = models.AutoField(primary_key=True)
    operatorid = models.CharField(db_column='OperatorID', max_length=10)  # Field name made lowercase.
    operatorname = models.CharField(db_column='OperatorName', max_length=30)  # Field name made lowercase.
    rectime = models.DateTimeField()
    operation = models.CharField(db_column='Operation', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sysoperator'


class Syssetting(models.Model):
    varname = models.CharField(db_column='VarName', primary_key=True, max_length=30)  # Field name made lowercase.
    varvalue = models.TextField(db_column='VarValue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'syssetting'


class Systemoptions(models.Model):
    otid = models.IntegerField(db_column='otID', primary_key=True)  # Field name made lowercase.
    otvalue = models.CharField(db_column='otValue', max_length=256)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'systemoptions'


class Temphumidityrecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    clerkid = models.CharField(db_column='ClerkID', max_length=30)  # Field name made lowercase.
    clerkname = models.CharField(db_column='ClerkName', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.
    place = models.CharField(db_column='Place', max_length=30)  # Field name made lowercase.
    temp = models.DecimalField(db_column='Temp', max_digits=6, decimal_places=2)  # Field name made lowercase.
    humidity = models.DecimalField(db_column='Humidity', max_digits=6, decimal_places=2)  # Field name made lowercase.
    recordtime = models.DateTimeField(db_column='RecordTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temphumidityrecords'


class Tmpprod(models.Model):
    autoid = models.IntegerField()
    prodid = models.CharField(db_column='ProdID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    prodname = models.CharField(db_column='ProdName', max_length=60)  # Field name made lowercase.
    commonname = models.CharField(db_column='CommonName', max_length=60)  # Field name made lowercase.
    spec = models.CharField(db_column='Spec', max_length=30)  # Field name made lowercase.
    allowno = models.CharField(db_column='AllowNo', max_length=30)  # Field name made lowercase.
    bpunit = models.CharField(db_column='bpUnit', max_length=20)  # Field name made lowercase.
    mpunit = models.CharField(db_column='mpUnit', max_length=20)  # Field name made lowercase.
    spunit = models.CharField(db_column='spUnit', max_length=20)  # Field name made lowercase.
    spamount = models.PositiveIntegerField(db_column='spAmount')  # Field name made lowercase.
    mpamount = models.PositiveIntegerField(db_column='mpAmount')  # Field name made lowercase.
    basicamount = models.DecimalField(db_column='BasicAmount', max_digits=8, decimal_places=4)  # Field name made lowercase.
    basicunit = models.CharField(db_column='BasicUnit', max_length=20)  # Field name made lowercase.
    spprice = models.DecimalField(db_column='spPrice', max_digits=8, decimal_places=3)  # Field name made lowercase.
    stockamount = models.DecimalField(db_column='StockAmount', max_digits=12, decimal_places=3)  # Field name made lowercase.
    piamount = models.DecimalField(db_column='piAmount', max_digits=12, decimal_places=3)  # Field name made lowercase.
    batchno = models.CharField(db_column='BatchNo', max_length=100)  # Field name made lowercase.
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    workshopid = models.CharField(db_column='WorkShopID', max_length=10)  # Field name made lowercase.
    workshopname = models.CharField(db_column='WorkShopName', max_length=30)  # Field name made lowercase.
    expireddays = models.IntegerField(db_column='ExpiredDays')  # Field name made lowercase.
    position = models.CharField(db_column='Position', max_length=60)  # Field name made lowercase.
    indate = models.DateField(db_column='InDate', blank=True, null=True)  # Field name made lowercase.
    inputcode = models.CharField(db_column='InputCode', max_length=60)  # Field name made lowercase.
    pisource = models.IntegerField(db_column='piSource')  # Field name made lowercase.
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    chkpaperno = models.CharField(db_column='chkPaperNo', max_length=30)  # Field name made lowercase.
    flag = models.IntegerField()
    hxamount = models.DecimalField(db_column='hxAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    hxstockamount = models.DecimalField(db_column='hxStockAmount', max_digits=10, decimal_places=3)  # Field name made lowercase.
    hxbatchno = models.CharField(db_column='hxBatchNo', max_length=30)  # Field name made lowercase.
    hxmakedate = models.DateField(db_column='hxMakeDate')  # Field name made lowercase.
    warehousemanid = models.CharField(db_column='WarehousemanID', max_length=10)  # Field name made lowercase.
    warehousemanname = models.CharField(db_column='WarehousemanName', max_length=30)  # Field name made lowercase.
    hxbpstockamount = models.DecimalField(db_column='hxbpStockAmount', max_digits=10, decimal_places=3)  # Field name made lowercase
    deptid = models.CharField(db_column='DeptID', max_length=30)  # Field name made lowercase.
    deptname = models.CharField(db_column='DeptName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tmpprod'


class Treestructure(models.Model):
    autoid = models.AutoField(primary_key=True)
    kind = models.IntegerField()
    kindname = models.CharField(db_column='KindName', max_length=20)  # Field name made lowercase.
    parentid = models.IntegerField(db_column='ParentID')  # Field name made lowercase.
    depth = models.IntegerField(db_column='Depth')  # Field name made lowercase.
    inputcode = models.CharField(db_column='InputCode', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'treestructure'
        unique_together = (('kind', 'kindname', 'parentid'),)


class Validateplan(models.Model):
    autoid = models.AutoField(primary_key=True)
    creatorid = models.CharField(db_column='CreatorID', max_length=20)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    y_period = models.IntegerField(db_column='Y_Period', unique=True)  # Field name made lowercase.
    doccode = models.CharField(db_column='DocCode', max_length=40)  # Field name made lowercase.
    makedate = models.DateField(db_column='MakeDate')  # Field name made lowercase.
    ofilename = models.CharField(db_column='oFileName', max_length=255)  # Field name made lowercase.
    docfilename = models.CharField(db_column='DocFileName', max_length=200)  # Field name made lowercase.
    doctitle = models.CharField(db_column='DocTitle', max_length=100)  # Field name made lowercase.
    doc = models.TextField(db_column='Doc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'validateplan'


class Validaterecords(models.Model):
    autoid = models.AutoField(primary_key=True)
    creatorid = models.CharField(db_column='CreatorID', max_length=20)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime')  # Field name made lowercase.
    valdate = models.DateField(db_column='ValDate')  # Field name made lowercase.
    valtype = models.IntegerField(db_column='ValType')  # Field name made lowercase.
    doccode = models.CharField(db_column='DocCode', max_length=40)  # Field name made lowercase.
    eqno = models.CharField(db_column='EqNo', max_length=40)  # Field name made lowercase.
    eqtype = models.CharField(db_column='EqType', max_length=40)  # Field name made lowercase.
    ofilename = models.CharField(db_column='oFileName', max_length=255)  # Field name made lowercase.
    docfilename = models.CharField(db_column='DocFileName', max_length=220)  # Field name made lowercase.
    doctitle = models.CharField(db_column='DocTitle', max_length=100)  # Field name made lowercase.
    doc = models.TextField(db_column='Doc')  # Field name made lowercase.
    kind = models.IntegerField(db_column='Kind')  # Field name made lowercase.
    auditorid = models.CharField(db_column='AuditorID', max_length=10)  # Field name made lowercase.
    auditorname = models.CharField(db_column='AuditorName', max_length=30)  # Field name made lowercase.
    auditdate = models.DateField(db_column='AuditDate')  # Field name made lowercase.
    approverid = models.CharField(db_column='ApproverID', max_length=10)  # Field name made lowercase.
    approvername = models.CharField(db_column='ApproverName', max_length=30)  # Field name made lowercase.
    approvedate = models.DateField(db_column='ApproveDate')  # Field name made lowercase.
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'validaterecords'


class Weighingrecord(models.Model):
    autoid = models.AutoField(primary_key=True)
    ppid = models.IntegerField(db_column='ppID')  # Field name made lowercase.
    temperature = models.DecimalField(db_column='Temperature', max_digits=6, decimal_places=2)  # Field name made lowercase.
    humidity = models.DecimalField(max_digits=6, decimal_places=2)
    operatorid = models.CharField(db_column='OperatorID', max_length=10)  # Field name made lowercase.
    operatorname = models.CharField(db_column='OperatorName', max_length=30)  # Field name made lowercase.
    checkerid = models.CharField(db_column='CheckerID', max_length=10)  # Field name made lowercase.
    checkername = models.CharField(db_column='CheckerName', max_length=30)  # Field name made lowercase.
    checkdate = models.DateField(db_column='CheckDate')  # Field name made lowercase.
    remark = models.CharField(max_length=100)
    operstep = models.TextField(db_column='OperStep')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'weighingrecord'


class Withdrawalmoneynotes(models.Model):
    autoid = models.AutoField(primary_key=True)
    clientid = models.CharField(db_column='ClientID', max_length=30)  # Field name made lowercase.
    clientname = models.CharField(db_column='ClientName', max_length=30)  # Field name made lowercase.
    salerid = models.CharField(db_column='SalerID', max_length=10)  # Field name made lowercase.
    salername = models.CharField(db_column='SalerName', max_length=30)  # Field name made lowercase.
    paydate = models.DateField(db_column='PayDate')  # Field name made lowercase.
    money = models.DecimalField(db_column='Money', max_digits=12, decimal_places=2)  # Field name made lowercase.
    creatorid = models.CharField(db_column='CreatorID', max_length=10)  # Field name made lowercase.
    creatorname = models.CharField(db_column='CreatorName', max_length=30)  # Field name made lowercase.
    auditorid = models.CharField(db_column='AuditorID', max_length=10)  # Field name made lowercase.
    auditorname = models.CharField(db_column='AuditorName', max_length=30)  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    remark = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'withdrawalmoneynotes'


class Workerpost(models.Model):
    clerkid = models.CharField(db_column='ClerkID', max_length=30)  # Field name made lowercase.
    deptid = models.CharField(db_column='DeptID', max_length=10)  # Field name made lowercase.
    plid = models.IntegerField(db_column='plID')  # Field name made lowercase.
    postname = models.CharField(db_column='PostName', max_length=30)  # Field name made lowercase.
    autoid = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'workerpost'
        unique_together = (('clerkid', 'deptid', 'plid', 'postname'),)


class Workflow(models.Model):
    autoid = models.AutoField(primary_key=True)
    plid = models.IntegerField(db_column='plID')  # Field name made lowercase.
    seqid = models.IntegerField(db_column='SeqID')  # Field name made lowercase.
    postname = models.CharField(db_column='PostName', max_length=100)  # Field name made lowercase.
    options = models.PositiveIntegerField(db_column='Options')  # Field name made lowercase.
    roomname = models.CharField(db_column='RoomName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'workflow'
        unique_together = (('plid', 'postname'),)

