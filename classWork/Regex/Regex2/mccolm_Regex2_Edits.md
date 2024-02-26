Steps to Reg Sonnets

Searched for &, <, and > but it resulted with strings not found.
Find \n\n Replace with \n
Find ^ + Replace with nothing to delete the spaces at the front of each line.
Find (.+) Replace with <line> \1 </line> (Ah, I could've used \0 instead of that)
Find <line> [LXMCIV]+ </line> Replace with <sonnet  number="\1">
Find <sonnet Replace with
</sonnet>
<sonnet
Then added </sonnet> to line 2466
)I could not figure out how to get all of the lines to stay between the sonnets :/)
Saved as XML, closed the program, reopened and then ctrl+e to add sonnets
Pretty print
