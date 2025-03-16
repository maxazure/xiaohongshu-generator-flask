# 小红书图片生成器 - Flask 版本

这是一个基于Flask的Web应用，用于创建、编辑和预览小红书风格的帖子。用户可以使用Markdown编写内容，并在模拟手机界面中预览效果。

## 功能特点

- 创建、编辑、删除和查看帖子
- 友好的Markdown编辑体验
- 模拟手机屏幕的预览界面
- 支持左右点击/滑动翻页
- 使用Markdown中的水平线(`---`或`<hr>`)作为分页符
- 预览界面按照自定义模板显示，支持多页浏览
- 支持键盘方向键翻页和触摸屏滑动操作

## 技术栈

- **后端**: Python 3.8+, Flask, SQLite, SQLAlchemy
- **前端**: HTML/CSS/JavaScript, Bootstrap 5, SimpleMDE, jQuery
- **其他**: Flask-WTF, Python-Markdown, Flask-Migrate

## 安装步骤

1. 克隆仓库
   ```
   git clone <repository-url>
   cd xiaohongshu-generator-flask
   ```

2. 创建并激活虚拟环境
   ```
   python -m venv venv
   source venv/bin/activate  # 在Windows上使用 venv\Scripts\activate
   ```

3. 安装依赖
   ```
   pip install -r requirements.txt
   ```

4. 初始化数据库
   ```
   python init_db.py
   ```

5. 运行应用
   ```
   python run.py
   ```

6. 访问应用
   在浏览器中打开 http://127.0.0.1:5000/

## 项目结构

```
/xiaohongshu-generator-flask/
├── app/                      # 应用主目录
│   ├── __init__.py           # Flask应用初始化
│   ├── config.py             # 配置文件
│   ├── models/               # 数据模型
│   ├── routes/               # 路由
│   ├── forms/                # 表单
│   ├── static/               # 静态文件
│   └── templates/            # 模板
├── migrations/               # 数据库迁移文件
├── .env                      # 环境变量
├── init_db.py                # 数据库初始化脚本
├── run.py                    # 应用入口
├── requirements.txt          # 依赖列表
└── README.md                 # 项目说明
```

## 预览功能详情

预览功能是本应用的核心特色，具有以下特点：

1. **自定义风格预览**：预览界面采用精美的设计模板，而非原始小红书界面样式
2. **分页显示**：使用Markdown中的水平线(`---`或`<hr>`)作为分页符，内容按页显示
3. **导航功能**：
   - 点击屏幕左侧：上一页/上一篇文章
   - 点击屏幕右侧：下一页/下一篇文章
   - 使用键盘左右箭头：翻页浏览
   - 支持触摸屏滑动操作
4. **页码指示器**：底部小圆点表示当前页码和总页数

## 使用说明

1. **创建帖子**
   - 点击导航栏中的"创建帖子"按钮
   - 填写标题和内容（使用Markdown格式）
   - 使用`---`作为分页符来创建多页内容
   - 点击"保存"按钮

2. **编辑帖子**
   - 在帖子列表中点击对应帖子的"编辑"按钮
   - 修改标题和内容
   - 点击"保存"按钮

3. **预览帖子**
   - 在帖子列表或查看页面中点击"预览"按钮
   - 在模拟手机界面中查看帖子效果
   - 点击左侧区域查看上一页或上一篇，点击右侧区域查看下一页或下一篇
   - 使用键盘左右箭头键也可以翻页

4. **删除帖子**
   - 在帖子列表中点击对应帖子的"删除"按钮
   - 确认删除操作

## Markdown 支持

应用支持常用的 Markdown 语法，包括：

- 标题（# 一级标题，## 二级标题，等）
- 加粗（**文本**）和斜体（*文本*）
- 列表（有序和无序）
- 链接（[文本](URL)）
- 图片（![描述](图片URL)）
- 引用（> 引用文本）
- 代码块（```语言 代码```）
- 水平线（`---`，用作分页符）

## 注意事项

- 在使用Python 3.13以上版本时，可能会遇到SQLAlchemy兼容性问题，建议使用Python 3.11或3.12
- 对于复杂的帖子内容，建议使用较新版本的浏览器以获得最佳体验

## 贡献指南

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 许可证

MIT
