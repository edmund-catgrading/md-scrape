# Phaser.Physics.Arcade.Components.Drag

Scope:
static

> Source: [src/physics/arcade/components/Drag.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Drag.js#L7)  
> Since: 3.0.0

# Static functions

## setDamping

### <instance> setDamping(value)

**Description:**

If this Body is using `drag` for deceleration this function controls how the drag is applied.

If set to `true` drag will use a damping effect rather than a linear approach. If you are

creating a game where the Body moves freely at any angle (i.e. like the way the ship moves in

the game Asteroids) then you will get a far smoother and more visually correct deceleration

by using damping, avoiding the axis-drift that is prone with linear deceleration.

If you enable this property then you should use far smaller `drag` values than with linear, as

they are used as a multiplier on the velocity. Values such as 0.95 will give a nice slow

deceleration, where-as smaller values, such as 0.5 will stop an object almost immediately.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to use damping for deceleration, or `false` to use linear deceleration. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Drag](physics-arcade-components-drag.md) - This Game Object.

> Source: [src/physics/arcade/components/Drag.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Drag.js#L100)  
> Since: 3.10.0

---

## setDrag

### <instance> setDrag(x, [y])

**Description:**

Sets the body's horizontal and vertical drag. If the vertical drag value is not provided, the vertical drag is set to the same value as the horizontal drag.

Drag can be considered as a form of deceleration that will return the velocity of a body back to zero over time.

It is the absolute loss of velocity due to movement, in pixels per second squared.

The x and y components are applied separately.

When `useDamping` is true, this is 1 minus the damping factor.

A value of 1 means the Body loses no velocity.

A value of 0.95 means the Body loses 5% of its velocity per step.

A value of 0.5 means the Body loses 50% of its velocity per step.

Drag is applied only when `acceleration` is zero.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The amount of horizontal drag to apply. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The amount of vertical drag to apply. |

**Returns:** [Phaser.Physics.Arcade.Components.Drag](physics-arcade-components-drag.md) - This Game Object.

> Source: [src/physics/arcade/components/Drag.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Drag.js#L15)  
> Since: 3.0.0

---

## setDragX

### <instance> setDragX(value)

**Description:**

Sets the body's horizontal drag.

Drag can be considered as a form of deceleration that will return the velocity of a body back to zero over time.

It is the absolute loss of velocity due to movement, in pixels per second squared.

The x and y components are applied separately.

When `useDamping` is true, this is 1 minus the damping factor.

A value of 1 means the Body loses no velocity.

A value of 0.95 means the Body loses 5% of its velocity per step.

A value of 0.5 means the Body loses 50% of its velocity per step.

Drag is applied only when `acceleration` is zero.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The amount of horizontal drag to apply. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Drag](physics-arcade-components-drag.md) - This Game Object.

> Source: [src/physics/arcade/components/Drag.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Drag.js#L44)  
> Since: 3.0.0

---

## setDragY

### <instance> setDragY(value)

**Description:**

Sets the body's vertical drag.

Drag can be considered as a form of deceleration that will return the velocity of a body back to zero over time.

It is the absolute loss of velocity due to movement, in pixels per second squared.

The x and y components are applied separately.

When `useDamping` is true, this is 1 minus the damping factor.

A value of 1 means the Body loses no velocity.

A value of 0.95 means the Body loses 5% of its velocity per step.

A value of 0.5 means the Body loses 50% of its velocity per step.

Drag is applied only when `acceleration` is zero.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The amount of vertical drag to apply. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Drag](physics-arcade-components-drag.md) - This Game Object.

> Source: [src/physics/arcade/components/Drag.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Drag.js#L72)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [setDamping](#setdamping)

    - [<instance> setDamping(value)](#instance-setdampingvalue)
  + [setDrag](#setdrag)

    - [<instance> setDrag(x, [y])](#instance-setdragx-y)
  + [setDragX](#setdragx)

    - [<instance> setDragX(value)](#instance-setdragxvalue)
  + [setDragY](#setdragy)

    - [<instance> setDragY(value)](#instance-setdragyvalue)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.Physics.Arcade.Components.Drag