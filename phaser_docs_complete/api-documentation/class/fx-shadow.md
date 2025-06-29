# Shadow

Phaser.FX.Shadow

The Shadow FX Controller.

This FX controller manages the shadow effect for a Game Object.

The shadow effect is a visual technique used to create the illusion of depth and realism by adding darker,

offset silhouettes or shapes beneath game objects, characters, or environments. These simulated shadows

help to enhance the visual appeal and immersion, making the 2D game world appear more dynamic and three-dimensional.

A Shadow effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addShadow();

sprite.postFX.addShadow();


```

**Constructor**

`new Shadow(gameObject, [x], [y], [decay], [power], [color], [samples], [intensity])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal offset of the shadow effect. |
| y | number | Yes | 0 | The vertical offset of the shadow effect. |
| decay | number | Yes | 0.1 | The amount of decay for shadow effect. |
| power | number | Yes | 1 | The power of the shadow effect. |
| color | number | Yes | "0x000000" | The color of the shadow. |
| samples | number | Yes | 6 | The number of samples that the shadow effect will run for. An integer between 1 and 12. |
| intensity | number | Yes | 1 | The intensity of the shadow effect. |

---

**Scope**: static

**Extends**

> [Phaser.FX.Controller](fx-controller.md)

> Source: [src/fx/Shadow.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shadow.js#L11)  
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

The color of the shadow.

> Source: [src/fx/Shadow.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shadow.js#L133)  
> Since: 3.60.0

---

## decay

### decay: number

**Description:**

The amount of decay for the shadow effect.

> Source: [src/fx/Shadow.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shadow.js#L80)  
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

> Source: [src/fx/Shadow.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shadow.js#L98)  
> Since: 3.60.0

---

## intensity

### intensity: number

**Description:**

The intensity of the shadow effect.

> Source: [src/fx/Shadow.js#L118](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shadow.js#L118)  
> Since: 3.60.0

---

## power

### power: number

**Description:**

The power of the shadow effect.

> Source: [src/fx/Shadow.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shadow.js#L89)  
> Since: 3.60.0

---

## samples

### samples: number

**Description:**

The number of samples that the shadow effect will run for.

This should be an integer with a minimum value of 1 and a maximum of 12.

> Source: [src/fx/Shadow.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shadow.js#L107)  
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

The horizontal offset of the shadow effect.

> Source: [src/fx/Shadow.js#L62](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shadow.js#L62)  
> Since: 3.60.0

---

## y

### y: number

**Description:**

The vertical offset of the shadow effect.

> Source: [src/fx/Shadow.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shadow.js#L71)  
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

**Returns:** [Phaser.FX.Shadow](fx-shadow.md) - This FX Controller instance.

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
  + [decay](#decay)

    - [decay: number](#decay-number)
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [glcolor](#glcolor)

    - [glcolor: Array.<number>](#glcolor-arraynumber)
  + [intensity](#intensity)

    - [intensity: number](#intensity-number)
  + [power](#power)

    - [power: number](#power-number)
  + [samples](#samples)

    - [samples: number](#samples-number)
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