

for file in *
do
	if test `-s $file`
	then
		echo $file file not empty
	else
		echo rm $file
		echo '$file removed'
	fi
done


