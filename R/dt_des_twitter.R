library('stargazer')
library('dplyr')
library('xts')

# > getwd()
# setwd('..')
# getwd()

print(paste('start: ', Sys.time()))
rm(list=ls())
# setwd('..')
print(getwd())
setwd(script.dir <- dirname(sys.frame(1)$ofile))
setwd('..')
setwd('./D_Data/')

# read input
dt.twitter <- read.csv(file=paste(getwd(), '/dt_twitter.csv', sep=''), header=TRUE, sep=",")

# delete all dates that have zero price value from start
# dt.twitter <- dt.twitter[apply(dt.twitter[c(2:2)],1,function(z) !any(z==0)),] 

# calcuate log-returns
dt.twitter$log.returns <- c(NA, diff(log(dt.twitter$tweets),lag = 1))

# calculate first differences
dt.twitter$first.differences <- c(NA, diff(dt.twitter$tweets,lag = 1))

# calculate percentage changes
dt.twitter$pct.changes <- dt.twitter$tweets / lag(dt.twitter$tweets, 1) - 1

# calculate 30day annualized volatility
dt.twitter <- as.xts(dt.twitter, order.by=as.Date(dt.twitter$date, format='%Y-%m-%d'))
dt.twitter <- dt.twitter[, colnames(dt.twitter) != 'date']
dt.twitter$vol_ann_30d <- rollapply(dt.twitter$log.returns,width=30, FUN=sd)*sqrt(365)

storage.mode(dt.twitter) <- "numeric"

# rename columns
# colnames(dt.twitter) = c('Date', 'Price', 'log.return', 'first.differences', 'pct.changes')
colnames(dt.twitter) = c('twitter', 'log.return', 'first.differences', 'pct.changes', 'ann_vol_30d')

dt.twitter$log.return[!is.finite(dt.twitter$log.return)] <- NA
stg.input <- data.frame(date = index(dt.twitter), dt.twitter$twitter, 
                        dt.twitter$log.return,
                        dt.twitter$first.differences,
                        dt.twitter$pct.changes,
                        dt.twitter$ann_vol_30d,
                        row.names = NULL)

# print(stargazer(dt.twitter))

# adf test (need to convert xts object to ts in order to apply adf test)
twitter.abs <- as.ts(dt.twitter$twitter)
twitter.abs <- na.remove(twitter.abs)
print(adf.test(twitter.abs, k = 23))

twitter.fd <- as.ts(dt.twitter$first.differences)
twitter.fd <- na.remove(twitter.fd)
print(adf.test(twitter.fd, k = 23))

twitter.log.return <- as.ts(dt.twitter$log.return)
twitter.log.return <- na.remove(twitter.log.return)
print(adf.test(twitter.log.return, k = 23))

print(paste('end: ', Sys.time()))