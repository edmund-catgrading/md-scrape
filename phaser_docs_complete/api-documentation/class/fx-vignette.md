# Vignette

Phaser.FX.Vignette

The Vignette FX Controller.

This FX controller manages the vignette effect for a Game Object.

The vignette effect is a visual technique where the edges of the screen, or a Game Object, gradually darken or blur,

creating a frame-like appearance. This effect is used to draw the player's focus towards the central action or subject,

enhance immersion, and provide a cinematic or artistic quality to the game's visuals.

A Vignette effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addVignette();

sprite.postFX.addVignette();


```

**Constructor**

`new Vignette(gameObject, [x], [y], [radius], [strength])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0.5 | The horizontal offset of the vignette effect. This value is normalized to the range 0 to 1. |
| y | number | Yes | 0.5 | The vertical offset of the vignette effect. This value is normalized to the range 0 to 1. |
| radius | number | Yes | 0.5 | The radius of the vignette effect. This value is normalized to the range 0 to 1. |
| strength | number | Yes | 0.5 | The strength of the vignette effect. |

---

**Scope**: static

**Extends**

> [Phaser.FX.Controller](fx-controller.md)

> Source: [src/fx/Vignette.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Vignette.js#L11)  
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

## radius

### radius: number

**Description:**

The radius of the vignette effect. This value is normalized to the range 0 to 1.

> Source: [src/fx/Vignette.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Vignette.js#L75)  
> Since: 3.60.0

---

## strength

### strength: number

**Description:**

The strength of the vignette effect.

> Source: [src/fx/Vignette.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Vignette.js#L84)  
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

The horizontal offset of the vignette effect. This value is normalized to the range 0 to 1.

> Source: [src/fx/Vignette.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Vignette.js#L57)  
> Since: 3.60.0

---

## y

### y: number

**Description:**

The vertical offset of the vignette effect. This value is normalized to the range 0 to 1.

> Source: [src/fx/Vignette.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Vignette.js#L66)  
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

**Returns:** [Phaser.FX.Vignette](fx-vignette.md) - This FX Controller instance.

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
  + [radius](#radius)

    - [radius: number](#radius-number)
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