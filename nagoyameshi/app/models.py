from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('general', '一般ユーザ'),
        ('store', '店舗ユーザ'),
        ('admin', '管理者'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)


class StoreDetail(models.Model):
    # 店舗名
    name = models.CharField(max_length=100)
    # ジャンル
    genre = models.CharField(max_length=100)
    # 都道府県
    prefecture = models.CharField(max_length=10)
    # 都道府県に続く住所
    address = models.CharField(max_length=100)


class GeneralUser(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class StoreUser(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class AdminUser(models.Model):
    name = models.CharField(max_length=100)
    id = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)