from math import ceil, gcd, floor


def GCD(a, b):
    if b == 0:
        x = 1
        y = 0
        return(x, y)
    A, B = GCD(b, a % b)
    x = B
    y = A-B*(a//b)
    return(x, y)


def find_ans(a, b, c, minx, maxx, miny, maxy):
    if c % gcd(abs(a), abs(b)) != 0:
        return 0
    sb = b//abs(b)  # sign of a
    sa = a//abs(a)  # sign of b
    x, y = GCD(abs(a), abs(b))  # a solution to the equation
    x *= sa  # adjusting the sign of x
    y *= sb  # adjusting the sign of x
    g = gcd(abs(a), abs(b))
    x *= c//g
    y *= c//g
    # lk1 (left_k) = lower bound for k due to [minx , maxx]
    lk1 = (minx-x)*g/b  # x+k*b/g >= minx --> k >= (minx-x)*g/b (if b>0)
    # rk1 (right_k) = upper bound for k due to [minx , maxx]
    rk1 = (maxx-x)*g/b  # x+k*b/g <= maxx --> k <= (maxx-x)*g/b (if b>0)
    # till this line of code, we have assumed that b>0 and we have : (minx-x)*g/b <= k <= (maxx-x)*g/b
    # if b<0, then : (minx-x)*g/b >= k >= (maxx-x)*g/b . Thus the lower bound and the upper bound will change
    if sb == -1:
        lk1, rk1 = rk1, lk1
    # for example if lk1= 1.5 , we have k>=2 ( the reason is that k must be integer), so we have to use ceil for lower bound
    lk1 = ceil(lk1)
    # for example if lk1= 10.5 , we have k<=10 , so we have to use floor for upper bound
    rk1 = floor(rk1)

    # we do the same thing for a
    rk2 = (y-miny)*g/a  # y-k*a/g >= miny --> k <= (y-miny)*g/a (if a>0)
    lk2 = (y-maxy)*g/a  # y-k*a/g <= maxy --> k >= lk2 = (y-maxy)*g/a (if a>0)
    if sa == -1:
        lk2, rk2 = rk2, lk2
    lk2 = ceil(lk2)
    rk2 = floor(rk2)
    #### finding the interval ####
    lans = max(lk1, lk2)  # lower bound of interval
    rans = min(rk1, rk2)  # upper bound of interval
    # it occurs when we have ( lk1 ------ rk1   lk2 ------ rk2 ) or (lk2 ------- rk2   lk1 -------- rk1).[lk1,rk1] and [lk2,rk2] don't have intersection
    if rans < lans:
        print(0)
    else:
        print(rans-lans+1)
