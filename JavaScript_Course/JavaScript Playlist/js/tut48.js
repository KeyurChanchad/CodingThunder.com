/*
Quantifier              Description

*               It matches zero or more times.

+               It matches one or more times.

?               It matches zero or one time.

{ x }           It matches exactly x times.

{x ,}            It matches at least x times.

{ x, y }         It matches from x to y times.



*/

console.log("This is tutorial 48");
// Regular Expressions:
    // Basic functions 
    // Metacharacter Symbols

// const regex = /^h/i;

// Character Sets - We use []
let regex = /k[a-z]yur/; // can be any one character from a to z
regex = /k[aty]ur/; // can be an a, t or y
regex = /k[^aty]yur/; // cannot be any of a, t or y
regex = /k[^aty]yu[rRc]/; // cannot be any of a, t or y + can be r R or c
regex = /k[a-zA-Z]ey[yu0-9][0-9]/; // we can have as many character sets as we want
// const str = "kpyuc  kCeyu365";

// Quantifiers - We use {}
regex = /key{2}ur/; // y can occur exactly 2 times
regex = /key{0,2}ur/; // y can occur exactly 0 to 2 (0 or 1 or 2) times
// str = "keyyur bhai"

// Groupings  - We use paranthesis for groupings ()
regex = /(key){2}([0-9]r){3}/
str = "keykey2r9r0r bhai";


let result = regex.exec(str);
console.log("The result from exec is ", result);


if(regex.test(str)){
    console.log(`The string ${str} matches the expression ${regex.source}`);
}
else{
    console.log(`The string ${str} does not match the expression ${regex.source}`);
}
