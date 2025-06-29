# ParticleBounds

Phaser.GameObjects.Particles.ParticleBounds

The Particle Bounds Processor.

Defines a rectangular region, in world space, within which particle movement

is restrained.

Use the properties `collideLeft`, `collideRight`, `collideTop` and

`collideBottom` to control if a particle will rebound off the sides

of this boundary, or not.

This happens when the particles worldPosition x/y coordinate hits the boundary.

The strength of the rebound is determined by the `Particle.bounce` property.

**Constructor**

`new ParticleBounds(x, y, width, height, [collideLeft], [collideRight], [collideTop], [collideBottom])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x position (top-left) of the bounds, in world space. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y position (top-left) of the bounds, in world space. |
| width | number | No |  | The width of the bounds. |
| height | number | No |  | The height of the bounds. |
| collideLeft | boolean | Yes | true | Whether particles interact with the left edge of the bounds. |
| collideRight | boolean | Yes | true | Whether particles interact with the right edge of the bounds. |
| collideTop | boolean | Yes | true | Whether particles interact with the top edge of the bounds. |
| collideBottom | boolean | Yes | true | Whether particles interact with the bottom edge of the bounds. |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.Particles.ParticleProcessor](gameobjects-particles-particleprocessor.md)

> Source: [src/gameobjects/particles/ParticleBounds.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleBounds.js#L11)  
> Since: 3.60.0

# Public Members

## active

### active: boolean

**Description:**

The active state of the Particle Processor.

An inactive Particle Processor will be skipped for processing by

its parent Emitter.

**Inherits:** [Phaser.GameObjects.Particles.ParticleProcessor#active](gameobjects-particles-particleprocessor.md)

> Source: [src/gameobjects/particles/ParticleProcessor.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleProcessor.js#L66)  
> Since: 3.60.0

---

## bounds

### bounds: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

A rectangular boundary constraining particle movement. Use the Emitter properties `collideLeft`,

`collideRight`, `collideTop` and `collideBottom` to control if a particle will rebound off

the sides of this boundary, or not. This happens when the particles x/y coordinate hits

the boundary.

> Source: [src/gameobjects/particles/ParticleBounds.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleBounds.js#L56)  
> Since: 3.60.0

---

## collideBottom

### collideBottom: boolean

**Description:**

Whether particles interact with the bottom edge of the emitter [Phaser.GameObjects.Particles.ParticleBounds#bounds](gameobjects-particles-particlebounds.md).

> Source: [src/gameobjects/particles/ParticleBounds.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleBounds.js#L98)  
> Since: 3.60.0

---

## collideLeft

### collideLeft: boolean

**Description:**

Whether particles interact with the left edge of the emitter [Phaser.GameObjects.Particles.ParticleEmitter#bounds](gameobjects-particles-particleemitter.md).

> Source: [src/gameobjects/particles/ParticleBounds.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleBounds.js#L68)  
> Since: 3.60.0

---

## collideRight

### collideRight: boolean

**Description:**

Whether particles interact with the right edge of the emitter [Phaser.GameObjects.Particles.ParticleBounds#bounds](gameobjects-particles-particlebounds.md).

> Source: [src/gameobjects/particles/ParticleBounds.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleBounds.js#L78)  
> Since: 3.60.0

---

## collideTop

### collideTop: boolean

**Description:**

Whether particles interact with the top edge of the emitter [Phaser.GameObjects.Particles.ParticleBounds#bounds](gameobjects-particles-particlebounds.md).

> Source: [src/gameobjects/particles/ParticleBounds.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleBounds.js#L88)  
> Since: 3.60.0

---

## manager

### manager: [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md)

**Description:**

A reference to the Particle Emitter that owns this Processor.

This is set automatically when the Processor is added to an Emitter

and nulled when removed or destroyed.

**Inherits:** [Phaser.GameObjects.Particles.ParticleProcessor#manager](gameobjects-particles-particleprocessor.md)

> Source: [src/gameobjects/particles/ParticleProcessor.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleProcessor.js#L37)  
> Since: 3.60.0

---

## x

### x: number

**Description:**

The x coordinate of the Particle Processor, in world space.

**Inherits:** [Phaser.GameObjects.Particles.ParticleProcessor#x](gameobjects-particles-particleprocessor.md)

> Source: [src/gameobjects/particles/ParticleProcessor.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleProcessor.js#L48)  
> Since: 3.60.0

---

## y

### y: number

**Description:**

The y coordinate of the Particle Processor, in world space.

**Inherits:** [Phaser.GameObjects.Particles.ParticleProcessor#y](gameobjects-particles-particleprocessor.md)

> Source: [src/gameobjects/particles/ParticleProcessor.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleProcessor.js#L57)  
> Since: 3.60.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this Particle Processor by removing all external references.

This is called automatically when the owning Particle Emitter is destroyed.

**Inherits:** [Phaser.GameObjects.Particles.ParticleProcessor#destroy](gameobjects-particles-particleprocessor.md)

> Source: [src/gameobjects/particles/ParticleProcessor.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleProcessor.js#L96)  
> Since: 3.60.0

---

## update

### <instance> update(particle)

**Description:**

Takes a Particle and updates it against the bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The Particle to update. |
| --- | --- | --- | --- |

**Overrides:** Phaser.GameObjects.Particles.ParticleProcessor#update

> Source: [src/gameobjects/particles/ParticleBounds.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleBounds.js#L109)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [bounds](#bounds)

    - [bounds: Phaser.Geom.Rectangle](#bounds-phasergeomrectangle)
  + [collideBottom](#collidebottom)

    - [collideBottom: boolean](#collidebottom-boolean)
  + [collideLeft](#collideleft)

    - [collideLeft: boolean](#collideleft-boolean)
  + [collideRight](#collideright)

    - [collideRight: boolean](#collideright-boolean)
  + [collideTop](#collidetop)

    - [collideTop: boolean](#collidetop-boolean)
  + [manager](#manager)

    - [manager: Phaser.GameObjects.Particles.ParticleEmitter](#manager-phasergameobjectsparticlesparticleemitter)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [update](#update)

    - [<instance> update(particle)](#instance-updateparticle)

Back to top

©2025[Phaser](https://docs.phaser.io)



ParticleBounds