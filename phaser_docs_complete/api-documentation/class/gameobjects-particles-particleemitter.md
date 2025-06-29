# ParticleEmitter

Phaser.GameObjects.Particles.ParticleEmitter

A Particle Emitter is a special kind of Game Object that controls a pool of [Particles](Phaser.GameObjects.Particles.Particle.md).

Particle Emitters are created via a configuration object. The properties of this object

can be specified in a variety of formats, given you plenty of scope over the values they

return, leading to complex visual effects. Here are the different forms of configuration

value you can give:

## An explicit static value:

```
Copy
x: 400


```

The x value will always be 400 when the particle is spawned.

## A random value:

```
Copy
x: [ 100, 200, 300, 400 ]


```

The x value will be one of the 4 elements in the given array, picked at random on emission.

## A custom callback:

```
Copy
x: (particle, key, t, value) => {

  return value + 50;

}


```

The x value is the result of calling this function. This is only used when the

particle is emitted, so it provides it's initial starting value. It is not used

when the particle is updated (see the onUpdate callback for that)

## A start / end object:

This allows you to control the change in value between the given start and

end parameters over the course of the particles lifetime:

```
Copy
scale: { start: 0, end: 1 }


```

The particle scale will start at 0 when emitted and ease to a scale of 1

over the course of its lifetime. You can also specify the ease function

used for this change (the default is Linear):

```
Copy
scale: { start: 0, end: 1, ease: 'bounce.out' }


```

## A start / end random object:

The start and end object can have an optional `random` parameter.

This forces it to pick a random value between the two values and use

this as the starting value, then easing to the 'end' parameter over

its lifetime.

```
Copy
scale: { start: 4, end: 0.5, random: true }


```

The particle will start with a random scale between 0.5 and 4 and then

scale to the end value over its lifetime. You can combine the above

with the `ease` parameter as well to control the value easing.

## An interpolation object:

You can provide an array of values which will be used for interpolation

during the particles lifetime. You can also define the interpolation

function to be used. There are three provided: `linear` (the default),

`bezier` and `catmull`, or you can provide your own function.

```
Copy
x: { values: [ 50, 500, 200, 800 ], interpolation: 'catmull' }


```

The particle scale will interpolate from 50 when emitted to 800 via the other

points over the course of its lifetime. You can also specify an ease function

used to control the rate of change through the values (the default is Linear):

```
Copy
x: { values: [ 50, 500, 200, 800 ], interpolation: 'catmull', ease: 'bounce.out }


```

## A stepped emitter object:

The `steps` parameter allows you to control the placement of sequential

particles across the start-end range:

```
Copy
x: { steps: 32, start: 0, end: 576 }


```

Here we have a range of 576 (start to end). This is divided into 32 steps.

The first particle will emit at the x position of 0. The next will emit

at the next 'step' along, which would be 18. The following particle will emit

at the next step, which is 36, and so on. Because the range of 576 has been

divided by 32, creating 18 pixels steps. When a particle reaches the 'end'

value the next one will start from the beginning again.

## A stepped emitter object with yoyo:

You can add the optional `yoyo` property to a stepped object:

```
Copy
x: { steps: 32, start: 0, end: 576, yoyo: true }


```

As with the stepped emitter, particles are emitted in sequence, from 'start'

to 'end' in step sized jumps. Normally, when a stepped emitter reaches the

end it snaps around to the start value again. However, if you provide the 'yoyo'

parameter then when it reaches the end it will reverse direction and start

emitting back down to 'start' again. Depending on the effect you require this

can often look better.

## A min / max object:

This allows you to pick a random float value between the min and max properties:

```
Copy
x: { min: 100, max: 700 }


```

The x value will be a random float between min and max.

You can force it select an integer by setting the 'int' flag:

```
Copy
x: { min: 100, max: 700, int: true }


```

Or, you could use the 'random' array approach (see below)

## A random object:

This allows you to pick a random integer value between the first and second array elements:

```
Copy
x: { random: [ 100, 700 ] }


```

The x value will be a random integer between 100 and 700 as it takes the first

element in the 'random' array as the 'min' value and the 2nd element as the 'max' value.

## Custom onEmit and onUpdate callbacks:

If the above won't give you the effect you're after, you can provide your own

callbacks that will be used when the particle is both emitted and updated:

```
Copy
x: {

  onEmit: (particle, key, t, value) => {

    return value;

  },

  onUpdate: (particle, key, t, value) => {

    return value;

  }

}


```

You can provide either one or both functions. The `onEmit` is called at the

start of the particles life and defines the value of the property on birth.

The `onUpdate` function is called every time the Particle Emitter updates

until the particle dies. Both must return a value.

The properties are:

particle - A reference to the Particle instance.

key - The string based key of the property, i.e. 'x' or 'lifespan'.

t - The current normalized lifetime of the particle, between 0 (birth) and 1 (death).

value - The current property value. At a minimum you should return this.

By using the above configuration options you have an unlimited about of

control over how your particles behave.

## v3.55 Differences

Prior to v3.60 Phaser used a `ParticleEmitterManager`. This was removed in v3.60

and now calling `this.add.particles` returns a `ParticleEmitter` instance instead.

In order to streamline memory and the display list we have removed the

`ParticleEmitterManager` entirely. When you call `this.add.particles` you're now

creating a `ParticleEmitter` instance, which is being added directly to the

display list and can be manipulated just like any other Game Object, i.e.

scaled, rotated, positioned, added to a Container, etc. It now extends the

`GameObject` base class, meaning it's also an event emitter, which allowed us

to create some handy new events for particles.

So, to create an emitter, you now give it an xy coordinate, a texture and an

