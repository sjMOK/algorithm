class Solution:
    def merge(self, intervals):
        result = []
        for interval in sorted(intervals):
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result
