import typing as t

class Solution:
    def countStudents(self, students: t.List[int], sandwiches: t.List[int]) -> int:
        num_std_sand0: int = 0
        num_std_sand1: int = 0
        num_sand0: int = 0
        num_sand1: int = 0

        for std in students:
            if std == 0:
                num_std_sand0 += 1
            else:
                num_std_sand1 += 1
        
        for sand in sandwiches:
            if sand == 0:
                num_sand0 += 1
            else:
                num_sand1 += 1
        
        print(num_std_sand0, num_sand0, num_std_sand1, num_sand1)
        
        if num_std_sand0 < num_sand0:
            for ind in range(0, len(sandwiches), 1):
                if sandwiches[ind] == 0:
                    if num_std_sand0 == 0:
                        return len(sandwiches) - ind
                    else:
                        num_std_sand0 -= 1
        
        if num_std_sand1 < num_sand1:
            for ind in range(0, len(sandwiches), 1):
                if sandwiches[ind] == 1:
                    if num_std_sand1 == 0:
                        return len(sandwiches) - ind
                    else:
                        num_std_sand1 -= 1

        return 0