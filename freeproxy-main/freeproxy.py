import requests
from concurrent.futures import ThreadPoolExecutor
import socket
import warnings
import os

warnings.filterwarnings("ignore")

# 固定变量
FOFA_KEY = "your_fofa_api_key_here"  # 请替换为您的Fofa API Key
FOFA_URL = f"https://fofa.info/api/v1/search/all?key={FOFA_KEY}&qbase64=cHJvdG9jb2w9PSJzb2NrczUiICYmICJWZXJzaW9uOjUgTWV0aG9kOk5vIEF1dGhlbnRpY2F0aW9uKDB4MDApIiAmJiBjb3VudHJ5PSJDTiI=&size=5000"

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 文件名 - 使用脚本所在目录
FOFA_OUTPUT_FILE = os.path.join(script_dir, "fofa_results.txt")
PORT_OPEN_FILE = os.path.join(script_dir, "open_ports.txt")
VALID_PROXY_FILE = os.path.join(script_dir, "valid_proxies.txt")

# 爬取 Fofa 数据并保存到指定文件
def fetch_fofa_data():
    if not FOFA_KEY or FOFA_KEY == "your_fofa_api_key_here":
        print("FOFA_KEY 未设置或使用默认值，跳过 Fofa 数据爬取")
        print("请在freeproxy.py文件中设置您的Fofa API Key")
        return

    print("正在爬取 Fofa 数据")
    try:
        response = requests.get(FOFA_URL)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()

        print("正在提取数据")
        extracted_data = [result[0] for result in data['results']]

        with open(FOFA_OUTPUT_FILE, 'w') as f:
            for it in extracted_data:
                f.write(it + '\n')

        print(f"数据爬取完毕，结果已保存到 {FOFA_OUTPUT_FILE}")
    except Exception as e:
        print(f"Fofa数据爬取失败: {str(e)}")
        # 如果没有Fofa数据，创建一个示例文件供测试使用
        if not os.path.exists(FOFA_OUTPUT_FILE):
            with open(FOFA_OUTPUT_FILE, 'w') as f:
                f.write("127.0.0.1:1080\n192.168.1.1:8080\n")
            print(f"已创建示例文件: {FOFA_OUTPUT_FILE}")

# 测试端口是否开放
def test_port(proxy):
    proxy = proxy.strip()
    if not proxy or ':' not in proxy:
        return
    try:
        ip, port = proxy.split(":")
        if not ip or not port:
            return
        port = int(port)
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            with open(PORT_OPEN_FILE, 'a') as f:  # 追加模式
                f.write(proxy + '\n')
        sock.close()
    except Exception as e:
        # print(f"端口测试错误: {proxy}, 错误: {str(e)}")
        pass

def check_ports():
    print("正在测试端口开放情况")
    # 确保输出文件存在并为空
    open(PORT_OPEN_FILE, 'w').close()
    
    try:
        with open(FOFA_OUTPUT_FILE, "r") as f:
            proxies = f.readlines()
            if not proxies:
                print(f"{FOFA_OUTPUT_FILE} 文件为空，无法进行端口检测")
                return
    except FileNotFoundError:
        print(f"{FOFA_OUTPUT_FILE} 文件不存在，请检查或手动创建")
        return

    with ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(test_port, proxies)

    print(f"端口检测完毕，结果已保存到 {PORT_OPEN_FILE}")

