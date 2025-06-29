# Phaser.Physics.Matter.Components.Mass

Scope:
static

> Source: [src/physics/matter-js/components/Mass.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Mass.js#L10)  
> Since: 3.0.0

# Static functions

## setDensity

### <instance> setDensity(value)

**Description:**

Sets density of the body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new density of the body. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Mass](physics-matter-components-mass.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Mass.js#L35](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Mass.js#L35)  
> Since: 3.0.0

---

## setMass

### <instance> setMass(value)

**Description:**

Sets the mass of the Game Object's Matter Body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new mass of the body. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.Components.Mass](physics-matter-components-mass.md) - This Game Object instance.

> Source: [src/physics/matter-js/components/Mass.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Mass.js#L18)  
> Since: 3.0.0

---

# Static functions

## centerOfMass

### centerOfMass: [Phaser.Math.Vector2](../class/math-vector2.md)

**Description:**

The body's center of mass.

Calling this creates a new `Vector2 each time to avoid mutation.

If you only need to read the value and won't change it, you can get it from `GameObject.body.centerOfMass`.

**Returns:** [Phaser.Math.Vector2](../class/math-vector2.md) - The center of mass.

> Source: [src/physics/matter-js/components/Mass.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/components/Mass.js#L52)  
> Since: 3.10.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [setDensity](#setdensity)

    - [<instance> setDensity(value)](#instance-setdensityvalue)
  + [setMass](#setmass)

    - [<instance> setMass(value)](#instance-setmassvalue)
* [Static functions](#static-functions-1)

  + [centerOfMass](#centerofmass)

    - [centerOfMass: Phaser.Math.Vector2](#centerofmass-phasermathvector2)

Back to top

©2025[Phaser](https://docs.phaser.io)



Phaser.Physics.Matter.Components.Mass