from django.db import models
from authentication.models import User


# Create your models here.

class Pharmacist(models.Model):
    GENDER_CHOICE = [
        ('SELECT GENDER', ''),
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(verbose_name="First Name", max_length=255)
    lastname = models.CharField(verbose_name="Last Name", max_length=255)
    about = models.TextField(verbose_name="About Me")
    gender = models.CharField(verbose_name="Gender", choices=GENDER_CHOICE, default='SELECT GENDER', max_length=10)
    employ_id = models.CharField(verbose_name="Employee ID", max_length=100)
    location = models.CharField(verbose_name="Location Address", max_length=255)
    registerd_date = models.DateField(verbose_name="Registered Date", auto_now_add=True)
    
    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)


class Supplier(models.Model):
    GENDER_CHOICE = [
        ('SELECT GENDER', ''),
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(verbose_name="First Name", max_length=255)
    lastname = models.CharField(verbose_name="Last Name", max_length=255)
    about = models.TextField(verbose_name="About Me")
    gender = models.CharField(verbose_name="Gender", choices=GENDER_CHOICE, default='SELECT GENDER', max_length=10)
    station_address = models.CharField(verbose_name="Location Address", max_length=255)
    registerd_date = models.DateField(verbose_name="Registered Date", auto_now_add=True)
    
    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)


class MedecineType(models.Model):
    type_name = models.CharField(verbose_name="Medecine Type", max_length=255)
    registerd_date = models.DateField(verbose_name="Registered Date", auto_now_add=True)
    created_by = models.ForeignKey(Pharmacist, verbose_name="Pharmacist", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.type_name


class MedecineCategory(models.Model):
    medecine_type = models.ForeignKey(MedecineType, verbose_name="Medecine Type", on_delete=models.CASCADE)
    category_name = models.CharField(verbose_name="Medecine Category", max_length=255)
    created_date  = models.DateField(verbose_name="Created Date", auto_now_add=True)
    created_by = models.ForeignKey(Pharmacist, verbose_name="Pharmacist", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.category_name
    

class Medecine(models.Model):
    category = models.ForeignKey(MedecineCategory, verbose_name="Medecine Category", on_delete=models.CASCADE)
    batch_no = models.CharField(verbose_name="Batch Number", max_length=255)
    medecine_name = models.CharField(verbose_name="Medecine Name", max_length=255)
    specification = models.TextField(verbose_name="Specification")
    measurement = models.CharField(verbose_name="Measurement", max_length=50)
    remarks = models.TextField(verbose_name="Remarks",)
    price  = models.FloatField(verbose_name="Price",)
    retail_price  = models.FloatField(verbose_name="Retail Price", max_length=255)
    quantity_on_hand  = models.IntegerField(verbose_name="Quantity on Hand",)
    expiry_date  = models.DateField(verbose_name="Expiry Date")
    created_by = models.ForeignKey(Pharmacist, verbose_name="Pharmacist", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.medecine_name
    

class PharmacyRequest(models.Model):
    STATUS_CHOICE = [
        ('Pending', 'STATUS PENDING'),
        ('Completed','STATUS COMPLETED'),
        ('Cancelled','STATUS CANCELLED' ),
    ]
    request_no = models.CharField(verbose_name="Request No", max_length=255, unique=True)
    supplier = models.ForeignKey(Supplier, verbose_name="Supplier", on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medecine, verbose_name="Medecine", on_delete=models.CASCADE)
    quantity  = models.IntegerField(verbose_name="Quantity",)
    status = models.CharField(verbose_name="Request Status", choices=STATUS_CHOICE, max_length=50, default='Pending')
    date_processed = models.DateField(verbose_name="Date Processed", auto_now_add=True)
    created_by = models.ForeignKey(Pharmacist, verbose_name="Pharmacist", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.request_no
    

class ReceivedMedecine(models.Model):
    supplier = models.ForeignKey(Supplier, verbose_name="Supplier", on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medecine, verbose_name="Medecine", on_delete=models.CASCADE)
    reference_no = models.CharField(verbose_name="Reference No", max_length=255)
    quantity  = models.IntegerField(verbose_name="Quantity")
    price  = models.FloatField(verbose_name="Price",)
    amount  = models.FloatField(verbose_name="Amount",)
    status = models.BooleanField(verbose_name="Recieved")
    date_processed = models.DateField(verbose_name="Date Processed", auto_now_add=True)
    created_by = models.ForeignKey(Pharmacist, verbose_name="Pharmacist", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.reference_no


class StockOut(models.Model):
    transaction_no = models.CharField(verbose_name="Transaction No", max_length=255)
    medicine = models.ForeignKey(Medecine, verbose_name="Medecine", on_delete=models.CASCADE)
    quantity  = models.IntegerField(verbose_name="Quantity",)
    price  = models.FloatField(verbose_name="Price",)
    amount  = models.FloatField(verbose_name="Amount",)
    reference_no = models.CharField(verbose_name="Reference No", max_length=255)
    date_processed = models.DateField(verbose_name="Date Processed", auto_now_add=True)
    created_by = models.ForeignKey(Pharmacist, verbose_name="Pharmacist", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.transaction_no
    
