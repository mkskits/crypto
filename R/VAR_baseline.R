# VAR specification

# package requirements: vars, tseries, forecast, strucchange, xts

library('tseries')
library('forecast')
library('vars')
library('strucchange')
library('xts')

# start
  print(paste('start: ', Sys.time()))
  
# directories 
  # setwd('..')
  print(getwd())
  # setwd(script.dir <- dirname(sys.frame(1)$ofile))
  setwd('..')
  setwd('./D_Data/')
  wd <- getwd()

# data input 
  data <- read.csv(paste(getwd(), '/dt_aggregated.csv', sep=''), header=TRUE, sep=",")
  dates <- as.Date(data$date, format = '%d.%m.%y')
  cols <- names(data) %in% c('price_usd', 'google_tr_btc', 'wikipedia', 'no_users', 'new_posts') 
  data <- data[cols]
  xts.data <- as.xts(data, order.by = dates)
  rm(cols)
  
  xts.data$price.log.rtn <- diff(log(xts.data$price_usd),lag = 1)
  xts.data$google.log.rtn <- diff(log(xts.data$google_tr_btc),lag = 1)
  # xts.data$wikipedia.log.rtn <- diff(log(xts.data$wikipedia),lag = 1)
  
  xts.data$price.log.rtn[!is.finite(xts.data$price.log.rtn)] <- NA
  xts.data$google.log.rtn[!is.finite(xts.data$google.log.rtn)] <- NA
  # xts.data$wikipedia.log.rtn[!is.finite(xts.data$wikipedia.log.rtn)] <- NA

# simple plots - data review
  plot(xts.data$price.log.rtn)
  plot(xts.data$google.log.rtn)
  plot(xts.data$wikipedia.log.rtn)

## Correlograms
#acf(x, 5)
#values=acf(x)
#values # to see the exact numerical value of the autocorrelations

# VAR estimation
xts.VAR <- xts.data
xts.VAR <- xts.data[, setdiff(colnames(xts.data),c('price_usd','wikipedia','google_tr_btc')) ]
xts.VAR <- na.omit(xts.VAR)

VAR(xts.VAR, p = 1) # p stands for number of lags one wants to implement

fit = VAR(Bitcoin, type = "both", ic="SC", lag.max=1) 
  # type both uses intercept and linear trend 
  # for VAR, ic takes BIC as criterion for best model
VAR_estimation=summary(fit)
VAR_estimation
plot(fit)

serial.test(fit, lags.pt=10) # Portmanteau test, combined over all components. This function computes the multivariate Portmanteau- 
                             # and Breusch-Godfrey test for serially correlatederrors.


## Granger-Causality test ##
causality(fit, cause = NULL, vcov.=vcovHC(fit), boot=TRUE, boot.runs=1000) # Computes the test statistics for Granger- and Instantaneous causality for a VAR(p). 
                                                                           # The Granger causality test is a statistical hypothesis test for determining 
                                                                           # whether one time series is useful in forecasting another. This test might help you to detect
                                                                           # the "best" predictors for Price of a bitcoin

### Impulse response functions for fitted VAR model ###
Impulse_Responses=irf(fit, ortho = F, n.ahead=12, boot=T) # basic IR functions

irf.ortho(fit, ortho = T, n.ahead = 12, boot = T) # orthogonalized IR functions
                                                  # boot=T gives bootstrap confidence intervals, if you don't want them -> boot=F
plot(Impulse_Responses)
plot(irf.ortho)


### Computing forecasts and prediction intervals ###
Forecasts=predict(fit, n.ahead=12, ci=0.95) # 12 periods forecast together with 95% conf. intervals

plot(Forecasts, xlab="Year")  #plot(predict)pos originally, but didnt work