emitter configuration object (you can also set this later, but most commonly

you'd do it on creation). I.e.:

```
Copy
const emitter = this.add.particles(100, 300, 'flares', {

  frame: 'red',

  angle: { min: -30, max: 30 },

  speed: 150

});


```

This will create a 'red flare' emitter at 100 x 300.

Please update your code to ensure it adheres to the new function signatures.

**Constructor**

`new ParticleEmitter(scene, [x], [y], [texture], [config])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to which this Game Object belongs. A Game Object can only belong to one Scene at a time. |
| --- | --- | --- | --- |
| x | number | Yes | The horizontal position of this Game Object in the world. |
| y | number | Yes | The vertical position of this Game Object in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | Yes | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](../typedef/types-gameobjects-particles.md) | Yes | Settings for this emitter. |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)  
> [Phaser.GameObjects.Components.AlphaSingle](../namespace/gameobjects-components-alphasingle.md)  
> [Phaser.GameObjects.Components.BlendMode](../namespace/gameobjects-components-blendmode.md)  
> [Phaser.GameObjects.Components.Depth](../namespace/gameobjects-components-depth.md)  
> [Phaser.GameObjects.Components.Mask](../namespace/gameobjects-components-mask.md)  
> [Phaser.GameObjects.Components.Pipeline](../namespace/gameobjects-components-pipeline.md)  
> [Phaser.GameObjects.Components.PostPipeline](../namespace/gameobjects-components-postpipeline.md)  
> [Phaser.GameObjects.Components.ScrollFactor](../namespace/gameobjects-components-scrollfactor.md)  
> [Phaser.GameObjects.Components.Texture](../namespace/gameobjects-components-texture.md)  
> [Phaser.GameObjects.Components.Transform](../namespace/gameobjects-components-transform.md)  
> [Phaser.GameObjects.Components.Visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/particles/ParticleEmitter.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L104)  
> Since: 3.60.0

# Public Members

## acceleration

### acceleration: boolean

**Description:**

Whether accelerationX and accelerationY are non-zero. Set automatically during configuration.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L458](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L458)  
> Since: 3.0.0

---

## accelerationX

### accelerationX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The horizontal acceleration applied to emitted particles, in pixels per second squared.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3096](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3096)  
> Since: 3.60.0

---

## accelerationY

### accelerationY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The vertical acceleration applied to emitted particles, in pixels per second squared.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3120)  
> Since: 3.60.0

---

## active

### active: boolean

**Description:**

The active state of this Game Object.

A Game Object with an active state of `true` is processed by the Scenes UpdateList, if added to it.

An active object is one which is having its logic and internal systems updated.

**Inherits:** [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L113)  
> Since: 3.0.0

---

## alpha

### alpha: number

**Description:**

The alpha value of the Game Object.

This is a global value, impacting the entire Game Object, not just a region of it.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#alpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L68)  
> Since: 3.0.0

---

## angle

### angle: number

**Description:**

The angle of this Game Object as expressed in degrees.

Phaser uses a right-hand clockwise rotation system, where 0 is right, 90 is down, 180/-180 is left

and -90 is up.

If you prefer to work in radians, see the `rotation` property instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#angle](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L211](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L211)  
> Since: 3.0.0

---

## animCounter

### animCounter: number

**Description:**

The internal animation counter.

Treat this property as read-only.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3738](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3738)  
> Since: 3.60.0

---

## animQuantity

### animQuantity: number

**Description:**

The number of consecutive particles that receive a single animation (per frame cycle).

> Source: [src/gameobjects/particles/ParticleEmitter.js#L784](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L784)  
> Since: 3.60.0

---

## anims

### anims: Array.<string>

**Description:**

The animations assigned to particles.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L764](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L764)  
> Since: 3.60.0

---

## blendMode

### blendMode: [Phaser.BlendModes](../namespace/blendmodes.md), string, number

**Description:**

Sets the Blend Mode being used by this Game Object.

This can be a const, such as `Phaser.BlendModes.SCREEN`, or an integer, such as 4 (for Overlay)

Under WebGL only the following Blend Modes are available:

* NORMAL
* ADD
* MULTIPLY
* SCREEN
* ERASE

Canvas has more available depending on browser support.

You can also create your own custom Blend Modes in WebGL.

Blend modes have different effects under Canvas and WebGL, and from browser to browser, depending

on support. Blend Modes also cause a WebGL batch flush should it encounter a new blend mode. For these

reasons try to be careful about the construction of your Scene and the frequency of which blend modes

are used.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#blendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L30)  
> Since: 3.0.0

---

## body

### body: [Phaser.Physics.Arcade.Body](physics-arcade-body.md), [Phaser.Physics.Arcade.StaticBody](physics-arcade-staticbody.md), MatterJS.BodyType

**Description:**

If this Game Object is enabled for Arcade or Matter Physics then this property will contain a reference to a Physics Body.

**Inherits:** [Phaser.GameObjects.GameObject#body](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L186)  
> Since: 3.0.0

---

## bounce

### bounce: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The amount of velocity particles will use when rebounding off the

emitter bounds, if set. A value of 0 means no bounce. A value of 1

means a full rebound.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3320](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3320)  
> Since: 3.60.0

---

## cameraFilter

### cameraFilter: number

**Description:**

A bitmask that controls if this Game Object is drawn by a Camera or not.

Not usually set directly, instead call `Camera.ignore`, however you can

set this property directly using the Camera.id property:

**Inherits:** [Phaser.GameObjects.GameObject#cameraFilter](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L160)  
> Since: 3.0.0

---

## colorEase

### colorEase: string

**Description:**

Controls the easing function used when you have created an

Emitter that uses the `color` property to interpolate the

tint of Particles over their lifetime.

Setting this has no effect if you haven't also applied a

`particleColor` to this Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3437](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3437)  
> Since: 3.60.0

---

## completeFlag

### completeFlag: boolean

**Description:**

The internal complete flag.

Treat this property as read-only.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3807](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3807)  
> Since: 3.60.0

---

## config

### config: [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](../typedef/types-gameobjects-particles.md)

**Description:**

An internal object holding the configuration for the Emitter.

These are populated as part of the Emitter configuration parsing.

You typically do not access them directly, but instead use the

`ParticleEmitter.setConfig` or `ParticleEmitter.updateConfig` methods.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L372](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L372)  
> Since: 3.85.0

---

## currentAnim

### currentAnim: number

**Description:**

The current animation index.

Treat this property as read-only.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3899](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3899)  
> Since: 3.60.0

---

## currentFrame

### currentFrame: number

**Description:**

The current frame index.

Treat this property as read-only.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3876](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3876)  
> Since: 3.60.0

---

## data

### data: [Phaser.Data.DataManager](data-datamanager.md)

**Description:**

A Data Manager.

It allows you to store, query and get key/value paired information specific to this Game Object.

`null` by default. Automatically created if you use `getData` or `setData` or `setDataEnabled`.

**Inherits:** [Phaser.GameObjects.GameObject#data](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L136)  
> Since: 3.0.0

---

## deathCallback

### deathCallback: [Phaser.Types.GameObjects.Particles.ParticleDeathCallback](../typedef/types-gameobjects-particles.md)

**Description:**

A function to call when a particle dies.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L501)  
> Since: 3.0.0

---

## deathCallbackScope

### deathCallbackScope: \*

**Description:**

The calling context for [Phaser.GameObjects.Particles.ParticleEmitter#deathCallback](gameobjects-particles-particleemitter.md).

> Source: [src/gameobjects/particles/ParticleEmitter.js#L511](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L511)  
> Since: 3.0.0

---

## deathZones

### deathZones: Array.<[Phaser.GameObjects.Particles.Zones.DeathZone](gameobjects-particles-zones-deathzone.md)>

**Description:**

An array containing Particle Death Zone objects. A particle is immediately killed as soon as its x/y coordinates

intersect with any of the configured Death Zones.

Prior to Phaser v3.60 an Emitter could only have one single Death Zone.

In 3.60 they can now have an array of Death Zones.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L660](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L660)  
> Since: 3.60.0

---

## defaultPipeline

### defaultPipeline: [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

**Description:**

The initial WebGL pipeline of this Game Object.

If you call `resetPipeline` on this Game Object, the pipeline is reset to this default.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Pipeline#defaultPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L19)  
> Since: 3.0.0

---

## delay

### delay: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The number of milliseconds to wait after emission before

the particles start updating. This allows you to emit particles

that appear 'static' or still on-screen and then, after this value,

begin to move.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3635](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3635)  
> Since: 3.60.0

---

## depth

### depth: number

**Description:**

The depth of this Game Object within the Scene. Ensure this value is only ever set to a number data-type.

The depth is also known as the 'z-index' in some environments, and allows you to change the rendering order

of Game Objects, without actually moving their position in the display list.

The default depth is zero. A Game Object with a higher depth

value will always render in front of one with a lower value.

Setting the depth will queue a depth sort event within the Scene.

**Inherits:** [Phaser.GameObjects.Components.Depth#depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L30)  
> Since: 3.0.0

---

## displayList

### displayList: [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md), [Phaser.GameObjects.Layer](gameobjects-layer.md)

**Description:**

Holds a reference to the Display List that contains this Game Object.

This is set automatically when this Game Object is added to a Scene or Layer.

You should treat this property as being read-only.

**Inherits:** [Phaser.GameObjects.GameObject#displayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L53)  
> Since: 3.50.0

---

## duration

### duration: number

**Description:**

The number of milliseconds this emitter will emit particles for when in flow mode,

before it stops emission. A value of 0 (the default) means there is no duration.

When the duration expires the `STOP` event is emitted. Note that entering a

stopped state doesn't mean all the particles have finished, just that it's

not emitting any further ones.

To know when the final particle expires, listen for the COMPLETE event.

The counter is reset each time the `ParticleEmitter.start` method is called.

0 means the emitter will not stop based on duration.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L571](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L571)  
> Since: 3.60.0

---

## elapsed

### elapsed: number

**Description:**

The internal elasped counter.

Treat this property as read-only.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3761](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3761)  
> Since: 3.60.0

---

## emitCallback

### emitCallback: [Phaser.Types.GameObjects.Particles.ParticleEmitterCallback](../typedef/types-gameobjects-particles.md)

**Description:**

A function to call when a particle is emitted.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L481](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L481)  
> Since: 3.0.0

---

## emitCallbackScope

### emitCallbackScope: \*

**Description:**

The calling context for [Phaser.GameObjects.Particles.ParticleEmitter#emitCallback](gameobjects-particles-particleemitter.md).

> Source: [src/gameobjects/particles/ParticleEmitter.js#L491](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L491)  
> Since: 3.0.0

---

## emitting

### emitting: boolean

**Description:**

Controls if the emitter is currently emitting a particle flow (when frequency >= 0).

Already alive particles will continue to update until they expire.

Controlled by [Phaser.GameObjects.Particles.ParticleEmitter#start](gameobjects-particles-particleemitter.md) and [Phaser.GameObjects.Particles.ParticleEmitter#stop](gameobjects-particles-particleemitter.md).

> Source: [src/gameobjects/particles/ParticleEmitter.js#L607](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L607)  
> Since: 3.0.0

---

## emitZones

### emitZones: Array.<[Phaser.Types.GameObjects.Particles.EmitZoneObject](../typedef/types-gameobjects-particles.md)>

**Description:**

An array containing Particle Emission Zones. These can be either EdgeZones or RandomZones.

Particles are emitted from a randomly selected zone from this array.

Prior to Phaser v3.60 an Emitter could only have one single Emission Zone.

In 3.60 they can now have an array of Emission Zones.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L645](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L645)  
> Since: 3.60.0

---

## flowCounter

### flowCounter: number

**Description:**

The internal flow counter.

Treat this property as read-only.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3692](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3692)  
> Since: 3.60.0

---

## follow

### follow: [Phaser.Types.Math.Vector2Like](../typedef/types-math.md)

**Description:**

A Game Object whose position is used as the particle origin.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L699](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L699)  
> Since: 3.0.0

---

## followOffset

### followOffset: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The offset of the particle origin from the [Phaser.GameObjects.Particles.ParticleEmitter#follow](gameobjects-particles-particleemitter.md) target.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L711](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L711)  
> Since: 3.0.0

---

## frame

### frame: [Phaser.Textures.Frame](textures-frame.md)

**Description:**

The Texture Frame this Game Object is using to render with.

**Inherits:** [Phaser.GameObjects.Components.Texture#frame](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L30)  
> Since: 3.0.0

---

## frameCounter

### frameCounter: number

**Description:**

The internal frame counter.

Treat this property as read-only.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3715](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3715)  
> Since: 3.60.0

---

## frameQuantity

### frameQuantity: number

**Description:**

The number of consecutive particles that receive a single texture frame (per frame cycle).

> Source: [src/gameobjects/particles/ParticleEmitter.js#L753](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L753)  
> Since: 3.0.0

---

## frames

### frames: Array.<[Phaser.Textures.Frame](textures-frame.md)>

**Description:**

The texture frames assigned to particles.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L733](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L733)  
> Since: 3.0.0

---

## frequency

### frequency: number

**Description:**

For a flow emitter, the time interval (>= 0) between particle flow cycles in ms.

A value of 0 means there is one particle flow cycle for each logic update (the maximum flow frequency). This is the default setting.

For an exploding emitter, this value will be -1.

Calling [Phaser.GameObjects.Particles.ParticleEmitter#flow](gameobjects-particles-particleemitter.md) also puts the emitter in flow mode (frequency >= 0).

Calling [Phaser.GameObjects.Particles.ParticleEmitter#explode](gameobjects-particles-particleemitter.md) also puts the emitter in explode mode (frequency = -1).

> Source: [src/gameobjects/particles/ParticleEmitter.js#L592](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L592)  
> Since: 3.0.0

---

## gravityX

### gravityX: number

**Description:**

Horizontal acceleration applied to emitted particles, in pixels per second squared.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L436](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L436)  
> Since: 3.0.0

---

## gravityY

### gravityY: number

**Description:**

Vertical acceleration applied to emitted particles, in pixels per second squared.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L447](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L447)  
> Since: 3.0.0

---

## hasPostPipeline

### hasPostPipeline: boolean

**Description:**

Does this Game Object have any Post Pipelines set?

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#hasPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L21)  
> Since: 3.60.0

---

## hasTransformComponent

### hasTransformComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Inherits:** [Phaser.GameObjects.Components.Transform#hasTransformComponent](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L26](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L26)  
> Since: 3.60.0

---

## hold

### hold: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The number of milliseconds to wait after a particle has finished

its life before it will be removed. This allows you to 'hold' a

particle on the screen once it has reached its final state

before it then vanishes.

Note that all particle updates will cease, including changing

alpha, scale, movement or animation.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3662](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3662)  
> Since: 3.60.0

---

## ignoreDestroy

### ignoreDestroy: boolean

**Description:**

This Game Object will ignore all calls made to its destroy method if this flag is set to `true`.

This includes calls that may come from a Group, Container or the Scene itself.

While it allows you to persist a Game Object across Scenes, please understand you are entirely

responsible for managing references to and from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#ignoreDestroy](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L196)  
> Since: 3.5.0

---

## input

### input: [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md)

**Description:**

If this Game Object is enabled for input then this property will contain an InteractiveObject instance.

Not usually set directly. Instead call `GameObject.setInteractive()`.

**Inherits:** [Phaser.GameObjects.GameObject#input](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L175](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L175)  
> Since: 3.0.0

---

## lifespan

### lifespan: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The lifespan of the emitted particles. This value is given

in milliseconds and defaults to 1000ms (1 second). When a

particle reaches this amount it is killed.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3526](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3526)  
> Since: 3.60.0

---

## mask

### mask: [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md), [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)

**Description:**

The Mask this Game Object is using during render.

**Inherits:** [Phaser.GameObjects.Components.Mask#mask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L19)  
> Since: 3.0.0

---

## maxAliveParticles

### maxAliveParticles: number

**Description:**

The maximum number of alive and rendering particles this emitter will update.

When this limit is reached, a particle needs to die before another can be emitted.

0 means no limits.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L535](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L535)  
> Since: 3.60.0

---

## maxParticles

### maxParticles: number

**Description:**

Set to hard limit the amount of particle objects this emitter is allowed to create

in total. This is the number of `Particle` instances it can create, not the number

of 'alive' particles.

0 means unlimited.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L521](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L521)  
> Since: 3.0.0

---

## maxVelocityX

### maxVelocityX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The maximum horizontal velocity emitted particles can reach, in pixels per second squared.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3144)  
> Since: 3.60.0

---

## maxVelocityY

### maxVelocityY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The maximum vertical velocity emitted particles can reach, in pixels per second squared.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3169)  
> Since: 3.60.0

---

## moveTo

### moveTo: boolean

**Description:**

Whether moveToX and moveToY are set. Set automatically during configuration.

When true the particles move toward the moveToX and moveToY coordinates and arrive at the end of their life.

Emitter angle, speedX, and speedY are ignored.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L468](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L468)  
> Since: 3.0.0

---

## moveToX

### moveToX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The x coordinate emitted particles move toward, when [Phaser.GameObjects.Particles.ParticleEmitter#moveTo](gameobjects-particles-particleemitter.md) is true.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3272)  
> Since: 3.60.0

---

## moveToY

### moveToY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The y coordinate emitted particles move toward, when [Phaser.GameObjects.Particles.ParticleEmitter#moveTo](gameobjects-particles-particleemitter.md) is true.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3296](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3296)  
> Since: 3.60.0

---

## name

### name: string

**Description:**

The name of this Game Object.

Empty by default and never populated by Phaser, this is left for developers to use.

**Inherits:** [Phaser.GameObjects.GameObject#name](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L102)  
> Since: 3.0.0

---

## ops

### ops: [Phaser.Types.GameObjects.Particles.ParticleEmitterOps](../typedef/types-gameobjects-particles.md)

**Description:**

An internal object holding all of the EmitterOp instances.

These are populated as part of the Emitter configuration parsing.

You typically do not access them directly, but instead use the

provided getters and setters on this class, such as `ParticleEmitter.speedX` etc.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L386](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L386)  
> Since: 3.60.0

---

## parentContainer

### parentContainer: [Phaser.GameObjects.Container](gameobjects-container.md)

**Description:**

The parent Container of this Game Object, if it has one.

**Inherits:** [Phaser.GameObjects.GameObject#parentContainer](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L93)  
> Since: 3.4.0

---

## particleAlpha

### particleAlpha: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The alpha value of the emitted particles. This is a value

between 0 and 1. Particles with alpha zero are invisible

and are therefore not rendered, but are still processed

by the Emitter.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3499](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3499)  
> Since: 3.60.0

---

## particleAngle

### particleAngle: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The angle at which the particles are emitted. The values are

given in degrees. This allows you to control the direction

of the emitter. If you wish instead to change the rotation

of the particles themselves, see the `particleRotate` property.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3552](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3552)  
> Since: 3.60.0

---

## particleBringToTop

### particleBringToTop: boolean

**Description:**

Newly emitted particles are added to the top of the particle list, i.e. rendered above those already alive.

Set to false to send them to the back.

Also see the `sortOrder` property for more complex particle sorting.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L621](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L621)  
> Since: 3.0.0

---

## particleClass

### particleClass: function

**Description:**

The Particle Class which will be emitted by this Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L361](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L361)  
> Since: 3.0.0

---

## particleColor

### particleColor: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

A color tint value that is applied to the texture of the emitted

particle. The value should be given in hex format, i.e. 0xff0000

for a red tint, and should not include the alpha channel.

Tints are additive, meaning a tint value of white (0xffffff) will

effectively reset the tint to nothing.

Modify the `ParticleEmitter.tintFill` property to change between

an additive and replacement tint mode.

When you define the color via the Emitter config you should give

it as an array of color values. The Particle will then interpolate

through these colors over the course of its lifespan. Setting this

will override any `tint` value that may also be given.

This is a WebGL only feature.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3398](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3398)  
> Since: 3.60.0

---

## particleRotate

### particleRotate: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The rotation (or angle) of each particle when it is emitted.

The value is given in degrees and uses a right-handed

coordinate system, where 0 degrees points to the right, 90 degrees

points down and -90 degrees points up.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3579](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3579)  
> Since: 3.60.0

---

## particleScaleX

### particleScaleX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The horizontal scale of emitted particles.

This is relative to the Emitters scale and that of any parent.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3346](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3346)  
> Since: 3.60.0

---

## particleScaleY

### particleScaleY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The vertical scale of emitted particles.

This is relative to the Emitters scale and that of any parent.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3372](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3372)  
> Since: 3.60.0

---

## particleTint

### particleTint: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

A color tint value that is applied to the texture of the emitted

particle. The value should be given in hex format, i.e. 0xff0000

for a red tint, and should not include the alpha channel.

Tints are additive, meaning a tint value of white (0xffffff) will

effectively reset the tint to nothing.

Modify the `ParticleEmitter.tintFill` property to change between

an additive and replacement tint mode.

The `tint` value will be overriden if a `color` array is provided.

This is a WebGL only feature.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3463](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3463)  
> Since: 3.60.0

---

## particleX

### particleX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md), [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](../typedef/types-gameobjects-particles.md)

**Description:**

The x coordinate the particles are emitted from.

This is relative to the Emitters x coordinate and that of any parent.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3044](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3044)  
> Since: 3.60.0

---

## particleY

### particleY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md), [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](../typedef/types-gameobjects-particles.md)

**Description:**

The y coordinate the particles are emitted from.

This is relative to the Emitters x coordinate and that of any parent.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3070](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3070)  
> Since: 3.60.0

---

## pipeline

### pipeline: [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

**Description:**

The current WebGL pipeline of this Game Object.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Pipeline#pipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L32](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L32)  
> Since: 3.0.0

---

## pipelineData

### pipelineData: object

**Description:**

An object to store pipeline specific data in, to be read by the pipelines this Game Object uses.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.Pipeline#pipelineData](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L43)  
> Since: 3.50.0

---

## postFX

### postFX: [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md)

**Description:**

The Post FX component of this Game Object.

This component allows you to apply a variety of built-in effects to this Game Object, such

as glow, blur, bloom, displacements, vignettes and more. You access them via this property,

for example:

```
Copy
const player = this.add.sprite();

player.postFX.addBloom();


```

All FX are WebGL only and do not have Canvas counterparts.

Please see the FX Class for more details and available methods.

This property is always `null` until the `initPostPipeline` method is called.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L88)  
> Since: 3.60.0

---

## postPipelineData

### postPipelineData: object

**Description:**

An object to store pipeline specific data in, to be read by the pipelines this Game Object uses.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postPipelineData](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L46)  
> Since: 3.60.0

---

## postPipelines

### postPipelines: Array.<[Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md)>

**Description:**

The WebGL Post FX Pipelines this Game Object uses for post-render effects.

The pipelines are processed in the order in which they appear in this array.

If you modify this array directly, be sure to set the

`hasPostPipeline` property accordingly.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#postPipelines](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L31)  
> Since: 3.60.0

---

## preFX

### preFX: [Phaser.GameObjects.Components.FX](gameobjects-components-fx.md)

**Description:**

The Pre FX component of this Game Object.

This component allows you to apply a variety of built-in effects to this Game Object, such

as glow, blur, bloom, displacements, vignettes and more. You access them via this property,

for example:

```
Copy
const player = this.add.sprite();

player.preFX.addBloom();


```

Only the following Game Objects support Pre FX:

* Image
* Sprite
* TileSprite
* Text
* RenderTexture
* Video

All FX are WebGL only and do not have Canvas counterparts.

Please see the FX Class for more details and available methods.

**Tags:**

* webglOnly

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#preFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L56)  
> Since: 3.60.0

---

## processors

### processors: Phaser.Structs.List.<Phaser.GameObjects.Particles.ParticleProcessor>

**Description:**

A list of Particle Processors being managed by this Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L890](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L890)  
> Since: 3.60.0

---

## quantity

### quantity: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The number of particles that are emitted each time an emission

occurs, i.e. from one 'explosion' or each frame in a 'flow' cycle.

The default is 1.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3606](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3606)  
> Since: 3.60.0

---

## radial

### radial: boolean

**Description:**

A radial emitter will emit particles in all directions between angle min and max,

using [Phaser.GameObjects.Particles.ParticleEmitter#speed](gameobjects-particles-particleemitter.md) as the value. If set to false then this acts as a point Emitter.

A point emitter will emit particles only in the direction derived from the speedX and speedY values.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L423](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L423)  
> Since: 3.0.0

---

## randomAnim

### randomAnim: boolean

**Description:**

Whether animations [Phaser.GameObjects.Particles.ParticleEmitter#anims](gameobjects-particles-particleemitter.md) are selected at random.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L773](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L773)  
> Since: 3.60.0

---

## randomFrame

### randomFrame: boolean

**Description:**

Whether texture [Phaser.GameObjects.Particles.ParticleEmitter#frames](gameobjects-particles-particleemitter.md) are selected at random.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L742](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L742)  
> Since: 3.0.0

---

## renderFlags

### renderFlags: number

**Description:**

The flags that are compared against `RENDER_MASK` to determine if this Game Object will render or not.

The bits are 0001 | 0010 | 0100 | 1000 set by the components Visible, Alpha, Transform and Texture respectively.

If those components are not used by your custom class then you can use this bitmask as you wish.

**Inherits:** [Phaser.GameObjects.GameObject#renderFlags](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L148)  
> Since: 3.0.0

---

## rotation

### rotation: number

**Description:**

The angle of this Game Object in radians.

Phaser uses a right-hand clockwise rotation system, where 0 is right, PI/2 is down, +-PI is left

and -PI/2 is up.

If you prefer to work in degrees, see the `angle` property instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#rotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L238](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L238)  
> Since: 3.0.0

---

## scale

### scale: number

**Description:**

This is a special setter that allows you to set both the horizontal and vertical scale of this Game Object

to the same value, at the same time. When reading this value the result returned is `(scaleX + scaleY) / 2`.

Use of this property implies you wish the horizontal and vertical scales to be equal to each other. If this

isn't the case, use the `scaleX` or `scaleY` properties instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#scale](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L113)  
> Since: 3.18.0

---

## scaleX

### scaleX: number

**Description:**

The horizontal scale of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#scaleX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L149)  
> Since: 3.0.0

---

## scaleY

### scaleY: number

**Description:**

The vertical scale of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#scaleY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L180)  
> Since: 3.0.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene to which this Game Object belongs.

Game Objects can only belong to one Scene.

You should consider this property as being read-only. You cannot move a

Game Object to another Scene by simply changing it.

**Inherits:** [Phaser.GameObjects.GameObject#scene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L39)  
> Since: 3.0.0

---

## scrollFactorX

### scrollFactorX: number

**Description:**

The horizontal scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#scrollFactorX](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L16)  
> Since: 3.0.0

---

## scrollFactorY

### scrollFactorY: number

**Description:**

The vertical scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#scrollFactorY](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L40)  
> Since: 3.0.0

---

## skipping

### skipping: boolean

**Description:**

An internal property used to tell when the emitter is in fast-forwarc mode.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L836](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L836)  
> Since: 3.60.0

---

## sortCallback

### sortCallback: [Phaser.Types.GameObjects.Particles.ParticleSortCallback](../typedef/types-gameobjects-particles.md)

**Description:**

The callback used to sort the particles. Only used if `sortProperty`

has been set. Set this via the `setSortCallback` method.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L880](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L880)  
> Since: 3.60.0

---

## sortOrderAsc

### sortOrderAsc: boolean

**Description:**

When `sortProperty` is defined this controls the sorting order,

either ascending or descending. Toggle to control the visual effect.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L870](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L870)  
> Since: 3.60.0

---

## sortProperty

### sortProperty: string

**Description:**

Optionally sort the particles before they render based on this

property. The property must exist on the `Particle` class, such

as `y`, `lifeT`, `scaleX`, etc.

When set this overrides the `particleBringToTop` setting.

To reset this and disable sorting, so this property to an empty string.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L855](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L855)  
> Since: 3.60.0

---

## speed

### speed: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The initial speed of emitted particles, in pixels per second.

If using this as a getter it will return the `speedX` value.

If using it as a setter it will update both `speedX` and `speedY` to the

given value.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3194](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3194)  
> Since: 3.60.0

---

## speedX

### speedX: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The initial horizontal speed of emitted particles, in pixels per second.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3224](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3224)  
> Since: 3.60.0

---

## speedY

### speedY: [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md)

**Description:**

The initial vertical speed of emitted particles, in pixels per second.

Accessing this property should typically return a number.

However, it can be set to any valid EmitterOp onEmit type.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3248](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3248)  
> Since: 3.60.0

---

## state

### state: number, string

**Description:**

The current state of this Game Object.

Phaser itself will never modify this value, although plugins may do so.

Use this property to track the state of a Game Object during its lifetime. For example, it could change from

a state of 'moving', to 'attacking', to 'dead'. The state value should be an integer (ideally mapped to a constant

in your game code), or a string. These are recommended to keep it light and simple, with fast comparisons.

If you need to store complex data about your Game Object, look at using the Data Component instead.

**Inherits:** [Phaser.GameObjects.GameObject#state](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L77)  
> Since: 3.16.0

---

## stopAfter

### stopAfter: number

**Description:**

If set, either via the Emitter config, or by directly setting this property,

the Particle Emitter will stop emitting particles once this total has been

reached. It will then enter a 'stopped' state, firing the `STOP`

event. Note that entering a stopped state doesn't mean all the particles

have finished, just that it's not emitting any further ones.

To know when the final particle expires, listen for the COMPLETE event.

Use this if you wish to launch an exact number of particles and then stop

your emitter afterwards.

The counter is reset each time the `ParticleEmitter.start` method is called.

0 means the emitter will not stop based on total emitted particles.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L548](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L548)  
> Since: 3.60.0

---

## stopCounter

### stopCounter: number

**Description:**

The internal stop counter.

Treat this property as read-only.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3784](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3784)  
> Since: 3.60.0

---

## tabIndex

### tabIndex: number

**Description:**

The Tab Index of the Game Object.

Reserved for future use by plugins and the Input Manager.

**Inherits:** [Phaser.GameObjects.GameObject#tabIndex](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L125)  
> Since: 3.0.0

---

## texture

### texture: [Phaser.Textures.Texture](textures-texture.md), [Phaser.Textures.CanvasTexture](textures-canvastexture.md)

**Description:**

The Texture this Game Object is using to render with.

**Inherits:** [Phaser.GameObjects.Components.Texture#texture](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L21)  
> Since: 3.0.0

---

## timeScale

### timeScale: number

**Description:**

The time rate applied to active particles, affecting lifespan, movement, and tweens. Values larger than 1 are faster than normal.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L635](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L635)  
> Since: 3.0.0

---

## tintFill

### tintFill: boolean

**Description:**

The tint fill mode used by the Particles in this Emitter.

`false` = An additive tint (the default), where vertices colors are blended with the texture.

`true` = A fill tint, where the vertices colors replace the texture, but respects texture alpha.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L899](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L899)  
> Since: 3.60.0

---

## trackVisible

### trackVisible: boolean

**Description:**

Whether the emitter's [Phaser.GameObjects.Particles.ParticleEmitter#visible](gameobjects-particles-particleemitter.md) state will track

the [Phaser.GameObjects.Particles.ParticleEmitter#follow](gameobjects-particles-particleemitter.md) target's visibility state.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L721](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L721)  
> Since: 3.0.0

---

## type

### type: string

**Description:**

A textual representation of this Game Object, i.e. `sprite`.

Used internally by Phaser but is available for your own custom classes to populate.

**Inherits:** [Phaser.GameObjects.GameObject#type](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L67](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L67)  
> Since: 3.0.0

---

## viewBounds

### viewBounds: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

An optional Rectangle object that is used during rendering to cull Particles from

display. For example, if your particles are limited to only move within a 300x300

sized area from their origin, then you can set this Rectangle to those dimensions.

The renderer will check to see if the `viewBounds` Rectangle intersects with the

Camera bounds during the render step and if not it will skip rendering the Emitter

entirely.

This allows you to create many emitters in a Scene without the cost of

rendering if the contents aren't visible.

Note that the Emitter will not perform any checks to see if the Particles themselves

are outside of these bounds, or not. It will simply check the bounds against the

camera. Use the `getBounds` method with the `advance` parameter to help define

the location and placement of the view bounds.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L674](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L674)  
> Since: 3.60.0

---

## visible

### visible: boolean

**Description:**

The visible state of the Game Object.

An invisible Game Object will skip rendering, but will still process update logic.

**Inherits:** [Phaser.GameObjects.Components.Visible#visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L31)  
> Since: 3.0.0

---

## w

### w: number

**Description:**

The w position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#w](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L103)  
> Since: 3.0.0

---

## worldMatrix

### worldMatrix: [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md)

**Description:**

An internal Transform Matrix used to cache this emitters world matrix.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L846](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L846)  
> Since: 3.60.0

---

## x

### x: number

**Description:**

The x position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#x](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L70)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#y](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L80)  
> Since: 3.0.0

---

## z

### z: number

**Description:**

The z position of this Game Object.

Note: The z position does not control the rendering order of 2D Game Objects. Use

[Phaser.GameObjects.Components.Depth#depth](../namespace/gameobjects-components-depth.md) instead.

**Inherits:** [Phaser.GameObjects.Components.Transform#z](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L90)  
> Since: 3.0.0

---

## zoneIndex

### zoneIndex: number

**Description:**

The internal zone index.

Treat this property as read-only.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3830](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3830)  
> Since: 3.60.0

---

## zoneTotal

### zoneTotal: number

**Description:**

The internal zone total.

Treat this property as read-only.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3853](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3853)  
> Since: 3.60.0

---

# Private Members

## \_alpha

### \_alpha: number

**Description:**

Private internal value. Holds the global alpha value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#\_alpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L22](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L22)  
> Since: 3.0.0

---

## \_blendMode

### \_blendMode: number

**Description:**

Private internal value. Holds the current blend mode.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.BlendMode#\_blendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L19)  
> Since: 3.0.0

---

## \_depth

### \_depth: number

**Description:**

Private internal value. Holds the depth of the Game Object.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Depth#\_depth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L19)  
> Since: 3.0.0

---

## \_rotation

### \_rotation: number

**Description:**

Private internal value. Holds the rotation value in radians.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_rotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L59)  
> Since: 3.0.0

---

## \_scaleX

### \_scaleX: number

**Description:**

Private internal value. Holds the horizontal scale value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_scaleX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L37)  
> Since: 3.0.0

---

## \_scaleY

### \_scaleY: number

**Description:**

Private internal value. Holds the vertical scale value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Transform#\_scaleY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L48)  
> Since: 3.0.0

---

## \_visible

### \_visible: boolean

**Description:**

Private internal value. Holds the visible value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Visible#\_visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L20](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L20)  
> Since: 3.0.0

---

## alive

### alive: Array.<[Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md)>

**Description:**

An array containing all currently live and rendering Particle instances.

**Access:** private

> Source: [src/gameobjects/particles/ParticleEmitter.js#L805](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L805)  
> Since: 3.0.0

---

## counters

### counters: Float32Array

**Description:**

Internal array that holds counter data:

0 - flowCounter - The time until next flow cycle.

1 - frameCounter - Counts up to [Phaser.GameObjects.Particles.ParticleEmitter#frameQuantity](gameobjects-particles-particleemitter.md).

2 - animCounter - Counts up to animQuantity.

3 - elapsed - The time remaining until the `duration` limit is reached.

4 - stopCounter - The number of particles remaining until `stopAfter` limit is reached.

5 - completeFlag - Has the COMPLETE event been emitted?

6 - zoneIndex - The emit zone index counter.

7 - zoneTotal - The emit zone total counter.

8 - currentFrame - The current texture frame, as an index of [Phaser.GameObjects.Particles.ParticleEmitter#frames](gameobjects-particles-particleemitter.md).

9 - currentAnim - The current animation, as an index of [Phaser.GameObjects.Particles.ParticleEmitter#anims](gameobjects-particles-particleemitter.md).

**Access:** private

> Source: [src/gameobjects/particles/ParticleEmitter.js#L815](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L815)  
> Since: 3.60.0

---

## dead

### dead: Array.<[Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md)>

**Description:**

An array containing all currently inactive Particle instances.

**Access:** private

> Source: [src/gameobjects/particles/ParticleEmitter.js#L795](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L795)  
> Since: 3.0.0

---

## isCropped

### isCropped: boolean

**Description:**

Internal flag. Not to be set by this Game Object.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Texture#isCropped](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L39)  
> Since: 3.11.0

---

# Public Methods

## addDeathZone

### <instance> addDeathZone(config)

**Description:**

Adds a new Particle Death Zone to this Emitter.

A particle is immediately killed as soon as its x/y coordinates intersect

with any of the configured Death Zones.

The `source` can be a Geometry Shape, such as a Circle, Rectangle or Triangle.

Any valid object from the `Phaser.Geometry` namespace is allowed, as long as

it supports a `contains` function. You can set the `type` to be either `onEnter`

or `onLeave`.

A single Death Zone instance can only exist once within this Emitter, but can belong

to multiple Emitters.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.GameObjects.Particles.DeathZoneObject](../typedef/types-gameobjects-particles.md) | Array.<[Phaser.Types.GameObjects.Particles.DeathZoneObject](../typedef/types-gameobjects-particles.md)> | No | A Death Zone configuration object, a Death Zone instance, a valid Geometry object or an array of them. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.GameObjects.Particles.Zones.DeathZone](gameobjects-particles-zones-deathzone.md)> - An array of the Death Zones that were added to this Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1705](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1705)  
> Since: 3.60.0

---

## addedToScene

### <instance> addedToScene()

**Description:**

This callback is invoked when this Game Object is added to a Scene.

Can be overriden by custom Game Objects, but be aware of some Game Objects that

will use this, such as Sprites, to add themselves into the Update List.

You can also listen for the `ADDED_TO_SCENE` event from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addedToScene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L562](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L562)  
> Since: 3.50.0

---

## addEmitZone

### <instance> addEmitZone(zone)

**Description:**

Adds a new Particle Emission Zone to this Emitter.

An [EdgeZone](../typedef/types-gameobjects-particles.md) places particles on its edges.

Its [source](../typedef/types-gameobjects-particles.md) can be a Curve, Path, Circle, Ellipse, Line, Polygon, Rectangle, or Triangle;

or any object with a suitable [getPoints](../typedef/types-gameobjects-particles.md) method.

A [RandomZone](../typedef/types-gameobjects-particles.md) places the particles randomly within its interior.

Its [source](gameobjects-particles-zones-randomzone.md) can be a Circle, Ellipse, Line, Polygon, Rectangle, or Triangle; or any object with a suitable [getRandomPoint](../typedef/types-gameobjects-particles.md) method.

An Emission Zone can only exist once within this Emitter.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| zone | [Phaser.Types.GameObjects.Particles.EmitZoneData](../typedef/types-gameobjects-particles.md) | Array.<[Phaser.Types.GameObjects.Particles.EmitZoneData](../typedef/types-gameobjects-particles.md)> | No | An Emission Zone configuration object, a RandomZone or EdgeZone instance, or an array of them. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Types.GameObjects.Particles.EmitZoneObject](../typedef/types-gameobjects-particles.md)> - An array of the Emission Zones that were added to this Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1803](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1803)  
> Since: 3.60.0

---

## addListener

### <instance> addListener(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addParticleBounds

### <instance> addParticleBounds(x, [y], [width], [height], [collideLeft], [collideRight], [collideTop], [collideBottom])

**Description:**

Creates a Particle Bounds processor and adds it to this Emitter.

This processor will check to see if any of the active Particles hit

the defined boundary, as specified by a Rectangle shape in world-space.

If so, they are 'rebounded' back again by having their velocity adjusted.

The strength of the rebound is controlled by the `Particle.bounce`

property.

You should be careful to ensure that you emit particles within a bounds,

if set, otherwise it will lead to unpredictable visual results as the

particles are hastily repositioned.

The Particle Bounds processor is returned from this method. If you wish

to modify the area you can directly change its `bounds` property, along

with the `collideLeft` etc values.

To disable the bounds you can either set its `active` property to `false`,

or if you no longer require it, call `ParticleEmitter.removeParticleProcessor`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | [Phaser.Types.GameObjects.Particles.ParticleEmitterBounds](../typedef/types-gameobjects-particles.md) | [Phaser.Types.GameObjects.Particles.ParticleEmitterBoundsAlt](../typedef/types-gameobjects-particles.md) | No |  |
| --- | --- | --- | --- | --- |
| y | number | Yes |  | The y-coordinate of the top edge of the boundary. |
| width | number | Yes |  | The width of the boundary. |
| height | number | Yes |  | The height of the boundary. |
| collideLeft | boolean | Yes | true | Whether particles interact with the left edge of the bounds. |
| collideRight | boolean | Yes | true | Whether particles interact with the right edge of the bounds. |
| collideTop | boolean | Yes | true | Whether particles interact with the top edge of the bounds. |
| collideBottom | boolean | Yes | true | Whether particles interact with the bottom edge of the bounds. |

**Returns:** [Phaser.GameObjects.Particles.ParticleBounds](gameobjects-particles-particlebounds.md) - The Particle Bounds processor.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1459](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1459)  
> Since: 3.60.0

---

## addParticleProcessor

### <instance> addParticleProcessor(processor)

**Description:**

Adds a Particle Processor, such as a Gravity Well, to this Emitter.

It will start processing particles from the next update as long as its `active`

property is set.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| processor | T | No | The Particle Processor to add to this Emitter Manager. |
| --- | --- | --- | --- |

**Returns:** T - The Particle Processor that was added to this Emitter Manager.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2034](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2034)  
> Since: 3.60.0

---

## addToDisplayList

### <instance> addToDisplayList([displayList])

**Description:**

Adds this Game Object to the given Display List.

If no Display List is specified, it will default to the Display List owned by the Scene to which

this Game Object belongs.

A Game Object can only exist on one Display List at any given time, but may move freely between them.

If this Game Object is already on another Display List when this method is called, it will first

be removed from it, before being added to the new list.

You can query which list it is on by looking at the `Phaser.GameObjects.GameObject#displayList` property.

If a Game Object isn't on any display list, it will not be rendered. If you just wish to temporarly

disable it from rendering, consider using the `setVisible` method, instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| displayList | [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md) | [Phaser.GameObjects.Layer](gameobjects-layer.md) | Yes | The Display List to add to. Defaults to the Scene Display List. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object.

**Fires:** [Phaser.Scenes.Events#event:ADDED\_TO\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:ADDED\_TO\_SCENE](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#addToDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L684](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L684)  
> Since: 3.53.0

---

## addToUpdateList

### <instance> addToUpdateList()

**Description:**

Adds this Game Object to the Update List belonging to the Scene.

When a Game Object is added to the Update List it will have its `preUpdate` method called

every game frame. This method is passed two parameters: `delta` and `time`.

If you wish to run your own logic within `preUpdate` then you should always call

`super.preUpdate(delta, time)` within it, or it may fail to process required operations,

such as Sprite animations.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#addToUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L735](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L735)  
> Since: 3.53.0

---

## atLimit

### <instance> atLimit()

**Description:**

Whether this emitter is at either its hard-cap limit (maxParticles), if set, or

the max allowed number of 'alive' particles (maxAliveParticles).

**Returns:** boolean - Returns `true` if this Emitter is at its limit, or `false` if no limit, or below the `maxParticles` level.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2195](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2195)  
> Since: 3.0.0

---

## clearAlpha

### <instance> clearAlpha()

**Description:**

Clears all alpha values associated with this Game Object.

Immediately sets the alpha levels back to 1 (fully opaque).

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#clearAlpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L33](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L33)  
> Since: 3.0.0

---

## clearDeathZones

### <instance> clearDeathZones()

**Description:**

Clear all Death Zones from this Particle Emitter.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1788](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1788)  
> Since: 3.70.0

