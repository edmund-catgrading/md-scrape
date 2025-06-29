# Phaser.Types.GameObjects.Particles

Scope:
static

> Source: [src/gameobjects/particles/typedefs/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/index.js#L7)

# Static functions

## DeathZoneObject

### DeathZoneObject

> Source: [src/gameobjects/particles/typedefs/DeathZoneObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/DeathZoneObject.js#L1)  
> Since: 3.60.0

---

## DeathZoneSource

### DeathZoneSource

> Source: [src/gameobjects/particles/typedefs/DeathZoneSource.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/DeathZoneSource.js#L1)  
> Since: 3.0.0

---

## DeathZoneSourceCallback

### DeathZoneSourceCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the particle to check against this source area. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the particle to check against this source area. |

**Returns:** boolean - - True if the coordinates are within the source area.

> Source: [src/gameobjects/particles/typedefs/DeathZoneSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/DeathZoneSourceCallback.js#L1)  
> Since: 3.0.0

---

## EdgeZoneSource

### EdgeZoneSource

> Source: [src/gameobjects/particles/typedefs/EdgeZoneSource.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EdgeZoneSource.js#L1)  
> Since: 3.0.0

---

## EdgeZoneSourceCallback

### EdgeZoneSourceCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| quantity | number | No | The number of particles to place on the source edge. If 0, `stepRate` should be used instead. |
| --- | --- | --- | --- |
| stepRate | number | Yes | The distance between each particle. When set, `quantity` is implied and should be set to `0`. |

**Returns:** Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> - - The points placed on the source edge.

> Source: [src/gameobjects/particles/typedefs/EdgeZoneSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EdgeZoneSourceCallback.js#L1)  
> Since: 3.0.0

---

## EmitterOpCustomEmitConfig

### EmitterOpCustomEmitConfig

> Source: [src/gameobjects/particles/typedefs/EmitterOpCustomEmitConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpCustomEmitConfig.js#L1)  
> Since: 3.0.0

---

## EmitterOpCustomUpdateConfig

### EmitterOpCustomUpdateConfig

> Source: [src/gameobjects/particles/typedefs/EmitterOpCustomUpdateConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpCustomUpdateConfig.js#L1)  
> Since: 3.0.0

---

## EmitterOpEaseConfig

### EmitterOpEaseConfig

**Description:**

Defines an operation yielding a value incremented continuously across a range.

> Source: [src/gameobjects/particles/typedefs/EmitterOpEaseConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpEaseConfig.js#L1)  
> Since: 3.0.0

---

## EmitterOpInterpolationConfig

### EmitterOpInterpolationConfig

**Description:**

Defines an operation yielding a value incremented continuously across an interpolated data set.

> Source: [src/gameobjects/particles/typedefs/EmitterOpInterpolationConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpInterpolationConfig.js#L1)  
> Since: 3.60.0

---

## EmitterOpOnEmitCallback

### EmitterOpOnEmitCallback

**Description:**

The returned value sets what the property will be at the START of the particle's life, on emit.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](../class/gameobjects-particles-particle.md) | Yes | The particle. |
| --- | --- | --- | --- |
| key | string | Yes | The name of the property. |
| value | number | Yes | The current value of the property. |

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/typedefs/EmitterOpOnEmitCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpOnEmitCallback.js#L1)  
> Since: 3.0.0

---

## EmitterOpOnEmitType

### EmitterOpOnEmitType

> Source: [src/gameobjects/particles/typedefs/EmitterOpOnEmitType.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpOnEmitType.js#L1)  
> Since: 3.18.0

---

## EmitterOpOnUpdateCallback

### EmitterOpOnUpdateCallback

**Description:**

The returned value updates the property for the duration of the particle's life.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](../class/gameobjects-particles-particle.md) | No | The particle. |
| --- | --- | --- | --- |
| key | string | No | The name of the property. |
| t | number | No | The normalized lifetime of the particle, between 0 (start) and 1 (end). |
| value | number | No | The current value of the property. |

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/typedefs/EmitterOpOnUpdateCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpOnUpdateCallback.js#L1)  
> Since: 3.0.0

---

## EmitterOpOnUpdateType

### EmitterOpOnUpdateType

> Source: [src/gameobjects/particles/typedefs/EmitterOpOnUpdateType.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpOnUpdateType.js#L1)  
> Since: 3.18.0

---

## EmitterOpRandomConfig

### EmitterOpRandomConfig

**Description:**

Defines an operation yielding a random value within a range.

> Source: [src/gameobjects/particles/typedefs/EmitterOpRandomConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpRandomConfig.js#L1)  
> Since: 3.0.0

---

## EmitterOpRandomMinMaxConfig

### EmitterOpRandomMinMaxConfig

**Description:**

Defines an operation yielding a random value within a range.

> Source: [src/gameobjects/particles/typedefs/EmitterOpRandomMinMaxConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpRandomMinMaxConfig.js#L1)  
> Since: 3.0.0

---

## EmitterOpSteppedConfig

### EmitterOpSteppedConfig

**Description:**

Defines an operation yielding a value incremented by steps across a range.

> Source: [src/gameobjects/particles/typedefs/EmitterOpSteppedConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitterOpSteppedConfig.js#L1)  
> Since: 3.0.0

---

## EmitZoneData

### EmitZoneData

> Source: [src/gameobjects/particles/typedefs/EmitZoneData.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitZoneData.js#L1)  
> Since: 3.60.0

---

## EmitZoneObject

### EmitZoneObject

> Source: [src/gameobjects/particles/typedefs/EmitZoneObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/EmitZoneObject.js#L1)  
> Since: 3.60.0

---

## GravityWellConfig

### GravityWellConfig

> Source: [src/gameobjects/particles/typedefs/GravityWellConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/GravityWellConfig.js#L1)  
> Since: 3.0.0

---

## ParticleClassConstructor

### ParticleClassConstructor

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](../class/gameobjects-particles-particleemitter.md) | No | The Emitter to which this Particle belongs. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/particles/typedefs/ParticleClassConstructor.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleClassConstructor.js#L1)  
> Since: 3.0.0

---

## ParticleData

### ParticleData

> Source: [src/gameobjects/particles/typedefs/ParticleData.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleData.js#L1)  
> Since: 3.60.0

---

## ParticleDataValue

### ParticleDataValue

> Source: [src/gameobjects/particles/typedefs/ParticleDataValue.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleDataValue.js#L1)  
> Since: 3.60.0

---

## ParticleDeathCallback

### ParticleDeathCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](../class/gameobjects-particles-particle.md) | No | The particle that died. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/particles/typedefs/ParticleDeathCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleDeathCallback.js#L1)  
> Since: 3.0.0

---

## ParticleEmitterAnimConfig

### ParticleEmitterAnimConfig

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterAnimConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterAnimConfig.js#L1)  
> Since: 3.60.0

---

## ParticleEmitterBounds

### ParticleEmitterBounds

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterBounds.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterBounds.js#L1)  
> Since: 3.0.0

---

## ParticleEmitterBoundsAlt

### ParticleEmitterBoundsAlt

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterBoundsAlt.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterBoundsAlt.js#L1)  
> Since: 3.0.0

---

## ParticleEmitterCallback

### ParticleEmitterCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](../class/gameobjects-particles-particle.md) | No | The particle associated with the call. |
| --- | --- | --- | --- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](../class/gameobjects-particles-particleemitter.md) | No | This particle emitter associated with the call. |

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterCallback.js#L1)  
> Since: 3.0.0

---

## ParticleEmitterConfig

### ParticleEmitterConfig

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterConfig.js#L1)  
> Since: 3.0.0

---

## ParticleEmitterCreatorConfig

### ParticleEmitterCreatorConfig

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterCreatorConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterCreatorConfig.js#L1)  
> Since: 3.60.0

---

## ParticleEmitterDeathZoneConfig

### ParticleEmitterDeathZoneConfig

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterDeathZoneConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterDeathZoneConfig.js#L1)  
> Since: 3.0.0

---

## ParticleEmitterEdgeZoneConfig

### ParticleEmitterEdgeZoneConfig

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterEdgeZoneConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterEdgeZoneConfig.js#L1)  
> Since: 3.0.0

---

## ParticleEmitterFrameConfig

### ParticleEmitterFrameConfig

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterFrameConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterFrameConfig.js#L1)  
> Since: 3.0.0

---

## ParticleEmitterOps

### ParticleEmitterOps

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterOps.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterOps.js#L1)  
> Since: 3.60.0

---

## ParticleEmitterRandomZoneConfig

### ParticleEmitterRandomZoneConfig

> Source: [src/gameobjects/particles/typedefs/ParticleEmitterRandomZoneConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleEmitterRandomZoneConfig.js#L1)  
> Since: 3.0.0

---

## ParticleSortCallback

### ParticleSortCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.GameObjects.Particles.Particle](../class/gameobjects-particles-particle.md) | No | The first Particle being compared. |
| --- | --- | --- | --- |
| b | [Phaser.GameObjects.Particles.Particle](../class/gameobjects-particles-particle.md) | No | The second Particle being compared. |

> Source: [src/gameobjects/particles/typedefs/ParticleSortCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/ParticleSortCallback.js#L1)  
> Since: 3.60.0

---

## RandomZoneSource

### RandomZoneSource

> Source: [src/gameobjects/particles/typedefs/RandomZoneSource.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/RandomZoneSource.js#L1)  
> Since: 3.0.0

---

## RandomZoneSourceCallback

### RandomZoneSourceCallback

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | A point to modify. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/particles/typedefs/RandomZoneSourceCallback.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/typedefs/RandomZoneSourceCallback.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [DeathZoneObject](#deathzoneobject)

    - [DeathZoneObject](#deathzoneobject-1)
  + [DeathZoneSource](#deathzonesource)

    - [DeathZoneSource](#deathzonesource-1)
  + [DeathZoneSourceCallback](#deathzonesourcecallback)

    - [DeathZoneSourceCallback](#deathzonesourcecallback-1)
  + [EdgeZoneSource](#edgezonesource)

    - [EdgeZoneSource](#edgezonesource-1)
  + [EdgeZoneSourceCallback](#edgezonesourcecallback)

    - [EdgeZoneSourceCallback](#edgezonesourcecallback-1)
  + [EmitterOpCustomEmitConfig](#emitteropcustomemitconfig)

    - [EmitterOpCustomEmitConfig](#emitteropcustomemitconfig-1)
  + [EmitterOpCustomUpdateConfig](#emitteropcustomupdateconfig)

    - [EmitterOpCustomUpdateConfig](#emitteropcustomupdateconfig-1)
  + [EmitterOpEaseConfig](#emitteropeaseconfig)

    - [EmitterOpEaseConfig](#emitteropeaseconfig-1)
  + [EmitterOpInterpolationConfig](#emitteropinterpolationconfig)

    - [EmitterOpInterpolationConfig](#emitteropinterpolationconfig-1)
  + [EmitterOpOnEmitCallback](#emitteroponemitcallback)

    - [EmitterOpOnEmitCallback](#emitteroponemitcallback-1)
  + [EmitterOpOnEmitType](#emitteroponemittype)

    - [EmitterOpOnEmitType](#emitteroponemittype-1)
  + [EmitterOpOnUpdateCallback](#emitteroponupdatecallback)

    - [EmitterOpOnUpdateCallback](#emitteroponupdatecallback-1)
  + [EmitterOpOnUpdateType](#emitteroponupdatetype)

    - [EmitterOpOnUpdateType](#emitteroponupdatetype-1)
  + [EmitterOpRandomConfig](#emitteroprandomconfig)

    - [EmitterOpRandomConfig](#emitteroprandomconfig-1)
  + [EmitterOpRandomMinMaxConfig](#emitteroprandomminmaxconfig)

    - [EmitterOpRandomMinMaxConfig](#emitteroprandomminmaxconfig-1)
  + [EmitterOpSteppedConfig](#emitteropsteppedconfig)

    - [EmitterOpSteppedConfig](#emitteropsteppedconfig-1)
  + [EmitZoneData](#emitzonedata)

    - [EmitZoneData](#emitzonedata-1)
  + [EmitZoneObject](#emitzoneobject)

    - [EmitZoneObject](#emitzoneobject-1)
  + [GravityWellConfig](#gravitywellconfig)

    - [GravityWellConfig](#gravitywellconfig-1)
  + [ParticleClassConstructor](#particleclassconstructor)

    - [ParticleClassConstructor](#particleclassconstructor-1)
  + [ParticleData](#particledata)

    - [ParticleData](#particledata-1)
  + [ParticleDataValue](#particledatavalue)

    - [ParticleDataValue](#particledatavalue-1)
  + [ParticleDeathCallback](#particledeathcallback)

    - [ParticleDeathCallback](#particledeathcallback-1)
  + [ParticleEmitterAnimConfig](#particleemitteranimconfig)

    - [ParticleEmitterAnimConfig](#particleemitteranimconfig-1)
  + [ParticleEmitterBounds](#particleemitterbounds)

    - [ParticleEmitterBounds](#particleemitterbounds-1)
  + [ParticleEmitterBoundsAlt](#particleemitterboundsalt)

    - [ParticleEmitterBoundsAlt](#particleemitterboundsalt-1)
  + [ParticleEmitterCallback](#particleemittercallback)

    - [ParticleEmitterCallback](#particleemittercallback-1)
  + [ParticleEmitterConfig](#particleemitterconfig)

    - [ParticleEmitterConfig](#particleemitterconfig-1)
  + [ParticleEmitterCreatorConfig](#particleemittercreatorconfig)

    - [ParticleEmitterCreatorConfig](#particleemittercreatorconfig-1)
  + [ParticleEmitterDeathZoneConfig](#particleemitterdeathzoneconfig)

    - [ParticleEmitterDeathZoneConfig](#particleemitterdeathzoneconfig-1)
  + [ParticleEmitterEdgeZoneConfig](#particleemitteredgezoneconfig)

    - [ParticleEmitterEdgeZoneConfig](#particleemitteredgezoneconfig-1)
  + [ParticleEmitterFrameConfig](#particleemitterframeconfig)

    - [ParticleEmitterFrameConfig](#particleemitterframeconfig-1)
  + [ParticleEmitterOps](#particleemitterops)

    - [ParticleEmitterOps](#particleemitterops-1)
  + [ParticleEmitterRandomZoneConfig](#particleemitterrandomzoneconfig)

    - [ParticleEmitterRandomZoneConfig](#particleemitterrandomzoneconfig-1)
  + [ParticleSortCallback](#particlesortcallback)

    - [ParticleSortCallback](#particlesortcallback-1)
  + [RandomZoneSource](#randomzonesource)

    - [RandomZoneSource](#randomzonesource-1)
  + [RandomZoneSourceCallback](#randomzonesourcecallback)

    - [RandomZoneSourceCallback](#randomzonesourcecallback-1)

Back to top

©2025[Phaser](https://docs.phaser.io)