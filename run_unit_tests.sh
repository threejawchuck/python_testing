#!/bin/bash
#run the unit tests
nosetests --with-xunit --xunit-file testresults.xml

echo -----------------
echo runnign pyflakes
pyflakes *.py