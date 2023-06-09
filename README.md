# APPL
AI-Powered Programming Language

---

APPL is an artificial intelligence-powered programming language.

That sounds cool, but what does it **mean?**

Here's a sample of the syntax:
```pl
set name to "Jerry"

if name is "Jerry" then
    write "Hi, Jerry!"
end if
```
And here's another:
```wl
var name = "Jerry";

if {name == "Jerry"} [
    outln("Hi, Jerry!");
]
```

The syntax of APPL can be ***whatever you want.***

Made with Google's Palm AI, APPL was created as a tool to test and run pseudocode, but it can be used for much more. For instance, if you want to use an imaginary imported module, just do something like this:
```js
import hello
// `greet` returns "Hi, " + the first parameter + "!"
println(hello.greet("Barbara"))
```

## Notes
APPL is compatible on Linux/Unix, Mac, and Windows.

## Usage
First, go to where you want APPL to be stored. I used my Desktop.

Then, `git clone` this repository:
```sh
git clone https://github.com/ThusEndingTheStory/APPL.git
```

Install `google.generativeai` with pip:
```sh
pip install google-generativeai
```

Go to [Google MakerSuite](https://makersuite.google.com/) and get an API key. Then go to `appl.py`. On line 31:
```py
palm.configure(api_key="Get your API key at Google MakerSuite and paste it here")
```
And paste your API key in the string.

There you go!

To run an APPL file, run
```sh
python3 appl.py <filename.appel>
```
If you're on Linux/Unix or Mac, you can put that code into an alias (eg. `appl`) in your `.bashrc`/`.zprofile`/`.profile`. ( I did `alias appl="python3 ~/Desktop/APPL/appl.py $1"`). I don't really know what to do on Windows if you want to use APPL anywhere, because I'm using Mac. You could just use APPL only in the directory where you have it stored. Sorry about that.

## Limitations
Keep in mind, there are many limitations. You can't use stdin, graphics, system commands, the list goes on.

I will try to keep adding features, but there is only so much that AI that only has access to the code and stdout can do.
