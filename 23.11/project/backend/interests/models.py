from django.db import models

# Create your models here.
class Product(models.Model):
    product_type = models.IntegerField()  # 0: 예금 / 1: 적금
    dcls_month = models.CharField()
    fin_co_no = models.CharField()
    fin_prdt_cd = models.CharField()
    kor_co_nm = models.CharField()
    fin_prdt_nm = models.CharField()
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.IntegerField()  #  1: 제한없음 / 2: 서민전용 / 3: 일부제한
    join_member = models.CharField()
    etc_note = models.TextField()
    max_limit = models.IntegerField()
    dcls_strt_day = models.CharField()
    dcls_end_day = models.CharField()
    fin_co_subm_day = models.CharField()
