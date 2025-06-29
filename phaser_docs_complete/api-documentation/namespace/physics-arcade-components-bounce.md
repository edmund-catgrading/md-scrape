# Phaser.Physics.Arcade.Components.Bounce

Scope:
static

> Source: [src/physics/arcade/components/Bounce.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Bounce.js#L7)  
> Since: 3.0.0

# Static functions

## setBounce

### <instance> setBounce(x, [y])

**Description:**

Sets the bounce values of this body.

Bounce is the amount of restitution, or elasticity, the body has when it collides with another object.

A value of 1 means that it will retain its full velocity after the rebound. A value of 0 means it will not rebound at all.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The amount of horizontal bounce to apply on collision. A float, typically between 0 and 1. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The amount of vertical bounce to apply on collision. A float, typically between 0 and 1. |

**Returns:** [Phaser.Physics.Arcade.Components.Bounce](physics-arcade-components-bounce.md) - This Game Object.

> Source: [src/physics/arcade/components/Bounce.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Bounce.js#L15)  
> Since: 3.0.0

---

## setBounceX

### <instance> setBounceX(value)

**Description:**

Sets the horizontal bounce value for this body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The amount of horizontal bounce to apply on collision. A float, typically between 0 and 1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Bounce](physics-arcade-components-bounce.md) - This Game Object.

> Source: [src/physics/arcade/components/Bounce.js#L36](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Bounce.js#L36)  
> Since: 3.0.0

---

## setBounceY

### <instance> setBounceY(value)

**Description:**

Sets the vertical bounce value for this body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The amount of vertical bounce to apply on collision. A float, typically between 0 and 1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Bounce](physics-arcade-components-bounce.md) - This Game Object.

> Source: [src/physics/arcade/components/Bounce.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Bounce.js#L53)  
> Since: 3.0.0

---

## setCollideWorldBounds

### <instance> setCollideWorldBounds([value], [bounceX], [bounceY], [onWorldBounds])

**Description:**

Sets whether this Body collides with the world boundary.

Optionally also sets the World Bounce values. If the `Body.worldBounce` is null, it's set to a new Phaser.Math.Vector2 first.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | `true` if this body should collide with the world bounds, otherwise `false`. |
| --- | --- | --- | --- | --- |
| bounceX | number | Yes |  | If given this will be replace the `worldBounce.x` value. |
| bounceY | number | Yes |  | If given this will be replace the `worldBounce.y` value. |
| onWorldBounds | boolean | Yes |  | If given this replaces the Body's `onWorldBounds` value. |

**Returns:** [Phaser.Physics.Arcade.Components.Bounce](physics-arcade-components-bounce.md) - This Game Object.

> Source: [src/physics/arcade/components/Bounce.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Bounce.js#L70)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [setBounce](#setbounce)

    - [<instance> setBounce(x, [y])](#instance-setbouncex-y)
  + [setBounceX](#setbouncex)

    - [<instance> setBounceX(value)](#instance-setbouncexvalue)
  + [setBounceY](#setbouncey)

    - [<instance> setBounceY(value)](#instance-setbounceyvalue)
  + [setCollideWorldBounds](#setcollideworldbounds)

    - [<instance> setCollideWorldBounds([value], [bounceX], [bounceY], [onWorldBounds])](#instance-setcollideworldboundsvalue-bouncex-bouncey-onworldbounds)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.Physics.Arcade.Components.Bounce