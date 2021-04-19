# Title     : TODO
# Objective : TODO
# Created by: rohit
# Created on: 10/2/20
marks <- c(78, 85, 90)

status <- ifelse(marks >= 80, "Above Average", "Average")
#head(ifelse(c(78, 85, 90) < 80, "Average", "Above Average"))
print(status)