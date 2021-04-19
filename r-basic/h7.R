# Title     : Handling NA
# Objective : TODO
# Created by: rohit
# Created on: 10/2/20

v <- c(1,4,NA,7,9,NA,2)
v <- v[!is.na(v)]
v <- v[v%%2==0]
print(v)