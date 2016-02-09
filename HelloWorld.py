# Hello World test for Mahmood @ CircleCI
# 
# Requirments: build a python web server that takes to GET arguments as integers and returns the result as JSON
#
# Goals:  simple, quick, just make it work
#

#Step 1:  print to STDOUT:
#  http://stackoverflow.com/questions/1077347/hello-world-in-python
#Step 2:  Update to make a web service:  
#  http://www.dreamsyssoft.com/python-scripting-tutorial/create-simple-rest-web-service-with-python.php?/archives/6-Create-a-simple-REST-web-service-with-Python.html


#!/usr/bin/env python
import web

urls = (
    '/add_integers', 'add_integers',
)

app = web.application(urls, globals())

class add_integers:
  def GET(self):
    web.header('Content-Type', 'application/json')
    get_input = web.input(_method='get')
    output = '{ "sum":';
    sum = 0;
    for key in get_input:
    # TODO: add safe access to values, error handling if there's not two arguments (maybe?), handling of non-integer argument values, etc...
#      output += str(key) + ' = ' + str(get_input[key]) + ','
        sum += int(get_input[key])
    output += str(sum) + " }";
    return output

#if __name__ == "__main__":
#    app.run()
 

#from: http://webpy.org/cookbook/testing_with_paste_and_nose
import os

def is_test():
    if 'WEBPY_ENV' in os.environ:
        return os.environ['WEBPY_ENV'] == 'test'

if (not is_test()) and __name__ == "__main__": app.run()
