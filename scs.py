import messages
from sys import argv
from time import time

# Shortness Common Supersequence
class SCS:
    def __init__(self, filepath: str):
        self.s1 = ''
        self.s2 = ''

        try:
            with open(filepath) as file:
                content =  file.readline().lower().strip()
                s1, s2 = content.split()
                self.s1 = s1
                self.s2 = s2
        except FileNotFoundError:
            print(messages.FILE_NOT_FOUND(filepath))
            exit(-1)

        except ValueError:
            print(messages.INCORRECT_FILE_FORMAT(content))
            exit(-1)

        self.n = len(s1) + 1
        self.m = len(s2) + 1
        self.dp = [[0] * self.m for _ in range(self.n)]

    def create_dp_table(self):
        for i in range(1, self.n):
            for j in range(1, self.m):
                if self.s1[i-1] == self.s2[j-1]:
                    self.dp[i][j] = self.dp[i-1][j-1] + 1
                else:
                    self.dp[i][j] = max(self.dp[i-1][j], self.dp[i][j-1])


    def solve(self):
        self.create_dp_table()
        i = self.n - 1
        j = self.m - 1
        answer = ''

        while (i > 0 and j > 0):
            if (self.s1[i-1] == self.s2[j-1]):
                answer = self.s1[i-1] + answer
                i-=1
                j-=1

            elif (self.dp[i-1][j] > self.dp[i][j-1]):
                answer = self.s1[i-1] + answer
                i-=1
            
            else:
                answer = self.s2[j-1] + answer
                j-=1


        while(i>0):
            answer = self.s1[i-1] + answer
            i-=1

        while(j>0):
            answer = self.s2[j-1] + answer
            j-=1




        return answer
    
    def __str__(self):
        return messages.RESULTS_MESSAGE(self.s1, self.s2, self.solve())



if __name__ == '__main__':
    start = time()
    args = argv[1:]
    arglen = len(args)
    if arglen == 0:
        print(SCS('./tests/test_0.txt'))
    
    elif arglen == 1:
        arg = args[0]
        
        if arg == '-a' or arg == '--all':
            for i in range(6):
                print(SCS(f'./tests/test_{i}.txt'))
        elif arg == '-h' or arg == '--help':
            print(messages.HELP_TEXT())
        else:
            print(SCS(arg))
    
    else:
       print(messages.EXCED_ARGUMENTS_ERROR(arglen))
    
    duration = time() - start
    duration = round(duration, 4)
    print(f'Duração: {duration}s')