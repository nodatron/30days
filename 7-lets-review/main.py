#!/usr/bin/env python

def main():
    number = int(input())

    for i in range(0, number):
        string = raw_input()

        even_s = ""
        odd_s = ""

        for j in range(0, len(string)):
            if j == 0 or j % 2 == 0:
                even_s = even_s + string[j]
            else:
                odd_s = odd_s + string[j]

        print "{} {}".format(even_s, odd_s)

if __name__ == "__main__":
    main()
