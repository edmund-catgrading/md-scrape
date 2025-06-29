# Phaser.Physics.Arcade.Components

Scope:
static

> Source: [src/physics/arcade/components/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/index.js#L7)

# Static functions

* [Acceleration](physics-arcade-components-acceleration.md)
* [Angular](physics-arcade-components-angular.md)
* [Bounce](physics-arcade-components-bounce.md)
* [Collision](physics-arcade-components-collision.md)
* [Debug](physics-arcade-components-debug.md)
* [Drag](physics-arcade-components-drag.md)
* [Enable](physics-arcade-components-enable.md)
* [Friction](physics-arcade-components-friction.md)
* [Gravity](physics-arcade-components-gravity.md)
* [Immovable](physics-arcade-components-immovable.md)
* [Mass](physics-arcade-components-mass.md)
* [Pushable](physics-arcade-components-pushable.md)
* [Size](physics-arcade-components-size.md)
* [Velocity](physics-arcade-components-velocity.md)

# Static functions

## OverlapCirc

### <static> OverlapCirc(x, y, radius, [includeDynamic], [includeStatic])

**Description:**

This method will search the given circular area and return an array of all physics bodies that

overlap with it. It can return either Dynamic, Static bodies or a mixture of both.

A body only has to intersect with the search area to be considered, it doesn't have to be fully

contained within it.

If Arcade Physics is set to use the RTree (which it is by default) then the search is rather fast,

otherwise the search is O(N) for Dynamic Bodies.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of the center of the area to search within. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate of the center of the area to search within. |
| radius | number | No |  | The radius of the area to search within. |
| includeDynamic | boolean | Yes | true | Should the search include Dynamic Bodies? |
| includeStatic | boolean | Yes | false | Should the search include Static Bodies? |

**Returns:** Array.<[Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md)>, Array.<[Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md)> - An array of bodies that overlap with the given area.

> Source: [src/physics/arcade/components/OverlapCirc.js#L6](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/OverlapCirc.js#L6)  
> Since: 3.21.0

---

## OverlapRect

### <static> OverlapRect(x, y, width, height, [includeDynamic], [includeStatic])

**Description:**

This method will search the given rectangular area and return an array of all physics bodies that

overlap with it. It can return either Dynamic, Static bodies or a mixture of both.

A body only has to intersect with the search area to be considered, it doesn't have to be fully

contained within it.

If Arcade Physics is set to use the RTree (which it is by default) then the search for is extremely fast,

otherwise the search is O(N) for Dynamic Bodies.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The top-left x coordinate of the area to search within. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The top-left y coordinate of the area to search within. |
| width | number | No |  | The width of the area to search within. |
| height | number | No |  | The height of the area to search within. |
| includeDynamic | boolean | Yes | true | Should the search include Dynamic Bodies? |
| includeStatic | boolean | Yes | false | Should the search include Static Bodies? |

**Returns:** Array.<[Phaser.Physics.Arcade.Body](../class/physics-arcade-body.md)>, Array.<[Phaser.Physics.Arcade.StaticBody](../class/physics-arcade-staticbody.md)> - An array of bodies that overlap with the given area.

> Source: [src/physics/arcade/components/OverlapRect.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/OverlapRect.js#L1)  
> Since: 3.17.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)

  + [OverlapCirc](#overlapcirc)

    - [<static> OverlapCirc(x, y, radius, [includeDynamic], [includeStatic])](#static-overlapcircx-y-radius-includedynamic-includestatic)
  + [OverlapRect](#overlaprect)

    - [<static> OverlapRect(x, y, width, height, [includeDynamic], [includeStatic])](#static-overlaprectx-y-width-height-includedynamic-includestatic)

Back to top

©2025[Phaser](https://docs.phaser.io)