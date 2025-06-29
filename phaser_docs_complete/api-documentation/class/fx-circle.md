# Circle

Phaser.FX.Circle

The Circle FX Controller.

This FX controller manages the circle effect for a Game Object.

This effect will draw a circle around the texture of the Game Object, effectively masking off

any area outside of the circle without the need for an actual mask. You can control the thickness

of the circle, the color of the circle and the color of the background, should the texture be

transparent. You can also control the feathering applied to the circle, allowing for a harsh or soft edge.

Please note that adding this effect to a Game Object will not change the input area or physics body of

the Game Object, should it have one.

A Circle effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addCircle();

sprite.postFX.addCircle();


```

**Constructor**

`new Circle(gameObject, [thickness], [color], [backgroundColor], [scale], [feather])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- | --- |
| thickness | number | Yes | 8 | The width of the circle around the texture, in pixels. |
| color | number | Yes | "0xfeedb6" | The color of the circular ring, given as a number value. |
| backgroundColor | number | Yes | "0xff0000" | The color of the background, behind the texture, given as a number value. |
| scale | number | Yes | 1 | The scale of the circle. The default scale is 1, which is a circle the full size of the underlying texture. |
| feather | number | Yes | 0.005 | The amount of feathering to apply to the circle from the ring. |

---

**Scope**: static

**Extends**

> [Phaser.FX.Controller](fx-controller.md)

> Source: [src/fx/Circle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Circle.js#L11)  
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

## backgroundAlpha

### backgroundAlpha: number

**Description:**

The alpha of the background, behind the texture, given as a number value.

> Source: [src/fx/Circle.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Circle.js#L180)  
> Since: 3.70.0

---

## backgroundColor

### backgroundColor: number

**Description:**

The color of the background, behind the texture, given as a number value.

> Source: [src/fx/Circle.js#L153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Circle.js#L153)  
> Since: 3.60.0

---

## color

### color: number

**Description:**

The color of the circular ring, given as a number value.

> Source: [src/fx/Circle.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Circle.js#L126)  
> Since: 3.60.0

---

## feather

### feather: number

**Description:**

The amount of feathering to apply to the circle from the ring,

extending into the middle of the circle. The default is 0.005,

which is a very low amount of feathering just making sure the ring

has a smooth edge. Increase this amount to a value such as 0.5

or 0.025 for larger amounts of feathering.

> Source: [src/fx/Circle.js#L73](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Circle.js#L73)  
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

The internal gl color array for the ring color.

> Source: [src/fx/Circle.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Circle.js#L97)  
> Since: 3.60.0

---

## glcolor2

### glcolor2: Array.<number>

**Description:**

The internal gl color array for the background color.

> Source: [src/fx/Circle.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Circle.js#L106)  
> Since: 3.60.0

---

## scale

### scale: number

**Description:**

The scale of the circle. The default scale is 1, which is a circle

the full size of the underlying texture. Reduce this value to create

a smaller circle, or increase it to create a circle that extends off

the edges of the texture.

> Source: [src/fx/Circle.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Circle.js#L61)  
> Since: 3.60.0

---

## thickness

### thickness: number

**Description:**

The width of the circle around the texture, in pixels. This value

doesn't factor in the feather, which can extend the thickness

internally depending on its value.

> Source: [src/fx/Circle.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/Circle.js#L86)  
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

**Returns:** [Phaser.FX.Circle](fx-circle.md) - This FX Controller instance.

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
  + [backgroundAlpha](#backgroundalpha)

    - [backgroundAlpha: number](#backgroundalpha-number)
  + [backgroundColor](#backgroundcolor)

    - [backgroundColor: number](#backgroundcolor-number)
  + [color](#color)

    - [color: number](#color-number)
  + [feather](#feather)

    - [feather: number](#feather-number)
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [glcolor](#glcolor)

    - [glcolor: Array.<number>](#glcolor-arraynumber)
  + [glcolor2](#glcolor2)

    - [glcolor2: Array.<number>](#glcolor2-arraynumber)
  + [scale](#scale)

    - [scale: number](#scale-number)
  + [thickness](#thickness)

    - [thickness: number](#thickness-number)
  + [type](#type)

    - [type: number](#type-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)