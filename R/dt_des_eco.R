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
setwd('./D_Data/C_Blockchain')

# read input
dt.eco <- read.csv(file=paste(getwd(), '/C-bitcoin-user_stats_base-heur_8ci_3.day.csv', sep=''), header=TRUE, sep=",")

# delete all dates that have zero price value from start
# dt.eco <- dt.eco[apply(dt.eco[c(2:2)],1,function(z) !any(z==0)),] 

# calcuate log-returns
dt.eco$new.users.log.returns <- c(NA, diff(log(dt.eco$new_users),lag = 1))
dt.eco$new.transactions.log.returns <- c(NA, diff(log(dt.eco$new_transactions),lag = 1))
dt.eco$new.curr.transacted.log.returns <- c(NA, diff(log(dt.eco$new_curr_transacted),lag = 1))

# storage.mode(dt.eco) <- "numeric"

# rename columns
# colnames(dt.eco) = c('Date', 'Price', 'log.return', 'first.differences', 'pct.changes')
#colnames(dt.eco) = c('google', 'segment', 'log.return', 'first.differences', 'pct.changes', 'ann_vol_30d')

dt.eco$new.users.log.returns[!is.finite(dt.eco$new.users.log.returns)] <- NA
dt.eco$new.transactions.log.returns[!is.finite(dt.eco$new.transactions.log.returns)] <- NA
dt.eco$new.curr.transacted.log.returns[!is.finite(dt.eco$new.curr.transacted.log.returns)] <- NA

stg.input <- data.frame(
                        dt.eco$new_users,
                        dt.eco$new_transactions,
                        dt.eco$new_curr_transacted,
                        dt.eco$new.users.log.returns,
                        dt.eco$new.transactions.log.returns,
                        dt.eco$new.curr.transacted.log.returns,
                        row.names = NULL)

# print(stargazer(dt.eco))

# calculate ADF test us govt
new.users <- as.ts(dt.eco$new_users)
k <- floor(12*((NROW(na.omit(new.users))/100)^0.25))
print(paste('new users adf test results', ' lags = ', k, sep=''))
adf.new.users <- adf.test(new.users, k = k)

# calculate ADF test log-returns new.users
log.new.users <- as.ts(dt.eco$new.users.log.returns)
k <- floor(12*((NROW(na.remove(log.new.users))/100)^0.25))
log.new.users <- na.remove(log.new.users)
print(paste('log-returns new.users adf test results', ' lags = ', k, sep=''))
adf.log.new.users <- adf.test(log.new.users, k = k)

# calculate ADF test us govt
new.transactions <- as.ts(dt.eco$new_transactions)
k <- floor(12*((NROW(na.remove(new.transactions))/100)^0.25))
print(paste('new users adf test results', ' lags = ', k, sep=''))
adf.new.transactions <- adf.test(new.transactions, k = k)


# calculate ADF test log-returns new.transactions
log.new.transactions <- as.ts(dt.eco$new.transactions.log.returns)
k <- floor(12*((NROW(na.remove(log.new.transactions))/100)^0.25))
log.new.transactions <- na.remove(log.new.transactions)
print(paste('log-returns new.transactions adf test results', ' lags = ', k, sep=''))
adf.log.new.transactions <- adf.test(log.new.transactions, k = k)

# calculate ADF test us govt
new.curr.transacted <- as.ts(dt.eco$new_curr_transacted)
k <- floor(12*((NROW(na.remove(new.curr.transacted))/100)^0.25))
print(paste('new users adf test results', ' lags = ', k, sep=''))
adf.new.curr.transacted <- adf.test(new.curr.transacted, k = k)

# calculate ADF test log-returns new.curr.transacteds
log.new.curr.transacted <- as.ts(dt.eco$new.curr.transacted.log.returns)
k <- floor(12*((NROW(na.remove(log.new.curr.transacted))/100)^0.25))
log.new.curr.transacted <- na.remove(log.new.curr.transacted)
print(paste('log-returns new.curr.transacted adf test results', ' lags = ', k, sep=''))
adf.log.new.curr.transacted <- adf.test(log.new.curr.transacted, k = k)


series <- c('New Users', 'New Transactions', 'Transaction Value', 
            'FD New Users (log)', 'New Transactions (log)', 'Transaction Value (log)')
            

df <- c(adf.new.users$statistic,
        adf.new.transactions$statistic,
        adf.new.curr.transacted$statistic,
        
        adf.log.new.users$statistic,
        adf.log.new.transactions$statistic,
        adf.log.new.curr.transacted$statistic
        )

dfp <- c(adf.new.users$p.value,
         adf.new.transactions$p.value,
         adf.new.curr.transacted$p.value,
         
         adf.log.new.users$p.value,
         adf.log.new.transactions$p.value,
         adf.log.new.curr.transacted$p.value
          )

adf.eco <- data.frame(series, df, dfp)

print(paste('end: ', Sys.time()))