# hps-python-unittest
[![Build Status](https://travis-ci.org/hiptest/hps-python-unittest.svg?branch=master)](https://travis-ci.org/hiptest/hps-python-unittest)

Hiptest publisher samples with Python/UnitTest

In this repository you'll find tests generated in Python/UnitTest format from [Hiptest](https://hiptest.com), using [Hiptest publisher](https://github.com/hiptest/hiptest-publisher).

The goals are:

 * to show how tests are exported in Python/UnitTest.
 * to check exports work out of the box (well, with implemented actionwords)

System under test
------------------

The SUT is a (not that much) simple coffee machine. You start it, you ask for a coffee and you get it, sometimes. But most of times you have to add water or beans, empty the grounds. You have an automatic expresso machine at work or at home? So you know how it goes :-)

Update tests
-------------


To update the tests:

    hiptest-publisher -c python-unittest.conf --only=tests

The tests are generated in [``src/tests``](https://github.com/hiptest/hps-python-unittest/tree/master/src/tests)

Run tests
---------


To build the project and run the tests, use the following command:

    python bootstrap.py
    bin/buildout
    bin/test --with-xunit

The SUT implementation can be seen in [``src/coffee_machine.py``](https://github.com/hiptest/hps-python-unittest/blob/master/src/coffee_machine.py)

The test report is generated in ```nosetests.xml```
