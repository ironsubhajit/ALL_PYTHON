# Statement: In this challenge, the task is to debug the existing code to successfully execute all provided test files.

# Hint: Python’s default arguments are evaluated once when the function is defined,
# not each time the function is called (like it is in say, Ruby).
# This means that if you use a mutable default argument and mutate it,
# you will and have mutated that object for all future calls to the function as well.


class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream=None):
    if not stream:
        stream = EvenStream()
    for _ in range(n):
        print(stream.get_next())


queries = int(input("q: "))
for _ in range(queries):
    stream_name, n = input("stream, n: ").split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())
