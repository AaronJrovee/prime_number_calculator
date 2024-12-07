Quit = False
while not Quit:
    count = 0
    factors = "Factors: "
    answer = input("Enter A to check for prime or composite and list its factors; B to list primes from an interval: ")

    if answer == "A":
        answer = input("Enter the number: ")
        count = 1
        factors = "Factors: "
        prime = "Prime"
        for i in range(int(answer)):
            if int(answer)%count == 0:
                factors = factors + str(count) + ", "
                if not count == 1 and not count == int(answer) or int(answer) == 1:
                    prime = "Composite"
            count += 1
        print(prime)
        print(factors)

    if answer == "B":
        start = input("Enter the starting number: ")
        end = input("Enter the ending number: ")
        number = int(start)
        nonprimes = 0
        while not number > int(end):
            count = 1
            prime = True
            for i in range(number):
                if number%count == 0:
                    if not count == 1 and not count == number or number == 1:
                        prime = False
                count += 1
            if prime:
                print(number)
            else:
                nonprimes += 1
            number += 1          
        if nonprimes == int(end)-int(start)+1:
            print("No primes")
    if answer == "Quit" or answer == "quit" or answer == "QUIT":
        Quit = True