# Granger Causality Tests for the Financial Asset serie

# package requirements: vars, tseries, forecast, strucchange, xts

library('tseries')
library('forecast')
library('vars')
library('strucchange')
library('xts')
library('stargazer')
library('xtable')
library('lmtest')

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
      'google',
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
  xts.data$google.log.rtn <- diff(log(xts.data$google),lag = 1)
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
  # par(mfrow=c(2,2))
  # plot(xts.data$price.log.rtn)
  # plot(xts.data$google.log.rtn)
  # plot(xts.data$btctalk.log.rtn)
  # plot(xts.data$users.log.rtn)
  # plot(xts.data$tweets.log.rtn)
  while (!is.null(dev.list()))  dev.off()
  
  
  
# granger casuality tests
  # The granger causality test is a statistical hypothesis test for determining 
  # whether one time series is useful in forecasting another. This test might help you to detect
  # the "best" predictors for Price of a bitcoin

  xts.granger <- xts.data
  xts.granger <- xts.data[, setdiff(colnames(xts.data),c('price',
                                                   'wikipedia',
                                                   'google',
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
  xts.granger <- na.omit(xts.granger)
  # xts.granger <- xts.granger['2014-01::2018-10']
  # xts.VAR <- ts(xts.VAR)

# Granger Casuality Tests ("xy granger-cause price")
  granger.price.xau <- grangertest(xts.granger$price.log.rtn ~ xts.granger$xau.log.rtn,
                              order = 1)
  granger.price.dxy <- grangertest(xts.granger$price.log.rtn ~ xts.granger$dxy.log.rtn,
                              order = 1)
  granger.price.spx <- grangertest(xts.granger$price.log.rtn ~ xts.granger$spx.log.rtn,
                              order = 1)
  granger.price.nvda <- grangertest(xts.granger$price.log.rtn ~ xts.granger$nvda.log.rtn,
                              order = 1)
  granger.price.qcom <- grangertest(xts.granger$price.log.rtn ~ xts.granger$qcom.log.rtn,
                              order = 1)
  granger.price.tsm <- grangertest(xts.granger$price.log.rtn ~ xts.granger$tsm.log.rtn,
                              order = 1)
  granger.price.amd <- grangertest(xts.granger$price.log.rtn ~ xts.granger$amd.log.rtn,
                              order = 1)
  granger.price.high.yield <- grangertest(xts.granger$price.log.rtn ~ xts.granger$high.yield.log.rtn,
                              order = 1)
  granger.price.global.govt <- grangertest(xts.granger$price.log.rtn ~ xts.granger$global.govt.log.rtn,
                              order = 1)
  granger.price.us.govt <- grangertest(xts.granger$price.log.rtn ~ xts.granger$us.govt.log.rtn,
                              order = 1)
  
# Granger Casuality Tests ("xy granger-cause Wikipedia")
  granger.wikipedia.xau <- grangertest(xts.granger$wikipedia.log.rtn ~ xts.granger$xau.log.rtn,
                                   order = 1)
  granger.wikipedia.dxy <- grangertest(xts.granger$wikipedia.log.rtn ~ xts.granger$dxy.log.rtn,
                                   order = 1)
  granger.wikipedia.spx <- grangertest(xts.granger$wikipedia.log.rtn ~ xts.granger$spx.log.rtn,
                                   order = 1)
  granger.wikipedia.nvda <- grangertest(xts.granger$wikipedia.log.rtn ~ xts.granger$nvda.log.rtn,
                                    order = 1)
  granger.wikipedia.qcom <- grangertest(xts.granger$wikipedia.log.rtn ~ xts.granger$qcom.log.rtn,
                                    order = 1)
  granger.wikipedia.tsm <- grangertest(xts.granger$wikipedia.log.rtn ~ xts.granger$tsm.log.rtn,
                                   order = 1)
  granger.wikipedia.amd <- grangertest(xts.granger$wikipedia.log.rtn ~ xts.granger$amd.log.rtn,
                                   order = 1)
  granger.wikipedia.high.yield <- grangertest(xts.granger$wikipedia.log.rtn ~ xts.granger$high.yield.log.rtn,
                                   order = 1)
  granger.wikipedia.global.govt <- grangertest(xts.granger$wikipedia.log.rtn ~ xts.granger$global.govt.log.rtn,
                                           order = 1)
  granger.wikipedia.us.govt <- grangertest(xts.granger$wikipedia.log.rtn ~ xts.granger$us.govt.log.rtn,
                                       order = 1)
  
# Granger Casuality Tests ("xy granger-cause Google")
  granger.google.xau <- grangertest(xts.granger$google.log.rtn ~ xts.granger$xau.log.rtn,
                                       order = 1)
  granger.google.dxy <- grangertest(xts.granger$google.log.rtn ~ xts.granger$dxy.log.rtn,
                                       order = 1)
  granger.google.spx <- grangertest(xts.granger$google.log.rtn ~ xts.granger$spx.log.rtn,
                                       order = 1)
  granger.google.nvda <- grangertest(xts.granger$google.log.rtn ~ xts.granger$nvda.log.rtn,
                                        order = 1)
  granger.google.qcom <- grangertest(xts.granger$google.log.rtn ~ xts.granger$qcom.log.rtn,
                                        order = 1)
  granger.google.tsm <- grangertest(xts.granger$google.log.rtn ~ xts.granger$tsm.log.rtn,
                                       order = 1)
  granger.google.amd <- grangertest(xts.granger$google.log.rtn ~ xts.granger$amd.log.rtn,
                                       order = 1)
  granger.google.high.yield <- grangertest(xts.granger$google.log.rtn ~ xts.granger$high.yield.log.rtn,
                                              order = 1)
  granger.google.global.govt <- grangertest(xts.granger$google.log.rtn ~ xts.granger$global.govt.log.rtn,
                                               order = 1)
  granger.google.us.govt <- grangertest(xts.granger$google.log.rtn ~ xts.granger$us.govt.log.rtn,
                                           order = 1)

# Granger Casuality Tests ("xy granger-cause Twitter")
  granger.tweets.xau <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$xau.log.rtn,
                                    order = 1)
  granger.tweets.dxy <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$dxy.log.rtn,
                                    order = 1)
  granger.tweets.spx <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$spx.log.rtn,
                                    order = 1)
  granger.tweets.nvda <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$nvda.log.rtn,
                                     order = 1)
  granger.tweets.qcom <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$qcom.log.rtn,
                                     order = 1)
  granger.tweets.tsm <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$tsm.log.rtn,
                                    order = 1)
  granger.tweets.amd <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$amd.log.rtn,
                                    order = 1)
  granger.tweets.high.yield <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$high.yield.log.rtn,
                                           order = 1)
  granger.tweets.global.govt <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$global.govt.log.rtn,
                                            order = 1)
  granger.tweets.us.govt <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$us.govt.log.rtn,
                                        order = 1)
  granger.tweets.wikipedia <- grangertest(xts.granger$tweets.log.rtn ~ xts.granger$wikipedia.log.rtn,
                                        order = 1)
  
  series <- c('XAU', 'DXY', 'SPX', 'NVDA', 'QCOM', 'TSM', 'AMD', 
              'High Yield', 'Global Gov', 'US Gov')
