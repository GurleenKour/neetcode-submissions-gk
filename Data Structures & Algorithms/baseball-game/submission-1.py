class Solution:
    def calPoints(self, operations: List[str]) -> int:
        newArr = []
        sum = 0
        for i in range(len(operations)):
            nl = len(newArr)
            if operations[i] == "+":
                x = newArr[nl-1]+ newArr[nl-2]
                newArr.append(x)
                sum += x
            elif operations[i] == "D":
                d = 2 * newArr[nl-1]
                newArr.append(d)
                sum += d

            elif operations[i] == "C":
                l = newArr.pop()
                sum -= l
                
            else:
                newArr.append(int(operations[i]))
                print(newArr,i)
                sum += int(operations[i])
        return sum
        