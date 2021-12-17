**策略改为自动化交易的信号指标流程**  
  
**步骤一：选好交易币种/交易对，选好K线时间段**  
  
如下图，首先点击这里选币
  
![image](https://user-images.githubusercontent.com/94948670/146497787-fef88716-4083-464b-b0bc-0a92fc522d7e.png)  
  
比如我们要用BTCUSDT然后选OKEX的是数据源，注意我们软件用OKEX，所以数据源一定要选OKEX，如果用合约，数据源最好也选对应的合约数据源，根据下图选取即可  
  
![image](https://user-images.githubusercontent.com/94948670/146497914-8540a4ef-f6c2-4505-a26c-0356f70fa99e.png)  
  
选择K线周期，以4小时为例  
  
![image](https://user-images.githubusercontent.com/94948670/146497979-22a8b2e0-0a66-4d9f-b64f-b2f6ea09ff1e.png)  
  
  
**步骤二：修改策略为指标**  
  
选定我们需要修改的策略，我们演示用MACD策略，记住这个名字 `MACD Strategy`，点击代码，查看策略代码  
  
![image](https://user-images.githubusercontent.com/94948670/146494270-a225e2c1-580f-43da-9d6a-25293bc7166f.png)  
  
出现这个代码窗口，点击解锁，然后可以改名，也可以直接点保存  
  
![image](https://user-images.githubusercontent.com/94948670/146494374-5fdc540e-f9a3-40f9-b732-54df4b821185.png)  
  
修改这一行代码，把strategy改为indicator。其他参数可不改  
  
![image](https://user-images.githubusercontent.com/94948670/146494482-3d5104f4-a362-479f-912a-dea3bd00f8a4.png)  
  
复制以下代码模板粘贴到代码窗口代码最下面  
  
```
condition1 = false
condition2 = false
condition3 = false

//开多代码信号
plotshape(condition1, text='▲', style=shape.labeldown, textcolor=color.white, color = color.green,   location = location.abovebar, title = "开多")
alertcondition(condition1 , title="Buy", message="Buy")
//开空代码信号  
plotshape(condition2, text='▼', style=shape.labeldown, textcolor=color.white, color = color.red,   location = location.abovebar, title = "开空")
alertcondition(condition2  , title="Sell", message="Sell")
//平仓代码信号  
alertcondition(condition3  , title="Cancel", message="Cancel")
```  
  
以上的 `condition1 = false`  `condition2 = false`  `condition3 = false` 就是需要操作判断的代码。也是我们需要修改的片段，根据视频教程修改即可。粘贴后的代码如下    
  
![image](https://user-images.githubusercontent.com/94948670/146494888-7a899348-178e-43bb-985e-06fca1454eee.png)  
  
接下来我们需要修改触发条件  
  
![image](https://user-images.githubusercontent.com/94948670/146495044-b86d9e2c-236a-4b07-9eeb-ed75715bf073.png)  
  
其他的不需要修改，接着我们把TradingView策略的代码用“//”注释掉，选中图中代码注释按CTRL+/键即可（注释的意思就是让所注释的代码失效，不执行功能）  
  
![image](https://user-images.githubusercontent.com/94948670/146495403-7dab9953-20e5-4848-929d-a60b51b43133.png)  
  
接下来就是保存代码并且添加到图表  
  
![image](https://user-images.githubusercontent.com/94948670/146495638-b0c816a2-59cc-479a-bd3b-673306fb135a.png)  
  
下一步我们就可以在图表中看到做多或者做空信号了，如下图所示  
  
![image](https://user-images.githubusercontent.com/94948670/146495782-07a4cc63-a29c-49fe-baa3-dd8f3a261f90.png)  
  
**步骤三：添加交易通知**  
  
接下来我们根据做多和做空信号通知提醒我们的服务器来实现策略自动下单，点击右上角这边的时钟图标   
  
![image](https://user-images.githubusercontent.com/94948670/146495922-68ea6800-a758-4b3f-8efd-a9272a43dfa9.png)  
  
接下来选择要设置交易提醒的条件，选择我们的策略 `MACD Strategy`，展开第二行的选项，有 Buy、 Sell 和 Cancel三个选项，这就是买入、卖出和取消信号。我们先选择一个 Buy 信号吧，Options选择Once Per Bar Close  

![image](https://user-images.githubusercontent.com/94948670/146496279-06c88f6f-ad15-44c3-b1a4-ef2226875d0c.png)  
  
接下来添加通知服务器的地址，勾选 `WebHook URL`，可以参考我这个地址，把IP地址换位你的腾讯云服务器IP地址即可  
  
![image](https://user-images.githubusercontent.com/94948670/146496959-6ac18d6d-0e99-4d8a-ae24-064eee449cb0.png)  
  

复制下面的 `TradingView通知参数模板` 到消息框(message)。

```
{
	"symbol": "SHIB-USDT-SWAP",
	"price": {{close}},
	"amount": "1000000",
	"side": "buy",
	"ordType": "limit",
	"apiSec": "5BFJYtNg7hwkgCzYQMwwQNctqan9CmqOzmtldJc"
}
```  
以上内容可能需要改动，怎么改可以看视频
symbol是交易对，可以从OKEX的官网地址栏或者，详见视频说明。  
price是挂单的价格，一般用{{close}}就是收盘价，还有 open(开盘价) / high(最高价) /low(最低价) 等  
amount就是挂单的数量，统一用币的单位计算，比如0.1个比特币就填0.1，1000000个shib就用1000000  
side就是挂单方向，有四种取值。sell -> 开空（如果有仓位会先平掉）；buy -> 开多（如果有仓位会先平掉）；close -> 平仓 ；cancel -> 取消所有未成交的挂单    
ordType挂单类型，可以是limit限价单，或者是market市价单，使用市价market的话price会失效  
apiSec是我们再软件服务配置页面中设置的通信密钥参数。  

复制以上代价粘贴进message  
  
![image](https://user-images.githubusercontent.com/94948670/146497227-d64b399d-e7cc-4828-9d71-7eb271e5a03e.png)  
  
继续点击create(创建)即可。然后重复第三步，但是这次要设置卖出信号源，因为买入的已经设置好了。  
设置完成以后即可自动通知交易  
更多信息看我的视频（油管/bilibili：区块普拉斯）

