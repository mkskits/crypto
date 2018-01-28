# ADF test on bitcoin price series

library('tseries')
library('stargazer')
library('dplyr')
library('xts')
library('timeSeries')

# start
  print(paste('start: ', Sys.time()))
  
# data handling
  # setwd('..')
  rm(list=ls())
  print(getwd())
  setwd(script.dir <- dirname(sys.frame(1)$ofile))
  setwd('..')
  setwd('./D_Data/B_Bitcoin_com/')
  # read input
    dt.btc.com <- read.csv(file=paste(getwd(), '/price.csv', sep=''), header=TRUE, sep=";")
  # delete all dates that have zero price value from start
    dt.btc.com <- dt.btc.com[apply(dt.btc.com[c(2:2)],1,function(z) !any(z==0)),] 
  # calcuate log-returns
    dt.btc.com$log.returns <- c(NA, diff(log(dt.btc.com$BitcoinPrice),lag = 1))
  # calculate first differences
    dt.btc.com$first.differences <- c(NA, diff(dt.btc.com$BitcoinPrice,lag = 1))
  # calculate percentage changes
    dt.btc.com$pct.changes <- dt.btc.com$BitcoinPrice / lag(dt.btc.com$BitcoinPrice, 1) - 1
    # dt.btc.com$pct.changes <- 0
  # calculate 30day annualized volatility
    dt.btc.com <- as.xts(dt.btc.com, order.by=as.Date(dt.btc.com$Date, format='%d.%m.%Y'))
    dt.btc.com <- dt.btc.com[, colnames(dt.btc.com) != 'Date']
    dt.btc.com$vol_ann_30d <- rollapply(dt.btc.com$log.returns,width=30, FUN=sd)*sqrt(365)
    storage.mode(dt.btc.com) <- "numeric"
  # rename columns
    colnames(dt.btc.com) = c('Price', 'log.return', 'first.differences', 'pct.changes', 'ann_vol_30d')
    stg.input <- data.frame(date = index(dt.btc.com), dt.btc.com$Price, 
                          dt.btc.com$log.return,
                          dt.btc.com$first.differences,
                          dt.btc.com$pct.changes,
                          dt.btc.com$ann_vol_30d,
                          row.names = NULL)
  # print(stargazer(dt.btc.com))
  
# adf test (need to convert xts object to ts in order to apply adf test)
  # acf(xbt.log.return, main="")
  # pacf(xbt.log.return, main="")
  xbt.log.return <- as.ts(dt.btc.com$log.return)
  xbt.log.return <- na.remove(xbt.log.return)
  # adf <- adf.test(xbt.log.return)
  
  p.values <- character(500)
  for (i in 1:500){
    adf <- adf.test(xbt.log.return, k=i)
    p.values[i] <- adf$p.value
    print(i)
  }
  
  p.values <- as.numeric(p.values)  
  
# store pvalues of adf tests
  write.table(p.values, 'dt_adf_pvalues.csv', sep=',')
    
# plot pvalues of adf tests on log-returns
  pdf('../../F_Figs/pt_log_rtn_pvalues.pdf')
  plot(rep(1:500), p.values,
        # main = 'title placeholder', 
        yaxt='n',
        pch = 18,
        col='blue',
        bg='blue', 
        ylab = "p-Value", xlab = "Number of Lags",
       cex.axis = 1.7, cex.main = 1.7, cex=1.7, cex.lab = 1.7, cex.sub = 1.7,
       oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
  abline(h = 0.05, col = "red")
  axis(2, at=c(0.05, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1), cex.axis = 1.7)
  dev.off()
  
# plot acf & pacf functions
  pdf('../../F_Figs/pt_log_rtn_p_acf.pdf')
  par(mfrow = c(2, 1))
  par(mar=c(4.5,4.5,1,1))
  acf(xbt.log.return, main=NA,cex.axis = 1.7, cex.main = 1.7, cex=1.7, cex.lab = 1.7,
      oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
  pacf(xbt.log.return, main = NA, cex.axis = 1.7, cex.main = 1.7, cex=1.7, cex.lab = 1.7,
       oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
  par(mfrow = c(1, 1))
  dev.off()
  
# end
  print(paste('end: ', Sys.time()))