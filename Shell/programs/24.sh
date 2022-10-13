if test $# -eq 2
then
	echo $1
	echo $2
	cmp $1 $2
	c=`echo $?`
	if test $c -eq 0
	then
		echo both are same content
	else
		echo both are different
	fi
else
	echo pls provid files
fi