---

## clearEmitZones

### <instance> clearEmitZones()

**Description:**

Clear all Emission Zones from this Particle Emitter.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1898](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1898)  
> Since: 3.70.0

---

## clearFX

### <instance> clearFX()

**Description:**

Removes all Pre and Post FX Controllers from this Game Object.

If you wish to remove a single controller, use the `preFX.remove(fx)` or `postFX.remove(fx)` methods instead.

If you wish to clear a single controller, use the `preFX.clear()` or `postFX.clear()` methods instead.

**Tags:**

* webglOnly

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#clearFX](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L337](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L337)  
> Since: 3.60.0

---

## clearMask

### <instance> clearMask([destroyMask])

**Description:**

Clears the mask that this Game Object was using.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| destroyMask | boolean | Yes | false | Destroy the mask before clearing it? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#clearMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L56)  
> Since: 3.6.2

---

## copyPosition

### <instance> copyPosition(source)

**Description:**

Copies an object's coordinates to this Game Object's position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | [Phaser.Types.Math.Vector3Like](../typedef/types-math.md) | [Phaser.Types.Math.Vector4Like](../typedef/types-math.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#copyPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L293](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L293)  
> Since: 3.50.0

---

## createBitmapMask

### <instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])

**Description:**

Creates and returns a Bitmap Mask. This mask can be used by any Game Object,

including this one, or a Dynamic Texture.

Note: Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.

To create the mask you need to pass in a reference to a renderable Game Object.

A renderable Game Object is one that uses a texture to render with, such as an

Image, Sprite, Render Texture or BitmapText.

If you do not provide a renderable object, and this Game Object has a texture,

it will use itself as the object. This means you can call this method to create

a Bitmap Mask from any renderable texture-based Game Object.

**Tags:**

* generic
* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| maskObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | [Phaser.Textures.DynamicTexture](textures-dynamictexture.md) | Yes | The Game Object or Dynamic Texture that will be used as the mask. If `null` it will generate an Image Game Object using the rest of the arguments. |
| --- | --- | --- | --- |
| x | number | Yes | If creating a Game Object, the horizontal position in the world. |
| y | number | Yes | If creating a Game Object, the vertical position in the world. |
| texture | string | [Phaser.Textures.Texture](textures-texture.md) | Yes | If creating a Game Object, the key, or instance of the Texture it will use to render with, as stored in the Texture Manager. |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | Yes |

**Returns:** [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) - This Bitmap Mask that was created.

**Inherits:** [Phaser.GameObjects.Components.Mask#createBitmapMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L80)  
> Since: 3.6.2

---

## createEmitter

### <instance> createEmitter()

**Description:**

Prints a warning to the console if you mistakenly call this function

thinking it works the same way as Phaser v3.55.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3032](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3032)  
> Since: 3.60.0

---

## createGeometryMask

### <instance> createGeometryMask([graphics])

**Description:**

Creates and returns a Geometry Mask. This mask can be used by any Game Object,

including this one.

To create the mask you need to pass in a reference to a Graphics Game Object.

If you do not provide a graphics object, and this Game Object is an instance

of a Graphics object, then it will use itself to create the mask.

This means you can call this method to create a Geometry Mask from any Graphics Game Object.

**Tags:**

* generic
* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | [Phaser.GameObjects.Shape](gameobjects-shape.md) | Yes | A Graphics Game Object, or any kind of Shape Game Object. The geometry within it will be used as the mask. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md) - This Geometry Mask that was created.

