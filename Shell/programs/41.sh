echo enter file for toggle content
read f

cat f | tr "[a-z][A-Z]""[A-Z][a-z]"
