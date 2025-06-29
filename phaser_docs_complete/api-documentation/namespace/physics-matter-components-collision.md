# Phaser.Physics.Matter.Components.Collision

Scope:
static

> Source: [src/physics/matter-js/components/Collision.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L7)  
> Since: 3.0.0

# Static functions

## setCollidesWith

### <instance> setCollidesWith(categories)

**Description:**

Sets the collision mask for this Game Object's Matter Body. Two Matter Bodies with different collision groups will only

collide if each one includes the other's category in its mask based on a bitwise AND, i.e. `(categoryA & maskB) !== 0`

and `(categoryB & maskA) !== 0` are both true.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| categories | number | Array.<number> | No | A unique category bitfield, or an array of them. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Collision](physics-matter-components-collision.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Collision.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L54)  
> Since: 3.0.0

---

## setCollisionCategory

### <instance> setCollisionCategory(value)

**Description:**

Sets the collision category of this Game Object's Matter Body. This number must be a power of two between 2^0 (= 1) and 2^31.

Two bodies with different collision groups (see <#setCollisionGroup>) will only collide if their collision

categories are included in their collision masks (see <#setCollidesWith>).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | Unique category bitfield. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Collision](physics-matter-components-collision.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Collision.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L15)  
> Since: 3.0.0

---

## setCollisionGroup

### <instance> setCollisionGroup(value)

**Description:**

Sets the collision group of this Game Object's Matter Body. If this is zero or two Matter Bodies have different values,

they will collide according to the usual rules (see <#setCollisionCategory> and <#setCollisionGroup>).

If two Matter Bodies have the same positive value, they will always collide; if they have the same negative value,

they will never collide.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | Unique group index. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Collision](physics-matter-components-collision.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Collision.js#L34](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L34)  
> Since: 3.0.0

---

## setOnCollide

### <instance> setOnCollide(callback)

**Description:**

The callback is sent a `Phaser.Types.Physics.Matter.MatterCollisionData` object.

This does not change the bodies collision category, group or filter. Those must be set in addition

to the callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The callback to invoke when this body starts colliding with another. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Collision](physics-matter-components-collision.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Collision.js#L87](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L87)  
> Since: 3.22.0

---

## setOnCollideActive

### <instance> setOnCollideActive(callback)

**Description:**

The callback is sent a `Phaser.Types.Physics.Matter.MatterCollisionData` object.

This does not change the bodies collision category, group or filter. Those must be set in addition

to the callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The callback to invoke for the duration of this body colliding with another. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Collision](physics-matter-components-collision.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Collision.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L127)  
> Since: 3.22.0

---

## setOnCollideEnd

### <instance> setOnCollideEnd(callback)

**Description:**

The callback is sent a `Phaser.Types.Physics.Matter.MatterCollisionData` object.

This does not change the bodies collision category, group or filter. Those must be set in addition

to the callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | function | No | The callback to invoke when this body stops colliding with another. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Collision](physics-matter-components-collision.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Collision.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L107)  
> Since: 3.22.0

---

## setOnCollideWith

### <instance> setOnCollideWith(body, callback)

**Description:**

The callback is sent a reference to the other body, along with a `Phaser.Types.Physics.Matter.MatterCollisionData` object.

This does not change the bodies collision category, group or filter. Those must be set in addition

to the callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | MatterJS.Body | Array.<MatterJS.Body> | No | The body, or an array of bodies, to test for collisions with. |
| --- | --- | --- | --- |
| callback | function | No | The callback to invoke when this body collides with the given body or bodies. |

**Returns:** [Phaser.Physics.Matter.Components.Collision](physics-matter-components-collision.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Collision.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Collision.js#L147)  
> Since: 3.22.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [setCollidesWith](#setcollideswith)

    - [<instance> setCollidesWith(categories)](#instance-setcollideswithcategories)
  + [setCollisionCategory](#setcollisioncategory)

    - [<instance> setCollisionCategory(value)](#instance-setcollisioncategoryvalue)
  + [setCollisionGroup](#setcollisiongroup)

    - [<instance> setCollisionGroup(value)](#instance-setcollisiongroupvalue)
  + [setOnCollide](#setoncollide)

    - [<instance> setOnCollide(callback)](#instance-setoncollidecallback)
  + [setOnCollideActive](#setoncollideactive)

    - [<instance> setOnCollideActive(callback)](#instance-setoncollideactivecallback)
  + [setOnCollideEnd](#setoncollideend)

    - [<instance> setOnCollideEnd(callback)](#instance-setoncollideendcallback)
  + [setOnCollideWith](#setoncollidewith)

    - [<instance> setOnCollideWith(body, callback)](#instance-setoncollidewithbody-callback)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.Physics.Matter.Components.Collision