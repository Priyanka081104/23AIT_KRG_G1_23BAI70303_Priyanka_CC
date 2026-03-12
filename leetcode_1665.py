class Solution(object):
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        sumi = 0
        maxi = 0
        for i in range(len(tasks)):
            actual = tasks[i][0]
            minimum = tasks[i][1]

            if maxi < minimum:
                sumi += (minimum - maxi)
                maxi = minimum
            maxi -= actual
        return sumi