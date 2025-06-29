# Shake

Phaser.Cameras.Scene2D.Effects.Shake

A Camera Shake effect.

This effect will shake the camera viewport by a random amount, bounded by the specified intensity, each frame.

Only the camera viewport is moved. None of the objects it is displaying are impacted, i.e. their positions do

not change.

The effect will dispatch several events on the Camera itself and you can also specify an `onUpdate` callback,

which is invoked each frame for the duration of the effect if required.

**Constructor**

`new Shake(camera)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The camera this effect is acting upon. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/cameras/2d/effects/Shake.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L12)  
> Since: 3.5.0

# Public Members

## camera

### camera: [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md)

**Description:**

The Camera this effect belongs to.

> Source: [src/cameras/2d/effects/Shake.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L37)  
> Since: 3.5.0

---

## duration

### duration: number

**Description:**

The duration of the effect, in milliseconds.

> Source: [src/cameras/2d/effects/Shake.js#L58](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L58)  
> Since: 3.5.0

---

## intensity

### intensity: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The intensity of the effect. Use small float values. The default when the effect starts is 0.05.

This is a Vector2 object, allowing you to control the shake intensity independently across x and y.

You can modify this value while the effect is active to create more varied shake effects.

> Source: [src/cameras/2d/effects/Shake.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L69)  
> Since: 3.5.0

---

## isRunning

### isRunning: boolean

**Description:**

Is this effect actively running?

> Source: [src/cameras/2d/effects/Shake.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L47)  
> Since: 3.5.0

---

## progress

### progress: number

**Description:**

If this effect is running this holds the current percentage of the progress, a value between 0 and 1.

> Source: [src/cameras/2d/effects/Shake.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L80)  
> Since: 3.5.0

---

# Private Members

## \_elapsed

### \_elapsed: number

**Description:**

Effect elapsed timer.

**Access:** private

> Source: [src/cameras/2d/effects/Shake.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L89)  
> Since: 3.5.0

---

## \_offsetX

### \_offsetX: number

**Description:**

How much to offset the camera by horizontally.

**Access:** private

> Source: [src/cameras/2d/effects/Shake.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L99)  
> Since: 3.0.0

---

## \_offsetY

### \_offsetY: number

**Description:**

How much to offset the camera by vertically.

**Access:** private

> Source: [src/cameras/2d/effects/Shake.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L110)  
> Since: 3.0.0

---

## \_onUpdate

### \_onUpdate: [Phaser.Types.Cameras.Scene2D.CameraShakeCallback](../typedef/types-cameras-scene2d.md)

**Description:**

This callback is invoked every frame for the duration of the effect.

**Access:** private

> Source: [src/cameras/2d/effects/Shake.js#L121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L121)  
> Since: 3.5.0

---

## \_onUpdateScope

### \_onUpdateScope: any

**Description:**

On Complete callback scope.

**Access:** private

> Source: [src/cameras/2d/effects/Shake.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L132)  
> Since: 3.5.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this effect, releasing it from the Camera.

> Source: [src/cameras/2d/effects/Shake.js#L297](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L297)  
> Since: 3.5.0

---

## effectComplete

### <instance> effectComplete()

**Description:**

Called internally when the effect completes.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:SHAKE\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/effects/Shake.js#L259](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L259)  
> Since: 3.5.0

---

## preRender

### <instance> preRender()

**Description:**

The pre-render step for this effect. Called automatically by the Camera.

> Source: [src/cameras/2d/effects/Shake.js#L198](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L198)  
> Since: 3.5.0

---

## reset

### <instance> reset()

**Description:**

Resets this camera effect.

If it was previously running, it stops instantly without calling its onComplete callback or emitting an event.

> Source: [src/cameras/2d/effects/Shake.js#L279](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L279)  
> Since: 3.5.0

---

## start

### <instance> start([duration], [intensity], [force], [callback], [context])

**Description:**

Shakes the Camera by the given intensity over the duration specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 100 | The duration of the effect in milliseconds. |
| --- | --- | --- | --- | --- |
| intensity | number | [Phaser.Math.Vector2](math-vector2.md) | Yes | 0.05 | The intensity of the shake. |
| force | boolean | Yes | false | Force the shake effect to start immediately, even if already running. |
| callback | [Phaser.Types.Cameras.Scene2D.CameraShakeCallback](../typedef/types-cameras-scene2d.md) | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - The Camera on which the effect was started.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:SHAKE\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:SHAKE\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/effects/Shake.js#L143](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L143)  
> Since: 3.5.0

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

> Source: [src/cameras/2d/effects/Shake.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Shake.js#L212)  
> Since: 3.5.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [camera](#camera)

    - [camera: Phaser.Cameras.Scene2D.Camera](#camera-phasercamerasscene2dcamera)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [intensity](#intensity)

    - [intensity: Phaser.Math.Vector2](#intensity-phasermathvector2)
  + [isRunning](#isrunning)

    - [isRunning: boolean](#isrunning-boolean)
  + [progress](#progress)

    - [progress: number](#progress-number)
* [Private Members](#private-members)

  + [\_elapsed](#_elapsed)

    - [\_elapsed: number](#_elapsed-number)
  + [\_offsetX](#_offsetx)

    - [\_offsetX: number](#_offsetx-number)
  + [\_offsetY](#_offsety)

    - [\_offsetY: number](#_offsety-number)
  + [\_onUpdate](#_onupdate)

    - [\_onUpdate: Phaser.Types.Cameras.Scene2D.CameraShakeCallback](#_onupdate-phasertypescamerasscene2dcamerashakecallback)
  + [\_onUpdateScope](#_onupdatescope)

    - [\_onUpdateScope: any](#_onupdatescope-any)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [effectComplete](#effectcomplete)

    - [<instance> effectComplete()](#instance-effectcomplete)
  + [preRender](#prerender)

    - [<instance> preRender()](#instance-prerender)
  + [reset](#reset)

    - [<instance> reset()](#instance-reset)
  + [start](#start)

    - [<instance> start([duration], [intensity], [force], [callback], [context])](#instance-startduration-intensity-force-callback-context)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)

Back to top

©2025[Phaser](https://docs.phaser.io)