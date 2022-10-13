echo 'enter filename'
read file

if [ -f $file -a -x $file ] 
then
	echo 'exist and executable'
else
	echo 'not exist and executable'
fi

