"""
数据库初始化脚本
创建数据库表并添加样本数据
"""
import os
import sys
from datetime import datetime
import sqlite3
from pathlib import Path

def init_db():
    """初始化数据库并添加样本数据"""
    # 创建实例目录（如果不存在）
    instance_path = Path("instance")
    instance_path.mkdir(exist_ok=True)
    
    # 连接到SQLite数据库
    db_path = instance_path / "app.db"
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # 创建posts表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(100) NOT NULL,
        content TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 检查是否已有数据
    cursor.execute("SELECT COUNT(*) FROM posts")
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
3. **预热**: 预热杯具
4. **注水**: 
   - 先倒入约30克水进行闷蒸30秒
   - 以画圈的方式慢慢注入剩余的水
   - 保持水位稳定，约2-3分钟完成萃取

![咖啡](https://example.com/coffee.jpg)

> 小贴士：水温、研磨度、注水速度都会影响咖啡的风味，可以根据个人口味调整参数！

今天一起来尝试制作一杯属于自己的完美咖啡吧！☕️
                    """
            },
            {
                'title': '居家办公的5个实用技巧',
                'content': """
# 居家办公的5个实用技巧

这两年居家办公成为很多人的工作方式，今天分享5个提高效率的小技巧，希望对你有所帮助！

## 1. 建立固定工作区域

在家中划分一个专门的工作空间，告诉大脑这里是"工作区"。

- 选择安静、光线充足的位置
- 保持整洁，减少干扰
- 配备舒适的座椅和合适高度的桌子

## 2. 制定工作计划

- 每天列出3-5个重要任务
- 使用番茄工作法：25分钟专注工作，休息5分钟
- 设置清晰的开始和结束时间

## 3. 减少数字干扰

- 工作时关闭社交媒体通知
- 将手机放在视线之外
- 使用应用限制工具

## 4. 保持规律作息

- 按时起床，做好晨间仪式
- 穿着得体（不要整天睡衣）
- 规律饮食和锻炼

## 5. 有效沟通协作

- 定期与团队视频会议
- 使用协作工具保持项目进度透明
- 及时回复邮件和消息

---

找到适合自己的居家办公节奏，工作效率和生活平衡都能兼顾！

#居家办公 #效率提升 #工作技巧
                    """
            },
            {
                'title': '春季穿搭灵感 | 温柔又有气质',
                'content': """
# 春季穿搭灵感 | 温柔又有气质

春天来了，是时候收起厚重的冬装，换上轻盈柔美的春装了！分享几套我最近常穿的春季搭配~

## Look 1: 奶油色系温柔风

- 米色针织开衫
- 白色棉质T恤
- 浅蓝直筒牛仔裤
- 米色帆布鞋
- 配饰: 珍珠耳环

> 温柔的奶油色调搭配经典蓝色牛仔裤，简约又不失温柔感

## Look 2: 浪漫碎花裙装

- 浅绿碎花连衣裙
- 短款牛仔外套
- 白色运动鞋
- 配饰: 简约项链、草编手提包

> 碎花元素是春天的标配，搭配牛仔外套增加层次感

## Look 3: 通勤知性风

- 杏色西装外套
- 白色丝质衬衫
- 黑色九分西装裤
- 裸色尖头平底鞋
- 配饰: 金属细框眼镜、简约手表

> 柔和的杏色让正式的西装也能散发温柔气质

---

春季穿搭小技巧:
1. 注重面料选择，选择棉麻、丝质等轻薄透气的材质
2. 色彩上以柔和的浅色系为主
3. 搭配合适的妆容，淡妆更能突显春日气息

记得保存这篇穿搭灵感，春天做个温柔又有气质的小姐姐吧！

#春季穿搭 #日常搭配 #温柔风
                    """
            }
        ]
        
        # 插入样本数据
        for post in sample_posts:
            cursor.execute(
                "INSERT INTO posts (title, content, created_at, updated_at) VALUES (?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
                (post['title'], post['content'])
            )
        
        # 提交更改
        conn.commit()
        print("数据库初始化完成，已添加样本数据。")
    else:
        print("数据库中已有数据，跳过样本数据添加。")
    
    # 关闭连接
    conn.close()

if __name__ == '__main__':
    init_db()
