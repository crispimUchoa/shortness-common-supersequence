import messages

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

    def create_dp_table(self):
        ...


scs = SCS('./tests/test_0.txt')