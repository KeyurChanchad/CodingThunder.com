echo enter the filename
read file

cat $file

echo 1.Display the content of the file sorted by marks in desending order

echo 2.name in alphabetiacal order 

echo 3.students accroding to their roll no

echo 4.sort file accroding to 2 field and save it in names

echo 5.students scored between 70 to 80

echo enter choice
read ch

case $ch in 
	1)sort -t"~" -k3 -r $file;;
	2)sort -t"~" -k2 $file;;
	3)sort -t"~" -k1 $file;;
	4)sort -t"~" -k2 $file >> names.txt;;
	5)awk '{if ($5 > 70 && $5 < 80)
		print $5 }' $file;;
	#here $5 means fifth first rollno, second |, third name, forth |, fifth marks
esac

		
