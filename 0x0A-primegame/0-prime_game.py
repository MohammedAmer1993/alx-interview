#!/usr/bin/python3
'''prime game'''


def isWinner(x, nums):
    """
    Determines the winner of a prime number game.

    Args:
      x: The number of rounds.
      nums: An array of n, where n is the upper limit of consecutive integers 
            for each round.

    Returns:
      The name of the player that won the most rounds, or None if 
      the winner cannot be determined.
    """
    def is_prime(n):
        """
        Checks if a number is prime.
        """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_primes(n):
        """
        Generates a list of prime numbers up to n.
        """
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_game(n):
        """
        Simulates a single round of the game.
        """
        numbers = list(range(1, n + 1))
        primes = get_primes(n)
        player = 0  # 0 for Maria, 1 for Ben

        while primes:
            prime = primes[0]
            for num in numbers:
                if num % prime == 0:
                    numbers.remove(num)
            primes.remove(prime)
            player = 1 - player

        return "Maria" if player == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
