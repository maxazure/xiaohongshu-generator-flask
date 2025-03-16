"""
使用纯SQLite的数据库初始化脚本
创建数据库表并添加样本数据
"""
import sqlite3
import os
from datetime import datetime

def init_db():
    """初始化SQLite数据库并添加样本数据"""
    # 确保数据库目录存在
    os.makedirs('instance', exist_ok=True)
    
    # 连接数据库
    conn = sqlite3.connect('instance/app.db')
    cursor = conn.cursor()
    
    # 创建帖子表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 检查是否已有数据
    cursor.execute('SELECT COUNT(*) FROM posts')
    count = cursor.fetchone()[0]
    
    if count == 0:
        # 添加一些示例帖子
        sample_posts = [
            {
                'title': '如何制作一杯完美的咖啡',
                'content': """
# 如何制作一杯完美的咖啡

每天早晨，一杯香气四溢的咖啡是开启美好一天的仪式。今天我来分享如何制作一杯完美的手冲咖啡！

## 你需要准备

- 新鲜烘焙的咖啡豆
- 磨豆机
- 手冲壶
- 滤杯与滤纸
- 电子秤
- 计时器
- 热水（90-92°C）

## 步骤

1. **准备工作**: 将滤纸放入滤杯，用热水润湿并倒掉多余的水
2. **磨豆**: 按照1:15的比例（如15克咖啡豆对应225克水）磨成中细度