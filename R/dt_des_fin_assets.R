library('stargazer')
library('dplyr')
library('zoo')
library('xts')

# > getwd()
# setwd('..')
# getwd()

# start
  print(paste('start: ', Sys.time()))

# directories 
  # setwd('..')
  print(getwd())
  # setwd(script.dir <- dirname(sys.frame(1)$ofile))
  setwd('..')
  setwd('./D_Data/B_Bloomberg/')

# read input (fin-assets.csv dump saved from bloomberg linked xls file)
  dt.fin.assets <- read.csv(file=paste(getwd(), '/fin-assets.csv', sep=''), header=TRUE, sep=",")
  dt.fin.assets <- subset(dt.fin.assets, select=c('Date',
                                                  'DXY.Curncy',
                                                  'XAU.Curncy',
                                                  'SPX.Index',
                                                  'MXWO.Index',
                                                  'QCOM.US.Equity',
                                                  'TSM.US.Equity',
                                                  'AMD.US.Equity',
                                                  'NVDA.US.Equity',
                                                  'LG30TRUU.Index',
                                                  'LGTRTRUU.Index',
                                                  'LUATTRUU.Index'
                                                  ))
  
# last observations carried forward (generic function for replacing each NA with the most recent
    # non-NA prior to it)
  dt.fin.assets <- na.locf(dt.fin.assets)
  colnames(dt.fin.assets) = c('Date', 'DXY', 'XAU', 'SPX', 'MXWO', 'QCOM', 'TSM', 'AMD', 'NVDA',
                              'High.Yield', 'Global.Govt', 'US.Govt')

# delete first 17 rows (align star of the matrix to the bitcoin price series)  
  dt.fin.assets <- tail(dt.fin.assets,-16)
  # delete all dates that have zero price value from start
  # XBT COMMENT dt.btc.com <- dt.btc.com[apply(dt.btc.com[c(2:2)],1,function(z) !any(z==0)),] 
  
  storage.mode(dt.fin.assets$DXY) <- 'numeric'
  storage.mode(dt.fin.assets$XAU) <- 'numeric'
  storage.mode(dt.fin.assets$SPX) <- 'numeric'
  storage.mode(dt.fin.assets$MXWO) <- 'numeric'
  storage.mode(dt.fin.assets$QCOM) <- 'numeric'
  storage.mode(dt.fin.assets$TSM) <- 'numeric'
  storage.mode(dt.fin.assets$AMD) <- 'numeric'
  storage.mode(dt.fin.assets$NVDA) <- 'numeric'
  storage.mode(dt.fin.assets$High.Yield) <- 'numeric'
  storage.mode(dt.fin.assets$Global.Govt) <- 'numeric'
  storage.mode(dt.fin.assets$US.Govt) <- 'numeric'
                 
# calcuate log-returns
  dt.fin.assets$log.DXY <- c(NA, diff(log(dt.fin.assets$DXY),lag = 1))
  dt.fin.assets$log.XAU <- c(NA, diff(log(dt.fin.assets$XAU),lag = 1))
  dt.fin.assets$log.SPX <- c(NA, diff(log(dt.fin.assets$SPX),lag = 1))
  dt.fin.assets$log.MXWO <- c(NA, diff(log(dt.fin.assets$MXWO),lag = 1))
  dt.fin.assets$log.QCOM <- c(NA, diff(log(dt.fin.assets$QCOM),lag = 1))
  dt.fin.assets$log.TSM <- c(NA, diff(log(dt.fin.assets$TSM),lag = 1))
  dt.fin.assets$log.AMD <- c(NA, diff(log(dt.fin.assets$AMD),lag = 1))
  dt.fin.assets$log.NVDA <- c(NA, diff(log(dt.fin.assets$NVDA),lag = 1))
  dt.fin.assets$log.High.Yield <- c(NA, diff(log(dt.fin.assets$High.Yield),lag = 1))
  dt.fin.assets$log.Global.Govt <- c(NA, diff(log(dt.fin.assets$Global.Govt),lag = 1))
  dt.fin.assets$log.US.Govt <- c(NA, diff(log(dt.fin.assets$US.Govt),lag = 1))
  
# calculate first differences
  dt.fin.assets$DXY.fd <- c(NA, diff(dt.fin.assets$DXY,lag = 1))
  dt.fin.assets$XAU.fd <- c(NA, diff(dt.fin.assets$XAU,lag = 1))
  dt.fin.assets$SPX.fd <- c(NA, diff(dt.fin.assets$SPX,lag = 1))
  dt.fin.assets$MXWO.fd <- c(NA, diff(dt.fin.assets$MXWO,lag = 1))
  dt.fin.assets$QCOM.fd <- c(NA, diff(dt.fin.assets$QCOM,lag = 1))
  dt.fin.assets$TSM.fd <- c(NA, diff(dt.fin.assets$TSM,lag = 1))
  dt.fin.assets$AMD.fd <- c(NA, diff(log(dt.fin.assets$AMD),lag = 1))
  dt.fin.assets$NVDA.fd <- c(NA, diff(log(dt.fin.assets$NVDA),lag = 1))
  dt.fin.assets$High.Yield.fd <- c(NA, diff(log(dt.fin.assets$High.Yield),lag = 1))
  dt.fin.assets$Global.Govt.fd <- c(NA, diff(dt.fin.assets$Global.Govt,lag = 1))
  dt.fin.assets$US.Govt.fd <- c(NA, diff(log(dt.fin.assets$US.Govt),lag = 1))
  
