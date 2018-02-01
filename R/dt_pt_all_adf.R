# ADF test on dxy

library('tseries')
library('stargazer')
library('dplyr')
library('xts')
library('timeSeries')

# start
  print(paste('start: ', Sys.time()))
  
# data handling
  # setwd('..')
  print(getwd())
  setwd(script.dir <- dirname(sys.frame(1)$ofile))
  setwd('..')
  setwd('./D_Data/B_Bloomberg/')
  # read input
    dt.fin.assets <- read.csv(file=paste(getwd(), '/dt_fin_assets.csv', sep=''), header=TRUE, sep=",")

    # calculate ADF test XAU
    xau <- as.ts(dt.fin.assets$XAU)
    k <- floor(12*((NROW(na.omit(xau))/100)^0.25))
    print(paste('xau adf test results', ' lags = ', k, sep=''))
    adf.xau <- adf.test(xau, k = k)
    
    # calculate ADF test dxy
    dxy <- as.ts(dt.fin.assets$DXY)
    k <- floor(12*((NROW(na.omit(dxy))/100)^0.25))
    print(paste('dxy adf test results', ' lags = ', k, sep=''))
    adf.dxy <- adf.test(dxy, k = k)
    
    # calculate ADF test spx
    spx <- as.ts(dt.fin.assets$SPX)
    k <- floor(12*((NROW(na.omit(spx))/100)^0.25))
    print(paste('spx adf test results', ' lags = ', k, sep=''))
    adf.spx <- adf.test(spx, k = k)
    
    # calculate ADF test NVDA
    nvda <- as.ts(dt.fin.assets$NVDA)
    k <- floor(12*((NROW(na.omit(nvda))/100)^0.25))
    print(paste('nvda adf test results', ' lags = ', k, sep=''))
    adf.nvda <- adf.test(nvda, k = k)
    
    # calculate ADF test QCOM
    qcom <- as.ts(dt.fin.assets$QCOM)
    k <- floor(12*((NROW(na.omit(qcom))/100)^0.25))
    print(paste('qcom adf test results', ' lags = ', k, sep=''))
    adf.qcom <- adf.test(qcom, k = k)
    
    # calculate ADF test tsm
    tsm <- as.ts(dt.fin.assets$TSM)
    k <- floor(12*((NROW(na.omit(tsm))/100)^0.25))
    print(paste('tsm adf test results', ' lags = ', k, sep=''))
    adf.tsm <- adf.test(tsm, k = k)
    
    # calculate ADF test amd
    amd <- as.ts(dt.fin.assets$AMD)
    k <- floor(12*((NROW(na.omit(amd))/100)^0.25))
    print(paste('amd adf test results', ' lags = ', k, sep=''))
    adf.amd <- adf.test(amd, k = k)
    
    # calculate ADF test high yield
    high.yield <- as.ts(dt.fin.assets$High.Yield)
    k <- floor(12*((NROW(na.omit(high.yield))/100)^0.25))
    print(paste('high yield adf test results', ' lags = ', k, sep=''))
    adf.high.yield <- adf.test(high.yield, k = k)
    
    # calculate ADF test global govt
    global.govt <- as.ts(dt.fin.assets$Global.Govt)
    k <- floor(12*((NROW(na.omit(global.govt))/100)^0.25))
    print(paste('global govt adf test results', ' lags = ', k, sep=''))
    adf.global.govt <- adf.test(global.govt, k = k)
    
    # calculate ADF test us govt
    us.govt <- as.ts(dt.fin.assets$US.Govt)
    k <- floor(12*((NROW(na.omit(us.govt))/100)^0.25))
    print(paste('us gov adf test results', ' lags = ', k, sep=''))
    adf.us.govt <- adf.test(us.govt, k = k)
    
    
    # calculate ADF test log-returns XAU
    log.xau <- as.ts(dt.fin.assets$log.XAU)
    k <- floor(12*((NROW(na.omit(log.xau))/100)^0.25))
    log.xau <- na.remove(log.xau)
    print(paste('log-returns xau adf test results', ' lags = ', k, sep=''))
    adf.log.xau <- adf.test(log.xau, k = k)
    
    # calculate ADF test log-returns dxy
    log.dxy <- as.ts(dt.fin.assets$log.DXY)
    k <- floor(12*((NROW(na.omit(log.dxy))/100)^0.25))
    log.dxy <- na.remove(log.dxy)
    print(paste('log-returns dxy adf test results', ' lags = ', k, sep=''))
    adf.log.dxy <- adf.test(log.dxy, k = k)

    # calculate ADF test log-returns spx
    log.spx <- as.ts(dt.fin.assets$log.SPX)
    k <- floor(12*((NROW(na.omit(log.spx))/100)^0.25))
    log.spx <- na.remove(log.spx)
    print(paste('log-returns spx adf test results', ' lags = ', k, sep=''))
    adf.log.spx <- adf.test(log.spx, k = k)
    
    # calculate ADF test log-returns nvda
    log.nvda <- as.ts(dt.fin.assets$log.NVDA)
    k <- floor(12*((NROW(na.omit(log.nvda))/100)^0.25))
    log.nvda <- na.remove(log.nvda)
    print(paste('log-returns nvda adf test results', ' lags = ', k, sep=''))
    adf.log.nvda <- adf.test(log.nvda, k = k)
    
    # calculate ADF test log-returns QCOM
    log.qcom <- as.ts(dt.fin.assets$log.QCOM)
    k <- floor(12*((NROW(na.omit(log.qcom))/100)^0.25))
    log.qcom <- na.remove(log.qcom)
    print(paste('log-returns qcom adf test results', ' lags = ', k, sep=''))
    adf.log.qcom <- adf.test(log.qcom, k = k)
    
    # calculate ADF test log-returns tsm
    log.tsm <- as.ts(dt.fin.assets$log.TSM)
    k <- floor(12*((NROW(na.omit(log.tsm))/100)^0.25))
    log.tsm <- na.remove(log.tsm)
    print(paste('log-returns tsm adf test results', ' lags = ', k, sep=''))
    adf.log.tsm <- adf.test(log.tsm, k = k)
    
    # calculate ADF test log-returns amd
    log.amd <- as.ts(dt.fin.assets$log.AMD)
    k <- floor(12*((NROW(na.omit(log.amd))/100)^0.25))
    log.amd <- na.remove(log.amd)
    print(paste('log-returns amd adf test results', ' lags = ', k, sep=''))
    adf.log.amd <- adf.test(log.amd, k = k)
    
    # calculate ADF test log-returns high.yield
    log.high.yield <- as.ts(dt.fin.assets$log.High.Yield)
    k <- floor(12*((NROW(na.omit(log.high.yield))/100)^0.25))
    log.high.yield <- na.remove(log.high.yield)
    print(paste('log-returns high.yield adf test results', ' lags = ', k, sep=''))
    adf.log.high.yield <- adf.test(log.high.yield, k = k)
    
    # calculate ADF test log-returns global.govt
    log.global.govt <- as.ts(dt.fin.assets$log.Global.Govt)
    k <- floor(12*((NROW(na.omit(log.global.govt))/100)^0.25))
    log.global.govt <- na.remove(log.global.govt)
    print(paste('log-returns global.govt adf test results', ' lags = ', k, sep=''))
    adf.log.global.govt <- adf.test(log.global.govt, k = k)
    
    # calculate ADF test log-returns us.govt
    log.us.govt <- as.ts(dt.fin.assets$log.US.Govt)
    k <- floor(12*((NROW(na.omit(log.us.govt))/100)^0.25))
    log.us.govt <- na.remove(log.us.govt)
    print(paste('log-returns us.govt adf test results', ' lags = ', k, sep=''))
    adf.log.us.govt <- adf.test(log.us.govt, k = k)
    
    series <- c('XAU', 'DXY', 'SPX', 'NVDA', 'QCOM', 'TSM', 'AMD', 'High Yield', 'Global Gov', 'US Gov',
                'XAU (Log-Return)', 'DXY (Log-Return)', 'SPX (Log-Return)', 'NVDA (Log-Return)', 'QCOM (Log-Return)',
                'TSM (Log-Return)', 'AMD (Log-Return)', 'High Yield (Log-Return)', 'Global Gov (Log-Return)', 'US Gov (Log-Return)')
 
       df <- c(adf.xau$statistic,
            adf.dxy$statistic,
            adf.spx$statistic,
            adf.nvda$statistic,
            adf.qcom$statistic,
            adf.tsm$statistic,
            adf.amd$statistic,
            adf.high.yield$statistic,
            adf.global.govt$statistic,
            adf.us.govt$statistic,
            
            adf.log.xau$statistic,
            adf.log.dxy$statistic,
            adf.log.spx$statistic,
            adf.log.nvda$statistic,
            adf.log.qcom$statistic,
            adf.log.tsm$statistic,
            adf.log.amd$statistic,
            adf.log.high.yield$statistic,
            adf.log.global.govt$statistic,
            adf.log.us.govt$statistic
            )
       
       dfp <- c(adf.xau$p.value,
               adf.dxy$p.value,
               adf.spx$p.value,
               adf.nvda$p.value,
               adf.qcom$p.value,
               adf.tsm$p.value,
               adf.amd$p.value,
               adf.high.yield$p.value,
               adf.global.govt$p.value,
               adf.us.govt$p.value,
               
               adf.log.xau$p.value,
               adf.log.dxy$p.value,
               adf.log.spx$p.value,
               adf.log.nvda$p.value,
               adf.log.qcom$p.value,
               adf.log.tsm$p.value,
               adf.log.amd$p.value,
               adf.log.high.yield$p.value,
               adf.log.global.govt$p.value,
               adf.log.us.govt$p.value
              )
       
    adf.fin <- data.frame(series, df, dfp)
  
  # end
  print(paste('end: ', Sys.time()))