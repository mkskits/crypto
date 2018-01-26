###Structural Break test ###

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
setwd('./B_Bitcoin_com/')
wd <- getwd()

data.price <- read.csv(paste(getwd(), '/price.csv', sep=''), header=TRUE, sep=",")

# data input 
wd <- "C:/Users/Ueli/Dropbox/G_GIT/D_DATA/B_Bitcoin_com"
data.price = read.csv("C:/Users/Ueli/Dropbox/G_GIT/D_DATA/B_Bitcoin_com/price.csv", header=TRUE, sep=";")

Price=data.price$BitcoinPrice
Price_ts=ts(Price, start=c(2009,1,10),end=c(2017,12,31),frequency=365)

### General structural break test (more than one break possible) ###
plot(Price_ts)
bp.Price=breakpoints(Price_ts~1, breaks = 1) # further specifications:  h=0.15, breaks=3
ci.Price=confint(bp.Price)
lines(ci.Price)
bp.Price  # Breakdate: 2013(301) which is 05.11.2013


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




# serial.test(fit, lags.pt=10) # Portmanteau test, combined over all components. This function computes the multivariate Portmanteau- 
# and Breusch-Godfrey test for serially correlatederrors.

# Granger-Causality test ##
# causality(fit, cause = NULL, vcov.=vcovHC(fit), boot=TRUE, boot.runs=1000) # Computes the test statistics for Granger- and Instantaneous causality for a VAR(p). 
# The Granger causality test is a statistical hypothesis test for determining 
# whether one time series is useful in forecasting another. This test might help you to detect
# the "best" predictors for Price of a bitcoin

# Computing forecasts and prediction intervals
# Forecasts=predict(fit, n.ahead=12, ci=0.95) # 12 periods forecast together with 95% conf. intervals

# plot(Forecasts, xlab="Year")  #plot(predict)pos originally, but didnt work
#ir2 <- irf(fit, ortho = T, n.ahead = 12, boot = F) # orthogonalized IR functions
# boot=T gives bootstrap confidence intervals, if you don't want them -> boot=F
#plot(ir2)