**Inherits:** [Phaser.GameObjects.Components.Mask#createGeometryMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L120)  
> Since: 3.6.2

---

## createGravityWell

### <instance> createGravityWell(config)

**Description:**

Creates a new Gravity Well, adds it to this Emitter and returns a reference to it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.GameObjects.Particles.GravityWellConfig](../typedef/types-gameobjects-particles.md) | No | Configuration settings for the Gravity Well to create. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.GravityWell](gameobjects-particles-gravitywell.md) - The Gravity Well that was created.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2106)  
> Since: 3.60.0

---

## depthSort

### <instance> depthSort()

**Description:**

Sorts active particles with [Phaser.GameObjects.Particles.ParticleEmitter#depthSortCallback](gameobjects-particles-particleemitter.md).

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2532](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2532)  
> Since: 3.0.0

---

## depthSortCallback

### <instance> depthSortCallback(a, b)

**Description:**

Calculates the difference of two particles, for sorting them by depth.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | object | No | The first particle. |
| --- | --- | --- | --- |
| b | object | No | The second particle. |

**Returns:** number - The difference of a and b's y coordinates.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2547](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2547)  
> Since: 3.0.0

---

## destroy

### <instance> destroy([fromScene])

**Description:**

Destroys this Game Object removing it from the Display List and Update List and

severing all ties to parent resources.

Also removes itself from the Input Manager and Physics Manager if previously enabled.

Use this to remove a Game Object from your game if you don't ever plan to use it again.

As long as no reference to it exists within your own code it should become free for

garbage collection by the browser.

If you just want to temporarily disable an object then look at using the

Game Object Pool instead of destroying it, as destroyed objects cannot be resurrected.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| fromScene | boolean | Yes | false | `True` if this Game Object is being destroyed by the Scene, `false` if not. |
| --- | --- | --- | --- | --- |

**Fires:** [Phaser.GameObjects.Events#event:DESTROY](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#destroy](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L855](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L855)  
> Since: 3.0.0

---

## disableInteractive

### <instance> disableInteractive([resetCursor])

**Description:**

If this Game Object has previously been enabled for input, this will disable it.

An object that is disabled for input stops processing or being considered for

input events, but can be turned back on again at any time by simply calling

`setInteractive()` with no arguments provided.

If want to completely remove interaction from this Game Object then use `removeInteractive` instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetCursor | boolean | Yes | false | Should the currently active Input cursor, if any, be reset to the default cursor? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#disableInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L494](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L494)  
> Since: 3.7.0

---

## emit

### <instance> emit(event, [args])

**Description:**

Calls each of the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| args | \* | Yes | Additional arguments that will be passed to the event handler. |

**Returns:** boolean - `true` if the event had listeners, else `false`.

**Inherits:** [Phaser.Events.EventEmitter#emit](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L86)  
> Since: 3.0.0

---

## emitParticle

### <instance> emitParticle([count], [x], [y])

**Description:**

Emits particles at a given position (or the emitters current position).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| count | number | Yes | "this.quantity" | The number of Particles to emit. |
| --- | --- | --- | --- | --- |
| x | number | Yes | "this.x" | The x coordinate to emit the Particles from. |
| y | number | Yes | "this.x" | The y coordinate to emit the Particles from. |

**Returns:** [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md), undefined - The most recently emitted Particle, or `undefined` if the emitter is at its limit.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2648](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2648)  
> Since: 3.0.0

---

## emitParticleAt

### <instance> emitParticleAt([x], [y], [count])

**Description:**

Emits particles at the given position. If no position is given, it will

emit from this Emitters current location.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | "this.x" | The x coordinate to emit the Particles from. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "this.x" | The y coordinate to emit the Particles from. |
| count | number | Yes | "this.quantity" | The number of Particles to emit. |

**Returns:** [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md), undefined - The most recently emitted Particle, or `undefined` if the emitter is at its limit.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2630](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2630)  
> Since: 3.0.0

---

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## explode

### <instance> explode([count], [x], [y])

**Description:**

Puts the emitter in explode mode (frequency = -1), stopping any current particle flow, and emits several particles all at once.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| count | number | Yes | "this.quantity" | The number of Particles to emit. |
| --- | --- | --- | --- | --- |
| x | number | Yes | "this.x" | The x coordinate to emit the Particles from. |
| y | number | Yes | "this.x" | The y coordinate to emit the Particles from. |

**Returns:** [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md), undefined - The most recently emitted Particle, or `undefined` if the emitter is at its limit.

**Fires:** [Phaser.GameObjects.Particles.Events#event:EXPLODE](../event/gameobjects-particles-events.md)

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2604](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2604)  
> Since: 3.0.0

---

## fastForward

### <instance> fastForward(time, [delta])

**Description:**

Fast forwards this Particle Emitter and all of its particles.

Works by running the Emitter `preUpdate` handler in a loop until the `time`

has been reached at `delta` steps per loop.

All callbacks and emitter related events that would normally be fired

will still be invoked.

You can make an emitter 'fast forward' via the emitter config using the

`advance` property. Set this value to the number of ms you wish the

emitter to be fast-forwarded by. Or, call this method post-creation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The number of ms to advance the Particle Emitter by. |
| --- | --- | --- | --- |
| delta | number | Yes | The amount of delta to use for each step. Defaults to 1000 / 60. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2729](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2729)  
> Since: 3.60.0

---

## flow

### <instance> flow(frequency, [count], [stopAfter])

**Description:**

Puts the emitter in flow mode (frequency >= 0) and starts (or restarts) a particle flow.

To resume a flow at the current frequency and quantity, use [Phaser.GameObjects.Particles.ParticleEmitter#start](gameobjects-particles-particleemitter.md) instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| frequency | number | No |  | The time interval (>= 0) of each flow cycle, in ms. |
| --- | --- | --- | --- | --- |
| count | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md) | Yes | 1 | The number of particles to emit at each flow cycle. |
| stopAfter | number | Yes |  | Stop this emitter from firing any more particles once this value is reached. Set to zero for unlimited. Setting this parameter will override any `stopAfter` value already set in the Emitter configuration object. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

**Fires:** [Phaser.GameObjects.Particles.Events#event:START](../event/gameobjects-particles-events.md)

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2572](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2572)  
> Since: 3.0.0

---

## forEachAlive

### <instance> forEachAlive(callback, context)

**Description:**

Calls a function for each active particle in this emitter. The function is

sent two parameters: a reference to the Particle instance and to this Emitter.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | [Phaser.Types.GameObjects.Particles.ParticleEmitterCallback](../typedef/types-gameobjects-particles.md) | No | The function. |
| --- | --- | --- | --- |
| context | \* | No | The functions calling context. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2301](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2301)  
> Since: 3.0.0

---

## forEachDead

### <instance> forEachDead(callback, context)

**Description:**

Calls a function for each inactive particle in this emitter.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | [Phaser.Types.GameObjects.Particles.ParticleEmitterCallback](../typedef/types-gameobjects-particles.md) | No | The function. |
| --- | --- | --- | --- |
| context | \* | No | The functions calling context. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2327](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2327)  
> Since: 3.0.0

---

## getAliveParticleCount

### <instance> getAliveParticleCount()

**Description:**

Gets the number of active (in-use) particles in this emitter.

**Returns:** number - The number of particles with `active=true`.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2156](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2156)  
> Since: 3.0.0

---

## getAnim

### <instance> getAnim()

**Description:**

Chooses an animation from [Phaser.GameObjects.Particles.ParticleEmitter#anims](gameobjects-particles-particleemitter.md), if populated.

**Returns:** string - The animation to play, or `null` if there aren't any.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1332)  
> Since: 3.60.0

---

## getBounds

### <instance> getBounds([padding], [advance], [delta], [output])

**Description:**

Returns a bounds Rectangle calculated from the bounds of all currently

*active* Particles in this Emitter. If this Emitter has only just been

created and not yet rendered, then calling this method will return a Rectangle

with a max safe integer for dimensions. Use the `advance` parameter to

avoid this.

Typically it takes a few seconds for a flow Emitter to 'warm up'. You can

use the `advance` and `delta` parameters to force the Emitter to

'fast forward' in time to try and allow the bounds to be more accurate,

as it will calculate the bounds based on the particle bounds across all

timesteps, giving a better result.

You can also use the `padding` parameter to increase the size of the

bounds. Emitters with a lot of randomness in terms of direction or lifespan

can often return a bounds smaller than their possible maximum. By using

the `padding` (and `advance` if needed) you can help limit this.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| padding | number | Yes | The amount of padding, in pixels, to add to the bounds Rectangle. |
| --- | --- | --- | --- |
| advance | number | Yes | The number of ms to advance the Particle Emitter by. Defaults to 0, i.e. not used. |
| delta | number | Yes | The amount of delta to use for each step. Defaults to 1000 / 60. |
| output | [Phaser.Geom.Rectangle](geom-rectangle.md) | Yes | The Rectangle to store the results in. If not given a new one will be created. |

**Returns:** [Phaser.Geom.Rectangle](geom-rectangle.md) - A Rectangle containing the calculated bounds of this Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2930](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2930)  
> Since: 3.60.0

---

## getData

### <instance> getData(key)

**Description:**

Retrieves the value for the given key in this Game Objects Data Manager, or undefined if it doesn't exist.

You can also access values via the `values` object. For example, if you had a key called `gold` you can do either:

```
Copy
sprite.getData('gold');


```

Or access the value directly:

```
Copy
sprite.data.values.gold;


```

You can also pass in an array of keys, in which case an array of values will be returned:

```
Copy
sprite.getData([ 'gold', 'armor', 'health' ]);


```

This approach is useful for destructuring arrays in ES6.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | Array.<string> | No | The key of the value to retrieve, or an array of keys. |
| --- | --- | --- | --- |

**Returns:** \* - The value belonging to the given key, or an array of values, the order of which will match the input array.

**Inherits:** [Phaser.GameObjects.GameObject#getData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L416](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L416)  
> Since: 3.0.0

---

## getDeadParticleCount

### <instance> getDeadParticleCount()

**Description:**

Gets the number of inactive (available) particles in this emitter.

**Returns:** number - The number of particles with `active=false`.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2169)  
> Since: 3.0.0

---

## getDeathZone

### <instance> getDeathZone(particle)

**Description:**

Takes the given particle and checks to see if any of the configured Death Zones

will kill it and returns the result. This method is called automatically as part

of the `Particle.update` process.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle to test against the Death Zones. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the particle should be killed, otherwise `false`.

**Fires:** [Phaser.GameObjects.Particles.Events#event:DEATH\_ZONE](../event/gameobjects-particles-events.md)

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1962](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1962)  
> Since: 3.60.0

---

## getDisplayList

### <instance> getDisplayList()

**Description:**

Returns a reference to the underlying display list *array* that contains this Game Object,

which will be either the Scene's Display List or the internal list belonging

to its parent Container, if it has one.

If this Game Object is not on a display list or in a container, it will return `null`.

You should be very careful with this method, and understand that it returns a direct reference to the

internal array used by the Display List. Mutating this array directly can cause all kinds of subtle

and difficult to debug issues in your game.

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - The internal Display List array of Game Objects, or `null`.

**Inherits:** [Phaser.GameObjects.GameObject#getDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L823](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L823)  
> Since: 3.85.0

---

## getEmitZone

### <instance> getEmitZone(particle)

**Description:**

Takes the given particle and sets its x/y coordinates to match the next available

emission zone, if any have been configured. This method is called automatically

as part of the `Particle.fire` process.

The Emit Zones are iterated in sequence. Once a zone has had a particle emitted

from it, then the next zone is used and so on, in a loop.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| particle | [Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md) | No | The particle to set the emission zone for. |
| --- | --- | --- | --- |

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1915](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1915)  
> Since: 3.60.0

---

## getFrame

### <instance> getFrame()

**Description:**

Chooses a texture frame from [Phaser.GameObjects.Particles.ParticleEmitter#frames](gameobjects-particles-particleemitter.md).

**Returns:** [Phaser.Textures.Frame](textures-frame.md) - The texture frame.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1221](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1221)  
> Since: 3.0.0

---

## getIndexList

### <instance> getIndexList()

**Description:**

Returns an array containing the display list index of either this Game Object, or if it has one,

its parent Container. It then iterates up through all of the parent containers until it hits the

root of the display list (which is index 0 in the returned array).

Used internally by the InputPlugin but also useful if you wish to find out the display depth of

this Game Object and all of its ancestors.

**Returns:** Array.<number> - An array of display list position indexes.

**Inherits:** [Phaser.GameObjects.GameObject#getIndexList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L635](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L635)  
> Since: 3.4.0

---

## getLocalPoint

### <instance> getLocalPoint(x, y, [point], [camera])

**Description:**

Takes the given `x` and `y` coordinates and converts them into local space for this

Game Object, taking into account parent and local transforms, and the Display Origin.

The returned Vector2 contains the translated point in its properties.

A Camera needs to be provided in order to handle modified scroll factors. If no

camera is specified, it will use the `main` camera from the Scene to which this

Game Object belongs.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position to translate. |
| --- | --- | --- | --- |
| y | number | No | The y position to translate. |
| point | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2, or point-like object, to store the results in. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Camera which is being tested against. If not given will use the Scene default camera. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The translated point.

**Inherits:** [Phaser.GameObjects.Components.Transform#getLocalPoint](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L542](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L542)  
> Since: 3.50.0

---

## getLocalTransformMatrix

### <instance> getLocalTransformMatrix([tempMatrix])

**Description:**

Gets the local transform matrix for this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | The matrix to populate with the values from this Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - The populated Transform Matrix.

**Inherits:** [Phaser.GameObjects.Components.Transform#getLocalTransformMatrix](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L484](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L484)  
> Since: 3.4.0

---

## getParentRotation

### <instance> getParentRotation()

**Description:**

Gets the sum total rotation of all of this Game Objects parent Containers.

The returned value is in radians and will be zero if this Game Object has no parent container.

**Returns:** number - The sum total rotation, in radians, of all parent containers of this Game Object.

**Inherits:** [Phaser.GameObjects.Components.Transform#getParentRotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L592](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L592)  
> Since: 3.18.0

---

## getParticleCount

### <instance> getParticleCount()

**Description:**

Gets the total number of particles in this emitter.

**Returns:** number - The number of particles, including both alive and dead.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2182)  
> Since: 3.0.0

---

## getPipelineName

### <instance> getPipelineName()

**Description:**

Gets the name of the WebGL Pipeline this Game Object is currently using.

**Tags:**

* webglOnly

**Returns:** string - The string-based name of the pipeline being used by this Game Object, or null.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#getPipelineName](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L201](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L201)  
> Since: 3.0.0

---

## getPostPipeline

### <instance> getPostPipeline(pipeline)

**Description:**

Gets a Post Pipeline instance from this Game Object, based on the given name, and returns it.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | function | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md), Array.<[Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md)> - An array of all the Post Pipelines matching the name. This array will be empty if there was no match. If there was only one single match, that pipeline is returned directly, not in an array.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#getPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L237)  
> Since: 3.60.0

---

## getProcessors

### <instance> getProcessors()

**Description:**

Gets all active Particle Processors.

**Returns:** Array.<[Phaser.GameObjects.Particles.ParticleProcessor](gameobjects-particles-particleprocessor.md)> - - An array of active Particle Processors.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2093](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2093)  
> Since: 3.60.0

---

## getWorldTransformMatrix

### <instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])

**Description:**

Gets the world transform matrix for this Game Object, factoring in any parent Containers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tempMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | The matrix to populate with the values from this Game Object. |
| --- | --- | --- | --- |
| parentMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | A temporary matrix to hold parent values during the calculations. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - The populated Transform Matrix.

**Inherits:** [Phaser.GameObjects.Components.Transform#getWorldTransformMatrix](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L501)  
> Since: 3.4.0

---

## incData

### <instance> incData(key, [amount])

**Description:**

Increase a value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is increased from 0.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

When the value is first set, a `setdata` event is emitted from this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key to change the value for. |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 1 | The amount to increase the given key by. Pass a negative value to decrease the key. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#incData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L357](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L357)  
> Since: 3.23.0

---

## initPipeline

### <instance> initPipeline([pipeline])

**Description:**

Sets the initial WebGL Pipeline of this Game Object.

This should only be called during the instantiation of the Game Object. After that, use `setPipeline`.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | Yes | Either the string-based name of the pipeline, or a pipeline instance to set. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the pipeline was set successfully, otherwise `false`.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#initPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L53)  
> Since: 3.0.0

---

## initPostPipeline

### <instance> initPostPipeline([preFX])

**Description:**

This should only be called during the instantiation of the Game Object.

It is called by default by all core Game Objects and doesn't need

calling again.

After that, use `setPostPipeline`.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| preFX | boolean | Yes | false | Does this Game Object support Pre FX? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#initPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L113)  
> Since: 3.60.0

---

## killAll

### <instance> killAll()

**Description:**

Deactivates every particle in this emitter immediately.

This particles are killed but do not emit an event or callback.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2278](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2278)  
> Since: 3.0.0

---

## listenerCount

### <instance> listenerCount(event)

**Description:**

Return the number of listeners listening to a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** number - The number of listeners.

**Inherits:** [Phaser.Events.EventEmitter#listenerCount](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L75)  
> Since: 3.0.0

---

## listeners

### <instance> listeners(event)

**Description:**

Return the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** Array.<function()> - The registered listeners.

**Inherits:** [Phaser.Events.EventEmitter#listeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L64)  
> Since: 3.0.0

---

## off

### <instance> off(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#off](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L151)  
> Since: 3.0.0

---

## on

### <instance> on(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## once

### <instance> once(event, fn, [context])

**Description:**

Add a one-time listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## onParticleDeath

### <instance> onParticleDeath(callback, [context])

**Description:**

Sets a function to call for each particle death.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | [Phaser.Types.GameObjects.Particles.ParticleDeathCallback](../typedef/types-gameobjects-particles.md) | No | The function. |
| --- | --- | --- | --- |
| context | \* | Yes | The function's calling context. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2246](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2246)  
> Since: 3.0.0

---

## onParticleEmit

### <instance> onParticleEmit(callback, [context])

**Description:**

Sets a function to call for each newly emitted particle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | [Phaser.Types.GameObjects.Particles.ParticleEmitterCallback](../typedef/types-gameobjects-particles.md) | No | The function. |
| --- | --- | --- | --- |
| context | \* | Yes | The calling context. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2214](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2214)  
> Since: 3.0.0

---

## overlap

### <instance> overlap(target)

**Description:**

Takes either a Rectangle Geometry object or an Arcade Physics Body and tests

to see if it intersects with any currently alive Particle in this Emitter.

Overlapping particles are returned in an array, where you can perform further

processing on them. If nothing overlaps then the array will be empty.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Geom.Rectangle](geom-rectangle.md) | [Phaser.Physics.Arcade.Body](physics-arcade-body.md) | No | A Rectangle or Arcade Physics Body to check for intersection against all alive particles. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.GameObjects.Particles.Particle](gameobjects-particles-particle.md)> - An array of Particles that overlap with the given target.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2894](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2894)  
> Since: 3.60.0

