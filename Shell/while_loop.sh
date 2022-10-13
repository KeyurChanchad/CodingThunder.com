echo "This is while loop"

num=10
count=0

while [ $count -le $num ]
do
	echo $count
	count=`expr $count + 1`

done


