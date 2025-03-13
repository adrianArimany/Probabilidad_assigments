library(poibin)
library(ggplot2)

win_probs <- c(4/5, 13/20, 3/10)

wins <- 0:3

pmf <- dpoibin(wins, win_probs)

# Create a data frame for plotting
df <- data.frame(Wins = wins, Probability = pmf)

# Plot the PMF using ggplot2
ggplot(df, aes(x = Wins, y = Probability)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  labs(title = "Poisson Binomial Distribution for Tournament Wins",
       x = "Number of Wins",
       y = "Probability") +
  theme_minimal()