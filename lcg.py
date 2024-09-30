class LinearCongruentialGenerator:
    def __init__(self, seed, a, c, m):
        self.seed = seed  # Starting value X0
        self.a = a        # Multiplier
        self.c = c        # Increment
        self.m = m        # Modulus
        self.current_value = seed

    def next(self):
        # Compute the next pseudo-random number
        self.current_value = (self.a * self.current_value + self.c) % self.m
        return self.current_value

    def generate_sequence(self, n):
        # Generate a sequence of n pseudo-random numbers
        sequence = []
        for _ in range(n):
            sequence.append(self.next())
        return sequence

# Example usage:
if __name__ == "__main__":
    # Ask user for LCG parameters
    seed = int(input("Enter the seed (X0): "))
    a = int(input("Enter the multiplier (a): "))
    c = int(input("Enter the increment (c): "))
    m = 2**32  # Modulus (commonly set to 2^32 for 32-bit systems)

    # Ask for the number of pseudo-random numbers to generate
    n = int(input("Enter how many random numbers you want to generate: "))

    # Create an instance of the LCG
    lcg = LinearCongruentialGenerator(seed, a, c, m)

    # Generate and display the sequence
    random_sequence = lcg.generate_sequence(n)
    print("Generated sequence:", random_sequence)
