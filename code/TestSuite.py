class TestSuite:

    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        print(len(self.tests))
        for test in self.tests:
            test.run(result)
