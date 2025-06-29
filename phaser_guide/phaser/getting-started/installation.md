# Installing

How to install Phaser

## Create Phaser Game App

The easiest way to get started quickly with Phaser is our `create-phaser-game` app. This CLI tool presents an interactive selection of official project templates and demo games. Issue the command, answer some questions and the app will download and configure the right package for you.

```
Copynpm create @phaserjs/game@latest
npx @phaserjs/create-game@latest
yarn create @phaserjs/game
pnpm create @phaserjs/game@latest
bun create @phaserjs/game@latest

```

We have a [create game app tutorial](https://phaser.io/tutorials/create-game-app) you can read to learn more about this tool and what it offers.

## Installing Phaser from NPM

Install via [npm](https://www.npmjs.com/package/phaser):

```
Copynpm install phaser

```

## Cloning Phaser from GitHub

Phaser is available on GitHub at <https://github.com/phaserjs/phaser>

You can clone it via git with either:

```
Copyhttps://github.com/phaserjs/phaser.git
# or
git@github.com:phaserjs/phaser.git

```

Or, you can use GitHub Desktop. See the [Phaser GitHub page](https://github.com/phaserjs/phaser) for details.

## Using Phaser from a CDN

[Phaser is on jsDelivr](https://www.jsdelivr.com/package/npm/phaser) which is a "super-fast CDN for developers". Include *either* of the following in your html:

```
Copy<script src="//cdn.jsdelivr.net/npm/phaser@3.86.0/dist/phaser.js"></script>
<script src="//cdn.jsdelivr.net/npm/phaser@3.86.0/dist/phaser.min.js"></script>

```

It is also available from Cloudflare's [cdnjs](https://cdnjs.com/libraries/phaser):

```
Copy<script src="https://cdnjs.cloudflare.com/ajax/libs/phaser/3.86.0/phaser.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/phaser/3.86.0/phaser.min.js"></script>

```

## Phaser TypeScript Definitions

Full TypeScript definitions can be found inside the [types folder](https://github.com/phaserjs/phaser/tree/master/types). They are also referenced in the `types` entry in `package.json`, meaning modern editors such as VSCode will detect them automatically.

Depending on your project, you may need to add the following to your `tsconfig.json` file:

```
Copy"lib": ["es6", "dom", "dom.iterable", "scripthost"],
"typeRoots": ["./node_modules/phaser/types"],
"types": ["Phaser"]

```

Updated on June 4, 2025, 1:16 PM UTC

---

[What is Phaser?](../../index.md)

[Working with Phaser](set-up-dev-environment.md)

On this page

* [Installing](#installing)

  + [Create Phaser Game App](#create-phaser-game-app)
  + [Installing Phaser from NPM](#installing-phaser-from-npm)
  + [Cloning Phaser from GitHub](#cloning-phaser-from-github)
  + [Using Phaser from a CDN](#using-phaser-from-a-cdn)
  + [Phaser TypeScript Definitions](#phaser-typescript-definitions)

Back to top

©2025[Phaser](../../index.md)