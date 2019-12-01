def take_input(n,list):
    list.sort()
    list.reverse()
    print(len(list))
    i = j = len(list)-1
    while (i>=0):
        while(j >= 0):
            if(list[i]>list[j]):
                list.remove(list[j])
                break
            j-=1
        i-=1
        j = len(list)-1
    return sum(list)
