---
name: "code-reviewer"
description: "Reviews code for best practices, bugs, and improvements. Invoke when user asks for code review or before merging changes."
---

# Code Reviewer Skill

This skill provides automated code review capabilities for the AI Code Agent system.

## 🎯 Purpose

The Code Reviewer skill enables the agent to:
- Analyze code quality and identify potential issues
- Suggest improvements based on best practices
- Detect security vulnerabilities and performance bottlenecks
- Provide constructive feedback on code structure

## 🔧 Implementation

### Core Review Capabilities

#### 1. Code Quality Analysis
- **Syntax Validation**: Check for syntax errors and inconsistencies
- **Style Compliance**: Verify adherence to coding standards (PEP 8, etc.)
- **Complexity Metrics**: Calculate cyclomatic complexity and maintainability

#### 2. Security Review
- **Vulnerability Detection**: Identify common security issues
- **Input Validation**: Check for proper input sanitization
- **Dependency Analysis**: Review third-party library security

#### 3. Performance Analysis
- **Efficiency Checks**: Identify performance bottlenecks
- **Memory Usage**: Analyze memory management practices
- **Algorithm Optimization**: Suggest more efficient algorithms

### Integration Points

```python
class CodeReviewerSkill:
    """Code Reviewer Skill Implementation"""
    
    def __init__(self):
        self.name = "code_reviewer"
        self.description = "Automated code review and quality analysis"
    
    def review_file(self, file_path: str) -> Dict[str, Any]:
        """Review a single file"""
        # Implementation details
        pass
    
    def review_project(self, project_path: str) -> Dict[str, Any]:
        """Review entire project structure"""
        # Implementation details
        pass
```

## 📊 Review Metrics

### Quality Score (0-100)
- **90-100**: Excellent - Minimal issues, follows best practices
- **80-89**: Good - Minor improvements possible
- **70-79**: Fair - Some issues need attention
- **Below 70**: Needs Work - Significant improvements required

### Issue Categories
1. **Critical**: Security vulnerabilities, major bugs
2. **High**: Performance issues, architectural problems
3. **Medium**: Code style violations, minor inefficiencies
4. **Low**: Cosmetic issues, documentation improvements

## 🚀 Usage Examples

### Basic File Review
```python
# Review a specific Python file
review_result = code_reviewer.review_file("src/main.py")
```

### Project-wide Review
```python
# Review entire project
project_review = code_reviewer.review_project("./")
```

### Integration with Agent
```python
# Agent can use the skill during development
agent.skills["code_reviewer"].review_file(generated_file)
```

## 🔍 Review Output Format

### Sample Review Report
```json
{
  "file_path": "src/main.py",
  "quality_score": 85,
  "issues": [
    {
      "type": "security",
      "severity": "high",
      "description": "Potential SQL injection vulnerability",
      "line": 45,
      "suggestion": "Use parameterized queries"
    },
    {
      "type": "performance", 
      "severity": "medium",
      "description": "Inefficient loop structure",
      "line": 78,
      "suggestion": "Consider using list comprehension"
    }
  ],
  "metrics": {
    "complexity": 15,
    "maintainability": 0.78,
    "test_coverage": 0.65
  }
}
```

## 📈 Integration with Testing

### Automated Review Pipeline
```python
def automated_review_pipeline():
    """Automated code review workflow"""
    
    # 1. Code generation by agent
    generated_code = agent.generate_code(task)
    
    # 2. Automated review
    review_results = code_reviewer.review_code(generated_code)
    
    # 3. Quality gate
    if review_results["quality_score"] >= 80:
        return {"status": "approved", "code": generated_code}
    else:
        # 4. Auto-fix suggestions
        improved_code = agent.improve_code(generated_code, review_results)
        return {"status": "improved", "code": improved_code}
```

## 🔮 Future Enhancements

### Planned Features
- [ ] **AI-powered suggestions**: Use LLM for contextual improvements
- [ ] **Multi-language support**: Extend beyond Python
- [ ] **Real-time review**: Integrate with IDE plugins
- [ ] **Team collaboration**: Share review results and track improvements

### Integration Goals
- [ ] **CI/CD pipeline**: Automated code review in build process
- [ ] **Quality dashboards**: Visualize code quality trends
- [ ] **Custom rules**: Allow project-specific review criteria

---

*This skill enhances the agent's ability to produce high-quality, secure, and efficient code.*