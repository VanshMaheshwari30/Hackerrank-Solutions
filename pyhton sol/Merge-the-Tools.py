def merge_the_tools(string, k):
    
    line = len(string)//k
    s = []
    split = [ string[i:i+k] for i in range(0,len(string),k)  ]

    for i in split:
        a = ''
        for j  in i:
            if j not in a:
                a += j
            else:
                a =a
        print(a)
             
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
