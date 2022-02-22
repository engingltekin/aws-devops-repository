#!/bin/bash
#
# This script creates a new user on the local system.
# You will be prompted to enter the username (login), the person name, and a password.
# The username, password, and host for the account will be displayed.

# Make sure the script is being executed with superuser privileges.
if [[ "$UID" -ne 0 ]]
then
echo "Please execute the script with super user privileges."
Exit
fi

# Get the username (login).
read -p "Please Enter Username : " userName
# Get the real name (contents for the description field).
read -p "Please Enter Full Name : " comments
#fullName=$REPLY

# Get the password.
read -s -p "Please Enter Password : " password
# password=$REPLY
# Create the account.
useradd -c $comments -m $userName
# Check to see if the useradd command succeeded.
if [[ $? -eq 0 ]]
then
  echo "Success! User has been created"
fi
# We dont want to tell the user that an account was created when it hasn't been.

# Set the password.
echo $password | passwd --stdin $userName 
# Check to see if the passwd command succeeded.
if [[ $? -eq 0 ]]
then
  echo "Password success"
fi
# Force password change on first login.
# sudo chage -d 0 $userName
passwd -e $userName
# Display the username, password, and the host where the user was created.
echo -e "Your username: $username
Your password: $password
Hostname : $HOSTNAME"