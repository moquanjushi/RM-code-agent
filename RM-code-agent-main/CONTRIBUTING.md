# 贡献指南

感谢您对 AI Code Agent 项目的关注！我们欢迎各种形式的贡献，包括但不限于代码改进、文档完善、问题报告等。

## 🚀 快速开始

### 开发环境设置

1. **克隆仓库**
   ```bash
   git clone https://github.com/your-username/rm-code-agent.git
   cd rm-code-agent
   ```

2. **设置Python环境**
   ```bash
   # 创建虚拟环境
   python -m venv venv
   
   # 激活虚拟环境
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   
   # 安装依赖
   pip install -r requirements.txt
   ```

3. **设置前端环境**
   ```bash
   cd frontend
   npm install
   cd ..
   ```

### 运行项目

```bash
# 启动后端服务器
python app.py

# 启动前端开发服务器（新终端）
cd frontend
npm run dev
```

## 📝 贡献流程

### 1. 创建Issue
- 在提交代码前，请先创建相关的Issue
- 描述问题或功能需求
- 讨论实现方案

### 2. 创建分支
```bash
git checkout -b feature/your-feature-name
# 或
git checkout -b fix/issue-number-description
```

**分支命名规范**：
- `feature/`: 新功能
- `fix/`: 问题修复
- `docs/`: 文档改进
- `refactor/`: 代码重构

### 3. 开发代码
- 遵循项目代码规范
- 添加适当的测试
- 更新相关文档

### 4. 提交代码
```bash
# 添加更改
git add .

# 提交更改（使用语义化提交信息）
git commit -m "feat: 添加新功能描述"
# 或
git commit -m "fix: 修复问题描述"
```

**提交信息格式**：
- `feat:` 新功能
- `fix:` 问题修复
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具变动

### 5. 推送分支
```bash
git push origin your-branch-name
```

### 6. 创建Pull Request
- 在GitHub上创建Pull Request
- 关联相关Issue
- 描述更改内容和测试情况
- 等待代码审查

## 🧪 测试要求

### 后端测试
```bash
# 运行所有测试
python -m pytest

# 运行特定测试
python -m pytest tests/test_agent.py

# 生成覆盖率报告
python -m pytest --cov=rm_agent
```

### 前端测试
```bash
cd frontend

# 运行测试
npm test

# 运行类型检查
npm run type-check

# 运行代码检查
npm run lint
```

## 📋 代码规范

### Python代码规范
- 遵循PEP 8规范
- 使用类型注解
- 编写清晰的文档字符串
- 保持函数简洁（不超过50行）

### 前端代码规范
- 使用TypeScript严格模式
- 遵循ESLint规则
- 组件命名使用PascalCase
- 使用函数式组件和Hooks

### 提交前检查
在提交代码前，请运行：
```bash
# 代码格式化
black rm_agent/

# 代码检查
flake8 rm_agent/

# 类型检查
mypy rm_agent/

# 前端代码检查
cd frontend && npm run lint && npm run type-check
```

## 🐛 报告问题

### Bug报告模板
```markdown
## 问题描述
清晰描述遇到的问题

## 重现步骤
1. 第一步
2. 第二步
3. ...

## 期望行为
描述期望的正常行为

## 实际行为
描述实际发生的异常行为

## 环境信息
- 操作系统：
- Python版本：
- 项目版本：
- 其他相关信息：

## 日志/截图
如果有错误日志或截图，请提供
```

### 功能请求模板
```markdown
## 功能描述
详细描述希望添加的功能

## 使用场景
说明该功能的使用场景和受益者

## 可能的实现方案
如果有实现思路，可以描述

## 备选方案
如果有其他实现方式，可以描述
```

## 🔧 开发工具推荐

### Python开发
- **编辑器**: VS Code, PyCharm
- **格式化**: Black, isort
- **检查**: flake8, mypy
- **测试**: pytest

### 前端开发
- **编辑器**: VS Code
- **包管理**: npm/yarn
- **构建工具**: Next.js
- **测试**: Jest, React Testing Library

## 🤝 行为准则

我们遵循以下行为准则：
- 尊重所有贡献者
- 建设性讨论
- 包容性语言
- 专业态度

## 📞 联系方式

如有问题，可以通过以下方式联系：
- 创建Issue
- 发送邮件到项目维护者
- 在讨论区发起话题

---

感谢您的贡献！🎉