echo enter filename
read filename

echo filename size date protection owner
echo "ls -l $filename | awk {print($column)}"

ls -l $filename | awk '{print ($9, $6, $7 $5, $1, $3)}'
