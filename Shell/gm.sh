hr=$(date "+%H")

echo $hr

if [$hr -lt 12]
then
	echo Good morning
elif [$hr -lt 17]
then
	echo Good Afternoon
else
	echo Good Evening
fi

