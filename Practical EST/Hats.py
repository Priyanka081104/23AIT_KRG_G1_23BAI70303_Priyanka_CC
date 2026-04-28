class Solution:
    def numberWays(self, hats):
        MOD = 10**9 + 7
        n = len(hats)
        hat_to_people = [[] for _ in range(41)]
        for person in range(n):
            for h in hats[person]:
                hat_to_people[h].append(person)
        dp = [0] * (1 << n)
        dp[0] = 1
        for h in range(1, 41):
            new_dp = dp[:]
            for mask in range(1 << n):
                if dp[mask] == 0:
                    continue

                for person in hat_to_people[h]:
                    if not (mask & (1 << person)):
                        new_mask = mask | (1 << person)
                        new_dp[new_mask] = (new_dp[new_mask] + dp[mask]) % MOD

            dp = new_dp
        return dp[(1 << n) - 1]
