# EdgeZone

Phaser.GameObjects.Particles.Zones.EdgeZone

A zone that places particles on a shape's edges.

**Constructor**

`new EdgeZone(source, quantity, [stepRate], [yoyo], [seamless], [total])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| source | [Phaser.Types.GameObjects.Particles.EdgeZoneSource](../typedef/types-gameobjects-particles.md) | No |  | An object instance with a `getPoints(quantity, stepRate)` method returning an array of points. |
| --- | --- | --- | --- | --- |
| quantity | number | No |  | The number of particles to place on the source edge. Set to 0 to use `stepRate` instead. |
| stepRate | number | Yes |  | The distance between each particle. When set, `quantity` is implied and should be set to 0. |
| yoyo | boolean | Yes | false | Whether particles are placed from start to end and then end to start. |
| seamless | boolean | Yes | true | Whether one endpoint will be removed if it's identical to the other. |
| total | number | Yes | -1 | The total number of particles this zone will emit before passing over to the next emission zone in the Emitter. -1 means it will never pass over and you must use `setEmitZone` to change it. |

---

**Scope**: static

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L9)  
> Since: 3.0.0

# Public Members

## counter

### counter: number

**Description:**

The counter used for iterating the EdgeZone's points.

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L81)  
> Since: 3.0.0

---

## points

### points: Array.<[Phaser.Geom.Point](geom-point.md)>

**Description:**

The points placed on the source edge.

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L44)  
> Since: 3.0.0

---

## quantity

### quantity: number

**Description:**

The number of particles to place on the source edge. Set to 0 to use `stepRate` instead.

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L54)  
> Since: 3.0.0

---

## seamless

### seamless: boolean

**Description:**

Whether one endpoint will be removed if it's identical to the other.

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L91)  
> Since: 3.0.0

---

## source

### source: [Phaser.Types.GameObjects.Particles.EdgeZoneSource](../typedef/types-gameobjects-particles.md), [Phaser.Types.GameObjects.Particles.RandomZoneSource](../typedef/types-gameobjects-particles.md)

**Description:**

An object instance with a `getPoints(quantity, stepRate)` method returning an array of points.

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L35](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L35)  
> Since: 3.0.0

---

## stepRate

### stepRate: number

**Description:**

The distance between each particle. When set, `quantity` is implied and should be set to 0.

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L63)  
> Since: 3.0.0

---

## total

### total: number

**Description:**

The total number of particles this zone will emit before the Emitter

transfers control over to the next zone in its emission zone list.

By default this is -1, meaning it will never pass over from this

zone to another one. You can call the `ParticleEmitter.setEmitZone`

method to change it, or set this value to something else via the

config, or directly at runtime.

A value of 1 would mean the zones rotate in order, but it can

be set to any integer value.

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L124)  
> Since: 3.60.0

---

## yoyo

### yoyo: boolean

**Description:**

Whether particles are placed from start to end and then end to start.

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L72)  
> Since: 3.0.0

---

# Private Members

## \_direction

### \_direction: number

**Description:**

An internal value used to keep track of the current iteration direction for the EdgeZone's points.

0 = forwards, 1 = backwards

**Access:** private

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L111)  
> Since: 3.0.0

---

## \_length

### \_length: number

**Description:**

An internal count of the points belonging to this EdgeZone.

**Access:** private

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L100)  
> Since: 3.0.0

---

# Public Methods

## changeSource

### <instance> changeSource(source)

**Description:**

Change the source of the EdgeZone.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Types.GameObjects.Particles.EdgeZoneSource](../typedef/types-gameobjects-particles.md) | No | An object instance with a `getPoints(quantity, stepRate)` method returning an array of points. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.Zones.EdgeZone](gameobjects-particles-zones-edgezone.md) - This Edge Zone.

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L185](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L185)  
> Since: 3.0.0

---

## getPoint

### <instance> getPoint(particle)

**Description:**

Get the next point in the Zone and set its coordinates on the given Particle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The Particle. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L202)  
> Since: 3.0.0

---

## updateSource

### <instance> updateSource()

**Description:**

Update the [Phaser.GameObjects.Particles.Zones.EdgeZone#points](gameobjects-particles-zones-edgezone.md) from the EdgeZone's

[Phaser.GameObjects.Particles.Zones.EdgeZone#source](gameobjects-particles-zones-edgezone.md).

Also updates internal properties.

**Returns:** [Phaser.GameObjects.Particles.Zones.EdgeZone](gameobjects-particles-zones-edgezone.md) - This Edge Zone.

> Source: [src/gameobjects/particles/zones/EdgeZone.js#L145](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/EdgeZone.js#L145)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [counter](#counter)

    - [counter: number](#counter-number)
  + [points](#points)

    - [points: Array.<Phaser.Geom.Point>](#points-arrayphasergeompoint)
  + [quantity](#quantity)

    - [quantity: number](#quantity-number)
  + [seamless](#seamless)

    - [seamless: boolean](#seamless-boolean)
  + [source](#source)

    - [source: Phaser.Types.GameObjects.Particles.EdgeZoneSource, Phaser.Types.GameObjects.Particles.RandomZoneSource](#source-phasertypesgameobjectsparticlesedgezonesource-phasertypesgameobjectsparticlesrandomzonesource)
  + [stepRate](#steprate)

    - [stepRate: number](#steprate-number)
  + [total](#total)

    - [total: number](#total-number)
  + [yoyo](#yoyo)

    - [yoyo: boolean](#yoyo-boolean)
* [Private Members](#private-members)

  + [\_direction](#_direction)

    - [\_direction: number](#_direction-number)
  + [\_length](#_length)

    - [\_length: number](#_length-number)
* [Public Methods](#public-methods)

  + [changeSource](#changesource)

    - [<instance> changeSource(source)](#instance-changesourcesource)
  + [getPoint](#getpoint)

    - [<instance> getPoint(particle)](#instance-getpointparticle)
  + [updateSource](#updatesource)

    - [<instance> updateSource()](#instance-updatesource)

Back to top

©2025[Phaser](https://docs.phaser.io)



EdgeZone