#for f in `ls`
#do
#	if [-x $f]
#	then
#		echo "$f executable"
#	else 
#		echo "$f not executable"
#	fi
#done

for file in *
do
	chmod a+x $file
done
