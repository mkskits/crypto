#Maikl VAR code Bitcoin Master


#install.packages("vars")
#install.packages("tseries")
#install.packages("forecast")

library("tseries")
library("forecast")
library("vars")

wd <- "C:/Users/Ueli/Documents/Documents/Studium/Master/Michi_MasterThesis"

x = read.csv("C:/Users/Ueli/Documents/Documents/Studium/Master/Michi_MasterThesis/data_aggregated.csv", header=TRUE, sep=";")

Price=x$price_usd_fd
Google=x$google_tr_fd
Wikipedia=x$wikipedia_fd

Bitcoin=cbind(Price_ts,Google_ts,Wikipedia_ts)
Bitcoin_ts=ts(Bitcoin, start=c(2015,7,1),end=c(2017,8,30),frequency=365)


#x = ts(x, freq=365, start=c(2013,1)
# starting with simple plot to see how time series look like

plot(Price)
plot(Google)
plot(Wikipedia)   # if they look stationary, okay to proceed with VAR. Here one could also do some Dickey-Fuller tests to have a more sophisticated evidence of stationarity

## Correlograms

#acf(x, 5)
#values=acf(x)
#values # to see the exact numerical value of the autocorrelations


# Creating first differences, because ts are I(1)

#diff.ts(x, lag=1,differences=1) # first order differences at lag 1 of time series


### Starting with the real shit ###

VAR(Bitcoin, p=1) # p stands for number of lags one wants to implement

fit=VAR(Bitcoin,type = "both", ic="SC", lag.max=1) # type both uses intercept and 
                                               #linear trend for VAR, ic takes BIC as criterion for best model
VAR_estimation=summary(fit)
VAR_estimation
plot(fit)

serial.test(fit, lags.pt=10) #Portmanteau test, combined over all components. This function computes the multivariate Portmanteau- and Breusch-Godfrey test for serially correlated
errors.

causality(fit, cause = NULL, vcov.=NULL, boot=FALSE, boot.runs=100) #Computes the test statistics for Granger- and Instantaneous causality for a VAR(p).

## Impulse response functions for fitted VAR model ##

Impulse_Responses=irf(fit, ortho = F, n.ahead=12, boot=T) # basic IR functions

irf.ortho(fit, ortho = T, n.ahead = 12, boot = T) # orthogonalized IR functions
                                            # boot=T gives bootstrap confidence intervals, if you don't want them -> boot=F
plot(Impulse_Responses)
plot(irf.ortho)

## Computing forecasts and prediction intervals

Forecasts=predict(fit, n.ahead=12, ci=0.95) # 12 periods forecast together with 95% conf. intervals

plot(Forecasts)  #plot(predict)pos originally, but didnt work
