# Particles

A Guide to the Phaser Particle System

A Particle Emitter is a special kind of Game Object that controls a pool of Particles.

Particle Emitters are created via a configuration object. The properties of this object can be specified in a variety of formats, given you plenty of scope over the values they return, leading to complex visual effects. Here are the different forms of configuration value you can give:

## An explicit static value:

```
Copyx: 400

```

The x value will always be 400 when the particle is spawned.

## A random value:

```
Copyx: [ 100, 200, 300, 400 ]

```

The x value will be one of the 4 elements in the given array, picked at random on emission.

## A custom callback:

```
Copyx: (particle, key, t, value) => {
  return value + 50;
}

```

The x value is the result of calling this function. This is only used when the particle is emitted, so it provides it's initial starting value. It is not used when the particle is updated (see the onUpdate callback for that)

## A start / end object:

This allows you to control the change in value between the given start and end parameters over the course of the particles lifetime:

```
Copyscale: { start: 0, end: 1 }

```

The particle scale will start at 0 when emitted and ease to a scale of 1 over the course of its lifetime. You can also specify the ease function used for this change (the default is Linear):

```
Copyscale: { start: 0, end: 1, ease: 'bounce.out' }

```

## A start / end random object:

The start and end object can have an optional `random` parameter. This forces it to pick a random value between the two values and use this as the starting value, then easing to the 'end' parameter over its lifetime.

```
Copyscale: { start: 4, end: 0.5, random: true }

```

The particle will start with a random scale between 0.5 and 4 and then scale to the end value over its lifetime. You can combine the above with the `ease` parameter as well to control the value easing.

## An interpolation object:

You can provide an array of values which will be used for interpolation during the particles lifetime. You can also define the interpolation function to be used. There are three provided: `linear` (the default), `bezier` and `catmull`, or you can provide your own function.

```
Copyx: { values: [ 50, 500, 200, 800 ], interpolation: 'catmull' }

```

The particle scale will interpolate from 50 when emitted to 800 via the other points over the course of its lifetime. You can also specify an ease function used to control the rate of change through the values (the default is Linear):

```
Copyx: { values: [ 50, 500, 200, 800 ], interpolation: 'catmull', ease: 'bounce.out }

```

## A stepped emitter object:

The `steps` parameter allows you to control the placement of sequential particles across the start-end range:

```
Copyx: { steps: 32, start: 0, end: 576 }

```

Here we have a range of 576 (start to end). This is divided into 32 steps.

The first particle will emit at the x position of 0. The next will emit at the next 'step' along, which would be 18. The following particle will emit at the next step, which is 36, and so on. Because the range of 576 has been divided by 32, creating 18 pixels steps. When a particle reaches the 'end' value the next one will start from the beginning again.

## A stepped emitter object with yoyo:

You can add the optional `yoyo` property to a stepped object:

```
Copyx: { steps: 32, start: 0, end: 576, yoyo: true }

```

As with the stepped emitter, particles are emitted in sequence, from 'start' to 'end' in step sized jumps. Normally, when a stepped emitter reaches the end it snaps around to the start value again. However, if you provide the 'yoyo' parameter then when it reaches the end it will reverse direction and start emitting back down to 'start' again. Depending on the effect you require this can often look better.

## A min / max object:

This allows you to pick a random float value between the min and max properties:

```
Copyx: { min: 100, max: 700 }

```

The x value will be a random float between min and max.

You can force it select an integer by setting the 'int' flag:

```
Copyx: { min: 100, max: 700, int: true }

```

Or, you could use the 'random' array approach (see below)

## A random object:

This allows you to pick a random integer value between the first and second array elements:

```
Copyx: { random: [ 100, 700 ] }

```

The x value will be a random integer between 100 and 700 as it takes the first element in the 'random' array as the 'min' value and the 2nd element as the 'max' value.

## Custom onEmit and onUpdate callbacks:

If the above won't give you the effect you're after, you can provide your own callbacks that will be used when the particle is both emitted and updated:

