### Steps to Regex Bojack Edits 

| Find      | Replace |
| :-----------: | :-----------: |
| ```(<!doctype html>\n*)?(</?)ht(ml>)```    | ```\2x\3```       |
| ```<!doctype html>```   | ``` ```        |
 |  ```<head>\s+?(<title>.+?</title>).+?</head>```  |  ```\1```       |
  |  ```<p> (CHAPTER [IVLXMC]+) </p>```  | ```<heading> \1 </heading>```        |
 | ```</article>```   |  ```</p>\n</article>```       |
 |  ```<h4>.+?</h1>```  |   ``` ```      |
 |  ```(<a href.+?>)(.+?)(</a>)```  |    ```<timestamp data-time="\2" />```     |
 |  ```(<p>\n\[)(.+?)(\])```  |     ```<p sound="\2">```    |

<i> The chart doesn't show all of the code when viewing the preview on github, please view the code on the Code tab!

<i> Changed files from html to xml through gitbash

[for f in *.html; do mv $f `basename $f .html;`.xml; done;]

  <i>The ```(<p>\n\[)(.+?)(\])``` code would not work in the Find/Replace in files, but would work in the normal Find/Replace :( I don't know how to solve this problem

<i> The {\an8} brings the subtitles to the top of the screen, which I believe is important to keep track of