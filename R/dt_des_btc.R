library('stargazer')
library('dplyr')
library('xts')

# > getwd()
# setwd('..')
# getwd()

print(paste('start: ', Sys.time()))

# setwd('..')
print(getwd())
setwd(script.dir <- dirname(sys.frame(1)$ofile))
setwd('..')
setwd('./D_Data/B_Bitcoin_com/')

# read input
dt.btc.com <- read.csv(file=paste(getwd(), '/price.csv', sep=''), header=TRUE, sep=",")

# delete all dates that have zero price value from start
dt.btc.com <- dt.btc.com[apply(dt.btc.com[c(2:2)],1,function(z) !any(z==0)),] 

# calcuate log-returns
dt.btc.com$log.returns <- c(NA, diff(log(dt.btc.com$Bitcoin.Price),lag = 1))

# calculate first differences
dt.btc.com$first.differences <- c(NA, diff(dt.btc.com$Bitcoin.Price,lag = 1))

# calculate percentage changes
dt.btc.com$pct.changes <- dt.btc.com$Bitcoin.Price / lag(dt.btc.com$Bitcoin.Price, 1) - 1
# dt.btc.com$pct.changes <- 0

# calculate 30day annualized volatility
dt.btc.com <- as.xts(dt.btc.com, order.by=as.Date(dt.btc.com$Date, format='%d-%m-%y'))
dt.btc.com <- dt.btc.com[, colnames(dt.btc.com) != 'Date']
dt.btc.com$vol_ann_30d <- rollapply(dt.btc.com$log.returns,width=30, FUN=sd)*sqrt(365)

storage.mode(dt.btc.com) <- "numeric"

# rename columns
# colnames(dt.btc.com) = c('Date', 'Price', 'log.return', 'first.differences', 'pct.changes')
colnames(dt.btc.com) = c('Price', 'log.return', 'first.differences', 'pct.changes', 'ann_vol_30d')

stg.input <- data.frame(date = index(dt.btc.com), dt.btc.com$Price, 
                        dt.btc.com$log.return,
                        dt.btc.com$first.differences,
                        dt.btc.com$pct.changes,
                        dt.btc.com$ann_vol_30d,
                        row.names = NULL)

# print(stargazer(dt.btc.com))

print(paste('end: ', Sys.time()))