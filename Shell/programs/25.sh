
if test $# -gt 0
then
	echo $1 $2
	echo both are provied
	if test -f $1 -a -f $2
	then
		cat $1 >> $2
	else
     		echo files does not exits
	fi
else
	echo files not provied
fi
