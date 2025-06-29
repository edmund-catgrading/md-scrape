# Phaser.Physics.Matter.Components.Friction

Scope:
static

> Source: [src/physics/matter-js/components/Friction.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Friction.js#L7)  
> Since: 3.0.0

# Static functions

## setFriction

### <instance> setFriction(value, [air], [fstatic])

**Description:**

Sets new friction values for this Game Object's Matter Body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new friction of the body, between 0 and 1, where 0 allows the Body to slide indefinitely, while 1 allows it to stop almost immediately after a force is applied. |
| --- | --- | --- | --- |
| air | number | Yes | If provided, the new air resistance of the Body. The higher the value, the faster the Body will slow as it moves through space. 0 means the body has no air resistance. |
| fstatic | number | Yes | If provided, the new static friction of the Body. The higher the value (e.g. 10), the more force it will take to initially get the Body moving when it is nearly stationary. 0 means the body will never "stick" when it is nearly stationary. |

**Returns:** [Phaser.Physics.Matter.Components.Friction](physics-matter-components-friction.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Friction.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Friction.js#L15)  
> Since: 3.0.0

---

## setFrictionAir

### <instance> setFrictionAir(value)

**Description:**

Sets a new air resistance for this Game Object's Matter Body.

A value of 0 means the Body will never slow as it moves through space.

The higher the value, the faster a Body slows when moving through space.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new air resistance for the Body. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Friction](physics-matter-components-friction.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Friction.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Friction.js#L44)  
> Since: 3.0.0

---

## setFrictionStatic

### <instance> setFrictionStatic(value)

**Description:**

Sets a new static friction for this Game Object's Matter Body.

A value of 0 means the Body will never "stick" when it is nearly stationary.

The higher the value (e.g. 10), the more force it will take to initially get the Body moving when it is nearly stationary.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new static friction for the Body. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Friction](physics-matter-components-friction.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Friction.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Friction.js#L63)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [setFriction](#setfriction)

    - [<instance> setFriction(value, [air], [fstatic])](#instance-setfrictionvalue-air-fstatic)
  + [setFrictionAir](#setfrictionair)

    - [<instance> setFrictionAir(value)](#instance-setfrictionairvalue)
  + [setFrictionStatic](#setfrictionstatic)

    - [<instance> setFrictionStatic(value)](#instance-setfrictionstaticvalue)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.Physics.Matter.Components.Friction