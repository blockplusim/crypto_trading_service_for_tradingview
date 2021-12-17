**常用代码模板**  
  
开多代码信号模板  
```
plotshape(condition1, text='▲', style=shape.labeldown, textcolor=color.white, color = color.green,   location = location.abovebar, title = "开多")
alertcondition(condition1 , title="CrossOver Double EMA Buy", message="CrossOver Double EMA Buy")
```  
  
开空代码信号模板  
```  
plotshape(condition2, text='▼', style=shape.labeldown, textcolor=color.white, color = color.red,   location = location.abovebar, title = "开空")
alertcondition(condition2  , title="CrossUnder Double EMA Sell", message="CrossUnder Double EMA Sell")
```  
  
平仓代码模板  
```  
plotshape(condition2, text='Cancel', style=shape.labeldown, textcolor=color.white, color = color.red,   location = location.abovebar, title = "开空")
alertcondition(condition2  , title="CrossUnder Double EMA Sell", message="CrossUnder Double EMA Sell")
```  
