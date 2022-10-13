echo "Enter file name"
read file

if [ -f $file ];then
	echo file exist!
else
	echo "file not found"
	echo here are some suggestion
	ls
fi