# calculate percentage changes
  dt.fin.assets$DXY.pct <- dt.fin.assets$DXY / lag(dt.fin.assets$DXY, 1) - 1
  dt.fin.assets$XAU.pct <- dt.fin.assets$XAU / lag(dt.fin.assets$XAU, 1) - 1
  dt.fin.assets$SPX.pct <- dt.fin.assets$SPX / lag(dt.fin.assets$SPX, 1) - 1
  dt.fin.assets$MXWO.pct <- dt.fin.assets$MXWO / lag(dt.fin.assets$MXWO, 1) - 1
  dt.fin.assets$QCOM.pct <- dt.fin.assets$QCOM / lag(dt.fin.assets$QCOM, 1) - 1
  dt.fin.assets$TSM.pct <- dt.fin.assets$TSM / lag(dt.fin.assets$TSM, 1) - 1
  dt.fin.assets$AMD.pct <- dt.fin.assets$AMD / lag(dt.fin.assets$AMD, 1) - 1
  dt.fin.assets$NVDA.pct <- dt.fin.assets$NVDA / lag(dt.fin.assets$NVDA, 1) - 1
  dt.fin.assets$High.Yield.pct <- dt.fin.assets$High.Yield / lag(dt.fin.assets$High.Yield, 1) - 1
  dt.fin.assets$Global.Govt.pct <- dt.fin.assets$Global.Govt / lag(dt.fin.assets$Global.Govt, 1) - 1
  dt.fin.assets$US.Govt.pct <- dt.fin.assets$US.Govt / lag(dt.fin.assets$US.Govt, 1) - 1
  
# calculate 30day annualized volatility
  dt.fin.assets <- as.xts(dt.fin.assets, order.by=as.Date(dt.fin.assets$Date, format='%d.%m.%y'))
  dt.fin.assets <- dt.fin.assets[, colnames(dt.fin.assets) != 'Date']
  storage.mode(dt.fin.assets) <- "numeric"
  
  dt.fin.assets$DXY.vol <- rollapply(dt.fin.assets$log.DXY,width=30, FUN=sd)*sqrt(250)
  dt.fin.assets$XAU.vol <- rollapply(dt.fin.assets$log.XAU,width=30, FUN=sd)*sqrt(250)
  dt.fin.assets$SPX.vol <- rollapply(dt.fin.assets$log.SPX,width=30, FUN=sd)*sqrt(250)
  dt.fin.assets$MXWO.vol <- rollapply(dt.fin.assets$log.MXWO,width=30, FUN=sd)*sqrt(250)
  dt.fin.assets$QCOM.vol <- rollapply(dt.fin.assets$log.QCOM,width=30, FUN=sd)*sqrt(250)
  dt.fin.assets$TSM.vol <- rollapply(dt.fin.assets$log.TSM,width=30, FUN=sd)*sqrt(250)
  dt.fin.assets$AMD.vol <- rollapply(dt.fin.assets$log.AMD,width=30, FUN=sd)*sqrt(250)
  dt.fin.assets$NVDA.vol <- rollapply(dt.fin.assets$log.NVDA,width=30, FUN=sd)*sqrt(250)
  dt.fin.assets$High.Yield.vol <- rollapply(dt.fin.assets$log.High.Yield,width=30, FUN=sd)*sqrt(250)
  dt.fin.assets$Global.Govt.vol <- rollapply(dt.fin.assets$log.Global.Govt,width=30, FUN=sd)*sqrt(250)
  dt.fin.assets$US.Govt.vol <- rollapply(dt.fin.assets$log.US.Govt,width=30, FUN=sd)*sqrt(250)
  
  storage.mode(dt.fin.assets) <- "numeric"
  
  stg.input <- data.frame(date = index(dt.fin.assets), 
                          dt.fin.assets$DXY,
                          dt.fin.assets$log.DXY,
                          dt.fin.assets$XAU,
                          dt.fin.assets$log.XAU,
                          dt.fin.assets$SPX,
                          dt.fin.assets$log.SPX,
                          dt.fin.assets$MXWO,
                          dt.fin.assets$log.MXWO,
                          dt.fin.assets$Global.Govt,
                          dt.fin.assets$log.Global.Govt,
                          dt.fin.assets$US.Govt,
                          dt.fin.assets$log.US.Govt,
                          dt.fin.assets$High.Yield,
                          dt.fin.assets$log.High.Yield,
                          dt.fin.assets$QCOM,
                          dt.fin.assets$log.QCOM,
                          dt.fin.assets$TSM,
                          dt.fin.assets$log.TSM,
                          dt.fin.assets$AMD,
                          dt.fin.assets$log.AMD,
                          dt.fin.assets$NVDA,
                          dt.fin.assets$log.NVDA,
                          row.names = NULL)
  
  write.csv(dt.fin.assets, file = 'dt_fin_assets.csv', row.names=index(dt.fin.assets))
  write.zoo(dt.fin.assets, sep=',',file='xts_fin_assets')
  # print(stargazer(dt.btc.com))
  
# end
  print(paste('end: ', Sys.time()))