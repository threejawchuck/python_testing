#!/bin/bash
#########################################
#The purpose is to tighten the compile
#run loop
#
#This script runs a script run.sh if the
#arguments to the script which are files
#or directories are updated.
#########################################

touch ON

# The Path containing this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Script to run on detected changes
# RUNSCRIPT=${DIR}/run_unit_tests.sh
RUNSCRIPT=${DIR}/run.sh

#Either monitor all specified files, or automatically grab every possible source file if no parameter is given
if [ "$1" == "" ]; then
    echo "No parameter was specified."
    echo "Automatically grabbing and monitoring all source files for changes:"

    #Get all py files
    pyFiles=`find . -name "*.py"`
    srcCppFiles=`find productTargets -name "*.cpp"`
    srcHFiles=`find productTargets -name "*.h"`
    srcYAMLFiles=`find productTargets -name "*.yaml"`
    srcSConscriptFiles=`find productTargets -name "SConscript"`
    srcSConstructFiles=`find productTargets -name "SConstruct"`
    unitCppFiles=`find tests -name "*.cpp"`
    unitHFiles=`find tests -name "*.h"`
    srcf90Files=`find productTargets -name "*.f90"`
    unitF90Files=`find tests -name "*.f90"`
    unitYAMLFiles=`find tests -name "*.yaml"`
    unitSConscriptFiles=`find tests -name "SConscript"`
    unitSConstructFiles=`find tests -name "SConstruct"`
    wrapSConscriptFiles=`find wrap -name "SConscript"`
    wrapSConstructFiles=`find wrap -name "SConstruct"`
    buildSettingsFiles=`find . -iname "buildsettings.yaml"`
    acceptanceTestFiles=`find tests/acceptance -iname "*.txt"`

    args="$RUNSCRIPT $pyFiles $srcCppFiles $srcHFiles $unitCppFiles $unitHFiles $srcf90Files $unitF90Files $srcSConscriptFiles $srcSConstructFiles $srcYAMLFiles $unitSConscriptFiles $unitSConstructFiles $wrapSConscriptFiles $wrapSConstructFiles $unitYAMLFiles $buildSettingsFiles $acceptanceTestFiles"
    echo "Monitoring the following files specified as parameters:"
    echo "$args"
else
    echo "Monitoring the following files specified as parameters:"
    args=$@
    echo "$args"
fi

#We compare against zero to see if there are any new files
zero=0
newFileCount=0
#We always want to execute the build when we first call the script,
#so call this before entering the loop.
${RUNSCRIPT}
echo "-------------------------------------------------------"
echo "Waiting for edits..."
echo "-------------------------------------------------------"

#Only run this loop while the file ON exists
while (ls ON > /dev/null)
do
    if [ "$newFileCount" -gt "$zero" ]; then
        echo "newFileCount = $newFileCount"
        echo "new files are $newFiles"
        touch ON
        ${RUNSCRIPT}

        echo "-------------------------------------------------------"
        echo "Waiting for edits..."
        echo "-------------------------------------------------------"

    fi
    sleep 1
    newFiles=`find $args -newer ON`
    newFileCount=`find $args -newer ON | wc | awk '{print $1}'`
done
