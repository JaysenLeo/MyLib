# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PackageAuth(models.Model):
    auth_id = models.IntegerField(blank=True, null=True)
    p_token = models.CharField(max_length=255, blank=True, null=True)
    p_username = models.CharField(max_length=25, blank=True, null=True)
    p_password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_auth'


class PackageMain(models.Model):
    main_id = models.IntegerField(primary_key=True)
    p_name = models.CharField(max_length=255, blank=True, null=True)
    p_version = models.CharField(max_length=30, blank=True, null=True)
    p_category = models.CharField(max_length=255, blank=True, null=True)
    p_local_downloads = models.CharField(max_length=255, blank=True, null=True)
    p_remote_downloads = models.CharField(max_length=255, blank=True, null=True)
    p_remote_down_count = models.CharField(max_length=255, blank=True, null=True)
    p_local_down_count = models.CharField(max_length=255, blank=True, null=True)
    p_create_time = models.CharField(max_length=255, blank=True, null=True)
    p_size = models.CharField(max_length=255, blank=True, null=True)
    p_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_main'
