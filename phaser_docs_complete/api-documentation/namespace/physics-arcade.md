# Phaser.Physics.Arcade

Scope:
static

> Source: [src/physics/arcade/index.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/index.js#L10)

# Static functions

* [ArcadePhysics](../class/physics-arcade-arcadephysics.md)
* [Body](../class/physics-arcade-body.md)
* [Collider](../class/physics-arcade-collider.md)
* [Factory](../class/physics-arcade-factory.md)
* [Group](../class/physics-arcade-group.md)
* [Image](../class/physics-arcade-image.md)
* [Sprite](../class/physics-arcade-sprite.md)
* [StaticBody](../class/physics-arcade-staticbody.md)
* [StaticGroup](../class/physics-arcade-staticgroup.md)
* [World](../class/physics-arcade-world.md)

# Static functions

* [Components](physics-arcade-components.md)
* [Events](physics-arcade-events.md)
* [ProcessX](physics-arcade-processx.md)
* [ProcessY](physics-arcade-processy.md)
* [Tilemap](physics-arcade-tilemap.md)

# Static functions

## DYNAMIC\_BODY

### DYNAMIC\_BODY: number

**Description:**

Dynamic Body.

> Source: [src/physics/arcade/const.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/const.js#L15)  
> Since: 3.0.0

---

## FACING\_DOWN

### FACING\_DOWN: number

**Description:**

Facing down.

> Source: [src/physics/arcade/const.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/const.js#L85)  
> Since: 3.0.0

---

## FACING\_LEFT

### FACING\_LEFT: number

**Description:**

Facing left.

> Source: [src/physics/arcade/const.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/const.js#L97)  
> Since: 3.0.0

---

## FACING\_NONE

### FACING\_NONE: number

**Description:**

Facing no direction (initial value).

> Source: [src/physics/arcade/const.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/const.js#L61)  
> Since: 3.0.0

---

## FACING\_RIGHT

### FACING\_RIGHT: number

**Description:**

Facing right.

> Source: [src/physics/arcade/const.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/const.js#L109)  
> Since: 3.0.0

---

## FACING\_UP

### FACING\_UP: number

**Description:**

Facing up.

> Source: [src/physics/arcade/const.js#L73](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/const.js#L73)  
> Since: 3.0.0

---

## GROUP

### GROUP: number

**Description:**

Arcade Physics Group containing Dynamic Bodies.

> Source: [src/physics/arcade/const.js#L41](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/const.js#L41)  
> Since: 3.0.0

---

## STATIC\_BODY

### STATIC\_BODY: number

**Description:**

Static Body.

> Source: [src/physics/arcade/const.js#L28](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/const.js#L28)  
> Since: 3.0.0

---

## TILEMAPLAYER

### TILEMAPLAYER: number

**Description:**

A Tilemap Layer.

> Source: [src/physics/arcade/const.js#L51](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/const.js#L51)  
> Since: 3.0.0

---

# Static functions

## GetCollidesWith

### <static> GetCollidesWith(categories)

**Description:**

Calculates and returns the bitmask needed to determine if the given

categories will collide with each other or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| categories | number | Array.<number> | No | A unique category bitfield, or an array of them. |
| --- | --- | --- | --- |

**Returns:** number - The collision mask.

> Source: [src/physics/arcade/GetCollidesWith.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/GetCollidesWith.js#L7)  
> Since: 3.70.0

---

## GetOverlapX

### <static> GetOverlapX(body1, body2, overlapOnly, bias)

**Description:**

Calculates and returns the horizontal overlap between two arcade physics bodies and sets their properties

accordingly, including: `touching.left`, `touching.right`, `touching.none` and `overlapX'.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The first Body to separate. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The second Body to separate. |
| overlapOnly | boolean | No | Is this an overlap only check, or part of separation? |
| bias | number | No | A value added to the delta values during collision checks. Increase it to prevent sprite tunneling(sprites passing through another instead of colliding). |

**Returns:** number - The amount of overlap.

> Source: [src/physics/arcade/GetOverlapX.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/GetOverlapX.js#L9)  
> Since: 3.0.0

---

## GetOverlapY

### <static> GetOverlapY(body1, body2, overlapOnly, bias)

**Description:**

Calculates and returns the vertical overlap between two arcade physics bodies and sets their properties

accordingly, including: `touching.up`, `touching.down`, `touching.none` and `overlapY'.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The first Body to separate. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The second Body to separate. |
| overlapOnly | boolean | No | Is this an overlap only check, or part of separation? |
| bias | number | No | A value added to the delta values during collision checks. Increase it to prevent sprite tunneling(sprites passing through another instead of colliding). |

**Returns:** number - The amount of overlap.

> Source: [src/physics/arcade/GetOverlapY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/GetOverlapY.js#L9)  
> Since: 3.0.0

---

## SeparateX

### <static> SeparateX(body1, body2, overlapOnly, bias, [overlap])

**Description:**

Separates two overlapping bodies on the X-axis (horizontally).

Separation involves moving two overlapping bodies so they don't overlap anymore and adjusting their velocities based on their mass. This is a core part of collision detection.

The bodies won't be separated if there is no horizontal overlap between them, if they are static, or if either one uses custom logic for its separation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The first Body to separate. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The second Body to separate. |
| overlapOnly | boolean | No | If `true`, the bodies will only have their overlap data set and no separation will take place. |
| bias | number | No | A value to add to the delta value during overlap checking. Used to prevent sprite tunneling. |
| overlap | number | Yes | If given then this value will be used as the overlap and no check will be run. |

**Returns:** boolean - `true` if the two bodies overlap vertically, otherwise `false`.

> Source: [src/physics/arcade/SeparateX.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/SeparateX.js#L10)  
> Since: 3.0.0

---

## SeparateY

### <static> SeparateY(body1, body2, overlapOnly, bias, [overlap])

**Description:**

Separates two overlapping bodies on the Y-axis (vertically).

Separation involves moving two overlapping bodies so they don't overlap anymore and adjusting their velocities based on their mass. This is a core part of collision detection.

The bodies won't be separated if there is no vertical overlap between them, if they are static, or if either one uses custom logic for its separation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body1 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The first Body to separate. |
| --- | --- | --- | --- |
| body2 | [Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md) | No | The second Body to separate. |
| overlapOnly | boolean | No | If `true`, the bodies will only have their overlap data set and no separation will take place. |
| bias | number | No | A value to add to the delta value during overlap checking. Used to prevent sprite tunneling. |
| overlap | number | Yes | If given then this value will be used as the overlap and no check will be run. |

**Returns:** boolean - `true` if the two bodies overlap vertically, otherwise `false`.

> Source: [src/physics/arcade/SeparateY.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/SeparateY.js#L10)  
> Since: 3.0.0

---

## SetCollisionObject

### <static> SetCollisionObject(noneFlip, [data])

**Description:**

Either sets or creates the Arcade Body Collision object.

Mostly only used internally.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| noneFlip | boolean | No | Is `none` true or false? |
| --- | --- | --- | --- |
| data | [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md) | Yes | The collision data object to populate, or create if not given. |

**Returns:** [Phaser.Types.Physics.Arcade.ArcadeBodyCollision](../typedef/types-physics-arcade.md) - The collision data.

> Source: [src/physics/arcade/SetCollisionObject.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/SetCollisionObject.js#L7)  
> Since: 3.70.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)
* [Static functions](#static-functions-2)

  + [DYNAMIC\_BODY](#dynamic_body)

    - [DYNAMIC\_BODY: number](#dynamic_body-number)
  + [FACING\_DOWN](#facing_down)

    - [FACING\_DOWN: number](#facing_down-number)
  + [FACING\_LEFT](#facing_left)

    - [FACING\_LEFT: number](#facing_left-number)
  + [FACING\_NONE](#facing_none)

    - [FACING\_NONE: number](#facing_none-number)
  + [FACING\_RIGHT](#facing_right)

    - [FACING\_RIGHT: number](#facing_right-number)
  + [FACING\_UP](#facing_up)

    - [FACING\_UP: number](#facing_up-number)
  + [GROUP](#group)

    - [GROUP: number](#group-number)
  + [STATIC\_BODY](#static_body)

    - [STATIC\_BODY: number](#static_body-number)
  + [TILEMAPLAYER](#tilemaplayer)

    - [TILEMAPLAYER: number](#tilemaplayer-number)
* [Static functions](#static-functions-3)

  + [GetCollidesWith](#getcollideswith)

    - [<static> GetCollidesWith(categories)](#static-getcollideswithcategories)
  + [GetOverlapX](#getoverlapx)

    - [<static> GetOverlapX(body1, body2, overlapOnly, bias)](#static-getoverlapxbody1-body2-overlaponly-bias)
  + [GetOverlapY](#getoverlapy)

    - [<static> GetOverlapY(body1, body2, overlapOnly, bias)](#static-getoverlapybody1-body2-overlaponly-bias)
  + [SeparateX](#separatex)

    - [<static> SeparateX(body1, body2, overlapOnly, bias, [overlap])](#static-separatexbody1-body2-overlaponly-bias-overlap)
  + [SeparateY](#separatey)

    - [<static> SeparateY(body1, body2, overlapOnly, bias, [overlap])](#static-separateybody1-body2-overlaponly-bias-overlap)
  + [SetCollisionObject](#setcollisionobject)

    - [<static> SetCollisionObject(noneFlip, [data])](#static-setcollisionobjectnoneflip-data)

Back to top

©2025[Phaser](https://docs.phaser.io)