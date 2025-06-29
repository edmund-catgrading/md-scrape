# RandomZone

Phaser.GameObjects.Particles.Zones.RandomZone

A zone that places particles randomly within a shapes area.

**Constructor**

`new RandomZone(source)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Types.GameObjects.Particles.RandomZoneSource](../typedef/types-gameobjects-particles.md) | No | An object instance with a `getRandomPoint(point)` method. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/gameobjects/particles/zones/RandomZone.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/RandomZone.js#L10)  
> Since: 3.0.0

# Public Members

## source

### source: [Phaser.Types.GameObjects.Particles.RandomZoneSource](../typedef/types-gameobjects-particles.md)

**Description:**

An object instance with a `getRandomPoint(point)` method.

> Source: [src/gameobjects/particles/zones/RandomZone.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/RandomZone.js#L27)  
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

> Source: [src/gameobjects/particles/zones/RandomZone.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/RandomZone.js#L46)  
> Since: 3.60.0

---

# Private Members

## \_tempVec

### \_tempVec: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

Internal calculation vector.

**Access:** private

> Source: [src/gameobjects/particles/zones/RandomZone.js#L36](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/RandomZone.js#L36)  
> Since: 3.0.0

---

# Public Methods

## getPoint

### <instance> getPoint(particle)

**Description:**

Get the next point in the Zone and set its coordinates on the given Particle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The Particle. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/particles/zones/RandomZone.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/RandomZone.js#L65)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [source](#source)

    - [source: Phaser.Types.GameObjects.Particles.RandomZoneSource](#source-phasertypesgameobjectsparticlesrandomzonesource)
  + [total](#total)

    - [total: number](#total-number)
* [Private Members](#private-members)

  + [\_tempVec](#_tempvec)

    - [\_tempVec: Phaser.Math.Vector2](#_tempvec-phasermathvector2)
* [Public Methods](#public-methods)

  + [getPoint](#getpoint)

    - [<instance> getPoint(particle)](#instance-getpointparticle)

Back to top

©2025[Phaser](https://docs.phaser.io)



RandomZone