echo press 1 to 4

echo 1. Show Date

echo 2. list files in current directory

echo 3. show current path

read ch

case $ch in 
	1) date;;
	2) ls -l;;
	3) pwd;;
	*) echo Invalid choice

esac

