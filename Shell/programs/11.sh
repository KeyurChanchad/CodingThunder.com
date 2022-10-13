for i in *
do
	if test -d $i; then
		countd=`expr $countd + 1`
	fi
	if test -f $i; then
		countf=`expr $countf + 1`
	fi
done

echo No. of directory $countd
echo no. of files $countf
