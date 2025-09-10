<div align="center">
  <h1>fir-proxy</h1>
  <p><strong>一个高可用的 HTTP/SOCKS5 代理池，具有强大的图形化界面和多种代理获取方式。</strong></p>
  <p>
   
  </p>
</div>

<hr/><h3 align="center">最好是导入可用代理哦,里面都是稳定的,且速度比较快的代理</h3>

<h2 align="center"> ✨ 项目特点 </h2>

<table border="0" cellpadding="10" cellspacing="0" width="100%">
  <tr valign="top">
    <td width="50%">
      <ul>
        <li><b>图形化界面</b>：基于 ttkbootstrap 的现代化图形界面，操作直观。</li>
        <li><b>多种代理源</b>：支持从在线API、网页抓取、本地文件等多种方式获取。</li>
        <li><b>高质量验证</b>：通过延迟、速度和国际连通性测试，确保代理真实可用。</li>
      </ul>
    </td>
    <td width="50%">
      <ul>
        <li><b>双协议服务</b>：一键启动本地 HTTP (127.0.0.1:1801) 和 SOCKS5 (127.0.0.1:1800) 服务。</li>
        <li><b>智能轮换与筛选</b>：支持按区域、质量筛选代理，并可按设定时间自动轮换IP。</li>
        <li><b>丰富的管理功能</b>：支持导出、复制、删除和全部重新测试等多种管理操作。</li>
      </ul>
    </td>
  </tr>
</table>

<hr/>

<h2 align="center"> 📸 界面截图 </h2>
<img src="img/代理池.png">
<p align="center">
  
</p>

<hr/>

<h2 align="center"> 🚀 快速开始 </h2>

<div align="center">
  <p><strong>环境要求:</strong> Python 3.10 或更高版本。</p>
</div>

<ol>
  <li>
    <strong>克隆或下载项目</strong>
<pre><code>git clone https://github.com/your-username/fir-proxy.git
cd fir-proxy</code></pre>
  </li>
  <li>
    <strong>安装依赖</strong>
<pre><code>pip install -r requirements.txt</code></pre>
  </li>
  <li>
    <strong>运行主程序</strong>
<pre><code>python main.py</code></pre>
  </li>
</ol>

<hr/>

<h2 align="center"> 📖 使用指南 </h2>

<h3 align="left">图形化界面 (main.py)</h3>

<ul>
  <li><b>获取代理</b>：
    <ul>
      <li><b>在线获取</b>：点击 <b>[获取在线代理]</b> 或者右键点击使用代理按钮，程序将自动从多个源抓取并验证。</li>
      <li><b>本地导入</b>：点击 <b>[导入代理]</b> 按钮，选择本地的 <code>.txt</code> 或 <code>.json</code> 文件。(建议选择导入可用代理里面的,里面的代理速度快且延迟也比较低)</li>
    </ul>
  </li>
  <br/>
  <li><b>使用代理</b>：
    <ul>
      <li>点击 <b>[启动服务]</b> 按钮，开启本地 <code>127.0.0.1:1801 (HTTP)</code> 和 <code>127.0.0.1:1800 (SOCKS5)</code> 端口。</li>
      <li>在需要代理的软件中配置上述地址即可。</li>
    </ul>
  </li>
  <br/>
  <li><b>IP 轮换</b>：
    <ul>
      <li><b>手动</b>：点击 <b>[轮换IP]</b> 立即切换。</li>
      <li><b>自动</b>：点击 <b>[自动]</b> 并设置秒数，程序将按时自动切换。</li>
    </ul>
  </li>
</ul>

<h3 align="left">独立命令行脚本 (hq.py / xdl.py)</h3>
<p>这两个脚本适合在服务器等无图形界面的环境下快速获取代理。</p>

<ul>
  <li><b>使用方法</b>：</li>
</ul>
<p><i># 运行智能模式脚本 (代理数量多,大约有30多w)</i></p>
<pre><code>python hq.py</code></pre>

<p><i># 运行快速模式脚本 (代理速度快,大约有1w左右)</i></p>
<pre><code>python xdl.py</code></pre>

<h3 align="left">脚本启动工具</h3>
<p>为了方便使用，项目提供了多个启动脚本：</p>
<ul>
  <li><b>start_fir_proxy.py</b>：标准启动脚本</li>
  <li><b>start_fir_proxy_simple.py</b>：简化版启动脚本</li>
  <li><b>start_fir_proxy_fixed.py</b>：修复路径问题的启动脚本</li>
  <li><b>run_fir_proxy_cli.py</b>：命令行版本启动脚本</li>
</ul>

<hr/>

<h2 align="center"> 🛠️ 项目结构 </h2>

<pre>
fir-proxy/
├── main.py             # 主程序入口（图形界面版）
├── hq.py               # 命令行版 - 智能模式
├── xdl.py              # 命令行版 - 快速模式
├── config.json         # 配置文件
├── requirements.txt    # 依赖清单
├── 可用代理.txt        # 示例代理文件
├── 可用代理2.txt       # 示例代理文件
└── modules/            # 核心模块
    ├── fetcher.py      # 代理获取模块
    ├── checker.py      # 代理验证模块
    ├── server.py       # 代理服务模块
    └── rotator.py      # 代理轮换模块
</pre>

<hr/>

<h2 align="center"> 📝 配置说明 </h2>

<p>在 <code>config.json</code> 文件中可以自定义以下配置：</p>

<pre><code>{
  "http_port": 1801,              # HTTP代理服务端口
  "socks5_port": 1800,            # SOCKS5代理服务端口
  "check_timeout": 5,             # 代理验证超时时间(秒)
  "max_workers": 100,             # 最大线程数
  "auto_rotate_interval": 60,     # 自动轮换时间间隔(秒)
  "api_sources": [                # 在线代理API源
    "https://api.proxy.example.com",
    "https://another.proxy.source"
  ]
}</code></pre>

<hr/>

<h2 align="center"> ⚠️ 注意事项 </h2>

<ul>
  <li>本工具仅用于学习和研究目的，请遵守相关法律法规。</li>
  <li>使用过程中，如遇到代理失效问题，请尝试重新获取或导入新的代理。</li>
  <li>大量请求可能会导致目标网站限制访问，请合理使用。</li>
  <li>如需长期稳定使用，建议定期更新代理列表。</li>
</ul>

<hr/>

<h2 align="center"> 🤝 贡献指南 </h2>

<p>欢迎对本项目进行贡献！您可以通过以下方式参与：</p>

<ol>
  <li>Fork 本仓库</li>
  <li>创建您的特性分支 (<code>git checkout -b feature/AmazingFeature</code>)</li>
  <li>提交您的更改 (<code>git commit -m 'Add some AmazingFeature'</code>)</li>
  <li>推送到分支 (<code>git push origin feature/AmazingFeature</code>)</li>
  <li>开启 Pull Request</li>
</ol>

<hr/>

<h2 align="center"> 📄 许可证 </h2>

<p>本项目采用 MIT 许可证 - 查看 <a href="LICENSE">LICENSE</a> 文件了解详情。