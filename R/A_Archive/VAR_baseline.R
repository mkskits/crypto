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
  sc.data <- read.csv(paste(getwd(), '/dt_aggregated.csv', sep=''), header=TRUE, sep=",")
  dates <- as.Date(sc.data$date, tryformats = c('%d.%m.%y', '%Y-%m-%d'))
  cols <- names(sc.data) %in% 
    c('price_usd',
      'google_tr_btc',
      'wikipedia', 
      'tweets',
      'no_users',
      'nTweets',
      'new_users')
    
  # 'new_posts' 'tweets'
  sc.data <- sc.data[cols]
  xts.data <- as.xts(sc.data, order.by = dates)
  xts.data$date <- NULL
  rm(cols)
  
  xts.data$price.log.rtn <- diff(log(xts.data$price_usd),lag = 1)
  xts.data$google.log.rtn <- diff(log(xts.data$google_tr_btc),lag = 1)
  # xts.data$btctalk.log.rtn <- diff(log(xts.data$new_posts),lag = 1)
  # xts.data$users.log.rtn <- diff(log(xts.data$no_users),lag = 1)
  # xts.data$users.log.rtn <- diff(log(xts.data$users.log.rtn),lag = 1)
  # xts.data$wikipedia.log.rtn <- diff(log(xts.data$wikipedia),lag = 1)
  xts.data$tweets.log.rtn <- diff(log(xts.data$nTweets),lag = 1)
  xts.data$new_users.log.rtn <- diff(log(xts.data$new_users),lag = 1)
  
  xts.data$price.log.rtn[!is.finite(xts.data$price.log.rtn)] <- NA
  xts.data$google.log.rtn[!is.finite(xts.data$google.log.rtn)] <- NA
  # xts.data$btctalk.log.rtn[!is.finite(xts.data$btctalk.log.rtn)] <- NA
  # xts.data$wikipedia.log.rtn[!is.finite(xts.data$wikipedia.log.rtn)] <- NA
  xts.data$tweets.log.rtn[!is.finite(xts.data$tweets.log.rtn)] <- NA
  xts.data$new_users.log.rtn[!is.finite(xts.data$new_users.log.rtn)] <- NA

# simple plots - data review
  pdf('pt_dt_plot.pdf')
  par(mfrow=c(2,2))
  # plot(xts.data$price.log.rtn)
  # plot(xts.data$google.log.rtn)
  # plot(xts.data$btctalk.log.rtn)
  # plot(xts.data$users.log.rtn)
  # plot(xts.data$tweets.log.rtn)
  while (!is.null(dev.list()))  dev.off()
  
# VAR estimation
  xts.VAR <- xts.data
  xts.VAR <- xts.data[, setdiff(colnames(xts.data),c('price_usd','wikipedia',
                                                   'google_tr_btc',
                                                   'tweets',  'no_users', 'new_posts',
                                                   'nTweets', 'new_users'))]
  xts.VAR <- na.omit(xts.VAR)
  xts.VAR <- xts.VAR['2014-01::2018-10']

  fit <- VAR(xts.VAR, type = 'both', ic="SC", lag.max=1, p = 1)
  VAR_estimation <- summary(fit)
  while (!is.null(dev.list()))  dev.off()
  # plot(fit)
  
  # xtable(VAR_estimation$varresult$price.log.rtn)
  
# Impulse response functions for fitted VAR model
  ir1 <- irf(fit, ortho = T, n.ahead=12, boot=T, ci=0.95, runs = 5) # basic IR functions
  while (!is.null(dev.list()))  dev.off()
  plot(ir1)

  
