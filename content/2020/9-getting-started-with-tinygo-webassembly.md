Title: Getting started with TinyGo and WebAssembly (WASM)
Date: 2020-10-23 18:00
Author: Andrea Grandi
Category: Development
Tags: go, golang, tinygo, web, webassembly, wasm, assembly, js, javascript, html, browser, macos, code, development, embedded, programming, language
Slug: getting-started-with-tinygo-webassembly
Status: published
Summary: This tutorial explains how to call a method written in Go and compiled to WebAssembly (WASM) from JavaScript by using TinyGo

[![tinygo logo]({static}/images/2020/10/tinygo-logo.png){width=30%}]()

With [WebAssembly](https://webassembly.org) we can write a library in almost any language, compile it to **WebAssembly (WASM)** and use it from **JavaScript**.

In this tutorial I will show you how to get started with [TinyGo](https://tinygo.org) by writing a simple `add()` method in **Go** and using it from a web page. All the code will be running **in the browser** without any backend process involved (you only need a static server to serve the html page and JavaScript files, but I will cover this part too).

## Install TinyGo

To be able to install [TinyGo](https://tinygo.org) you need to have [Go](https://golang.org) installed first. I have personally tested this on my Mac, so I will provide instructions for MacOS, but you can find instructions for the other operating systems directly on the project website: <https://tinygo.org/getting-started>

You can install TinyGo on MacOS using **brew**:

    :::shell
    brew tap tinygo-org/tools
    brew install tinygo

If installation is successful, you should be able to run this:

    :::shell
    tinygo version
    tinygo version 0.15.0 darwin/amd64 (using go version go1.15.3 and LLVM version 10.0.1)

## Implement an add() method in Go

Create a new empty project/repository using your favourite IDE (I personally used **VSCode**, but of course you can use anything else) and then create `main.go` file with this code:

    :::golang
    package main

    func main() {
    }

    // This function is exported to JavaScript, so can be called using
    // exports.add() in JavaScript.
    //export add
    func add(x, y int) int {
        return x + y
    }

## Compile to WebAssembly (WASM)

To compile the above code to **WebAssembly** you need to run this command:

    :::shell
    tinygo build -o wasm.wasm -target wasm ./main.go

that will create a file named `wasm.wasm` in the same directory of your project. This is the compiled web binary that will be loaded later by JavaScript.

## Add required WASM library

There is a file that is provided with TinyGo that you need to distribute with your application: `wasm_exec.js`. To include it in your project, you need to run this:

    :::shell
    cp $(tinygo env TINYGOROOT)/targets/wasm_exec.js .

## Script to load the WebAssembly

At this point you will need an additional JavaScript file that will take care of loading the WebAssembly code. This file is not "standard" and may be different for every project, but the essential commands will be very similar.

Create a new file named `wasm.js` with this code and save it in the root of your project along with the other files:

    :::javascript
    'use strict';

    const WASM_URL = 'wasm.wasm';
    var wasm;

    function init() {
        const go = new Go();

        if ('instantiateStreaming' in WebAssembly) {
            WebAssembly.instantiateStreaming(fetch(WASM_URL), go.importObject).then(function (obj) {
                wasm = obj.instance;
                go.run(wasm);
            })
        }
    }

    init();

## HTML page to collect input and show result

We create a simple HTML page that will display two input boxes and a third one to show the result. Create a new file named `index.html` in the root of your project:

    :::html
    <!DOCTYPE html>

    <html>

    <head>
        <meta charset="utf-8" />
        <title>Go WebAssembly</title>
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <script src="wasm_exec.js"></script>
        <script src="wasm.js"></script>
    </head>

    <body>
        <h1>WebAssembly</h1>
        <p>Add two numbers, using WebAssembly calling an add() method written in Go:</p>
        <input type="number" id="a" value="2" /> + <input type="number" id="b" value="2" /> = <input type="number" id="result"/>
        <button>Calculate</button>
        <script>
            const button = document.querySelector('button');

            button.addEventListener('click', event => {
                var a = parseInt(document.getElementById("a").value);
                var b = parseInt(document.getElementById("b").value);
                var res = wasm.exports.add(a, b);
                var sum_box = document.getElementById("result");
                sum_box.value = res;
            });
        </script>
    </body>

    </html>

**Please note:** frontend development is really not my daily bread. I'm sure the above code can be written in a better way, but I can assure you that at least it works.

## Serving the static files

The project itself would be complete, but you need something able to serve static pages and set a couple of required headers. We can implement one with a few lines of Go. Create a new file named `server.go`:

    :::golang
    package main

    import (
        "log"
        "net/http"
        "strings"
    )

    const dir = "./"

    func main() {
        fs := http.FileServer(http.Dir(dir))
        log.Print("Serving " + dir + " on http://localhost:8080")
        http.ListenAndServe(":8080", http.HandlerFunc(func(resp http.ResponseWriter, req *http.Request) {
            resp.Header().Add("Cache-Control", "no-cache")
            if strings.HasSuffix(req.URL.Path, ".wasm") {
                resp.Header().Set("content-type", "application/wasm")
            }
            fs.ServeHTTP(resp, req)
        }))
    }

## Testing the project

The project is now complete and can be tested. There are at least two methods to check if everything works: **using the webpage** we just created and **calling the method from the JavaScript console**.

To test the application using the web page, run the server from the command line:

    :::shell
    go run server.go

Open a **web browser** and visit the address <http://localhost:8080>

You should see something like this:

[![web assembly browser]({static}/images/2020/10/tinygo_web_assembly_browser.png){width=60%}]()


Once the page is loaded you can also open the **JavaScript console** (it's in you browser developers tools and at least Chrome and Firefox have one) and call the method directly:

[![web assembly js console]({static}/images/2020/10/tinygo_web_assembly_js_console.png){width=60%}]()

## Conclusion

If you want to learn more about **TinyGo** I suggest you to visit the project website <https://tinygo.org> while more technical information and details about **WebAssembly** can be found here <https://webassembly.org>

You can find the **complete source code** of this project on **GitHub**: <https://github.com/andreagrandi/tinygo-adder>

## Credits

I want to thank my colleague [Ross Jones](https://twitter.com/rossjones) for introducing me to WASM and for the help given.

## References

- <https://tinygo.org/webassembly>
- <https://webassembly.org/>
