**代码模板**  
  
修改策略/指标为方便与本软件对接的代码，需要添加和修改以下代码


```
condition1 = false
condition2 = false
condition3 = false

//开多代码信号
plotshape(condition1, text='▲', style=shape.labeldown, textcolor=color.white, color = color.green,   location = location.abovebar, title = "开多")
alertcondition(condition1 , title="CrossOver Double EMA Buy", message="CrossOver Double EMA Buy")
//开空代码信号模板  
plotshape(condition2, text='▼', style=shape.labeldown, textcolor=color.white, color = color.red,   location = location.abovebar, title = "开空")
alertcondition(condition2  , title="CrossUnder Double EMA Sell", message="CrossUnder Double EMA Sell")
//平仓代码模板   
plotshape(condition3, text='Cancel', style=shape.labeldown, textcolor=color.white, color = color.red,   location = location.abovebar, title = "开空")
alertcondition(condition3  , title="CrossUnder Double EMA Sell", message="CrossUnder Double EMA Sell")
```  

以上的 `condition1 = false`  `condition2 = false`  `condition3 = false` 就是需要操作判断的代码。也是我们需要修改的片段，根据视频教程修改即可。
