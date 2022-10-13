echo enter username
read user

c=`whoami|grep -c $user`

if [ $c -gt 0 ]
then
	echo user logged in
else
	echo user not logged in
fi
