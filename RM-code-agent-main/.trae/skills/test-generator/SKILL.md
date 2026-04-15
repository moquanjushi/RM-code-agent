---
name: "test-generator"
description: "Generates comprehensive test cases for code. Invoke when user requests test creation or when code changes require testing."
---

# Test Generator Skill

This skill provides automated test generation capabilities for the AI Code Agent system.

## 🎯 Purpose

The Test Generator skill enables the agent to:
- Generate unit tests for functions and classes
- Create integration tests for multi-component systems
- Produce test data and fixtures
- Ensure test coverage and quality

## 🔧 Implementation

### Core Test Generation Capabilities

#### 1. Unit Test Generation
- **Function Testing**: Create tests for individual functions
- **Class Testing**: Generate tests for class methods and properties
- **Edge Cases**: Identify and test boundary conditions
- **Mock Objects**: Create appropriate mocks for dependencies

#### 2. Integration Test Generation
- **Component Integration**: Test interactions between modules
- **API Testing**: Generate tests for REST APIs and endpoints
- **Database Testing**: Create tests for database operations
- **System Testing**: Test complete system workflows

#### 3. Test Quality Assurance
- **Coverage Analysis**: Ensure adequate test coverage
- **Test Data Generation**: Create realistic test data
- **Performance Testing**: Generate performance benchmarks
- **Security Testing**: Create security-focused test cases

### Integration Points

```python
class TestGeneratorSkill:
    """Test Generator Skill Implementation"""
    
    def __init__(self):
        self.name = "test_generator"
        self.description = "Automated test case generation"
    
    def generate_unit_tests(self, code: str, framework: str = "pytest") -> Dict[str, Any]:
        """Generate unit tests for given code"""
        # Implementation details
        pass
    
    def generate_integration_tests(self, components: List[str]) -> Dict[str, Any]:
        """Generate integration tests for component interactions"""
        # Implementation details
        pass
    
    def analyze_test_coverage(self, code: str, tests: str) -> Dict[str, float]:
        """Analyze test coverage for code"""
        # Implementation details
        pass
```

## 📊 Test Quality Metrics

### Coverage Metrics
- **Line Coverage**: Percentage of code lines executed by tests
- **Branch Coverage**: Percentage of code branches tested
- **Function Coverage**: Percentage of functions/methods tested
- **Condition Coverage**: Percentage of conditions tested

### Quality Metrics
- **Test Effectiveness**: Ability to detect real bugs
- **Maintainability**: Ease of test maintenance
- **Execution Speed**: Test execution performance
- **Readability**: Test code clarity and documentation

## 🚀 Usage Examples

### Basic Unit Test Generation
```python
# Generate tests for a specific function
test_result = test_generator.generate_unit_tests("""
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
""")
```

### Integration Test Generation
```python
# Generate tests for API endpoints
api_tests = test_generator.generate_integration_tests([
    "user_service", "order_service", "payment_service"
])
```

### Test Coverage Analysis
```python
# Analyze test coverage
coverage_report = test_generator.analyze_test_coverage(
    source_code, generated_tests
)
```

## 🔍 Test Output Format

### Sample Test Generation Report
```json
{
  "test_framework": "pytest",
  "generated_tests": [
    {
      "test_name": "test_calculate_total_basic",
      "test_code": "def test_calculate_total_basic():\n    result = calculate_total(10.0, 2)\n    assert result == 20.0",
      "coverage": {"lines": 1, "branches": 0, "functions": 1},
      "category": "unit_test"
    },
    {
      "test_name": "test_calculate_total_edge_cases", 
      "test_code": "def test_calculate_total_edge_cases():\n    # Test zero quantity\n    result = calculate_total(10.0, 0)\n    assert result == 0.0",
      "coverage": {"lines": 1, "branches": 1, "functions": 1},
      "category": "edge_case"
    }
  ],
  "coverage_summary": {
    "total_lines": 5,
    "covered_lines": 4,
    "coverage_percentage": 80.0
  }
}
```

## 📈 Integration with Development Workflow

### Automated Test Pipeline
```python
def automated_test_pipeline():
    """Automated test generation workflow"""
    
    # 1. Code generation by agent
    generated_code = agent.generate_code(task)
    
    # 2. Test generation
    test_results = test_generator.generate_tests(generated_code)
    
    # 3. Test execution and validation
    execution_results = execute_tests(test_results["generated_tests"])
    
    # 4. Quality assessment
    if execution_results["pass_rate"] >= 95:
        return {"status": "tests_passed", "code": generated_code}
    else:
        # 5. Test improvement
        improved_tests = test_generator.improve_tests(
            generated_code, test_results, execution_results
        )
        return {"status": "tests_improved", "tests": improved_tests}
```

## 🔮 Future Enhancements

### Planned Features
- [ ] **AI-powered test generation**: Use LLM for more intelligent test creation
- [ ] **Multi-language support**: Extend beyond Python to other languages
- [ ] **Property-based testing**: Generate property-based tests
- [ ] **Fuzz testing**: Create fuzz testing scenarios

### Integration Goals
- [ ] **CI/CD integration**: Automated test generation in pipelines
- [ ] **Test optimization**: Smart test selection and prioritization
- [ ] **Mutation testing**: Generate mutation tests for quality assurance
- [ ] **Performance testing**: Automated performance test generation

### Advanced Capabilities
- [ ] **Test data synthesis**: Generate realistic test data automatically
- [ ] **Test oracle generation**: Create expected results for complex functions
- [ ] **Regression test detection**: Identify tests affected by code changes
- [ ] **Test maintenance**: Automated test refactoring and updates

---

*This skill enhances the agent's ability to create comprehensive, high-quality test suites that ensure code reliability and maintainability.*