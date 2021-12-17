## okex_trading.py 使用指南  
适用于有python使用经验的朋友，因为只是一个python脚本  

**使用流程**  
1.购买海外服务器，注意必须是中国大陆以外的，因为许多交易所目前大陆IP无法连接和交易  
2.安装 Python3.6 环境，安装必备的包：ccxt flask 等  
3.我们需要修改 ***config.ini***  文件。该文件包含以下内容   

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
