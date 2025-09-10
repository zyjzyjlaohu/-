# freeproxy

通过fofa资产测绘平台获取大量代理数据，利用并发技术快速检测代理的可用性并爆破弱口令，爆破用户名密码可以自行添加到user.txt和pass.txt


使用fofa以下fofa语句进行搜索socks5代理数据，需要key，支持无key，无key可以将key设为空然后可以使用下面的语法进行查询后导出到fofa_results.txt

```
protocol=="socks5" && "Version:5 Method:No Authentication(0x00)" && country="CN"
```


示范格式

```
127.0.0.1:1080
```

![image示例](https://github.com/user-attachments/assets/d5d0810b-aff7-429f-a140-b9a6665cd0f8)



可食用的地址输出在valid_proxies.txt中

![结果示例](https://github.com/user-attachments/assets/f2bcfa6a-5222-4287-ab0a-dc178e362096)


可以将valid_proxies.txt直接放入到ProxyCat代理的ip.txt中，开启ProxyCat的代理就使用成功了

## 安装方法

1. 确保已安装Python 3.6或更高版本

2. 安装依赖：
```bash
pip install requests
```

3. 修改配置：
   - 在freeproxy.py文件中，设置您的Fofa API Key
   - 或使用无key方式，将key设为空

4. 准备用户名和密码文件：
   - user.txt：包含可能的用户名，每行一个
   - pass.txt：包含可能的密码，每行一个

5. 运行程序：
```bash
python freeproxy.py
```

## 使用说明

1. **获取代理数据**：
   - 程序会使用配置的Fofa API查询socks5代理
   - 查询结果会保存到fofa_results.txt

2. **检测开放端口**：
   - 程序会并发检测查询到的IP和端口是否开放
   - 开放的端口会保存到open_ports.txt

3. **验证代理有效性**：
   - 程序会验证开放端口的代理是否可用
   - 有效的代理会保存到valid_proxies.txt

4. **弱口令爆破**：
   - 程序会尝试使用user.txt和pass.txt中的用户名密码组合进行代理认证
   - 支持认证的代理也会保存到valid_proxies.txt中

## 配置说明

在freeproxy.py文件中，您可以修改以下配置：

- `FOFA_KEY`：您的Fofa API Key
- `FOFA_URL`：Fofa API查询URL（包含查询语法）
- 输出文件路径：可以自定义保存结果的文件路径
- 线程数：可以根据您的系统性能调整并发线程数
- 超时时间：可以调整连接和验证的超时时间

## 注意事项

1. 使用本工具需要有有效的Fofa API Key（可选）
2. 大量请求可能会消耗Fofa API的调用额度
3. 建议根据您的系统性能调整线程数，避免资源占用过高
4. 代理的有效性会随着时间变化，建议定期更新代理列表
5. 本工具仅用于学习和研究目的，请遵守相关法律法规

## 常见问题

### 1. 运行时提示"API调用失败"怎么办？
- 检查您的Fofa API Key是否正确
- 检查您的网络连接是否正常
- 检查您的Fofa账号是否有足够的API调用额度

### 2. 收集到的代理数量很少怎么办？
- 尝试修改Fofa搜索语法，使用更广泛的搜索条件
- 增加搜索结果数量（默认为5000）

### 3. 验证后的有效代理为什么很少？
- 免费代理的稳定性和可用性通常较低
- 可以尝试调整超时时间，增加验证时间

## 更新日志

### v1.0
- 初始版本，实现基本的代理收集和验证功能

### v1.1
- 增加多线程并发处理
- 优化代理验证逻辑
- 增加弱口令爆破功能