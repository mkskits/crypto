# VAR specification

# package requirements: vars, tseries, forecast, strucchange, xts

library('tseries')
library('forecast')
library('vars')
library('strucchange')
library('xts')
library('stargazer')
library('xtable')

# start
  print(paste('start: ', Sys.time()))
  rm(list=ls())
  while (!is.null(dev.list()))  dev.off()
  
# directories 
  # setwd('..')
  print(getwd())
  setwd(script.dir <- dirname(sys.frame(1)$ofile))
  setwd('..')
  setwd('./D_Data/')
  wd <- getwd()

# data input 
  sc.data <- read.csv(paste(getwd(), '/dt_aggregated_fin_assets.csv', sep=''), header=TRUE, sep=",")
  dates <- as.Date(sc.data$date, tryformats = c('%d.%m.%y', '%Y-%m-%d'))
  cols <- names(sc.data) %in% 
    c('price',
      'wikipedia',
      'tweets',
      'new_users',
      # fin assets
      'xau',
      'dxy',
      'spx',
      'nvda',
      'qcom',
      'tsm',
      'amd',
      'high.yield',
      'global.govt',
      'us.govt'
      )
  sc.data <- sc.data[cols]
  
  xts.data <- as.xts(sc.data, order.by = dates)
  xts.data$date <- NULL
  rm(cols)
  
  xts.data$price.log.rtn <- diff(log(xts.data$price),lag = 1)
  # xts.data$google.log.rtn <- diff(log(xts.data$google),lag = 1)
  xts.data$wikipedia.log.rtn <- diff(log(xts.data$wikipedia),lag = 1)
  xts.data$tweets.log.rtn <- diff(log(xts.data$tweets),lag = 1)
  # xts.data$new_users.log.rtn <- diff(log(xts.data$new_users),lag = 1)
  # fin assets
  xts.data$xau.log.rtn <- diff(log(xts.data$xau),lag = 1)
  xts.data$dxy.log.rtn <- diff(log(xts.data$dxy),lag = 1)
  xts.data$spx.log.rtn <- diff(log(xts.data$spx),lag = 1)
  xts.data$nvda.log.rtn <- diff(log(xts.data$nvda),lag = 1)
  xts.data$qcom.log.rtn <- diff(log(xts.data$qcom),lag = 1)
  xts.data$tsm.log.rtn <- diff(log(xts.data$tsm),lag = 1)
  xts.data$amd.log.rtn <- diff(log(xts.data$amd),lag = 1)
  xts.data$high.yield.log.rtn <- diff(log(xts.data$high.yield),lag = 1)
  xts.data$global.govt.log.rtn <- diff(log(xts.data$global.govt),lag = 1)
  xts.data$us.govt.log.rtn <- diff(log(xts.data$us.govt),lag = 1)
  
  # replace inf / -inf log-returns with NA (case for 4 points out of 793)
    # xts.data$new_topcis.log.rtn[!is.finite(xts.data$new_topcis.log.rtn)] <- NA
    # xts.data$new_posts.log.rtn[!is.finite(xts.data$new_posts.log.rtn)] <- NA

# simple plots - data review
  # pdf('pt_dt_plot.pdf')
  par(mfrow=c(2,2))
  # plot(xts.data$price.log.rtn)
  # plot(xts.data$google.log.rtn)
  # plot(xts.data$btctalk.log.rtn)
  # plot(xts.data$users.log.rtn)
  # plot(xts.data$tweets.log.rtn)
  while (!is.null(dev.list()))  dev.off()
  
# VAR estimation
  xts.VAR <- xts.data
  xts.VAR <- xts.data[, setdiff(colnames(xts.data),c('price',
                                                   # 'google',
                                                   'wikipedia',
                                                   'tweets',
                                                   # fin assets
                                                   'xau',
                                                   'dxy',
                                                   'spx',
                                                   'nvda',
                                                   'qcom',
                                                   'tsm',
                                                   'amd',
                                                   'high.yield',
                                                   'global.govt',
                                                   'us.govt'
                                                   ))]
                                                   
  xts.VAR <- na.omit(xts.VAR)
  # xts.VAR <- xts.VAR['2014-01::2018-10']

  # xts.VAR <- ts(xts.VAR)
  fit <- VAR(xts.VAR, type = 'both', ic="SC", lag.max=1, p = 1)
  VAR_estimation <- summary(fit)
  granger <- causality(fit, cause = NULL, boot=TRUE, boot.runs=1000) 
  # Computes the test statistics for granger- and Instantaneous causality for a VAR(p).
  while (!is.null(dev.list()))  dev.off()
  # plot(fit)
  
  # print(xtable(VAR_estimation$varresult$price.log.rtn))
  # print(xtable(VAR_estimation$varresult$wikipedia.log.rtn))
  # print(xtable(VAR_estimation$varresult$tweets.log.rtn))
  # print(xtable(VAR_estimation$varresult$new_users.log.rtn))
  
  ir = irf(fit, ortho = T, n.ahead = 12, boot = 12, ci = 0.95, runs = 10)
# Impulse response functions for fitted VAR model
  # ir_search <- irf(fit, impulse = c('price.log.rtn'), response = c('wikipedia.log.rtn'),
  #                   ortho = T, n.ahead=12, boot=T, ci=0.95, runs = 100) # basic IR functions
  # while (!is.null(dev.list()))  dev.off()
  # # ir1$irf$wikipedia.log.rtn = 100 * ir1$irf$wikipedia.log.rtn
  # pdf('../F_Figs/pt_fit_baseline_a_search.pdf')
  # plot(ir_search, main='', xlab='', ylab='Information Search Response',
  #      sub='t (days)', xlim=c(1, 10),
  #      cex.axis = 2, cex.main = 2, cex=2, cex.lab = 2,
  #      oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
  # dev.off()
  # print('IR fin assets done)')