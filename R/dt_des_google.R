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
dt.google <- read.csv(file=paste(getwd(), '/dt_google_daily.csv', sep=''), header=TRUE, sep=",")

# delete all dates that have zero price value from start
# dt.google <- dt.google[apply(dt.google[c(2:2)],1,function(z) !any(z==0)),] 

# calcuate log-returns
dt.google$log.returns <- c(NA, diff(log(dt.google$google),lag = 1))

# calculate first differences
dt.google$first.differences <- c(NA, diff(dt.google$google,lag = 1))

# calculate percentage changes
dt.google$pct.changes <- dt.google$google / lag(dt.google$google, 1) - 1

# calculate 30day annualized volatility
dt.google <- as.xts(dt.google, order.by=as.Date(dt.google$X, format='%Y-%m-%d'))
dt.google <- dt.google[, colnames(dt.google) != 'X']
dt.google$vol_ann_30d <- rollapply(dt.google$log.returns,width=30, FUN=sd)*sqrt(365)

storage.mode(dt.google) <- "numeric"

# rename columns
# colnames(dt.google) = c('Date', 'Price', 'log.return', 'first.differences', 'pct.changes')
colnames(dt.google) = c('google', 'segment', 'log.return', 'first.differences', 'pct.changes', 'ann_vol_30d')

dt.google$log.return[!is.finite(dt.google$log.return)] <- NA
stg.input <- data.frame(date = index(dt.google), dt.google$google, 
                        dt.google$log.return,
                        dt.google$first.differences,
                        dt.google$pct.changes,
                        dt.google$ann_vol_30d,
                        row.names = NULL)

# print(stargazer(dt.google))

print(paste('end: ', Sys.time()))