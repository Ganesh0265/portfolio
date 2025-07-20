from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import (
    Skill, Achievement, Project, BlogPost, BlogCategory, 
    GalleryItem, GalleryCategory, Testimonial, SocialLink, SiteSettings, TimelineItem
)


def get_site_settings():
    """Get or create site settings"""
    settings, created = SiteSettings.objects.get_or_create(
        pk=1,
        defaults={
            'site_title': 'Ganesh - Python Developer',
            'site_description': 'Passionate Python Developer specializing in Django web applications',
            'hero_title': "Hi, I'm Ganesh — a passionate Python Developer",
            'hero_subtitle': 'Building innovative web solutions with clean code and creative problem-solving.',
        }
    )
    return settings


def home(request):
    """Home page view"""
    context = {
        'settings': get_site_settings(),
        'skills': Skill.objects.all()[:8],  # Top 8 skills for navbar
        'featured_projects': Project.objects.filter(featured=True)[:3],
        'featured_blogs': BlogPost.objects.filter(featured=True, published=True)[:2],
        'testimonials': Testimonial.objects.filter(featured=True)[:6],
        'social_links': SocialLink.objects.filter(active=True),
    }
    return render(request, 'main/home.html', context)


def projects(request):
    """Projects page view"""
    projects_list = Project.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        projects_list = projects_list.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(technologies__name__icontains=search_query)
        ).distinct()
    
    # Technology filter
    tech_filter = request.GET.get('tech')
    if tech_filter:
        projects_list = projects_list.filter(technologies__name__icontains=tech_filter)
    
    # Pagination
    paginator = Paginator(projects_list, 6)
    page_number = request.GET.get('page')
    projects_page = paginator.get_page(page_number)
    
    # Get all technologies for filter
    all_technologies = set()
    for project in Project.objects.all():
        for tag in project.technologies.all():
            all_technologies.add(tag.name)
    
    context = {
        'settings': get_site_settings(),
        'projects': projects_page,
        'all_technologies': sorted(all_technologies),
        'search_query': search_query,
        'tech_filter': tech_filter,
        'social_links': SocialLink.objects.filter(active=True),
        'skills': Skill.objects.all(),
    }
    return render(request, 'main/projects.html', context)


def project_detail(request, pk):
    """Project detail view"""
    project = get_object_or_404(Project, pk=pk)
    related_projects = Project.objects.exclude(pk=pk)[:3]
    
    context = {
        'settings': get_site_settings(),
        'project': project,
        'related_projects': related_projects,
        'social_links': SocialLink.objects.filter(active=True),
    }
    return render(request, 'main/project_detail.html', context)


def about(request):
    """About page view"""
    context = {
        'settings': get_site_settings(),
        'skills': Skill.objects.all(),
        'achievements': Achievement.objects.all(),
        'social_links': SocialLink.objects.filter(active=True),
        'timeline_items': TimelineItem.objects.all(),
    }
    return render(request, 'main/about.html', context)


def blogs(request):
    """Blog listing view"""
    posts_list = BlogPost.objects.filter(published=True)
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        posts_list = posts_list.filter(category__slug=category_slug)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        posts_list = posts_list.filter(
            Q(title__icontains=search_query) | 
            Q(excerpt__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(tags__name__icontains=search_query)
        ).distinct()
    
    # Pagination
    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    posts_page = paginator.get_page(page_number)
    
    context = {
        'settings': get_site_settings(),
        'posts': posts_page,
        'featured_posts': BlogPost.objects.filter(featured=True, published=True)[:2],
        'categories': BlogCategory.objects.all(),
        'search_query': search_query,
        'category_slug': category_slug,
        'social_links': SocialLink.objects.filter(active=True),
        'skills': Skill.objects.all(),
    }
    return render(request, 'main/blogs.html', context)


def blog_detail(request, slug):
    """Blog detail view"""
    post = get_object_or_404(BlogPost, slug=slug, published=True)
    related_posts = BlogPost.objects.filter(
        category=post.category, published=True
    ).exclude(pk=post.pk)[:3]
    
    context = {
        'settings': get_site_settings(),
        'post': post,
        'related_posts': related_posts,
        'social_links': SocialLink.objects.filter(active=True),
    }
    return render(request, 'main/blog_detail.html', context)


def blog_category(request, slug):
    """Blog category view"""
    category = get_object_or_404(BlogCategory, slug=slug)
    posts_list = BlogPost.objects.filter(category=category, published=True)
    
    # Pagination
    paginator = Paginator(posts_list, 6)
    page_number = request.GET.get('page')
    posts_page = paginator.get_page(page_number)
    
    context = {
        'settings': get_site_settings(),
        'category': category,
        'posts': posts_page,
        'social_links': SocialLink.objects.filter(active=True),
    }
    return render(request, 'main/blog_category.html', context)


def gallery(request):
    """Gallery view"""
    items_list = GalleryItem.objects.all()
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        items_list = items_list.filter(category__slug=category_slug)
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        items_list = items_list.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(tags__name__icontains=search_query)
        ).distinct()
    
    # Pagination
    paginator = Paginator(items_list, 12)
    page_number = request.GET.get('page')
    items_page = paginator.get_page(page_number)
    
    context = {
        'settings': get_site_settings(),
        'items': items_page,
        'categories': GalleryCategory.objects.all(),
        'search_query': search_query,
        'category_slug': category_slug,
        'social_links': SocialLink.objects.filter(active=True),
        'skills': Skill.objects.all(),
    }
    return render(request, 'main/gallery.html', context)


def testimonials(request):
    """Testimonials view"""
    testimonials_list = Testimonial.objects.all()
    
    context = {
        'settings': get_site_settings(),
        'testimonials': testimonials_list,
        'social_links': SocialLink.objects.filter(active=True),
    }
    return render(request, 'main/testimonials.html', context)