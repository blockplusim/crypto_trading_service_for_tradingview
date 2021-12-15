## okex_trading_ui 使用说明  
预编译好且带有操作界面的程序，操作比较简单，适合新手小白

**使用前准备**  
1.需要准备一个欧易OKEX交易所账号，如果你还没有注册，请先[注册一个账号](http://okex.pw/tvbot)，然后到账号API申请V5API，备注名称随意，权限需要选择只读和交易，不要勾选提现！然后确认添加即可  
2.你需要购买一台海外的服务器用于24小时自动运行这个自动交易程序，可以选择腾讯云轻量应用服务器香港等东亚地区的服务器（注意必须买海外的，推荐香港），可查看[腾讯轻量服务器教程](https://cloud.tencent.com/document/product/1207/44549)  

**使用步骤**  
1.在服务器上下载程序，从 `release` 中下载 `okex_trading_ui` 程序并解压到服务器上。[服务器上打开这个链接下载](https://github.com/blockplusim/crypto_trading_service_for_tradingview/releases)  
2.下载完成以后解压，直接双击打开 `okex_trading_ui.exe` 界面如下：  
  
<img src="https://user-images.githubusercontent.com/94948670/146109501-70f09b0d-59c2-4690-8993-64c33d823d0f.png" alt="" width="40%" height="40%" />  
  
在上面的界面中，我们看到需要用到三个参数 apiKey / secret / password 。这三个参数我们可以在欧易OKEX个人中心中API中申请V5API中获取，然后把三个参数复制过来  
  
<img src="https://user-images.githubusercontent.com/94948670/146110819-1b3a1ea5-39df-4fd7-8a98-35d7ca0763a0.png" alt="" width="70%" height="70%" />  
  
下一步我们配置交易相关信息  
  
<img src="https://user-images.githubusercontent.com/94948670/146111099-c4fc3341-038d-48c3-a80b-55a95647d638.png" alt="" width="40%" height="40%" />  
  
下一步在服务配置这边，一般需要修改 `通信密钥`， 这里就是一个简单的密码，用于验证身份。我们在TradingView调用的时候需要用到  
  
<img src="https://user-images.githubusercontent.com/94948670/146111335-9842154a-3f0b-48d2-8cf1-a8d9ba5d6a02.png" alt="" width="40%" height="40%" />  
  
配置完成后，点击 `保存配置`，然后再点击 `启动服务` 即可  
  
<img src="https://user-images.githubusercontent.com/94948670/146111551-c7a011f0-82fc-4e07-bdec-0989aa1b46ec.png" alt="" width="40%" height="40%" />  

这个启动完成后，我们就可以对接 `TradingView` 来实现自动交易了
