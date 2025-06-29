# Phaser.GameObjects.Particles.Events

Scope:
static

> Source: [src/gameobjects/particles/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/events/index.js#L7)

# Static functions

## COMPLETE

### COMPLETE

**Description:**

The Particle Emitter Complete Event.

This event is dispatched when the final particle, emitted from a Particle Emitter that

has been stopped, dies. Upon receipt of this event you know that no particles are

still rendering at this point in time.

Listen for it on a Particle Emitter instance using `ParticleEmitter.on('complete', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](../class/gameobjects-particles-particleemitter.md) | No | A reference to the Particle Emitter that just completed. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/particles/events/COMPLETE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/events/COMPLETE_EVENT.js#L7)  
> Since: 3.60.0

---

## DEATH\_ZONE

### DEATH\_ZONE

**Description:**

The Particle Emitter Death Zone Event.

This event is dispatched when a Death Zone kills a Particle instance.

Listen for it on a Particle Emitter instance using `ParticleEmitter.on('deathzone', listener)`.

If you wish to know when the final particle is killed, see the `COMPLETE` event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](../class/gameobjects-particles-particleemitter.md) | No | A reference to the Particle Emitter that owns the Particle and Death Zone. |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](../class/gameobjects-particles-particle.md) | No | The Particle that has been killed. |
| zone | [Phaser.GameObjects.Particles.Zones.DeathZone](../class/gameobjects-particles-zones-deathzone.md) | No | The Death Zone that killed the particle. |

> Source: [src/gameobjects/particles/events/DEATH\_ZONE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/events/DEATH_ZONE_EVENT.js#L7)  
> Since: 3.60.0

---

## EXPLODE

### EXPLODE

**Description:**

The Particle Emitter Explode Event.

This event is dispatched when a Particle Emitter explodes a set of particles.

Listen for it on a Particle Emitter instance using `ParticleEmitter.on('explode', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](../class/gameobjects-particles-particleemitter.md) | No | A reference to the Particle Emitter that just completed. |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](../class/gameobjects-particles-particle.md) | No | The most recently emitted Particle. |

> Source: [src/gameobjects/particles/events/EXPLODE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/events/EXPLODE_EVENT.js#L7)  
> Since: 3.60.0

---

## START

### START

**Description:**

The Particle Emitter Start Event.

This event is dispatched when a Particle Emitter starts emission of particles.

Listen for it on a Particle Emitter instance using `ParticleEmitter.on('start', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](../class/gameobjects-particles-particleemitter.md) | No | A reference to the Particle Emitter that just completed. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/particles/events/START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/events/START_EVENT.js#L7)  
> Since: 3.60.0

---

## STOP

### STOP

**Description:**

The Particle Emitter Stop Event.

This event is dispatched when a Particle Emitter is stopped. This can happen either

when you directly call the `ParticleEmitter.stop` method, or if the emitter has

been configured to stop after a set time via the `duration` property, or after a

set number of particles via the `stopAfter` property.

Listen for it on a Particle Emitter instance using `ParticleEmitter.on('stop', listener)`.

Note that just because the emitter has stopped, that doesn't mean there aren't still

particles alive and rendering. It just means the emitter has stopped emitting particles.

If you wish to know when the final particle is killed, see the `COMPLETE` event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](../class/gameobjects-particles-particleemitter.md) | No | A reference to the Particle Emitter that just completed. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/particles/events/STOP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/events/STOP_EVENT.js#L7)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [COMPLETE](#complete)

    - [COMPLETE](#complete-1)
  + [DEATH\_ZONE](#death_zone)

    - [DEATH\_ZONE](#death_zone-1)
  + [EXPLODE](#explode)

    - [EXPLODE](#explode-1)
  + [START](#start)

    - [START](#start-1)
  + [STOP](#stop)

    - [STOP](#stop-1)

Back to top

©2025[Phaser](https://docs.phaser.io)