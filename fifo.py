def fifo(pagestring, msize):
    mptr, hit, miss = 0, 0, 0
    memory = [-1 for i in range(msize)]
    
    for i in pagestring:
        flag = 0
        for j in memory:
            if j == int(i):
                hit += 1
                flag = 1
                print("hit")
                break

        if flag == 0:
            miss += 1
            print("fault")
            memory[mptr] = int(i)
            mptr += 1
            if mptr == msize:
                mptr = 0
        print(memory)

    # Calculating average hits and misses
    total_pages = len(pagestring)
    avg_hit_rate = hit / total_pages
    avg_miss_rate = miss / total_pages

    print("Total Hits =", hit)
    print("Total Misses =", miss)
    print("Average Hit Rate =", avg_hit_rate)
    print("Average Miss Rate =", avg_miss_rate)


def main():
    x = input("Enter the page string: ")
    m = int(input("Enter the size of memory: "))
    fifo(x, m)

main()
