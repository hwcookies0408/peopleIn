from django.db import models


# class Device(models.Model):
#
#     code = models.CharField(max_length=30, blank=False)
#     total  = models.IntegerField()
#
#     choices = (
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('SOLD', 'Item Sold'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )
#
#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=100, default='No issues')
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return 'Type : {0} Price : {1}'.format(self.code, self.price)
#
# class Laptop(Device):
#     pass
#
# class Desktop(Device):
#     pass
#
# class Mobile(Device):
#     pass
#
# # Create your models here.


class Analysis(models.Model):

    code = models.CharField(max_length=30, blank=False)
    total = models.IntegerField()
    mTotal = models.IntegerField()
    fTotal = models.IntegerField()

    # Gangnamgu = 1
    # Gwangingu = 2
    # Mapogu = 3
    # Seongdonggu = 4
    # Songpagu = 5
    # Yeongdeungpogu = 6

    area_choices = (
        ('광진구', '광진구'),
        ('강남구', '강남구'),
        ('마포구', '마포구'),
        ('성동구', '성동구'),
        ('송파구', '송파구'),
        ('영등포구', '영등포구')
    )

    area = models.CharField(max_length=10, choices=area_choices, default='성동구')


    class Meta:
        abstract = True

    def __str__(self):
        return '{0}'.format(self.id)


class People(Analysis):
    pass