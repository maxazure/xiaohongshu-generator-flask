# 小红书图片生成器 Flask 版

这是一个基于Flask的小红书图片生成器应用，让你可以轻松创建小红书风格的图片内容。

## 功能特点

- 支持Markdown格式编辑内容
- 实时预览小红书样式效果
- 分页显示，方便内容排版
- 支持小红书特殊格式（标题、子标题、编号段落等）
- 可导出为图片（小红书风格）

## 快速开始

### 使用Docker

```bash
docker pull maxazure/xiaohongshu-generator-flask
docker run -p 8911:8911 maxazure/xiaohongshu-generator-flask
```

### 本地开发

1. 克隆仓库
```bash
git clone https://github.com/maxazure/xiaohongshu-generator-flask.git
cd xiaohongshu-generator-flask
```

2. 创建虚拟环境并安装依赖
```bash
python -m venv venv
source venv/bin/activate  # Windows使用 venv\Scripts\activate
pip install -r requirements.txt
```

3. 初始化数据库
```bash
python init_db.py
```

4. 启动应用
```bash
python run.py
```

5. 访问 http://localhost:8911 开始使用

## 特殊格式指南

- 主标题：使用 `# 标题文本`
- 子标题：使用 `- 子标题文本 -`
- 编号段落：使用 `01 段落内容` (支持01-99编号)
- 分页：使用 `---` 或 `***` 分隔不同页面

## 技术栈

- Flask
- SQLite / PostgreSQL
- Bootstrap 5
- SimpleMDE (Markdown编辑器)

## 许可证

MIT
