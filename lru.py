def lru(pagestring,msize):
    mptr,hit,miss =0,0,0
    memory=[-1 for i in range(msize)]
    for i in range(len(pagestring)):
        flag=0
        for j in memory:
            if j == int(pagestring[i]):
                hit += 1
                flag = 1
                print("HIT")
                break
        if (flag==0):
            miss += 1
            print("MISS")
            if(mptr >= msize):
                left = pagestring[0:i]
                dist = [-1 for i in range(10)]
                present = [-1 for i in range(10)]
                for j in range(len(left)):
                    k = int(left[j])
                    dist[k] = i-j
                    for l in range(len(memory)):
                        if memory[l] == int(left[j]):
                            present[k] =l
                            break
                max,num =0,0
                for j in range(len(dist)):
                    if (dist[j] > max and present[j] > -1):
                        max = dist[j]
                        num = present[i]
                memory[num] = int(pagestring[i])
            else:
                memory[mptr] = int(pagestring[i])
                mptr += 1
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
    lru(x,m)

main()


