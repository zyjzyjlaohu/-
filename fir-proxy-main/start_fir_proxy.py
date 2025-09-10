import subprocess
import os

# 切换到fir-proxy目录
target_dir = os.path.join(r"i:", "代理池", "fir-proxy-main", "fir-proxy - 1.2")
print(f"正在切换到目录: {target_dir}")
try:
    os.chdir(target_dir)
    print(f"成功切换到目录: {os.getcwd()}")
    
    # 运行main.py
    print("正在运行main.py...")
    subprocess.run(["python", "main.py"])
    print("main.py执行完成")
except Exception as e:
    print(f"切换目录或运行main.py时出错: {str(e)}")
    print(f"当前工作目录: {os.getcwd()}")
    print("请检查路径是否正确。")