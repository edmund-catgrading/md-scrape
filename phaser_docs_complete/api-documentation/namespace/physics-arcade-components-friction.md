# Phaser.Physics.Arcade.Components.Friction

Scope:
static

> Source: [src/physics/arcade/components/Friction.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Friction.js#L7)  
> Since: 3.0.0

# Static functions

## setFriction

### <instance> setFriction(x, [y])

**Description:**

Sets the friction of this game object's physics body.

In Arcade Physics, friction is a special case of motion transfer from an "immovable" body to a riding body.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The amount of horizontal friction to apply, [0, 1]. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The amount of vertical friction to apply, [0, 1]. |

**Returns:** [Phaser.Physics.Arcade.Components.Friction](physics-arcade-components-friction.md) - This Game Object.

> Source: [src/physics/arcade/components/Friction.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Friction.js#L19)  
> Since: 3.0.0

---

## setFrictionX

### <instance> setFrictionX(x)

**Description:**

Sets the horizontal friction of this game object's physics body.

This can move a riding body horizontally when it collides with this one on the vertical axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The amount of friction to apply, [0, 1]. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Friction](physics-arcade-components-friction.md) - This Game Object.

> Source: [src/physics/arcade/components/Friction.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Friction.js#L40)  
> Since: 3.0.0

---

## setFrictionY

### <instance> setFrictionY(y)

**Description:**

Sets the vertical friction of this game object's physics body.

This can move a riding body vertically when it collides with this one on the horizontal axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| y | number | No | The amount of friction to apply, [0, 1]. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Friction](physics-arcade-components-friction.md) - This Game Object.

> Source: [src/physics/arcade/components/Friction.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Friction.js#L60)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [setFriction](#setfriction)

    - [<instance> setFriction(x, [y])](#instance-setfrictionx-y)
  + [setFrictionX](#setfrictionx)

    - [<instance> setFrictionX(x)](#instance-setfrictionxx)
  + [setFrictionY](#setfrictiony)

    - [<instance> setFrictionY(y)](#instance-setfrictionyy)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.Physics.Arcade.Components.Friction