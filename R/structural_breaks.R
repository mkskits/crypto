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
