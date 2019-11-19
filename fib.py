# fibonacci.py

def fib():
    fibs = [1, 2]
    x = 2
    
    for i in range(1,9):
        Fn = fibs[x-1] + fibs[x-2]
        fibs.append(Fn)
        x = x + 1

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
