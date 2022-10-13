for i in *
do 
	if test `echo $i | grep ^n`;then
		echo $i rename
		mv $i newname
		
	fi
done


