# GitHub 部署指南

本文档提供将 AI Code Agent 项目部署到 GitHub 的完整指南。

## 🚀 快速部署

### 前提条件
- Git 已安装
- GitHub 账户
- 项目代码已准备就绪

### 三步部署流程

1. **初始化 Git 仓库**
   ```bash
   # 运行初始化脚本
   init_git_repo.bat
   ```

2. **配置 GitHub 仓库**
   ```bash
   # 运行配置脚本
   setup_github.bat
   ```

3. **部署到 GitHub**
   ```bash
   # 运行部署脚本
   deploy_to_github.bat
   ```

## 📋 详细部署步骤

### 步骤 1: 准备 GitHub 仓库

1. **创建 GitHub 仓库**
   - 访问 https://github.com/new
   - 输入仓库名称（如：rm-code-agent）
   - 选择公开或私有
   - **不要**初始化 README、.gitignore 或 LICENSE
   - 点击 "Create repository"

2. **获取仓库 URL**
   - 复制仓库的 HTTPS 或 SSH URL
   - 格式：`https://github.com/用户名/仓库名.git`

### 步骤 2: 本地 Git 配置

1. **运行初始化脚本**
   ```bash
   # 双击运行或命令行执行
   init_git_repo.bat
   ```

2. **输入用户信息**
   - 姓名（用于提交记录）
   - 邮箱（用于提交记录）

### 步骤 3: 连接 GitHub

1. **运行配置脚本**
   ```bash
   setup_github.bat
   ```

2. **输入 GitHub 仓库 URL**
   - 粘贴步骤 1 中复制的 URL

### 步骤 4: 部署代码

1. **运行部署脚本**
   ```bash
   deploy_to_github.bat
   ```

2. **身份验证**
   - 首次推送可能需要输入 GitHub 用户名和密码
   - 建议使用 Personal Access Token

## 🔑 身份验证配置

### 使用 Personal Access Token

1. **生成 Token**
   - 访问 GitHub Settings → Developer settings → Personal access tokens
   - 点击 "Generate new token"
   - 选择权限：repo（全选）、workflow
   - 复制生成的 token

2. **配置 Git**
   ```bash
   # 使用 token 作为密码
git config --global credential.helper store
   ```

### 使用 SSH 密钥

1. **生成 SSH 密钥**
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```

2. **添加密钥到 GitHub**
   - 复制公钥：`cat ~/.ssh/id_ed25519.pub`
   - 添加到 GitHub Settings → SSH and GPG keys

## ⚙️ GitHub 仓库设置

### 分支保护规则

1. **启用分支保护**
   - 仓库 Settings → Branches → Add branch protection rule
   - 分支名称模式：main
   - 启用选项：
     - Require pull request reviews before merging
     - Require status checks to pass before merging
     - Require conversation resolution before merging

2. **配置状态检查**
   - 选择需要通过的检查：
     - Python CI/CD
     - Frontend CI/CD
     - Security scan

### GitHub Pages 配置

1. **启用 GitHub Pages**
   - 仓库 Settings → Pages
   - Source：Deploy from a branch
   - Branch：gh-pages，文件夹：/(root)

2. **访问项目文档**
   - 访问：https://用户名.github.io/仓库名

## 🔧 自动化工作流

### 已配置的工作流

1. **Python CI/CD**
   - 代码质量检查（black, flake8, mypy）
   - 单元测试和覆盖率报告
   - 安全扫描
   - 自动构建和发布

2. **Frontend CI/CD**
   - 前端代码检查
   - 类型检查和测试
   - 自动构建和部署到 GitHub Pages

### 工作流触发条件

- **推送代码**：自动运行所有检查
- **Pull Request**：运行测试和检查
- **发布版本**：自动构建和发布包

## 📊 部署验证

### 检查部署状态

1. **GitHub Actions**
   - 访问仓库的 Actions 标签页
   - 确认所有工作流通过

2. **代码质量报告**
   - 检查代码覆盖率
   - 查看安全扫描结果

3. **项目文档**
   - 确认 README 显示正常
   - 测试 GitHub Pages 部署

### 常见问题解决

#### 推送失败
```bash
# 错误：权限被拒绝
# 解决方案：检查身份验证配置

# 错误：远程仓库不存在
# 解决方案：确认仓库 URL 正确
```

#### 工作流失败
```bash
# 错误：依赖安装失败
# 解决方案：检查 requirements.txt 和 package.json

# 错误：测试失败
# 解决方案：修复测试代码
```

## 🎯 最佳实践

### 提交规范
- 使用语义化提交信息
- 保持提交历史清晰
- 定期同步远程仓库

### 分支管理
- 主分支（main）：稳定版本
- 开发分支（develop）：开发中功能
- 功能分支（feature/）：新功能开发

### 版本发布
- 使用语义化版本号
- 创建版本标签
- 编写发布说明

## 📞 技术支持

### 问题报告
- 使用 GitHub Issues 报告问题
- 提供详细的重现步骤
- 包含环境信息和错误日志

### 社区支持
- 查看项目文档
- 参与讨论区
- 联系项目维护者

---

## 🎉 恭喜！

您的 AI Code Agent 项目已成功部署到 GitHub！

下一步建议：
1. 邀请团队成员协作
2. 配置代码审查流程
3. 设置依赖安全扫描
4. 探索 GitHub 高级功能

如有问题，请参考本文档或创建 Issue 寻求帮助。