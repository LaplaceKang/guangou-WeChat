# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    adminid = models.AutoField(db_column='adminID', primary_key=True)  # Field name made lowercase.
    adminname = models.CharField(db_column='adminName', max_length=30)  # Field name made lowercase.
    identitynumber = models.CharField(db_column='identityNumber', max_length=18, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=11)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    openid = models.CharField(max_length=255, blank=True, null=True)
    isvaild = models.IntegerField(db_column='isVaild')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class AdminAdminCourt(models.Model):
    adminid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminID', related_name='%(class)s_adminid')  # Field name made lowercase.
    admincourtid = models.ForeignKey('AdminCourt', models.DO_NOTHING, db_column='adminCourtID', related_name='%(class)s_admincourtid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin-admin_court'


class AdminCourt(models.Model):
    admincourtid = models.AutoField(db_column='adminCourtID', primary_key=True)  # Field name made lowercase.
    admincourtname = models.CharField(db_column='adminCourtName', max_length=30)  # Field name made lowercase.
    identitynumber = models.CharField(db_column='identityNumber', max_length=18, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=11)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    openid = models.CharField(max_length=255, blank=True, null=True)
    isvaild = models.IntegerField(db_column='isVaild')  # Field name made lowercase.
    courtid = models.ForeignKey('Court', models.DO_NOTHING, db_column='courtID', blank=True, null=True, related_name='%(class)s_courtid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_court'


class Court(models.Model):
    courtid = models.AutoField(db_column='courtID', primary_key=True)  # Field name made lowercase.
    courtname = models.CharField(db_column='courtName', max_length=50)  # Field name made lowercase.
    courttypeid = models.ForeignKey('CourtType', models.DO_NOTHING, db_column='courtTypeID', related_name='%(class)s_courttypeid')  # Field name made lowercase.
    lowestprice = models.DecimalField(db_column='lowestPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    venueid = models.ForeignKey('Venue', models.DO_NOTHING, db_column='venueID', related_name='%(class)s_venueid')  # Field name made lowercase.
    starttime = models.TimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    businesstime = models.TextField(db_column='businessTime', blank=True, null=True)  # Field name made lowercase.
    specifications = models.TextField(blank=True, null=True)
    bookingrules = models.TextField(db_column='bookingRules', blank=True, null=True)  # Field name made lowercase.
    validperiod = models.TextField(db_column='validPeriod', blank=True, null=True)  # Field name made lowercase.
    cancelrule = models.TextField(db_column='cancelRule', blank=True, null=True)  # Field name made lowercase.
    userule = models.TextField(db_column='useRule', blank=True, null=True)  # Field name made lowercase.
    isusable = models.IntegerField(db_column='isUsable')  # Field name made lowercase.
    closingstartdate = models.DateTimeField(db_column='closingStartDate', blank=True, null=True)  # Field name made lowercase.
    closingenddate = models.DateTimeField(db_column='closingEndDate', blank=True, null=True)  # Field name made lowercase.
    closingreason = models.TextField(db_column='closingReason', blank=True, null=True)  # Field name made lowercase.
    havingmeasuredcard = models.IntegerField(db_column='havingMeasuredCard', blank=True, null=True)  # Field name made lowercase.
    havingrechargecard = models.IntegerField(db_column='havingRechargeCard', blank=True, null=True)  # Field name made lowercase.
    havingperiodcard = models.IntegerField(db_column='havingPeriodCard', blank=True, null=True)  # Field name made lowercase.
    timeinterval = models.TimeField(db_column='timeInterval', blank=True, null=True)  # Field name made lowercase.
    minrentaltime = models.TimeField(db_column='minRentalTime', blank=True, null=True)  # Field name made lowercase.
    siteidentification = models.CharField(db_column='siteIdentification', max_length=10, blank=True, null=True)  # Field name made lowercase.
    minreservationmethodid = models.ForeignKey('CourtMinReservationMethod', models.DO_NOTHING, db_column='minReservationMethodID', blank=True, null=True, related_name='%(class)s_minreservationmethodid')  # Field name made lowercase.
    orderadvancedays = models.IntegerField(db_column='orderAdvanceDays', blank=True, null=True)  # Field name made lowercase.
    orderstarttime = models.TimeField(db_column='orderStartTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court'


class CourtCourtFacility(models.Model):
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    facilityid = models.ForeignKey('CourtFacility', models.DO_NOTHING, db_column='facilityID', related_name='%(class)s_facilityid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court-court_facility'


class CourtCourtType(models.Model):
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    courttypeid = models.ForeignKey('CourtType', models.DO_NOTHING, db_column='courtTypeID', related_name='%(class)s_courttypeid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court-court_type'


class CourtSiteSpecification(models.Model):
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    sitespecificationid = models.ForeignKey('SiteSpecification', models.DO_NOTHING, db_column='siteSpecificationID', related_name='%(class)s_sitespecificationid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court-site_specification'


class CourtCampaignType(models.Model):
    campaigntypeid = models.IntegerField(db_column='campaignTypeID', primary_key=True)  # Field name made lowercase.
    campaigntypename = models.CharField(db_column='campaignTypeName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_campaign_type'


class CourtCourse(models.Model):
    courtcourseid = models.IntegerField(db_column='courtCourseID', primary_key=True)  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    courtname = models.CharField(db_column='courtName', max_length=30)  # Field name made lowercase.
    coursename = models.CharField(db_column='courseName', max_length=30)  # Field name made lowercase.
    mondayeffective = models.IntegerField(db_column='mondayEffective', blank=True, null=True)  # Field name made lowercase.
    tuesdayeffective = models.IntegerField(db_column='tuesdayEffective', blank=True, null=True)  # Field name made lowercase.
    wednesdayeffective = models.IntegerField(db_column='wednesdayEffective', blank=True, null=True)  # Field name made lowercase.
    thursdayeffective = models.IntegerField(db_column='thursdayEffective', blank=True, null=True)  # Field name made lowercase.
    fridayeffective = models.IntegerField(db_column='fridayEffective', blank=True, null=True)  # Field name made lowercase.
    saturdayeffective = models.IntegerField(db_column='saturdayEffective', blank=True, null=True)  # Field name made lowercase.
    sundayeffective = models.IntegerField(db_column='sundayEffective', blank=True, null=True)  # Field name made lowercase.
    applyallsite = models.IntegerField(db_column='applyAllSite', blank=True, null=True)  # Field name made lowercase.
    starttime = models.TimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    teacher = models.CharField(max_length=10, blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    iseffective = models.IntegerField(db_column='isEffective', blank=True, null=True)  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='effectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='effectiveEndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_course'


class CourtCourseSite(models.Model):
    courtcourseid = models.ForeignKey(CourtCourse, models.DO_NOTHING, db_column='courtCourseID', related_name='%(class)s_courtcourseid')  # Field name made lowercase.
    siteid = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    sitename = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteName', related_name='%(class)s_sitename')  # Field name made lowercase.
    childsiteid = models.ForeignKey('SiteChild', models.DO_NOTHING, db_column='childSiteID', blank=True, null=True, related_name='%(class)s_childsiteid')  # Field name made lowercase.
    childsitename = models.ForeignKey('SiteChild', models.DO_NOTHING, db_column='childSiteName', blank=True, null=True, related_name='%(class)s_childsitename')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_course-site'


class CourtDiscountCard(models.Model):
    discountcardid = models.AutoField(db_column='discountCardID', primary_key=True)  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID')  # Field name made lowercase.
    discountcardtypeid = models.ForeignKey('CourtDiscountCardType', models.DO_NOTHING, db_column='discountCardTypeID', blank=True, null=True)  # Field name made lowercase.
    discountcardname = models.CharField(db_column='discountCardName', max_length=30)  # Field name made lowercase.
    sellingprice = models.DecimalField(db_column='sellingPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    giftprice = models.DecimalField(db_column='giftPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    availabletimes = models.IntegerField(db_column='availableTimes', blank=True, null=True)  # Field name made lowercase.
    gifttimes = models.IntegerField(db_column='giftTimes', blank=True, null=True)  # Field name made lowercase.
    day = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'court_discount_card'


class CourtDiscountCardType(models.Model):
    discountcardtypeid = models.AutoField(db_column='discountCardTypeID', primary_key=True)  # Field name made lowercase.
    discountcardtypename = models.CharField(db_column='discountCardTypeName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_discount_card_type'


class CourtDiscountCardUserType(models.Model):
    discountcardid = models.ForeignKey(CourtDiscountCard, models.DO_NOTHING, db_column='discountCardID', related_name='%(class)s_discountcardid')  # Field name made lowercase.
    usertypeid = models.ForeignKey('UserType', models.DO_NOTHING, db_column='userTypeID', related_name='%(class)s_usertypeid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_discount_card_user_type'


class CourtFacility(models.Model):
    facilityid = models.AutoField(db_column='facilityID', primary_key=True)  # Field name made lowercase.
    facilityname = models.CharField(db_column='facilityName', max_length=30)  # Field name made lowercase.
    facilityicon = models.CharField(db_column='facilityIcon', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_facility'


class CourtImg(models.Model):
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    courtimg = models.CharField(db_column='courtImg', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_img'


class CourtInsideMap(models.Model):
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    courtinsidemap = models.CharField(db_column='courtInsideMap', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_inside_map'


class CourtMinReservationMethod(models.Model):
    minreservationmethodid = models.AutoField(db_column='MinReservationMethodID', primary_key=True)  # Field name made lowercase.
    minreservationmethodname = models.CharField(db_column='MinReservationMethodName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_min_reservation_method'


class CourtPrizeManagement(models.Model):
    courtprizemanagementid = models.AutoField(db_column='courtPrizeManagementID', primary_key=True)  # Field name made lowercase.
    managementname = models.CharField(db_column='managementName', max_length=255)  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    courtname = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtName', related_name='%(class)s_courtname')  # Field name made lowercase.
    iseffective = models.IntegerField(db_column='isEffective')  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='effectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='effectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    applywholesite = models.IntegerField(db_column='applyWholeSite', blank=True, null=True)  # Field name made lowercase.
    applyallsite = models.IntegerField(db_column='applyAllSite', blank=True, null=True)  # Field name made lowercase.
    mondayeffective = models.IntegerField(db_column='mondayEffective')  # Field name made lowercase.
    tuesdayeffective = models.IntegerField(db_column='tuesdayEffective')  # Field name made lowercase.
    wednesdayeffective = models.IntegerField(db_column='wednesdayEffective')  # Field name made lowercase.
    thursdayeffective = models.IntegerField(db_column='thursdayEffective')  # Field name made lowercase.
    fridayeffective = models.IntegerField(db_column='fridayEffective')  # Field name made lowercase.
    saturdayeffective = models.IntegerField(db_column='saturdayEffective')  # Field name made lowercase.
    sundayeffective = models.IntegerField(db_column='sundayEffective')  # Field name made lowercase.
    userprice = models.DecimalField(db_column='userPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    studentprice = models.DecimalField(db_column='studentPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    staffprice = models.DecimalField(db_column='staffPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_prize_management'


class CourtPrizeManagementSite(models.Model):
    courtprizemanagementid = models.ForeignKey(CourtPrizeManagement, models.DO_NOTHING, db_column='courtPrizeManagementID', related_name='%(class)s_courtprizemanagementid')  # Field name made lowercase.
    siteid = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    sitename = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteName', related_name='%(class)s_sitename')  # Field name made lowercase.
    childsiteid = models.ForeignKey('SiteChild', models.DO_NOTHING, db_column='childSiteID', blank=True, null=True, related_name='%(class)s_childsiteid')  # Field name made lowercase.
    childsitename = models.ForeignKey('SiteChild', models.DO_NOTHING, db_column='childSiteName', blank=True, null=True, related_name='%(class)s_childsitename')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_prize_management-site'


class CourtTeaching(models.Model):
    courtteachingid = models.AutoField(db_column='courtTeachingID', primary_key=True)  # Field name made lowercase.
    courtteachingname = models.CharField(db_column='courtTeachingName', max_length=255)  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    courtname = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtName', related_name='%(class)s_courtname')  # Field name made lowercase.
    iseffective = models.IntegerField(db_column='isEffective')  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='effectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='effectiveEndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_teaching'


class CourtTeachingSession(models.Model):
    courtteachingsessionid = models.AutoField(db_column='courtTeachingSessionID', primary_key=True)  # Field name made lowercase.
    courtteachingid = models.ForeignKey(CourtTeaching, models.DO_NOTHING, db_column='courtTeachingID', related_name='%(class)s_courtteachingid')  # Field name made lowercase.
    sessionname = models.CharField(db_column='sessionName', max_length=30)  # Field name made lowercase.
    starttime = models.TimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime')  # Field name made lowercase.
    applyallsite = models.IntegerField(db_column='applyAllSite', blank=True, null=True)  # Field name made lowercase.
    mondayeffective = models.IntegerField(db_column='mondayEffective', blank=True, null=True)  # Field name made lowercase.
    tuesdayeffective = models.IntegerField(db_column='tuesdayEffective', blank=True, null=True)  # Field name made lowercase.
    wednesdayeffective = models.IntegerField(db_column='wednesdayEffective', blank=True, null=True)  # Field name made lowercase.
    thursdayeffective = models.IntegerField(db_column='thursdayEffective', blank=True, null=True)  # Field name made lowercase.
    fridayeffective = models.IntegerField(db_column='fridayEffective', blank=True, null=True)  # Field name made lowercase.
    saturdayeffective = models.IntegerField(db_column='saturdayEffective', blank=True, null=True)  # Field name made lowercase.
    sundayeffective = models.IntegerField(db_column='sundayEffective', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_teaching_session'


class CourtTeachingSessionSite(models.Model):
    courtteachingsessionid = models.ForeignKey(CourtTeachingSession, models.DO_NOTHING, db_column='courtTeachingSessionID', related_name='%(class)s_courtteachingsessionid')  # Field name made lowercase.
    siteid = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    sitename = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteName', related_name='%(class)s_sitename')  # Field name made lowercase.
    childsiteid = models.ForeignKey('SiteChild', models.DO_NOTHING, db_column='childSiteID', blank=True, null=True, related_name='%(class)s_childsiteid')  # Field name made lowercase.
    childsitename = models.ForeignKey('SiteChild', models.DO_NOTHING, db_column='childSiteName', blank=True, null=True, related_name='%(class)s_childsitename')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_teaching_session-site'


class CourtTeachingSessionUser(models.Model):
    courtteachingsessionid = models.ForeignKey(CourtTeachingSession, models.DO_NOTHING, db_column='courtTeachingSessionID', related_name='%(class)s_courtteachingsessionid')  # Field name made lowercase.
    usertypeid = models.ForeignKey('UserType', models.DO_NOTHING, db_column='userTypeID', related_name='%(class)s_usertypeid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_teaching_session-user'


class CourtTimeManagement(models.Model):
    courttimemanagementid = models.AutoField(db_column='courtTimeManagementID', primary_key=True)  # Field name made lowercase.
    managementname = models.CharField(db_column='managementName', max_length=255)  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    courtname = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtName', related_name='%(class)s_courtname')  # Field name made lowercase.
    starttime = models.TimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime')  # Field name made lowercase.
    interval = models.IntegerField(blank=True, null=True)
    iseffective = models.IntegerField(db_column='isEffective')  # Field name made lowercase.
    effectivestartdate = models.DateField(db_column='effectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateField(db_column='effectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    applywholesite = models.IntegerField(db_column='applyWholeSite', blank=True, null=True)  # Field name made lowercase.
    mondayeffective = models.IntegerField(db_column='mondayEffective', blank=True, null=True)  # Field name made lowercase.
    tuesdayeffective = models.IntegerField(db_column='tuesdayEffective', blank=True, null=True)  # Field name made lowercase.
    wednesdayeffective = models.IntegerField(db_column='wednesdayEffective', blank=True, null=True)  # Field name made lowercase.
    thursdayeffective = models.IntegerField(db_column='thursdayEffective', blank=True, null=True)  # Field name made lowercase.
    fridayeffective = models.IntegerField(db_column='fridayEffective', blank=True, null=True)  # Field name made lowercase.
    saturdayeffective = models.IntegerField(db_column='saturdayEffective', blank=True, null=True)  # Field name made lowercase.
    sundayeffective = models.IntegerField(db_column='sundayEffective', blank=True, null=True)  # Field name made lowercase.
    isprimetime = models.IntegerField(db_column='isPrimeTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_time_management'


class CourtTimeManagementSite(models.Model):
    courttimemanagementid = models.ForeignKey(CourtTimeManagement, models.DO_NOTHING, db_column='courtTimeManagementID', related_name='%(class)s_courttimemanagementid')  # Field name made lowercase.
    siteid = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    sitename = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteName', related_name='%(class)s_sitename')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_time_management-site'


class CourtType(models.Model):
    courttypeid = models.IntegerField(db_column='courtTypeID', primary_key=True)  # Field name made lowercase.
    courttypename = models.CharField(db_column='courtTypeName', max_length=30)  # Field name made lowercase.
    campaigntypeid = models.ForeignKey(CourtCampaignType, models.DO_NOTHING, db_column='campaignTypeID', blank=True, null=True, related_name='%(class)s_campaigntypeid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'court_type'


class LegalPerson(models.Model):
    legalid = models.AutoField(db_column='legalID', primary_key=True)  # Field name made lowercase.
    legalname = models.CharField(db_column='legalName', max_length=10)  # Field name made lowercase.
    documenttypeid = models.ForeignKey('LegalPersonDocument', models.DO_NOTHING, db_column='documentTypeID', blank=True, null=True, related_name='%(class)s_documenttypeid')  # Field name made lowercase.
    documentnumber = models.CharField(db_column='documentNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    frontimg = models.CharField(db_column='frontImg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reverseimg = models.CharField(db_column='reverseImg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    handheldfrontimg = models.CharField(db_column='handheldFrontImg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    documentvalidstartdate = models.DateField(db_column='documentValidStartDate', blank=True, null=True)  # Field name made lowercase.
    documentvalidenddate = models.DateField(db_column='documentValidEndDate', blank=True, null=True)  # Field name made lowercase.
    islongterm = models.IntegerField(db_column='isLongTerm', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=11)  # Field name made lowercase.
    password = models.CharField(max_length=255, blank=True, null=True)
    img = models.CharField(max_length=255, blank=True, null=True)
    venueid = models.ForeignKey('Venue', models.DO_NOTHING, db_column='venueID', blank=True, null=True, related_name='%(class)s_venueid')  # Field name made lowercase.
    openid = models.CharField(max_length=255, blank=True, null=True)
    isvaild = models.IntegerField(db_column='isVaild', blank=True, null=True)  # Field name made lowercase.
    isnewuser = models.IntegerField(db_column='isNewUser', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'legal_person'


class LegalPersonAdmin(models.Model):
    legalid = models.ForeignKey(LegalPerson, models.DO_NOTHING, db_column='legalID', related_name='%(class)s_legalid')  # Field name made lowercase.
    adminid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminID', related_name='%(class)s_adminid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'legal_person-admin'


class LegalPersonDocument(models.Model):
    documenttypeid = models.AutoField(db_column='documentTypeID', primary_key=True)  # Field name made lowercase.
    documenttypename = models.CharField(db_column='documentTypeName', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'legal_person_document'


class OrderAddAmount(models.Model):
    supplementalamountorderid = models.IntegerField(db_column='supplementalAmountOrderID', primary_key=True)  # Field name made lowercase.
    siteorderid = models.ForeignKey('OrderSite', models.DO_NOTHING, db_column='siteOrderID', related_name='%(class)s_siteorderid')  # Field name made lowercase.
    supplementaryamount = models.DecimalField(db_column='supplementaryAmount', max_digits=10, decimal_places=2)  # Field name made lowercase.
    orderstateid = models.ForeignKey('OrderState', models.DO_NOTHING, db_column='orderStateID', related_name='%(class)s_orderstateid')  # Field name made lowercase.
    reasonid = models.ForeignKey('OrderAddAmountReason', models.DO_NOTHING, db_column='reasonID', blank=True, null=True, related_name='%(class)s_reasonid')  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_add_amount'


class OrderAddAmountReason(models.Model):
    addreasonid = models.IntegerField(db_column='addReasonID', primary_key=True)  # Field name made lowercase.
    addreason = models.TextField(db_column='addReason', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_add_amount_reason'


class OrderCardType(models.Model):
    cardtypeid = models.IntegerField(db_column='cardTypeID', primary_key=True)  # Field name made lowercase.
    cardtypename = models.CharField(db_column='cardTypeName', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_card_type'


class OrderLongBook(models.Model):
    longbookorderid = models.IntegerField(db_column='longBookOrderID', primary_key=True)  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    siteid = models.ForeignKey('SiteAllPeriod', models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    sitename = models.ForeignKey('SiteAllPeriod', models.DO_NOTHING, db_column='siteName', related_name='%(class)s_sitename')  # Field name made lowercase.
    childsitename = models.CharField(db_column='childSiteName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    childsiteid = models.ForeignKey('SiteAllPeriod', models.DO_NOTHING, db_column='childSiteID', blank=True, null=True, related_name='%(class)s_childsiteid')  # Field name made lowercase.
    mondaybooking = models.IntegerField(db_column='mondayBooking', blank=True, null=True)  # Field name made lowercase.
    tuesdaybooking = models.IntegerField(db_column='tuesdayBooking', blank=True, null=True)  # Field name made lowercase.
    wednesdaybooking = models.IntegerField(db_column='wednesdayBooking', blank=True, null=True)  # Field name made lowercase.
    thursdaybooking = models.IntegerField(db_column='thursdayBooking', blank=True, null=True)  # Field name made lowercase.
    fridaybooking = models.IntegerField(db_column='fridayBooking', blank=True, null=True)  # Field name made lowercase.
    saturdaybooking = models.IntegerField(db_column='saturdayBooking', blank=True, null=True)  # Field name made lowercase.
    sundaybooking = models.IntegerField(db_column='sundayBooking', blank=True, null=True)  # Field name made lowercase.
    periodstartid = models.ForeignKey('SiteAllPeriod', models.DO_NOTHING, db_column='periodStartID', related_name='%(class)s_periodstartid')  # Field name made lowercase.
    periodendid = models.ForeignKey('SiteAllPeriod', models.DO_NOTHING, db_column='periodEndID', related_name='%(class)s_periodendid')  # Field name made lowercase.
    startdate = models.DateField(db_column='startDate')  # Field name made lowercase.
    enddate = models.DateField(db_column='endDate')  # Field name made lowercase.
    orderstateid = models.ForeignKey('OrderState', models.DO_NOTHING, db_column='orderStateID', related_name='%(class)s_orderstateid')  # Field name made lowercase.
    singledeductionamount = models.DecimalField(db_column='singleDeductionAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cardtypeid = models.ForeignKey(OrderCardType, models.DO_NOTHING, db_column='cardTypeID', blank=True, null=True, related_name='%(class)s_cardtypeid')  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_long_book'


class OrderPayMethod(models.Model):
    paymentmethodid = models.IntegerField(db_column='paymentMethodID', primary_key=True)  # Field name made lowercase.
    paymentmethodname = models.CharField(db_column='paymentMethodName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_pay_method'


class OrderSite(models.Model):
    siteorderid = models.AutoField(db_column='siteOrderID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', related_name='%(class)s_userid')  # Field name made lowercase.
    venueid = models.ForeignKey('Venue', models.DO_NOTHING, db_column='venueID', related_name='%(class)s_venueid')  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', blank=True, null=True, related_name='%(class)s_courtid')  # Field name made lowercase.
    ordertime = models.DateTimeField(db_column='orderTime')  # Field name made lowercase.
    orderstateid = models.ForeignKey('OrderState', models.DO_NOTHING, db_column='orderStateID', related_name='%(class)s_orderstateid')  # Field name made lowercase.
    paymentmethodid = models.ForeignKey(OrderPayMethod, models.DO_NOTHING, db_column='paymentMethodID', blank=True, null=True, related_name='%(class)s_paymentmethodid')  # Field name made lowercase.
    cancelremaintime = models.TimeField(db_column='cancelRemainTime', blank=True, null=True)  # Field name made lowercase.
    courttypename = models.CharField(db_column='courtTypeName', max_length=30)  # Field name made lowercase.
    originalprice = models.DecimalField(db_column='originalPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    userdiscountcardid = models.ForeignKey('UserDiscountCard', models.DO_NOTHING, db_column='userDiscountCardID', blank=True, null=True, related_name='%(class)s_userdiscountcardid')  # Field name made lowercase.
    discountedprice = models.DecimalField(db_column='discountedPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paidprice = models.DecimalField(db_column='paidPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_site'


class OrderSiteChild(models.Model):
    sitechildorderid = models.AutoField(db_column='siteChildOrderID', primary_key=True)  # Field name made lowercase.
    siteorderid = models.ForeignKey(OrderSite, models.DO_NOTHING, db_column='siteOrderID', related_name='%(class)s_siteorderid')  # Field name made lowercase.
    siteid = models.ForeignKey('Site', models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    childsiteid = models.ForeignKey('SiteChild', models.DO_NOTHING, db_column='childSiteID', blank=True, null=True, related_name='%(class)s_childsiteid')  # Field name made lowercase.
    cancelremaintime = models.TimeField(db_column='cancelRemainTime', blank=True, null=True)  # Field name made lowercase.
    sitename = models.CharField(db_column='siteName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    childsitename = models.CharField(db_column='childSiteName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(blank=True, null=True)
    starttime = models.TimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='endtime', blank=True, null=True)  # Field name made lowercase.
    originalprice = models.DecimalField(db_column='originalPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    userdiscountcardid = models.IntegerField(db_column='userDiscountCardID', blank=True, null=True)  # Field name made lowercase.
    discountedprice = models.DecimalField(db_column='discountedPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paidamount = models.DecimalField(db_column='paidAmount', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_site_child'
        unique_together = (('sitechildorderid', 'siteorderid'),)


class OrderState(models.Model):
    orderstateid = models.IntegerField(db_column='orderStateID', primary_key=True)  # Field name made lowercase.
    orderstatename = models.CharField(db_column='orderStateName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_state'


class Site(models.Model):
    siteid = models.AutoField(db_column='siteID', primary_key=True)  # Field name made lowercase.
    sitespecificationid = models.ForeignKey('SiteSpecification', models.DO_NOTHING, db_column='siteSpecificationID', blank=True, null=True, related_name='%(class)s_sitespecificationid')  # Field name made lowercase.
    sitename = models.CharField(db_column='siteName', max_length=30)  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    isusable = models.IntegerField(db_column='isUsable')  # Field name made lowercase.
    havingchildsite = models.IntegerField(db_column='havingChildSite')  # Field name made lowercase.
    closingstartdate = models.DateTimeField(db_column='closingStartDate', blank=True, null=True)  # Field name made lowercase.
    closingenddate = models.DateTimeField(db_column='closingEndDate', blank=True, null=True)  # Field name made lowercase.
    closingreason = models.TextField(db_column='closingReason', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site'


class SiteAllPeriod(models.Model):
    periodid = models.AutoField(db_column='periodID', primary_key=True)  # Field name made lowercase.
    week = models.IntegerField()
    siteperiodid = models.IntegerField(db_column='sitePeriodID')  # Field name made lowercase.
    siteid = models.ForeignKey(Site, models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    sitename = models.ForeignKey(Site, models.DO_NOTHING, db_column='siteName', related_name='%(class)s_sitename')  # Field name made lowercase.
    date = models.DateField()
    childsiteid = models.ForeignKey('SiteChild', models.DO_NOTHING, db_column='childSiteID', blank=True, null=True, related_name='%(class)s_childsiteid')  # Field name made lowercase.
    childsitename = models.ForeignKey('SiteChild', models.DO_NOTHING, db_column='childSiteName', blank=True, null=True, related_name='%(class)s_childsitename')  # Field name made lowercase.
    starttime = models.TimeField(db_column='startTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.TimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    stateid = models.ForeignKey('SitePeriodState', models.DO_NOTHING, db_column='stateID', blank=True, null=True, related_name='%(class)s_stateid')  # Field name made lowercase.
    prompt = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    studentprice = models.DecimalField(db_column='studentPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    staffprice = models.DecimalField(db_column='staffPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    orderusername = models.CharField(db_column='orderUserName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    orderuserpaymethod = models.CharField(db_column='orderUserPayMethod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    needsubcard = models.IntegerField(db_column='needSubcard', blank=True, null=True)  # Field name made lowercase.
    teachingperiodname = models.CharField(db_column='teachingPeriodName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    teacher = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_all_period'


class SiteBundlingPeriod(models.Model):
    bundlingperiodid = models.IntegerField(db_column='bundlingPeriodID', primary_key=True)  # Field name made lowercase.
    periodstartid = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='periodStartID', related_name='%(class)s_periodstartid')  # Field name made lowercase.
    periodendid = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='periodEndID', related_name='%(class)s_periodendid')  # Field name made lowercase.
    siteid = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    childsiteid = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='childSiteID', blank=True, null=True, related_name='%(class)s_childsiteid')  # Field name made lowercase.
    date = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='date', related_name='%(class)s_date')

    class Meta:
        managed = False
        db_table = 'site_bundling_period'


class SiteChild(models.Model):
    siteid = models.ForeignKey(Site, models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    childsiteid = models.IntegerField(db_column='childSiteID', primary_key=True)  # Field name made lowercase.
    childsitespecificationid = models.ForeignKey('SiteSpecification', models.DO_NOTHING, db_column='childSiteSpecificationID', blank=True, null=True, related_name='%(class)s_childsitespecificationid')  # Field name made lowercase.
    childsitename = models.CharField(db_column='childSiteName', max_length=30)  # Field name made lowercase.
    isusable = models.IntegerField(db_column='isUsable')  # Field name made lowercase.
    closingstartdate = models.DateTimeField(db_column='closingStartDate', blank=True, null=True)  # Field name made lowercase.
    closingenddate = models.DateTimeField(db_column='closingEndDate', blank=True, null=True)  # Field name made lowercase.
    closingreason = models.TextField(db_column='closingReason', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site_child'
        unique_together = (('childsiteid', 'siteid'),)


class SitePeriodState(models.Model):
    stateid = models.AutoField(db_column='stateID', primary_key=True)  # Field name made lowercase.
    statename = models.CharField(db_column='stateName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site_period_state'


class SiteSpecification(models.Model):
    sitespecificationid = models.IntegerField(db_column='siteSpecificationID', primary_key=True)  # Field name made lowercase.
    sitespecificationname = models.CharField(db_column='siteSpecificationName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site_specification'


class SiteTeachingUserType(models.Model):
    periodid = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='periodID', related_name='%(class)s_periodid')  # Field name made lowercase.
    usertypeid = models.ForeignKey('UserType', models.DO_NOTHING, db_column='userTypeID', blank=True, null=True, related_name='%(class)s_usertypeid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site_teaching-user_type'


class SiteWeekAllPeriod(models.Model):
    periodid = models.AutoField(db_column='periodID', primary_key=True)  # Field name made lowercase.
    week = models.IntegerField()
    siteperiodid = models.IntegerField(db_column='sitePeriodID')  # Field name made lowercase.
    siteid = models.ForeignKey(Site, models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    sitename = models.ForeignKey(Site, models.DO_NOTHING, db_column='siteName', related_name='%(class)s_sitename')  # Field name made lowercase.
    childsiteid = models.ForeignKey(SiteChild, models.DO_NOTHING, db_column='childSiteID', blank=True, null=True, related_name='%(class)s_childsiteid')  # Field name made lowercase.
    childsitename = models.ForeignKey(SiteChild, models.DO_NOTHING, db_column='childSiteName', blank=True, null=True, related_name='%(class)s_childsitename')  # Field name made lowercase.
    startdate = models.TimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.TimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    stateid = models.ForeignKey(SitePeriodState, models.DO_NOTHING, db_column='stateID', blank=True, null=True, related_name='%(class)s_stateid')  # Field name made lowercase.
    prompt = models.CharField(max_length=50, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    studentprice = models.DecimalField(db_column='studentPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    staffprice = models.DecimalField(db_column='staffPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    orderusername = models.CharField(db_column='orderUserName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    orderuserpaymethod = models.CharField(db_column='orderUserPayMethod', max_length=30, blank=True, null=True)  # Field name made lowercase.
    needsubcard = models.IntegerField(db_column='needSubcard', blank=True, null=True)  # Field name made lowercase.
    teachingperiodname = models.CharField(db_column='teachingPeriodName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    teacher = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'site_week_all_period'


class SiteWeekBundlingPeriod(models.Model):
    bundlingperiodid = models.IntegerField(db_column='bundlingPeriodID', primary_key=True)  # Field name made lowercase.
    periodstartid = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='periodStartID', related_name='%(class)s_periodstartid')  # Field name made lowercase.
    periodendid = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='periodEndID', related_name='%(class)s_periodendid')  # Field name made lowercase.
    siteid = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='siteID', related_name='%(class)s_siteid')  # Field name made lowercase.
    childsiteid = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='childSiteID', blank=True, null=True, related_name='%(class)s_childsiteid')  # Field name made lowercase.
    date = models.ForeignKey(SiteAllPeriod, models.DO_NOTHING, db_column='date', related_name='%(class)s_date')

    class Meta:
        managed = False
        db_table = 'site_week_bundling_period'


class SiteWeekTeachingUsersType(models.Model):
    periodid = models.ForeignKey(SiteWeekAllPeriod, models.DO_NOTHING, db_column='periodID', related_name='%(class)s_periodid')  # Field name made lowercase.
    usertypeid = models.ForeignKey('UserType', models.DO_NOTHING, db_column='userTypeID', related_name='%(class)s_usertypeid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'site_week_teaching-users_type'


class User(models.Model):
    userid = models.AutoField(db_column='userID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    identitynumber = models.CharField(db_column='identityNumber', max_length=18, blank=True, null=True)  # Field name made lowercase.
    studentid = models.CharField(db_column='studentID', max_length=30, blank=True, null=True)  # Field name made lowercase.
    usertypeid = models.ForeignKey('UserType', models.DO_NOTHING, db_column='userTypeID', related_name='%(class)s_usertypeid')  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=11, blank=True, null=True)  # Field name made lowercase.
    nickname = models.CharField(max_length=30, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    userstudentimg = models.CharField(db_column='userStudentImg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    useravatar = models.CharField(db_column='userAvatar', max_length=255, blank=True, null=True)  # Field name made lowercase.
    openid = models.CharField(db_column='openID', max_length=255)  # Field name made lowercase.
    checkintimes = models.IntegerField(db_column='checkInTimes', blank=True, null=True)  # Field name made lowercase.
    isvaild = models.IntegerField(db_column='isVaild', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class UserChargeRecord(models.Model):
    chargerecordid = models.IntegerField(db_column='chargeRecordID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userID', related_name='%(class)s_userid')  # Field name made lowercase.
    time = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    forcourt = models.IntegerField(db_column='forCourt', blank=True, null=True)  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', blank=True, null=True, related_name='%(class)s_courtid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_charge_record'


class UserCollectedVenue(models.Model):
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    venueid = models.ForeignKey('Venue', models.DO_NOTHING, db_column='venueID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_collected_venue'


class UserCourtRemainingPrice(models.Model):
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userID', related_name='%(class)s_userid')  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID', related_name='%(class)s_courtid')  # Field name made lowercase.
    remainingprice = models.DecimalField(db_column='remainingPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_court_remaining_price'


class UserDiscountCard(models.Model):
    userdiscountcardid = models.AutoField(db_column='userDiscountCardID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userID')  # Field name made lowercase.
    discountcardid = models.ForeignKey(CourtDiscountCard, models.DO_NOTHING, db_column='discountCardID')  # Field name made lowercase.
    courtid = models.ForeignKey(Court, models.DO_NOTHING, db_column='courtID')  # Field name made lowercase.
    remainingtimes = models.IntegerField(db_column='remainingTimes', blank=True, null=True)  # Field name made lowercase.
    remainingprice = models.DecimalField(db_column='remainingPrice', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.     
    isvaild = models.TextField(db_column='isVaild')  # Field name made lowercase. This field type is a guess.
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_discount_card'


class UserSchoolCourt(models.Model):
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userID', related_name='%(class)s_userid')  # Field name made lowercase.
    schoolvenueid = models.ForeignKey('Venue', models.DO_NOTHING, db_column='schoolVenueID', blank=True, null=True, related_name='%(class)s_schoolvenueid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_school_court'


class UserType(models.Model):
    usertypeid = models.AutoField(db_column='userTypeID', primary_key=True)  # Field name made lowercase.
    usertypename = models.CharField(db_column='userTypeName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_type'


class Venue(models.Model):
    venueid = models.IntegerField(db_column='venueID', primary_key=True)  # Field name made lowercase.
    venuename = models.CharField(db_column='venueName', max_length=50)  # Field name made lowercase.
    cityid = models.ForeignKey('VenueCity', models.DO_NOTHING, db_column='cityID', related_name='%(class)s_cityid')  # Field name made lowercase.
    address = models.CharField(max_length=50)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    latitude = models.FloatField()
    certificateimg = models.CharField(db_column='certificateImg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    homepageimg = models.CharField(db_column='homePageImg', max_length=255, blank=True, null=True)  # Field name made lowercase.
    addressshort = models.CharField(db_column='addressShort', max_length=30)  # Field name made lowercase.
    specialtip = models.TextField(db_column='specialTip', blank=True, null=True)  # Field name made lowercase.
    venuetypeid = models.ForeignKey('VenueType', models.DO_NOTHING, db_column='venueTypeID', blank=True, null=True, related_name='%(class)s_venuetypeid')  # Field name made lowercase.
    facadephoto = models.CharField(db_column='facadePhoto', max_length=255, blank=True, null=True)  # Field name made lowercase.
    in_storephotos = models.CharField(db_column='in-storePhotos', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    logo = models.CharField(max_length=255, blank=True, null=True)
    mainqualificationtypeid = models.ForeignKey('VenueMainQualificationType', models.DO_NOTHING, db_column='mainQualificationTypeID', blank=True, null=True, related_name='%(class)s_mainqualificationtypeid')  # Field name made lowercase.
    mainqualificationphotos = models.CharField(db_column='mainQualificationPhotos', max_length=255, blank=True, null=True)  # Field name made lowercase.
    industryqualificationtypeid = models.ForeignKey('VenueIndustryQualificationType', models.DO_NOTHING, db_column='industryQualificationTypeID', blank=True, null=True, related_name='%(class)s_industryqualificationtypeid')  # Field name made lowercase.
    industryqualificationphotos = models.CharField(db_column='industryQualificationPhotos', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=11, blank=True, null=True)  # Field name made lowercase.
    information = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venue'


class VenueVenueFacility(models.Model):
    venueid = models.ForeignKey(Venue, models.DO_NOTHING, db_column='venueID', related_name='%(class)s_venueid')  # Field name made lowercase.
    facilityid = models.ForeignKey(CourtFacility, models.DO_NOTHING, db_column='facilityID', related_name='%(class)s_facilityid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venue-venue_facility'


class VenueCourtType(models.Model):
    venueid = models.ForeignKey(Venue, models.DO_NOTHING, db_column='venueID')  # Field name made lowercase.
    courttypeid = models.ForeignKey(CourtType, models.DO_NOTHING, db_column='courtTypeID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venue-court_type'


class VenueCity(models.Model):
    cityid = models.IntegerField(db_column='cityID', primary_key=True)  # Field name made lowercase.
    cityname = models.CharField(db_column='cityName', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venue_city'
        
class VenueCityCourtType(models.Model):
    cityid = models.ForeignKey(VenueCity, models.DO_NOTHING, db_column='cityID')  # Field name made lowercase.
    courttypeid = models.ForeignKey(CourtType, models.DO_NOTHING, db_column='courtTypeID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venue_city-court_type'

class VenueImage(models.Model):
    venueid = models.ForeignKey(Venue, models.DO_NOTHING, db_column='venueID', related_name='%(class)s_venueid')  # Field name made lowercase.
    venueimg = models.CharField(db_column='venueImg', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venue_image'


class VenueIndustryQualificationType(models.Model):
    industryqualificationtypeid = models.IntegerField(db_column='industryQualificationTypeID', primary_key=True)  # Field name made lowercase.
    industryqualificationtypename = models.TextField(db_column='industryQualificationTypeName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venue_industry_qualification_type'


class VenueMainQualificationType(models.Model):
    mainqualificationtypeid = models.IntegerField(db_column='mainQualificationTypeID', primary_key=True)  # Field name made lowercase.
    mainqualificationtypename = models.TextField(db_column='mainQualificationTypeName', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venue_main_qualification_type'


class VenueType(models.Model):
    venuetypeid = models.IntegerField(db_column='venueTypeID', primary_key=True)  # Field name made lowercase.
    venuetypename = models.TextField(db_column='venueTypeName')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'venue_type'
