# Bloom

Phaser.FX.Bloom

The Bloom FX Controller.

This FX controller manages the bloom effect for a Game Object.

Bloom is an effect used to reproduce an imaging artifact of real-world cameras.

The effect produces fringes of light extending from the borders of bright areas in an image,

contributing to the illusion of an extremely bright light overwhelming the

camera or eye capturing the scene.

A Bloom effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addBloom();

sprite.postFX.addBloom();


```

**Constructor**

`new Bloom(gameObject, [color], [offsetX], [offsetY], [blurStrength], [strength], [steps])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- | --- |
| color | number | Yes | "0xffffff" | The color of the Bloom, as a hex value. |
| offsetX | number | Yes | 1 | The horizontal offset of the bloom effect. |
| offsetY | number | Yes | 1 | The vertical offset of the bloom effect. |
| blurStrength | number | Yes | 1 | The strength of the blur process of the bloom effect. |
| strength | number | Yes | 1 | The strength of the blend process of the bloom effect. |
| steps | number | Yes | 4 | The number of steps to run the Bloom effect for. This value should always be an integer. |

---

**Scope**: static

**Extends**

> [Phaser.FX.Controller](fx-controller.md)

> Source: [src/fx/Bloom.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Bloom.js#L11)  
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

## blurStrength

### blurStrength: number

**Description:**

The strength of the blur process of the bloom effect.

> Source: [src/fx/Bloom.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Bloom.js#L96)  
> Since: 3.60.0

---

## color

### color: number

**Description:**

The color of the bloom as a number value.

> Source: [src/fx/Bloom.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Bloom.js#L129)  
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

> Source: [src/fx/Bloom.js#L114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Bloom.js#L114)  
> Since: 3.60.0

---

## offsetX

### offsetX: number

**Description:**

The horizontal offset of the bloom effect.

> Source: [src/fx/Bloom.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Bloom.js#L78)  
> Since: 3.60.0

---

## offsetY

### offsetY: number

**Description:**

The vertical offset of the bloom effect.

> Source: [src/fx/Bloom.js#L87](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Bloom.js#L87)  
> Since: 3.60.0

---

## steps

### steps: number

**Description:**

The number of steps to run the Bloom effect for.

This value should always be an integer.

It defaults to 4. The higher the value, the smoother the Bloom,

but at the cost of exponentially more gl operations.

Keep this to the lowest possible number you can have it, while

still looking correct for your game.

> Source: [src/fx/Bloom.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Bloom.js#L61)  
> Since: 3.60.0

---

## strength

### strength: number

**Description:**

The strength of the blend process of the bloom effect.

> Source: [src/fx/Bloom.js#L105](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Bloom.js#L105)  
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

**Returns:** [Phaser.FX.Bloom](fx-bloom.md) - This FX Controller instance.

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
  + [blurStrength](#blurstrength)

    - [blurStrength: number](#blurstrength-number)
  + [color](#color)

    - [color: number](#color-number)
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [glcolor](#glcolor)

    - [glcolor: Array.<number>](#glcolor-arraynumber)
  + [offsetX](#offsetx)

    - [offsetX: number](#offsetx-number)
  + [offsetY](#offsety)

    - [offsetY: number](#offsety-number)
  + [steps](#steps)

    - [steps: number](#steps-number)
  + [strength](#strength)

    - [strength: number](#strength-number)
  + [type](#type)

    - [type: number](#type-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)