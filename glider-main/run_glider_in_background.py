import subprocess
import time
import os

# 定义日志文件路径
log_file = os.path.join(r"i:", "代理池", "glider-main", "glider.log")

# 在后台运行 glider.exe，并将输出重定向到日志文件
print(f"正在尝试在后台运行glider.exe，日志将输出到: {log_file}")
try:
    process = subprocess.Popen(
        [os.path.join(r"i:", "代理池", "glider-main", "glider.exe"), "-config", os.path.join(r"i:", "代理池", "glider-main", "my_config.conf")],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        shell=False
    )

    # 等待几秒钟让 glider 有时间启动
    time.sleep(2)

    print(f"glider 已尝试在后台启动，进程 ID: {process.pid}")
    print(f"请查看 {log_file} 文件了解详细输出。")
    
    # 将输出写入日志文件
    with open(log_file, "w") as f:
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output.strip())
                f.write(output)
                f.flush()
        
        # 写入错误信息
        stderr = process.stderr.read()
        if stderr:
            print(f"错误输出: {stderr}")
            f.write(f"\n错误输出:\n{stderr}")
    
    print(f"glider 进程已结束，退出码: {process.returncode}")
except Exception as e:
    print(f"启动glider时出错: {str(e)}")