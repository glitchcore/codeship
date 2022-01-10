import pdb
from time import sleep

class PdbHandler:
    def __init__(self):
        self.returning = False

    def write(self, buffer):
        if buffer == '--Return--':
            self.returning = True

        # each line of code is prefixed with a '-> '
        _, *code = buffer.split('\n-> ', 1)
        if code:
            if self.returning:
                self.returning = False
            else:
                print(code[0])
                sleep(1)

    def readline(self):
        return 'n\n'

    def flush(self):
        pass

def example_function():
    for x in range(5):
        print(x)
    print("line 1")
    print("line 2")
    return (3)

handler = PdbHandler()
print('returns', pdb.Pdb(stdin=handler, stdout=handler).runcall(example_function))