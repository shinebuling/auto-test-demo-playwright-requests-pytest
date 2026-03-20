# 🚀 Enterprise Automated Testing Framework Demo

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Pytest](https://img.shields.io/badge/Pytest-Latest-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-Web_UI-2ea44f)
![Requests](https://img.shields.io/badge/Requests-API-orange)
![Allure](https://img.shields.io/badge/Allure-Report-yellow)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ed)

本项目是一个自动化测试框架脚手架（Demo），包含了 **Web UI 测试**、**RESTful API 测试**、**并发性能测试** 以及配套的 **CI/CD 流水线**。旨在提供一个高可维护性、高扩展性的综合质量保障解决方案。

## 🎯 核心特性 (Features)

- **Web UI 自动化 (Playwright)**
  - 采用 **POM (Page Object Model)** 设计模式，实现页面元素定位、业务操作与断言逻辑的彻底解耦。
  - 依托 `pytest-playwright` 原生 fixture，实现浏览器上下文的自动管理器与无头模式切换。
- **API 接口自动化 (Requests)**
  - 基于 `@pytest.mark.parametrize` 实现 **数据驱动测试 (Data-Driven)**，一份代码多组数据，覆盖正向及边界/异常场景。
  - 全局共用 Session 连接池与统一环境配置 (`conftest.py`)。
- **性能/压力测试 (Locust)**
  - 内置基于 Python 协程的压测模块，支持按权重配比定义读写场景，可实时生成并探索多并发用户模型下的性能拐点。
- **高阶可视化报告 (Allure)**
  - 深度集成 Allure，支持以业务模块划分（Feature/Story/Title），包含精准的执行步骤追踪日志（`@allure.step`）。
- **容器化与持续集成 (Docker & CI/CD)**
  - 提供完整 `Dockerfile`，采用微软官方镜像二次构建，支持无缝一键隔离部署与用例回归。
  - 预设 GitHub Actions 流水线，监听 Push/PR 自动在 Linux 环境（Ubuntu）执行测试流水线并归档报告。

## 📂 目录结构 (Structure)

```text
.
├── Dockerfile                  # Docker 容器化部署脚本
├── pytest.ini                  # Pytest 全局和 Allure 运行参数配置
├── requirements.txt            # Python 依赖清单
├── .github/workflows/          # GitHub Actions CI/CD 流水线配置文件
├── pages/                      # POM 模式下的页面对象业务类
│   └── search_page.py          # 示例：大厂 Web 主页操作层抽离
├── performance_tests/          # 性能/压力测试脚本
│   └── locustfile.py           # 示例：API 高并发读写压测脚本
└── tests/                      # 自动化测试用例核心目录
    ├── conftest.py             # 核心 fixture、请求全局拦截与共享资源池
    ├── test_api.py             # API 接口集成用例 (含异常/边界/数据驱动)
    └── test_web_ui.py          # Web UI 场景端到端用户流测试
```

## 🛠️ 快速开始 (Quick Start)

### 1. 本地环境部署
```bash
# 解析并安装 Python 核心组件依赖
pip install -r requirements.txt

# 下载并安装 Playwright 自动化所需浏览器内核
playwright install chromium
```

### 2. 执行自动化功能回归测试
```bash
# 执行所有接口与 Web 前端功能测试用例（并生成 Allure 结果数据）
pytest

# 生成并查看动态可视化测试报告（前提需在系统环境配置好 Allure 命令行环境）
allure serve ./allure-results
```

### 3. 各模块独立运行演示
- **单独触发压力容灾测试**
  ```bash
  locust -f performance_tests/locustfile.py
  # 然后通过浏览器访问 http://localhost:8089 设定并发数实时启动压测
  ```
- **基于 Docker 的一键构建与隔离式运行**
  ```bash
  docker build -t auto-test-demo .
  docker run --rm auto-test-demo
  ```
