# Phaser

Scope:
global

> Source: [src/phaser.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/phaser.js#L12)

# Static functions

* [FacebookInstantGamesLeaderboard](../class/facebookinstantgamesleaderboard.md)
* [FacebookInstantGamesPlugin](../class/facebookinstantgamesplugin.md)
* [Game](../class/game.md)
* [Scene](../class/scene.md)

# Static functions

* [Actions](actions.md)
* [Animations](animations.md)
* [BlendModes](blendmodes.md)
* [Cache](cache.md)
* [Cameras](cameras.md)
* [Core](core.md)
* [Create](create.md)
* [Curves](curves.md)
* [Data](data.md)
* [Device](device.md)
* [Display](display.md)
* [DOM](dom.md)
* [Events](events.md)
* [FX](fx.md)
* [GameObjects](gameobjects.md)
* [Geom](geom.md)
* [Input](input.md)
* [Loader](loader.md)
* [Math](math.md)
* [Physics](physics.md)
* [Plugins](plugins.md)
* [Renderer](renderer.md)
* [Scale](scale.md)
* [ScaleModes](scalemodes.md)
* [Scenes](scenes.md)
* [Sound](sound.md)
* [Structs](structs.md)
* [Textures](textures.md)
* [Tilemaps](tilemaps.md)
* [Time](time.md)
* [Tweens](tweens.md)
* [Types](types.md)
* [Utils](utils.md)

# Static functions

## AUTO

### AUTO: number

**Description:**

This setting will auto-detect if the browser is capable of suppporting WebGL.

If it is, it will use the WebGL Renderer. If not, it will fall back to the Canvas Renderer.

> Source: [src/const.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L39)  
> Since: 3.0.0

---

## CANVAS

### CANVAS: number

**Description:**

Forces Phaser to only use the Canvas Renderer, regardless if the browser supports

WebGL or not.

> Source: [src/const.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L50)  
> Since: 3.0.0

---

## DOWN

### DOWN: number

**Description:**

Direction constant.

> Source: [src/const.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L116)  
> Since: 3.0.0

---

## FOREVER

### FOREVER: number

**Description:**

In Phaser the value -1 means 'forever' in lots of cases, this const allows you to use it instead

to help you remember what the value is doing in your code.

> Source: [src/const.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L85)  
> Since: 3.0.0

---

## HEADLESS

### HEADLESS: number

**Description:**

A Headless Renderer doesn't create either a Canvas or WebGL Renderer. However, it still

absolutely relies on the DOM being present and available. This mode is meant for unit testing,

not for running Phaser on the server, which is something you really shouldn't do.

> Source: [src/const.js#L73](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L73)  
> Since: 3.0.0

---

## LEFT

### LEFT: number

**Description:**

Direction constant.

> Source: [src/const.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L126)  
> Since: 3.0.0

---

## LOG\_VERSION

### LOG\_VERSION: string

**Description:**

Phaser Release Version as displayed in the console.log header URL.

> Source: [src/const.js#L25](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L25)  
> Since: 3.87.0

---

## NONE

### NONE: number

**Description:**

Direction constant.

> Source: [src/const.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L96)  
> Since: 3.0.0

---

## RIGHT

### RIGHT: number

**Description:**

Direction constant.

> Source: [src/const.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L136)  
> Since: 3.0.0

---

## UP

### UP: number

**Description:**

Direction constant.

> Source: [src/const.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L106)  
> Since: 3.0.0

---

## VERSION

### VERSION: string

**Description:**

Phaser Release Version

> Source: [src/const.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L15)  
> Since: 3.0.0

---

## WEBGL

### WEBGL: number

**Description:**

Forces Phaser to use the WebGL Renderer. If the browser does not support it, there is

no fallback to Canvas with this setting, so you should trap it and display a suitable

message to the user.

> Source: [src/const.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/const.js#L61)  
> Since: 3.0.0

---

# Static functions

## DeviceConf

### DeviceConf

> Source: [src/device/index.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/device/index.js#L17)

---

# Static functions

## CSSBlendModes

### CSSBlendModes: string

**Description:**

Phaser Blend Modes to CSS Blend Modes Map.

> Source: [src/gameobjects/domelement/CSSBlendModes.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/domelement/CSSBlendModes.js#L7)  
> Since: 3.12.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)
* [Static functions](#static-functions-2)

  + [AUTO](#auto)

    - [AUTO: number](#auto-number)
  + [CANVAS](#canvas)

    - [CANVAS: number](#canvas-number)
  + [DOWN](#down)

    - [DOWN: number](#down-number)
  + [FOREVER](#forever)

    - [FOREVER: number](#forever-number)
  + [HEADLESS](#headless)

    - [HEADLESS: number](#headless-number)
  + [LEFT](#left)

    - [LEFT: number](#left-number)
  + [LOG\_VERSION](#log_version)

    - [LOG\_VERSION: string](#log_version-string)
  + [NONE](#none)

    - [NONE: number](#none-number)
  + [RIGHT](#right)

    - [RIGHT: number](#right-number)
  + [UP](#up)

    - [UP: number](#up-number)
  + [VERSION](#version)

    - [VERSION: string](#version-string)
  + [WEBGL](#webgl)

    - [WEBGL: number](#webgl-number)
* [Static functions](#static-functions-3)

  + [DeviceConf](#deviceconf)

    - [DeviceConf](#deviceconf-1)
* [Static functions](#static-functions-4)

  + [CSSBlendModes](#cssblendmodes)

    - [CSSBlendModes: string](#cssblendmodes-string)

Back to top

©2025[Phaser](https://docs.phaser.io)