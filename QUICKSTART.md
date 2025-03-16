# 小红书图片生成器 - 快速启动指南

## 前提条件

确保您已经安装了以下软件：

- Python 3.8 或更高版本（推荐使用Python 3.11或3.12以避免兼容性问题）
- pip (Python包管理器)
- git (可选，用于克隆仓库)

## 快速启动步骤

1. **打开终端或命令提示符**

2. **导航到项目目录**
   ```
   cd /Users/maxazure/projects/xiaohongshu-generator-flask
   ```

3. **创建虚拟环境**
   ```
   python -m venv venv
   ```

4. **激活虚拟环境**
   - 在macOS/Linux上:
     ```
     source venv/bin/activate
     ```
   - 在Windows上:
     ```
     venv\Scripts\activate
     ```

5. **安装依赖**
   ```
   pip install -r requirements.txt
   ```

6. **初始化数据库**
   ```
   python init_db.py
   ```

7. **启动应用**
   ```
   python run.py
   ```

8. **访问应用**
   - 打开浏览器
   - 访问 http://127.0.0.1:8911/

## 使用技巧

1. **创建分页内容**
   - 在Markdown编辑器中使用 `---` 作为分页符
   - 每个分页符会在预览时将内容分成单独的页面
   - 示例：
     ```markdown
     # 第一页内容
     这是第一页的文字

     ---

     # 第二页内容
     这是第二页的文字
     ```

2. **预览界面操作**
   - 点击左侧区域：上一页/上一篇文章
   - 点击右侧区域：下一页/下一篇文章
   - 使用键盘左右箭头键：翻页浏览
   - 滑动操作（触摸屏）：左右滑动切换页面
   - 底部小圆点：直接点击切换到指定页面

3. **示例模板**
   项目中包含一个示例模板文件 `sample_post.md`，您可以参考它来创建格式良好的分页帖子。

## 常见问题解决

1. **问题: 依赖安装失败**
   - 确保您的pip是最新版本: `pip install --upgrade pip`
   - 尝试单独安装失败的依赖: `pip install <package_name>`
   - 如果使用Python 3.13遇到SQLAlchemy兼容性问题，请切换到Python 3.11或3.12

2. **问题: 数据库初始化错误**
   - 确保您有SQLite的写入权限
   - 如果数据库文件已存在: `rm instance/app.db` 然后重新运行 `python init_db.py`

3. **问题: 应用无法启动**
   - 检查是否有其他应用占用了8911端口
   - 查看错误日志，解决相应问题

4. **问题: 预览功能不工作**
   - 确保您的浏览器启用了JavaScript
   - 检查浏览器控制台是否有错误

5. **问题: 保存帖子时出现错误**
   - 确保标题不为空
   - 确保内容不为空

## 其他资源

- 完整文档请参考 `README.md` 和 `README_zh.md`
- 有关Markdown语法的帮助: [Markdown指南](https://www.markdownguide.org/basic-syntax/)
- Flask文档: [Flask官方文档](https://flask.palletsprojects.com/)
