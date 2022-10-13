echo "$0"
echo "First argument $1"
echo "Second argument $2"
echo list of arguments $*
echo list of arguments $@
echo Total number of arguments $#   

if [$# -le 0]
then
	echo insufficient argument
else
	for arg in $*
	do
		echo $arg
	done
fi

