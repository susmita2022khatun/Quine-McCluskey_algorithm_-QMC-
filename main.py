import numpy as np
def comparison(string1,string2):
    l1 = np.array(string1)
    l2 = np.array(string2)
    count = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            count +=1
            l1[i] = "_"
    if count > 1:
        return -1
    else:
        return"".join(l1)   #recursion


def check(binary):
    pi = []
    while True:
        check1 = ["$"]*len(binary)
        temp = []
        for i in range(len(binary)):
            for j in range(i+1, len(binary)):
                k = comparison(binary[i],binary[j])
                if k != -1:
                    check1[i] = "*"
                    check1[j] = "*"
                    temp.append(k)
        for i in range(len(binary)):
            if check1[i] == "$":
                pi.append(binary[i])
        if len(temp) == 0:
            return pi
        binary = np.array(set(temp))

def dec_to_bin(no_of_variable, minterms):
    temp = []
    s = []
    for m in minterms:
        for i in range(no_of_variable):
            s = s.append(m%2)
            m = m/2
        temp.append(s)
        s = []
    return temp

def table(string1, string2, count):
    l1 = np.array(string1)
    l2 = np.array(string2)
    count_n = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            count_n += 1
    if count_n == count:
        return True
    else:
        return False

def selection(chart, prime_implicants):
    temp = []
    select = [0]*len(chart)
    for i in range(len(chart[0])):
        count = 0
        rem = -1
        for j in range(len(chart)):
            if chart[i][j] == 1:
                count += 1
                rem = j
        if count == 1:
            select[rem] = 1
    for i in range(len(select)):
        if select[i] == 1:
            for j in range(len(chart[0])):
                if chart[i][j] == 1:
                    for k in range(len(chart)):
                        chart[k][k] = 0
            temp.append(prime_implicants[i])
    while True:
        max_n = 0
        rem = -1
        count_n = 0
        for i in range(len(chart)):
            count_n = chart[i].count(1)
            if count_n > max_n:
                max_n = count_n
                rem = i

        if max_n == 0:
            return temp

        temp.append(prime_implicants[rem])

        for i in range(len(chart[0])):
            if chart[rem][i] == 1:
                for j in range(len(chart)):
                    chart[j][i] = 0


def prime_implicant_chart(prime_implicants, binary):
    chart = [[0 for x in range(len(binary))] for x in range(len(prime_implicants))]
    for i in range(len(prime_implicants)):
        count = prime_implicants[i].count("_")
        for j in range(len(binary)):
            if table(prime_implicants[i], binary[j], count):
                chart[i][j] = 1
    return chart

def main():
    no_of_variable = int(input("enter number of variables:\n"))
    minterms = [
        int(x)
        for x in input(
            "enter deciml representation of minterms\n"
        ).split()
    ]
    binary = dec_to_bin(no_of_variable, minterms)
    prime_implicants = check(binary)
    print("primeimplicants are:\n")
    chart = prime_implicant_chart(prime_implicants, binary)

    essential_prime_implicant = chart(prime_implicants, binary)
    print("Essential Prime Implicants are:")
    print(essential_prime_implicant)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()