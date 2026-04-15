"""工具模块 - 提供智能体可用的各类工具（已集成 Docker 沙盒）"""

from typing import Any, Dict, List, Optional

# 1. 导入沙盒类
from ..sandbox import DockerSandbox
from .base import Tool
from .file_tools import (
    create_file,
    edit_file,
    list_directory,
    read_file,
    search_in_file,
)
# 注意：我们不再使用 execution_tools 中的 run_python 和 run_shell，而是使用下面的沙盒版本
from .execution_tools import run_linter, run_tests
from .code_analysis_tools import (
    parse_ast,
    get_function_signature,
    find_dependencies,
    get_code_metrics,
)

# --- 沙盒管理区域 Start ---

# 创建全局沙盒实例
_sandbox = DockerSandbox(workspace_dir="./workspace")  # 确保这里和你的实际工作目录一致
_sandbox_enabled = True  # 沙盒启用状态


def start_sandbox():
    """启动沙盒容器"""
    global _sandbox_enabled
    try:
        _sandbox.start()
        _sandbox_enabled = True
    except Exception as e:
        print(f"⚠️ Docker沙盒启动失败: {e}")
        print("⚠️ 将降级为本地执行模式（不推荐用于不可信任务）")
        _sandbox_enabled = False


def stop_sandbox():
    """停止沙盒容器"""
    global _sandbox_enabled
    if _sandbox_enabled:
        try:
            _sandbox.stop()
        except Exception as e:
            print(f"⚠️ Docker沙盒关闭失败: {e}")
        _sandbox_enabled = False


def _run_python_sandbox(arguments: Dict[str, Any]) -> str:
    """在沙盒中执行 Python 代码"""
    global _sandbox_enabled
    
    # 如果沙盒不可用，降级到本地执行
    if not _sandbox_enabled:
        from .execution_tools import run_python
        return run_python(arguments)
    
    code = arguments.get("code")
    path = arguments.get("path")
    args = arguments.get("args", "")

    if isinstance(args, list):
        args = " ".join(args)

    if path:
        # 在容器内执行文件
        # 假设 Docker 挂载时将 workspace_dir 挂载到了 /workspace
        cmd = f"python {path} {args}"
    elif code:
        # 在容器内执行代码字符串
        # 注意：为了防止复杂的引号转义问题，生产环境通常建议先 create_file 再运行
        # 这里做简单的转义处理
        safe_code = code.replace('"', '\\"')
        cmd = f'python -c "{safe_code}"'
    else:
        return "Error: Missing 'code' or 'path' argument."

    return _sandbox.run_command(cmd)


def _run_shell_sandbox(arguments: Dict[str, Any]) -> str:
    """在沙盒中执行 Shell 命令"""
    global _sandbox_enabled
    
    # 如果沙盒不可用，降级到本地执行
    if not _sandbox_enabled:
        from .execution_tools import run_shell
        return run_shell(arguments)
    
    cmd = arguments.get("command")
    if not cmd:
        return "Error: Missing 'command' argument."
    return _sandbox.run_command(cmd)


def _run_tests_sandbox(arguments: Dict[str, Any]) -> str:
    """在沙盒中运行测试"""
    global _sandbox_enabled
    
    # 如果沙盒不可用，降级到本地执行
    if not _sandbox_enabled:
        from .execution_tools import run_tests
        return run_tests(arguments)
    
    test_path = arguments.get("test_path", ".")
    framework = arguments.get("framework", "pytest")
    verbose = arguments.get("verbose", False)
    
    if framework not in ["pytest", "unittest"]:
        return "Error: framework must be 'pytest' or 'unittest'."
    
    if framework == "pytest":
        cmd = f"python -m pytest {test_path}"
        if verbose:
            cmd += " -v"
    else:
        cmd = f"python -m unittest discover -s {test_path}"
        if verbose:
            cmd += " -v"
    
    return _sandbox.run_command(cmd)


def _run_linter_sandbox(arguments: Dict[str, Any]) -> str:
    """在沙盒中运行代码检查"""
    global _sandbox_enabled
    
    # 如果沙盒不可用，降级到本地执行
    if not _sandbox_enabled:
        from .execution_tools import run_linter
        return run_linter(arguments)
    
    path_value = arguments.get("path")
    tool = arguments.get("tool", "flake8")
    
    if not path_value:
        return "Error: Missing 'path' argument."
    
    if tool not in ["pylint", "flake8", "mypy", "black"]:
        return "Error: tool must be 'pylint', 'flake8', 'mypy', or 'black'."
    
    if tool == "black":
        cmd = f"python -m black --check {path_value}"
    else:
        cmd = f"python -m {tool} {path_value}"
    
    return _sandbox.run_command(cmd)


