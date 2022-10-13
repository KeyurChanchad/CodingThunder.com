echo 1.display all the words of a file in assending order
echo 2.display  a file in desending order
echo 3. display a file in reverse order
echo 4. toggle  all the character in the file
echo 5. display type of the file

echo enter a file
read file

echo enter choice
read ch
case $ch in 
	1)sort $file;;
	2)sort -r  $file;;
	3)rev $file;;
	4)cat $file | tr "[a-z][A-Z]" "[A-Z][a-z]";;
	5)file $file;;
esac
