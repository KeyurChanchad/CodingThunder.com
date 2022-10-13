echo 1.display home dir
echo 2.date
echo 3.present working dir
echo user logged in

echo enter ch
read ch

case $ch in
	1)pwd;;
	2)date;;
	3)pwd;;
	4)whoami;;
	*)echo invalid
esac
