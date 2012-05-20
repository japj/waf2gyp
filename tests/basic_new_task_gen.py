""" basic new_task_gen test
"""
import os
import sys

import unittest


class BasicNewTaskGenTest(unittest.TestCase):
    def setUp(self):
        # ensure the waf2gyp library is in the path
        waf2gypImportDir = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
        sys.path.insert(0, waf2gypImportDir)

    def test(self):
        from wafstub import stubbedRunWscript
        from waf2gyp import convertBuildContext2Gyp

        testDirectory = os.path.dirname(__file__)
        testWscript = os.path.join(testDirectory, "basic_new_task_gen.wscript")
        testGyp = os.path.join(testDirectory, "basic_new_task_gen.gyp")

        buildContext = stubbedRunWscript(testWscript)
        gypDict = convertBuildContext2Gyp(buildContext)

        import json
        testGypDict = json.load(open(testGyp))
        self.assertEqual(gypDict, testGypDict)

if __name__ == '__main__':
    unittest.main()
