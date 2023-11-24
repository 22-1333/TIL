from django.db import models

# Create your models here.
class Product(models.Model):
    dcls_month = models.TextField()
    fin_co_no = models.TextField()
    fin_prdt_cd = models.TextField()
    kor_co_nm = models.TextField(null=True, blank=True)
    fin_prdt_nm = models.TextField(null=True, blank=True)
    join_way = models.TextField(null=True, blank=True)
    mtrt_int = models.TextField(null=True, blank=True)
    spcl_cnd = models.TextField(null=True, blank=True)
    join_deny = models.IntegerField(null=True, blank=True)  #  1: 제한없음 / 2: 서민전용 / 3: 일부제한
    join_member = models.TextField(null=True, blank=True)
    etc_note = models.TextField(null=True, blank=True)
    max_limit = models.IntegerField(null=True, blank=True)
    dcls_strt_day = models.TextField(null=True, blank=True)
    dcls_end_day = models.TextField(null=True, blank=True)
    fin_co_subm_day = models.TextField(null=True, blank=True)
    product_type = models.IntegerField(null=True, blank=True)  # 0: 예금 / 1: 적금


class Option(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='options')
    intr_rate_type = models.TextField()
    save_trm = models.TextField()
    intr_rate = models.FloatField(null=True, blank=True)
    intr_rate2 = models.FloatField(null=True, blank=True)
