# Shine

Phaser.FX.Shine

The Shine FX Controller.

This FX controller manages the shift effect for a Game Object.

The shine effect is a visual technique that simulates the appearance of reflective

or glossy surfaces by passing a light beam across a Game Object. This effect is used to

enhance visual appeal, emphasize certain features, and create a sense of depth or

material properties.

A Shine effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addShine();

sprite.postFX.addShine();


```

**Constructor**

`new Shine(gameObject, [speed], [lineWidth], [gradient], [reveal])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- | --- |
| speed | number | Yes | 0.5 | The speed of the Shine effect. |
| lineWidth | number | Yes | 0.5 | The line width of the Shine effect. |
| gradient | number | Yes | 3 | The gradient of the Shine effect. |
| reveal | boolean | Yes | false | Does this Shine effect reveal or get added to its target? |

---

**Scope**: static

**Extends**

> [Phaser.FX.Controller](fx-controller.md)

> Source: [src/fx/Shine.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shine.js#L11)  
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

## gameObject

### gameObject: [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)

**Description:**

A reference to the Game Object that owns this effect.

**Inherits:** [Phaser.FX.Controller#gameObject](fx-controller.md)

> Source: [src/fx/Controller.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Controller.js#L38)  
> Since: 3.60.0

---

## gradient

### gradient: number

**Description:**

The gradient of the Shine effect.

> Source: [src/fx/Shine.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shine.js#L76)  
> Since: 3.60.0

---

## lineWidth

### lineWidth: number

**Description:**

The line width of the Shine effect.

> Source: [src/fx/Shine.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shine.js#L67)  
> Since: 3.60.0

---

## reveal

### reveal: boolean

**Description:**

Does this Shine effect reveal or get added to its target?

> Source: [src/fx/Shine.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shine.js#L85)  
> Since: 3.60.0

---

## speed

### speed: number

**Description:**

The speed of the Shine effect.

> Source: [src/fx/Shine.js#L58](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Shine.js#L58)  
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

**Returns:** [Phaser.FX.Shine](fx-shine.md) - This FX Controller instance.

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
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [gradient](#gradient)

    - [gradient: number](#gradient-number)
  + [lineWidth](#linewidth)

    - [lineWidth: number](#linewidth-number)
  + [reveal](#reveal)

    - [reveal: boolean](#reveal-boolean)
  + [speed](#speed)

    - [speed: number](#speed-number)
  + [type](#type)

    - [type: number](#type-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)