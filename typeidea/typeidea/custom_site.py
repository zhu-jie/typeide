from django.contrib.admin import AdminSite

class CustomeSite(AdminSite):
    site_header = 'Zhu\'s 博客'
    site_title = 'Zhu\'s 博客管理后台'
    index_title = '首页'

custom_site = CustomeSite(name='cus_admin')