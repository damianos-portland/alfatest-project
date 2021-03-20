from django.db import models
from jsonfield import JSONField
from multiselectfield import MultiSelectField
from django.contrib.admin.widgets import AdminDateWidget








class Dokimi(models.Model):
	name_dokimis = models.CharField(max_length=200, null=True, unique=True)







class Customer(models.Model):
	afm = models.CharField(max_length=200, null=True, unique=True)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	engineer = models.CharField(max_length=200, null=True)
	address = models.CharField(max_length=200, null=True)
	doy = models.CharField(max_length=200, null=True)
	fax = models.CharField(max_length=200, null=True)


	def __str__(self):
		return self.name

class Ergo(models.Model):

	Dokimes = (
					('Dokimi1', 'Dokimi1'),
					('Dokimi2', 'Dokimi2'),
					('Dokimi3', 'Dokimi3'),
					('Dokimi4', 'Dokimi4'),
					('Dokimi5', 'Dokimi5'),
					('Dokimi6', 'Dokimi6'),
					('Dokimi7', 'Dokimi7'),
					('Dokimi8', 'Dokimi8'),

					)
	Eidos = (
				('Mpeto', 'Mpeto'),
				('Sidero', 'Sidero'),
				('Adrani', 'Adrani'),
				)


	eidos = models.CharField(max_length=200, null=True, choices=Eidos)

	dokimi = models.ManyToManyField(Dokimi)

	def __str__(self):
			return self.eidos


class Trial(models.Model):
	STATUS = (
				('Pending', 'Pending'),
				('Out for delivery', 'Out for delivery'),
				('Delivered', 'Delivered'),
				)

	name = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS, default='Pending')
	yliko = models.ForeignKey(Ergo, null=True, on_delete= models.SET_NULL)

	def __str__(self):
		return self.name


# class Tag(models.Model):
# 	name = models.CharField(max_length=200, null=True)
#
# 	def __str__(self):
# 		return self.name

# class Product(models.Model):
# 	CATEGORY = (
# 			('Indoor', 'Indoor'),
# 			('Out Door', 'Out Door'),
# 			)
#
# 	name = models.CharField(max_length=200, null=True)
# 	price = models.FloatField(null=True)
# 	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
# 	description = models.CharField(max_length=200, null=True, blank=True)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)
# 	tags = models.ManyToManyField(Tag)
#
# 	def __str__(self):
# 		return self.name

# class Order(models.Model):
# 	STATUS = (
# 			('Pending', 'Pending'),
# 			('Out for delivery', 'Out for delivery'),
# 			('Delivered', 'Delivered'),
# 			)
#
# 	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
# 	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
# 	date_created = models.DateTimeField(auto_now_add=True, null=True)
# 	status = models.CharField(max_length=200, null=True, choices=STATUS)
# 	note = models.CharField(max_length=1000, null=True)
#
# 	def __str__(self):
# 		return self.product.name



class Application(models.Model):

	MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))

	TESTS=(
	    ('ΥΓΕΙΑ', 'ΥΓΕΙΑ'),
	    ('ΠΛΑΣΤΙΚΟΤΗΤΑ', 'ΠΛΑΣΤΙΚΟΤΗΤΑ'),
	    ('ΕΙΣΚΟΜΙΣΗ ΜΗΤΡΩΝ', 'ΕΙΣΚΟΜΙΣΗ ΜΗΤΡΩΝ'),
		('ΘΡΑΥΣΗ ΔΟΚΙΜΙΩΝ', 'ΘΡΑΥΣΗ ΔΟΚΙΜΙΩΝ')
		)

	STATUS=(
		('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
		)




    #customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	protocol_number = models.IntegerField(unique=True)
	ergo = models.ForeignKey(Ergo, null=True, on_delete= models.SET_NULL)
	# name = models.CharField(max_length=264,unique=True)
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	# address = models.CharField(max_length=264)
	date = models.DateField(auto_now=True)
	# tests = models.CharField(max_length=200, null=True, choices=TESTS)
	status = models.CharField(max_length=200, null=True, choices=STATUS, default='Pending')
	# status_list = MultiSelectField(choices=MY_CHOICES,null=True)
	trials = models.ManyToManyField(Trial,null=True)

	class Meta:
		ordering = ['-date']




	def __str__(self):
		return str(self.protocol_number)