---

## pause

### <instance> pause()

**Description:**

[Deactivates](gameobjects-particles-particleemitter.md) the emitter.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2431](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2431)  
> Since: 3.0.0

---

## preDestroy

### <instance> preDestroy()

**Description:**

Destroys this Particle Emitter and all Particles it owns.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L3922](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L3922)  
> Since: 3.60.0

---

## preUpdate

### <instance> preUpdate(time, delta)

**Description:**

Updates this emitter and its particles.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp as generated by the Request Animation Frame or SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time, in ms, elapsed since the last frame. |

**Fires:** [Phaser.GameObjects.Particles.Events#event:COMPLETE](../event/gameobjects-particles-events.md)

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2770](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2770)  
> Since: 3.0.0

---

## removeAllListeners

### <instance> removeAllListeners([event])

**Description:**

Remove all listeners, or those of the specified event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | Yes | The event name. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeDeathZone

### <instance> removeDeathZone(zone)

**Description:**

Removes the given Particle Death Zone from this Emitter.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| zone | [Phaser.GameObjects.Particles.Zones.DeathZone](gameobjects-particles-zones-deathzone.md) | No | The Death Zone that should be removed from this Emitter. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1771](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1771)  
> Since: 3.60.0

---

## removedFromScene

### <instance> removedFromScene()

**Description:**

This callback is invoked when this Game Object is removed from a Scene.

Can be overriden by custom Game Objects, but be aware of some Game Objects that

will use this, such as Sprites, to removed themselves from the Update List.

You can also listen for the `REMOVED_FROM_SCENE` event from this Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#removedFromScene](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L577](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L577)  
> Since: 3.50.0

---

## removeEmitZone

### <instance> removeEmitZone(zone)

**Description:**

Removes the given Particle Emission Zone from this Emitter.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| zone | [Phaser.GameObjects.Particles.Zones.EdgeZone](gameobjects-particles-zones-edgezone.md) | [Phaser.GameObjects.Particles.Zones.RandomZone](gameobjects-particles-zones-randomzone.md) | No | The Emission Zone that should be removed from this Emitter. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1879](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1879)  
> Since: 3.60.0

---

## removeFromDisplayList

### <instance> removeFromDisplayList()

**Description:**

Removes this Game Object from the Display List it is currently on.

A Game Object can only exist on one Display List at any given time, but may move freely removed

and added back at a later stage.

You can query which list it is on by looking at the `Phaser.GameObjects.GameObject#displayList` property.

If a Game Object isn't on any Display List, it will not be rendered. If you just wish to temporarly

disable it from rendering, consider using the `setVisible` method, instead.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object.

**Fires:** [Phaser.Scenes.Events#event:REMOVED\_FROM\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:REMOVED\_FROM\_SCENE](../event/gameobjects-events.md)

**Inherits:** [Phaser.GameObjects.GameObject#removeFromDisplayList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L760](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L760)  
> Since: 3.53.0

---

## removeFromUpdateList

### <instance> removeFromUpdateList()

**Description:**

Removes this Game Object from the Scene's Update List.

When a Game Object is on the Update List, it will have its `preUpdate` method called

every game frame. Calling this method will remove it from the list, preventing this.

Removing a Game Object from the Update List will stop most internal functions working.

For example, removing a Sprite from the Update List will prevent it from being able to

run animations.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.GameObject#removeFromUpdateList](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L798](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L798)  
> Since: 3.53.0

---

## removeInteractive

### <instance> removeInteractive([resetCursor])

**Description:**

If this Game Object has previously been enabled for input, this will queue it

for removal, causing it to no longer be interactive. The removal happens on

the next game step, it is not immediate.

The Interactive Object that was assigned to this Game Object will be destroyed,

removed from the Input Manager and cleared from this Game Object.

If you wish to re-enable this Game Object at a later date you will need to

re-create its InteractiveObject by calling `setInteractive` again.

If you wish to only temporarily stop an object from receiving input then use

`disableInteractive` instead, as that toggles the interactive state, where-as

this erases it completely.

If you wish to resize a hit area, don't remove and then set it as being

interactive. Instead, access the hitarea object directly and resize the shape

being used. I.e.: `sprite.input.hitArea.setSize(width, height)` (assuming the

shape is a Rectangle, which it is by default.)

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetCursor | boolean | Yes | false | Should the currently active Input cursor, if any, be reset to the default cursor? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#removeInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L519](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L519)  
> Since: 3.7.0

---

## removeListener

### <instance> removeListener(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## removeParticleProcessor

### <instance> removeParticleProcessor(processor)

**Description:**

Removes a Particle Processor from this Emitter.

The Processor must belong to this Emitter to be removed.

It is not destroyed when removed, allowing you to move it to another Emitter Manager,

so if you no longer require it you should call its `destroy` method directly.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| processor | T | No | The Particle Processor to remove from this Emitter Manager. |
| --- | --- | --- | --- |

**Returns:** T - The Particle Processor that was removed, or null if it could not be found.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2065](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2065)  
> Since: 3.60.0

---

## removePostPipeline

### <instance> removePostPipeline(pipeline)

**Description:**

Removes a type of Post Pipeline instances from this Game Object, based on the given name, and destroys them.

If you wish to remove all Post Pipelines use the `resetPostPipeline` method instead.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) | No | The string-based name of the pipeline, or a pipeline class. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#removePostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L299)  
> Since: 3.60.0

---

## reserve

### <instance> reserve(count)

**Description:**

Creates inactive particles and adds them to this emitter's pool.

If `ParticleEmitter.maxParticles` is set it will limit the

value passed to this method to make sure it's not exceeded.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| count | number | No | The number of particles to create. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2121)  
> Since: 3.0.0

---

## resetCounters

### <instance> resetCounters(frequency, on)

**Description:**

Resets the internal counter trackers.

You shouldn't ever need to call this directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| frequency | number | No | The frequency counter. |
| --- | --- | --- | --- |
| on | boolean | No | Set the complete flag. |

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1153)  
> Since: 3.60.0

---

## resetPipeline

### <instance> resetPipeline([resetData])

**Description:**

Resets the WebGL Pipeline of this Game Object back to the default it was created with.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetData | boolean | Yes | false | Reset the `pipelineData` object to being an empty object? |
| --- | --- | --- | --- | --- |

**Returns:** boolean - `true` if the pipeline was reset successfully, otherwise `false`.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#resetPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L176)  
> Since: 3.0.0

---

## resetPostPipeline

### <instance> resetPostPipeline([resetData])

**Description:**

Resets the WebGL Post Pipelines of this Game Object. It does this by calling

the `destroy` method on each post pipeline and then clearing the local array.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| resetData | boolean | Yes | false | Reset the `postPipelineData` object to being an empty object? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#resetPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L269](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L269)  
> Since: 3.60.0

---

## resume

### <instance> resume()

**Description:**

[Activates](gameobjects-particles-particleemitter.md) the emitter.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2446](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2446)  
> Since: 3.0.0

---

## setAbove

### <instance> setAbove(gameObject)

**Description:**

Move this Game Object so that it appears above the given Game Object.

This means it will render immediately after the other object in the display list.

Both objects must belong to the same display list, or parent container.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that this Game Object will be moved to be above. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setAbove](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L139)  
> Since: 3.85.0

---

## setActive

### <instance> setActive(value)

**Description:**

Sets the `active` property of this Game Object and returns this Game Object for further chaining.

A Game Object with its `active` property set to `true` will be updated by the Scenes UpdateList.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | True if this Game Object should be set as active, false if not. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setActive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L216)  
> Since: 3.0.0

---

## setAlpha

### <instance> setAlpha([value])

**Description:**

Set the Alpha level of this Game Object. The alpha controls the opacity of the Game Object as it renders.

Alpha values are provided as a float between 0, fully transparent, and 1, fully opaque.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 1 | The alpha value applied across the whole Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.AlphaSingle#setAlpha](../namespace/gameobjects-components-alphasingle.md)

> Source: [src/gameobjects/components/AlphaSingle.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/AlphaSingle.js#L48)  
> Since: 3.0.0

---

## setAngle

### <instance> setAngle([degrees])

**Description:**

Sets the angle of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| degrees | number | Yes | 0 | The rotation of this Game Object, in degrees. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setAngle](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L364](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L364)  
> Since: 3.0.0

---

## setAnim

### <instance> setAnim(anims, [pickRandom], [quantity])

**Description:**

Sets a pattern for assigning animations to emitted particles. The `anims` configuration can be any of:

anim: 'red'

anim: [ 'red', 'green', 'blue', 'pink', 'white' ]

anim: { anims: [ 'red', 'green', 'blue', 'pink', 'white' ], [cycle: bool], [quantity: int] }

Call this method at least once before any particles are created, or set `anim` in the Particle Emitter's configuration when creating the Emitter.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| anims | string | Array.<string> | [Phaser.Types.GameObjects.Particles.ParticleEmitterAnimConfig](../typedef/types-gameobjects-particles.md) | No |  |
| --- | --- | --- | --- | --- |
| pickRandom | boolean | Yes | true | Whether animations should be assigned at random from `anims`. If a config object is given, this parameter is ignored. |
| quantity | number | Yes | 1 | The number of consecutive particles that will receive each animation. If a config object is given, this parameter is ignored. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1373](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1373)  
> Since: 3.60.0

---

## setBelow

### <instance> setBelow(gameObject)

**Description:**

Move this Game Object so that it appears below the given Game Object.

This means it will render immediately under the other object in the display list.

Both objects must belong to the same display list, or parent container.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that this Game Object will be moved to be below. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setBelow](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L167)  
> Since: 3.85.0

---

## setBlendMode

### <instance> setBlendMode(value)

**Description:**

Sets the Blend Mode being used by this Game Object.

This can be a const, such as `Phaser.BlendModes.SCREEN`, or an integer, such as 4 (for Overlay)

Under WebGL only the following Blend Modes are available:

* NORMAL
* ADD
* MULTIPLY
* SCREEN
* ERASE (only works when rendering to a framebuffer, like a Render Texture)

Canvas has more available depending on browser support.

You can also create your own custom Blend Modes in WebGL.

Blend modes have different effects under Canvas and WebGL, and from browser to browser, depending

on support. Blend Modes also cause a WebGL batch flush should it encounter a new blend mode. For these

reasons try to be careful about the construction of your Scene and the frequency in which blend modes

are used.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | [Phaser.BlendModes](../namespace/blendmodes.md) | number | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.BlendMode#setBlendMode](../namespace/gameobjects-components-blendmode.md)

> Source: [src/gameobjects/components/BlendMode.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/BlendMode.js#L80)  
> Since: 3.0.0

---

## setConfig

### <instance> setConfig(config)

**Description:**

Takes an Emitter Configuration file and resets this Emitter, using any

properties defined in the config to then set it up again.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](../typedef/types-gameobjects-particles.md) | No | Settings for this emitter. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L936](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L936)  
> Since: 3.60.0

---

## setData

### <instance> setData(key, [data])

**Description:**

Allows you to store a key value pair within this Game Objects Data Manager.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

```
Copy
sprite.setData('name', 'Red Gem Stone');


```

You can also pass in an object of key value pairs as the first argument:

```
Copy
sprite.setData({ name: 'Red Gem Stone', level: 2, owner: 'Link', gold: 50 });


```

To get a value back again you can call `getData`:

```
Copy
sprite.getData('gold');


```

Or you can access the value directly via the `values` property, where it works like any other variable:

```
Copy
sprite.data.values.gold += 50;


```

When the value is first set, a `setdata` event is emitted from this Game Object.

If the key already exists, a `changedata` event is emitted instead, along an event named after the key.

For example, if you updated an existing key called `PlayerLives` then it would emit the event `changedata-PlayerLives`.

These events will be emitted regardless if you use this method to set the value, or the direct `values` setter.

Please note that the data keys are case-sensitive and must be valid JavaScript Object property strings.

This means the keys `gold` and `Gold` are treated as two unique values within the Data Manager.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | object | No | The key to set the value for. Or an object of key value pairs. If an object the `data` argument is ignored. |
| --- | --- | --- | --- |
| data | \* | Yes | The value to set for the given key. If an object is provided as the key this argument is ignored. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L295)  
> Since: 3.0.0

---

## setDataEnabled

### <instance> setDataEnabled()

**Description:**

Adds a Data Manager component to this Game Object.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setDataEnabled](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L276)  
> Since: 3.0.0

---

## setDepth

### <instance> setDepth(value)

**Description:**

The depth of this Game Object within the Scene.

The depth is also known as the 'z-index' in some environments, and allows you to change the rendering order

of Game Objects, without actually moving their position in the display list.

The default depth is zero. A Game Object with a higher depth

value will always render in front of one with a lower value.

Setting the depth will queue a depth sort event within the Scene.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The depth of this Game Object. Ensure this value is only ever a number data-type. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L64)  
> Since: 3.0.0

---

## setEmitterAngle

### <instance> setEmitterAngle(value)

**Description:**

Sets the angle of a [Phaser.GameObjects.Particles.ParticleEmitter#radial](gameobjects-particles-particleemitter.md) particle stream.

The value is given in degrees using Phaser's right-handed coordinate system.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md) | No | The angle of the initial velocity of emitted particles, in degrees. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1626](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1626)  
> Since: 3.0.0

---

## setEmitterFrame

### <instance> setEmitterFrame(frames, [pickRandom], [quantity])

**Description:**

Sets a pattern for assigning texture frames to emitted particles. The `frames` configuration can be any of:

frame: 0

frame: 'red'

frame: [ 0, 1, 2, 3 ]

frame: [ 'red', 'green', 'blue', 'pink', 'white' ]

frame: { frames: [ 'red', 'green', 'blue', 'pink', 'white' ], [cycle: bool], [quantity: int] }

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| frames | array | string | number | [Phaser.Types.GameObjects.Particles.ParticleEmitterFrameConfig](../typedef/types-gameobjects-particles.md) | No |
| --- | --- | --- | --- | --- |
| pickRandom | boolean | Yes | true | Whether frames should be assigned at random from `frames`. |
| quantity | number | Yes | 1 | The number of consecutive particles that will receive each frame. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1265](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1265)  
> Since: 3.0.0

---

## setEmitZone

### <instance> setEmitZone(zone)

**Description:**

Changes the currently active Emission Zone. The zones should have already

