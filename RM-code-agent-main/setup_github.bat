@echo off
echo ========================================
echo AI Code Agent - GitHub仓库配置脚本
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

REM 检查是否是Git仓库
if not exist .git (
    echo ❌ 当前目录不是Git仓库
    echo 请先运行 init_git_repo.bat 初始化Git仓库
    pause
    exit /b 1
)

echo 📋 当前Git仓库状态:
git status
echo.

REM 配置GitHub远程仓库
echo 🌐 配置GitHub远程仓库...
echo 请输入GitHub仓库URL（格式: https://github.com/用户名/仓库名.git）:
set /p github_url=

if "%github_url%"=="" (
    echo ❌ 请输入有效的GitHub仓库URL
    pause
    exit /b 1
)

echo 🔗 添加远程仓库...
git remote add origin %github_url%
if %errorlevel% neq 0 (
    echo ❌ 添加远程仓库失败
    echo 请检查URL格式是否正确
    pause
    exit /b 1
)

echo ✅ 远程仓库配置成功
echo.

REM 验证远程连接
echo 🔍 验证远程连接...
git remote -v
echo.

REM 设置默认分支
echo 🌿 设置默认分支...
git branch -M main
if %errorlevel% neq 0 (
    echo ⚠ 设置分支名称失败，可能已经是main分支
)

echo ✅ 分支设置完成
echo.

REM 配置推送设置
echo ⚙ 配置推送设置...
git config push.default simple
echo.

echo ========================================
echo 🎉 GitHub仓库配置完成！
echo ========================================
echo.
echo 下一步操作：
echo 1. 确保GitHub仓库已创建且为空
echo 2. 运行 deploy_to_github.bat 部署代码
echo 3. 在GitHub上设置分支保护规则
echo.
echo 📝 重要提醒：
echo - 确保GitHub仓库已创建且为空
echo - 确保您有推送权限
echo - 首次推送可能需要身份验证
echo.
pause