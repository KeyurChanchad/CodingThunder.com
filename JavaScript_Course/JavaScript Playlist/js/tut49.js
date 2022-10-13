/*
Character    DESCRIPTION        Example

\d          This character means any digit character; functionally equivalent to [0-9] or [[:digit:]]       
                                \d matches 1,56,77 12, 123, etc., but not 1b7 or aabb6. One or more of any digit characters.

\D          This character means any non-digit character; functionally equivalent to [^0-9] or [^[:digit:]]    
                                 \D matches a, ab, abcd, ab&, but not 1.

\w          This character means any "word" character. That is, any alphanumeric character and its functionally equivalent to [_A-Za-z0-9] or [_[:alnum:]]      
                                \w matches a, ab, a1,abc123 but not !&. One or more upper- or lower-case letters or digits, but not punctuation or other special symbols/characters.

\W          This character means any non-alphanumeric character; functionally equivalent to [^_A-Za-z0-9] or [^_[:alnum:]]      
                                \W matches *, &, but not race or y1. One or more of any character but upper- or lower-case letters and digits.

\s          This character means any white space character; space, new line, tab, non-breaking space, etc.; functionally equivalent to [[:space]]       
                                vegetable\s matches "vegetable" followed by any non-white space character.

\S          This character means any non-whitespace character; anything other than space, newline, tab, non-breaking space, etc.; functionally equivalent to [^[: space]]       
                                vegetable\S matches "vegetable" followed by any non-whitespace character.


 ^: The symbol "^" matches at the beginning of the string.
 $: The symbol "$" matches only at the end of the string.
 \b: The character "\b" matches only at a word boundary.
 \B: the character "\B" Matches only if not at a word boundary.
 (?=«pattern»): This is a positive lookahead. It matches the regular expression with the pattern only if the pattern matches what comes next. The pattern is used only to look ahead but otherwise ignored.
 (?!«pattern»): This is the negative lookahead: It matches the regular expression with the pattern only if the pattern does not match what comes next. The pattern is used only to look ahead but otherwise ignored.

*/

console.log("This is tutorial 49");

// Character classes
let regex = /\wry/;     //word character - _ or alphabet or numbers
regex = /\w+d1r/;       // \w+ means one or more word characters
regex = /\Wbhai/;       // Non word character
regex = /\W+bhai/;      // \W+ means more than one Non word character
regex = /number \d999/; // \d means digit
regex = /number \d+/;   // \d+ means more than one digit
regex = /\D999/;        // \D means non digit
regex = /\D+999/;       // \D+ means more than one non digit
regex = /\ska number/;  // Match whitespace character
regex = /\s+ka number/; // \s+ means match one or more than one whitespace characters
regex = /\Ska number/;  // Match non whitespace character
regex = /\S+ka number/; // Match one or more than one non whitespace character
regex = /4r5r\b/;  // word boundary

// Assertions
regex = /A(?=y)/;
regex = /A(?!y)/;
str = "keyye7rd1r4r5ry%%$@bhaiA_     ka number 899999keyur9999";


let result = regex.exec(str);
console.log("The result from exec is ", result);

if(regex.test(str)){
    console.log(`The string ${str} matches the expression ${regex.source}`);
}
else{
    console.log(`The string ${str} does not match the expression ${regex.source}`);
}
