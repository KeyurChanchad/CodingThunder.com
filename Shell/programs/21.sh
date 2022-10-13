for i in *.dat
do
	s=`echo $i | cut -d "." -f1`
	echo $s
	mv $i $s.txt
done
