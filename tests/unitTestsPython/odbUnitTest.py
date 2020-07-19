import unittest
import testtools

class TestCase(unittest.TestCase):
    #Function to change a value and test the change effect
    def changeAndTest(self,obj,SetterName,GetterName,expectedVal,*args):
        getattr(obj, SetterName)(*args)
        self.assertEqual(getattr(obj, GetterName)(),expectedVal)
    def check(self,obj,GetterName,expectedVal,*args):
        self.assertEqual(getattr(obj, GetterName)(*args),expectedVal)
    def change(self,obj,SetterName,*args):
        return getattr(obj, SetterName)(*args)
    
class TracingStreamResult(testtools.StreamResult):
    def status(self, *args, **kwargs):
        print('{0[test_id]}: {0[test_status]}'.format(kwargs))
def main():
    unittest.main()
def mainParallel(Test):
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())
    result = TracingStreamResult()
    result.startTestRun()
    concurrent_suite.run(result)
    result.stopTestRun()