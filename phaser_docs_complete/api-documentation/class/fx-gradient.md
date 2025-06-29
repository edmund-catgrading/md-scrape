# Gradient

Phaser.FX.Gradient

The Gradient FX Controller.

This FX controller manages the gradient effect for a Game Object.

The gradient overlay effect is a visual technique where a smooth color transition is applied over Game Objects,

such as sprites or UI components. This effect is used to enhance visual appeal, emphasize depth, or create

stylistic and atmospheric variations. It can also be utilized to convey information, such as representing

progress or health status through color changes.

A Gradient effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addGradient();

sprite.postFX.addGradient();


```

**Constructor**

`new Gradient(gameObject, [color1], [color2], [alpha], [fromX], [fromY], [toX], [toY], [size])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- | --- |
| color1 | number | Yes | "0xff0000" | The first gradient color, given as a number value. |
| color2 | number | Yes | "0x00ff00" | The second gradient color, given as a number value. |
| alpha | number | Yes | 0.2 | The alpha value of the gradient effect. |
| fromX | number | Yes | 0 | The horizontal position the gradient will start from. This value is normalized, between 0 and 1, and is not in pixels. |
| fromY | number | Yes | 0 | The vertical position the gradient will start from. This value is normalized, between 0 and 1, and is not in pixels. |
| toX | number | Yes | 0 | The horizontal position the gradient will end at. This value is normalized, between 0 and 1, and is not in pixels. |
| toY | number | Yes | 1 | The vertical position the gradient will end at. This value is normalized, between 0 and 1, and is not in pixels. |
| size | number | Yes | 0 | How many 'chunks' the gradient is divided in to, as spread over the entire height of the texture. Leave this at zero for a smooth gradient, or set higher for a more retro chunky effect. |

---

**Scope**: static

**Extends**

> [Phaser.FX.Controller](fx-controller.md)

> Source: [src/fx/Gradient.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L11)  
> Since: 3.60.0

# Public Members

## active

### active: boolean

**Description:**

Toggle this boolean to enable or disable this effect,

without removing and adding it from the Game Object.

Only works for Pre FX.

Post FX are always active.

**Inherits:** [Phaser.FX.Controller#active](fx-controller.md)

> Source: [src/fx/Controller.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Controller.js#L47)  
> Since: 3.60.0

---

## alpha

### alpha: number

**Description:**

The alpha value of the gradient effect.

> Source: [src/fx/Gradient.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L64)  
> Since: 3.60.0

---

## color1

### color1: number

**Description:**

The first gradient color, given as a number value.

> Source: [src/fx/Gradient.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L150)  
> Since: 3.60.0

---

## color2

### color2: number

**Description:**

The second gradient color, given as a number value.

> Source: [src/fx/Gradient.js#L177](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L177)  
> Since: 3.60.0

---

## fromX

### fromX: number

**Description:**

The horizontal position the gradient will start from. This value is normalized, between 0 and 1 and is not in pixels.

> Source: [src/fx/Gradient.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L85)  
> Since: 3.60.0

---

## fromY

### fromY: number

**Description:**

The vertical position the gradient will start from. This value is normalized, between 0 and 1 and is not in pixels.

> Source: [src/fx/Gradient.js#L94](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L94)  
> Since: 3.60.0

---

## gameObject

### gameObject: [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)

**Description:**

A reference to the Game Object that owns this effect.

**Inherits:** [Phaser.FX.Controller#gameObject](fx-controller.md)

> Source: [src/fx/Controller.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Controller.js#L38)  
> Since: 3.60.0

---

## glcolor1

### glcolor1: Array.<number>

**Description:**

The internal gl color array for the starting color.

> Source: [src/fx/Gradient.js#L121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L121)  
> Since: 3.60.0

---

## glcolor2

### glcolor2: Array.<number>

**Description:**

The internal gl color array for the ending color.

> Source: [src/fx/Gradient.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L130)  
> Since: 3.60.0

---

## size

### size: number

**Description:**

Sets how many 'chunks' the gradient is divided in to, as spread over the

entire height of the texture. Leave this at zero for a smooth gradient,

or set to a higher number to split the gradient into that many sections, giving

a more banded 'retro' effect.

> Source: [src/fx/Gradient.js#L73](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L73)  
> Since: 3.60.0

---

## toX

### toX: number

**Description:**

The horizontal position the gradient will end. This value is normalized, between 0 and 1 and is not in pixels.

> Source: [src/fx/Gradient.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L103)  
> Since: 3.60.0

---

## toY

### toY: number

**Description:**

The vertical position the gradient will end. This value is normalized, between 0 and 1 and is not in pixels.

> Source: [src/fx/Gradient.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Gradient.js#L112)  
> Since: 3.60.0

---

## type

### type: number

**Description:**

The FX\_CONST type of this effect.

**Inherits:** [Phaser.FX.Controller#type](fx-controller.md)

> Source: [src/fx/Controller.js#L29](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Controller.js#L29)  
> Since: 3.60.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this FX Controller.

**Inherits:** [Phaser.FX.Controller#destroy](fx-controller.md)

> Source: [src/fx/Controller.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Controller.js#L81)  
> Since: 3.60.0

---

## setActive

### <instance> setActive(value)

**Description:**

Sets the active state of this FX Controller.

A disabled FX Controller will not be updated.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to enable this FX Controller, or `false` to disable it. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FX.Gradient](fx-gradient.md) - This FX Controller instance.

**Inherits:** [Phaser.FX.Controller#setActive](fx-controller.md)

> Source: [src/fx/Controller.js#L62](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Controller.js#L62)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [color1](#color1)

    - [color1: number](#color1-number)
  + [color2](#color2)

    - [color2: number](#color2-number)
  + [fromX](#fromx)

    - [fromX: number](#fromx-number)
  + [fromY](#fromy)

    - [fromY: number](#fromy-number)
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [glcolor1](#glcolor1)

    - [glcolor1: Array.<number>](#glcolor1-arraynumber)
  + [glcolor2](#glcolor2)

    - [glcolor2: Array.<number>](#glcolor2-arraynumber)
  + [size](#size)

    - [size: number](#size-number)
  + [toX](#tox)

    - [toX: number](#tox-number)
  + [toY](#toy)

    - [toY: number](#toy-number)
  + [type](#type)

    - [type: number](#type-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)