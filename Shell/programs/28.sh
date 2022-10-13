echo enter 1 file
read f1
echo enter 2 file
read f2

echo horizontally combining
cat $f1 >> $f2

echo vertically combining 
paste $f1 $f2

