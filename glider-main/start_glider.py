import subprocess
import os

# 切换到glider-main目录
target_dir = os.path.join(r"i:", "代理池", "glider-main")
print(f"正在切换到目录: {target_dir}")
try:
    os.chdir(target_dir)
    print(f"成功切换到目录: {os.getcwd()}")
    
    # 运行glider.exe，使用配置文件
    print("正在运行glider.exe...")
    subprocess.run(["glider.exe", "-config", "my_config.conf"])
    print("glider.exe执行完成")
except Exception as e:
    print(f"切换目录或运行glider.exe时出错: {str(e)}")
    print(f"当前工作目录: {os.getcwd()}")
    print("请检查路径是否正确。")