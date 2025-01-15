import pandas as pd
import numpy as np

def sq_dist(x, y, xp, yp):
    return (x-xp)*(x-xp) + (y-yp)*(y-yp)

def sq_test(x, y, xp, yp, L1, L2):
    if abs(x-xp)<L1 and abs(y-yp)<L1:
        L2test = sq_dist(x, y, xp, yp)
        if L2test < L2:
            return True, L2test
    return False, 0

def setmax(d):
    L2 = -1
    for i in d.keys():
        if d[i] > L2:
            L2 = d[i]
            m = i
    d["m"] = m
    d["L2"] = L2

def findk(df,xp,yp,k):
    N = len(df)
    if k > N:
        print("Too few data")
        exit(1)
    # First compute k distances
    ans = {}
    for i in range(k):
        x, y = df.iloc[i]['x'], df.iloc[i]['y']
        L2 = sq_dist(x, y, xp, yp)
        ans[i] = L2
    setmax(ans)
    # Test all subsequent points, if closer, then replace
    L2 = ans["L2"]
    L1 = np.sqrt(L2)
    for i in range(k,N):
        x, y = df.iloc[i]['x'], df.iloc[i]['y']
        test, L = sq_test(x,y,xp,yp,L1,L2)
        if test:
            del ans[ans["m"]]
            del ans["m"]
            ans[i] = L
            setmax(ans)
    return ans

if __name__ == "__main__":
    data = {
        'x': [1.0, 2.0, 3.0, 4.0, 5.0],
        'y': [1.0, 2.0, 3.0, 4.0, 5.0]
    }
    df = pd.DataFrame(data)

    xp, yp = 0.0, 0.0
    k = 3
    result = findk(df, xp, yp, k)
    print(result)

