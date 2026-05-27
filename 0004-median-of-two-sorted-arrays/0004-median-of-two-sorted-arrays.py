class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        low = 0
        high = len(nums1)
        n1 = len(nums1)
        n2 = len(nums2)
        while low <= high:
            part1 = (low + high) // 2
            part2 = (n1 + n2 + 1) // 2 - part1
            
            max_left1 = nums1[part1 - 1] if part1 > 0 else float('-inf')
            min_right1 = nums1[part1] if part1 < n1 else float('inf')

            max_left2 = nums2[part2 - 1] if part2 > 0 else float('-inf')
            min_right2 = nums2[part2] if part2 < n2 else float('inf')

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (n1 + n2) % 2 == 1:
                    return max(max_left1, max_left2)
                return (max(max_left1, max_left2) +
                        min(min_right1, min_right2)) / 2.0

            if max_left1 > min_right2:
                high = part1 - 1
            else:
                low = part1 + 1