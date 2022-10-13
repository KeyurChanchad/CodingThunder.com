echo press 1 to 4
read ch

case $ch in
	0|1)who;;
	2)uname;;
	3)ls *.sh;;
	4)cal 2022;;
	*)echo invalid choice
	esac
