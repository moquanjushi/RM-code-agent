@echo off
echo ========================================
echo AI Code Agent - Git仓库初始化脚本
echo ========================================
echo.

REM 检查Git是否安装
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git未安装，请先安装Git
    echo 下载地址: https://git-scm.com/downloads
    pause
    exit /b 1
)

echo ✅ Git已安装
echo.

REM 检查是否已经是Git仓库
if exist .git (
    echo ℹ 当前目录已经是Git仓库
    goto :config_user
)

echo 📦 初始化Git仓库...
git init
if %errorlevel% neq 0 (
    echo ❌ Git初始化失败
    pause
    exit /b 1
)

echo ✅ Git仓库初始化成功
echo.

:config_user
echo 👤 配置Git用户信息...
echo 请输入您的姓名（用于Git提交记录）:
set /p git_name=
echo 请输入您的邮箱（用于Git提交记录）:
set /p git_email=

git config user.name "%git_name%"
git config user.email "%git_email%"

echo ✅ 用户信息配置完成
echo.

REM 添加所有文件到暂存区
echo 📝 添加文件到暂存区...
git add .
if %errorlevel% neq 0 (
    echo ❌ 添加文件失败
    pause
    exit /b 1
)

echo ✅ 文件添加成功
echo.

REM 创建初始提交
echo 💾 创建初始提交...
git commit -m "feat: 初始化AI Code Agent项目\n\n- 添加核心ReAct智能体实现\n- 集成多模型支持（DeepSeek/OpenAI/Claude/Gemini）\n- 实现MCP协议工具扩展\n- 添加Docker安全沙盒\n- 提供Web界面和CLI界面"
if %errorlevel% neq 0 (
    echo ❌ 提交失败
    pause
    exit /b 1
)

echo ✅ 初始提交创建成功
echo.
echo ========================================
echo 🎉 Git仓库初始化完成！
echo ========================================
echo.
echo 下一步操作：
echo 1. 在GitHub上创建新仓库
echo 2. 运行 setup_github.bat 配置远程仓库
echo 3. 运行 deploy_to_github.bat 部署到GitHub
echo.
pause