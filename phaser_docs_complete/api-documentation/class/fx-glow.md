# Glow

Phaser.FX.Glow

The Glow FX Controller.

This FX controller manages the glow effect for a Game Object.

The glow effect is a visual technique that creates a soft, luminous halo around game objects,

characters, or UI elements. This effect is used to emphasize importance, enhance visual appeal,

or convey a sense of energy, magic, or otherworldly presence. The effect can also be set on

the inside of the Game Object. The color and strength of the glow can be modified.

A Glow effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addGlow();

sprite.postFX.addGlow();


```

**Constructor**

`new Glow(gameObject, [color], [outerStrength], [innerStrength], [knockout])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- | --- |
| color | number | Yes | "0xffffff" | The color of the glow effect as a number value. |
| outerStrength | number | Yes | 4 | The strength of the glow outward from the edge of the Sprite. |
| innerStrength | number | Yes | 0 | The strength of the glow inward from the edge of the Sprite. |
| knockout | boolean | Yes | false | If `true` only the glow is drawn, not the texture itself. |

---

**Scope**: static

**Extends**

> [Phaser.FX.Controller](fx-controller.md)

> Source: [src/fx/Glow.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Glow.js#L11)  
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

The color of the glow as a number value.

> Source: [src/fx/Glow.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Glow.js#L99)  
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

A 4 element array of gl color values.

> Source: [src/fx/Glow.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Glow.js#L84)  
> Since: 3.60.0

---

## innerStrength

### innerStrength: number

**Description:**

The strength of the glow inward from the edge of the Sprite.

> Source: [src/fx/Glow.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Glow.js#L66)  
> Since: 3.60.0

---

## knockout

### knockout: number

**Description:**

If `true` only the glow is drawn, not the texture itself.

> Source: [src/fx/Glow.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Glow.js#L75)  
> Since: 3.60.0

---

## outerStrength

### outerStrength: number

**Description:**

The strength of the glow outward from the edge of the Sprite.

> Source: [src/fx/Glow.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Glow.js#L57)  
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

**Returns:** [Phaser.FX.Glow](fx-glow.md) - This FX Controller instance.

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
  + [innerStrength](#innerstrength)

    - [innerStrength: number](#innerstrength-number)
  + [knockout](#knockout)

    - [knockout: number](#knockout-number)
  + [outerStrength](#outerstrength)

    - [outerStrength: number](#outerstrength-number)
  + [type](#type)

    - [type: number](#type-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)