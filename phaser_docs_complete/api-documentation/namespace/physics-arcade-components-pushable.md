# Phaser.Physics.Arcade.Components.Pushable

Scope:
static

> Source: [src/physics/arcade/components/Pushable.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Pushable.js#L7)  
> Since: 3.50.0

# Static functions

## setPushable

### <instance> setPushable([value])

**Description:**

Sets if this Body can be pushed by another Body.

A body that cannot be pushed will reflect back all of the velocity it is given to the

colliding body. If that body is also not pushable, then the separation will be split

between them evenly.

If you want your body to never move or seperate at all, see the `setImmovable` method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | Sets if this body can be pushed by collisions with another Body. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Pushable](physics-arcade-components-pushable.md) - This Game Object.

> Source: [src/physics/arcade/components/Pushable.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Pushable.js#L15)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [setPushable](#setpushable)

    - [<instance> setPushable([value])](#instance-setpushablevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.Physics.Arcade.Components.Pushable