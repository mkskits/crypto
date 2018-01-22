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
  
# define bootstrap for IR bands
  cl <- 10
  
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
      # 'google',
      # 'wikipedia',
      'tweets',
      # 'new_users'
      # fin assets
      'xau'
      # 'dxy'
      )
  sc.data <- sc.data[cols]
  
  xts.data <- as.xts(sc.data, order.by = dates)
  xts.data$date <- NULL
  rm(cols)
  
  xts.data$price.log.rtn <- diff(log(xts.data$price),lag = 1)
  # xts.data$google.log.rtn <- diff(log(xts.data$google),lag = 1)
  # xts.data$wikipedia.log.rtn <- diff(log(xts.data$wikipedia),lag = 1)
  xts.data$tweets.log.rtn <- diff(log(xts.data$tweets),lag = 1)
  # xts.data$new_users.log.rtn <- diff(log(xts.data$new_users),lag = 1)
  # fin assets
  xts.data$xau.log.rtn <- diff(log(xts.data$xau),lag = 1)
  # xts.data$dxy.log.rtn <- diff(log(xts.data$dxy),lag = 1)
  
  # replace inf / -inf log-returns with NA
    # xts.data$new_topcis.log.rtn[!is.finite(xts.data$new_topcis.log.rtn)] <- NA
    # xts.data$new_posts.log.rtn[!is.finite(xts.data$new_posts.log.rtn)] <- NA

# simple plots - data review
  # pdf('pt_dt_plot.pdf')
  # par(mfrow=c(2,2))
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
                                                   # 'wikipedia',
                                                   'tweets',
                                                   # fin assets
                                                   'xau'
                                                   # 'dxy'
                                                   ))]
                                                   
  xts.VAR <- na.omit(xts.VAR)
  xts.VAR <- xts.VAR['2014-01::2017-12']

  # xts.VAR <- ts(xts.VAR)
  fit <- VAR(xts.VAR, type = 'both', ic="AIC", lag.max=1)
  VAR_estimation <- summary(fit)
  while (!is.null(dev.list()))  dev.off()
  # plot(fit)
  
  # xtable(VAR_estimation$varresult$price.log.rtn)
  # xtable(VAR_estimation$varresult$wikipedia.log.rtn)
  # xtable(VAR_estimation$varresult$tweets.log.rtn)
  # xtable(VAR_estimation$varresult$xau.log.rtn)
  
# store estimation result summary into data frame
  
  ir = irf(fit, ortho = T, n.ahead = 12, boot = TRUE, ci = 0.95, runs = cl)
  # Impulse response functions for fitted VAR model
  # Social Feedback Cycle
  
  
  
  
  # Price (impulse: sharing - respone: price)
  ir_price_s <- irf(fit, impulse = c('tweets.log.rtn'), response = c('price.log.rtn'),
                    ortho = T, n.ahead=24, boot=T, ci=0.95, runs = cl) # basic IR functions
  while (!is.null(dev.list()))  dev.off()
  # ir1$irf$wikipedia.log.rtn = 100 * ir1$irf$wikipedia.log.rtn
  pdf('../F_Figs/pt_fit_fin_b_tweets_price.pdf')
  plot(ir_price_s, main='', xlab='', ylab='Price Response',
       sub='t (days)', xlim=c(1, 24),
       cex.axis = 2, cex.main = 2, cex=2, cex.lab = 2,
       oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
  dev.off()
  print('Price (impulse: sharing - respone: price)')
  

  
  # # Price2 (impulse: XAU - respone: Price)
  # ir_price_s <- irf(fit, impulse = c('xau.log.rtn'), response = c('price.log.rtn'),
  #                   ortho = T, n.ahead=24, boot=T, ci=0.95, runs = cl) # basic IR functions
  # while (!is.null(dev.list()))  dev.off()
  # # ir1$irf$wikipedia.log.rtn = 100 * ir1$irf$wikipedia.log.rtn
  # pdf('../F_Figs/pt_fit_fin_b_xau_price.pdf')
  # plot(ir_price_s, main='', xlab='', ylab='Price Response',
  #      sub='t (days)', xlim=c(1, 24),
  #      cex.axis = 2, cex.main = 2, cex=2, cex.lab = 2,
  #      oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
  # dev.off()
  # print('Price (impulse: xau - respone: price)')
  # 
  # 