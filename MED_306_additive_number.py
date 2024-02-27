class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        num3 = ""
        possible_starting_combinations = []
        for i in range(len(num)):
            num1 = num[0:i+1]
            for j in range(i+1, len(num)):
                num2 = num[i+1:j+1]
                sum = str(int(num1) + int(num2))
                expected_sum = num[j+1:j+1+len(sum)]
                if (len(sum) > len(num) / 2):
                    break
                if (sum == expected_sum):
                    num3 = sum
                    if (num1.startswith("0") and len(num1) != 1):
                        break
                    if (num2.startswith("0") and len(num2) != 1):
                        break
                    if (num3.startswith("0") and len(num3) != 1):
                        break
                    possible_starting_combinations.append([num1, num2, num3])
                if (len(sum) >= len(num) / 2):
                    break
                else:
                    continue

        while len(possible_starting_combinations) != 0:
            combination = possible_starting_combinations[0]
            starting_index = len(combination[0] + combination[1] + combination[2])
            if (starting_index == len(num)):
                return True
            while True:
                num1, num2, num3 = combination
                num1 = num2
                num2 = num3
                sum = str(int(num1) + int(num2))
                end_index = starting_index + len(sum)
                expected_sum = num[starting_index:end_index]
                if (sum == expected_sum):
                    num3 = sum
                    if end_index == len(num):
                        return True 
                    starting_index = end_index
                    combination = num1, num2, num3
                    continue
                else:
                    possible_starting_combinations.pop(0)
                    break
        return False
    
    '''
    Ideally, I would like to fix the logic to make it simplier. Efficiency can be a bit better by 
    Combining the bottom 2 while loops and the top 2 for loops. 

    Also we dont need a nested for loop, we can have a for while instead
     
    '''