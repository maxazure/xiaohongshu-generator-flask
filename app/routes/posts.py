from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify, abort
from app import db
from app.models.post import Post
from app.forms.post_form import PostForm
import markdown
import re

posts_bp = Blueprint('posts', __name__)

def process_xiaohongshu_format(html):
    """Process HTML to match xiaohongshu style"""
    # 处理子标题，如「- TITLE -」类型的标题
    html = re.sub(r'<p>\s*-\s*([^-]+)\s*-\s*</p>', 
        r'<div class="subtitle-container"><div class="subtitle-box">\1</div></div>', html)
    
    # 处理数字前缀，如「01」开头的段落
    html = re.sub(r'<p>\s*(0\d|\d\d)\s+([^<]+)</p>', 
        r'<p class="with-number"><span class="number-circle">\1</span><span>\2</span></p>', html)
    
    # 在各段落间添加分隔线
    html = re.sub(r'</p>\s*<p class="with-number">', r'</p><div class="content-line"></div><p class="with-number">', html)
    
    return html

@posts_bp.route('/')
def index():
    """Redirect to posts list."""
    return redirect(url_for('posts.list_posts'))

@posts_bp.route('/posts')
def list_posts():
    """Display all posts."""
    page = request.args.get('page', 1, type=int)
    per_page = 10
    posts = Post.query.order_by(Post.created_at.desc()).paginate(page=page, per_page=per_page)
    return render_template('posts/index.html', posts=posts)

@posts_bp.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    """Create a new post."""
    form = PostForm()
    if form.validate_on_submit():
        # 获取表单数据
        title = form.title.data
        content = form.content.data
        
        # 手动验证内容不为空
        if not content or not content.strip():
            flash('请输入内容', 'danger')
            return render_template('posts/new.html', form=form)
        
        # 创建新的Post对象
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        
        flash('帖子创建成功!', 'success')
        return redirect(url_for('posts.show_post', id=post.id))
    return render_template('posts/new.html', form=form)

@posts_bp.route('/posts/<int:id>')
def show_post(id):
    """Show a single post."""
    post = Post.query.get_or_404(id)
    content_html = markdown.markdown(
        post.content,
        extensions=['tables', 'fenced_code', 'codehilite']
    )
    return render_template('posts/show.html', post=post, content_html=content_html)

@posts_bp.route('/posts/<int:id>/edit', methods=['GET', 'POST'])
def edit_post(id):
    """Edit an existing post."""
    post = Post.query.get_or_404(id)
    form = PostForm(obj=post)
    
    if form.validate_on_submit():
        # 获取表单数据
        title = form.title.data
        content = form.content.data
        
        # 手动验证内容不为空
        if not content or not content.strip():
            flash('请输入内容', 'danger')
            return render_template('posts/edit.html', form=form, post=post)
        
        # 更新帖子
        post.title = title
        post.content = content
        db.session.commit()
        
        flash('帖子更新成功!', 'success')
        return redirect(url_for('posts.show_post', id=post.id))
    
    return render_template('posts/edit.html', form=form, post=post)

@posts_bp.route('/posts/<int:id>/delete', methods=['POST'])
def delete_post(id):
    """Delete a post."""
    post = Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    flash('帖子已删除!', 'success')
    return redirect(url_for('posts.list_posts'))

@posts_bp.route('/posts/<int:id>/preview')
def preview_post(id):
    """Preview a post in xiaohongshu style."""
    post = Post.query.get_or_404(id)
    
    # Get previous and next posts for navigation
    prev_post = Post.query.filter(Post.id < id).order_by(Post.id.desc()).first()
    next_post = Post.query.filter(Post.id > id).order_by(Post.id.asc()).first()
    
    # Convert markdown to HTML (preserving hr tags for pagination)
    content_html = markdown.markdown(
        post.content,
        extensions=['tables', 'fenced_code', 'codehilite']
    )
    
    # 处理小红书特殊格式
    content_html = process_xiaohongshu_format(content_html)
    
    return render_template(
        'posts/preview.html',
        post=post,
        content_html=content_html,
        prev_post_id=prev_post.id if prev_post else None,
        next_post_id=next_post.id if next_post else None
    )

@posts_bp.route('/api/posts/<int:id>/render', methods=['POST'])
def render_markdown(id):
    """API endpoint to render markdown content."""
    data = request.get_json()
    if not data or 'content' not in data:
        return jsonify({'error': 'No content provided'}), 400
    
    # 处理内容分页
    # 在这里我们先将Markdown渲染为HTML，然后如果需要可以在前端对HTML进行分页
    content = data['content']
    
    # 将分页符号转换为<hr>标签便于前端处理
    # 注意：这里我们需要特别处理，因为markdown默认将---转换为<hr>
    # 但它不会识别当---单独一行并且前后有空行时的特殊含义
    # 这里我们直接交给markdown库处理，它已经可以处理单行的---或***为<hr>
    
    html = markdown.markdown(
        content,
        extensions=['tables', 'fenced_code', 'codehilite']
    )
    
    # 处理小红书特殊格式
    html = process_xiaohongshu_format(html)
    
    return jsonify({'html': html, 'has_pages': '---' in content or '***' in content})
