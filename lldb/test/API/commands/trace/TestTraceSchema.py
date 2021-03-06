import lldb
from lldbsuite.test.lldbtest import *
from lldbsuite.test import lldbutil
from lldbsuite.test.decorators import *

class TestTraceLoad(TestBase):

    mydir = TestBase.compute_mydir(__file__)
    NO_DEBUG_INFO_TESTCASE = True

    def setUp(self):
        TestBase.setUp(self)
        if 'intel-pt' not in configuration.enabled_plugins:
            self.skipTest("The intel-pt test plugin is not enabled")


    def testSchema(self):
        self.expect("trace schema intel-pt", substrs=["trace", "triple", "threads", "traceFile"])

    def testInvalidPluginSchema(self):
        self.expect("trace schema invalid-plugin", error=True,
            substrs=['error: no trace plug-in matches the specified type: "invalid-plugin"'])
