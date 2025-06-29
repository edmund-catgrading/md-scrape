# Phaser.Types.Physics.Matter

Scope:
static

> Source: [src/physics/matter-js/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/index.js#L7)

# Static functions

## MatterBody

### MatterBody

> Source: [src/physics/matter-js/typedefs/MatterBody.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterBody.js#L1)  
> Since: 3.22.0

---

## MatterBodyConfig

### MatterBodyConfig

> Source: [src/physics/matter-js/typedefs/MatterBodyConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterBodyConfig.js#L1)  
> Since: 3.22.0

---

## MatterBodyRenderConfig

### MatterBodyRenderConfig

> Source: [src/physics/matter-js/typedefs/MatterBodyRenderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterBodyRenderConfig.js#L1)  
> Since: 3.22.0

---

## MatterBodyTileOptions

### MatterBodyTileOptions

> Source: [src/physics/matter-js/typedefs/MatterBodyTileOptions.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterBodyTileOptions.js#L1)  
> Since: 3.0.0

---

## MatterChamferConfig

### MatterChamferConfig

> Source: [src/physics/matter-js/typedefs/MatterChamferConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterChamferConfig.js#L1)  
> Since: 3.22.0

---

## MatterCollisionData

### MatterCollisionData

> Source: [src/physics/matter-js/typedefs/MatterCollisionData.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterCollisionData.js#L1)  
> Since: 3.22.0

---

## MatterCollisionFilter

### MatterCollisionFilter

**Description:**

An `Object` that specifies the collision filtering properties of this body.

Collisions between two bodies will obey the following rules:

* If the two bodies have the same non-zero value of `collisionFilter.group`,

  they will always collide if the value is positive, and they will never collide

  if the value is negative.
* If the two bodies have different values of `collisionFilter.group` or if one

  (or both) of the bodies has a value of 0, then the category/mask rules apply as follows:

Each body belongs to a collision category, given by `collisionFilter.category`. This

value is used as a bit field and the category should have only one bit set, meaning that

the value of this property is a power of two in the range [1, 2^31]. Thus, there are 32

different collision categories available.

Each body also defines a collision bitmask, given by `collisionFilter.mask` which specifies

the categories it collides with (the value is the bitwise AND value of all these categories).

Using the category/mask rules, two bodies `A` and `B` collide if each includes the other's

category in its mask, i.e. `(categoryA & maskB) !== 0` and `(categoryB & maskA) !== 0`

are both true.

> Source: [src/physics/matter-js/typedefs/MatterCollisionFilter.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterCollisionFilter.js#L1)  
> Since: 3.22.0

---

## MatterCollisionPair

### MatterCollisionPair

> Source: [src/physics/matter-js/typedefs/MatterCollisionPair.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterCollisionPair.js#L1)  
> Since: 3.22.0

---

## MatterConstraintConfig

### MatterConstraintConfig

> Source: [src/physics/matter-js/typedefs/MatterConstraintConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterConstraintConfig.js#L1)  
> Since: 3.22.0

---

## MatterConstraintRenderConfig

### MatterConstraintRenderConfig

> Source: [src/physics/matter-js/typedefs/MatterConstraintRenderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterConstraintRenderConfig.js#L1)  
> Since: 3.22.0

---

## MatterDebugConfig

### MatterDebugConfig

> Source: [src/physics/matter-js/typedefs/MatterDebugConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterDebugConfig.js#L1)  
> Since: 3.22.0

---

## MatterRunnerConfig

### MatterRunnerConfig

> Source: [src/physics/matter-js/typedefs/MatterRunnerConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterRunnerConfig.js#L1)  
> Since: 3.22.0

---

## MatterSetBodyConfig

### MatterSetBodyConfig

> Source: [src/physics/matter-js/typedefs/MatterSetBodyConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterSetBodyConfig.js#L1)  
> Since: 3.22.0

---

## MatterTileOptions

### MatterTileOptions

> Source: [src/physics/matter-js/typedefs/MatterTileOptions.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterTileOptions.js#L1)  
> Since: 3.0.0

---

## MatterWalls

### MatterWalls

> Source: [src/physics/matter-js/typedefs/MatterWalls.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterWalls.js#L1)  
> Since: 3.0.0

---

## MatterWorldConfig

### MatterWorldConfig

> Source: [src/physics/matter-js/typedefs/MatterWorldConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/typedefs/MatterWorldConfig.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [MatterBody](#matterbody)

    - [MatterBody](#matterbody-1)
  + [MatterBodyConfig](#matterbodyconfig)

    - [MatterBodyConfig](#matterbodyconfig-1)
  + [MatterBodyRenderConfig](#matterbodyrenderconfig)

    - [MatterBodyRenderConfig](#matterbodyrenderconfig-1)
  + [MatterBodyTileOptions](#matterbodytileoptions)

    - [MatterBodyTileOptions](#matterbodytileoptions-1)
  + [MatterChamferConfig](#matterchamferconfig)

    - [MatterChamferConfig](#matterchamferconfig-1)
  + [MatterCollisionData](#mattercollisiondata)

    - [MatterCollisionData](#mattercollisiondata-1)
  + [MatterCollisionFilter](#mattercollisionfilter)

    - [MatterCollisionFilter](#mattercollisionfilter-1)
  + [MatterCollisionPair](#mattercollisionpair)

    - [MatterCollisionPair](#mattercollisionpair-1)
  + [MatterConstraintConfig](#matterconstraintconfig)

    - [MatterConstraintConfig](#matterconstraintconfig-1)
  + [MatterConstraintRenderConfig](#matterconstraintrenderconfig)

    - [MatterConstraintRenderConfig](#matterconstraintrenderconfig-1)
  + [MatterDebugConfig](#matterdebugconfig)

    - [MatterDebugConfig](#matterdebugconfig-1)
  + [MatterRunnerConfig](#matterrunnerconfig)

    - [MatterRunnerConfig](#matterrunnerconfig-1)
  + [MatterSetBodyConfig](#mattersetbodyconfig)

    - [MatterSetBodyConfig](#mattersetbodyconfig-1)
  + [MatterTileOptions](#mattertileoptions)

    - [MatterTileOptions](#mattertileoptions-1)
  + [MatterWalls](#matterwalls)

    - [MatterWalls](#matterwalls-1)
  + [MatterWorldConfig](#matterworldconfig)

    - [MatterWorldConfig](#matterworldconfig-1)

Back to top

©2025[Phaser](https://docs.phaser.io)