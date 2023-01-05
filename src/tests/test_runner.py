import unittest
import xmlrunner
from test_solver_add import TestSolver as TestSolverAdd
from test_solver_substract import TestSolver as TestSolverSubstract

# Load the test case classes from the module
suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSolverAdd)
suite2 = unittest.TestLoader().loadTestsFromTestCase(TestSolverSubstract)

# Create a test suite that contains all of the other test suites
all_suites = unittest.TestSuite([suite1, suite2])
# Create an XML runner
runner = xmlrunner.XMLTestRunner(output='test-reports')

# Run the test suite using the XML runner
runner.run(all_suites)
