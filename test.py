import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame.BowlingGame()
    
    def testGutterGame(self): 
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score()==0
# test.TestBowlingGame.testGutterGame failed with error: <class 'TypeError'> 'list' object is not callable
# Traceback (most recent call last):
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
#     yield
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 623, in run
#     self._callTestMethod(testMethod)
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 579, in _callTestMethod
#     if method() is not None:
#        ^^^^^^^^
#   File "/Users/Jedi/Desktop/Project_IT6039/test.py", line 10, in testGutterGame
#     self.game.rolls(0)
# TypeError: 'list' object is not callable
    def testAllOnes(self):
#         test.TestBowlingGame.testAllOnes failed with error: <class 'AttributeError'> 'TestBowlingGame' object has no attribute 'rollMany'
# Traceback (most recent call last):
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
#     yield
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 623, in run
#     self._callTestMethod(testMethod)
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 579, in _callTestMethod
#     if method() is not None:
#        ^^^^^^^^
#   File "/Users/Jedi/Desktop/Project_IT6039/test.py", line 25, in testAllOnes
#     self.rollMany(1, 20)
#     ^^^^^^^^^^^^^
# AttributeError: 'TestBowlingGame' object has no attribute 'rollMany'
        self.rollMany(1, 20)
        assert self.game.score()==20

    def testOneSpare(self):
#         test.TestBowlingGame.testOneSpare failed with error: <class 'TypeError'> 'list' object is not callable
# Traceback (most recent call last):
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
#     yield
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 623, in run
#     self._callTestMethod(testMethod)
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 579, in _callTestMethod
#     if method() is not None:
#        ^^^^^^^^
#   File "/Users/Jedi/Desktop/Project_IT6039/test.py", line 42, in testOneSpare
#     self.game.rolls(5)
# TypeError: 'list' object is not callable
        self.game.rolls(5)
        self.game.rolls(5)      
        self.game.rolls(3)
        self.rollMany(0,17)
        assert self.game.score()==16

    def testOneStrike(self):
#         test.TestBowlingGame.testOneStrike failed with error: <class 'TypeError'> 'list' object is not callable
# Traceback (most recent call last):
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
#     yield
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 623, in run
#     self._callTestMethod(testMethod)
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 579, in _callTestMethod
#     if method() is not None:
#        ^^^^^^^^
#   File "/Users/Jedi/Desktop/Project_IT6039/test.py", line 61, in testOneStrike
#     self.game.rolls(10)
# TypeError: 'list' object is not callable
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        assert self.game.score()==24

    def testPerfectGame(self):
#         test.TestBowlingGame.testPerfectGame failed with error: <class 'AttributeError'> 'TestBowlingGame' object has no attribute 'rollMany'
# Traceback (most recent call last):
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
#     yield
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 623, in run
#     self._callTestMethod(testMethod)
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 579, in _callTestMethod
#     if method() is not None:
#        ^^^^^^^^
#   File "/Users/Jedi/Desktop/Project_IT6039/test.py", line 80, in testPerfectGame
#     self.rollMany(10,12)
#     ^^^^^^^^^^^^^
# AttributeError: 'TestBowlingGame' object has no attribute 'rollMany'
        self.rollMany(10,12)
        assert self.game.score()==300
    
    def testOneSpare(self):
#         test.TestBowlingGame.testOneSpare failed with error: <class 'AttributeError'> 'TestBowlingGame' object has no attribute 'rollMany'
# Traceback (most recent call last):
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 57, in testPartExecutor
#     yield
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 623, in run
#     self._callTestMethod(testMethod)
#   File "/opt/homebrew/Cellar/python@3.11/3.11.6_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/unittest/case.py", line 579, in _callTestMethod
#     if method() is not None:
#        ^^^^^^^^
#   File "/Users/Jedi/Desktop/Project_IT6039/test.py", line 97, in testOneSpare
#     self.rollMany(5,21)
#     ^^^^^^^^^^^^^
# AttributeError: 'TestBowlingGame' object has no attribute 'rollMany'
        self.rollMany(5,21)
        assert self.game.score()==150