```
Copyx: {
  onEmit: (particle, key, t, value) => {
    return value;
  },
  onUpdate: (particle, key, t, value) => {
    return value;
  }
}

```

You can provide either one or both functions. The `onEmit` is called at the start of the particles life and defines the value of the property on birth.

The `onUpdate` function is called every time the Particle Emitter updates until the particle dies. Both must return a value.

The properties are:

`particle` - A reference to the Particle instance.
`key` - The string based key of the property, i.e. 'x' or 'lifespan'.
`t` - The current normalized lifetime of the particle, between 0 (birth) and 1 (death).
`value` - The current property value. At a minimum you should return this.

By using the above configuration options you have an unlimited about of control over how your particles behave.

## v3.55 Differences

Prior to v3.60 Phaser used a `ParticleEmitterManager`. This was removed in v3.60 and now calling `this.add.particles` returns a `ParticleEmitter` instance instead.

In order to streamline memory and the display list we have removed the `ParticleEmitterManager` entirely. When you call `this.add.particles` you're now creating a `ParticleEmitter` instance, which is being added directly to the
display list and can be manipulated just like any other Game Object, i.e. scaled, rotated, positioned, added to a Container, etc. It now extends the `GameObject` base class, meaning it's also an event emitter, which allowed us
to create some handy new events for particles.

