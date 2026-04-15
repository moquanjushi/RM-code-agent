@echo off
echo ========================================
echo AI Code Agent - GitHub部署脚本
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

REM 检查远程仓库配置
echo 🔍 检查远程仓库配置...
git remote -v
if %errorlevel% neq 0 (
    echo ❌ 远程仓库配置检查失败
    pause
    exit /b 1
)

echo.
echo 📦 开始部署到GitHub...
echo.

REM 拉取远程更改（如果有）
echo 🔄 拉取远程更改...
git pull origin main --allow-unrelated-histories
if %errorlevel% neq 0 (
    echo ⚠ 拉取远程更改失败，可能是首次推送
)

echo.

REM 推送代码到GitHub
echo 🚀 推送代码到GitHub...
echo 这可能需要一些时间，请耐心等待...
echo.

git push -u origin main
if %errorlevel% neq 0 (
    echo ❌ 推送失败
    echo.
    echo 📝 可能的原因：
    echo - 远程仓库不存在或权限不足
    echo - 网络连接问题
    echo - 身份验证失败
    echo.
    echo 💡 解决方案：
    echo 1. 确保GitHub仓库已创建
    echo 2. 检查SSH密钥或Personal Access Token配置
    echo 3. 重新运行 setup_github.bat 配置远程仓库
    pause
    exit /b 1
)

echo.
echo ✅ 代码推送成功！
echo.

REM 创建版本标签
echo 🏷 创建版本标签 v1.4.0...
git tag -a v1.4.0 -m "版本 1.4.0: AI Code Agent with Security Sandbox"
if %errorlevel% neq 0 (
    echo ⚠ 创建标签失败
) else (
    git push origin v1.4.0
    if %errorlevel% neq 0 (
        echo ⚠ 推送标签失败
    ) else (
        echo ✅ 版本标签创建成功
    )
)

echo.
echo ========================================
echo 🎉 部署完成！
echo ========================================
echo.
echo 📊 部署结果：
echo - ✅ 代码已推送到GitHub主分支
echo - ✅ 版本标签 v1.4.0 已创建
echo - 🔄 GitHub Actions工作流将自动运行
echo.
echo 🔗 访问您的GitHub仓库查看：
echo - 代码质量检查结果
echo - 构建状态
echo - 项目文档
echo.
echo 💡 后续操作建议：
echo 1. 在GitHub仓库设置中启用分支保护规则
echo 2. 配置GitHub Pages展示项目文档
echo 3. 设置代码审查流程
echo 4. 配置依赖安全扫描
echo.
pause