# --- 沙盒管理区域 End ---


def task_complete(arguments: Dict[str, Any]) -> str:
    """
    标记任务完成的工具。
    """
    message = arguments.get("message", "")
    if message and isinstance(message, str):
        return f"任务完成：{message.strip()}"
    return "任务已完成。"


def default_tools(include_mcp: bool = True, mcp_tools: Optional[List[Tool]] = None) -> List[Tool]:
    """返回默认工具集（使用沙盒版执行工具）"""
    tools = [
        Tool(
            name="list_directory",
            description=(
                "List entries for the given directory path. Arguments: {\"path\": optional string (default '.'), "
                "\"recursive\": optional bool (default false), \"file_type\": optional string filter like '.py' or '.js'}."
            ),
            runner=list_directory,
        ),
        Tool(
            name="read_file",
            description=(
                "Read a UTF-8 text file. Arguments: {\"path\": string, "
                "\"line_start\": optional int, \"line_end\": optional int}."
            ),
            runner=read_file,
        ),
        Tool(
            name="create_file",
            description="Create or overwrite a text file. Arguments: {\"path\": string, \"content\": string}.",
            runner=create_file,
        ),
        Tool(
            name="edit_file",
            description=(
                "Edit specific lines in a file. Arguments: {\"path\": string, \"operation\": \"insert\"|\"replace\"|\"delete\", "
                "\"line_start\": int, \"line_end\": int (for replace/delete), \"content\": string (for insert/replace)}."
            ),
            runner=edit_file,
        ),
        Tool(
            name="search_in_file",
            description=(
                "Search for text or regex pattern in a file. Arguments: {\"path\": string, \"pattern\": string, "
                "\"context_lines\": optional int (default 2)}."
            ),
            runner=search_in_file,
        ),
        # --- 修改点：使用沙盒 Runner ---
        Tool(
            name="run_python",
            description=(
                "Execute Python code inside a secure Docker Sandbox. Arguments: either {\"code\": string} or {\"path\": string, \"args\": optional string or list}."
            ),
            runner=_run_python_sandbox,  # <--- 替换为 _run_python_sandbox
        ),
        Tool(
            name="run_shell",
            description="Execute a shell command inside a secure Docker Sandbox. Arguments: {\"command\": string}.",
            runner=_run_shell_sandbox,  # <--- 替换为 _run_shell_sandbox
        ),
        # ---------------------------
        Tool(
            name="run_tests",
            description=(
                "Run Python test suite inside a secure Docker Sandbox. Arguments: {\"test_path\": optional string (default '.'), "
                "\"framework\": optional \"pytest\"|\"unittest\" (default 'pytest'), \"verbose\": optional bool (default false)}."
            ),
            runner=_run_tests_sandbox,  # <--- 替换为沙盒版本
        ),
        Tool(
            name="run_linter",
            description=(
                "Run code linter/formatter inside a secure Docker Sandbox. Arguments: {\"path\": string, "
                "\"tool\": optional \"pylint\"|\"flake8\"|\"mypy\"|\"black\" (default 'flake8')}."
            ),
            runner=_run_linter_sandbox,  # <--- 替换为沙盒版本
        ),
        Tool(
            name="parse_ast",
            description=(
                "Parse Python file AST to extract structure (functions, classes, imports). Arguments: {\"path\": string}."
            ),
            runner=parse_ast,
        ),
        Tool(
            name="get_function_signature",
            description=(
                "Get function signature with type hints. Arguments: {\"path\": string, \"function_name\": string}."
            ),
            runner=get_function_signature,
        ),
        Tool(
            name="find_dependencies",
            description=(
                "Analyze file dependencies (imports). Arguments: {\"path\": string}."
            ),
            runner=find_dependencies,
        ),
        Tool(
            name="get_code_metrics",
            description=(
                "Get code metrics (lines, functions, classes count). Arguments: {\"path\": string}."
            ),
            runner=get_code_metrics,
        ),
        Tool(
            name="task_complete",
            description="Mark the task as complete and finish execution. Arguments: {\"message\": optional string with completion summary}.",
            runner=task_complete,
        ),
    ]

    # 添加 MCP 工具
    if include_mcp and mcp_tools:
        tools.extend(mcp_tools)

    return tools


# 导出新增的控制函数
__all__ = [
    "Tool",
    "default_tools",
    "task_complete",
    "start_sandbox",
    "stop_sandbox",
]