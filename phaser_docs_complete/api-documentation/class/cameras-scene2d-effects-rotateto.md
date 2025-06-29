# RotateTo

Phaser.Cameras.Scene2D.Effects.RotateTo

A Camera Rotate effect.

This effect will rotate the Camera so that the its viewport finishes at the given angle in radians,

over the duration and with the ease specified.

Camera rotation always takes place based on the Camera viewport. By default, rotation happens

in the center of the viewport. You can adjust this with the `originX` and `originY` properties.

Rotation influences the rendering of *all* Game Objects visible by this Camera. However, it does not

rotate the Camera viewport itself, which always remains an axis-aligned rectangle.

Only the camera is rotates. None of the objects it is displaying are impacted, i.e. their positions do

not change.

The effect will dispatch several events on the Camera itself and you can also specify an `onUpdate` callback,

which is invoked each frame for the duration of the effect if required.

**Constructor**

`new RotateTo(camera)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The camera this effect is acting upon. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/cameras/2d/effects/RotateTo.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L12)  
> Since: 3.23.0

# Public Members

## camera

### camera: [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md)

**Description:**

The Camera this effect belongs to.

> Source: [src/cameras/2d/effects/RotateTo.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L44)  
> Since: 3.23.0

---

## clockwise

### clockwise: boolean

**Description:**

The direction of the rotation.

> Source: [src/cameras/2d/effects/RotateTo.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L160)  
> Since: 3.23.0

---

## current

### current: number

**Description:**

The constantly updated value based on the force.

> Source: [src/cameras/2d/effects/RotateTo.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L85)  
> Since: 3.23.0

---

## destination

### destination: number

**Description:**

The destination angle in radians to rotate the camera to.

> Source: [src/cameras/2d/effects/RotateTo.js#L94](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L94)  
> Since: 3.23.0

---

## duration

### duration: number

**Description:**

The duration of the effect, in milliseconds.

> Source: [src/cameras/2d/effects/RotateTo.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L65)  
> Since: 3.23.0

---

## ease

### ease: function

**Description:**

The ease function to use during the Rotate.

> Source: [src/cameras/2d/effects/RotateTo.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L103)  
> Since: 3.23.0

---

## isRunning

### isRunning: boolean

**Description:**

Is this effect actively running?

> Source: [src/cameras/2d/effects/RotateTo.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L54)  
> Since: 3.23.0

---

## progress

### progress: number

**Description:**

If this effect is running this holds the current percentage of the progress, a value between 0 and 1.

> Source: [src/cameras/2d/effects/RotateTo.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L112)  
> Since: 3.23.0

---

## shortestPath

### shortestPath: boolean

**Description:**

The shortest direction to the target rotation.

> Source: [src/cameras/2d/effects/RotateTo.js#L169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L169)  
> Since: 3.23.0

---

## source

### source: number

**Description:**

The starting angle to rotate the camera from.

> Source: [src/cameras/2d/effects/RotateTo.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L76)  
> Since: 3.23.0

---

# Private Members

## \_elapsed

### \_elapsed: number

**Description:**

Effect elapsed timer.

**Access:** private

> Source: [src/cameras/2d/effects/RotateTo.js#L121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L121)  
> Since: 3.23.0

---

## \_onUpdate

### \_onUpdate: CameraRotateCallback

**Description:**

This callback is invoked every frame for the duration of the effect.

**Access:** private

> Source: [src/cameras/2d/effects/RotateTo.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L139)  
> Since: 3.23.0

---

## \_onUpdateScope

### \_onUpdateScope: any

**Description:**

On Complete callback scope.

**Access:** private

> Source: [src/cameras/2d/effects/RotateTo.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L150)  
> Since: 3.23.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this effect, releasing it from the Camera.

> Source: [src/cameras/2d/effects/RotateTo.js#L410](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L410)  
> Since: 3.23.0

---

## effectComplete

### <instance> effectComplete()

**Description:**

Called internally when the effect completes.

> Source: [src/cameras/2d/effects/RotateTo.js#L379](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L379)  
> Since: 3.23.0

---

## reset

### <instance> reset()

**Description:**

Resets this camera effect.

If it was previously running, it stops instantly without calling its onComplete callback or emitting an event.

> Source: [src/cameras/2d/effects/RotateTo.js#L395](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L395)  
> Since: 3.23.0

---

## start

### <instance> start(radians, [shortestPath], [duration], [ease], [force], [callback], [context])

**Description:**

This effect will scroll the Camera so that the center of its viewport finishes at the given angle,

over the duration and with the ease specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| radians | number | No |  | The destination angle in radians to rotate the Camera viewport to. If the angle is positive then the rotation is clockwise else anticlockwise |
| --- | --- | --- | --- | --- |
| shortestPath | boolean | Yes | false | If shortest path is set to true the camera will rotate in the quickest direction clockwise or anti-clockwise. |
| duration | number | Yes | 1000 | The duration of the effect in milliseconds. |
| ease | string | function | Yes | "'Linear'" | The ease to use for the Rotate. Can be any of the Phaser Easing constants or a custom function. |
| force | boolean | Yes | false | Force the rotation effect to start immediately, even if already running. |
| callback | CameraRotateCallback | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent four arguments: A reference to the camera, a progress amount between 0 and 1 indicating how complete the effect is, the current camera scroll x coordinate and the current camera scroll y coordinate. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - The Camera on which the effect was started.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:ROTATE\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:ROTATE\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/effects/RotateTo.js#L179](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L179)  
> Since: 3.23.0

---

## update

### <instance> update(time, delta)

**Description:**

The main update loop for this effect. Called automatically by the Camera.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp as generated by the Request Animation Frame or SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time, in ms, elapsed since the last frame. |

> Source: [src/cameras/2d/effects/RotateTo.js#L299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/RotateTo.js#L299)  
> Since: 3.23.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [camera](#camera)

    - [camera: Phaser.Cameras.Scene2D.Camera](#camera-phasercamerasscene2dcamera)
  + [clockwise](#clockwise)

    - [clockwise: boolean](#clockwise-boolean)
  + [current](#current)

    - [current: number](#current-number)
  + [destination](#destination)

    - [destination: number](#destination-number)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [ease](#ease)

    - [ease: function](#ease-function)
  + [isRunning](#isrunning)

    - [isRunning: boolean](#isrunning-boolean)
  + [progress](#progress)

    - [progress: number](#progress-number)
  + [shortestPath](#shortestpath)

    - [shortestPath: boolean](#shortestpath-boolean)
  + [source](#source)

    - [source: number](#source-number)
* [Private Members](#private-members)

  + [\_elapsed](#_elapsed)

    - [\_elapsed: number](#_elapsed-number)
  + [\_onUpdate](#_onupdate)

    - [\_onUpdate: CameraRotateCallback](#_onupdate-camerarotatecallback)
  + [\_onUpdateScope](#_onupdatescope)

    - [\_onUpdateScope: any](#_onupdatescope-any)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [effectComplete](#effectcomplete)

    - [<instance> effectComplete()](#instance-effectcomplete)
  + [reset](#reset)

    - [<instance> reset()](#instance-reset)
  + [start](#start)

    - [<instance> start(radians, [shortestPath], [duration], [ease], [force], [callback], [context])](#instance-startradians-shortestpath-duration-ease-force-callback-context)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)

Back to top

©2025[Phaser](https://docs.phaser.io)