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
setwd('./D_DATA/B_Bitcoin_com/')
wd <- getwd()

dt.btc.com <- read.csv(paste(getwd(), '/price.csv', sep=''), header=TRUE, sep=";")
# delete all dates that have zero price value from start
dt.btc.com <- dt.btc.com[apply(dt.btc.com[c(2:2)],1,function(z) !any(z==0)),] 
dt.btc.com <- as.xts(dt.btc.com, order.by=as.Date(dt.btc.com$Date, format='%d.%m.%Y'))
dt.btc.com <- dt.btc.com[, colnames(dt.btc.com) != 'Date']
storage.mode(dt.btc.com) <- "numeric"

Price_ts <- as.ts(dt.btc.com$BitcoinPrice)

# General structural break test (more than one break possible) #
bp.Price <- breakpoints(dt.btc.com$BitcoinPrice~1, h = 180, breaks = 6, format.times = TRUE) 
summary(bp.Price)
plot(bp.Price)
plot(Price_ts)
lines(bp.Price)
ci.Price <- confint(bp.Price)
lines(ci.Price)