been added to this Emitter either via the emitter config, or the

`addEmitZone` method.

Call this method by passing either a numeric zone index value, or

the zone instance itself.

Prior to v3.60 an Emitter could only have a single Emit Zone and this

method was how you set it. From 3.60 and up it now performs a different

function and swaps between all available active zones.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| zone | number | [Phaser.GameObjects.Particles.Zones.EdgeZone](gameobjects-particles-zones-edgezone.md) | [Phaser.GameObjects.Particles.Zones.RandomZone](gameobjects-particles-zones-randomzone.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1994](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1994)  
> Since: 3.0.0

---

## setFrame

### <instance> setFrame(frame, [updateSize], [updateOrigin])

**Description:**

Sets the frame this Game Object will use to render with.

If you pass a string or index then the Frame has to belong to the current Texture being used

by this Game Object.

If you pass a Frame instance, then the Texture being used by this Game Object will also be updated.

Calling `setFrame` will modify the `width` and `height` properties of your Game Object.

It will also change the `origin` if the Frame has a custom pivot point, as exported from packages like Texture Packer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | No |  |
| --- | --- | --- | --- | --- |
| updateSize | boolean | Yes | true | Should this call adjust the size of the Game Object? |
| updateOrigin | boolean | Yes | true | Should this call adjust the origin of the Game Object? |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Texture#setFrame](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L75)  
> Since: 3.0.0

---

## setFrequency

### <instance> setFrequency(frequency, [quantity])

**Description:**

Sets the emitter's [Phaser.GameObjects.Particles.ParticleEmitter#frequency](gameobjects-particles-particleemitter.md)

and [Phaser.GameObjects.Particles.ParticleEmitter#quantity](gameobjects-particles-particleemitter.md).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| frequency | number | No | The time interval (>= 0) of each flow cycle, in ms; or -1 to put the emitter in explosion mode. |
| --- | --- | --- | --- |
| quantity | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md) | Yes | The number of particles to release at each flow cycle or explosion. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1679](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1679)  
> Since: 3.0.0

---

## setInteractive

### <instance> setInteractive([hitArea], [callback], [dropZone])

**Description:**

Pass this Game Object to the Input Manager to enable it for Input.

Input works by using hit areas, these are nearly always geometric shapes, such as rectangles or circles, that act as the hit area

for the Game Object. However, you can provide your own hit area shape and callback, should you wish to handle some more advanced

input detection.

If no arguments are provided it will try and create a rectangle hit area based on the texture frame the Game Object is using. If

this isn't a texture-bound object, such as a Graphics or BitmapText object, this will fail, and you'll need to provide a specific

shape for it to use.

You can also provide an Input Configuration Object as the only argument to this method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| hitArea | [Phaser.Types.Input.InputConfiguration](../typedef/types-input.md) | any | Yes |  | Either an input configuration object, or a geometric shape that defines the hit area for the Game Object. If not given it will try to create a Rectangle based on the texture frame. |
| --- | --- | --- | --- | --- |
| callback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes |  | The callback that determines if the pointer is within the Hit Area shape or not. If you provide a shape you must also provide a callback. |
| dropZone | boolean | Yes | false | Should this Game Object be treated as a drop zone target? |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setInteractive](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L456](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L456)  
> Since: 3.0.0

---

## setMask

### <instance> setMask(mask)

**Description:**

Sets the mask that this Game Object will use to render with.

The mask must have been previously created and can be either a GeometryMask or a BitmapMask.

Note: Bitmap Masks only work on WebGL. Geometry Masks work on both WebGL and Canvas.

If a mask is already set on this Game Object it will be immediately replaced.

Masks are positioned in global space and are not relative to the Game Object to which they

are applied. The reason for this is that multiple Game Objects can all share the same mask.

Masks have no impact on physics or input detection. They are purely a rendering component

that allows you to limit what is visible during the render pass.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mask | [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) | [Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md) | No | The mask this Game Object will use when rendering. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Mask#setMask](../namespace/gameobjects-components-mask.md)

> Source: [src/gameobjects/components/Mask.js#L28](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Mask.js#L28)  
> Since: 3.6.2

---

## setName

### <instance> setName(value)

**Description:**

Sets the `name` property of this Game Object and returns this Game Object for further chaining.

The `name` property is not populated by Phaser and is presented for your own use.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | No | The name to be given to this Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setName](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L234)  
> Since: 3.0.0

---

## setParticleAlpha

### <instance> setParticleAlpha(value)

**Description:**

Sets the opacity (alpha) of emitted particles.

You can also set the alpha of the entire emitter via `setAlpha`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md) | [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](../typedef/types-gameobjects-particles.md) | No | A value between 0 (transparent) and 1 (opaque). |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1587](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1587)  
> Since: 3.60.0

---

## setParticleGravity

### <instance> setParticleGravity(x, y)

**Description:**

Sets the gravity applied to emitted particles.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | Horizontal acceleration due to gravity, in pixels per second squared. Set to zero for no gravity. |
| --- | --- | --- | --- |
| y | number | No | Vertical acceleration due to gravity, in pixels per second squared. Set to zero for no gravity. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1568](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1568)  
> Since: 3.60.0

---

## setParticleLifespan

### <instance> setParticleLifespan(value)

**Description:**

Sets the lifespan of newly emitted particles in milliseconds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md) | No | The lifespan of a particle, in ms. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1645](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1645)  
> Since: 3.60.0

---

## setParticleScale

### <instance> setParticleScale([x], [y])

**Description:**

Sets the vertical and horizontal scale of the emitted particles.

You can also set the scale of the entire emitter via `setScale`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 1 | The horizontal scale of the emitted Particles. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scale of emitted Particles. If not set it will use the `x` value. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1544](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1544)  
> Since: 3.60.0

---

## setParticleSpeed

### <instance> setParticleSpeed(x, [y])

**Description:**

Sets the initial radial speed of emitted particles.

Changes the emitter to radial mode.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal speed of the emitted Particles. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical speed of emitted Particles. If not set it will use the `x` value. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1510](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1510)  
> Since: 3.60.0

---

## setParticleTint

### <instance> setParticleTint(value)

**Description:**

Sets the color tint of emitted particles.

This is a WebGL only feature.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md) | [Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](../typedef/types-gameobjects-particles.md) | No | A value between 0 and 0xffffff. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1606](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1606)  
> Since: 3.60.0

---

## setPipeline

### <instance> setPipeline(pipeline, [pipelineData], [copyData])

**Description:**

Sets the main WebGL Pipeline of this Game Object.

Also sets the `pipelineData` property, if the parameter is given.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| pipeline | string | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | No |  | Either the string-based name of the pipeline, or a pipeline instance to set. |
| --- | --- | --- | --- | --- |
| pipelineData | object | Yes |  | Optional pipeline data object that is set in to the `pipelineData` property of this Game Object. |
| copyData | boolean | Yes | true | Should the pipeline data object be *deep copied* into the `pipelineData` property of this Game Object? If `false` it will be set by reference instead. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#setPipeline](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L100)  
> Since: 3.0.0

---

## setPipelineData

### <instance> setPipelineData(key, [value])

**Description:**

Adds an entry to the `pipelineData` object belonging to this Game Object.

If the 'key' already exists, its value is updated. If it doesn't exist, it is created.

If `value` is undefined, and `key` exists, `key` is removed from the data object.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the pipeline data to set, update, or delete. |
| --- | --- | --- | --- |
| value | any | Yes | The value to be set with the key. If `undefined` then `key` will be deleted from the object. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Pipeline#setPipelineData](../namespace/gameobjects-components-pipeline.md)

> Source: [src/gameobjects/components/Pipeline.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Pipeline.js#L144)  
> Since: 3.50.0

---

## setPosition

### <instance> setPosition([x], [y], [z], [w])

**Description:**

Sets the position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The y position of this Game Object. If not set it will use the `x` value. |
| z | number | Yes | 0 | The z position of this Game Object. |
| w | number | Yes | 0 | The w position of this Game Object. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L265](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L265)  
> Since: 3.0.0

---

## setPostPipeline

### <instance> setPostPipeline(pipelines, [pipelineData], [copyData])

**Description:**

Sets one, or more, Post Pipelines on this Game Object.

Post Pipelines are invoked after this Game Object has rendered to its target and

are commonly used for post-fx.

The post pipelines are appended to the `postPipelines` array belonging to this

Game Object. When the renderer processes this Game Object, it iterates through the post

pipelines in the order in which they appear in the array. If you are stacking together

multiple effects, be aware that the order is important.

If you call this method multiple times, the new pipelines will be appended to any existing

post pipelines already set. Use the `resetPostPipeline` method to clear them first, if required.

You can optionally also set the `postPipelineData` property, if the parameter is given.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| pipelines | string | Array.<string> | function | Array.<function()> | [Phaser.Renderer.WebGL.Pipelines.PostFXPipeline](renderer-webgl-pipelines-postfxpipeline.md) |
| --- | --- | --- | --- | --- |
| pipelineData | object | Yes |  | Optional pipeline data object that is set in to the `postPipelineData` property of this Game Object. |
| copyData | boolean | Yes | true | Should the pipeline data object be *deep copied* into the `postPipelineData` property of this Game Object? If `false` it will be set by reference instead. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#setPostPipeline](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L140)  
> Since: 3.60.0

---

## setPostPipelineData

### <instance> setPostPipelineData(key, [value])

**Description:**

Adds an entry to the `postPipelineData` object belonging to this Game Object.

If the 'key' already exists, its value is updated. If it doesn't exist, it is created.

If `value` is undefined, and `key` exists, `key` is removed from the data object.

**Tags:**

* webglOnly

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the pipeline data to set, update, or delete. |
| --- | --- | --- | --- |
| value | any | Yes | The value to be set with the key. If `undefined` then `key` will be deleted from the object. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.PostPipeline#setPostPipelineData](../namespace/gameobjects-components-postpipeline.md)

> Source: [src/gameobjects/components/PostPipeline.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/PostPipeline.js#L205)  
> Since: 3.60.0

---

## setQuantity

### <instance> setQuantity(quantity)

**Description:**

Sets the number of particles released at each flow cycle or explosion.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| quantity | [Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](../typedef/types-gameobjects-particles.md) | No | The number of particles to release at each flow cycle or explosion. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1662](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1662)  
> Since: 3.0.0

---

## setRadial

### <instance> setRadial([value])

**Description:**

Turns [Phaser.GameObjects.Particles.ParticleEmitter#radial](gameobjects-particles-particleemitter.md) particle movement on or off.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | Radial mode (true) or point mode (true). |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1440](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1440)  
> Since: 3.0.0

---

## setRandomPosition

### <instance> setRandomPosition([x], [y], [width], [height])

**Description:**

Sets the position of this Game Object to be a random position within the confines of

the given area.

If no area is specified a random position between 0 x 0 and the game width x height is used instead.

The position does not factor in the size of this Game Object, meaning that only the origin is

guaranteed to be within the area.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of the top-left of the random area. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y position of the top-left of the random area. |
| width | number | Yes |  | The width of the random area. |
| height | number | Yes |  | The height of the random area. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRandomPosition](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L313](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L313)  
> Since: 3.8.0

---

## setRotation

### <instance> setRotation([radians])

**Description:**

Sets the rotation of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radians | number | Yes | 0 | The rotation of this Game Object, in radians. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setRotation](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L345](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L345)  
> Since: 3.0.0

---

## setScale

### <instance> setScale([x], [y])

**Description:**

Sets the scale of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 1 | The horizontal scale of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scale of this Game Object. If not set it will use the `x` value. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setScale](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L383](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L383)  
> Since: 3.0.0

---

## setScrollFactor

### <instance> setScrollFactor(x, [y])

**Description:**

Sets the scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal scroll factor of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scroll factor of this Game Object. If not set it will use the `x` value. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#setScrollFactor](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L64)  
> Since: 3.0.0

---

## setSortCallback

### <instance> setSortCallback([callback])

**Description:**

Sets a callback to be used to sort the particles before rendering each frame.

This allows you to define your own logic and behavior in the callback.

The callback will be sent two parameters: the two Particles being compared,

and must adhere to the criteria of the `compareFn` in `Array.sort`:

<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/sort#description>

Call this method with no parameters to reset the sort callback.

Setting your own callback will override both the `particleBringToTop` and

`sortProperty` settings of this Emitter.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | [Phaser.Types.GameObjects.Particles.ParticleSortCallback](../typedef/types-gameobjects-particles.md) | Yes | The callback to invoke when the particles are sorted. Leave undefined to reset to the default. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2494](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2494)  
> Since: 3.60.0

---

## setSortProperty

### <instance> setSortProperty([property], [ascending])

**Description:**

Set the property by which active particles are sorted prior to be rendered.

It allows you to control the rendering order of the particles.

This can be any valid property of the `Particle` class, such as `y`, `alpha`

or `lifeT`.

The 'alive' particles array is sorted in place each game frame. Setting a

sort property will override the `particleBringToTop` setting.

If you wish to use your own sorting function, see `setSortCallback` instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| property | string | Yes |  | The property on the `Particle` class to sort by. |
| --- | --- | --- | --- | --- |
| ascending | boolean | Yes | true | Should the particles be sorted in ascending or descending order? |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2461](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2461)  
> Since: 3.60.0

---

## setState

### <instance> setState(value)

**Description:**

Sets the current state of this Game Object.

Phaser itself will never modify the State of a Game Object, although plugins may do so.

For example, a Game Object could change from a state of 'moving', to 'attacking', to 'dead'.

The state value should typically be an integer (ideally mapped to a constant

in your game code), but could also be a string. It is recommended to keep it light and simple.

If you need to store complex data about your Game Object, look at using the Data Component instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | string | No | The state of the Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#setState](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L252)  
> Since: 3.16.0

---

## setTexture

### <instance> setTexture(key, [frame], [updateSize], [updateOrigin])

**Description:**

Sets the texture and frame this Game Object will use to render with.

Textures are referenced by their string-based keys, as stored in the Texture Manager.

Calling this method will modify the `width` and `height` properties of your Game Object.

It will also change the `origin` if the Frame has a custom pivot point, as exported from packages like Texture Packer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Textures.Texture](textures-texture.md) | No |  | The key of the texture to be used, as stored in the Texture Manager, or a Texture instance. |
| --- | --- | --- | --- | --- |
| frame | string | number | Yes |  | The name or index of the frame within the Texture. |
| updateSize | boolean | Yes | true | Should this call adjust the size of the Game Object? |
| updateOrigin | boolean | Yes | true | Should this call change the origin of the Game Object? |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Texture#setTexture](../namespace/gameobjects-components-texture.md)

> Source: [src/gameobjects/components/Texture.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L49)  
> Since: 3.0.0

---

## setToBack

### <instance> setToBack()

**Description:**

Sets this Game Object to the back of the display list, or the back of its parent container.

Being at the back means it will render below everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToBack](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L115)  
> Since: 3.85.0

---

## setToTop

### <instance> setToTop()

**Description:**

Sets this Game Object to be at the top of the display list, or the top of its parent container.

Being at the top means it will render on-top of everything else.

This method does not change this Game Objects `depth` value, it simply alters its list position.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Depth#setToTop](../namespace/gameobjects-components-depth.md)

> Source: [src/gameobjects/components/Depth.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Depth.js#L91)  
> Since: 3.85.0

---

## setVisible

### <instance> setVisible(value)

**Description:**

Sets the visibility of this Game Object.

An invisible Game Object will skip rendering, but will still process update logic.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The visible state of the Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Visible#setVisible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L63)  
> Since: 3.0.0

---

## setW

### <instance> setW([value])

**Description:**

Sets the w position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The w position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setW](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L465](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L465)  
> Since: 3.0.0

---

## setX

### <instance> setX([value])

**Description:**

Sets the x position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The x position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setX](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L405](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L405)  
> Since: 3.0.0

---

## setY

### <instance> setY([value])

**Description:**

Sets the y position of this Game Object.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The y position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setY](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L424](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L424)  
> Since: 3.0.0

---

## setZ

### <instance> setZ([value])

**Description:**

Sets the z position of this Game Object.

Note: The z position does not control the rendering order of 2D Game Objects. Use

