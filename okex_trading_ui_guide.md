## okex_trading_ui 使用说明  
预编译好且带有操作界面的程序，操作比较简单，适合新手小白

**使用前准备**  
1.需要准备一个欧易OKEX交易所账号，如果你还没有注册，请先[注册一个账号](https://www.ouyicn.group/join/GITHUB)，然后到账号API申请V5API，备注名称随意，权限需要选择只读和交易，不要勾选提现！然后确认添加即可  
2.你需要购买一台海外的服务器用于24小时自动运行这个自动交易程序，可以选择腾讯云轻量应用服务器香港等东亚地区的服务器（注意必须买海外的，推荐香港服务器，因为OKX服务在香港，这样速度快点），可查看[腾讯轻量服务器教程](https://www.bilibili.com/video/BV1VP4y1H71e?spm_id_from=333.999.0.0)  
  
**需要注意的东西**  
1.开始跑策略对接这个软件之前，务必清空你再这个币种的现有仓位，以免导致管理混乱    
2.支持同时跑多个策略和多个币种的，但是一个币种只能同时跑一个策略，不要同时一个币跑多个币种，必然会管理混乱  
3.如果在软件运行过程中，你手动去管理你的这个策略仓位，可能导致数据不一致，这时候你应该在软件界面停止服务再启动服务才可以  
4.请注意，如果启动后发现没有下单成功，可以登录OKEX电脑版，交易界面，右边有个设置，把 `下单模式` 改为 `买卖模式`   
  
**使用步骤**  
1.在服务器上下载程序，从 `release` 中下载 `okex_trading_ui` 程序并解压到服务器上。[服务器上打开这个链接下载](https://github.com/blockplusim/crypto_trading_service_for_tradingview/releases)  
2.下载完成以后解压，直接双击打开 `configurator.exe` 界面如下：  

<img src="https://user-images.githubusercontent.com/94948670/157452366-b8aaffc9-87ae-43d7-bc44-0477336e536d.png" alt="" width="60%" height="40%" />  
  
在上面的界面中，我们看到需要用到三个参数 apiKey / secret / password 。这三个参数我们可以在欧易OKEX个人中心中API中申请V5API中获取，然后把三个参数复制过来。如果你用的是香港或者其他海外服务器，那么启用代理这个不需要勾选  
  
<img src="https://user-images.githubusercontent.com/94948670/146110819-1b3a1ea5-39df-4fd7-8a98-35d7ca0763a0.png" alt="" width="70%" height="70%" />  
  
下一步我们配置交易相关信息，这里的防止重复下单意思是不允许重复下单，也就是不允许金字塔加仓模式的，如果允许加仓，就不要勾选防止重复下单  
  
<img src="https://user-images.githubusercontent.com/94948670/157452612-e7b12e59-3518-4dc1-9133-3e7a955550fc.png" alt="" width="60%" height="40%" />  
  
下一步在服务配置这边，一般需要修改 `通信密钥` 和 `外网IP`， 这里通信密钥就是一个简单的密码，用于验证身份；外网IP就是你运行这个软件的服务器的IP地址。我们在TradingView调用的时候需要用到  
  
<img src="https://user-images.githubusercontent.com/94948670/157452927-a67bda7e-4d30-418c-a45d-1db5091946b3.png" alt="" width="60%" height="40%" />  
  
配置完成后，点击 `保存配置`，然后再点击 `启动服务` 即可，然后点击 `查看日志` 可以看到运行的情况  
  
<img src="https://user-images.githubusercontent.com/94948670/157453563-7c79d750-7e83-4e23-8941-2e207121c5d2.png" alt="" width="60%" height="40%" />  

这个启动完成后，我们就可以对接 `TradingView` 来实现自动交易了  
  
<img src="https://user-images.githubusercontent.com/94948670/146113041-85c79ee7-4917-4953-9f07-17a86e023ee9.png" alt="" width="100%" height="100%" />  
  
在香港服务器上运行成功界面如上图所示
  
当我们运行成功后，下一步需要和TradingView进行对接
  
点击 `警报生成` 选项来生成TradingView对接信息
  
<img src="https://user-images.githubusercontent.com/94948670/157454834-83a584bb-c06c-48fc-a6b5-f03e6f2a09a9.png" alt="" width="60%" height="100%" />  
  
这里有四个选项，分别是 `做多`、`做空`、`市价平仓`和`取消挂单`，我们可以根据TradingView的代码需求进行对接，点击 `生成TradingView告警配置` 生成如下信息
  
<img src="https://user-images.githubusercontent.com/94948670/157455288-2d244acb-6fba-4071-8cab-1ae97cff9cf3.png" alt="" width="60%" height="100%" /> 
  
将对应的信息粘贴到TradingView配置项即可
  
<img src="https://user-images.githubusercontent.com/94948670/157455696-cd957f17-f6c1-467d-a54f-d5bb05c708df.png" alt="" width="100%" height="100%" /> 
