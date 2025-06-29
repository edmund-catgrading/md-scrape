# EmitterOp

Phaser.GameObjects.Particles.EmitterOp

This class is responsible for taking control over a single property

in the Particle class and managing its emission and updating functions.

Particles properties such as `x`, `y`, `scaleX`, `lifespan` and others all use

EmitterOp instances to manage them, as they can be given in a variety of

formats: from simple values, to functions, to dynamic callbacks.

See the `ParticleEmitter` class for more details on emitter op configuration.

**Constructor**

`new EmitterOp(key, defaultValue, [emitOnly])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The name of the property. |
| --- | --- | --- | --- | --- |
| defaultValue | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md) | [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](../typedef/types-gameobjects-particles.md) | No |  | The default value of the property. |
| emitOnly | boolean | Yes | false | Whether the property can only be modified when a Particle is emitted. |

---

**Scope**: static

> Source: [src/gameobjects/particles/EmitterOp.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L17)  
> Since: 3.0.0

# Public Members

## active

### active: boolean

**Description:**

Set to `false` to disable this EmitterOp.

> Source: [src/gameobjects/particles/EmitterOp.js#L203](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L203)  
> Since: 3.60.0

---

## counter

### counter: number

**Description:**

The step counter for stepped easing, per emit.

> Source: [src/gameobjects/particles/EmitterOp.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L89)  
> Since: 3.0.0

---

## current

### current: number

**Description:**

The most recently calculated value. Updated every time an

emission or update method is called. Treat as read-only.

> Source: [src/gameobjects/particles/EmitterOp.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L132)  
> Since: 3.60.0

---

## defaultValue

### defaultValue: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md), [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](../typedef/types-gameobjects-particles.md)

**Description:**

The default value of this property.

This can be a simple value, an array, a function or an onEmit

configuration object.

> Source: [src/gameobjects/particles/EmitterOp.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L66)  
> Since: 3.0.0

---

## direction

### direction: number

**Description:**

The counter direction. 0 for up and 1 for down.

> Source: [src/gameobjects/particles/EmitterOp.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L110)  
> Since: 3.60.0

---

## ease

### ease: function

**Description:**

The easing function to use for updating this property, if any.

> Source: [src/gameobjects/particles/EmitterOp.js#L152](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L152)  
> Since: 3.0.0

---

## emitOnly

### emitOnly: boolean

**Description:**

Whether this property can only be modified when a Particle is emitted.

Set to `true` to allow only [Phaser.GameObjects.Particles.EmitterOp#onEmit](gameobjects-particles-emitterop.md) callbacks to be set and

affect this property.

Set to `false` to allow both [Phaser.GameObjects.Particles.EmitterOp#onEmit](gameobjects-particles-emitterop.md) and

[Phaser.GameObjects.Particles.EmitterOp#onUpdate](gameobjects-particles-emitterop.md) callbacks to be set and affect this property.

> Source: [src/gameobjects/particles/EmitterOp.js#L170](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L170)  
> Since: 3.0.0

---

## end

### end: number

**Description:**

The end value for this property to ease between.

> Source: [src/gameobjects/particles/EmitterOp.js#L142](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L142)  
> Since: 3.0.0

---

## interpolation

### interpolation: function

**Description:**

The interpolation function to use for updating this property, if any.

> Source: [src/gameobjects/particles/EmitterOp.js#L161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L161)  
> Since: 3.60.0

---

## method

### method: number

**Description:**

The onEmit method type of this EmitterOp.

Set as part of `setMethod` and cached here to avoid

re-setting when only the value changes.

> Source: [src/gameobjects/particles/EmitterOp.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L212)  
> Since: 3.60.0

---

## onEmit

### onEmit: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitCallback](../typedef/types-gameobjects-particles.md)

**Description:**

The callback to run for Particles when they are emitted from the Particle Emitter.

> Source: [src/gameobjects/particles/EmitterOp.js#L185](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L185)  
> Since: 3.0.0

---

## onUpdate

### onUpdate: [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateCallback](../typedef/types-gameobjects-particles.md)

**Description:**

The callback to run for Particles when they are updated.

> Source: [src/gameobjects/particles/EmitterOp.js#L194](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L194)  
> Since: 3.0.0

---

## propertyKey

### propertyKey: string

**Description:**

The name of this property.

> Source: [src/gameobjects/particles/EmitterOp.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L45)  
> Since: 3.0.0

---

## propertyValue

### propertyValue: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md), [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](../typedef/types-gameobjects-particles.md)

**Description:**

The current value of this property.

This can be a simple value, an array, a function or an onEmit

configuration object.

> Source: [src/gameobjects/particles/EmitterOp.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L54)  
> Since: 3.0.0

---

## start

### start: number, Array.<number>

**Description:**

The start value for this property to ease between.

If an interpolation this holds a reference to the number data array.

> Source: [src/gameobjects/particles/EmitterOp.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L120)  
> Since: 3.0.0

---

## steps

### steps: number

**Description:**

The number of steps for stepped easing between [Phaser.GameObjects.Particles.EmitterOp#start](gameobjects-particles-emitterop.md) and

[Phaser.GameObjects.Particles.EmitterOp#end](gameobjects-particles-emitterop.md) values, per emit.

> Source: [src/gameobjects/particles/EmitterOp.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L78)  
> Since: 3.0.0

---

## yoyo

### yoyo: boolean

**Description:**

When the step counter reaches it's maximum, should it then

yoyo back to the start again, or flip over to it?

> Source: [src/gameobjects/particles/EmitterOp.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L99)  
> Since: 3.60.0

---

# Private Members

## \_onEmit

### \_onEmit: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitCallback](../typedef/types-gameobjects-particles.md)

**Description:**

The callback to run for Particles when they are emitted from the Particle Emitter.

This is set during `setMethods` and used by `proxyEmit`.

**Access:** private

> Source: [src/gameobjects/particles/EmitterOp.js#L224](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L224)  
> Since: 3.60.0

---

## \_onUpdate

### \_onUpdate: [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateCallback](../typedef/types-gameobjects-particles.md)

**Description:**

The callback to run for Particles when they are updated.

This is set during `setMethods` and used by `proxyUpdate`.

**Access:** private

> Source: [src/gameobjects/particles/EmitterOp.js#L235](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L235)  
> Since: 3.60.0

---

# Public Methods

## defaultEmit

### <instance> defaultEmit(particle, key, [value])

**Description:**

The returned value sets what the property will be at the START of the particles life, on emit.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle. |
| --- | --- | --- | --- |
| key | string | No | The name of the property. |
| value | number | Yes | The current value of the property. |

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L596](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L596)  
> Since: 3.0.0

---

## defaultUpdate

### <instance> defaultUpdate(particle, key, t, value)

**Description:**

The returned value updates the property for the duration of the particles life.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle. |
| --- | --- | --- | --- |
| key | string | No | The name of the property. |
| t | number | No | The current normalized lifetime of the particle, between 0 (birth) and 1 (death). |
| value | number | No | The current value of the property. |

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L613](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L613)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this EmitterOp instance and all of its references.

Called automatically when the ParticleEmitter that owns this

EmitterOp is destroyed.

> Source: [src/gameobjects/particles/EmitterOp.js#L901](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L901)  
> Since: 3.60.0

---

## easedValueEmit

### <instance> easedValueEmit(particle, key)

**Description:**

An `onEmit` callback for an eased property.

It prepares the particle for easing by [Phaser.GameObjects.Particles.EmitterOp#easeValueUpdate](gameobjects-particles-emitterop.md).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle. |
| --- | --- | --- | --- |
| key | string | No | The name of the property. |

**Returns:** number - {@link Phaser.GameObjects.Particles.EmitterOp#start}, as the new value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L838](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L838)  
> Since: 3.0.0

---

## easeValueUpdate

### <instance> easeValueUpdate(particle, key, t)

**Description:**

An `onUpdate` callback that returns an eased value between the

[Phaser.GameObjects.Particles.EmitterOp#start](gameobjects-particles-emitterop.md) and [Phaser.GameObjects.Particles.EmitterOp#end](gameobjects-particles-emitterop.md)

range.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle. |
| --- | --- | --- | --- |
| key | string | No | The name of the property. |
| t | number | No | The current normalized lifetime of the particle, between 0 (birth) and 1 (death). |

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L866](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L866)  
> Since: 3.0.0

---

## getMethod

### <instance> getMethod()

**Description:**

Checks the type of `EmitterOp.propertyValue` to determine which

method is required in order to return values from this op function.

**Returns:** number - A number between 0 and 9 which should be passed to `setMethods`.

> Source: [src/gameobjects/particles/EmitterOp.js#L360](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L360)  
> Since: 3.60.0

---

## has

### <instance> has(object, key)

**Description:**

Check whether an object has the given property.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object | object | No | The object to check. |
| --- | --- | --- | --- |
| key | string | No | The key of the property to look for in the object. |

**Returns:** boolean - `true` if the property exists in the object, `false` otherwise.

> Source: [src/gameobjects/particles/EmitterOp.js#L546](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L546)  
> Since: 3.0.0

---

## hasBoth

### <instance> hasBoth(object, key1, key2)

**Description:**

Check whether an object has both of the given properties.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object | object | No | The object to check. |
| --- | --- | --- | --- |
| key1 | string | No | The key of the first property to check the object for. |
| key2 | string | No | The key of the second property to check the object for. |

**Returns:** boolean - `true` if both properties exist in the object, `false` otherwise.

> Source: [src/gameobjects/particles/EmitterOp.js#L562](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L562)  
> Since: 3.0.0

---

## hasEither

### <instance> hasEither(object, key1, key2)

**Description:**

Check whether an object has at least one of the given properties.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object | object | No | The object to check. |
| --- | --- | --- | --- |
| key1 | string | No | The key of the first property to check the object for. |
| key2 | string | No | The key of the second property to check the object for. |

**Returns:** boolean - `true` if at least one of the properties exists in the object, `false` if neither exist.

> Source: [src/gameobjects/particles/EmitterOp.js#L579](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L579)  
> Since: 3.0.0

---

## loadConfig

### <instance> loadConfig([config], [newKey])

**Description:**

Load the property from a Particle Emitter configuration object.

Optionally accepts a new property key to use, replacing the current one.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](../typedef/types-gameobjects-particles.md) | Yes | Settings for the Particle Emitter that owns this property. |
| --- | --- | --- | --- |
| newKey | string | Yes | The new key to use for this property, if any. |

> Source: [src/gameobjects/particles/EmitterOp.js#L247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L247)  
> Since: 3.0.0

---

## onChange

### <instance> onChange(value)

**Description:**

Change the current value of the property and update its callback methods.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The new numeric value of this property. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.EmitterOp](gameobjects-particles-emitterop.md) - This Emitter Op object.

> Source: [src/gameobjects/particles/EmitterOp.js#L300](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L300)  
> Since: 3.0.0

---

## proxyEmit

### <instance> proxyEmit(particle, key, [value])

**Description:**

The returned value sets what the property will be at the START of the particles life, on emit.

This method is only used when you have provided a custom emit callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle. |
| --- | --- | --- | --- |
| key | string | No | The name of the property. |
| value | number | Yes | The current value of the property. |

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L631](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L631)  
> Since: 3.60.0

---

## proxyUpdate

### <instance> proxyUpdate(particle, key, t, value)

**Description:**

The returned value updates the property for the duration of the particles life.

This method is only used when you have provided a custom update callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle. |
| --- | --- | --- | --- |
| key | string | No | The name of the property. |
| t | number | No | The current normalized lifetime of the particle, between 0 (birth) and 1 (death). |
| value | number | No | The current value of the property. |

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L654](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L654)  
> Since: 3.60.0

---

## randomRangedIntEmit

### <instance> randomRangedIntEmit(particle, key)

**Description:**

An `onEmit` callback that returns a value between the [Phaser.GameObjects.Particles.EmitterOp#start](gameobjects-particles-emitterop.md) and

[Phaser.GameObjects.Particles.EmitterOp#end](gameobjects-particles-emitterop.md) range.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle. |
| --- | --- | --- | --- |
| key | string | No | The key of the property. |

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L748](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L748)  
> Since: 3.60.0

---

## randomRangedValueEmit

### <instance> randomRangedValueEmit(particle, key)

**Description:**

An `onEmit` callback that returns a value between the [Phaser.GameObjects.Particles.EmitterOp#start](gameobjects-particles-emitterop.md) and

[Phaser.GameObjects.Particles.EmitterOp#end](gameobjects-particles-emitterop.md) range.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle. |
| --- | --- | --- | --- |
| key | string | No | The key of the property. |

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L721](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L721)  
> Since: 3.0.0

---

## randomStaticValueEmit

### <instance> randomStaticValueEmit()

**Description:**

An `onEmit` callback that returns a random value from the current value array.

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L704](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L704)  
> Since: 3.0.0

---

## setMethods

### <instance> setMethods()

**Description:**

Update the [Phaser.GameObjects.Particles.EmitterOp#onEmit](gameobjects-particles-emitterop.md) and

[Phaser.GameObjects.Particles.EmitterOp#onUpdate](gameobjects-particles-emitterop.md) callbacks based on the method returned

from `getMethod`. The method is stored in the `EmitterOp.method` property

and is a number between 0 and 9 inclusively.

**Returns:** [Phaser.GameObjects.Particles.EmitterOp](gameobjects-particles-emitterop.md) - This Emitter Op object.

> Source: [src/gameobjects/particles/EmitterOp.js#L436](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L436)  
> Since: 3.0.0

---

## staticValueEmit

### <instance> staticValueEmit()

**Description:**

An `onEmit` callback that returns the current value of the property.

**Returns:** number - The current value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L678](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L678)  
> Since: 3.0.0

---

## staticValueUpdate

### <instance> staticValueUpdate()

**Description:**

An `onUpdate` callback that returns the current value of the property.

**Returns:** number - The current value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L691](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L691)  
> Since: 3.0.0

---

## steppedEmit

### <instance> steppedEmit()

**Description:**

An `onEmit` callback that returns a stepped value between the

[Phaser.GameObjects.Particles.EmitterOp#start](gameobjects-particles-emitterop.md) and [Phaser.GameObjects.Particles.EmitterOp#end](gameobjects-particles-emitterop.md)

range.

**Returns:** number - The new value of the property.

> Source: [src/gameobjects/particles/EmitterOp.js#L775](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L775)  
> Since: 3.0.0

---

## toJSON

### <instance> toJSON()

**Description:**

Build a JSON representation of this Particle Emitter property.

**Returns:** object - A JSON representation of this Particle Emitter property.

> Source: [src/gameobjects/particles/EmitterOp.js#L287](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/EmitterOp.js#L287)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [counter](#counter)

    - [counter: number](#counter-number)
  + [current](#current)

    - [current: number](#current-number)
  + [defaultValue](#defaultvalue)

    - [defaultValue: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType, Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](#defaultvalue-phasertypesgameobjectsparticlesemitteroponemittype-phasertypesgameobjectsparticlesemitteroponupdatetype)
  + [direction](#direction)

    - [direction: number](#direction-number)
  + [ease](#ease)

    - [ease: function](#ease-function)
  + [emitOnly](#emitonly)

    - [emitOnly: boolean](#emitonly-boolean)
  + [end](#end)

    - [end: number](#end-number)
  + [interpolation](#interpolation)

    - [interpolation: function](#interpolation-function)
  + [method](#method)

    - [method: number](#method-number)
  + [onEmit](#onemit)

    - [onEmit: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitCallback](#onemit-phasertypesgameobjectsparticlesemitteroponemitcallback)
  + [onUpdate](#onupdate)

    - [onUpdate: Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateCallback](#onupdate-phasertypesgameobjectsparticlesemitteroponupdatecallback)
  + [propertyKey](#propertykey)

    - [propertyKey: string](#propertykey-string)
  + [propertyValue](#propertyvalue)

    - [propertyValue: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType, Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](#propertyvalue-phasertypesgameobjectsparticlesemitteroponemittype-phasertypesgameobjectsparticlesemitteroponupdatetype)
  + [start](#start)

    - [start: number, Array.<number>](#start-number-arraynumber)
  + [steps](#steps)

    - [steps: number](#steps-number)
  + [yoyo](#yoyo)

    - [yoyo: boolean](#yoyo-boolean)
* [Private Members](#private-members)

  + [\_onEmit](#_onemit)

    - [\_onEmit: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitCallback](#_onemit-phasertypesgameobjectsparticlesemitteroponemitcallback)
  + [\_onUpdate](#_onupdate)

    - [\_onUpdate: Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateCallback](#_onupdate-phasertypesgameobjectsparticlesemitteroponupdatecallback)
* [Public Methods](#public-methods)

  + [defaultEmit](#defaultemit)

    - [<instance> defaultEmit(particle, key, [value])](#instance-defaultemitparticle-key-value)
  + [defaultUpdate](#defaultupdate)

    - [<instance> defaultUpdate(particle, key, t, value)](#instance-defaultupdateparticle-key-t-value)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [easedValueEmit](#easedvalueemit)

    - [<instance> easedValueEmit(particle, key)](#instance-easedvalueemitparticle-key)
  + [easeValueUpdate](#easevalueupdate)

    - [<instance> easeValueUpdate(particle, key, t)](#instance-easevalueupdateparticle-key-t)
  + [getMethod](#getmethod)

    - [<instance> getMethod()](#instance-getmethod)
  + [has](#has)

    - [<instance> has(object, key)](#instance-hasobject-key)
  + [hasBoth](#hasboth)

    - [<instance> hasBoth(object, key1, key2)](#instance-hasbothobject-key1-key2)
  + [hasEither](#haseither)

    - [<instance> hasEither(object, key1, key2)](#instance-haseitherobject-key1-key2)
  + [loadConfig](#loadconfig)

    - [<instance> loadConfig([config], [newKey])](#instance-loadconfigconfig-newkey)
  + [onChange](#onchange)

    - [<instance> onChange(value)](#instance-onchangevalue)
  + [proxyEmit](#proxyemit)

    - [<instance> proxyEmit(particle, key, [value])](#instance-proxyemitparticle-key-value)
  + [proxyUpdate](#proxyupdate)

    - [<instance> proxyUpdate(particle, key, t, value)](#instance-proxyupdateparticle-key-t-value)
  + [randomRangedIntEmit](#randomrangedintemit)

    - [<instance> randomRangedIntEmit(particle, key)](#instance-randomrangedintemitparticle-key)
  + [randomRangedValueEmit](#randomrangedvalueemit)

    - [<instance> randomRangedValueEmit(particle, key)](#instance-randomrangedvalueemitparticle-key)
  + [randomStaticValueEmit](#randomstaticvalueemit)

    - [<instance> randomStaticValueEmit()](#instance-randomstaticvalueemit)
  + [setMethods](#setmethods)

    - [<instance> setMethods()](#instance-setmethods)
  + [staticValueEmit](#staticvalueemit)

    - [<instance> staticValueEmit()](#instance-staticvalueemit)
  + [staticValueUpdate](#staticvalueupdate)

    - [<instance> staticValueUpdate()](#instance-staticvalueupdate)
  + [steppedEmit](#steppedemit)

    - [<instance> steppedEmit()](#instance-steppedemit)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)

Back to top

©2025[Phaser](https://docs.phaser.io)



EmitterOp