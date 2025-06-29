# Flash

Phaser.Cameras.Scene2D.Effects.Flash

A Camera Flash effect.

This effect will flash the camera viewport to the given color, over the duration specified.

Only the camera viewport is flashed. None of the objects it is displaying are impacted, i.e. their colors do

not change.

The effect will dispatch several events on the Camera itself and you can also specify an `onUpdate` callback,

which is invoked each frame for the duration of the effect, if required.

**Constructor**

`new Flash(camera)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The camera this effect is acting upon. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/cameras/2d/effects/Flash.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L11)  
> Since: 3.5.0

# Public Members

## alpha

### alpha: number

**Description:**

The value of the alpha channel used during the flash effect.

A value between 0 and 1.

> Source: [src/cameras/2d/effects/Flash.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L101)  
> Since: 3.5.0

---

## camera

### camera: [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md)

**Description:**

The Camera this effect belongs to.

> Source: [src/cameras/2d/effects/Flash.js#L36](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L36)  
> Since: 3.5.0

---

## duration

### duration: number

**Description:**

The duration of the effect, in milliseconds.

> Source: [src/cameras/2d/effects/Flash.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L57)  
> Since: 3.5.0

---

## isRunning

### isRunning: boolean

**Description:**

Is this effect actively running?

> Source: [src/cameras/2d/effects/Flash.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L46)  
> Since: 3.5.0

---

## progress

### progress: number

**Description:**

If this effect is running this holds the current percentage of the progress, a value between 0 and 1.

> Source: [src/cameras/2d/effects/Flash.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L111)  
> Since: 3.5.0

---

# Private Members

## \_alpha

### \_alpha: number

**Description:**

This is an internal copy of the initial value of `this.alpha`, used to calculate the current alpha value of the fade effect.

**Access:** private

> Source: [src/cameras/2d/effects/Flash.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L130)  
> Since: 3.60.0

---

## \_elapsed

### \_elapsed: number

**Description:**

Effect elapsed timer.

**Access:** private

> Source: [src/cameras/2d/effects/Flash.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L120)  
> Since: 3.5.0

---

## \_onUpdate

### \_onUpdate: [Phaser.Types.Cameras.Scene2D.CameraFlashCallback](../typedef/types-cameras-scene2d.md)

**Description:**

This callback is invoked every frame for the duration of the effect.

**Access:** private

> Source: [src/cameras/2d/effects/Flash.js#L141](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L141)  
> Since: 3.5.0

---

## \_onUpdateScope

### \_onUpdateScope: any

**Description:**

On Complete callback scope.

**Access:** private

> Source: [src/cameras/2d/effects/Flash.js#L152](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L152)  
> Since: 3.5.0

---

## blue

### blue: number

**Description:**

The value of the blue color channel the camera will use for the flash effect.

A value between 0 and 255.

**Access:** private

> Source: [src/cameras/2d/effects/Flash.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L90)  
> Since: 3.5.0

---

## green

### green: number

**Description:**

The value of the green color channel the camera will use for the flash effect.

A value between 0 and 255.

**Access:** private

> Source: [src/cameras/2d/effects/Flash.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L79)  
> Since: 3.5.0

---

## red

### red: number

**Description:**

The value of the red color channel the camera will use for the flash effect.

A value between 0 and 255.

**Access:** private

> Source: [src/cameras/2d/effects/Flash.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L68)  
> Since: 3.5.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this effect, releasing it from the Camera.

> Source: [src/cameras/2d/effects/Flash.js#L341](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L341)  
> Since: 3.5.0

---

## effectComplete

### <instance> effectComplete()

**Description:**

Called internally when the effect completes.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:FLASH\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/effects/Flash.js#L308](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L308)  
> Since: 3.5.0

---

## postRenderCanvas

### <instance> postRenderCanvas(ctx)

**Description:**

Called internally by the Canvas Renderer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ctx | CanvasRenderingContext2D | No | The Canvas context to render to. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the effect drew to the renderer, otherwise `false`.

> Source: [src/cameras/2d/effects/Flash.js#L251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L251)  
> Since: 3.5.0

---

## postRenderWebGL

### <instance> postRenderWebGL(pipeline, getTintFunction)

**Description:**

Called internally by the WebGL Renderer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.Pipelines.MultiPipeline](renderer-webgl-pipelines-multipipeline.md) | No | The WebGL Pipeline to render to. Must provide the `drawFillRect` method. |
| --- | --- | --- | --- |
| getTintFunction | function | No | A function that will return the gl safe tint colors. |

**Returns:** boolean - `true` if the effect drew to the renderer, otherwise `false`.

> Source: [src/cameras/2d/effects/Flash.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L276)  
> Since: 3.5.0

---

## reset

### <instance> reset()

**Description:**

Resets this camera effect.

If it was previously running, it stops instantly without calling its onComplete callback or emitting an event.

> Source: [src/cameras/2d/effects/Flash.js#L326](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L326)  
> Since: 3.5.0

---

## start

### <instance> start([duration], [red], [green], [blue], [force], [callback], [context])

**Description:**

Flashes the Camera to or from the given color over the duration specified.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 250 | The duration of the effect in milliseconds. |
| --- | --- | --- | --- | --- |
| red | number | Yes | 255 | The amount to flash the red channel towards. A value between 0 and 255. |
| green | number | Yes | 255 | The amount to flash the green channel towards. A value between 0 and 255. |
| blue | number | Yes | 255 | The amount to flash the blue channel towards. A value between 0 and 255. |
| force | boolean | Yes | false | Force the effect to start immediately, even if already running. |
| callback | [Phaser.Types.Cameras.Scene2D.CameraFlashCallback](../typedef/types-cameras-scene2d.md) | Yes |  | This callback will be invoked every frame for the duration of the effect. It is sent two arguments: A reference to the camera and a progress amount between 0 and 1 indicating how complete the effect is. |
| context | any | Yes |  | The context in which the callback is invoked. Defaults to the Scene to which the Camera belongs. |

**Returns:** [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) - The Camera on which the effect was started.

**Fires:** [Phaser.Cameras.Scene2D.Events#event:FLASH\_START](../event/cameras-scene2d-events.md), [Phaser.Cameras.Scene2D.Events#event:FLASH\_COMPLETE](../event/cameras-scene2d-events.md)

> Source: [src/cameras/2d/effects/Flash.js#L163](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L163)  
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

> Source: [src/cameras/2d/effects/Flash.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/cameras/2d/effects/Flash.js#L216)  
> Since: 3.5.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [camera](#camera)

    - [camera: Phaser.Cameras.Scene2D.Camera](#camera-phasercamerasscene2dcamera)
  + [duration](#duration)

    - [duration: number](#duration-number)
  + [isRunning](#isrunning)

    - [isRunning: boolean](#isrunning-boolean)
  + [progress](#progress)

    - [progress: number](#progress-number)
* [Private Members](#private-members)

  + [\_alpha](#_alpha)

    - [\_alpha: number](#_alpha-number)
  + [\_elapsed](#_elapsed)

    - [\_elapsed: number](#_elapsed-number)
  + [\_onUpdate](#_onupdate)

    - [\_onUpdate: Phaser.Types.Cameras.Scene2D.CameraFlashCallback](#_onupdate-phasertypescamerasscene2dcameraflashcallback)
  + [\_onUpdateScope](#_onupdatescope)

    - [\_onUpdateScope: any](#_onupdatescope-any)
  + [blue](#blue)

    - [blue: number](#blue-number)
  + [green](#green)

    - [green: number](#green-number)
  + [red](#red)

    - [red: number](#red-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [effectComplete](#effectcomplete)

    - [<instance> effectComplete()](#instance-effectcomplete)
  + [postRenderCanvas](#postrendercanvas)

    - [<instance> postRenderCanvas(ctx)](#instance-postrendercanvasctx)
  + [postRenderWebGL](#postrenderwebgl)

    - [<instance> postRenderWebGL(pipeline, getTintFunction)](#instance-postrenderwebglpipeline-gettintfunction)
  + [reset](#reset)

    - [<instance> reset()](#instance-reset)
  + [start](#start)

    - [<instance> start([duration], [red], [green], [blue], [force], [callback], [context])](#instance-startduration-red-green-blue-force-callback-context)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)

Back to top

©2025[Phaser](https://docs.phaser.io)