# VAR specification

# package requirements: vars, tseries, forecast, strucchange, xts

library('tseries')
library('forecast')
library('vars')
library('strucchange')
library('xts')

# start
  print(paste('start: ', Sys.time()))
  rm(list=ls())
  while (!is.null(dev.list()))  dev.off()
  
# directories 
  # setwd('..')
  print(getwd())
  setwd(script.dir <- dirname(sys.frame(1)$ofile))
  setwd('..')
  setwd('./R/')
  wd <- getwd()

# data input 1 for price
  sc.data1 <- read.csv(paste(getwd(), '/prices.txt', sep=''), header=TRUE, sep="\t")
  dates <- as.Date(sc.data1$date, tryformats = c('%d.%m.%y', '%Y-%m-%d'))
  #cols <- names(sc.data) %in% c('WeightedPrice')
  
 # data input 2 for other variables
  sc.data2 <- read.csv(paste(getwd(), '/social_signals.txt', sep=''), header=TRUE, sep="\t")
  dates <- as.Date(sc.data2$date, tryformats = c('%d.%m.%y', '%Y-%m-%d'))
  #cols <- names(sc.data) %in% c('nTweets','googleSearch','wikiViews','totalTweets','nUsersFiltered',)  
  
 # Merge the two datasets
  sc.data <- merge(sc.data1, sc.data2, by="date")
  dates <- as.Date(sc.data$date, tryformats = c('%d.%m.%y', '%Y-%m-%d'))
  
    # 'new_posts' 'tweets'          These 5 lines are used to delete unnecessary columns
  #sc.data <- sc.data[cols]
  sc.data$date <- NULL
  xts.data <- as.xts(sc.data, order.by = dates)
  xts.data$date <- NULL
  xts.data.num <- as.numeric(xts.data)
  #rm(cols)
  
  xts.data$price.rtn <- diff(xts.data$WeightedPrice,lag = 1)/lag(xts.data$WeightedPrice)
  xts.data$google.rtn <- diff(xts.data$googleSearch,lag = 1)/lag(xts.data$googleSearch, k=1)
  # xts.data$btctalk.rtn <- diff(xts.data$new_posts,lag = 1)
  # xts.data$users.rtn <- diff(xts.data$no_users,lag = 1)
  # xts.data$users.rtn <- diff(xts.data$users.rtn,lag = 1)
  # xts.data$wikipedia.rtn <- diff(xts.data$wikipedia,lag = 1)
  WeightedTweets <- (xts.data$nTweets/xts.data$totalTweets*1000000)
  xts.data$tweets.rtn <- diff(WeightedTweets,lag = 1)/lag(WeightedTweets, k=1)
  xts.data$new_users.rtn <- diff(xts.data$nUsersFilteredNet,lag = 1)/lag(xts.data$nUsersFilteredNet, k=1)
  
  xts.data$price.rtn[!is.finite(xts.data$price.rtn)] <- NA
  xts.data$google.rtn[!is.finite(xts.data$google.rtn)] <- NA
  # xts.data$btctalk.rtn[!is.finite(xts.data$btctalk.rtn)] <- NA
  # xts.data$wikipedia.rtn[!is.finite(xts.data$wikipedia.rtn)] <- NA
  xts.data$tweets.rtn[!is.finite(xts.data$tweets.rtn)] <- NA
  xts.data$new_users.rtn[!is.finite(xts.data$new_users.rtn)] <- NA

 # These lines were saved for later regressions with logs of vars instead of sole diffs 
  # xts.data$price.log.rtn <- diff(log(xts.data$price_usd),lag = 1)
  # xts.data$google.log.rtn <- diff(log(xts.data$google_tr_btc),lag = 1)
  # # xts.data$btctalk.log.rtn <- diff(log(xts.data$new_posts),lag = 1)
  # # xts.data$users.log.rtn <- diff(log(xts.data$no_users),lag = 1)
  # # xts.data$users.log.rtn <- diff(log(xts.data$users.log.rtn),lag = 1)
  # # xts.data$wikipedia.log.rtn <- diff(log(xts.data$wikipedia),lag = 1)
  # xts.data$tweets.log.rtn <- diff(log(xts.data$nTweets),lag = 1)
  # xts.data$new_users.log.rtn <- diff(log(xts.data$new_users),lag = 1)
  # 
  # xts.data$price.log.rtn[!is.finite(xts.data$price.log.rtn)] <- NA
  # xts.data$google.log.rtn[!is.finite(xts.data$google.log.rtn)] <- NA
  # # xts.data$btctalk.log.rtn[!is.finite(xts.data$btctalk.log.rtn)] <- NA
  # # xts.data$wikipedia.log.rtn[!is.finite(xts.data$wikipedia.log.rtn)] <- NA
  # xts.data$tweets.log.rtn[!is.finite(xts.data$tweets.log.rtn)] <- NA
  # xts.data$new_users.log.rtn[!is.finite(xts.data$new_users.log.rtn)] <- NA  
  
  
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
  xts.VAR <- xts.data[, setdiff(colnames(xts.data),c('price_usd',
                                                   'google_tr_btc',
                                                   'tweets','new_users'))]
  xts.VAR <- na.omit(xts.VAR)
  xts.VAR <- -xts.VAR[,-c(1:15)]
  xts.VAR <- xts.VAR['2010-07-18::2013-10-31']

  fit <- VAR(xts.VAR, type = 'both', ic="SC", lag.max=1, p = 1)
  VAR_estimation <- summary(fit)
  while (!is.null(dev.list()))  dev.off()
  # plot(fit)

# Impulse response functions for fitted VAR model
  ir1 <- irf(fit, ortho = F, n.ahead=12, boot=T, ci=0.95, runs = 5) # basic IR functions
  while (!is.null(dev.list()))  dev.off()
  plot(ir1)

  #ir2 <- irf(fit, ortho = T, n.ahead = 12, boot = F) # orthogonalized IR functions
                                                  # boot=T gives bootstrap confidence intervals, if you don't want them -> boot=F
  #plot(ir2)
