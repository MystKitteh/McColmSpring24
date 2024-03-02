### Steps to Regex Dracula Edits 
| Find      | Replace |
| :-----------: | :-----------: |
| &    | ```&amp;```       |
| ```\n\n```   | ```\n```        |
 |  (^.+$)  |  ```<p> \0 </p>```       |
  |  ```<p> (CHAPTER [IVLXMC]+) </p>```  | ```<heading> \1 </heading>```        |
 | ```<heading>```   |  ```</chapter> <chapter> <heading>```       |
 |  ```(".+?")```  |   ```<q> (\1) </q>```      |
 |  ```\"?(\d(-))?(\d+ (January|February|March|April|May|June|July|August|September|October|November|December))[\.|,]?```  |    ```<date>\0</date>```     |
 |  â€™  |     '    |
|  â€  |     -    |
|  ```(\d\d?):(\d\d) (([aApP]\. [mM]\.)?)|(\d\d? [aApP]\. [mM]\.)|(\d?\d:\d\d)```  |     ```<time> \0 </time>```    |


<i>Adjust code slightly to fix the chapters

ctrl+a -> ctrl+e

add book around all of the text

Then pretty print

  <i>Adjusted the date code after I thought I was done due to some missing dates.

