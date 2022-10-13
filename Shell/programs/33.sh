echo enter filename
read file

ls -l $file | cut -c 2-10
