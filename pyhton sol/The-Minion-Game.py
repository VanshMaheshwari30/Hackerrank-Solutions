def minion_game(string):
    k=0
    s=0
    v="AEIOU"
    for x in range(len(string)):
        if string[x] in v:
            k+=len(string)-x
        else:
            s+=len(string)-x
    if k>s:
        print("Kevin",k)
    elif s>k:
        print("Stuart",s)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
