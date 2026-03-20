# 使用微软官方提供的包含 Playwright 依赖的镜像作为基础镜像
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装 Python 包（优先复制以利用 Docker 缓存层）
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制代码项目
COPY . .

# 容器启动时默认的运行命令
CMD ["pytest", "-v", "--html=report.html", "--self-contained-html"]