# Outlier removal: find the number of events a user must have in order to be 
# considered an outlier. Assume we cut off at the 80th percentile.
events <- read.csv("events.csv", header = TRUE)
events.expanded = rep(events$event_count, events$user_count)
summary(events.expanded)
# 80% of users had more than 3 events
quantile(events.expanded, 0.2)
# 50% of users had more than 33 events
quantile(events.expanded, 0.5)
# 20% of users had more than 50 events
quantile(events.expanded, 0.8)
