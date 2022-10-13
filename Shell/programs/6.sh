echo enter filename
read file

if test -f $file
then
	`ls -l $file | cut -d " " -f9`  
else 
	echo file does not exists
fi

