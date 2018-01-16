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
  sc.data <- read.csv(paste(getwd(), '/dt_aggregated_baseline_a.csv', sep=''), header=TRUE, sep=",")
  dates <- as.Date(sc.data$date, tryformats = c('%d.%m.%y', '%Y-%m-%d'))
  cols <- names(sc.data) %in% 
    c('price',
      'wikipedia',
      'new_topics',
      'new_users'
      # addition to baseline_a
      # 'google',
      # 'new_topics'
      # 'new_posts'
      )
    
  # 'new_posts' 'tweets'
  sc.data <- sc.data[cols]
  xts.data <- as.xts(sc.data, order.by = dates)
  xts.data$date <- NULL
  rm(cols)
  
# Generate log-return series from data input
  xts.data$price.log.rtn <- diff(log(xts.data$price),lag = 1)
  # xts.data$google.log.rtn <- diff(log(xts.data$google),lag = 1)
  xts.data$wikipedia.log.rtn <- diff(log(xts.data$wikipedia),lag = 1)
  xts.data$new_topcis.log.rtn <- diff(log(xts.data$new_topics),lag = 1)
  # xts.data$tweets.log.rtn <- diff(log(xts.data$tweets),lag = 1)
  xts.data$new_users.log.rtn <- diff(log(xts.data$new_users),lag = 1)
  # addition to baseline_a
  # xts.data$new_topcis.log.rtn <- diff(log(xts.data$new_topics),lag = 1)
  # xts.data$new_posts.log.rtn <- diff(log(xts.data$new_posts),lag = 1)
  
# replace inf / -inf log-returns with NA (case for 4 points out of 793)
  xts.data$new_topcis.log.rtn[!is.finite(xts.data$new_topcis.log.rtn)] <- NA
  # xts.data$new_posts.log.rtn[!is.finite(xts.data$new_posts.log.rtn)] <- NA

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
  xts.VAR <- xts.data[, setdiff(colnames(xts.data),c('price',
                                                   # 'google',
                                                   'wikipedia',
                                                   'new_topics',
                                                   'new_users'
                                                   # addition to baseline_a
                                                   # 'new_topics'
                                                   #'new_posts'
                                                   ))]
                                                   
  xts.VAR <- na.omit(xts.VAR)
  xts.VAR <- xts.VAR['2014-01::2018-10']

  # xts.VAR <- ts(xts.VAR)
  fit <- VAR(xts.VAR, type = 'none', ic="SC", lag.max=1, p = 1)
  VAR_estimation <- summary(fit)
  while (!is.null(dev.list()))  dev.off()
  # plot(fit)
  
  print(xtable(VAR_estimation$varresult$price.log.rtn))
  print(xtable(VAR_estimation$varresult$wikipedia.log.rtn))
  print(xtable(VAR_estimation$varresult$new_topics.log.rtn))
  print(xtable(VAR_estimation$varresult$new_users.log.rtn))
  
# Impulse response functions for fitted VAR model
  ir1 <- irf(fit, ortho = T, n.ahead=12, boot=T, ci=0.95, runs = 5) # basic IR functions
  while (!is.null(dev.list()))  dev.off()
  # plot(ir1)

  
