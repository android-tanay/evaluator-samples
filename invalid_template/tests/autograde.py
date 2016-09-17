class ProgQuestionPublic(unittest.TestCase):
    def setUp(self):
        # clears the dictionary containing meta data for each test
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }

# Do not modify above this line, unless you know what you are doing

    @timeout_decorator.timeout(2)
    def test_public_1(self):
        self.meta['expression'] = 'test_result("public", 1)'
        self.meta['expected'] = 'True'
        self.meta['output'] = str(test_result('public', 1))
        self.meta['hint'] = 'public 1: Your function return type is ' + str(type(test_result('public', 1)))

        self.assertTrue(test_result('public', 1))

class ProgQuestionPrivate(unittest.TestCase):
    def setUp(self):
        # clears the dictionary containing meta data for each test
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }

    @timeout_decorator.timeout(2)
    def test_private_1(self):
        self.meta['expression'] = 'test_result("private", 1)'
        self.meta['expected'] = 'True'
        self.meta['output'] = str(test_result('private', 1))
        self.meta['hint'] = 'You can try raising exceptions'

        try:
            self.assertTrue(test_result('private', 1))
        except Exception:
            self.meta['hint'] = 'private 1: Exception raised'
            self.fail()

    @timeout_decorator.timeout(2)
    def test_private_2(self):
        self.meta['expression'] = 'test_result("private", 2)'
        self.meta['expected'] = 'True'
        self.meta['output'] = str(test_result('private', 2))
        self.meta['hint'] = 'Private 2'

        self.assertTrue(test_result('private', 2))

class ProgQuestionEvaluation(unittest.TestCase):
    def setUp(self):
        # clears the dictionary containing meta data for each test
        self.meta = { 'expression': '', 'expected': '', 'hint': '' }

    def test_evaluation_1(self):
        self.meta['expression'] = 'test_result("evaluation", 1)'
        self.meta['expected'] = 'True'
        self.meta['output'] = str(test_result('evaluation', 1))
        self.meta['hint'] = 'evaluation 1: Your function return type is ' + str(type(test_result('evaluation', 1)))

        self.assertTrue(test_result('evaluation', 1))

    def test_evaluation_2(self):
        self.meta['expression'] = 'test_result("evaluation", 2)'
        self.meta['expected'] = 'True'
        self.meta['output'] = str(test_result('evaluation', 2))
        self.meta['hint'] = 'evaluation 2: Your function return type is ' + str(type(test_result('evaluation', 2)))

        self.assertTrue(test_result('evaluation', 2))

# Do not modify beyond this line
if __name__ == '__main__':
    unittest.main(
            testRunner=xmlrunner.XMLTestRunner(open('report.xml', 'wb'), outsuffix = ''),
            failfast=False,
            buffer=False,
            catchbreak=False)
