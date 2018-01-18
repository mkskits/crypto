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
      'tweets',
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
  
  xts.data$price.log.rtn <- diff(log(xts.data$price),lag = 1)
  # xts.data$google.log.rtn <- diff(log(xts.data$google),lag = 1)
  xts.data$wikipedia.log.rtn <- diff(log(xts.data$wikipedia),lag = 1)
  xts.data$tweets.log.rtn <- diff(log(xts.data$tweets),lag = 1)
  xts.data$new_users.log.rtn <- diff(log(xts.data$new_users),lag = 1)
  # addition to baseline_a
  # xts.data$new_topcis.log.rtn <- diff(log(xts.data$new_topics),lag = 1)
  # xts.data$new_posts.log.rtn <- diff(log(xts.data$new_posts),lag = 1)
  
  # replace inf / -inf log-returns with NA (case for 4 points out of 793)
    # xts.data$new_topcis.log.rtn[!is.finite(xts.data$new_topcis.log.rtn)] <- NA
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
                                                   'tweets',
                                                   'new_users'
                                                   # addition to baseline_a
                                                   # 'new_topics'
                                                   #'new_posts'
                                                   ))]
                                                   
  xts.VAR <- na.omit(xts.VAR)
  xts.VAR <- xts.VAR['2014-01::2018-10']

  # xts.VAR <- ts(xts.VAR)
  fit <- VAR(xts.VAR, type = 'none', ic="SC", lag.max=2, p = 2)
  VAR_estimation <- summary(fit)
  while (!is.null(dev.list()))  dev.off()
  # plot(fit)
  
  print(xtable(VAR_estimation$varresult$price.log.rtn))
  print(xtable(VAR_estimation$varresult$wikipedia.log.rtn))
  print(xtable(VAR_estimation$varresult$tweets.log.rtn))
  print(xtable(VAR_estimation$varresult$new_users.log.rtn))
  
# Impulse response functions for fitted VAR model
# Social Feedback Cycle
  # information search (impulse: price - respone: search)
    ir_search <- irf(fit, impulse = c('price.log.rtn'), response = c('wikipedia.log.rtn'),
                      ortho = T, n.ahead=12, boot=T, ci=0.95, runs = 100) # basic IR functions
    while (!is.null(dev.list()))  dev.off()
    # ir1$irf$wikipedia.log.rtn = 100 * ir1$irf$wikipedia.log.rtn
    pdf('../F_Figs/pt_fit_baseline_a_search.pdf')
    plot(ir_search, main='', xlab='', ylab='Information Search Response',
         sub='t (days)', xlim=c(1, 10),
         cex.axis = 2, cex.main = 2, cex=2, cex.lab = 2,
         oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
    dev.off()
    print('information search (impulse: price - respone: search)')
  
  # information sharing (impulse: search - respone: sharing)
    ir_sharing <- irf(fit, impulse = c('wikipedia.log.rtn'), response = c('tweets.log.rtn'),
               ortho = T, n.ahead=12, boot=T, ci=0.95, runs = 100) # basic IR functions
    while (!is.null(dev.list()))  dev.off()
    # ir1$irf$wikipedia.log.rtn = 100 * ir1$irf$wikipedia.log.rtn
    pdf('../F_Figs/pt_fit_baseline_a_sharing.pdf')
    plot(ir_sharing, main='', xlab='', ylab='Information Sharing Response',
         sub='t (days)', xlim=c(1, 10),
         cex.axis = 2, cex.main = 2, cex=2, cex.lab = 2,
         oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
    dev.off()
    print('information sharing (impulse: search - respone: sharing)')
    
  # Price (impulse: sharing - respone: price)
    ir_price_s <- irf(fit, impulse = c('tweets.log.rtn'), response = c('price.log.rtn'),
                      ortho = T, n.ahead=12, boot=T, ci=0.95, runs = 100) # basic IR functions
    while (!is.null(dev.list()))  dev.off()
    # ir1$irf$wikipedia.log.rtn = 100 * ir1$irf$wikipedia.log.rtn
    pdf('../F_Figs/pt_fit_baseline_a_price_s.pdf')
    plot(ir_price_s, main='', xlab='', ylab='Price Response',
         sub='t (days)', xlim=c(1, 10),
         cex.axis = 2, cex.main = 2, cex=2, cex.lab = 2,
         oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
    dev.off()
    print('Price (impulse: sharing - respone: price)')
    
# User adoption Cycle  
  # Adoption (impulse: search - respone: users)
    ir_adoption <- irf(fit, impulse = c('wikipedia.log.rtn'), response = c('new_users.log.rtn'),
                    ortho = T, n.ahead=12, boot=T, ci=0.95, runs = 100) # basic IR functions
    while (!is.null(dev.list()))  dev.off()
    # ir1$irf$wikipedia.log.rtn = 100 * ir1$irf$wikipedia.log.rtn
    pdf('../F_Figs/pt_fit_baseline_a_adoption.pdf')
    plot(ir_adoption, main='', xlab='', ylab='New Users Response',
         sub='t (days)', xlim=c(1, 10),
         cex.axis = 2, cex.main = 2, cex=2, cex.lab = 2,
         oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
    dev.off()  
    print('Adoption (impulse: search - respone: users)')
    
  #  Price (from adoption) (impulse: users - respone: price)
    ir_price_a <- irf(fit, impulse = c('new_users.log.rtn'), response = c('price.log.rtn'),
                       ortho = T, n.ahead=12, boot=T, ci=0.95, runs = 100) # basic IR functions
    while (!is.null(dev.list()))  dev.off()
    # ir1$irf$wikipedia.log.rtn = 100 * ir1$irf$wikipedia.log.rtn
    pdf('../F_Figs/pt_fit_baseline_a_price_a.pdf')
    plot(ir_price_a, main='', xlab='', ylab='New Users Response',
         sub='t (days)', xlim=c(1, 10),
         cex.axis = 2, cex.main = 2, cex=2, cex.lab = 2,
         oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
    dev.off()  
    print('Price (from adoption) (impulse: users - respone: price)')
    
  #  Price (impulse: seach - respone: price)
    ir_price_d <- irf(fit, impulse = c('wikipedia.log.rtn'), response = c('price.log.rtn'),
                      ortho = T, n.ahead=12, boot=T, ci=0.95, runs = 100) # basic IR functions
    while (!is.null(dev.list()))  dev.off()
    # ir1$irf$wikipedia.log.rtn = 100 * ir1$irf$wikipedia.log.rtn
    pdf('../F_Figs/pt_fit_baseline_a_price_d.pdf')
    plot(ir_price_d, main='', xlab='', ylab='Price Response',
         sub='t (days)', xlim=c(1, 10),
         cex.axis = 2, cex.main = 2, cex=2, cex.lab = 2,
         oma=c(5.5,0,0.3,0), mar=c(0,5,2,0.1))
    dev.off()  
    print('Price (direct - from search) (impulse: seach - respone: price)')