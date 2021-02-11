#!/bin/bash

# we are going to ask user for number 11

echo "Hello user, enter number between 10 and 12: "
read user_input

if [ ! ${user_input} -eq 11 ] ; then
	echo "The number ${user_input} is not what we're looking for !..."
else
	echo "Great! The number ${user_input} is match..."
fi
