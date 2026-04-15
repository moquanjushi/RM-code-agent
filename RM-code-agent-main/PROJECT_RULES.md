# 项目开发规则与最佳实践

## 📋 开发规范

### 代码风格要求
- **Python代码**: 遵循PEP 8规范
- **TypeScript**: 使用严格模式，类型定义完整
- **文件命名**: 小写字母+下划线，如 `react_agent.py`
- **函数命名**: 动词开头，描述性强，如 `generate_task_plan()`

### 文档标准
- **函数文档**: 必须包含参数说明、返回值、异常说明
- **类文档**: 包含类功能描述、属性说明、方法说明
- **模块文档**: 模块级别的功能概述

## 🛠️ 工具使用规范

### 代码质量工具
```bash
# 代码格式化
black rm_agent/

# 代码检查
flake8 rm_agent/

# 类型检查
mypy rm_agent/

# 导入排序
isort rm_agent/
```

### 测试规范
- **单元测试**: 每个功能模块必须有对应的测试
- **集成测试**: 测试智能体完整工作流
- **性能测试**: 定期测试执行效率和资源使用

## 🔧 智能体开发规范

### 工具开发要求
```python
class CustomTool(Tool):
    """工具类必须继承自Tool基类"""
    
    def __init__(self):
        super().__init__(
            name="custom_tool",
            description="工具功能描述",
            parameters={
                "param1": {"type": "string", "description": "参数说明"}
            }
        )
    
    def execute(self, params: Dict[str, Any]) -> str:
        """
        工具执行方法
        
        Args:
            params: 参数字典
            
        Returns:
            str: 执行结果描述
            
        Raises:
            ToolError: 工具执行失败时抛出
        """
        # 工具实现逻辑
        return "执行结果"
```

### 客户端开发规范
```python
class CustomClient(BaseLLMClient):
    """LLM客户端必须继承自BaseLLMClient"""
    
    def respond(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        实现模型响应方法
        
        Args:
            messages: 消息列表
            **kwargs: 其他参数
            
        Returns:
            str: 模型响应内容
        """
        # 客户端实现逻辑
        return "模型响应"
```

## 📊 性能监控规范

### 关键指标监控
- **执行时间**: 单任务平均执行时间
- **Token使用**: 每次调用的Token消耗
- **成功率**: 任务完成成功率
- **错误率**: 工具调用错误率

### 日志规范
```python
# 使用标准日志格式
import logging

logger = logging.getLogger(__name__)
logger.info("任务开始执行", extra={"task": task, "steps": max_steps})
logger.error("工具执行失败", extra={"tool": tool_name, "error": str(e)})
```

## 🔒 安全规范

### 代码执行安全
- **沙盒隔离**: 所有代码必须在Docker沙盒中执行
- **权限控制**: 限制文件系统访问权限
- **输入验证**: 所有用户输入必须验证

### API安全
- **密钥管理**: API密钥必须通过环境变量配置
- **请求限制**: 实现合理的API调用频率限制
- **错误处理**: 避免泄露敏感信息的错误消息

## 📈 测试与验证规范

### 智能体能力测试
```python
# 基础功能测试
def test_agent_basic_functionality():
    """测试智能体基础功能"""
    agent = ReactAgent(client, tools)
    result = agent.run("简单任务")
    assert "final_answer" in result
    assert result["final_answer"] != ""

# 工具集成测试
def test_tool_integration():
    """测试工具集成"""
    # 验证工具是否正确加载和执行
    pass

# 性能基准测试
def test_performance_benchmark():
    """性能基准测试"""
    # 测试执行时间、内存使用等
    pass
```

### 量化评估指标
```python
# 智能体能力评估类
class AgentEvaluator:
    """智能体能力评估器"""
    
    def evaluate_code_generation(self, task: str) -> Dict[str, float]:
        """评估代码生成能力"""
        return {
            "completeness": 0.95,  # 完整性
            "correctness": 0.90,   # 正确性
            "efficiency": 0.85     # 效率
        }
    
    def evaluate_problem_solving(self, task: str) -> Dict[str, float]:
        """评估问题解决能力"""
        return {
            "accuracy": 0.88,      # 准确率
            "steps_optimization": 0.35,  # 步骤优化率
            "success_rate": 0.82   # 成功率
        }
```

## 🔄 版本管理规范

### 版本号规则
- **主版本**: 不兼容的API修改
- **次版本**: 向下兼容的功能性新增
- **修订号**: 向下兼容的问题修正

### 发布流程
1. **功能开发** → 2. **单元测试** → 3. **集成测试** → 4. **性能测试** → 5. **文档更新** → 6. **版本发布**

## 🎯 质量保证

### 代码审查清单
- [ ] 代码符合PEP 8规范
- [ ] 类型注解完整
- [ ] 文档字符串齐全
- [ ] 单元测试覆盖
- [ ] 错误处理完善
- [ ] 性能考虑充分

### 发布检查清单
- [ ] 所有测试通过
- [ ] 文档更新完成
- [ ] 版本号正确
- [ ] 变更日志更新
- [ ] 兼容性验证通过

## 📚 参考资源

### 开发工具链
- **代码格式化**: Black, isort
- **代码检查**: flake8, pylint
- **类型检查**: mypy
- **测试框架**: pytest
- **文档生成**: Sphinx

### 最佳实践指南
- [Python最佳实践](https://docs.python-guide.org/)
- [TypeScript最佳实践](https://www.typescriptlang.org/docs/)
- [AI智能体开发指南](https://ai.google.dev/)

---

*本文档为项目开发提供标准化指导，确保代码质量和可维护性*