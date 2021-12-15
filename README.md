# ouyi_trading_bot_for_tradingview

你是否想将TradingView交易策略做实盘运行但是苦于不会代码？这个程序就是让你即使不会写代码也能将TradingView策略实盘交易实现  
欧易交易所TradingView交易机器人接口服务，通过HTTP接口来对接TradingView交易策略和交易指标，实现TradingView策略自动交易  
  
**它是如何工作的**  

![image](https://user-images.githubusercontent.com/94948670/143181162-54d46868-d4cd-4f1f-bbc4-a5836f0c1f5d.png)  
要实现自动交易，我们需要做的工作就是：  
1.稍微小改一下TradingView的交易策略代码，这一部分很简单，人人都能学会，我的Youtube频道和B站频道会教大家如何修改  
2.我们需要一台海外服务器来运行这个软件，不建议使用个人电脑，因为不稳定，而且一般没有外网IP。具体如何部署请看我的另一个视频和文章 如何在服务器上运行这个软件
  
**写在前面**  
1.只支持欧易交易所，目前不支持币安binance，因为欧易可以继续为国内用户服务，没注册过的可以通过这里注册：http://okex.pw/20off  享受二折手续费优惠，别小看这二折优惠，在量化交易中累积起来是很恐怖的  
2.目前建议使用合约交易，使用一倍杠杆就和现货一样了  
3.此脚本仅作学习使用，请勿

**使用方法**  
方法一(推荐！适合新手小白不会写程序的)：直接使用我这里写好的UI界面程序，在本页面找到“Release”下载Configer程序即可。[前往查看使用说明>>](https://github.com/blockplusim/crypto_trading_service_for_tradingview/blob/main/okex_trading_ui_guide.md)  
方法二(适合有Python开发经验的)：在Python环境中直接运行本`Okex_trading.py`程序。[前往查看使用说明>>](https://github.com/blockplusim/crypto_trading_service_for_tradingview/blob/main/okex_trading_guide.md)  

**使用流程**  
1.在你的服务器上运行这个程序，可以在本页面的 release 中直接下载 exe 程序，将程序所有文件放到你的海外Windows服务器上解压  
2.解压出来后，我们需要修改 ***config.ini***  文件。该文件包含以下内容  
```ini
[account]
apiKey = 
secret = 
password = 
enable_proxies = False
proxies = 

[trading]
symbol = TRX-USDT-SWAP
amount = 1
tdMode = isolated
lever = 5

[service]
apiSec = 5BFJYtNg7hwkgCzYQMwwQNctqan9CmqOzmtldJc
listenHost = 0.0.0.0
listenPort = 80
debugMode = True
ipWhiteList = 52.89.214.238,34.212.75.30,54.218.53.128,52.32.178.7,127.0.0.1
```  
  
**[account]** 节点主要配置欧易交易所的API信息  
apiKey、secret和password可以在欧易个人中心的API中创建（创建API记得给予交易和读取权限，不要给提现的权限），enable_proxies是是否启用代理的意思，如果你的服务器是国内服务器，一般需要启用，启用填写True，proxies填写具体的代理地址，如：http://127.0.0.1:1080  所以建议使用海外服务器来运行这个程序  
  
**[trading]** 交易API的默认配置  
**symbol**：交易对，比特币BTC/USDT永续合约就是 BTC-USDT-SWAP 其他币也类似，不知道这个怎么设置的话，可以打开电脑版欧易，打开 交易 -> 基础交易 -> 切换你要交易的币对 -> 浏览器地址栏最后面就有交易对信息  
**amount**：交易的数量，币的个数。注意这里统一使用币来计价，比如你开BTC，那么这里就是开BTC的数量  
**lever**：默认杠杆倍数，如果 /order 请求中带有这个参数，系统会根据lever重新修改杠杆倍数  
**tdMode**：保证金模式，isolated：逐仓 ；cross：全仓

**[service]** 服务配置  
**apiSec**：通信密钥，这个一定要修改，随便改长一点复杂一点就行了  
**listenHost**: 服务监听地址，一般默认即可  
**listenPort**：服务监听端口，一般80即可，注意 TradingView 只支持80和443  
**debugMode**：True或者False，开启debug模式的话日志输出会更详细  
**ipWhiteList**：授权使用本服务接口的IP地址集合，每个IP地址用英文逗号 **,** 隔开，这里默认前面四个地址是 TradingView 的官方地址  


**运行环境**  
Python 3.6.10  
ccxt 1.56.41  
flask 1.1.2  

**如何运行**  
修改玩config.ini中的配置后，直接使用 `python okex_trading.py` 启动即可 
