h=date '+%H'
if [$h -ge 6 -a $h -lt 12]
then
	echo Good Morning
elif [$h -gt 12 -a $h -lt 16]
then
	echo Good Afternoon
else
	echo Good Evening
fi

