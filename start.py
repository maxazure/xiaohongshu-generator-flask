"""
应用启动脚本
初始化数据库并启动Flask应用
"""
import os
import sys
from pathlib import Path

# 确保实例目录存在
instance_path = Path("instance")
instance_path.mkdir(exist_ok=True)

# 初始化数据库
print("正在初始化数据库...")
import init_db
init_db.init_db()

# 启动Flask应用
print("正在启动应用...")
from run import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
