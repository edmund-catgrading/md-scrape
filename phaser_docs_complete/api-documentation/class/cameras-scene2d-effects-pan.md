# Pan

Phaser.Cameras.Scene2D.Effects.Pan

A Camera Pan effect.

This effect will scroll the Camera so that the center of its viewport finishes at the given destination,

over the duration and with the ease specified.

Only the camera scroll is moved. None of the objects it is displaying are impacted, i.e. their positions do

not change.

The effect will dispatch several events on the Camera itself and you can also specify an `onUpdate` callback,

which is invoked each frame for the duration of the effect if required.

**Constructor**

`new Pan(camera)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The camera this effect is acting upon. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/cameras/2d/effects/Pan.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L13)  
> Since: 3.11.0

# Public Members

## camera

### camera: [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md)

**Description:**

The Camera this effect belongs to.

> Source: [src/cameras/2d/effects/Pan.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L39)  
> Since: 3.11.0

---

## current

### current: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The constantly updated value based on zoom.

> Source: [src/cameras/2d/effects/Pan.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L80)  
> Since: 3.11.0

---

## destination

### destination: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The destination scroll coordinates to pan the camera to.

> Source: [src/cameras/2d/effects/Pan.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L89)  
> Since: 3.11.0

---

## duration

### duration: number

**Description:**

The duration of the effect, in milliseconds.

> Source: [src/cameras/2d/effects/Pan.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L60)  
> Since: 3.11.0

---

## ease

### ease: function

**Description:**

The ease function to use during the pan.

> Source: [src/cameras/2d/effects/Pan.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L98)  
> Since: 3.11.0

---

## isRunning

### isRunning: boolean

**Description:**

Is this effect actively running?

> Source: [src/cameras/2d/effects/Pan.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L49)  
> Since: 3.11.0

---

## progress

### progress: number

**Description:**

If this effect is running this holds the current percentage of the progress, a value between 0 and 1.

> Source: [src/cameras/2d/effects/Pan.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L107)  
> Since: 3.11.0

---

## source

### source: [Phaser.Math.Vector2](math-vector2.md)

**Description:**

The starting scroll coordinates to pan the camera from.

> Source: [src/cameras/2d/effects/Pan.js#L71](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L71)  
> Since: 3.11.0

---

# Private Members

## \_elapsed

### \_elapsed: number

**Description:**

Effect elapsed timer.

**Access:** private

> Source: [src/cameras/2d/effects/Pan.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L116)  
> Since: 3.11.0

---

## \_onUpdate

### \_onUpdate: [Phaser.Types.Cameras.Scene2D.CameraPanCallback](../typedef/types-cameras-scene2d.md)

**Description:**

This callback is invoked every frame for the duration of the effect.

**Access:** private

> Source: [src/cameras/2d/effects/Pan.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L126)  
> Since: 3.11.0

---

## \_onUpdateScope

### \_onUpdateScope: any

**Description:**

On Complete callback scope.

**Access:** private

> Source: [src/cameras/2d/effects/Pan.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L137)  
> Since: 3.11.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this effect, releasing it from the Camera.

> Source: [src/cameras/2d/effects/Pan.js#L302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L302)  
> Since: 3.11.0

---

## effectComplete

### <instance> effectComplete()

**Description:**

Called internally when the effect completes.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:PAN\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/effects/Pan.js#L270](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L270)  
> Since: 3.11.0

---

## reset

### <instance> reset()

**Description:**

Resets this camera effect.

If it was previously running, it stops instantly without calling its onComplete callback or emitting an event.

> Source: [src/cameras/2d/effects/Pan.js#L287](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L287)  
> Since: 3.11.0

---

## start

### <instance> start(x, y, [duration], [ease], [force], [callback], [context])

**Description:**

This effect will scroll the Camera so that the center of its viewport finishes at the given destination,

over the duration and with the ease specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The destination x coordinate to scroll the center of the Camera viewport to. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The destination y coordinate to scroll the center of the Camera viewport to. |
| duration | number | Yes | 1000 | The duration of the effect in milliseconds. |
| ease | string | function | Yes | "'Linear'" | The ease to use for the pan. Can be any of the Phaser Easing constants or a custom function. |
| force | boolean | Yes | false | Force the pan effect to start immediately, even if already running. |
| callback | [Phaser.Types.Cameras.Scene2D.CameraPanCallback](../typedef/types-cameras-scene2d.md) | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent four arguments: A reference to the camera, a progress amount between 0 and 1 indicating how complete the effect is, the current camera scroll x coordinate and the current camera scroll y coordinate. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - The Camera on which the effect was started.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:PAN\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:PAN\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/effects/Pan.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L148)  
> Since: 3.11.0

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

> Source: [src/cameras/2d/effects/Pan.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Pan.js#L217)  
> Since: 3.11.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [camera](#camera)

    - [camera: Phaser.Cameras.Scene2D.Camera](#camera-phasercamerasscene2dcamera)
  + [current](#current)

    - [current: Phaser.Math.Vector2](#current-phasermathvector2)
  + [destination](#destination)

    - [destination: Phaser.Math.Vector2](#destination-phasermathvector2)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [ease](#ease)

    - [ease: function](#ease-function)
  + [isRunning](#isrunning)

    - [isRunning: boolean](#isrunning-boolean)
  + [progress](#progress)

    - [progress: number](#progress-number)
  + [source](#source)

    - [source: Phaser.Math.Vector2](#source-phasermathvector2)
* [Private Members](#private-members)

  + [\_elapsed](#_elapsed)

    - [\_elapsed: number](#_elapsed-number)
  + [\_onUpdate](#_onupdate)

    - [\_onUpdate: Phaser.Types.Cameras.Scene2D.CameraPanCallback](#_onupdate-phasertypescamerasscene2dcamerapancallback)
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

    - [<instance> start(x, y, [duration], [ease], [force], [callback], [context])](#instance-startx-y-duration-ease-force-callback-context)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)

Back to top

©2025[Phaser](https://docs.phaser.io)