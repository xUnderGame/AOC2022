# Part one of the problem
def partOne():
    f = open("input.txt", "r")
    lines = f.readlines()

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    
    for line in lines:
        line = line.strip()
        firstHalf = slice(0, int(len(line)/2))
        secondHalf = slice(int(len(line)/2), len(line))

        # Iterate through
        for char in line[firstHalf]:
            if char in line[secondHalf] and char.isupper():
                count += 1 + alphabet.index(char.lower())+26
                break
            elif char in line[secondHalf] and char.islower():
                count += 1 + alphabet.index(char)
                break
    print(count) #7495, low. 9653, high, 7795 answer.


# Part two of the problem
def partTwo():
    f = open("input.txt", "r")
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    doLoop = True
    
    while doLoop:
        line1 = f.readline().strip()
        line2 = f.readline().strip()
        line3 = f.readline().strip()

        # Iterate through
        for char in line1:
            if char in line2 and char in line3 and char.isupper():
                count += 1 + alphabet.index(char.lower())+26
                break
            elif char in line2 and char in line3 and char.islower():
                count += 1 + alphabet.index(char)
                break
        if line1 == "":
            doLoop = False
    print(count) #2703 answer.

# Main Program
if __name__ == "__main__":
    partOne()
    partTwo()
