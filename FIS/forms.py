from django import forms


from FIS.models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields=('eNumber', 'Assigned_User', 'Seniorty_Date', 'Computer_Name', 'Asset_Tag','Service_Tag','Model_Name','Warranty_EndDate','Warranty_Status','ModelBrand_Name','ModelParent_Name','Docking_Station','Secreen1_Model','Secreen1_ServiceTag','Secreen2_Model','Secreen2_ServiceTag','Model_USBheadset','SN_USBheadset','Model_DeskPhoneHeadset','SN_DeskPhone')


class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields=('eNumber', 'Assigned_User', 'Seniorty_Date', 'Computer_Name', 'Asset_Tag','Service_Tag','Model_Name','Warranty_EndDate','Warranty_Status','ModelBrand_Name','ModelParent_Name','Docking_Station','Secreen1_Model','Secreen1_ServiceTag','Secreen2_Model','Secreen2_ServiceTag','Model_USBheadset','SN_USBheadset','Model_DeskPhoneHeadset','SN_DeskPhone')


