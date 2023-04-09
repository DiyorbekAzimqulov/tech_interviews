class Solution:

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        we iterate over temperatures
        for each temperature we keep counter 
        and iterate from 1 right to the end of the temperatures
        while inner iteration we search when greater value occurs while maintaining counter
        after inner iteration we put it to answers
        we also keep found boolean variable to know whether there is greater day exist

        O(n^2)
        O(n)

        
        """
        # answer = []
        # ctr = 1
        # for i in range(len(temperatures)):
        #     for j in range(i + 1, len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             answer.append(ctr)
        #             ctr = 1
        #             break
        #         else:
        #             ctr += 1
        #     if ctr != 1 or i + 1 == len(temperatures):
        #         answer.append(0)
        #         ctr = 1
        # return answer
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res
