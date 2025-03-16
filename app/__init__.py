import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import warnings

# 忽略SQLAlchemy的弃用警告
warnings.filterwarnings('ignore', category=DeprecationWarning)

# Load environment variables from .env file
load_dotenv()

# Initialize SQLAlchemy and Migrate extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    # Load configuration from environment variables
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'connect_args': {'check_same_thread': False}}
    
    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 设置应用上下文
    app.app_context().push()
    
    # Import models to ensure they are registered with SQLAlchemy
    from app.models.post import Post
    
    # Import and register blueprints
    from app.routes.posts import posts_bp
    app.register_blueprint(posts_bp)
    
    # 确保实例目录存在
    if not os.path.exists('instance'):
        os.makedirs('instance')
    
    # 创建所有表
    db.create_all()
    
    return app
