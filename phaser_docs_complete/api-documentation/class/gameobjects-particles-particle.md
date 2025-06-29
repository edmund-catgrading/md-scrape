# Particle

Phaser.GameObjects.Particles.Particle

A Particle is a simple object owned and controlled by a Particle Emitter.

It encapsulates all of the properties required to move and update according

to the Emitters operations.

**Constructor**

`new Particle(emitter)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) | No | The Emitter to which this Particle belongs. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/gameobjects/particles/Particle.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L15)  
> Since: 3.0.0

# Public Members

## accelerationX

### accelerationX: number

**Description:**

The x acceleration of this Particle.

> Source: [src/gameobjects/particles/Particle.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L117)  
> Since: 3.0.0

---

## accelerationY

### accelerationY: number

**Description:**

The y acceleration of this Particle.

> Source: [src/gameobjects/particles/Particle.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L127)  
> Since: 3.0.0

---

## alpha

### alpha: number

**Description:**

The alpha value of this Particle.

> Source: [src/gameobjects/particles/Particle.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L187)  
> Since: 3.0.0

---

## angle

### angle: number

**Description:**

The angle of this Particle in degrees.

> Source: [src/gameobjects/particles/Particle.js#L197](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L197)  
> Since: 3.0.0

---

## anims

### anims: [Phaser.Animations.AnimationState](animations-animationstate.md)

**Description:**

The Animation State component of this Particle.

This component provides features to apply animations to this Particle.

It is responsible for playing, loading, queuing animations for later playback,

mixing between animations and setting the current animation frame to this Particle.

It is created only if the Particle's Emitter has at least one Animation.

> Source: [src/gameobjects/particles/Particle.js#L326](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L326)  
> Since: 3.60.0

---

## bounce

### bounce: number

**Description:**

The bounciness, or restitution, of this Particle.

> Source: [src/gameobjects/particles/Particle.js#L157](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L157)  
> Since: 3.0.0

---

## bounds

### bounds: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

A rectangle that holds the bounds of this Particle after a call to

the `Particle.getBounds` method has been made.

> Source: [src/gameobjects/particles/Particle.js#L347](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L347)  
> Since: 3.60.0

---

## data

### data: [Phaser.Types.GameObjects.Particles.ParticleData](../typedef/types-gameobjects-particles.md)

**Description:**

The data used by the ease equation.

> Source: [src/gameobjects/particles/Particle.js#L277](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L277)  
> Since: 3.0.0

---

## delayCurrent

### delayCurrent: number

**Description:**

The delay applied to this Particle upon emission, in ms.

> Source: [src/gameobjects/particles/Particle.js#L247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L247)  
> Since: 3.0.0

---

## emitter

### emitter: [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md)

**Description:**

The Emitter to which this Particle belongs.

A Particle can only belong to a single Emitter and is created, updated and destroyed by it.

> Source: [src/gameobjects/particles/Particle.js#L35](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L35)  
> Since: 3.0.0

---

## frame

### frame: [Phaser.Textures.Frame](textures-frame.md)

**Description:**

The texture frame used by this Particle when it renders.

> Source: [src/gameobjects/particles/Particle.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L56)  
> Since: 3.0.0

---

## holdCurrent

### holdCurrent: number

**Description:**

The hold applied to this Particle before it expires, in ms.

> Source: [src/gameobjects/particles/Particle.js#L257](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L257)  
> Since: 3.60.0

---

## life

### life: number

**Description:**

The lifespan of this Particle in ms.

> Source: [src/gameobjects/particles/Particle.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L227)  
> Since: 3.0.0

---

## lifeCurrent

### lifeCurrent: number

**Description:**

The current life of this Particle in ms.

> Source: [src/gameobjects/particles/Particle.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L237)  
> Since: 3.0.0

---

## lifeT

### lifeT: number

**Description:**

The normalized lifespan T value, where 0 is the start and 1 is the end.

> Source: [src/gameobjects/particles/Particle.js#L267](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L267)  
> Since: 3.0.0

---

## maxVelocityX

### maxVelocityX: number

**Description:**

The maximum horizontal velocity this Particle can travel at.

> Source: [src/gameobjects/particles/Particle.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L137)  
> Since: 3.0.0

---

## maxVelocityY

### maxVelocityY: number

**Description:**

The maximum vertical velocity this Particle can travel at.

> Source: [src/gameobjects/particles/Particle.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L147)  
> Since: 3.0.0

---

## rotation

### rotation: number

**Description:**

The angle of this Particle in radians.

> Source: [src/gameobjects/particles/Particle.js#L207](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L207)  
> Since: 3.0.0

---

## scaleX

### scaleX: number

**Description:**

The horizontal scale of this Particle.

> Source: [src/gameobjects/particles/Particle.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L167)  
> Since: 3.0.0

---

## scaleY

### scaleY: number

**Description:**

The vertical scale of this Particle.

> Source: [src/gameobjects/particles/Particle.js#L177](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L177)  
> Since: 3.0.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene to which this Game Object belongs.

Game Objects can only belong to one Scene.

You should consider this property as being read-only. You cannot move a

Game Object to another Scene by simply changing it.

> Source: [src/gameobjects/particles/Particle.js#L312](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L312)  
> Since: 3.60.0

---

## texture

### texture: [Phaser.Textures.Texture](textures-texture.md)

**Description:**

The texture used by this Particle when it renders.

> Source: [src/gameobjects/particles/Particle.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L46)  
> Since: 3.60.0

---

## tint

### tint: number

**Description:**

The tint applied to this Particle.

**Tags:**

* webglOnly

> Source: [src/gameobjects/particles/Particle.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L217)  
> Since: 3.0.0

---

## velocityX

### velocityX: number

**Description:**

The x velocity of this Particle.

> Source: [src/gameobjects/particles/Particle.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L97)  
> Since: 3.0.0

---

## velocityY

### velocityY: number

**Description:**

The y velocity of this Particle.

> Source: [src/gameobjects/particles/Particle.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L107)  
> Since: 3.0.0

---

## worldPosition

### worldPosition: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The coordinates of this Particle in world space.

Updated as part of `computeVelocity`.

> Source: [src/gameobjects/particles/Particle.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L86)  
> Since: 3.60.0

---

## x

### x: number

**Description:**

The x coordinate of this Particle.

> Source: [src/gameobjects/particles/Particle.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L66)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y coordinate of this Particle.

> Source: [src/gameobjects/particles/Particle.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L76)  
> Since: 3.0.0

---

# Private Members

## isCropped

### isCropped: boolean

**Description:**

Internal private value.

**Access:** private

> Source: [src/gameobjects/particles/Particle.js#L301](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L301)  
> Since: 3.60.0

---

# Public Methods

## computeVelocity

### <instance> computeVelocity(emitter, delta, step, processors, t)

**Description:**

An internal method that calculates the velocity of the Particle and

its world position. It also runs it against any active Processors

that are set on the Emitter.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| emitter | [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) | No | The Emitter that is updating this Particle. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms. |
| step | number | No | The delta value divided by 1000. |
| processors | Array.<[Phaser.GameObjects.Particles.ParticleProcessor](gameobjects-particles-particleprocessor.md)> | No | An array of all active Particle Processors. |
| t | number | No | The current normalized lifetime of the particle, between 0 (birth) and 1 (death). |

> Source: [src/gameobjects/particles/Particle.js#L668](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L668)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this Particle.

> Source: [src/gameobjects/particles/Particle.js#L789](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L789)  
> Since: 3.60.0

---

## emit

### <instance> emit(event, [a1], [a2], [a3], [a4], [a5])

**Description:**

The Event Emitter proxy.

Passes on all parameters to the `ParticleEmitter` to emit directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | Symbol | No | The event name. |
| --- | --- | --- | --- |
| a1 | any | Yes | Optional argument 1. |
| a2 | any | Yes | Optional argument 2. |
| a3 | any | Yes | Optional argument 3. |
| a4 | any | Yes | Optional argument 4. |
| a5 | any | Yes | Optional argument 5. |

**Returns:** boolean - `true` if the event had listeners, else `false`.

> Source: [src/gameobjects/particles/Particle.js#L358](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L358)  
> Since: 3.60.0

---

## fire

### <instance> fire([x], [y])

**Description:**

Starts this Particle from the given coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | Yes | The x coordinate to launch this Particle from. |
| --- | --- | --- | --- |
| y | number | Yes | The y coordinate to launch this Particle from. |

**Returns:** boolean - `true` if the Particle is alive, or `false` if it was spawned inside a DeathZone.

> Source: [src/gameobjects/particles/Particle.js#L425](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L425)  
> Since: 3.0.0

---

## getBounds

### <instance> getBounds([matrix])

**Description:**

Gets the bounds of this particle as a Geometry Rectangle, factoring in any

transforms of the parent emitter and anything else above it in the display list.

Once calculated the bounds can be accessed via the `Particle.bounds` property.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| matrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | Optional transform matrix to apply to this particle. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - A Rectangle containing the transformed bounds of this particle.

> Source: [src/gameobjects/particles/Particle.js#L735](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L735)  
> Since: 3.60.0

---

## isAlive

### <instance> isAlive()

**Description:**

Checks to see if this Particle is alive and updating.

**Returns:** boolean - `true` if this Particle is alive and updating, otherwise `false`.

> Source: [src/gameobjects/particles/Particle.js#L380](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L380)  
> Since: 3.0.0

---

## kill

### <instance> kill()

**Description:**

Kills this particle. This sets the `lifeCurrent` value to 0, which forces

the Particle to be removed the next time its parent Emitter runs an update.

> Source: [src/gameobjects/particles/Particle.js#L393](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L393)  
> Since: 3.60.0

---

## setPosition

### <instance> setPosition([x], [y])

**Description:**

Sets the position of this particle to the given x/y coordinates.

If the parameters are left undefined, it resets the particle back to 0x0.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x coordinate to set this Particle to. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y coordinate to set this Particle to. |

> Source: [src/gameobjects/particles/Particle.js#L405](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L405)  
> Since: 3.60.0

---

## setSizeToFrame

### <instance> setSizeToFrame()

**Description:**

This is a NOOP method and does nothing when called.

> Source: [src/gameobjects/particles/Particle.js#L724](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L724)  
> Since: 3.60.0

---

## update

### <instance> update(delta, step, processors)

**Description:**

The main update method for this Particle.

Updates its life values, computes the velocity and repositions the Particle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms. |
| --- | --- | --- | --- |
| step | number | No | The delta value divided by 1000. |
| processors | Array.<[Phaser.GameObjects.Particles.ParticleProcessor](gameobjects-particles-particleprocessor.md)> | No | An array of all active Particle Processors. |

**Returns:** boolean - Returns `true` if this Particle has now expired and should be removed, otherwise `false` if still active.

> Source: [src/gameobjects/particles/Particle.js#L563](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/Particle.js#L563)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [accelerationX](#accelerationx)

    - [accelerationX: number](#accelerationx-number)
  + [accelerationY](#accelerationy)

    - [accelerationY: number](#accelerationy-number)
  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [angle](#angle)

    - [angle: number](#angle-number)
  + [anims](#anims)

    - [anims: Phaser.Animations.AnimationState](#anims-phaseranimationsanimationstate)
  + [bounce](#bounce)

    - [bounce: number](#bounce-number)
  + [bounds](#bounds)

    - [bounds: Phaser.Geom.Rectangle](#bounds-phasergeomrectangle)
  + [data](#data)

    - [data: Phaser.Types.GameObjects.Particles.ParticleData](#data-phasertypesgameobjectsparticlesparticledata)
  + [delayCurrent](#delaycurrent)

    - [delayCurrent: number](#delaycurrent-number)
  + [emitter](#emitter)

    - [emitter: Phaser.GameObjects.Particles.ParticleEmitter](#emitter-phasergameobjectsparticlesparticleemitter)
  + [frame](#frame)

    - [frame: Phaser.Textures.Frame](#frame-phasertexturesframe)
  + [holdCurrent](#holdcurrent)

    - [holdCurrent: number](#holdcurrent-number)
  + [life](#life)

    - [life: number](#life-number)
  + [lifeCurrent](#lifecurrent)

    - [lifeCurrent: number](#lifecurrent-number)
  + [lifeT](#lifet)

    - [lifeT: number](#lifet-number)
  + [maxVelocityX](#maxvelocityx)

    - [maxVelocityX: number](#maxvelocityx-number)
  + [maxVelocityY](#maxvelocityy)

    - [maxVelocityY: number](#maxvelocityy-number)
  + [rotation](#rotation)

    - [rotation: number](#rotation-number)
  + [scaleX](#scalex)

    - [scaleX: number](#scalex-number)
  + [scaleY](#scaley)

    - [scaleY: number](#scaley-number)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [texture](#texture)

    - [texture: Phaser.Textures.Texture](#texture-phasertexturestexture)
  + [tint](#tint)

    - [tint: number](#tint-number)
  + [velocityX](#velocityx)

    - [velocityX: number](#velocityx-number)
  + [velocityY](#velocityy)

    - [velocityY: number](#velocityy-number)
  + [worldPosition](#worldposition)

    - [worldPosition: Phaser.Math.Vector2](#worldposition-phasermathvector2)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Private Members](#private-members)

  + [isCropped](#iscropped)

    - [isCropped: boolean](#iscropped-boolean)
* [Public Methods](#public-methods)

  + [computeVelocity](#computevelocity)

    - [<instance> computeVelocity(emitter, delta, step, processors, t)](#instance-computevelocityemitter-delta-step-processors-t)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [a1], [a2], [a3], [a4], [a5])](#instance-emitevent-a1-a2-a3-a4-a5)
  + [fire](#fire)

    - [<instance> fire([x], [y])](#instance-firex-y)
  + [getBounds](#getbounds)

    - [<instance> getBounds([matrix])](#instance-getboundsmatrix)
  + [isAlive](#isalive)

    - [<instance> isAlive()](#instance-isalive)
  + [kill](#kill)

    - [<instance> kill()](#instance-kill)
  + [setPosition](#setposition)

    - [<instance> setPosition([x], [y])](#instance-setpositionx-y)
  + [setSizeToFrame](#setsizetoframe)

    - [<instance> setSizeToFrame()](#instance-setsizetoframe)
  + [update](#update)

    - [<instance> update(delta, step, processors)](#instance-updatedelta-step-processors)

Back to top

©2025[Phaser](https://docs.phaser.io)