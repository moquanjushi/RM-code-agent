# dm_agent/sandbox.py
import docker
import os
import time


class DockerSandbox:
    def __init__(self, image="python:3.9-slim", workspace_dir="./workspace"):
        self.client = docker.from_env()
        self.image = image
        # 确保本地工作目录存在
        self.workspace_host = os.path.abspath(workspace_dir)
        os.makedirs(self.workspace_host, exist_ok=True)
        self.container_name = "dm_agent_sandbox"
        self.container = None

    def start(self):
        """启动沙盒容器"""
        try:
            # 清理旧容器
            self.stop()
        except:
            pass

        print(f"📦 正在启动 Docker 沙盒 ({self.image})...")

        try:
            self.container = self.client.containers.run(
                self.image,
                command="tail -f /dev/null",  # 让容器保持运行
                name=self.container_name,
                detach=True,
                working_dir="/workspace",  # 容器内的工作目录
                volumes={
                    self.workspace_host: {
                        'bind': '/workspace',
                        'mode': 'rw'
                    }
                },
                # 限制资源防止死循环耗尽资源
                mem_limit="512m",
                cpu_quota=50000,
                network_mode="bridge"  # 允许联网装包，或设为 "none" 禁止联网
            )
            print("✅ 沙盒启动成功")
        except Exception as e:
            print(f"❌ 沙盒启动失败: {e}")
            raise e

    def stop(self):
        """停止并删除容器"""
        try:
            old = self.client.containers.get(self.container_name)
            old.stop()
            old.remove()
            print("🛑 沙盒已关闭")
        except docker.errors.NotFound:
            pass

    def run_command(self, command: str, timeout: int = 30) -> str:
        """在容器内执行命令"""
        if not self.container:
            return "Error: Sandbox not running"

        try:
            # exec_run 返回 (exit_code, output)
            exec_result = self.container.exec_run(
                cmd=["/bin/sh", "-c", command],
                workdir="/workspace"
            )
            output = exec_result.output.decode("utf-8")
            exit_code = exec_result.exit_code

            if exit_code != 0:
                return f"执行出错 (Exit Code {exit_code}):\n{output}"
            return output if output.strip() else "执行成功，无输出。"

        except Exception as e:
            return f"Docker执行异常: {str(e)}"