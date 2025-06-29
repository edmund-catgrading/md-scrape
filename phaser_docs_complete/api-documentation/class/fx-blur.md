# Blur

Phaser.FX.Blur

The Blur FX Controller.

This FX controller manages the blur effect for a Game Object.

A Gaussian blur is the result of blurring an image by a Gaussian function. It is a widely used effect,

typically to reduce image noise and reduce detail. The visual effect of this blurring technique is a

smooth blur resembling that of viewing the image through a translucent screen, distinctly different

from the bokeh effect produced by an out-of-focus lens or the shadow of an object under usual illumination.

A Blur effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addBlur();

sprite.postFX.addBlur();


```

**Constructor**

`new Blur(gameObject, [quality], [x], [y], [strength], [color], [steps])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- | --- |
| quality | number | Yes | 0 | The quality of the blur effect. Can be either 0 for Low Quality, 1 for Medium Quality or 2 for High Quality. |
| x | number | Yes | 2 | The horizontal offset of the blur effect. |
| y | number | Yes | 2 | The vertical offset of the blur effect. |
| strength | number | Yes | 1 | The strength of the blur effect. |
| color | number | Yes | "0xffffff" | The color of the blur, as a hex value. |
| steps | number | Yes | 4 | The number of steps to run the blur effect for. This value should always be an integer. |

---

**Scope**: static

**Extends**

> [Phaser.FX.Controller](fx-controller.md)

> Source: [src/fx/Blur.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Blur.js#L11)  
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

## color

### color: number

**Description:**

The color of the blur as a number value.

> Source: [src/fx/Blur.js#L143](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Blur.js#L143)  
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

## glcolor

### glcolor: Array.<number>

**Description:**

The internal gl color array.

> Source: [src/fx/Blur.js#L128](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Blur.js#L128)  
> Since: 3.60.0

---

## quality

### quality: number

**Description:**

The quality of the blur effect.

This can be:

0 for Low Quality

1 for Medium Quality

2 for High Quality

The higher the quality, the more complex shader is used

and the more processing time is spent on the GPU calculating

the final blur. This value is used in conjunction with the

`steps` value, as one has a direct impact on the other.

Keep this value as low as you can, while still achieving the

desired effect you need for your game.

> Source: [src/fx/Blur.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Blur.js#L61)  
> Since: 3.60.0

---

## steps

### steps: number

**Description:**

The number of steps to run the Blur effect for.

This value should always be an integer.

It defaults to 4. The higher the value, the smoother the blur,

but at the cost of exponentially more gl operations.

Keep this to the lowest possible number you can have it, while

still looking correct for your game.

> Source: [src/fx/Blur.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Blur.js#L102)  
> Since: 3.60.0

---

## strength

### strength: number

**Description:**

The strength of the blur effect.

> Source: [src/fx/Blur.js#L119](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Blur.js#L119)  
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

## x

### x: number

**Description:**

The horizontal offset of the blur effect.

> Source: [src/fx/Blur.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Blur.js#L84)  
> Since: 3.60.0

---

## y

### y: number

**Description:**

The vertical offset of the blur effect.

> Source: [src/fx/Blur.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Blur.js#L93)  
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

**Returns:** [Phaser.FX.Blur](fx-blur.md) - This FX Controller instance.

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
  + [color](#color)

    - [color: number](#color-number)
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [glcolor](#glcolor)

    - [glcolor: Array.<number>](#glcolor-arraynumber)
  + [quality](#quality)

    - [quality: number](#quality-number)
  + [steps](#steps)

    - [steps: number](#steps-number)
  + [strength](#strength)

    - [strength: number](#strength-number)
  + [type](#type)

    - [type: number](#type-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)