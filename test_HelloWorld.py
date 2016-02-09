#from: http://webpy.org/cookbook/testing_with_paste_and_nose

from paste.fixture import TestApp
from nose.tools import *
from HelloWorld import app

#TODO: add better JSON validation here instead of just mustcontain(), instead parse the JSON and do a value lookup for key = "sum"

class TestCode():
    def test_index(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        r = testApp.get('/add_integers?a=1&b=2')
        assert_equal(r.status, 200)
        r.mustcontain('"sum":3')
        
    def test_index2(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        r = testApp.get('/add_integers?a=2&b=3')
        assert_equal(r.status, 200)
        r.mustcontain('"sum":5')        
        
    def test_index3(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        r = testApp.get('/add_integers?a=1&b=2&c=3&d=4')
        assert_equal(r.status, 200)
        r.mustcontain('"sum":10')
