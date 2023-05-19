# APPL
AI-Powered Programming Language

---

APPL is an artificial intelligence-powered programming language.

That sounds cool, but what does it **mean?**

Here's a sample of the syntax:
```
set name to "Jerry"

if name is "Jerry" then
    write "Hi, Jerry!"
end if
```
And here's another:
```
var name = "Jerry";

if {name == "Jerry"} [
    outln("Hi, Jerry!");
]
```

The syntax of APPL can be ***whatever you want.***

Made with Google's Palm AI, APPL was created as a tool to test and run pseudocode, but it can be used for much more. For instance, if you want to use an imaginary imported module, just do something like this:
```
import hello
// `greet` returns "Hi, " + the first parameter + "!"
println(hello.greet("Barbara"))
```

## About

## Usage
First, install `google.generativeai` with pip:
```
pip install google-generativeai
```

Then go to `appl.py`. On line 31, change
```py

```

To run an APPL file, run
```
python3 appl.py <filename.appel>
```
If you're on Linux/Unix or Mac, you can put that code into an alias (eg. `appl`) in your `.bashrc`/`.zprofile`/`.profile`.

## Limitations
Keep in mind, there are many limitations. You can't use stdin, graphics, system commands, the list goes on.

I will try to keep adding features, but there is only so much that AI that only has access to the code and stdout can do.
