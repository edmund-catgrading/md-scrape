# Barrel

Phaser.FX.Barrel

The Barrel FX Controller.

This FX controller manages the barrel distortion effect for a Game Object.

A barrel effect allows you to apply either a 'pinch' or 'expand' distortion to

a Game Object. The amount of the effect can be modified in real-time.

A Barrel effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addBarrel();

sprite.postFX.addBarrel();


```

**Constructor**

`new Barrel(gameObject, [amount])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The amount of distortion applied to the barrel effect. A value of 1 is no distortion. Typically keep this within +- 1. |

---

**Scope**: static

**Extends**

> [Phaser.FX.Controller](fx-controller.md)

> Source: [src/fx/Barrel.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Barrel.js#L11)  
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

## amount

### amount: number

**Description:**

The amount of distortion applied to the barrel effect.

Typically keep this within the range 1 (no distortion) to +- 1.

> Source: [src/fx/Barrel.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Barrel.js#L50)  
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

**Returns:** [Phaser.FX.Barrel](fx-barrel.md) - This FX Controller instance.

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
  + [amount](#amount)

    - [amount: number](#amount-number)
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [type](#type)

    - [type: number](#type-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)