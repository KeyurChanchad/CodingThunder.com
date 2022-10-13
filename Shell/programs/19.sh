m1=$1
y1=$2
wat=$3
m2=$4
y2=$5

echo $m1 $y1 $wat $m2 $y2

if test $wat = ","; then
	cal $m1 $y1;cal $m2 $y2
elif test $wat = "-";then
	while [ $y1 -le $y2 ]
	then
		cal $m1 $y1
		if [ $y1 -eq $y2 -a $m1 -gt $m2 ]
		then
			exit
		fi
		m1=`expr $m1 + 1`
		if [ $m1 -gt 12 ]
		then
			m1=1
			y1=`expr $y1 + 1`
		fi
