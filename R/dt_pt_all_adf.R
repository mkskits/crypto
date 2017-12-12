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
  print(paste('dxy adf test results', ' lags = ', k, sep=''))
  print(adf.test(dxy, k = k))
  
  # calculate ADF test log-returns dxy
  log.dxy <- as.ts(dt.fin.assets$log.DXY)
  k <- floor(12*((NROW(na.omit(log.dxy))/100)^0.25))
  log.dxy <- na.remove(log.dxy)
  print(paste('log-returns dxy adf test results', ' lags = ', k, sep=''))
  print(adf.test(log.dxy, k = k))
  
  # plot acf & pacf functions (dxy log-returns)
  pdf('../../F_Figs/pt_dxy_acf.pdf')
  par(mfrow = c(2, 1))
  par(mar=c(4.5,4.5,1,1))
  acf(log.dxy, main=NA)
  pacf(log.dxy, main = NA)
  par(mfrow = c(1, 1))
  dev.off()
  
  # calculate ADF test XAU
  xau <- as.ts(dt.fin.assets$XAU)
  k <- floor(12*((NROW(na.omit(xau))/100)^0.25))
  print(paste('xau adf test results', ' lags = ', k, sep=''))
  print(adf.test(xau, k = k))
  
  # calculate ADF test log-returns XAU
  log.XAU <- as.ts(dt.fin.assets$log.XAU)
  k <- floor(12*((NROW(na.omit(log.XAU))/100)^0.25))
  log.XAU <- na.remove(log.XAU)
  print(paste('log-returns xau adf test results', ' lags = ', k, sep=''))
  print(adf.test(log.XAU, k = k))
  
  # calculate ADF test Global.Govt (Global Aggreate Treasuries)
  gat <- as.ts(dt.fin.assets$Global.Govt)
  k <- floor(12*((NROW(na.omit(gat))/100)^0.25))
  print(paste('gat adf test results', ' lags = ', k, sep=''))
  print(adf.test(gat, k = k))
  
  # calculate ADF test log-returns Global.Govt (Global Aggreate Treasuries)
  log.gat <- as.ts(dt.fin.assets$log.Global.Govt)
  k <- floor(12*((NROW(na.omit(log.gat))/100)^0.25))
  log.gat <- na.remove(log.gat)
  print(paste('log-returns gat adf test results', ' lags = ', k, sep=''))
  print(adf.test(log.gat, k = k))
  
  # calculate ADF test S&P 500
  spx <- as.ts(dt.fin.assets$SPX)
  k <- floor(12*((NROW(na.omit(spx))/100)^0.25))
  spx <- na.remove(spx)
  print(paste('SPX adf test results', ' lags = ', k, sep=''))
  print(adf.test(spx, k = k))
  
  # calculate ADF test log-returns S&P 500
  log.spx <- as.ts(dt.fin.assets$log.SPX)
  k <- floor(12*((NROW(na.omit(log.spx))/100)^0.25))
  log.spx <- na.remove(log.spx)
  print(paste('log-returns SPX adf test results', ' lags = ', k, sep=''))
  print(adf.test(log.spx, k = k))
  
  # calculate ADF test MSCI World
  mxwo <- as.ts(dt.fin.assets$MXWO)
  k <- floor(12*((NROW(na.omit(mxwo))/100)^0.25))
  mxwo <- na.remove(mxwo)
  print(paste('MXWO adf test results', ' lags = ', k, sep=''))
  print(adf.test(mxwo, k = k))
  
  # calculate ADF test log-returns MSCI World
  log.mxwo <- as.ts(dt.fin.assets$log.MXWO)
  k <- floor(12*((NROW(na.omit(log.mxwo))/100)^0.25))
  log.mxwo <- na.remove(log.mxwo)
  print(paste('log-returns MXWO adf test results', ' lags = ', k, sep=''))
  print(adf.test(log.mxwo, k = k))
  
  # plot acf & pacf functions (xau log-returns)
  pdf('../../F_Figs/pt_xau_acf.pdf')
  par(mfrow = c(2, 1))
  par(mar=c(4.5,4.5,1,1))
  acf(log.XAU, main=NA)
  pacf(log.XAU, main = NA)
  par(mfrow = c(1, 1))
  dev.off()
  
  # plot acf & pacf functions (global aggregate treasuries log-returns)
  pdf('../../F_Figs/pt_gat_acf.pdf')
  par(mfrow = c(2, 1))
  par(mar=c(4.5,4.5,1,1))
  acf(log.gat, main=NA)
  pacf(log.gat, main = NA)
  par(mfrow = c(1, 1))
  dev.off()
  
  # plot acf & pacf functions (S&P 500 log-returns)
  pdf('../../F_Figs/pt_spx_acf.pdf')
  par(mfrow = c(2, 1))
  par(mar=c(4.5,4.5,1,1))
  acf(log.spx, main=NA)
  pacf(log.spx, main = NA)
  par(mfrow = c(1, 1))
  dev.off()
  
  # plot acf & pacf functions (xau log-returns)
  pdf('../../F_Figs/pt_mxwo_acf.pdf')
  par(mfrow = c(2, 1))
  par(mar=c(4.5,4.5,1,1))
  acf(log.mxwo, main=NA)
  pacf(log.mxwo, main = NA)
  par(mfrow = c(1, 1))
  dev.off()

  # end
  print(paste('end: ', Sys.time()))