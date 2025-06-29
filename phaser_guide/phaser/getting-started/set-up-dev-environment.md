# Working with Phaser

How to set-up a Phaser Development Environment

In this tutorial we're going to cover setting-up a development environment with which you can build your Phaser games. This will include running a local web server, picking an IDE, getting the latest version of Phaser and checking it all works together.

If you trust us that you *do* need a local web server for development, then you can skip the explanation below and [head directly to part 2](#installing-a-web-server).

If you'd like to know the reasoning why, please read on ...

### A web server? But I want to make games!

Not these days, no. I appreciate that it's a bit confusing, even contradictory at times, but it all boils down to browser security. If you're making a static html web page then you can happily drag this file into your browser and see the end results. You can also "Save As" entire web pages locally and re-open them with most the contents intact. If both of these things work why can't you drag an HTML5 game into a browser and run it?

It's to do with the protocol used to access the files. When you request anything over the web you're using `http`, and the server level security is enough to ensure you can only access files you're meant to. But when you drag a file in it's loaded via the local file system (technically `file://`) and that is massively restricted, for obvious reasons. Under `file://` there's no concept of domains, no server level security, just a raw file system. If JavaScript had free reign while operating under `file://` there would be nothing stopping it loading pretty much *any* file, and sending it off who knows where.

Because this is so dangerous browsers lock themselves down when running under `file://`. Every single page becomes treated as a unique local domain. That is why "Save Web page" works, to a degree. It opens under the same cross-site restrictions as if they were on a live server.

There's a detailed post about it on the [Chromium blog](http://blog.chromium.org/2008/12/security-in-depth-local-web-pages.html) that is well worth a read if you'd like to learn more.

Your game is going to need to load resources: images, audio files, JSON data, maybe other JavaScript files. And in order to do this it needs to run unhindered by the browser security shackles. It needs `http://` access to the game files. And for that we need a web server.

## Installing a web server

### Windows

On Windows there are lots of "bundle installers" available which package together and set-up popular web technologies like Apache, PHP and MySQL from a single exe.

We would recommend [WAMP.Net](https://wamp.net/). It has an easy set-up guide available, installs an icon into your system-tray from which you can stop and restart the services, as well as modify Apache or Nginx settings and makes creating new sites a breeze, including with SSL certificates.

Cesanta provide the [Mongoose web server](https://cesanta.com/binary.html). This is a really small application that requires no installation and can run as a single exe file. Without all of the additional bundles like SSI and WebDAV (none of which you'll need for an HTML5 game) the exe is a paltry 45KB in size. Even the fully featured version is only 355KB.

Instead of an 'all in one' solution you could also download a web server on its own. Both [Microsoft IIS](http://www.iis.net) and [Apache](http://httpd.apache.org) can be downloaded for free.

### macOS

Being a Unix environment at heart there are more options available on macOS than Windows. But if you'd like an "all in one" approach like WAMP, with a nice clean and easy to use interface, then we'd strongly recommend [MAMP](http://www.mamp.info/en/index.html). This comes in two versions: one free and one paid for.

Naturally there are also guides for setting up a local web server manually, such as [this guide written for Mountain Lion](https://discussions.apple.com/docs/DOC-3083). Pick whichever approach you feel most comfortable with.

### Simple HTTP Server with Python

If you need a quick web server running and you don't want to mess around with setting up Apache or downloading an app, then Python can help. Python comes with a simple built-in HTTP server, which can serve files from any local folder. Naturally the only thing you need to have installed is Python. [Read the full guide here](http://www.linuxjournal.com/content/tech-tip-really-simple-http-server-python)

### http-server for node.js

*http-server* is a simple, zero-configuration command-line http server for [node.js](http://nodejs.org). It is powerful enough for production usage, but is simple and hackable enough to be used for testing, local development and learning. Or as the web site says "Serving up static files like they were turtles strapped to rockets". Get the npm and instructions from the [http-server web site](https://npmjs.org/package/http-server)

### php built-in web server

As of PHP 5.4.0, the CLI SAPI provides a built-in web server. It's only really suitable for development purposes and serves all files sequentially, but is easily powerful enough for testing HTML5 games. It's invoked from a single command-line call and you can find details on how to do this here [in the PHP Manual](http://php.net/manual/en/features.commandline.webserver.php).

However you do it, it's important to have the ability to serve files locally. With that done you're ready to pick an editor.

---

## Choosing an Editor

You're going to need an editor in which to prepare your JavaScript code. There are *many* available, each with their own strengths and weaknesses. If you're an experienced developer you will probably already have your own preferred editor, in which case carry on to Part 4 of this guide. Otherwise here are some options for you:

### Visual Studio Code

This is the editor the Phaser team use for building the framework and all projects. It's even the editor this guide is being written in.

Visual Studio Code is a lightweight but powerful source code editor which runs on your desktop and is available for Windows, macOS and Linux. It comes with built-in support for JavaScript, TypeScript and Node.js and has a rich ecosystem of extensions for other languages (such as C++, C#, Java, Python, PHP, Go) and runtimes (such as .NET and Unity).

Visit the [VS Code](https://code.visualstudio.com/) web site.

### Sublime Text

Sublime should be considered as an extremely powerful text editor rather than an IDE.

Features such as the ability to "Goto" anything, Split Editing, Multiple cursors, Distraction Free mode and loads of powerful Plugins make this the fastest and most versatile editor we've ever used in literally *decades* of development.

Using its comprehensive Package system you can enhance it in multiple ways. Here is an [excellent guide](http://scotch.io/bar-talk/best-of-sublime-text-3-features-plugins-and-settings) to features and packages for Sublime.

The full version costs $70 but is worth every penny and is available for Windows, OS X and Linux.

Visit the [Sublime Text](http://www.sublimetext.com) web site.

### WebStorm

JetBrains WebStorm is an extremely advanced full development environment. It goes well beyond simple code editing and offers all of the high-level features you'd expect from a proper IDE. Including code insight, npm built-in, code style and syntax reports, source control and a wealth of other features. Lots of the features are designed for web developers rather than game developers, but are still handy to have around.

It's based on IntelliJ IDEA, a heavily Java based editor, which is both a good and bad thing. For a start the actual code editing experience is nothing like as smooth and freeform as with Sublime, and the non-standard OS integration is weak. But the power features can often make up for that. Having errors with your code spotted for you, before you've even tested your game can be really useful. And code-completion is great too, although obviously somewhat limited by the myriad ways JavaScript can be written.

The full version starts from $49 and is available for Windows and OS X. There are often deals to be found on the JetBrains site too.

Visit the [JetBrains WebStorm](http://www.jetbrains.com/webstorm/) web site.

---

## Downloading Phaser

Phaser is made available as a JavaScript library. This can be downloaded, linked from a Content Delivery Network (CDN), or installed via any of the standard JavaScript package managers, such as npm. Phaser is not a desktop application. You do not 'install' it and there is no 'Phaser IDE'. It is a JavaScript library that you include in your own web pages, or bundle. You then write your game code in JavaScript and run them together in a web browser.

Phaser is an open source project and available to download for free. There are no fees to pay when using Phaser, regardless if you use it for a commercial or free project. We use GitHub to manage the project and you have various options on how to download it. These are all explained on the [download page](https://phaser.io/download/stable).

### Can I just get a zip/tar file?

> Get Phaser by cloning the repository, grabbing the js file or downloading it all as a zip

Yes. GitHub provides the option to download the whole repository as a zip or tar file. However we would strongly recommend you learn to use git instead. It will allow you to easily update to the latest versions of Phaser as they are released. And if in time you wish to contribute code towards Phaser it makes doing so much easier.

If you don't fancy learning to use git via the command-line there are some great applications you can use instead. We'd recommend [SmartGIT](http://www.syntevo.com/smartgithg/) on Windows or [Git Tower](http://www.git-tower.com) on macOS.

---

## Hello World!

With your editor set-up, web server installed and Phaser downloaded it's time to create something and check everything is working.

You need to discover where your 'web root' is on your machine. This is the folder in which the server looks for files. If you are using WAMP on Windows you can locate it by clicking the WAMP icon in your system-tray and select "www directory" from the pop-up menu. Other servers will have other methods of determining the location, but from this point on we'll refer to it as the 'webroot'.

Create a file called `index.html` inside of the webroot and paste the following code into it:

```
Copy<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/phaser@3.85.2/dist/phaser-arcade-physics.min.js"></script>
</head>
<body>

    <script>
    class Example extends Phaser.Scene
    {
        preload ()
        {
            this.load.setBaseURL('https://cdn.phaserfiles.com/v385');

            this.load.image('sky', 'assets/skies/space3.png');
            this.load.image('logo', 'assets/sprites/phaser3-logo.png');
            this.load.image('red', 'assets/particles/red.png');
        }

        create ()
        {
            this.add.image(400, 300, 'sky');

            const particles = this.add.particles(0, 0, 'red', {
                speed: 100,
                scale: { start: 1, end: 0 },
                blendMode: 'ADD'
            });

            const logo = this.physics.add.image(400, 100, 'logo');

            logo.setVelocity(100, 200);
            logo.setBounce(1, 1);
            logo.setCollideWorldBounds(true);

            particles.startFollow(logo);
        }
    }

    const config = {
        type: Phaser.AUTO,
        width: 800,
        height: 600,
        scene: Example,
        physics: {
            default: 'arcade',
            arcade: {
                gravity: { y: 200 }
            }
        }
    };

    const game = new Phaser.Game(config);
    </script>

</body>
</html>

```

### Testing, testing ...

Open your web browser and load the `index.html` page up. This may be as simple as typing in `localhost/` or `127.0.0.1/` into your browser. Or you may need to specify a port number as well, it depends entirely on which server set-up method you used.

If everything goes right it will display the following demo in your browser:

![Phaser 3 Demo](https://cdn.hashnode.com/res/hashnode/image/upload/v1749042988400/f86546d0-5174-4177-ac05-f6cd005c3beb.png?auto=compress,format&format=webp)

If it doesn't for whatever reason you need to bring up the debug console and see what errors are output. In most browsers you can do this by pressing `F12`. This works in Chrome, Firefox and Internet Explorer 11. Check to see what the error is, hopefully it's a simple one like a file being missing, in which case check your folder names and refresh the page.

If it's something more complex, please join us in the [Phaser Discord](https://phaser.io/community/discord) and talk in our Beginners channel. We'll try our best to help.

It's just a tiny example, and we've [hundreds more](https://phaser.io/examples) for you to explore, but hopefully it shows how expressive and quick Phaser is to use. With just a few easily readable lines of code we've got something pretty impressive up on screen!

## Phaser Examples

From the moment we released the first version of Phaser we knew that one of the best ways for people to learn how to use it would be to produce examples. So we set out to create many different examples, covering all the key areas of Phaser. From how to set-up animations to how to use the physics.

### Online Phaser Examples

You can browse all the [Phaser Examples](https://phaser.io/examples) on this site. You'll also find a live code editor, so you can modify the source and re-run it in real-time to see the changes immediately.

### Making a Game in Phaser Tutorial

Now you're all set-up we strongly recommend you work through the guide to [Making a Game in Phaser 3](https://phaser.io/tutorials/making-your-first-phaser-3-game). From it you'll learn how to construct a game allowing you to control a character who can leap off platforms and collect items.

## Next Steps

Your game development experience with Phaser begins here! Although we've only touched upon the basics, if you've followed this guide through you now have a fully working development environment, access to the API docs and hundreds of examples.

Even so it's always best to code as part of a community. And for that we cannot recommend our forum enough. It has gone from strength to strength over the past few months and you're sure to find help and support when you need it most.

Bounce ideas off others, hang-out in the chat room, browse the games showcase and just be involved!

[Join the Forum](https://phaser.io/community/forum) or [Chat on Discord](https://discord.gg/phaser)

### Contribute

You can help shape the way in which Phaser grows. If you find a bug, please report it. It won't take you long, and to date we have fixed over 91% of all reported issues (and we're still working on the other 9%). You can also issue Pull Requests against the development branch, or release your own plugins or filters.

[Report Issues on GitHub](https://github.com/phaserjs/phaser/issues/new)

### Show us your games!

We spend many tireless hours working on Phaser because we want it to be the best HTML5 game development framework it can possibly be. We understand it won't be perfect for everyone, and we're cool with that. But if you use it and make something, no matter how small you think that is, please do let us know. You won't believe what a real motivational boost it is when devs show us the games they've been working on! Reach out to us either on the forum, via twitter ([@phaser\_](https://twitter.com/phaser_)) or by [email](mailto:support@phaser.io).

Most of all though, we truly hope you have fun making your game.

Updated on June 4, 2025, 1:16 PM UTC

---

[Installing](installation.md)

[Project Templates](project-templates.md)

On this page

* [Working with Phaser](#working-with-phaser)

  + [A web server? But I want to make games!](#a-web-server-but-i-want-to-make-games)
  + [Installing a web server](#installing-a-web-server)

    - [Windows](#windows)
    - [macOS](#macos)
    - [Simple HTTP Server with Python](#simple-http-server-with-python)
    - [http-server for node.js](#http-server-for-nodejs)
    - [php built-in web server](#php-built-in-web-server)
  + [Choosing an Editor](#choosing-an-editor)

    - [Visual Studio Code](#visual-studio-code)
    - [Sublime Text](#sublime-text)
    - [WebStorm](#webstorm)
  + [Downloading Phaser](#downloading-phaser)

    - [Can I just get a zip/tar file?](#can-i-just-get-a-ziptar-file)
  + [Hello World!](#hello-world)

    - [Testing, testing ...](#testing-testing-)
  + [Phaser Examples](#phaser-examples)

    - [Online Phaser Examples](#online-phaser-examples)
    - [Making a Game in Phaser Tutorial](#making-a-game-in-phaser-tutorial)
  + [Next Steps](#next-steps)

    - [Contribute](#contribute)
    - [Show us your games!](#show-us-your-games)

Back to top

©2025[Phaser](../../index.md)