So, to create an emitter, you now give it an xy coordinate, a texture and an emitter configuration object (you can also set this later, but most commonly you'd do it on creation). I.e.:

```
Copyconst emitter = this.add.particles(100, 300, 'flares', {
  frame: 'red',
  angle: { min: -30, max: 30 },
  speed: 150
});

```

This will create a 'red flare' emitter at 100 x 300.

Please update your code to ensure it adheres to the new function signatures.

## Advanced Emitter Examples

First, load an image:

```
Copythis.load.image(key, url);

```

Reference: [load image](../loader.md)

## Add particle

```
Copyvar particles = this.add.particles(x, y, texture, {
    
    // EmitterOp
    accelerationX: 0,
    accelerationY: 0,
    alpha: 1,
    angle: { min: 0, max: 360 },
    bounce: 0,
    color: undefined,
    delay: 0,
    hold: 0,
    lifespan: 1000,
    maxVelocityX: 10000,
    maxVelocityY: 10000,
    moveToX: 0,
    moveToY: 0,
    quantity: 1,
    rotate: 0,
    scaleX: 1,
    scaleY: 1,
    // scale:
    speedX: 0,
    speedY: 0,
    speed: 
    tint: 0xffffff,
    x: 0,
    y: 0,

    // Emitter properties
    active:
    advance:
    blendMode:
    colorEase:
    deathCallback:
    deathCallbackScope:
    duration:
    emitCallback:
    emitCallbackScope:
    // callbackScope    
    frequency:
    gravityX:
    gravityY:
    maxAliveParticles:
    maxParticles:
    name:
    emitting:
    particleBringToTop:
    particleClass:
    radial:
    sortCallback:
    sortOrderAsc:
    sortProperty:
    stopAfter:
    tintFill:
    timeScale:
    trackVisible:
    visible:

    // Position
    // emitZone : random-zone, edge-zone
    // random-zone
    emitZone: {
        type: 'random',
        source: geom,
    },

    // edge-zone
    emitZone:{
        type: 'edge',
        source: geom,
        quantity: 1,
        stepRate: 0,
        total: -1,
        yoyo: false,
        seamless: true
    },

    deathZone: {
        type: 'onEnter', // 'onEnter', or 'onLeave'
        source: geom,
    },

    bounds:               // {x, y, w, h}, or {x, y, width, height}, or Phaser.Geom.Rectangle
    collideLeft: true,
    collideRight: true,
    collideTop: true,
    collideBottom: true,

    follow:
    followOffset:{
       x: 0,
       y: 0
    },

    // Texture
    texture:
    frame:
    anim: [],  // string, or array of string
    
    reserve: 0,
    advance: 0
});

```

* Parameters of EmitterOp : Number, Random Array, Custom Callback, Stepped start/end, Eased start/end, min/max, Random object, Custom onEmit onUpdate, Interpolation

  + A number
  + `{min, max}` : Pick a random value between min and max
  + `{min, max, int}`
  + `{start, end}` : Pick values incremented continuously across a range. (`ease`=`'Linear'`)

    - `{start, end, ease}`
    - `{start, end, ease, easeParams}`
  + `{start, end, steps}` : Pick values incremented by steps across a range.
  + `{start, end, steps, yoyo: true}`
  + `{start, end, random}`

    - `random`: `true` or `false`
  + `{random: [start, end]}` : Pick a random number between start and and.
  + `[a, b, c, d]` : Pick a random number from an array.
  + `{min, max, steps}` : Pick values between min to max, with steps.
  + `{ values: [ a, b, c, d ], interpolation: 'catmull', ease: 'linear' }` : Interpolation (`linear`, `bezier`, `catmull`) in values array.
  + `function(particle, key, t, value) { return value; }`
  + `{onEmit, onUpdate}` : Get return value from a function invoking.

    ```
    Copyfunction(particle, key, t, value) {
        return value;
    }

    ```
* `active` : Whether this emitter updates itself and its particles.

  + `false` : Equal to pause.
* `advance` : If you wish to *fast forward* the emitter in time, set this value to a number representing the amount of ms the emitter should advance.
* `blendMode` : See [blend mode](../display.md)
* `colorEase` : The string-based name of the Easing function to use if you have enabled Particle color interpolation via the `color` property, otherwise has no effect.
* `deathCallback`, `deathCallbackScope`

  ```
  Copyfunction(particle) {

  }

  ```
* `emitCallback`, `emitCallbackScope`

  ```
  Copyfunction(particle, emitter) {

  }

  ```
* `duration` : Limit the emitter to emit particles for a maximum of `duration` ms.

  + `0` : Forever, default behavior.
* `follow` : A Game Object whose position is used as the particle origin.
* `followOffset` : The offset of the particle origin from thefollow target.
* `frequency`

  + `0` : One particle flow cycle for each logic update (the maximum flow frequency).
  + `> 0` : The time interval between particle flow cycles in ms.
  + `-1` : Exploding emitter.
* `hold` : Frozen or 'held in place' after it has finished its lifespan for a set number of ms
* `gravityX`, `gravityY`
* `maxAliveParticles`
* `maxParticles`

  + `0` : Unlimited.
  + `> 0` : Hard limit the amount of particle objects.
* `frames` : One or more texture frames, or a configuration object.

  + String or number value
  + Array of string or number value
  + Configuration object :

    ```
    Copy{
        frames: [],
        cycle: false,
        quantity: 1
    }

    ```
* `anim` :

  + String
  + Array of string
  + Configuration object :

    ```
    Copy{
        anim: [],  // Array of string
        cycle: false,
        quantity: 1
    }

    ```
* `particleBringToTop` :

  + `true` : Newly emitted particles are added to the top of the particle list, i.e. rendered above those already alive. Default behavior.
* `sortCallback` : The callback used to sort the particles.
* `sortProperty` : Optionally sort the particles before they render based on this property. The property must exist on the `Particle` class, such as `y`, `lifeT`, `scaleX`, etc.
* `sortOrderAsc` : When `sortProperty` is defined this controls the sorting order, either ascending or descending.
* `stopAfter` : The Particle Emitter will stop emitting particles once this total has been reached. It will then enter a 'stopped' state, firing the `STOP` event.
* `radial` : A radial emitter will emit particles in all directions between angle min and max,
* `emitting` : Controls if the emitter is currently emitting a particle flow (when frequency >= 0).
  Already alive particles will continue to update until they expire.

  + `false` : Equal to stop
* `tintFill` :
* `timeScale` : The time rate applied to active particles, affecting lifespan, movement, and tweens. Values larger than 1 are faster than normal.
* `trackVisible` : Whether the emitter's `visible` state will track the follow target's visibility state.
* `emitZone` :

  + [Emit zone](#emit-zone)

    ```
    Copy{
        type: 'random',
        source: geom,
    }            

    ```
  + [Emit edge](#add-emit-edge)

    ```
    Copy{
        type: 'edge',
        source: curve,

        quantity: 1,
        stepRate: 0,
        yoyo: false,
        seamless: true
    }            

    ```
* [`deathZone`](#death-zone)

  ```
  Copy{
      type: 'onEnter', // 'onEnter', or 'onLeave'
      source: geom
  }

  ```
* `bounds` : `{x, y, w, h}`, or `{x, y, width, height}`, or [Rectangle](../geometry.md).
* `collideLeft`, `collideRight`, `collideTop`, `collideBottom` : Whether particles interact with the left/right/top/bottom edge of the bounds.
* `name`
* [`particleClass`](#custom-particle-class)

## Control

* Start

  ```
  Copyemitter.start();
  // emitter.start(advance, duration);

  ```

  + `advance` : Advance this number of ms in time through the emitter.
  + `duration` : Limit this emitter to only emit particles for the given number of ms. Setting this parameter will override any duration already set in the Emitter configuration object.
* Stop

  ```
  Copyemitter.stop();
  // emitter.stop(kill);

  ```

  + `kill` :
    - `true` : Kill all particles immediately
    - `false` : Leave them to die after their lifespan expires. Default behavior.
* Pause

  ```
  Copyemitter.pause();  // set `active` to false

  ```
* Resume

  ```
  Copyemitter.resume();  // set `active` to true

  ```
* Starts (or restarts) a particle flow.

  ```
  Copyemitter.flow(frequency, count, stopAfter);

  ```

  + `frequency` :
    - `>= 0` : The time interval of each flow cycle, in ms
    - `-1` : Explosion mode.
  + `count` : The number of particles to emit at each flow cycle.
  + `stopAfter` : Stop this emitter from firing any more particles once this value is reached.
    - Setting this parameter will override any `stopAfter` value already set in the Emitter configuration object.
    - `0` : Unlimited
* Explode : Puts the emitter in explode mode (`frequency` = `-1`), stopping any current particle flow, and emits several particles all at once.

  ```
  Copyemitter.explode();
  // emitter.explode(count, x, y);

  ```

  + `count` : The number of Particles to emit.
  + `x`, `y` : The x, y coordinate to emit the Particles from.
* Emit : Emits particles at the given position. If no position is given, it will emit from this Emitters current location.

  ```
  Copyemitter.emitParticleAt();
  // emitter.emitParticleAt(x, y, count);    

  ```

  or

  ```
  Copyemitter.emitParticle(count, x, y);

  ```

  + `count` : The number of Particles to emit.
  + `x`, `y` : The x, y coordinate to emit the Particles from.
* Fast forward

  ```
  Copyemitter.fastForward(time, delta);

  ```

  + `time` : The number of ms to advance the Particle Emitter by.
  + `delta` : The amount of delta to use for each step. Defaults to `1000 / 60`.
* Kill all alive particles

  ```
  Copyemitter.killAll()

  ```

## Follow target

* Start

  ```
  Copyemitter.startFollow(target);
  // emitter.startFollow(target, offsetX, offsetY, trackVisible);

  ```

  + `target` : The Game Object to follow.
  + `offsetX`, `offsetY` : Horizontal/vertical offset of the particle origin from the Game Object.
  + `trackVisible` : Whether the emitter's visible state will track the target's visible state.
* Stop

  ```
  Copyemitter.stopFollow();

  ```

## Frame

```
Copyemitter.setEmitterFrame(frames);
// emitter.setEmitterFrame(frames, pickRandom, quantity);

```

* `frames` : One or more texture frames, or a configuration object.

  + String or number value
  + Array of string or number value
  + Configuration object :

    ```
    Copy{
        frames: [],
        cycle: false,
        quantity: 1
    }

    ```
* `pickRandom` :

  + `true` : Whether frames should be assigned at random from `frames`. Default behavior.
* `quantity` : The number of consecutive particles that will receive each frame. Default value is `1`.

## Animation

```
Copyemitter.setAnim(anims);
// emitter.setAnim(anims, pickRandom, quantity);

```

* `anims` : One or more animations, or a configuration object.
  + String
  + Array of string
  + Configuration object :

    ```
    Copy{
        anims: [],
        cycle: false,
        quantity: 1
    }

    ```

    - `anims` : One or more animations names, or Play Animation Config objects.
      * String
      * Array of string
      * [Animation config](../animations.md)
      * Array of [Animation config](../animations.md)
* `pickRandom` :
  + `true` : Whether frames should be assigned at random from `frames`. Default behavior.
* `quantity` : The number of consecutive particles that will receive each frame. Default value is `1`.

## Particle

* Speed

  ```
  Copyemitter.setParticleSpeed(x, y);

  ```

  or

  ```
  Copyemitter.speedX = x;
  emitter.speedY = y;

  ```

  + Changes the emitter from radial to a point emitter
* Bounce

  ```
  Copyemitter.bounce = value;

  ```

  + `0` : No bounce
  + `1` : Full rebound
* Max velocity

  ```
  Copyemitter.maxVelocityX = x;
  emitter.maxVelocityY = y;

  ```
* Gravity

  ```
  Copyemitter.setParticleGravity(x, y);

  ```

  or

  ```
  Copyemitter.gravityX = x;
  emitter.gravityY = y;

  ```
* Acceleration

  ```
  Copyemitter.accelerationX = x;
  emitter.accelerationY = y;

  ```
* Lifespan : Sets the lifespan of newly emitted particles in milliseconds.

  ```
  Copyemitter.setParticleLifespan(time);

  ```

  or

  ```
  Copyemitter.lifespan = time

  ```
* The number of milliseconds to wait after emission before the particles start updating.

  ```
  Copyemitter.delay = time;

  ```
* The number of milliseconds to wait after a particle has finished its life before it will be removed.

  ```
  Copyemitter.hold = time;

  ```
* Tint

  ```
  Copyemitter.setParticleTint(tint);

  ```

  or

  ```
  Copyemitter.particleTint = tint;

  ```

  + Webgl only
* Color

  ```
  Copyemitter.particleColor = color;   // WebGL only.
  emitter.colorEase = easeName;

  ```

  + Webgl only
* Alpha

  ```
  Copyemitter.setParticleAlpha(alpha);

  ```

  or

  ```
  Copyemitter.setAlpha(alpha);

  ```

  or

  ```
  Copyemitter.particleAlpha = alpha;

  ```
* Scale : Sets the vertical and horizontal scale of the emitted particles.

  ```
  Copyemitter.setParticleScale(x, y);

  ```

  or

  ```
  Copyemitter.setScale(x, y);

  ```

  or

  ```
  Copyemitter.particleScaleX = x;
  emitter.particleScaleY = y;

  ```
* Position

  ```
  Copyemitter.particleX = x;
  emitter.particleY = y;

  ```
* Position to move toward

  ```
  Copyemitter.moveToX = x;
  emitter.moveToY = y;

  ```
* The angle at which the particles are emitted.

  ```
  Copyemitter.particleAngle = angle;  // degrees    

  ```
* The rotation (or angle) of each particle when it is emitted.

  ```
  Copyemitter.particleRotate = rotation; // degrees

  ```
* The number of particles that are emitted each time an emission occurs

  ```
  Copyemitter.quantity = quantity;

  ```
* Hard limit the amount of particle objects

  ```
  Copyvar count = emitter.maxParticles;

  ```

  + Whether this emitter is at its limit

    ```
    Copyvar atLimit = emitter.atLimit();

    ```
* Alive (active) particles

  + Amount of alive particles

    ```
    Copyvar count = emitter.getAliveParticleCount();

    ```

    or

    ```
    Copyvar count = emitter.alive.length;

    ```
  + Add callback for newly emitted particle

    ```
    Copyvar callback = function(particle, emitter) { /* ... */ }
    emitter.onParticleEmit(callback, context);

    ```

    - Clear callback

      ```
      Copyemitter.onParticleEmit();

      ```
  + For each alive particle

    ```
    Copyvar callback = function(particle, emitter) { /* ... */ }
    emitter.forEachAlive(callback, context);

    ```
* Dead (inactive) particles

  + Amount of dead particles

    ```
    Copyvar count = emitter.getDeadParticleCount();

    ```

    or

    ```
    Copyvar count = emitter.dead.length;

    ```
  + Add callback for each particle death

    ```
    Copyvar callback = function(particle, emitter) { /* ... */ }
    emitter.onParticleDeath(callback, context);

    ```

    - Clear callback

      ```
      Copyemitter.onParticleDeath();

      ```
  + For each dead particle

    ```
    Copyvar callback = function(particle, emitter) { /* ... */ }
    emitter.forEachDead(callback, context);

    ```
  + Add dead particles into pool

    ```
    Copyemitter.reserve(count);

    ```
* Total (alive + dead) number of particles.

  ```
  Copyvar count = emitter.getParticleCount();

  ```
* Active particles overlaps with a Rectangle Geometry object or an Arcade Physics Body.

  ```
  Copyvar particles = emitter.overlap(target);

  ```

  + `target` :
    - A [Rectangle](../geometry.md).
    - Arcade Physics Body.
  + `particles` : An array of Particles that overlap with the given target
* Gets a bounds Rectangle calculated from the bounds of all currently active Particles

  ```
  Copyemitter.getBounds(padding, advance, delta, output);

  ```

  + `padding` : The amount of padding, in pixels, to add to the bounds Rectangle.
  + `advance`, `delta` : *Fast forward* in time to try and allow the bounds to be more accurate.
  + `output` : The [Rectangle](../geometry.md) to store the results in.
* Gets the bounds of this particle as a Geometry Rectangle

  ```
  Copyparticle.getBounds();

  ```

### Render order

* Sort by property

  ```
  Copyemitter.setSortProperty(property, ascending);

  ```

  + `property` : The property on the `Particle` class to sort by.
  + `ascending` : Should the particles be sorted in ascending or descending order?
* Sort by callback

  ```
  Copyvar callback = function(particleA, particleB) {
      return 1; // 0,1,-1
  }
  emitter.setSortCallback(callback);

  ```

## Emitter

* Frequency

  ```
  Copyemitter.setFrequency(frequency);
  // emitter.setFrequency(frequency, quantity);

  ```

  + `frequency` :
    - `>= 0` : The time interval of each flow cycle, in ms
    - `-1` : Explosion mode.
  + `quantity` : The number of particles to release at each flow cycle or explosion.
* Quantity

  ```
  Copyemitter.setQuantity(quantity);

  ```

  + `quantity` : The number of particles to release at each flow cycle or explosion.

## Zone

## Emit zone

### Add emit zone

```
Copyvar zone = emitter.addEmitZone({
    type: 'random',
    source: geom,
});

```

* `source` : Geom like [Circle](../geometry.md), [Ellipse](../geometry.md), [Rectangle](../geometry.md),[Triangle](../geometry.md), [Polygon](../geometry.md), or [Path or Curve](../math.md), which has `getRandomPoint(point)` method
  + Custom zone

    ```
    Copy{
        getRandomPoint: function(point) {
            // point.x = ...
            // point.y = ...
            return point;
        }
    }

    ```

### Add emit edge

```
Copyvar zone = emitter.addEmitZone({
    type: 'edge',
    source: curve,

    quantity: 1,
    stepRate: 0,
    yoyo: false,
    seamless: true,
    total: -1
});

```

* `source` : Geom like [Circle](../geometry.md), [Ellipse](../geometry.md), [Rectangle](../geometry.md),[Triangle](../geometry.md), [Polygon](../geometry.md), or [Path or Curve](../math.md), which has `getPoints(quantity, stepRate)` method

  + Custom edge

    ```
    Copy{
        getPoints: function(quantity, stepRate) {
            // output = [point0, point1, ...];  // point: Phaser.Math.Vector2, or {x, y}
            return output;
        }
    }

    ```
* `quantity` : The number of particles to place on the source edge. Set to 0 to use `stepRate` instead.
* `stepRate` : The distance between each particle. When set, `quantity` is implied and should be set to 0.
* `yoyo` : Whether particles are placed from start to end and then end to start. Default is `false`.
* `seamless` : Whether one endpoint will be removed if it's identical to the other. Default is `true`.
* `total` : The total number of particles this zone will emit before passing over to the next emission zone in the Emitter.

!!! note "quantity or stepRate"
- Any geometry like [circle](../geometry.md), [ellipse](../geometry.md), [line](../geometry.md), [polygon](../geometry.md), [rectangle](../geometry.md), [triangle](../geometry.md) source has *quantity*, or *stepRate*
- [Curve](../math.md) source has *quantity*, or *stepRate*
- [Path](../math.md) source only has *quantity*

### Set emit zone

```
Copyemitter.setEmitZone(zone);

```

* `zone` : The Emit Zone to set as the active zone.
  + A zone object
  + A number as index

### Zone source

* Get

  ```
  Copy// var zone = emitter.emitZones[i];
  var source = zone.source;    

  ```
* (Edge type only) Update points of curve source

  ```
  Copyzone.updateSource();

  ```
* (Edge type only) Set source to another curve, also update points

  ```
  Copyzone.changeSource(curve);

  ```

### Remove emit zone

```
Copyemitter.removeEmitZone(zone)

```

### Clear emit zone

```
Copyemitter.clearEmitZones();

```

or

```
Copyemitter.emitZones.length = 0;
emitter.zoneIndex = 0;

```

## Death zone

```
Copyvar zone = emitter.addDeathZone({
     type: 'onEnter',
     source: geom
});

```

* `type` : `'onEnter'` or `'onLeave'`
* `source` : Geom like [Circle](../geometry.md), [Ellipse](../geometry.md), [Rectangle](../geometry.md),[Triangle](../geometry.md), [Polygon](../geometry.md)
  + Custom `source` :

    ```
    Copy{
        contains: function (x, y) {
            // ...
            return bool;
        }
    }

    ```

### Remove death zone

```
Copyemitter.removeDeathZone(zone)

```

### Clear death zone

```
Copyemitter.clearDeathZones();

```

or

```
Copyemitter.deathZones.length = 0;

```

## Events

* Starts emission of particles.

  ```
  Copyemitter.on('start', function(emitter) {

  })

  ```
* Explodes a set of particles.

  ```
  Copyemitter.on('explode', function(emitter, particle) {

  })

  ```
* Death Zone kills a Particle instance.

  ```
  Copyemitter.on('deathzone', function(emitter, particle, zone) {

  })

  ```
* Stops emission

  ```
  Copyemitter.on('stop', function(emitter) {

  })

  ```

  + Directly call the `ParticleEmitter.stop` method.
  + Stop after a set time via the `duration` property.
  + Stop after a set number of particles via the `stopAfter` property.
* Complete Event, no particles are still rendering at this point in time.

  ```
  Copyemitter.on('complete', function(emitter) {

  })

  ```

## Bounds

* Add bounds

  ```
  Copyvar bounds = emitter.addParticleBounds(x, y, width, height);
  // var bounds = emitter.addParticleBounds(x, y, width, height, collideLeft, collideRight, collideTop, collideBottom);

  ```

  or

  ```
  Copyvar bounds = emitter.addParticleBounds(rect);

  ```

  + `x, y, width, height`, `{x, y, width, height}`, or `{x, y, w, h}`, or [Rectangle](../geometry.md) : Bounds
  + `collideLeft`, `collideRight`, `collideTop`, `collideBottom` : Whether particles interact with the left/right/top/bottom edge of the bounds.
* Collide edges

  ```
  Copybounds.collideLeft = enabled;
  bounds.collideRight = enabled;
  bounds.collideTop = enabled;
  bounds.collideBottom = enabled;

  ```
* Bound rectangle

  ```
  Copyvar rect = bounds.bounds;

  ```

  + `rect` : [Rectangle](../geometry.md)

## Gravity well

* Create a gravity well

  ```
  Copyvar well = particles.createGravityWell({
      // x: 0,
      // y: 0,
      // power: 0,
      // epsilon: 100,
      // gravity: 50
  });

  ```
* Enable

  + Active

    ```
    Copywell.active = true;

    ```
  + Inactive

    ```
    Copywell.active = false;

    ```
* Position

  ```
  Copywell.x = x;
  well.y = y;

  ```
* Gravity

  ```
  Copywell.gravity = value;

  ```
* Power

  ```
  Copywell.power = value;

  ```

## Custom Particle Processor

* Declare Particle Processor class

  ```
  Copyclass MyParticleProcessor extends Phaser.GameObjects.Particles.ParticleProcessor {
      constructor() {
          super(x, y, active);
          // ...
      }

      update(particle, delta, step, t) {
          // particle : The Particle to update.
          // delta : The delta time in ms.
          // step : The delta value divided by 1000.
          // t : The current normalized lifetime of the particle, between 0 (birth) and 1 (death).
      }

      destroy() {
          super.destroy();
      }
  }

  ```

  + Override `update` method
* Add to emitter

  ```
  Copyvar myParticleProcessor = emitter.addParticleProcessor(new MyParticleProcessor);

  ```

## Custom particle class

```
Copyclass MyParticle extends Phaser.GameObjects.Particles.Particle {
    constructor (emitter) {
        super(emitter);
        /* ... */
    }

    update (delta, step, processors) {
        super.update(delta, step, processors);
        /* ... */
    }
}

```

## Other properties

See [game object](../gameobjects.md)

## Create mask

```
Copyvar mask = emitter.createBitmapMask();

```

See [mask](../display.md)

## Shader effects

Support [postFX effects](shader.md)

!!! note
No preFX effect support

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Nine Slice](nine-slice.md)

[Plane](plane.md)

On this page

* [Particles](#particles)

  + [An explicit static value:](#an-explicit-static-value)
  + [A random value:](#a-random-value)
  + [A custom callback:](#a-custom-callback)
  + [A start / end object:](#a-start--end-object)
  + [A start / end random object:](#a-start--end-random-object)
  + [An interpolation object:](#an-interpolation-object)
  + [A stepped emitter object:](#a-stepped-emitter-object)
  + [A stepped emitter object with yoyo:](#a-stepped-emitter-object-with-yoyo)
  + [A min / max object:](#a-min--max-object)
  + [A random object:](#a-random-object)
  + [Custom onEmit and onUpdate callbacks:](#custom-onemit-and-onupdate-callbacks)
  + [v3.55 Differences](#v355-differences)
  + [Advanced Emitter Examples](#advanced-emitter-examples)
  + [Add particle](#add-particle)
  + [Control](#control)
  + [Follow target](#follow-target)
  + [Frame](#frame)
  + [Animation](#animation)
  + [Particle](#particle)

    - [Render order](#render-order)
  + [Emitter](#emitter)
  + [Zone](#zone)
  + [Emit zone](#emit-zone)

    - [Add emit zone](#add-emit-zone)
    - [Add emit edge](#add-emit-edge)
    - [Set emit zone](#set-emit-zone)
    - [Zone source](#zone-source)
    - [Remove emit zone](#remove-emit-zone)
    - [Clear emit zone](#clear-emit-zone)
  + [Death zone](#death-zone)

    - [Remove death zone](#remove-death-zone)
    - [Clear death zone](#clear-death-zone)
  + [Events](#events)
  + [Bounds](#bounds)
  + [Gravity well](#gravity-well)
  + [Custom Particle Processor](#custom-particle-processor)
  + [Custom particle class](#custom-particle-class)
  + [Other properties](#other-properties)
  + [Create mask](#create-mask)
  + [Shader effects](#shader-effects)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)