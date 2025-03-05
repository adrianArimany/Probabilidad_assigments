# Set the win probability on red for standard American roulette:
# 18 red pockets out of 38 total.
p <- 18/38

# Number of series (games) to simulate
nGames <- 1000

# Initialize vector to store outcome of each game
results <- numeric(nGames)

set.seed(123)  

for(i in 1:nGames) {
  # First bet: if win (red) with probability p, outcome = +1.
  if(runif(1) < p) {
    results[i] <- 1
  } else {
    # First bet lost, so outcome is -1 plus outcome of 2 additional bets.
    # Simulate 2 bets: number of wins ~ Binomial(2, p)
    wins <- rbinom(1, size = 2, prob = p)
    results[i] <- wins - 1  # (if wins==2: +1, if wins==1: 0, if wins==0: -1)
  }
}

# Calculate cumulative sum and running average
cumWins <- cumsum(results)
runningAvg <- cumWins / seq_len(nGames)

# Plot the running average of winnings over games
plot(runningAvg, type = "l", col = "blue", lwd = 2,
     xlab = "Number of Games", ylab = "Cumulative Average Winning",
     main = "Running Average of Winnings per Game")

# Add a horizontal line at the overall mean of the simulated results
abline(h = mean(results), col = "red", lty = 2)

# Display the overall expected winning per game (simulated average)
overallExp <- mean(results)
cat("Simulated expected winning per game: ", overallExp, "\n")

# Optionally, compare with the theoretical expectation:
# The theoretical expectation is: E[X] = p + (1-p)*(2p - 1)
theoreticalExp <- p + (1 - p) * (2 * p - 1)
cat("Theoretical expected winning per game: ", theoreticalExp, "\n")
