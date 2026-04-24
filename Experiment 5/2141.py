def maxRunTime(n, batteries):
    batteries.sort()
    total = sum(batteries)

    left, right = 0, total // n
    while left < right:
        mid = (left + right + 1) // 2
        if sum(min(b, mid) for b in batteries) >= n * mid:
            left = mid
        else:
            right = mid - 1

    return left
