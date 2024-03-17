### Steps to Regex Bojack Edits 

| Find      | Replace |
| :-----------: | :-----------: |
| ```p>```    | ```line>```       |
| ```\[(.+?)\]```   | ```<sound noise="\1"/>```        |
 |  ```<line>```  |  ``` ```       |
  |  ```<timestamp```  | ```<line>\n<timestamp```        |
 |  ```"<i>(.+?)</i>```  |   ```"(\1) ```      |
 |  ```""(.+?)"```  |    ```"(\1)```     |
 |  ```/> \{\\an8\}```  |     ``` sub="\{\\an8\}" />```    |

<i> The chart doesn't show all of the code when viewing the preview on github, please view the code on the Code tab!

<i> Went to tools and used the Format and Indent Files to pretty print all of the files.

<i> Went into two files that wouldn't pretty print to touch up the few errors
