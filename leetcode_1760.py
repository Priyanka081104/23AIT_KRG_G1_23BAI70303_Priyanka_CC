class Solution(object):
    def minimumSize(self, nums, maxOperations):
        def check(mid):
            totalopt=0
            opt=0
            for n in nums:
                opt=n//mid
                if n%mid==0:
                    opt=opt-1
                totalopt=totalopt+opt
            if totalopt<=maxOperations:
                return True
            else:
                return False
        l=1
        h=max(nums)
        result=h
        while l<=h:
            mid=l+((h-l)//2)
            if check(mid):
                result=mid
                h=mid-1
            else:
                l=mid+1
        return result