# ProxyCat

<p align="center">
  <a href="/README-EN.md">English</a>
  ·
  <a href="/README.md">简体中文</a>
</p>

## 目录

- [开发缘由](#开发缘由)
- [功能特点](#功能特点)
- [安装与使用](#安装与使用)
- [免责申明](#免责申明)
- [更新日志](#更新日志)
- [开发计划](#开发计划)
- [特别鸣谢](#特别鸣谢)
- [赞助开源](#赞助开源)
- [代理推荐](#代理推荐)

## 开发缘由

在渗透过程中，经常需要隐藏或更换IP地址以绕过安全设备。然而，市面上的隧道代理价格高昂，普遍在20-40元/天，这对于许多人来说难以接受。笔者注意到，短效IP的性价比很高，一个IP只需几分钱，平均每天0.2-3元。

综上所述，**ProxyCat** 应运而生！本工具旨在将持续时间仅有1分钟至60分钟不等的短效IP转变为固定IP供其他工具使用，形成代理池服务器，部署一次即可永久使用。

![项目原理图](assets/项目原理图.png)

## 功能特点

### 核心功能

- **自动轮换代理**：持续监控代理有效性，自动切换到可用代理
- **多协议支持**：同时支持HTTP和SOCKS5代理协议
- **高并发验证**：高效验证代理可用性，确保服务稳定性
- **自定义白名单**：支持配置代理白名单，限制特定IP访问代理服务
- **自定义黑名单**：支持配置代理黑名单，阻止恶意IP访问
- **界面友好**：提供直观的命令行界面，实时显示代理状态

### 扩展功能

- **代理池管理**：自动管理多个代理，实现负载均衡
- **自动更新**：支持检查工具更新，及时获取最新功能
- **性能监控**：实时显示代理响应时间，帮助选择最优代理
- **配置灵活**：通过配置文件自定义各种参数
- **端口复用**：支持在同一端口同时提供HTTP和SOCKS5服务

## 安装与使用

### 环境要求

- Python 3.7 或更高版本
- 必要的依赖包（通过requirements.txt安装）

### 安装步骤

1. 克隆或下载本项目

```bash
git clone https://github.com/your-username/ProxyCat.git
cd ProxyCat
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 配置代理池

编辑 `config/config.ini` 文件，根据需要修改配置参数：

```ini
[Proxy]
# 代理服务监听地址和端口
listen_host = 127.0.0.1
listen_port = 8888

# 代理验证相关配置
check_interval = 30
check_timeout = 5
max_workers = 50

# 代理池相关配置
proxy_rotation = True
rotation_interval = 60

# 白名单和黑名单配置
use_whitelist = False
use_blacklist = False
```

4. 添加代理IP

在 `config/ip.txt` 文件中添加您的代理IP列表，格式为：

```
http://username:password@ip:port
socks5://username:password@ip:port
```

5. 启动ProxyCat

```bash
python ProxyCat.py
```

## 使用方法

启动后，ProxyCat会自动验证代理IP的有效性，并在指定端口提供HTTP和SOCKS5代理服务。您可以在其他工具中配置代理地址为 `http://localhost:8888` 或 `socks5://localhost:8888` 使用代理服务。

### 命令行参数

ProxyCat支持以下命令行参数：

```
-h, --help          显示帮助信息
-c, --config        指定配置文件路径
-p, --port          指定代理服务端口
-H, --host          指定代理服务监听地址
```

## 配置详解

### 主要配置项

| 配置项 | 说明 | 默认值 |
|-------|------|-------|
| listen_host | 代理服务监听地址 | 127.0.0.1 |
| listen_port | 代理服务监听端口 | 8888 |
| check_interval | 代理检查间隔（秒） | 30 |
| check_timeout | 代理检查超时时间（秒） | 5 |
| max_workers | 并发检查线程数 | 50 |
| proxy_rotation | 是否启用代理轮换 | True |
| rotation_interval | 代理轮换间隔（秒） | 60 |
| use_whitelist | 是否启用白名单 | False |
| use_blacklist | 是否启用黑名单 | False |

### 白名单和黑名单配置

在 `config/whitelist.txt` 和 `config/blacklist.txt` 文件中可以配置IP白名单和黑名单，每行一个IP地址。

## 免责申明

本工具仅用于学习和安全测试，请勿用于非法用途。使用本工具产生的一切后果由使用者自行承担。

## 更新日志

### v1.0
- 初始版本，实现基本的代理池功能
- 支持HTTP和SOCKS5代理协议
- 实现代理自动验证和轮换

### v1.1
- 增加白名单和黑名单功能
- 优化代理验证逻辑
- 增加性能监控功能

### v1.2
- 修复已知bug
- 优化命令行界面
- 增加配置项灵活性

## 开发计划

- [ ] 增加Web管理界面
- [ ] 支持更多代理协议
- [ ] 增加代理质量评估功能
- [ ] 实现自动获取代理功能
- [ ] 支持Docker部署

## 特别鸣谢

感谢所有为本项目做出贡献的开发者和用户！

## 赞助开源

如果您觉得本工具对您有帮助，欢迎赞助支持开源开发：

![赞助图片](assets/赞助.png)

## 代理推荐

以下是一些高性价比的代理服务提供商，供您参考：

- [XXX代理](https://example.com)：提供稳定的短效IP服务
- [YYY代理](https://example.com)：价格实惠，质量可靠
- [ZZZ代理](https://example.com)：支持多种代理类型