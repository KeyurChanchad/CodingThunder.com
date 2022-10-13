/*Character     Explanation                                         Example

.               This metacharacter allows any character             matches any character

+               This character allows one or more preceding term    /ah+x/ matches ""ahx" or "ahhhhhhhx"

*               This character allows zero or more preceding term   /ah*x/ matches "aax", "ahx", or "ahhhhx"

?               This character allows zero or one preceding term    /ah?x/ matches "aax" and "ahx" but not "ahhx"

\.              This character allows a period(.) in the text       /etc\./ matches "etc."

\/              This character allows forward slash in the text.    /.+\/.+/ matches "home/my"

\*              This character allows asterik in the text.          /my\*name/ matches "my*name"

\+              This character allows Plus sign in the text.        /.+ \+ .+/ matches "five + four"

\?              This character allows question mark in the text.    /.+\?/ matches "really?"

^               The string should begin with the specified word written after this character.   /^Bye/ matches "Bye" in "Bye Harry"

$               The string should end with the specified word written before this character.    /Harry$/ matches "Harry" in "and Harry"
 */

console.log('This is tutorial 47');

let regex = /keyur/;
// Lets look into some metacharacter symbols
regex = /^key/; // ^ means expression will match if string starts with
// regex = /se.$/; // $ at the end of the string means "string ends with"
// regex = /b.y/; //matches any one character
// regex = /g*d/;//matches any 0 or more characters
// regex = /ke?y?ur/; //? after character means that characptional
// regex = /k\*eyur/

let str = "kur is a good boy and king of universe."; // 

let result = regex.exec(str);
console.log("The result from exec is ", result);

if(regex.test(str)){
    console.log(`The string ${str} matches the expression ${regex.source}`);
}
else{
    console.log(`The string ${str} does not match the expression ${regex.source}`);
}
