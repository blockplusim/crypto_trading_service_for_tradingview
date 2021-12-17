# ouyi_trading_bot_for_tradingview

你是否想将TradingView交易策略做实盘运行但是苦于不会代码？这个程序就是让你即使不会写代码也能将TradingView策略实盘交易实现  
欧易交易所TradingView交易机器人接口服务，通过HTTP接口来对接TradingView交易策略和交易指标，实现TradingView策略自动交易  
  
**它是如何工作的**  

![image](https://user-images.githubusercontent.com/94948670/143181162-54d46868-d4cd-4f1f-bbc4-a5836f0c1f5d.png)  
要实现自动交易，我们需要做的工作就是：  
1.稍微小改一下TradingView的交易策略代码，这一部分很简单，人人都能学会，我的Youtube频道和B站频道会教大家如何修改  
2.我们需要一台海外服务器来运行这个软件，不建议使用个人电脑，因为不稳定，而且一般没有外网IP。具体如何部署请看我的另一个视频和文章 如何在服务器上运行这个软件
  
**写在前面**  
1.只支持欧易交易所，目前不支持币安binance，因为欧易可以继续为国内用户服务，没注册过的可以通过这里注册：http://okex.pw/20off  享受20%手续费优惠，别小看这20%的优惠(之前口误了)，在量化交易中累积起来是很恐怖的  
2.目前建议使用合约交易，使用一倍杠杆就和现货一样了  
3.此脚本仅作学习使用，抛砖引玉，希望大家从这里得到启发，写出更好的东西

**使用方法**  
方法一(推荐！适合新手小白不会写程序的)：直接使用我这里写好的UI界面程序，在本页面找到“Release”下载Configer程序即可。[前往查看使用说明>>](https://github.com/blockplusim/crypto_trading_service_for_tradingview/blob/main/okex_trading_ui_guide.md)  
方法二(适合有Python开发经验的)：在Python环境中直接运行本`Okex_trading.py`程序。[前往查看使用说明>>](https://github.com/blockplusim/crypto_trading_service_for_tradingview/blob/main/okex_trading_guide.md)  

**视频教程**  
Youtube教程：https://youtu.be/UEYo3aVgtjQ  
Bilibili教程：https://www.bilibili.com/video/BV1aF411z7tM/
