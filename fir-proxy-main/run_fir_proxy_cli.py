import subprocess
import os

# 直接使用绝对路径运行 hq.py 命令行版本脚本
print("尝试运行 fir-proxy 的命令行版本脚本 hq.py...")
process = subprocess.Popen(
    ["python", os.path.join(r"i:", "代理池", "fir-proxy-main", "fir-proxy - 1.2", "hq.py")],
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# 获取输出并实时打印
while True:
    output = process.stdout.readline()
    if output == '' and process.poll() is not None:
        break
    if output:
        print(output.strip())

# 打印错误信息
stderr = process.stderr.read()
if stderr:
    print(f"错误输出: {stderr}")

print(f"命令行版本脚本执行完成，退出码: {process.returncode}")