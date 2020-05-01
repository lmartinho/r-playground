library(tidyverse)
n <- 100000

#df <- data.frame(1:n, runif(n, 0, 6))
df <- data.frame(1:n, rnorm(n, 0, 1))
names(df) <- c('x', 'y')
ggplot(data=df, aes(x=x,y=y)) + geom_point() 
hist(df$y)
mean(df$y)

# Compactly Display the Structure of an Arbitrary R Object
str(df)

# Write an Object to a File or Recreate it
dput(df)

df2x = list(x=c(1,2,3), y=c(2,4,6))
df2x_str = structure(df2x)
#scatter.smooth(x=df2x$x, y=df2x$y, main="X ~ Y")
