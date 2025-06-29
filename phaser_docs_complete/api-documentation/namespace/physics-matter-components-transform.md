# Phaser.Physics.Matter.Components.Transform

Scope:
static

> Source: [src/physics/matter-js/components/Transform.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L17)  
> Since: 3.0.0

# Static functions

## angle

### angle: number

**Description:**

Use `angle` to set or get rotation of the physics body associated to this GameObject.

Unlike rotation, when using set the value can be in degrees, which will be converted to radians internally.

> Source: [src/physics/matter-js/components/Transform.js#L146](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L146)  
> Since: 3.0.0

---

## rotation

### rotation: number

**Description:**

Use `rotation` to set or get the rotation of the physics body associated with this GameObject.

The value when set must be in radians.

> Source: [src/physics/matter-js/components/Transform.js#L168](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L168)  
> Since: 3.0.0

---

## scaleX

### scaleX: number

**Description:**

The horizontal scale of this Game Object.

> Source: [src/physics/matter-js/components/Transform.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L71)  
> Since: 3.0.0

---

## scaleY

### scaleY: number

**Description:**

The vertical scale of this Game Object.

> Source: [src/physics/matter-js/components/Transform.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L109)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x position of this Game Object.

> Source: [src/physics/matter-js/components/Transform.js#L25](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L25)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of this Game Object.

> Source: [src/physics/matter-js/components/Transform.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L48)  
> Since: 3.0.0

---

# Static functions

## setAngle

### <instance> setAngle([degrees])

**Description:**

Immediately sets the angle of the Body.

Angular velocity, position, force etc. are unchanged.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| degrees | number | Yes | 0 | The angle to set, in degrees. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Transform](physics-matter-components-transform.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Transform.js#L255](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L255)  
> Since: 3.0.0

---

## setFixedRotation

### <instance> setFixedRotation()

**Description:**

Setting fixed rotation sets the Body inertia to Infinity, which stops it

from being able to rotate when forces are applied to it.

**Returns:** [Phaser.Physics.Matter.Components.Transform](physics-matter-components-transform.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Transform.js#L239](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L239)  
> Since: 3.0.0

---

## setPosition

### <instance> setPosition([x], [y])

**Description:**

Sets the position of the physics body along x and y axes.

Both the parameters to this function are optional and if not passed any they default to 0.

Velocity, angle, force etc. are unchanged.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of the body. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical position of the body. |

**Returns:** [Phaser.Physics.Matter.Components.Transform](physics-matter-components-transform.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Transform.js#L192](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L192)  
> Since: 3.0.0

---

## setRotation

### <instance> setRotation([radians])

**Description:**

Immediately sets the angle of the Body.

Angular velocity, position, force etc. are unchanged.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radians | number | Yes | 0 | The angle of the body, in radians. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Transform](physics-matter-components-transform.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Transform.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L217)  
> Since: 3.0.0

---

## setScale

### <instance> setScale([x], [y], [point])

**Description:**

Sets the scale of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 1 | The horizontal scale of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scale of this Game Object. If not set it will use the x value. |
| point | [Phaser.Math.Vector2](../class/math-vector2.md) | Yes |  | The point (Vector2) from which scaling will occur. |

**Returns:** [Phaser.Physics.Matter.Components.Transform](physics-matter-components-transform.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Transform.js#L277](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Transform.js#L277)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [angle](#angle)

    - [angle: number](#angle-number)
  + [rotation](#rotation)

    - [rotation: number](#rotation-number)
  + [scaleX](#scalex)

    - [scaleX: number](#scalex-number)
  + [scaleY](#scaley)

    - [scaleY: number](#scaley-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Static functions](#static-functions-1)

  + [setAngle](#setangle)

    - [<instance> setAngle([degrees])](#instance-setangledegrees)
  + [setFixedRotation](#setfixedrotation)

    - [<instance> setFixedRotation()](#instance-setfixedrotation)
  + [setPosition](#setposition)

    - [<instance> setPosition([x], [y])](#instance-setpositionx-y)
  + [setRotation](#setrotation)

    - [<instance> setRotation([radians])](#instance-setrotationradians)
  + [setScale](#setscale)

    - [<instance> setScale([x], [y], [point])](#instance-setscalex-y-point)

Back to top

©2025[Phaser](https://docs.phaser.io)