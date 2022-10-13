d=`date +%u`
echo $d
if test $d -eq 7; then
	echo it is weekend
else
	echo it is a weekday
fi
