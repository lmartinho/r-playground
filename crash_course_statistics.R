library(ggplot2)

pasta <- read.csv("crash_course_statistics_5_pasta.csv", header = TRUE)
pasta$Total <- pasta$White + pasta$Red

ggplot(pasta, aes(x = Pasta.Type, y = Total)) + 
  # geom_col() makes the heights of the bars represent values in the data
  # and it uses stat_identity(), while geom_bar uses stat_count()
  geom_col(width = .5)

