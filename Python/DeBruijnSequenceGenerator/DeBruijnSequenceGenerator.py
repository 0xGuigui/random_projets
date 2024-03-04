def de_bruijn(k, n):
    """Generate the de Bruijn sequence for alphabet k and subsequences of length n."""
    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                for j in range(1, p + 1):
                    sequence.append(a[j])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return sequence

def generate_wordlist(start, end, k, n):
    """Generate a wordlist of numbers between start and end using the de Bruijn sequence."""
    sequence = de_bruijn(k, n)
    wordlist = []

    num_digits = len(str(end))
    num_start = int(str(start)[:n])
    num_end = int(str(end)[:n])

    for i in range(len(sequence)):
        num_str = ''.join(map(str, sequence[i:i + n]))
        num = int(num_str)
        if num >= num_start and num <= num_end and num <= end:
            wordlist.append(num)
            print(num)

    return wordlist

def write_wordlist_to_file(wordlist, filename):
    """Write the wordlist to a file."""
    with open(filename, 'w') as f:
        for word in wordlist:
            f.write(str(word) + '\n')

start = int(input("Chiffre de départ: "))
end = int(input("Chiffre de fin: "))
k = 10  # Base 10
n = len(str(end))  # Length of end gives the length of each subsequence
wordlist = generate_wordlist(start, end, k, n)
write_wordlist_to_file(wordlist, 'wordlist.txt')
