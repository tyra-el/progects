n = int(input())

def pascal(n):
    if n == 0:
        return [[0, 1, 0]]
    else:
        top = pascal(n-1)
        top.append([
            [0] + [top[-1][i]+top[-1][i+1] for i in range(len(top[-1])-1)] + [0]
        ])
        print(top)
        return(top)


pascal(n)
