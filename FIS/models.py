from django.db import models
from django.db.models import CharField


class Device(models.Model):
    eNumber = models.CharField(max_length=100, null=True)
    Assigned_User = models.CharField(max_length=100, null=True)
    Seniorty_Date = models.DateField(null=True)
    Computer_Name = models.CharField(max_length=100, null=True,default='EX:EMEA-LP0440')
    Asset_Tag = models.IntegerField(null=True)
    Service_Tag = models.CharField(max_length=100, null=True)
    Model_Name = models.CharField(max_length=100, null=True)
    Warranty_EndDate = models.DateField(null=True)
    Status = (
        ('Out Of Warranty', 'Out Of Warranty'),
        ('In Warranty', 'In Warranty')

    )
    Warranty_Status = models.CharField(max_length=100, choices=Status, default='In Warranty', null=True)
    choices = (
        ('DELL', 'DELL'),
        ('Hewlett Packard', 'Hewlett Pckard')

    )
    ModelBrand_Name = models.CharField(max_length=100, choices=choices, default='DELL', null=True)
    choice = (
        ('Laptop', 'Laptop'),
        ('Desktop', 'Desktop')

    )
    ModelParent_Name = models.CharField(max_length=100, choices=choice, default='DELL', null=True)
    choix = (
        ('YES', 'YES'),
        ('NO', 'NO'),
        ('YES', 'yes'),
        ('NO', 'no')

    )
    Docking_Station = models.CharField(max_length=100, choices=choix, null=True,default='NO')
    Secreen1_Model = models.CharField(max_length=100, null=True)
    Secreen1_ServiceTag = models.CharField(max_length=100, null=True)
    Secreen2_Model = models.CharField(max_length=100, null=True)
    Secreen2_ServiceTag = models.CharField(max_length=100, null=True)
    choice = (
        ('Jabra UCV - 550', 'Jabra UCV - 550'),
        ('PLANTRONIC C 420', 'PLANTRONIC C 420'),
        ('SENNHEISER SC 60 USB CTRL', 'SENNHEISER SC 60 USB CTRL'),
        ('Jabra UCV - 750', 'Jabra UCV - 750'),
        ('JABRA - BIZ620', 'JABRA - BIZ620')

    )
    Model_USBheadset = models.CharField(max_length=100, choices=choice, null=True,default='SENNHEISER SC 60 USB CTRL')
    SN_USBheadset = models.IntegerField(null=True)
    choix = (
        ('SENNHEISER', 'SENNHEISER SC 230'),
        ('SENNHEISER ', 'SENNHEISER SC 260'),
        ('JABRA', 'Jabra  GN 2000'),
        ('JABRA', 'JABRA - GN 2000 - BIZ'),
        ('JABRA', 'JABRA GN 1216'),
        ('JABRA ', 'JABRA -SC 260'),
        ('JABRA ', 'JABRA - BIZ620'),
        ('JABRA', 'JABRA 2300'),
        ('JABRA', 'JABRA')

    )

    Model_DeskPhoneHeadset: CharField = models.CharField(max_length=100, choices=choix, null=True)
    SN_DeskPhone = models.IntegerField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type :{0},{1}'.format(self.eNumber, self.Assigned_User)


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class All_Products(Device):
    pass

# Create your models here.