[Phaser.GameObjects.Components.Depth#setDepth](../namespace/gameobjects-components-depth.md) instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The z position of this Game Object. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Transform#setZ](../namespace/gameobjects-components-transform.md)

> Source: [src/gameobjects/components/Transform.js#L443](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Transform.js#L443)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## start

### <instance> start([advance], [duration])

**Description:**

Turns [Phaser.GameObjects.Particles.ParticleEmitter#on](gameobjects-particles-particleemitter.md) the emitter and resets the flow counter.

If this emitter is in flow mode (frequency >= 0; the default), the particle flow will start (or restart).

If this emitter is in explode mode (frequency = -1), nothing will happen.

Use [Phaser.GameObjects.Particles.ParticleEmitter#explode](gameobjects-particles-particleemitter.md) or [Phaser.GameObjects.Particles.ParticleEmitter#flow](gameobjects-particles-particleemitter.md) instead.

Calling this method will emit the `START` event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| advance | number | Yes | 0 | Advance this number of ms in time through the emitter. |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 0 | Limit this emitter to only emit particles for the given number of ms. Setting this parameter will override any duration already set in the Emitter configuration object. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

**Fires:** [Phaser.GameObjects.Particles.Events#event:START](../event/gameobjects-particles-events.md)

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2351](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2351)  
> Since: 3.0.0

---

## startFollow

### <instance> startFollow(target, [offsetX], [offsetY], [trackVisible])

**Description:**

Continuously moves the particle origin to follow a Game Object's position.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No |  | The Object to follow. |
| --- | --- | --- | --- | --- |
| offsetX | number | Yes | 0 | Horizontal offset of the particle origin from the Game Object. |
| offsetY | number | Yes | 0 | Vertical offset of the particle origin from the Game Object. |
| trackVisible | boolean | Yes | false | Whether the emitter's visible state will track the target's visible state. |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1178](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1178)  
> Since: 3.0.0

---

## stop

### <instance> stop([kill])

**Description:**

Turns [off](gameobjects-particles-particleemitter.md) the emitter and

stops it from emitting further particles. Currently alive particles will remain

active until they naturally expire unless you set the `kill` parameter to `true`.

Calling this method will emit the `STOP` event. When the final particle has

expired the `COMPLETE` event will be emitted.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| kill | boolean | Yes | false | Kill all particles immediately (true), or leave them to die after their lifespan expires? (false, the default) |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

**Fires:** [Phaser.GameObjects.Particles.Events#event:STOP](../event/gameobjects-particles-events.md)

> Source: [src/gameobjects/particles/ParticleEmitter.js#L2396](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L2396)  
> Since: 3.11.0

---

## stopFollow

### <instance> stopFollow()

**Description:**

Stops following a Game Object.

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1204](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1204)  
> Since: 3.0.0

---

## toggleData

### <instance> toggleData(key)

**Description:**

Toggle a boolean value for the given key within this Game Objects Data Manager. If the key doesn't already exist in the Data Manager then it is toggled from false.

If the Game Object has not been enabled for data (via `setDataEnabled`) then it will be enabled

before setting the value.

If the key doesn't already exist in the Data Manager then it is created.

When the value is first set, a `setdata` event is emitted from this Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key to toggle the value for. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This GameObject.

**Inherits:** [Phaser.GameObjects.GameObject#toggleData](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L387)  
> Since: 3.23.0

---

## toJSON

### <instance> toJSON()

**Description:**

Creates a description of this emitter suitable for JSON serialization.

**Overrides:** Phaser.GameObjects.GameObject#toJSON

**Returns:** [Phaser.Types.GameObjects.JSONGameObject](../typedef/types-gameobjects.md) - A JSON representation of the Game Object.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1102)  
> Since: 3.0.0

---

## update

### <instance> update([args])

**Description:**

To be overridden by custom GameObjects. Allows base objects to be used in a Pool.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| args | \* | Yes | args |
| --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.GameObject#update](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L592](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L592)  
> Since: 3.0.0

---

## updateConfig

### <instance> updateConfig(config)

**Description:**

Takes an existing Emitter Configuration file and updates this Emitter.

Existing properties are overriden while new properties are added. The

updated configuration is then passed to the `setConfig` method to reset

the Emitter with the updated configuration.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](../typedef/types-gameobjects-particles.md) | No | Settings for this emitter. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Particles.ParticleEmitter](gameobjects-particles-particleemitter.md) - This Particle Emitter.

> Source: [src/gameobjects/particles/ParticleEmitter.js#L1072](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/particles/ParticleEmitter.js#L1072)  
> Since: 3.85.0

---

## willRender

### <instance> willRender(camera)

**Description:**

Compares the renderMask with the renderFlags to see if this Game Object will render or not.

Also checks the Game Object against the given Cameras exclusion list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera to check against this Game Object. |
| --- | --- | --- | --- |

**Returns:** boolean - True if the Game Object should be rendered, otherwise false.

**Inherits:** [Phaser.GameObjects.GameObject#willRender](gameobjects-gameobject.md)

> Source: [src/gameobjects/GameObject.js#L617](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/GameObject.js#L617)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [An explicit static value:](#an-explicit-static-value)
* [A random value:](#a-random-value)
* [A custom callback:](#a-custom-callback)
* [A start / end object:](#a-start--end-object)
* [A start / end random object:](#a-start--end-random-object)
* [An interpolation object:](#an-interpolation-object)
* [A stepped emitter object:](#a-stepped-emitter-object)
* [A stepped emitter object with yoyo:](#a-stepped-emitter-object-with-yoyo)
* [A min / max object:](#a-min--max-object)
* [A random object:](#a-random-object)
* [Custom onEmit and onUpdate callbacks:](#custom-onemit-and-onupdate-callbacks)
* [v3.55 Differences](#v355-differences)
* [Public Members](#public-members)

  + [acceleration](#acceleration)

    - [acceleration: boolean](#acceleration-boolean)
  + [accelerationX](#accelerationx)

    - [accelerationX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#accelerationx-phasertypesgameobjectsparticlesemitteroponemittype)
  + [accelerationY](#accelerationy)

    - [accelerationY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#accelerationy-phasertypesgameobjectsparticlesemitteroponemittype)
  + [active](#active)

    - [active: boolean](#active-boolean)
  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [angle](#angle)

    - [angle: number](#angle-number)
  + [animCounter](#animcounter)

    - [animCounter: number](#animcounter-number)
  + [animQuantity](#animquantity)

    - [animQuantity: number](#animquantity-number)
  + [anims](#anims)

    - [anims: Array.<string>](#anims-arraystring)
  + [blendMode](#blendmode)

    - [blendMode: Phaser.BlendModes, string, number](#blendmode-phaserblendmodes-string-number)
  + [body](#body)

    - [body: Phaser.Physics.Arcade.Body, Phaser.Physics.Arcade.StaticBody, MatterJS.BodyType](#body-phaserphysicsarcadebody-phaserphysicsarcadestaticbody-matterjsbodytype)
  + [bounce](#bounce)

    - [bounce: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#bounce-phasertypesgameobjectsparticlesemitteroponemittype)
  + [cameraFilter](#camerafilter)

    - [cameraFilter: number](#camerafilter-number)
  + [colorEase](#colorease)

    - [colorEase: string](#colorease-string)
  + [completeFlag](#completeflag)

    - [completeFlag: boolean](#completeflag-boolean)
  + [config](#config)

    - [config: Phaser.Types.GameObjects.Particles.ParticleEmitterConfig](#config-phasertypesgameobjectsparticlesparticleemitterconfig)
  + [currentAnim](#currentanim)

    - [currentAnim: number](#currentanim-number)
  + [currentFrame](#currentframe)

    - [currentFrame: number](#currentframe-number)
  + [data](#data)

    - [data: Phaser.Data.DataManager](#data-phaserdatadatamanager)
  + [deathCallback](#deathcallback)

    - [deathCallback: Phaser.Types.GameObjects.Particles.ParticleDeathCallback](#deathcallback-phasertypesgameobjectsparticlesparticledeathcallback)
  + [deathCallbackScope](#deathcallbackscope)

    - [deathCallbackScope: \*](#deathcallbackscope-)
  + [deathZones](#deathzones)

    - [deathZones: Array.<Phaser.GameObjects.Particles.Zones.DeathZone>](#deathzones-arrayphasergameobjectsparticleszonesdeathzone)
  + [defaultPipeline](#defaultpipeline)

    - [defaultPipeline: Phaser.Renderer.WebGL.WebGLPipeline](#defaultpipeline-phaserrendererwebglwebglpipeline)
  + [delay](#delay)

    - [delay: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#delay-phasertypesgameobjectsparticlesemitteroponemittype)
  + [depth](#depth)

    - [depth: number](#depth-number)
  + [displayList](#displaylist)

    - [displayList: Phaser.GameObjects.DisplayList, Phaser.GameObjects.Layer](#displaylist-phasergameobjectsdisplaylist-phasergameobjectslayer)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [elapsed](#elapsed)

    - [elapsed: number](#elapsed-number)
  + [emitCallback](#emitcallback)

    - [emitCallback: Phaser.Types.GameObjects.Particles.ParticleEmitterCallback](#emitcallback-phasertypesgameobjectsparticlesparticleemittercallback)
  + [emitCallbackScope](#emitcallbackscope)

    - [emitCallbackScope: \*](#emitcallbackscope-)
  + [emitting](#emitting)

    - [emitting: boolean](#emitting-boolean)
  + [emitZones](#emitzones)

    - [emitZones: Array.<Phaser.Types.GameObjects.Particles.EmitZoneObject>](#emitzones-arrayphasertypesgameobjectsparticlesemitzoneobject)
  + [flowCounter](#flowcounter)

    - [flowCounter: number](#flowcounter-number)
  + [follow](#follow)

    - [follow: Phaser.Types.Math.Vector2Like](#follow-phasertypesmathvector2like)
  + [followOffset](#followoffset)

    - [followOffset: Phaser.Math.Vector2](#followoffset-phasermathvector2)
  + [frame](#frame)

    - [frame: Phaser.Textures.Frame](#frame-phasertexturesframe)
  + [frameCounter](#framecounter)

    - [frameCounter: number](#framecounter-number)
  + [frameQuantity](#framequantity)

    - [frameQuantity: number](#framequantity-number)
  + [frames](#frames)

    - [frames: Array.<Phaser.Textures.Frame>](#frames-arrayphasertexturesframe)
  + [frequency](#frequency)

    - [frequency: number](#frequency-number)
  + [gravityX](#gravityx)

    - [gravityX: number](#gravityx-number)
  + [gravityY](#gravityy)

    - [gravityY: number](#gravityy-number)
  + [hasPostPipeline](#haspostpipeline)

    - [hasPostPipeline: boolean](#haspostpipeline-boolean)
  + [hasTransformComponent](#hastransformcomponent)

    - [hasTransformComponent: boolean](#hastransformcomponent-boolean)
  + [hold](#hold)

    - [hold: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#hold-phasertypesgameobjectsparticlesemitteroponemittype)
  + [ignoreDestroy](#ignoredestroy)

    - [ignoreDestroy: boolean](#ignoredestroy-boolean)
  + [input](#input)

    - [input: Phaser.Types.Input.InteractiveObject](#input-phasertypesinputinteractiveobject)
  + [lifespan](#lifespan)

    - [lifespan: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#lifespan-phasertypesgameobjectsparticlesemitteroponemittype)
  + [mask](#mask)

    - [mask: Phaser.Display.Masks.BitmapMask, Phaser.Display.Masks.GeometryMask](#mask-phaserdisplaymasksbitmapmask-phaserdisplaymasksgeometrymask)
  + [maxAliveParticles](#maxaliveparticles)

    - [maxAliveParticles: number](#maxaliveparticles-number)
  + [maxParticles](#maxparticles)

    - [maxParticles: number](#maxparticles-number)
  + [maxVelocityX](#maxvelocityx)

    - [maxVelocityX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#maxvelocityx-phasertypesgameobjectsparticlesemitteroponemittype)
  + [maxVelocityY](#maxvelocityy)

    - [maxVelocityY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#maxvelocityy-phasertypesgameobjectsparticlesemitteroponemittype)
  + [moveTo](#moveto)

    - [moveTo: boolean](#moveto-boolean)
  + [moveToX](#movetox)

    - [moveToX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#movetox-phasertypesgameobjectsparticlesemitteroponemittype)
  + [moveToY](#movetoy)

    - [moveToY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#movetoy-phasertypesgameobjectsparticlesemitteroponemittype)
  + [name](#name)

    - [name: string](#name-string)
  + [ops](#ops)

    - [ops: Phaser.Types.GameObjects.Particles.ParticleEmitterOps](#ops-phasertypesgameobjectsparticlesparticleemitterops)
  + [parentContainer](#parentcontainer)

    - [parentContainer: Phaser.GameObjects.Container](#parentcontainer-phasergameobjectscontainer)
  + [particleAlpha](#particlealpha)

    - [particleAlpha: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#particlealpha-phasertypesgameobjectsparticlesemitteroponemittype)
  + [particleAngle](#particleangle)

    - [particleAngle: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#particleangle-phasertypesgameobjectsparticlesemitteroponemittype)
  + [particleBringToTop](#particlebringtotop)

    - [particleBringToTop: boolean](#particlebringtotop-boolean)
  + [particleClass](#particleclass)

    - [particleClass: function](#particleclass-function)
  + [particleColor](#particlecolor)

    - [particleColor: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#particlecolor-phasertypesgameobjectsparticlesemitteroponemittype)
  + [particleRotate](#particlerotate)

    - [particleRotate: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#particlerotate-phasertypesgameobjectsparticlesemitteroponemittype)
  + [particleScaleX](#particlescalex)

    - [particleScaleX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#particlescalex-phasertypesgameobjectsparticlesemitteroponemittype)
  + [particleScaleY](#particlescaley)

    - [particleScaleY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#particlescaley-phasertypesgameobjectsparticlesemitteroponemittype)
  + [particleTint](#particletint)

    - [particleTint: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#particletint-phasertypesgameobjectsparticlesemitteroponemittype)
  + [particleX](#particlex)

    - [particleX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType, Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](#particlex-phasertypesgameobjectsparticlesemitteroponemittype-phasertypesgameobjectsparticlesemitteroponupdatetype)
  + [particleY](#particley)

    - [particleY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType, Phaser.Types.GameObjects.Particles.EmitterOpOnUpdateType](#particley-phasertypesgameobjectsparticlesemitteroponemittype-phasertypesgameobjectsparticlesemitteroponupdatetype)
  + [pipeline](#pipeline)

    - [pipeline: Phaser.Renderer.WebGL.WebGLPipeline](#pipeline-phaserrendererwebglwebglpipeline)
  + [pipelineData](#pipelinedata)

    - [pipelineData: object](#pipelinedata-object)
  + [postFX](#postfx)

    - [postFX: Phaser.GameObjects.Components.FX](#postfx-phasergameobjectscomponentsfx)
  + [postPipelineData](#postpipelinedata)

    - [postPipelineData: object](#postpipelinedata-object)
  + [postPipelines](#postpipelines)

    - [postPipelines: Array.<Phaser.Renderer.WebGL.Pipelines.PostFXPipeline>](#postpipelines-arrayphaserrendererwebglpipelinespostfxpipeline)
  + [preFX](#prefx)

    - [preFX: Phaser.GameObjects.Components.FX](#prefx-phasergameobjectscomponentsfx)
  + [processors](#processors)

    - [processors: Phaser.Structs.List.<Phaser.GameObjects.Particles.ParticleProcessor>](#processors-phaserstructslistphasergameobjectsparticlesparticleprocessor)
  + [quantity](#quantity)

    - [quantity: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#quantity-phasertypesgameobjectsparticlesemitteroponemittype)
  + [radial](#radial)

    - [radial: boolean](#radial-boolean)
  + [randomAnim](#randomanim)

    - [randomAnim: boolean](#randomanim-boolean)
  + [randomFrame](#randomframe)

    - [randomFrame: boolean](#randomframe-boolean)
  + [renderFlags](#renderflags)

    - [renderFlags: number](#renderflags-number)
  + [rotation](#rotation)

    - [rotation: number](#rotation-number)
  + [scale](#scale)

    - [scale: number](#scale-number)
  + [scaleX](#scalex)

    - [scaleX: number](#scalex-number)
  + [scaleY](#scaley)

    - [scaleY: number](#scaley-number)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [scrollFactorX](#scrollfactorx)

    - [scrollFactorX: number](#scrollfactorx-number)
  + [scrollFactorY](#scrollfactory)

    - [scrollFactorY: number](#scrollfactory-number)
  + [skipping](#skipping)

    - [skipping: boolean](#skipping-boolean)
  + [sortCallback](#sortcallback)

    - [sortCallback: Phaser.Types.GameObjects.Particles.ParticleSortCallback](#sortcallback-phasertypesgameobjectsparticlesparticlesortcallback)
  + [sortOrderAsc](#sortorderasc)

    - [sortOrderAsc: boolean](#sortorderasc-boolean)
  + [sortProperty](#sortproperty)

    - [sortProperty: string](#sortproperty-string)
  + [speed](#speed)

    - [speed: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#speed-phasertypesgameobjectsparticlesemitteroponemittype)
  + [speedX](#speedx)

    - [speedX: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#speedx-phasertypesgameobjectsparticlesemitteroponemittype)
  + [speedY](#speedy)

    - [speedY: Phaser.Types.GameObjects.Particles.EmitterOpOnEmitType](#speedy-phasertypesgameobjectsparticlesemitteroponemittype)
  + [state](#state)

    - [state: number, string](#state-number-string)
  + [stopAfter](#stopafter)

    - [stopAfter: number](#stopafter-number)
  + [stopCounter](#stopcounter)

    - [stopCounter: number](#stopcounter-number)
  + [tabIndex](#tabindex)

    - [tabIndex: number](#tabindex-number)
  + [texture](#texture)

    - [texture: Phaser.Textures.Texture, Phaser.Textures.CanvasTexture](#texture-phasertexturestexture-phasertexturescanvastexture)
  + [timeScale](#timescale)

    - [timeScale: number](#timescale-number)
  + [tintFill](#tintfill)

    - [tintFill: boolean](#tintfill-boolean)
  + [trackVisible](#trackvisible)

    - [trackVisible: boolean](#trackvisible-boolean)
  + [type](#type)

    - [type: string](#type-string)
  + [viewBounds](#viewbounds)

    - [viewBounds: Phaser.Geom.Rectangle](#viewbounds-phasergeomrectangle)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
  + [w](#w)

    - [w: number](#w-number)
  + [worldMatrix](#worldmatrix)

    - [worldMatrix: Phaser.GameObjects.Components.TransformMatrix](#worldmatrix-phasergameobjectscomponentstransformmatrix)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
  + [z](#z)

    - [z: number](#z-number)
  + [zoneIndex](#zoneindex)

    - [zoneIndex: number](#zoneindex-number)
  + [zoneTotal](#zonetotal)

    - [zoneTotal: number](#zonetotal-number)
* [Private Members](#private-members)

  + [\_alpha](#_alpha)

    - [\_alpha: number](#_alpha-number)
  + [\_blendMode](#_blendmode)

    - [\_blendMode: number](#_blendmode-number)
  + [\_depth](#_depth)

    - [\_depth: number](#_depth-number)
  + [\_rotation](#_rotation)

    - [\_rotation: number](#_rotation-number)
  + [\_scaleX](#_scalex)

    - [\_scaleX: number](#_scalex-number)
  + [\_scaleY](#_scaley)

    - [\_scaleY: number](#_scaley-number)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
  + [alive](#alive)

    - [alive: Array.<Phaser.GameObjects.Particles.Particle>](#alive-arrayphasergameobjectsparticlesparticle)
  + [counters](#counters)

    - [counters: Float32Array](#counters-float32array)
  + [dead](#dead)

    - [dead: Array.<Phaser.GameObjects.Particles.Particle>](#dead-arrayphasergameobjectsparticlesparticle)
  + [isCropped](#iscropped)

    - [isCropped: boolean](#iscropped-boolean)
* [Public Methods](#public-methods)

  + [addDeathZone](#adddeathzone)

    - [<instance> addDeathZone(config)](#instance-adddeathzoneconfig)
  + [addedToScene](#addedtoscene)

    - [<instance> addedToScene()](#instance-addedtoscene)
  + [addEmitZone](#addemitzone)

    - [<instance> addEmitZone(zone)](#instance-addemitzonezone)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addParticleBounds](#addparticlebounds)

    - [<instance> addParticleBounds(x, [y], [width], [height], [collideLeft], [collideRight], [collideTop], [collideBottom])](#instance-addparticleboundsx-y-width-height-collideleft-collideright-collidetop-collidebottom)
  + [addParticleProcessor](#addparticleprocessor)

    - [<instance> addParticleProcessor(processor)](#instance-addparticleprocessorprocessor)
  + [addToDisplayList](#addtodisplaylist)

    - [<instance> addToDisplayList([displayList])](#instance-addtodisplaylistdisplaylist)
  + [addToUpdateList](#addtoupdatelist)

    - [<instance> addToUpdateList()](#instance-addtoupdatelist)
  + [atLimit](#atlimit)

    - [<instance> atLimit()](#instance-atlimit)
  + [clearAlpha](#clearalpha)

    - [<instance> clearAlpha()](#instance-clearalpha)
  + [clearDeathZones](#cleardeathzones)

    - [<instance> clearDeathZones()](#instance-cleardeathzones)
  + [clearEmitZones](#clearemitzones)

    - [<instance> clearEmitZones()](#instance-clearemitzones)
  + [clearFX](#clearfx)

    - [<instance> clearFX()](#instance-clearfx)
  + [clearMask](#clearmask)

    - [<instance> clearMask([destroyMask])](#instance-clearmaskdestroymask)
  + [copyPosition](#copyposition)

    - [<instance> copyPosition(source)](#instance-copypositionsource)
  + [createBitmapMask](#createbitmapmask)

    - [<instance> createBitmapMask([maskObject], [x], [y], [texture], [frame])](#instance-createbitmapmaskmaskobject-x-y-texture-frame)
  + [createEmitter](#createemitter)

    - [<instance> createEmitter()](#instance-createemitter)
  + [createGeometryMask](#creategeometrymask)

    - [<instance> createGeometryMask([graphics])](#instance-creategeometrymaskgraphics)
  + [createGravityWell](#creategravitywell)

    - [<instance> createGravityWell(config)](#instance-creategravitywellconfig)
  + [depthSort](#depthsort)

    - [<instance> depthSort()](#instance-depthsort)
  + [depthSortCallback](#depthsortcallback)

    - [<instance> depthSortCallback(a, b)](#instance-depthsortcallbacka-b)
  + [destroy](#destroy)

    - [<instance> destroy([fromScene])](#instance-destroyfromscene)
  + [disableInteractive](#disableinteractive)

    - [<instance> disableInteractive([resetCursor])](#instance-disableinteractiveresetcursor)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [emitParticle](#emitparticle)

    - [<instance> emitParticle([count], [x], [y])](#instance-emitparticlecount-x-y)
  + [emitParticleAt](#emitparticleat)

    - [<instance> emitParticleAt([x], [y], [count])](#instance-emitparticleatx-y-count)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [explode](#explode)

    - [<instance> explode([count], [x], [y])](#instance-explodecount-x-y)
  + [fastForward](#fastforward)

    - [<instance> fastForward(time, [delta])](#instance-fastforwardtime-delta)
  + [flow](#flow)

    - [<instance> flow(frequency, [count], [stopAfter])](#instance-flowfrequency-count-stopafter)
  + [forEachAlive](#foreachalive)

    - [<instance> forEachAlive(callback, context)](#instance-foreachalivecallback-context)
  + [forEachDead](#foreachdead)

    - [<instance> forEachDead(callback, context)](#instance-foreachdeadcallback-context)
  + [getAliveParticleCount](#getaliveparticlecount)

    - [<instance> getAliveParticleCount()](#instance-getaliveparticlecount)
  + [getAnim](#getanim)

    - [<instance> getAnim()](#instance-getanim)
  + [getBounds](#getbounds)

    - [<instance> getBounds([padding], [advance], [delta], [output])](#instance-getboundspadding-advance-delta-output)
  + [getData](#getdata)

    - [<instance> getData(key)](#instance-getdatakey)
  + [getDeadParticleCount](#getdeadparticlecount)

    - [<instance> getDeadParticleCount()](#instance-getdeadparticlecount)
  + [getDeathZone](#getdeathzone)

    - [<instance> getDeathZone(particle)](#instance-getdeathzoneparticle)
  + [getDisplayList](#getdisplaylist)

    - [<instance> getDisplayList()](#instance-getdisplaylist)
  + [getEmitZone](#getemitzone)

    - [<instance> getEmitZone(particle)](#instance-getemitzoneparticle)
  + [getFrame](#getframe)

    - [<instance> getFrame()](#instance-getframe)
  + [getIndexList](#getindexlist)

    - [<instance> getIndexList()](#instance-getindexlist)
  + [getLocalPoint](#getlocalpoint)

    - [<instance> getLocalPoint(x, y, [point], [camera])](#instance-getlocalpointx-y-point-camera)
  + [getLocalTransformMatrix](#getlocaltransformmatrix)

    - [<instance> getLocalTransformMatrix([tempMatrix])](#instance-getlocaltransformmatrixtempmatrix)
  + [getParentRotation](#getparentrotation)

    - [<instance> getParentRotation()](#instance-getparentrotation)
  + [getParticleCount](#getparticlecount)

    - [<instance> getParticleCount()](#instance-getparticlecount)
  + [getPipelineName](#getpipelinename)

    - [<instance> getPipelineName()](#instance-getpipelinename)
  + [getPostPipeline](#getpostpipeline)

    - [<instance> getPostPipeline(pipeline)](#instance-getpostpipelinepipeline)
  + [getProcessors](#getprocessors)

    - [<instance> getProcessors()](#instance-getprocessors)
  + [getWorldTransformMatrix](#getworldtransformmatrix)

    - [<instance> getWorldTransformMatrix([tempMatrix], [parentMatrix])](#instance-getworldtransformmatrixtempmatrix-parentmatrix)
  + [incData](#incdata)

    - [<instance> incData(key, [amount])](#instance-incdatakey-amount)
  + [initPipeline](#initpipeline)

    - [<instance> initPipeline([pipeline])](#instance-initpipelinepipeline)
  + [initPostPipeline](#initpostpipeline)

    - [<instance> initPostPipeline([preFX])](#instance-initpostpipelineprefx)
  + [killAll](#killall)

    - [<instance> killAll()](#instance-killall)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [onParticleDeath](#onparticledeath)

    - [<instance> onParticleDeath(callback, [context])](#instance-onparticledeathcallback-context)
  + [onParticleEmit](#onparticleemit)

    - [<instance> onParticleEmit(callback, [context])](#instance-onparticleemitcallback-context)
  + [overlap](#overlap)

    - [<instance> overlap(target)](#instance-overlaptarget)
  + [pause](#pause)

    - [<instance> pause()](#instance-pause)
  + [preDestroy](#predestroy)

    - [<instance> preDestroy()](#instance-predestroy)
  + [preUpdate](#preupdate)

    - [<instance> preUpdate(time, delta)](#instance-preupdatetime-delta)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeDeathZone](#removedeathzone)

    - [<instance> removeDeathZone(zone)](#instance-removedeathzonezone)
  + [removedFromScene](#removedfromscene)

    - [<instance> removedFromScene()](#instance-removedfromscene)
  + [removeEmitZone](#removeemitzone)

    - [<instance> removeEmitZone(zone)](#instance-removeemitzonezone)
  + [removeFromDisplayList](#removefromdisplaylist)

    - [<instance> removeFromDisplayList()](#instance-removefromdisplaylist)
  + [removeFromUpdateList](#removefromupdatelist)

    - [<instance> removeFromUpdateList()](#instance-removefromupdatelist)
  + [removeInteractive](#removeinteractive)

    - [<instance> removeInteractive([resetCursor])](#instance-removeinteractiveresetcursor)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [removeParticleProcessor](#removeparticleprocessor)

    - [<instance> removeParticleProcessor(processor)](#instance-removeparticleprocessorprocessor)
  + [removePostPipeline](#removepostpipeline)

    - [<instance> removePostPipeline(pipeline)](#instance-removepostpipelinepipeline)
  + [reserve](#reserve)

    - [<instance> reserve(count)](#instance-reservecount)
  + [resetCounters](#resetcounters)

    - [<instance> resetCounters(frequency, on)](#instance-resetcountersfrequency-on)
  + [resetPipeline](#resetpipeline)

    - [<instance> resetPipeline([resetData])](#instance-resetpipelineresetdata)
  + [resetPostPipeline](#resetpostpipeline)

    - [<instance> resetPostPipeline([resetData])](#instance-resetpostpipelineresetdata)
  + [resume](#resume)

    - [<instance> resume()](#instance-resume)
  + [setAbove](#setabove)

    - [<instance> setAbove(gameObject)](#instance-setabovegameobject)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha([value])](#instance-setalphavalue)
  + [setAngle](#setangle)

    - [<instance> setAngle([degrees])](#instance-setangledegrees)
  + [setAnim](#setanim)

    - [<instance> setAnim(anims, [pickRandom], [quantity])](#instance-setanimanims-pickrandom-quantity)
  + [setBelow](#setbelow)

    - [<instance> setBelow(gameObject)](#instance-setbelowgameobject)
  + [setBlendMode](#setblendmode)

    - [<instance> setBlendMode(value)](#instance-setblendmodevalue)
  + [setConfig](#setconfig)

    - [<instance> setConfig(config)](#instance-setconfigconfig)
  + [setData](#setdata)

    - [<instance> setData(key, [data])](#instance-setdatakey-data)
  + [setDataEnabled](#setdataenabled)

    - [<instance> setDataEnabled()](#instance-setdataenabled)
  + [setDepth](#setdepth)

    - [<instance> setDepth(value)](#instance-setdepthvalue)
  + [setEmitterAngle](#setemitterangle)

    - [<instance> setEmitterAngle(value)](#instance-setemitteranglevalue)
  + [setEmitterFrame](#setemitterframe)

    - [<instance> setEmitterFrame(frames, [pickRandom], [quantity])](#instance-setemitterframeframes-pickrandom-quantity)
  + [setEmitZone](#setemitzone)

    - [<instance> setEmitZone(zone)](#instance-setemitzonezone)
  + [setFrame](#setframe)

    - [<instance> setFrame(frame, [updateSize], [updateOrigin])](#instance-setframeframe-updatesize-updateorigin)
  + [setFrequency](#setfrequency)

    - [<instance> setFrequency(frequency, [quantity])](#instance-setfrequencyfrequency-quantity)
  + [setInteractive](#setinteractive)

    - [<instance> setInteractive([hitArea], [callback], [dropZone])](#instance-setinteractivehitarea-callback-dropzone)
  + [setMask](#setmask)

    - [<instance> setMask(mask)](#instance-setmaskmask)
  + [setName](#setname)

    - [<instance> setName(value)](#instance-setnamevalue)
  + [setParticleAlpha](#setparticlealpha)

    - [<instance> setParticleAlpha(value)](#instance-setparticlealphavalue)
  + [setParticleGravity](#setparticlegravity)

    - [<instance> setParticleGravity(x, y)](#instance-setparticlegravityx-y)
  + [setParticleLifespan](#setparticlelifespan)

    - [<instance> setParticleLifespan(value)](#instance-setparticlelifespanvalue)
  + [setParticleScale](#setparticlescale)

    - [<instance> setParticleScale([x], [y])](#instance-setparticlescalex-y)
  + [setParticleSpeed](#setparticlespeed)

    - [<instance> setParticleSpeed(x, [y])](#instance-setparticlespeedx-y)
  + [setParticleTint](#setparticletint)

    - [<instance> setParticleTint(value)](#instance-setparticletintvalue)
  + [setPipeline](#setpipeline)

    - [<instance> setPipeline(pipeline, [pipelineData], [copyData])](#instance-setpipelinepipeline-pipelinedata-copydata)
  + [setPipelineData](#setpipelinedata)

    - [<instance> setPipelineData(key, [value])](#instance-setpipelinedatakey-value)
  + [setPosition](#setposition)

    - [<instance> setPosition([x], [y], [z], [w])](#instance-setpositionx-y-z-w)
  + [setPostPipeline](#setpostpipeline)

    - [<instance> setPostPipeline(pipelines, [pipelineData], [copyData])](#instance-setpostpipelinepipelines-pipelinedata-copydata)
  + [setPostPipelineData](#setpostpipelinedata)

    - [<instance> setPostPipelineData(key, [value])](#instance-setpostpipelinedatakey-value)
  + [setQuantity](#setquantity)

    - [<instance> setQuantity(quantity)](#instance-setquantityquantity)
  + [setRadial](#setradial)

    - [<instance> setRadial([value])](#instance-setradialvalue)
  + [setRandomPosition](#setrandomposition)

    - [<instance> setRandomPosition([x], [y], [width], [height])](#instance-setrandompositionx-y-width-height)
  + [setRotation](#setrotation)

    - [<instance> setRotation([radians])](#instance-setrotationradians)
  + [setScale](#setscale)

    - [<instance> setScale([x], [y])](#instance-setscalex-y)
  + [setScrollFactor](#setscrollfactor)

    - [<instance> setScrollFactor(x, [y])](#instance-setscrollfactorx-y)
  + [setSortCallback](#setsortcallback)

    - [<instance> setSortCallback([callback])](#instance-setsortcallbackcallback)
  + [setSortProperty](#setsortproperty)

    - [<instance> setSortProperty([property], [ascending])](#instance-setsortpropertyproperty-ascending)
  + [setState](#setstate)

    - [<instance> setState(value)](#instance-setstatevalue)
  + [setTexture](#settexture)

    - [<instance> setTexture(key, [frame], [updateSize], [updateOrigin])](#instance-settexturekey-frame-updatesize-updateorigin)
  + [setToBack](#settoback)

    - [<instance> setToBack()](#instance-settoback)
  + [setToTop](#settotop)

    - [<instance> setToTop()](#instance-settotop)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value)](#instance-setvisiblevalue)
  + [setW](#setw)

    - [<instance> setW([value])](#instance-setwvalue)
  + [setX](#setx)

    - [<instance> setX([value])](#instance-setxvalue)
  + [setY](#sety)

    - [<instance> setY([value])](#instance-setyvalue)
  + [setZ](#setz)

    - [<instance> setZ([value])](#instance-setzvalue)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [start](#start)

    - [<instance> start([advance], [duration])](#instance-startadvance-duration)
  + [startFollow](#startfollow)

    - [<instance> startFollow(target, [offsetX], [offsetY], [trackVisible])](#instance-startfollowtarget-offsetx-offsety-trackvisible)
  + [stop](#stop)

    - [<instance> stop([kill])](#instance-stopkill)
  + [stopFollow](#stopfollow)

    - [<instance> stopFollow()](#instance-stopfollow)
  + [toggleData](#toggledata)

    - [<instance> toggleData(key)](#instance-toggledatakey)
  + [toJSON](#tojson)

    - [<instance> toJSON()](#instance-tojson)
  + [update](#update)

    - [<instance> update([args])](#instance-updateargs)
  + [updateConfig](#updateconfig)

    - [<instance> updateConfig(config)](#instance-updateconfigconfig)
  + [willRender](#willrender)

    - [<instance> willRender(camera)](#instance-willrendercamera)

Back to top

©2025[Phaser](https://docs.phaser.io)



ParticleEmitter