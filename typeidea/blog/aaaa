from django.contrib import admin
from django.contrib.admin.decorators import register
from django.db import models
from django.urls import reverse
from django.utils.html import format_html 
# Register your models here.
from .models import Post, Category, Tag
from .adminforms import PostAdminForm
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site

class PostInline(admin.StackedInline):
    fields = ('title', 'desc')
    extra = 1 # 控制额外多几个
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count',)
    fields = ('name', 'status', 'is_nav')
    inlines = [PostInline,]

    def post_count(self, obj):
        return obj.post_set.count()
        
    post_count.short_description = '文章数量'
    
@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

class CategoryOwnerFilter(admin.SimpleListFilter):
    """
    自定义过滤器，只展示当前用户分类
    """
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        """
        返回展示的内容和查询用的ID
        """
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        """
        根据URL Query的内容返回列表页数据，比如如果URL最后的Query是?owner_category=1，那么这里拿到的self.value()就是1，此时就会根据1来过去Query
        """
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset

@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    # 用来配置列表页面展示
    list_display = [
        'title', 'category', 'status','owner',
        'created_time', 'operator'
    ]
    # 用来配置哪些字段可作为链接，点击进入编辑界面,留空则默认是list_display的第一个值
    list_display_links = []
    # 页面过滤，表示可以通过category进行过滤
    # list_filter = ['category']
    list_filter = [CategoryOwnerFilter,]
    # 表示可以用于搜索的字段
    search_fields = ['title', 'category__name']
    # 动作相关的配置是否展示在顶部
    actions_on_top = True
    # 动作相关的配置是否展示在底部
    actions_on_bottom = False
    # 保存，编辑，编辑并新建按钮是否在顶部
    save_on_top = False
    # exclude = ('owner',)
    # fields = (
    #     ('category', 'title'),
    #     'desc',
    #     'status',
    #     'content',
    #     'tag',
    # )
    fieldsets = (
        ('基础配置', {
            # 'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                'status',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content',
            ),
        }),
        ('额外信息', {
            'classes': ('wide',), # collapse隐藏 wide展示
            'fields': ('tag',),
        })
    )
    # 多对多字段展示的配置
    filter_horizontal = ('tag',) # 横向展示
    # filter_vertical = ('tag',) # 竖向展示
    def operator(self, obj):
        "用于在list_display中展示自定义字段"
        return format_html(
            '<a style="color:red" href="{}">编辑</a>',
            # reverse('admin:blog_post_change', args=(obj.id,)) # 使用系统自带admin时
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'
    # class Media:
    #     """
    #     定义额外样式
    #     """
    #     css = {
    #         'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
    #     }
    #     js = ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js",)
