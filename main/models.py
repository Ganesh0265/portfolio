from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager
from django.utils import timezone


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField(default=0, help_text="Skill level (0-100)")
    icon = models.CharField(max_length=10, help_text="Emoji icon for the skill")
    xp = models.IntegerField(default=0, help_text="Experience points")
    category = models.CharField(max_length=50, choices=[
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ], default='other')
    order = models.IntegerField(default=0, help_text="Display order")
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.level}%)"


class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name")
    xp = models.IntegerField(default=0)
    unlocked = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'title']
    
    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    detailed_description = RichTextUploadingField(blank=True)
    image = models.ImageField(upload_to='projects/images/')
    video_preview = models.ImageField(upload_to='projects/videos/', blank=True, null=True)
    github_url = models.URLField()
    live_url = models.URLField(blank=True)
    technologies = TaggableManager()
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Blog Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('blog_category', kwargs={'slug': self.slug})


class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    excerpt = models.TextField(max_length=300)
    content = RichTextUploadingField()
    image = models.ImageField(upload_to='blog/images/')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='posts')
    tags = TaggableManager()
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    read_time = models.IntegerField(default=5, help_text="Estimated read time in minutes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'slug': self.slug})


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "Gallery Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name='items')
    tags = TaggableManager()
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='testimonials/')
    text = models.TextField()
    rating = models.IntegerField(default=5, choices=[(i, i) for i in range(1, 6)])
    project = models.CharField(max_length=200, blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.company}"


class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()
    icon_name = models.CharField(max_length=50, help_text="Lucide icon name")
    order = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class SiteSettings(models.Model):
    site_title = models.CharField(max_length=200, default="Ganesh - Python Developer")
    site_description = models.TextField(default="Passionate Python Developer specializing in Django web applications")
    hero_title = models.CharField(max_length=200, default="Hi, I'm Ganesh — a passionate Python Developer")
    hero_subtitle = models.TextField(default="Building innovative web solutions with clean code and creative problem-solving.")
    email = models.EmailField(default="ganesh@example.com")
    phone = models.CharField(max_length=20, default="+91 9876543210")
    location = models.CharField(max_length=100, default="Mumbai, India")
    resume_url = models.URLField(blank=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return "Site Settings"
    
    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteSettings.objects.exists():
            raise ValueError('There can be only one SiteSettings instance')
        return super().save(*args, **kwargs)


class TimelineItem(models.Model):
    TIMELINE_TYPE_CHOICES = [
        ('study', 'Study'),
        ('training', 'Training'),
        ('work', 'Work'),
    ]
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=TIMELINE_TYPE_CHOICES)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0, help_text="Display order")

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.title} at {self.institution} ({self.get_type_display()})"