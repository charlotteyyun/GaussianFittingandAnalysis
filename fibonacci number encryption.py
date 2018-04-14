def main():

    def conversion(entry):

        for x in range(0,len(entry)):
            if entry[x] == '-':
                exit()

        else:
            y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            new_entry = [y.index(x) + 1 for x in entry[2:]]

            fibonacci_numbers = [0, 1]
            for i in range(2, 700):
                fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])

            new_entry1=[]
            for i in range(0, len(new_entry)):
                z = map(str,entry[0])
                z = ''.join(z)
                z = int(z)
                fibonacci_numbers1 = fibonacci_numbers[z-1:]
                new_entry1.append(new_entry[i] + fibonacci_numbers1[i])

            new_entry2=[x % 26 for x in new_entry1]

            new_entry3 = [y[x-1] for x in new_entry2]
            new_entry3 = ''.join(new_entry3)
            new_entry3 = new_entry3.upper()

            print(new_entry3)

    entry = list(input("Enter the nth number to start the Fibonacci sequence for the key followed by a ‘;’ and then the word that needs to be encoded:").lower())
    conversion(entry)

main()


