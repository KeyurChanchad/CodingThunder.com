echo enter the username
read user

c=whoami | grep -h $user
if test $c = $user
then
	echo user is logged in
else
	echo user is not logged in
fi
