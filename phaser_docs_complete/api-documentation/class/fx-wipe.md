# Wipe

Phaser.FX.Wipe

The Wipe FX Controller.

This FX controller manages the wipe effect for a Game Object.

The wipe or reveal effect is a visual technique that gradually uncovers or conceals elements

in the game, such as images, text, or scene transitions. This effect is often used to create

a sense of progression, reveal hidden content, or provide a smooth and visually appealing transition

between game states.

You can set both the direction and the axis of the wipe effect. The following combinations are possible:

* left to right: direction 0, axis 0
* right to left: direction 1, axis 0
* top to bottom: direction 1, axis 1
* bottom to top: direction 1, axis 0

It is up to you to set the `progress` value yourself, i.e. via a Tween, in order to transition the effect.

A Wipe effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addWipe();

sprite.postFX.addWipe();

sprite.preFX.addReveal();

sprite.postFX.addReveal();


```

**Constructor**

`new Wipe(gameObject, [wipeWidth], [direction], [axis], [reveal])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- | --- |
| wipeWidth | number | Yes | 0.1 | The width of the wipe effect. This value is normalized in the range 0 to 1. |
| direction | number | Yes | 0 | The direction of the wipe effect. Either 0 or 1. Set in conjunction with the axis property. |
| axis | number | Yes | 0 | The axis of the wipe effect. Either 0 or 1. Set in conjunction with the direction property. |
| reveal | boolean | Yes | false | Is this a reveal (true) or a fade (false) effect? |

---

**Scope**: static

**Extends**

> [Phaser.FX.Controller](fx-controller.md)

> Source: [src/fx/Wipe.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Wipe.js#L11)  
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

## axis

### axis: number

**Description:**

The axis of the wipe effect. Either 0 or 1. Set in conjunction with the direction property.

> Source: [src/fx/Wipe.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Wipe.js#L98)  
> Since: 3.60.0

---

## direction

### direction: number

**Description:**

The direction of the wipe effect. Either 0 or 1. Set in conjunction with the axis property.

> Source: [src/fx/Wipe.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Wipe.js#L89)  
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

## progress

### progress: number

**Description:**

The progress of the Wipe effect. This value is normalized to the range 0 to 1.

Adjust this value to make the wipe transition (i.e. via a Tween)

> Source: [src/fx/Wipe.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Wipe.js#L69)  
> Since: 3.60.0

---

## reveal

### reveal: boolean

**Description:**

Is this a reveal (true) or a fade (false) effect?

> Source: [src/fx/Wipe.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Wipe.js#L107)  
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

## wipeWidth

### wipeWidth: number

**Description:**

The width of the wipe effect. This value is normalized in the range 0 to 1.

> Source: [src/fx/Wipe.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Wipe.js#L80)  
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

**Returns:** [Phaser.FX.Wipe](fx-wipe.md) - This FX Controller instance.

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
  + [axis](#axis)

    - [axis: number](#axis-number)
  + [direction](#direction)

    - [direction: number](#direction-number)
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [progress](#progress)

    - [progress: number](#progress-number)
  + [reveal](#reveal)

    - [reveal: boolean](#reveal-boolean)
  + [type](#type)

    - [type: number](#type-number)
  + [wipeWidth](#wipewidth)

    - [wipeWidth: number](#wipewidth-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)