echo Enter a number 
read no

rem=`expr $no % 2`
if test $rem -eq 0; then
	echo $no is even 
else
	echo $no is odd
fi
