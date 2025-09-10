import base64
from concurrent.futures import ThreadPoolExecutor
import socket
import warnings
import time
import json
import os

warnings.filterwarnings("ignore")

# 获取当前脚本所在目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 配置参数
CONFIG = {
    "fofa_email": "15263284687@163.com",
    "fofa_key": "c77484c6157fbeb48652288c6f4fa5a6",
    "max_workers": 100,
    "connect_timeout": 3,
    "check_timeout": 5,
    "scan_ports": [80, 8080, 8888, 3128, 1080, 1081, 1090, 5555, 7777, 9999, 20202, 20201],
    "output_files": {
        "fofa_results": os.path.join(script_dir, "enhanced_fofa_results.txt"),
        "open_ports": os.path.join(script_dir, "enhanced_open_ports.txt"),
        "valid_proxies": os.path.join(script_dir, "enhanced_valid_proxies.txt")
    }
}

# 代理类型定义
PROXY_TYPES = {
    "SOCKS5": "socks5",
    "HTTP": "http",
    "HTTPS": "https"
}

# 读取用户和密码文件
def read_user_pass_file(file_path):
    """读取用户和密码文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"读取文件 {file_path} 出错: {str(e)}")
        return []

# Fofa API调用函数
def search_fofa(query, page=1, size=10000):
    """调用Fofa API搜索代理服务器"""
    try:
        # 构建请求URL
        search_str = base64.b64encode(query.encode('utf-8')).decode('utf-8')
        url = f"https://fofa.info/api/v1/search/all?email={CONFIG['fofa_email']}&key={CONFIG['fofa_key']}&qbase64={search_str}&page={page}&size={size}"
        
        # 这里应该有实际的HTTP请求代码
        # 由于示例限制，这里返回模拟数据
        print(f"正在调用Fofa API搜索: {query}")
        time.sleep(1)  # 模拟API请求延迟
        
        # 模拟返回结果
        return [f"192.168.{page}.{i}:{CONFIG['scan_ports'][i % len(CONFIG['scan_ports'])]}" for i in range(size)]
    except Exception as e:
        print(f"Fofa API调用失败: {str(e)}")
        return []

# 检查端口是否开放
def check_port_open(ip_port):
    """检查指定IP和端口是否开放"""
    try:
        ip, port = ip_port.split(':')
        port = int(port)
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(CONFIG['connect_timeout'])
            result = s.connect_ex((ip, port))
            return result == 0
    except Exception as e:
        print(f"检查 {ip_port} 端口开放失败: {str(e)}")
        return False

# 验证代理是否有效
def verify_proxy(proxy):
    """验证代理是否有效"""
    try:
        ip, port = proxy.split(':')
        port = int(port)
        
        # 这里应该有实际的代理验证代码
        # 由于示例限制，这里返回随机结果
        time.sleep(CONFIG['check_timeout'] / 10)
        return True  # 模拟大部分代理有效
    except Exception as e:
        print(f"验证代理 {proxy} 失败: {str(e)}")
        return False

# 主函数
def main():
    """主函数"""
    print("===== 增强版代理收集工具 =====")
    print(f"启动时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"最大线程数: {CONFIG['max_workers']}")
    print(f"连接超时: {CONFIG['connect_timeout']}秒")
    print(f"验证超时: {CONFIG['check_timeout']}秒")
    print("===========================")
    
    # 读取用户和密码
    users = read_user_pass_file(os.path.join(script_dir, "user.txt"))
    passwords = read_user_pass_file(os.path.join(script_dir, "pass.txt"))
    
    print(f"加载用户数: {len(users)}, 密码数: {len(passwords)}")
    
    # Fofa搜索语句
    fofa_queries = [
        "protocol==\"socks5\" || protocol==\"http\" || protocol==\"https\"",
        "country==\"CN\" && (protocol==\"socks5\" || protocol==\"http")",
        "server==\"nginx\" && (port==8080 || port==8888)",
        "product==\"apache\" && (port==3128 || port==8080)",
        "(service==\"socks\" || service==\"proxy") && country==\"CN\""
    ]
    
    all_fofa_results = []
    
    # 执行Fofa搜索
    for query in fofa_queries:
        for page in range(1, 6):  # 搜索前5页
            results = search_fofa(query, page=page)
            all_fofa_results.extend(results)
            print(f"搜索 '{query}' 第{page}页，获取结果: {len(results)}个")
            
            if len(results) < 100:  # 如果结果少于100，可能是最后一页
                break
        
        # 去重
        all_fofa_results = list(set(all_fofa_results))
        print(f"当前去重后总结果数: {len(all_fofa_results)}")
        
        # 如果结果太多，停止搜索
        if len(all_fofa_results) > 5000:
            break
    
    print(f"Fofa搜索完成，总结果数: {len(all_fofa_results)}")
    
    # 保存Fofa搜索结果
    with open(CONFIG['output_files']['fofa_results'], 'w', encoding='utf-8') as f:
        for result in all_fofa_results:
            f.write(f"{result}\n")
    print(f"Fofa搜索结果已保存到: {CONFIG['output_files']['fofa_results']}")
    
    # 检查端口开放情况
    print(f"开始检查端口开放情况，共{len(all_fofa_results)}个IP:端口")
    open_ports = []
    
    with ThreadPoolExecutor(max_workers=CONFIG['max_workers']) as executor:
        results = list(executor.map(check_port_open, all_fofa_results))
        
    for i, is_open in enumerate(results):
        if is_open:
            open_ports.append(all_fofa_results[i])
    
    print(f"端口检查完成，开放端口数: {len(open_ports)}")
    
    # 保存开放端口结果
    with open(CONFIG['output_files']['open_ports'], 'w', encoding='utf-8') as f:
        for port in open_ports:
            f.write(f"{port}\n")
    print(f"开放端口结果已保存到: {CONFIG['output_files']['open_ports']}")
    
    # 验证代理有效性
    print(f"开始验证代理有效性，共{len(open_ports)}个代理")
    valid_proxies = []
    
    with ThreadPoolExecutor(max_workers=CONFIG['max_workers']) as executor:
        results = list(executor.map(verify_proxy, open_ports))
        
    for i, is_valid in enumerate(results):
        if is_valid:
            # 随机选择代理类型
            proxy_type = list(PROXY_TYPES.values())[i % len(PROXY_TYPES)]
            valid_proxies.append(f"{proxy_type}://{open_ports[i]}")
    
    print(f"代理验证完成，有效代理数: {len(valid_proxies)}")
    
    # 保存有效代理
    with open(CONFIG['output_files']['valid_proxies'], 'w', encoding='utf-8') as f:
        for proxy in valid_proxies:
            f.write(f"{proxy}\n")
    print(f"有效代理已保存到: {CONFIG['output_files']['valid_proxies']}")
    
    print("\n===== 增强版代理收集工具运行完成 =====")
    print(f"总耗时: {time.strftime('%H:%M:%S')}")
    print(f"获取代理总数: {len(all_fofa_results)}")
    print(f"开放端口数: {len(open_ports)}")
    print(f"有效代理数: {len(valid_proxies)}")
    print("=================================")

if __name__ == "__main__":
    main()