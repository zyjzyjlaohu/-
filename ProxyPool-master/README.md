# ProxyPool

![build](https://github.com/Python3WebSpider/ProxyPool/workflows/build/badge.svg)
![deploy](https://github.com/Python3WebSpider/ProxyPool/workflows/deploy/badge.svg)
![](https://img.shields.io/badge/python-3.6%2B-brightgreen)
![Docker Pulls](https://img.shields.io/docker/pulls/germey/proxypool)

简易高效的代理池，提供如下功能：

- 定时抓取免费代理网站，简易可扩展。
- 使用 Redis 对代理进行存储并对代理可用性进行排序。
- 定时测试和筛选，剔除不可用代理，留下可用代理。
- 提供代理 API，随机取用测试通过的可用代理。

代理池原理解析可见「[如何搭建一个高效的代理池](https://cuiqingcai.com/7048.html)」，建议使用之前阅读。

## 使用前注意

本代理池是基于市面上各种公开代理源搭建的，所以可用性并不高，很可能上百上千个代理中才能找到一两个可用代理，不适合直接用于爬虫爬取任务。

如果您的目的是为了尽快使用代理完成爬取任务，建议您对接一些付费代理或者直接使用已有代理资源；如果您的目的是为了学习如何搭建一个代理池，您可以参考本项目继续完成后续步骤。

付费代理推荐：

- [ADSL 拨号代理](https://platform.acedata.cloud/documents/a82a528a-8e32-4c4c-a9d0-a21be7c9ef8c)：海量拨号（中国境内）高质量代理
- [海外/全球代理](https://platform.acedata.cloud/documents/50f1437a-1857-43c5-85cf-5800ae1b31e4)：中国境外高质量代理
- [蜂窝 4G/5G 代理](https://platform.acedata.cloud/documents/1cc59b19-1550-4169-a59d-ad6faf7f7517)：极高质量（中国境内）防风控代理

## 使用准备

### 安装 Docker

推荐使用 Docker 部署，避免环境配置问题。首先安装 Docker：

- [Windows Docker 安装](https://docs.docker.com/docker-for-windows/install/)
- [macOS Docker 安装](https://docs.docker.com/docker-for-mac/install/)
- [Linux Docker 安装](https://docs.docker.com/engine/install/)

### 克隆项目

```bash
git clone https://github.com/Python3WebSpider/ProxyPool.git
cd ProxyPool
```

## Docker 部署

### 快速启动

```bash
docker-compose up -d
```

这样就可以启动代理池了，其中包含了 Redis 和代理池服务。

### 访问代理

代理池启动后，可以通过以下 API 访问：

- 获取随机代理：`http://localhost:5555/random`
- 获取代理数量：`http://localhost:5555/count`

### 自定义配置

如果需要自定义配置，可以修改 `config.json` 文件，然后重新启动容器：

```bash
docker-compose down
docker-compose up -d
```

## 本地部署

### 安装 Redis

首先需要安装 Redis 并启动：

- [Windows Redis 安装](https://github.com/microsoftarchive/redis/releases)
- [macOS Redis 安装](https://redis.io/download#installation-installing-redis-on-macos)
- [Linux Redis 安装](https://redis.io/download#installation-installing-redis-on-linux)

### 安装依赖

```bash
pip install -r requirements.txt
```

### 修改配置

修改 `config.json` 文件，配置 Redis 连接信息：

```json
{
    "HOST": "localhost",
    "PORT": 6379,
    "PASSWORD": "",
    "DB": 0
}
```

### 启动代理池

```bash
python run.py
```

## 项目结构

```
ProxyPool/
├── proxypool/
│   ├── crawlers/            # 爬虫模块，负责抓取代理
│   │   ├── public/          # 公开代理爬虫
│   │   └── private/         # 私有代理爬虫
│   ├── processors/          # 处理器模块
│   │   ├── getter.py        # 获取器，负责从爬虫获取代理
│   │   ├── server.py        # 服务器，提供 API 接口
│   │   └── tester.py        # 测试器，负责测试代理可用性
│   ├── storages/            # 存储模块
│   │   └── redis.py         # Redis 存储实现
│   ├── testers/             # 测试模块
│   ├── utils/               # 工具模块
│   ├── __init__.py          # 初始化文件
│   ├── scheduler.py         # 调度器
│   └── setting.py           # 设置文件
├── config.json              # 配置文件
├── requirements.txt         # 依赖文件
└── run.py                   # 运行入口
```

## API 接口

代理池提供了以下 API 接口：

### 获取随机代理

```
GET http://localhost:5555/random
```

返回格式：

```
127.0.0.1:8080
```

### 获取代理数量

```
GET http://localhost:5555/count
```

返回格式：

```
{
    "count": 100
}
```

### 获取所有代理

```
GET http://localhost:5555/all
```

返回格式：

```
[
    "127.0.0.1:8080",
    "127.0.0.1:8081",
    ...
]
```

## 自定义爬虫

如果需要添加自定义爬虫，只需要在 `proxypool/crawlers/public` 目录下创建一个新的 Python 文件，然后实现一个继承自 `BaseCrawler` 的类，并实现 `crawl` 方法即可。

例如：

```python
from proxypool.crawlers.base import BaseCrawler
from proxypool.schemas.proxy import Proxy

class MyCrawler(BaseCrawler):
    urls = ['https://example.com/proxies']
    
    def crawl(self):
        for url in self.urls:
            response = self.get(url)
            # 解析 response 并提取代理
            proxies = self.parse(response.text)
            for proxy in proxies:
                yield Proxy(host=proxy['host'], port=proxy['port'])
```

## 常见问题

### Redis 连接失败

请检查 Redis 是否启动，以及 `config.json` 中的连接信息是否正确。

### 代理不可用

免费代理的可用性本来就不高，如果需要高可用的代理，建议使用付费代理。

### API 访问失败

请检查代理池服务是否正常运行，可以通过 `docker logs proxypool` 查看日志。

## License

MIT