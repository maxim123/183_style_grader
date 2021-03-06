#!/usr/bin/python
from eecs183style.style_grader_functions import *
from eecs183style.StyleRubric import *
import unittest, pytest
import sys, os

def load_code_segment(filename):
    def wrapper(func):
        def fn(self, *args, **kwargs):
            #Redirect stdout because it's annoying
            #tempout,temperr = sys.stdout, sys.stderr
            #sys.stdout = sys.stderr = open(os.devnull, 'w')
            self.rubric = StyleRubric()
            self.rubric.grade_student_file('test_source/'+filename)
            #sys.stdout, sys.stderr = tempout, temperr  
            return func(self, *args, **kwargs)
        return fn
    return wrapper

class RegressionTesting(unittest.TestCase):

    def setUp(self):
        #Nothing to do here for now
        pass

    def tearDown(self):
        #For debugging FAILs
        #print "-- RESULTS ------------------"
        #for x,y in self.rubric.error_types.items():
        #    print x,y
        #print "-----------------------------\n\n"
        pass

    @load_code_segment('good.cpp')
    def test_good_file(self): self.assertTrue(not len(self.rubric.error_types))
    @load_code_segment('num_of_commands.cpp')
    def test_statements_per_line(self): self.assertEqual(self.rubric.error_types['STATEMENTS_PER_LINE'], 3)
    @load_code_segment('test_valid_return.cpp')
    def test_int_for_bool(self): self.assertEqual(self.rubric.error_types['INT_FOR_BOOL'], 2)
    #@load_code_segment('if_else_good.cpp')
    #def test_good_if_else(self): self.assertEqual(0, self.rubric.error_types['IF_ELSE_ERROR'])
    #@load_code_segment('if_else_bad.cpp')
    #def test_bad_if_else(self): self.assertEqual(3, self.rubric.error_types['IF_ELSE_ERROR'])
    @load_code_segment('equals_true.cpp')
    def test_equals_true(self): self.assertEqual(5, self.rubric.error_types['EQUALS_TRUE']) 
    @load_code_segment('check_function_def_above_main_good.cpp')
    def test_def_above_main_good(self): self.assertEqual(0, self.rubric.error_types['DEFINITION_ABOVE_MAIN']) 
    @load_code_segment('check_function_def_above_main_bad.cpp')
    def test_def_above_main_bad(self): self.assertEqual(3, self.rubric.error_types['DEFINITION_ABOVE_MAIN']) 
    @load_code_segment('goto_good.cpp')
    def test_goto_good(self): self.assertEqual(0, self.rubric.error_types['GOTO']) 
    @load_code_segment('goto_bad.cpp')
    def test_goto_bad(self): self.assertEqual(3, self.rubric.error_types['GOTO']) 
    @load_code_segment('continue_good.cpp')
    def test_continue_good(self): self.assertEqual(0, self.rubric.error_types['CONTINUE_STATEMENT']) 
    @load_code_segment('continue_bad.cpp')
    def test_continue_bad(self): self.assertEqual(4, self.rubric.error_types['CONTINUE_STATEMENT']) 
    @load_code_segment('define_good.cpp')
    def test_define_good(self): self.assertEqual(0, self.rubric.error_types['DEFINE_STATEMENT']) 
    @load_code_segment('define_bad.cpp')
    def test_define_bad(self): self.assertEqual(2, self.rubric.error_types['DEFINE_STATEMENT']) 
    @load_code_segment('ternary_good.cpp')
    def test_ternary_good(self): self.assertEqual(0, self.rubric.error_types['TERNARY_OPERATOR']) 
    @load_code_segment('ternary_bad.cpp')
    def test_ternary_bad(self): self.assertEqual(3, self.rubric.error_types['TERNARY_OPERATOR']) 
    @load_code_segment('while_true_good.cpp')
    def test_while_true_good(self): self.assertEqual(0, self.rubric.error_types['WHILE_TRUE']) 
    @load_code_segment('while_true_bad.cpp')
    def test_while_true_bad(self): self.assertEqual(3, self.rubric.error_types['WHILE_TRUE']) 
    #@load_code_segment('global_good.cpp')
    #def test_global_good(self): self.assertEqual(0, self.rubric.error_types['NON_CONST_GLOBAL']) 
    #@load_code_segment('global_bad.cpp')
    #def test_global_bad(self): self.assertEqual(3, self.rubric.error_types['NON_CONST_GLOBAL']) 
    @load_code_segment('main_good.cpp')
    def test_main_good(self): self.assertEqual(0, self.rubric.error_types['MAIN_SYNTAX']) 
    @load_code_segment('main_bad.cpp')
    def test_main_bad(self): self.assertEqual(2, self.rubric.error_types['MAIN_SYNTAX']) 
    @load_code_segment('first_char_good.cpp')
    def test_first_char_good(self): self.assertEqual(0, self.rubric.error_types['FIRST_CHAR']) 
    @load_code_segment('first_char_bad.cpp')
    def test_first_char_bad(self): self.assertEqual(6, self.rubric.error_types['FIRST_CHAR']) 
    @load_code_segment('semicolon_spacing_good1.cpp')
    def test_semicolon_spacing_good(self): self.assertEqual(0, self.rubric.error_types['FOR_LOOP_SEMICOLON_SPACING'])
    @load_code_segment('semicolon_spacing_good2.cpp')
    def test_semicolon_spacing_good(self): self.assertEqual(0, self.rubric.error_types['FOR_LOOP_SEMICOLON_SPACING'])
    @load_code_segment('semicolon_spacing_bad.cpp')
    def test_semicolon_spacing_bad(self): self.assertEqual(4, self.rubric.error_types['FOR_LOOP_SEMICOLON_SPACING'])


def main():
    print "\n"
    suite = unittest.TestLoader().loadTestsFromTestCase(RegressionTesting)
    if unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful():
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())
