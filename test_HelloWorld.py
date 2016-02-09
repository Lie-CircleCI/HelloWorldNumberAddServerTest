from paste.fixture import TestApp
from nose.tools import *
from HelloWorld import app

class TestCode():
    def test_index(self):
        middleware = []
        testApp = TestApp(app.wsgifunc(*middleware))
        r = testApp.get('/add_integers?a=1&b=2')
        assert_equal(r.status, 200)
        r.mustcontain('sum:3')