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
dt.wiki <- read.csv(file=paste(getwd(), '/dt_wiki.csv', sep=''), header=TRUE, sep=",")

# delete all dates that have zero price value from start
# dt.wiki <- dt.wiki[apply(dt.wiki[c(2:2)],1,function(z) !any(z==0)),] 

# calcuate log-returns
dt.wiki$log.returns <- c(NA, diff(log(dt.wiki$wikipedia),lag = 1))

# calculate first differences
dt.wiki$first.differences <- c(NA, diff(dt.wiki$wikipedia,lag = 1))

# calculate percentage changes
dt.wiki$pct.changes <- dt.wiki$wikipedia / lag(dt.wiki$wikipedia, 1) - 1

# calculate 30day annualized volatility
dt.wiki <- as.xts(dt.wiki, order.by=as.Date(dt.wiki$tstamp, format='%Y-%m-%d'))
dt.wiki <- dt.wiki[, colnames(dt.wiki) != 'tstamp']
dt.wiki$vol_ann_30d <- rollapply(dt.wiki$log.returns,width=30, FUN=sd)*sqrt(365)

storage.mode(dt.wiki) <- "numeric"

# rename columns
# colnames(dt.wiki) = c('Date', 'Price', 'log.return', 'first.differences', 'pct.changes')
colnames(dt.wiki) = c('wikipedia', 'log.return', 'first.differences', 'pct.changes', 'ann_vol_30d')

dt.wiki$log.return[!is.finite(dt.wiki$log.return)] <- NA
stg.input <- data.frame(date = index(dt.wiki), dt.wiki$wikipedia, 
                        dt.wiki$log.return,
                        dt.wiki$first.differences,
                        dt.wiki$pct.changes,
                        dt.wiki$ann_vol_30d,
                        row.names = NULL)

# print(stargazer(dt.wiki))

# adf test (need to convert xts object to ts in order to apply adf test)
wiki.abs <- as.ts(dt.wiki$wikipedia)
wiki.abs <- na.remove(wiki.abs)
print(adf.test(wiki.abs, k = 27))

wiki.fd <- as.ts(dt.wiki$first.differences)
wiki.fd <- na.remove(wiki.fd)
print(adf.test(wiki.fd, k = 27))

wiki.log.return <- as.ts(dt.wiki$log.return)
wiki.log.return <- na.remove(wiki.log.return)
print(adf.test(wiki.log.return, k = 27))

print(paste('end: ', Sys.time()))