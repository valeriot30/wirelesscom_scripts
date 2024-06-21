
from math import factorial
import ion
import kandisky

def erlangb():

    N = int(input("Inserisci il numero di canali: "))
    Pb = float(input("Inserisci la probabilità di blocco: "))
    
    tolerance = 0.0001  # Set tolerance for convergence
    j = 0.0
    step = 0.01  # Initial step size for searching the traffic usage

    def calculate_blocking_probability(A, N):
        numerator = pow(A, N) / factorial(N)
        denominator = sum(pow(A, i) / factorial(i) for i in range(N + 1))
        return numerator / denominator

    while True:
        B = calculate_blocking_probability(j, N)
        if abs(B - Pb) <= tolerance:
            print(j)
            break
        j += step

    

erlangb()