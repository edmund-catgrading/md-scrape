# Phaser.Physics.Arcade.Components.Collision

Scope:
static

> Source: [src/physics/arcade/components/Collision.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L9)  
> Since: 3.70.0

# Static functions

## addCollidesWith

### <instance> addCollidesWith(category)

**Description:**

Adds the given Collision Category to the list of those that this

Arcade Physics Body will collide with.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category to add. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Collision](physics-arcade-components-collision.md) - This Game Object.

> Source: [src/physics/arcade/components/Collision.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L60)  
> Since: 3.70.0

---

## removeCollidesWith

### <instance> removeCollidesWith(category)

**Description:**

Removes the given Collision Category from the list of those that this

Arcade Physics Body will collide with.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category to add. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Collision](physics-arcade-components-collision.md) - This Game Object.

> Source: [src/physics/arcade/components/Collision.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L80)  
> Since: 3.70.0

---

## resetCollisionCategory

### <instance> resetCollisionCategory()

**Description:**

Resets the Collision Category and Mask back to the defaults,

which is to collide with everything.

**Returns:** [Phaser.Physics.Arcade.Components.Collision](physics-arcade-components-collision.md) - This Game Object.

> Source: [src/physics/arcade/components/Collision.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L130)  
> Since: 3.70.0

---

## setCollidesWith

### <instance> setCollidesWith(categories)

**Description:**

Sets all of the Collision Categories that this Arcade Physics Body

will collide with. You can either pass a single category value, or

an array of them.

Calling this method will reset all of the collision categories,

so only those passed to this method are enabled.

If you wish to add a new category to the existing mask, call

the `addCollisionCategory` method.

If you wish to reset the collision category and mask, call

the `resetCollisionCategory` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| categories | number | Array.<number> | No | The collision category to collide with, or an array of them. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Collision](physics-arcade-components-collision.md) - This Game Object.

> Source: [src/physics/arcade/components/Collision.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L100)  
> Since: 3.70.0

---

## setCollisionCategory

### <instance> setCollisionCategory(category)

**Description:**

Sets the Collision Category that this Arcade Physics Body

will use in order to determine what it can collide with.

It can only have one single category assigned to it.

If you wish to reset the collision category and mask, call

the `resetCollisionCategory` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.Components.Collision](physics-arcade-components-collision.md) - This Game Object.

> Source: [src/physics/arcade/components/Collision.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L17)  
> Since: 3.70.0

---

## willCollideWith

### <instance> willCollideWith(category)

**Description:**

Checks to see if the given Collision Category will collide with

this Arcade Physics object or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | Collision category value to test. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the given category will collide with this object, otherwise `false`.

> Source: [src/physics/arcade/components/Collision.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L42)  
> Since: 3.70.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [addCollidesWith](#addcollideswith)

    - [<instance> addCollidesWith(category)](#instance-addcollideswithcategory)
  + [removeCollidesWith](#removecollideswith)

    - [<instance> removeCollidesWith(category)](#instance-removecollideswithcategory)
  + [resetCollisionCategory](#resetcollisioncategory)

    - [<instance> resetCollisionCategory()](#instance-resetcollisioncategory)
  + [setCollidesWith](#setcollideswith)

    - [<instance> setCollidesWith(categories)](#instance-setcollideswithcategories)
  + [setCollisionCategory](#setcollisioncategory)

    - [<instance> setCollisionCategory(category)](#instance-setcollisioncategorycategory)
  + [willCollideWith](#willcollidewith)

    - [<instance> willCollideWith(category)](#instance-willcollidewithcategory)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.Physics.Arcade.Components.Collision