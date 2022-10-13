echo enter a word
read word

for file in $@
do
	grep $word $file
done