# 测试代理的有效性，并输出对应的用户名和密码
def test_proxy(proxy):
    try:
        # 尝试无密码代理
        response = requests.get(
            'https://www.baidu.com/',
            proxies={'http': f"socks5://{proxy}", 'https': f"socks5://{proxy}"},
            timeout=6,
            verify=False
        )
        if response.status_code == 200:
            print(f'Working proxy: {proxy}')
            with open(VALID_PROXY_FILE, 'a') as file:
                file.write(f'socks5://{proxy}\n')
            return
    except Exception as e:
        # print(f"无密码代理测试失败: {proxy}, 错误: {str(e)}")
        pass

    # 尝试使用用户名和密码
    try:
        # 检查用户和密码文件是否存在
        if not os.path.exists('user.txt') or not os.path.exists('pass.txt'):
            # 创建默认的用户和密码文件
            with open('user.txt', 'w') as f:
                f.write('test\nguest\nadmin\n')
            with open('pass.txt', 'w') as f:
                f.write('123456\npassword\nadmin123\n')
            print("已创建默认的user.txt和pass.txt文件")
        
        with open('user.txt', 'r') as user_file:
            usernames = [line.strip() for line in user_file.readlines() if line.strip()]
        with open('pass.txt', 'r') as pass_file:
            passwords = [line.strip() for line in pass_file.readlines() if line.strip()]

        for username in usernames:
            for password in passwords:
                try:
                    response2 = requests.get(
                        'https://www.baidu.com/',
                        proxies={
                            'http': f"socks5://{username}:{password}@{proxy}",
                            'https': f"socks5://{username}:{password}@{proxy}"
                        },
                        timeout=2,
                        verify=False
                    )
                    if response2.status_code == 200:
                        print(f'Working proxy with credentials: {proxy} | Username: {username} | Password: {password}')
                        with open(VALID_PROXY_FILE, 'a') as file:
                            file.write(f'socks5://{username}:{password}@{proxy}\n')
                        return
                except Exception as e:
                    # print(f"带凭证代理测试失败: {proxy}, 错误: {str(e)}")
                    pass
    except Exception as e:
        print(f"读取用户或密码文件错误: {str(e)}")
    
    # print(f'Failed proxy: {proxy}')

def check_proxies():
    print("正在测试代理的有效性")
    # 确保输出文件存在并为空
    open(VALID_PROXY_FILE, 'w').close()
    
    try:
        with open(PORT_OPEN_FILE, 'r') as file:
            proxies = [line.strip() for line in file.readlines() if line.strip()]
            if not proxies:
                print(f"{PORT_OPEN_FILE} 文件为空，无法进行代理检测")
                return
    except FileNotFoundError:
        print(f"{PORT_OPEN_FILE} 文件不存在，请检查或手动创建")
        return

    with ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(test_proxy, proxies)

    print(f"代理检测完毕，结果已保存到 {VALID_PROXY_FILE}")

# 主函数
def main():
    print("===== 免费代理收集工具 ======")
    print(f"当前时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"脚本目录: {script_dir}")
    print("==========================")
    
    # 确保所有输出目录存在
    for file_path in [FOFA_OUTPUT_FILE, PORT_OPEN_FILE, VALID_PROXY_FILE]:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # 开始处理
    fetch_fofa_data()
    check_ports()
    check_proxies()
    
    # 显示统计信息
    try:
        if os.path.exists(FOFA_OUTPUT_FILE):
            with open(FOFA_OUTPUT_FILE, 'r') as f:
                fofa_count = len(f.readlines())
            print(f"Fofa搜索结果总数: {fofa_count}")
        
        if os.path.exists(PORT_OPEN_FILE):
            with open(PORT_OPEN_FILE, 'r') as f:
                port_count = len(f.readlines())
            print(f"开放端口数: {port_count}")
        
        if os.path.exists(VALID_PROXY_FILE):
            with open(VALID_PROXY_FILE, 'r') as f:
                valid_count = len(f.readlines())
            print(f"有效代理数: {valid_count}")
        
        print("\n===== 处理完成 =====")
        print(f"结束时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        if valid_count > 0:
            print(f"有效代理已保存到: {VALID_PROXY_FILE}")
            print("您可以将valid_proxies.txt中的内容添加到其他代理工具中使用")
        else:
            print("未找到有效代理，请尝试修改Fofa搜索语法或检查网络连接")
    except Exception as e:
        print(f"显示统计信息时出错: {str(e)}")

if __name__ == '__main__':
    import time
    main()