# DeathZone

Phaser.GameObjects.Particles.Zones.DeathZone

A Death Zone.

A Death Zone is a special type of zone that will kill a Particle as soon as it either enters, or leaves, the zone.

The zone consists of a `source` which could be a Geometric shape, such as a Rectangle or Ellipse, or your own

object as long as it includes a `contains` method for which the Particles can be tested against.

**Constructor**

`new DeathZone(source, killOnEnter)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Types.GameObjects.Particles.DeathZoneSource](../typedef/types-gameobjects-particles.md) | No | An object instance that has a `contains` method that returns a boolean when given `x` and `y` arguments. |
| --- | --- | --- | --- |
| killOnEnter | boolean | No | Should the Particle be killed when it enters the zone? `true` or leaves it? `false` |

---

**Scope**: static

> Source: [src/gameobjects/particles/zones/DeathZone.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/DeathZone.js#L9)  
> Since: 3.0.0

# Public Members

## killOnEnter

### killOnEnter: boolean

**Description:**

Set to `true` if the Particle should be killed if it enters this zone.

Set to `false` to kill the Particle if it leaves this zone.

> Source: [src/gameobjects/particles/zones/DeathZone.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/DeathZone.js#L42)  
> Since: 3.0.0

---

## source

### source: [Phaser.Types.GameObjects.Particles.DeathZoneSource](../typedef/types-gameobjects-particles.md)

**Description:**

An object instance that has a `contains` method that returns a boolean when given `x` and `y` arguments.

This could be a Geometry shape, such as `Phaser.Geom.Circle`, or your own custom object.

> Source: [src/gameobjects/particles/zones/DeathZone.js#L32](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/DeathZone.js#L32)  
> Since: 3.0.0

---

# Public Methods

## willKill

### <instance> willKill(particle)

**Description:**

Checks if the given Particle will be killed or not by this zone.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle to test against this Death Zones. |
| --- | --- | --- | --- |

**Returns:** boolean - Return `true` if the Particle is to be killed, otherwise return `false`.

> Source: [src/gameobjects/particles/zones/DeathZone.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/zones/DeathZone.js#L53)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [killOnEnter](#killonenter)

    - [killOnEnter: boolean](#killonenter-boolean)
  + [source](#source)

    - [source: Phaser.Types.GameObjects.Particles.DeathZoneSource](#source-phasertypesgameobjectsparticlesdeathzonesource)
* [Public Methods](#public-methods)

  + [willKill](#willkill)

    - [<instance> willKill(particle)](#instance-willkillparticle)

Back to top

©2025[Phaser](https://docs.phaser.io)