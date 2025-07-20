from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Skill, Achievement, Project, BlogCategory, BlogPost, 
    GalleryCategory, GalleryItem, Testimonial, SocialLink, SiteSettings, TimelineItem
)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'level', 'xp', 'category', 'order']
    list_filter = ['category']
    list_editable = ['level', 'xp', 'order']
    ordering = ['order', 'name']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'xp', 'unlocked', 'order']
    list_filter = ['unlocked']
    list_editable = ['unlocked', 'order']
    ordering = ['order']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'order', 'created_at']
    list_filter = ['featured', 'technologies', 'created_at']
    list_editable = ['featured', 'order']
    search_fields = ['title', 'description']
    prepopulated_fields = {'github_url': ('title',)}
    ordering = ['order', '-created_at']
    
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('technologies')


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'post_count']
    prepopulated_fields = {'slug': ('name',)}
    
    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Posts'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'published', 'read_time', 'created_at']
    list_filter = ['category', 'featured', 'published', 'created_at', 'tags']
    list_editable = ['featured', 'published']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'excerpt')
        }),
        ('Content', {
            'fields': ('content', 'image')
        }),
        ('Meta', {
            'fields': ('tags', 'read_time', 'featured', 'published')
        }),
    )


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'item_count']
    prepopulated_fields = {'slug': ('name',)}
    
    def item_count(self, obj):
        return obj.items.count()
    item_count.short_description = 'Items'


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'created_at']
    list_filter = ['category', 'tags', 'created_at']
    list_editable = ['order']
    search_fields = ['title', 'description']
    ordering = ['order', '-created_at']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'rating', 'featured', 'order']
    list_filter = ['rating', 'featured', 'created_at']
    list_editable = ['featured', 'order']
    search_fields = ['name', 'company', 'text']
    ordering = ['order', '-created_at']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return ['created_at']
        return []


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'icon_name', 'active', 'order']
    list_editable = ['active', 'order']
    ordering = ['order']


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Site Information', {
            'fields': ('site_title', 'site_description')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location', 'resume_url')
        }),
    )
    
    def has_add_permission(self, request):
        # Prevent adding more than one instance
        return not SiteSettings.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the settings
        return False


# Customize admin site
admin.site.site_header = "Ganesh Portfolio Administration"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Portfolio Administration"
admin.site.register(TimelineItem)