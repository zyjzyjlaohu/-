@echo off

rem 设置中文编码
chcp 65001 >nul

rem 确保中文显示正常
setshell="%comspec%" /c chcp 65001

rem 设置脚本标题
title 增强版代理收集工具

rem 启动界面
cls
echo.          ==========================================================
echo.                          增强版代理收集工具启动器                          
echo.          ==========================================================
echo.
echo.  欢迎使用增强版代理收集工具，本工具可以自动从多个渠道收集代理并验证有效性
echo.  功能特点：
echo.  - 使用Fofa API搜索代理服务器
echo.  - 批量检查端口开放情况
echo.  - 多线程验证代理有效性

echo.
echo 正在检查Python环境...
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo 错误: 未找到Python环境，请先安装Python。
    echo 访问 https://www.python.org/downloads/ 下载并安装Python
    pause
    exit /b 1
)

echo 正在检查增强版代理收集工具文件...
if not exist "enhanced_proxy_collector.py" (
    echo 错误: 未找到enhanced_proxy_collector.py文件，请确保在正确的目录下运行。
    pause
    exit /b 1
)

echo 正在检查配置文件...
if not exist "user.txt" (
    echo 警告: 未找到user.txt文件，将使用默认用户名列表
    echo test>user.txt
    echo guest>>user.txt
)

if not exist "pass.txt" (
    echo 警告: 未找到pass.txt文件，将使用默认密码列表
    echo 123456>pass.txt
    echo 12345678>>pass.txt
    echo password>>pass.txt
    echo admin123>>pass.txt
)

echo.
echo ========== 系统信息 ==========
echo 当前目录: %cd%
echo 脚本名称: %~nx0
echo Python版本: 
python --version
echo =============================
echo.

:start_menu
cls
echo          ==========================================================
echo.                          增强版代理收集工具                          
echo.          ==========================================================
echo.
echo 请选择操作：
echo [1] 开始收集代理
echo [2] 查看已收集的代理

echo [3] 清空所有结果文件
echo [4] 查看帮助信息
echo [0] 退出程序

echo.
set /p choice=请输入选择 [0-4]: 

if %choice% equ 1 goto start_collection
if %choice% equ 2 goto view_results
if %choice% equ 3 goto clear_results
if %choice% equ 4 goto show_help
if %choice% equ 0 goto exit_program

echo 无效的选择，请重新输入。
pause
goto start_menu

:start_collection
cls
echo ========== 开始收集代理 ==========
echo 正在启动增强版代理收集工具...
echo 这可能需要一些时间，请耐心等待...
echo =================================

rem 启动主程序
python enhanced_proxy_collector.py

if %errorlevel% neq 0 (
    echo 错误: 程序执行失败，请检查错误信息。
) else (
    echo 程序执行成功！
)

pause
goto start_menu

:view_results
cls
echo ========== 查看已收集的代理 ==========

if exist "enhanced_valid_proxies.txt" (
    echo 有效代理列表（enhanced_valid_proxies.txt）：
    echo =======================================
    type enhanced_valid_proxies.txt | more
    echo =======================================
    for /f %%i in ('find /v /c "" ^< enhanced_valid_proxies.txt') do set valid_count=%%i
    echo 有效代理总数: %valid_count%
) else (
    echo 尚未收集到有效代理，请先执行收集操作。
)

if exist "enhanced_fofa_results.txt" (
    for /f %%i in ('find /v /c "" ^< enhanced_fofa_results.txt') do set fofa_count=%%i
    echo Fofa搜索结果总数: %fofa_count%
)

if exist "enhanced_open_ports.txt" (
    for /f %%i in ('find /v /c "" ^< enhanced_open_ports.txt') do set port_count=%%i
    echo 开放端口总数: %port_count%
)

echo =======================================
pause
goto start_menu

:clear_results
cls
echo ========== 清空所有结果文件 ==========
echo 警告：此操作将清空所有已收集的代理结果！
echo 是否确认执行？
echo [Y] 确认清空
[其他] 取消操作

echo.
set /p confirm=请输入选择: 

if /i "%confirm%" equ "Y" (
    if exist "enhanced_fofa_results.txt" del "enhanced_fofa_results.txt"
    if exist "enhanced_open_ports.txt" del "enhanced_open_ports.txt"
    if exist "enhanced_valid_proxies.txt" del "enhanced_valid_proxies.txt"
    echo 所有结果文件已清空。
) else (
    echo 操作已取消。
)

pause
goto start_menu

:show_help
cls
echo ========== 帮助信息 ==========
echo 增强版代理收集工具使用指南
echo ===========================
echo.
echo 本工具用于自动收集和验证代理服务器，主要功能包括：
echo.
echo 1. 使用Fofa API搜索潜在的代理服务器
 echo 2. 批量检查端口开放情况
 echo 3. 多线程验证代理的有效性
 echo 4. 将结果保存到不同的文件中
 echo.
 echo 使用说明：
 echo - 确保已安装Python环境
 echo - 在运行工具前，确保user.txt和pass.txt文件存在
 echo - 工具会自动搜索、验证并保存代理
 echo - 可以通过主菜单查看结果或清空数据
 echo.
 echo 配置说明：
 echo - 可以在enhanced_proxy_collector.py中修改配置参数
 echo - 包括Fofa API凭证、线程数、超时时间等
 echo - 可以自定义扫描端口列表
 echo.
 echo 输出文件：
 echo - enhanced_fofa_results.txt: Fofa搜索结果
 echo - enhanced_open_ports.txt: 开放端口列表
 echo - enhanced_valid_proxies.txt: 有效代理列表
 echo.
 echo 注意事项：
 echo - 使用前请确保有有效的Fofa API凭证
 echo - 大量请求可能会消耗Fofa API的调用额度
 echo - 建议合理设置线程数，避免系统资源占用过高
 echo ===========================
 pause
 goto start_menu

 :exit_program
 cls
 echo 感谢使用增强版代理收集工具，再见！
 pause
 exit /b 0