Done:
  
[x] Created GitHub Account:  
    u: Lie-CircleCI
    p: 6tSyxnREVqqwL-_t5T
    
[x] Create new GitHub Repository:
  https://github.com/Lie-CircleCI/HelloWorldNumberAddServerTest.git
  
[x] Clone repository locally to start work

[x] Commit+Push simple HelloWorld.py to master to test GitHub integration

[x] Link GitHub account to CircleCI

[x] Build first repo: failed, no tests

[x] Find example Python code to take GET arguments from URL
  > sudo easy_install web.py:
http://www.dreamsyssoft.com/python-scripting-tutorial/create-simple-rest-web-service-with-python.php?/archives/6-Create-a-simple-REST-web-service-with-Python.html

[x] Turn arguments into Integers, test for valid integers, and return error or the result as JSON
  test via:     python HelloWorld.py
  in a browser: http://localhost:8080/add_integers?a=1&b=2

[x] setup the requirements.txt to force version numbers of python packages

[x] Find test engine for Python that works with CircleCI and will test web.py, using Nose + Paste as described here:
  http://webpy.org/cookbook/testing_with_paste_and_nose

[x] Update to return JSON  (and fix bug for Content-Type to "application/json" from default

[x] Create CircleCI account linked into GitHub

[x] Learn about CircleCI broken test results and how to use UI

[x] Create and bugfix circle.yml to use custom enviornment flag "WEBPY_ENV=test"  to avoid kicking off web.py's webserver when we run our tests

[x] Debug until test passes
  > several circle.yml config and typo errors until build finally completed and said "Fixed":
https://circleci.com/gh/Lie-CircleCI/HelloWorldNumberAddServerTest/10

[x] Added two more tests, one should fail, one should pass for a total of 2 pass + 1 fail, which it does (see "$ nosetests" detail in report):
https://circleci.com/gh/Lie-CircleCI/HelloWorldNumberAddServerTest/12

[x] test fixing to remove forced bug:
https://circleci.com/gh/Lie-CircleCI/HelloWorldNumberAddServerTest/13
 
[x] Change test output to be more descriptive in CircleCI interface by updating circle.yml:
test:
  override:
    - mkdir -p $CIRCLE_TEST_REPORTS/nosetests
    - nosetests --with-xunit --xunit-file=$CIRCLE_TEST_REPORTS/nosetests/nosetests.xml
Works:
  https://circleci.com/gh/Lie-CircleCI/HelloWorldNumberAddServerTest/16 

[x] Switch second test to fail to test XML output:
https://circleci.com/gh/Lie-CircleCI/HelloWorldNumberAddServerTest/17

[x] Fix test so final test says "Fixed":
https://circleci.com/gh/Lie-CircleCI/HelloWorldNumberAddServerTest/18

[x] Email Mahmood when done