# store (price granger-caused by xy)  
  price.f <- c(granger.price.xau $F[2],
               granger.price.dxy $F[2],
               granger.price.spx $F[2],
               granger.price.nvda $F[2],
               granger.price.qcom $F[2],
               granger.price.tsm $F[2],
               granger.price.amd $F[2],
               granger.price.high.yield $F[2],
               granger.price.global.govt $F[2],
               granger.price.us.govt $F[2])
  
  price.p <- c(granger.price.xau $`Pr(>F)`[2],
               granger.price.dxy $`Pr(>F)`[2],
               granger.price.spx $`Pr(>F)`[2],
               granger.price.nvda $`Pr(>F)`[2],
               granger.price.qcom $`Pr(>F)`[2],
               granger.price.tsm $`Pr(>F)`[2],
               granger.price.amd $`Pr(>F)`[2],
               granger.price.high.yield $`Pr(>F)`[2],
               granger.price.global.govt $`Pr(>F)`[2],
               granger.price.us.govt $`Pr(>F)`[2])
  
  # store wikipedia (price granger-caused by xy)  
    wikipedia.f <- c(granger.wikipedia.xau $F[2],
                 granger.wikipedia.dxy $F[2],
                 granger.wikipedia.spx $F[2],
                 granger.wikipedia.nvda $F[2],
                 granger.wikipedia.qcom $F[2],
                 granger.wikipedia.tsm $F[2],
                 granger.wikipedia.amd $F[2],
                 granger.wikipedia.high.yield $F[2],
                 granger.wikipedia.global.govt $F[2],
                 granger.wikipedia.us.govt $F[2])
    
    wikipedia.p <- c(granger.wikipedia.xau $`Pr(>F)`[2],
                 granger.wikipedia.dxy $`Pr(>F)`[2],
                 granger.wikipedia.spx $`Pr(>F)`[2],
                 granger.wikipedia.nvda $`Pr(>F)`[2],
                 granger.wikipedia.qcom $`Pr(>F)`[2],
                 granger.wikipedia.tsm $`Pr(>F)`[2],
                 granger.wikipedia.amd $`Pr(>F)`[2],
                 granger.wikipedia.high.yield $`Pr(>F)`[2],
                 granger.wikipedia.global.govt $`Pr(>F)`[2],
                 granger.wikipedia.us.govt $`Pr(>F)`[2])
    
  # store google (price granger-caused by xy)  
    google.f <- c(granger.google.xau $F[2],
                     granger.google.dxy $F[2],
                     granger.google.spx $F[2],
                     granger.google.nvda $F[2],
                     granger.google.qcom $F[2],
                     granger.google.tsm $F[2],
                     granger.google.amd $F[2],
                     granger.google.high.yield $F[2],
                     granger.google.global.govt $F[2],
                     granger.google.us.govt $F[2])
    
    google.p <- c(granger.google.xau $`Pr(>F)`[2],
                     granger.google.dxy $`Pr(>F)`[2],
                     granger.google.spx $`Pr(>F)`[2],
                     granger.google.nvda $`Pr(>F)`[2],
                     granger.google.qcom $`Pr(>F)`[2],
                     granger.google.tsm $`Pr(>F)`[2],
                     granger.google.amd $`Pr(>F)`[2],
                     granger.google.high.yield $`Pr(>F)`[2],
                     granger.google.global.govt $`Pr(>F)`[2],
                     granger.google.us.govt $`Pr(>F)`[2])    
    
  # store tweets (price granger-caused by xy)  
    tweets.f <- c(granger.tweets.xau $F[2],
                  granger.tweets.dxy $F[2],
                  granger.tweets.spx $F[2],
                  granger.tweets.nvda $F[2],
                  granger.tweets.qcom $F[2],
                  granger.tweets.tsm $F[2],
                  granger.tweets.amd $F[2],
                  granger.tweets.high.yield $F[2],
                  granger.tweets.global.govt $F[2],
                  granger.tweets.us.govt $F[2])
    
    tweets.p <- c(granger.tweets.xau $`Pr(>F)`[2],
                  granger.tweets.dxy $`Pr(>F)`[2],
                  granger.tweets.spx $`Pr(>F)`[2],
                  granger.tweets.nvda $`Pr(>F)`[2],
                  granger.tweets.qcom $`Pr(>F)`[2],
                  granger.tweets.tsm $`Pr(>F)`[2],
                  granger.tweets.amd $`Pr(>F)`[2],
                  granger.tweets.high.yield $`Pr(>F)`[2],
                  granger.tweets.global.govt $`Pr(>F)`[2],
                  granger.tweets.us.govt $`Pr(>F)`[2])
  
# combine granger test results into data-frame
    granger.results <- data.frame(series, price.f, price.p, wikipedia.f, wikipedia.p,
                                  google.f, google.p, tweets.f, tweets.p)
    
  
  while (!is.null(dev.list()))  dev.off()
  # plot(fit)
  
# end
  print('financial assets granger causalities calculated')
  print(paste('end: ', Sys.time()))