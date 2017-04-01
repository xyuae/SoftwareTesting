# The MIT License (MIT)
# Copyright (c) 2016 Arie Gurfinkel

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import unittest
import wlang.ast as ast
import wlang.sym

class TestSym (unittest.TestCase):
    def test_one (self):
        
        prg1 = "havoc x; assume x > 10; assert x > 15; x := x * 1; x := x / 1; x := x - 0; if x > 0 and x = 0 or true then skip else skip"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        self.assertEquals (len(out), 1)
    def test_two (self):
        prg1 = "havoc x, y; assume y >= 0; c := 0; r := x; while c < y inv c <= y do { r := r + 1; c := c + 1 }; assert r = x + y"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        self.assertEquals (len(out), 1)
        
    def test_two_no_inv (self):
        prg1 = "havoc x, y; assume y >= 0; c := 0; r := x; while c < y do { r := r + 1; c := c + 1 }; assert r = x + y"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        self.assertEquals (len(out), 11)
        
    def test_two_wrong (self):
        prg1 = "havoc x, y; assume y > 0; c := 0; r := x; while c < y inv c <= y do { r := r + 1; c := c + 1 }; assert r = x + y"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        self.assertEquals (len(out), 1)
        
    def test_two_wrong_inv (self):
        prg1 = "havoc x, y; assume y >= 0; c := 0; r := x; while c < y inv c < y do { r := r + 1; c := c + 1 }; assert r = x + y"
        ast1 = ast.parse_string (prg1)
        sym = wlang.sym.SymExec ()
        st = wlang.sym.SymState ()
        out = [s for s in sym.run (ast1, st)]
        self.assertEquals (len(out), 0)

    def test_three (self):
    	prg1 = "havoc x; if false then skip else skip"
    	ast1 = ast.parse_string(prg1)
    	sym = wlang.sym.SymExec ()
    	st = wlang.sym.SymState()
    	out = [s for s in sym.run (ast1, st)]
    	self.assertEquals (len(out), 1)  
    
    def test_four (self):
    	prg1 = "havoc x; if not true then skip else skip; print_state"
    	ast1 = ast.parse_string(prg1)
    	sym = wlang.sym.SymExec ()
    	st = wlang.sym.SymState()
    	out = [s for s in sym.run (ast1, st)]
    	self.assertEquals (len(out), 1)
        
    def test_five (self):
    	prg1 = "havoc x; if not true then skip; {skip} "
    	ast1 = ast.parse_string(prg1)
    	sym = wlang.sym.SymExec ()
    	st = wlang.sym.SymState()
    	out = [s for s in sym.run (ast1, st)]
    	self.assertEquals (len(out), 1)
