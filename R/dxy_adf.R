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
  
  # calculate ADF test dxy
  dxy <- as.ts(dt.fin.assets$DXY)
  k <- floor(12*((NROW(na.omit(dxy))/100)^0.25))
  print(paste('dxy adf test results', lags = k, sep=''))
  print(adf.test(dxy, k = k))
  
  # calculate ADF test log-returns dxy
  log.dxy <- as.ts(dt.fin.assets$log.DXY)
  k <- floor(12*((NROW(na.omit(log.dxy))/100)^0.25))
  log.dxy <- na.remove(log.dxy)
  print(paste('log-returns dxy adf test results', lags = k, sep=''))
  print(adf.test(log.dxy, k = k))
  
  # plot acf & pacf functions (log-returns)
  pdf('../../F_Figs/pt_dxy_acf.pdf')
  par(mfrow = c(2, 1))
  par(mar=c(4.5,4.5,1,1))
  acf(log.dxy, main=NA)
  pacf(log.dxy, main = NA)
  par(mfrow = c(1, 1))
  dev.off()
  
  # calculate ADF test log-returns XAU
  log.XAU <- as.ts(dt.fin.assets$log.XAU)
  k <- floor(12*((NROW(na.omit(log.XAU))/100)^0.25))
  log.XAU <- na.remove(log.XAU)
  print(paste('log-returns dxy adf test results', lags = k, sep=''))
  print(adf.test(log.dxy, k = k))
  
# end
  print(paste('end: ', Sys.time()))