#*# Maikl VAR code Bitcoin Master #*#

#install.packages("vars")
#install.packages("tseries")
#install.packages("forecast")
#install.packages("strucchange")

library("tseries")
library("forecast")
library("vars")
library("strucchange")

# start
  print(paste('start: ', Sys.time()))
  
# directories 
  # setwd('..')
  print(getwd())
  # setwd(script.dir <- dirname(sys.frame(1)$ofile))
  setwd('..')
  setwd('./D_Data/')

  wd <- getwd()
  x = read.csv(paste(getwd(), '/dt_aggregated.csv', sep=''), header=TRUE, sep=";")

  Price=x$price_usd_fd
  Google=x$google_tr_fd
  Wikipedia=x$wikipedia_fd

### Create time series ###
  Price_ts=ts(Price, start=c(2015,7,1),end=c(2017,8,30),frequency=365)
  Google_ts=ts(Google, start=c(2015,7,1),end=c(2017,8,30),frequency=365)
  Wikipedia_ts=ts(Wikipedia, start=c(2015,7,1),end=c(2017,8,30),frequency=365)
  Bitcoin=cbind(Price_ts,Google_ts,Wikipedia_ts)
  Bitcoin_ts=ts(Bitcoin, start=c(2015,7,1),end=c(2017,8,30),frequency=365)

### starting with simple plot to see how time series look like ###
  plot(Price_ts)
  plot(Google_ts)
  plot(Wikipedia_ts)   # if they look stationary, okay to proceed with VAR. Here one could also do some Dickey-Fuller tests to have a more sophisticated evidence of stationarity


### Chow test for 1 structural break ###
regP <- lm(Price_ts[1:800]~Google_ts[1:800] + Wikipedia_ts[1:800]) # Choose time span
summary(regP)
regP$df
rssP <- sum(residuals(regP)^2)
rssP

regA <- lm(Price_ts[1:400]~Google_ts[1:400] + Wikipedia_ts[1:400]) # Time span before assumed structural break point
summary(regA)
regA$df
rssA <- sum(residuals(regA)^2)
rssA

regB <- lm(Price_ts[401:800]~Google_ts[401:800] + Wikipedia_ts[401:800]) # Time span after assumed structural break point
summary(regB)
regB$df
rssB <- sum(residuals(regB)^2)
rssB

k=3 # Number of variables in equation (including intercept)

fcrit=qf(.95,df1=regA$df,df2=regB$df)
fcrit
Chow_Statistic=((rssP-(rssA+rssB))/k)/((rssA+rssB)/(regA$df+regB$df-(2*k)))
Chow_Statistic # If value of Chow-statistic bigger than critical F-value, then reject Null-Hypothesis of NO structural break


### General structural break test (more than one break possible) ###
plot(Price_ts)
bp.Price=breakpoints(Price_ts~1) # further specifications:  h=0.15, breaks=3
ci.Price=confint(bp.Price,breaks=1)
lines(ci.Price)


## Correlograms
#acf(x, 5)
#values=acf(x)
#values # to see the exact numerical value of the autocorrelations


### Creating first differences, because ts are I(1) ###)
#diff.ts(x, lag=1,differences=1) # first order differences at lag 1 of time series


### Starting with the real shit (VAR estimation) ###

VAR(Bitcoin, p=1) # p stands for number of lags one wants to implement

fit=VAR(Bitcoin,type = "both", ic="SC", lag.max=1) # type both uses intercept and 
                                               #linear trend for VAR, ic takes BIC as criterion for best model
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
