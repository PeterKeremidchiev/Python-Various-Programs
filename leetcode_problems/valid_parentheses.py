from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        deq = deque(s)
        open_parent = []
        # closed_parent = []
        flag = True
        while deq:
            current = deq.popleft()

            if current in "({[":
                if not deq:
                    flag = False
                    break
                open_parent.append(current)

            elif not open_parent:
                flag = False
                break
            else:
                # if current in ")}]":
                #     closed_parent.append(current)
                if f'{open_parent.pop() + current}' not in "(){}[]":
                    flag = False
                    break
                # else:
                #     closed_parent.remove(current)

        # if not closed_parent:
        #     flag = False
        return flag


sol = Solution()
print(sol.isValid("("))
