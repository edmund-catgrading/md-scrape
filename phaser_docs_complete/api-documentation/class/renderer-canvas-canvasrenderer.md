# CanvasRenderer

Phaser.Renderer.Canvas.CanvasRenderer

The Canvas Renderer is responsible for managing 2D canvas rendering contexts,

including the one used by the Games canvas. It tracks the internal state of a

given context and can renderer textured Game Objects to it, taking into

account alpha, blending, and scaling.

**Constructor**

`new CanvasRenderer(game)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | The Phaser Game instance that owns this renderer. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/renderer/canvas/CanvasRenderer.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L19)  
> Since: 3.0.0

# Public Members

## antialias

### antialias: boolean

**Description:**

Should the Canvas use Image Smoothing or not when drawing Sprites?

> Source: [src/renderer/canvas/CanvasRenderer.js#L139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L139)  
> Since: 3.20.0

---

## blendModes

### blendModes: array

**Description:**

The blend modes supported by the Canvas Renderer.

This object maps the [Phaser.BlendModes](../namespace/Phaser.BlendModes.md) to canvas compositing operations.

> Source: [src/renderer/canvas/CanvasRenderer.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L148)  
> Since: 3.0.0

---

## config

### config: object

**Description:**

The local configuration settings of the CanvasRenderer.

> Source: [src/renderer/canvas/CanvasRenderer.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L46)  
> Since: 3.0.0

---

## currentContext

### currentContext: CanvasRenderingContext2D

**Description:**

The canvas context currently used by the CanvasRenderer for all rendering operations.

> Source: [src/renderer/canvas/CanvasRenderer.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L130)  
> Since: 3.0.0

---

## drawCount

### drawCount: number

**Description:**

The total number of Game Objects which were rendered in a frame.

> Source: [src/renderer/canvas/CanvasRenderer.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L78)  
> Since: 3.0.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

The Phaser Game instance that owns this renderer.

> Source: [src/renderer/canvas/CanvasRenderer.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L60)  
> Since: 3.0.0

---

## gameCanvas

### gameCanvas: HTMLCanvasElement

**Description:**

The canvas element which the Game uses.

> Source: [src/renderer/canvas/CanvasRenderer.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L106)  
> Since: 3.0.0

---

## gameContext

### gameContext: CanvasRenderingContext2D

**Description:**

The canvas context used to render all Cameras in all Scenes during the game loop.

> Source: [src/renderer/canvas/CanvasRenderer.js#L121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L121)  
> Since: 3.0.0

---

## height

### height: number

**Description:**

The height of the canvas being rendered to.

> Source: [src/renderer/canvas/CanvasRenderer.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L97)  
> Since: 3.0.0

---

## isBooted

### isBooted: boolean

**Description:**

Has this renderer fully booted yet?

> Source: [src/renderer/canvas/CanvasRenderer.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L209)  
> Since: 3.50.0

---

## snapshotState

### snapshotState: [Phaser.Types.Renderer.Snapshot.SnapshotState](../typedef/types-renderer-snapshot.md)

**Description:**

Details about the currently scheduled snapshot.

If a non-null `callback` is set in this object, a snapshot of the canvas will be taken after the current frame is fully rendered.

> Source: [src/renderer/canvas/CanvasRenderer.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L159)  
> Since: 3.16.0

---

## type

### type: number

**Description:**

A constant which allows the renderer to be easily identified as a Canvas Renderer.

> Source: [src/renderer/canvas/CanvasRenderer.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L69)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The width of the canvas being rendered to.

> Source: [src/renderer/canvas/CanvasRenderer.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L88)  
> Since: 3.0.0

---

# Private Members

## \_tempMatrix1

### \_tempMatrix1: [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md)

**Description:**

A temporary Transform Matrix, re-used internally during batching.

**Access:** private

> Source: [src/renderer/canvas/CanvasRenderer.js#L179](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L179)  
> Since: 3.11.0

---

## \_tempMatrix2

### \_tempMatrix2: [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md)

**Description:**

A temporary Transform Matrix, re-used internally during batching.

**Access:** private

> Source: [src/renderer/canvas/CanvasRenderer.js#L189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L189)  
> Since: 3.11.0

---

## \_tempMatrix3

### \_tempMatrix3: [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md)

**Description:**

A temporary Transform Matrix, re-used internally during batching.

**Access:** private

> Source: [src/renderer/canvas/CanvasRenderer.js#L199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L199)  
> Since: 3.11.0

---

# Public Methods

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

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## batchSprite

### <instance> batchSprite(sprite, frame, camera, [parentTransformMatrix])

**Description:**

Takes a Sprite Game Object, or any object that extends it, and draws it to the current context.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The texture based Game Object to draw. |
| --- | --- | --- | --- |
| frame | [Phaser.Textures.Frame](textures-frame.md) | No | The frame to draw, doesn't have to be that owned by the Game Object. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera to use for the rendering transform. |
| parentTransformMatrix | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | The transform matrix of the parent container, if set. |

> Source: [src/renderer/canvas/CanvasRenderer.js#L673](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L673)  
> Since: 3.12.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys all object references in the Canvas Renderer.

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/renderer/canvas/CanvasRenderer.js#L864](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L864)  
> Since: 3.0.0

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

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## init

### <instance> init()

**Description:**

Prepares the game canvas for rendering.

> Source: [src/renderer/canvas/CanvasRenderer.js#L221](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L221)  
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

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - `this`.

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

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - `this`.

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

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## onResize

### <instance> onResize(gameSize, baseSize)

**Description:**

The event handler that manages the `resize` event dispatched by the Scale Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameSize | [Phaser.Structs.Size](structs-size.md) | No | The default Game Size object. This is the un-modified game dimensions. |
| --- | --- | --- | --- |
| baseSize | [Phaser.Structs.Size](structs-size.md) | No | The base Size object. The game dimensions multiplied by the resolution. The canvas width / height values match this. |

> Source: [src/renderer/canvas/CanvasRenderer.js#L255](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L255)  
> Since: 3.16.0

---

## postRender

### <instance> postRender()

**Description:**

Restores the game context's global settings and takes a snapshot if one is scheduled.

The post-render step happens after all Cameras in all Scenes have been rendered.

**Fires:** [Phaser.Renderer.Events#event:POST\_RENDER](../event/renderer-events.md)

> Source: [src/renderer/canvas/CanvasRenderer.js#L511](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L511)  
> Since: 3.0.0

---

## preRender

### <instance> preRender()

**Description:**

Called at the start of the render loop.

**Fires:** [Phaser.Renderer.Events#event:PRE\_RENDER\_CLEAR](../event/renderer-events.md), [Phaser.Renderer.Events#event:PRE\_RENDER](../event/renderer-events.md)

> Source: [src/renderer/canvas/CanvasRenderer.js#L353](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L353)  
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

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

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

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## render

### <instance> render(scene, children, camera)

**Description:**

The core render step for a Scene Camera.

Iterates through the given array of Game Objects and renders them with the given Camera.

This is called by the `CameraManager.render` method. The Camera Manager instance belongs to a Scene, and is invoked

by the Scene Systems.render method.

This method is not called if `Camera.visible` is `false`, or `Camera.alpha` is zero.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to render. |
| --- | --- | --- | --- |
| children | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of filtered Game Objects that can be rendered by the given Camera. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Scene Camera to render with. |

**Fires:** [Phaser.Renderer.Events#event:RENDER](../event/renderer-events.md)

> Source: [src/renderer/canvas/CanvasRenderer.js#L393](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L393)  
> Since: 3.0.0

---

## resetTransform

### <instance> resetTransform()

**Description:**

Resets the transformation matrix of the current context to the identity matrix, thus resetting any transformation.

> Source: [src/renderer/canvas/CanvasRenderer.js#L291](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L291)  
> Since: 3.0.0

---

## resize

### <instance> resize([width], [height])

**Description:**

Resize the main game canvas.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | Yes | The new width of the renderer. |
| --- | --- | --- | --- |
| height | number | Yes | The new height of the renderer. |

**Fires:** [Phaser.Renderer.Events#event:RESIZE](../event/renderer-events.md)

> Source: [src/renderer/canvas/CanvasRenderer.js#L273](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L273)  
> Since: 3.0.0

---

## setAlpha

### <instance> setAlpha(alpha)

**Description:**

Sets the global alpha of the current context.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| alpha | number | No | The new alpha to use, where 0 is fully transparent and 1 is fully opaque. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - This CanvasRenderer object.

> Source: [src/renderer/canvas/CanvasRenderer.js#L336](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L336)  
> Since: 3.0.0

---

## setBlendMode

### <instance> setBlendMode(blendMode)

**Description:**

Sets the blend mode (compositing operation) of the current context.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| blendMode | string | No | The new blend mode which should be used. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - This CanvasRenderer object.

> Source: [src/renderer/canvas/CanvasRenderer.js#L302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L302)  
> Since: 3.0.0

---

## setContext

### <instance> setContext([ctx])

**Description:**

Changes the Canvas Rendering Context that all draw operations are performed against.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ctx | CanvasRenderingContext2D | Yes | The new Canvas Rendering Context to draw everything to. Leave empty to reset to the Game Canvas. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - The Canvas Renderer instance.

> Source: [src/renderer/canvas/CanvasRenderer.js#L319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L319)  
> Since: 3.12.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## snapshot

### <instance> snapshot(callback, [type], [encoderOptions])

**Description:**

Schedules a snapshot of the entire game viewport to be taken after the current frame is rendered.

To capture a specific area see the `snapshotArea` method. To capture a specific pixel, see `snapshotPixel`.

Only one snapshot can be active *per frame*. If you have already called `snapshotPixel`, for example, then

calling this method will override it.

Snapshots work by creating an Image object from the canvas data, this is a blocking process, which gets

more expensive the larger the canvas size gets, so please be careful how you employ this in your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](../typedef/types-renderer-snapshot.md) | No |  | The Function to invoke after the snapshot image is created. |
| --- | --- | --- | --- | --- |
| type | string | Yes | "'image/png'" | The format of the image to create, usually `image/png` or `image/jpeg`. |
| encoderOptions | number | Yes | 0.92 | The image quality, between 0 and 1. Used for image formats with lossy compression, such as `image/jpeg`. |

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - This WebGL Renderer.

> Source: [src/renderer/canvas/CanvasRenderer.js#L578](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L578)  
> Since: 3.0.0

---

## snapshotArea

### <instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions])

**Description:**

Schedules a snapshot of the given area of the game viewport to be taken after the current frame is rendered.

To capture the whole game viewport see the `snapshot` method. To capture a specific pixel, see `snapshotPixel`.

Only one snapshot can be active *per frame*. If you have already called `snapshotPixel`, for example, then

calling this method will override it.

Snapshots work by creating an Image object from the canvas data, this is a blocking process, which gets

more expensive the larger the canvas size gets, so please be careful how you employ this in your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate to grab from. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate to grab from. |
| width | number | No |  | The width of the area to grab. |
| height | number | No |  | The height of the area to grab. |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](../typedef/types-renderer-snapshot.md) | No |  | The Function to invoke after the snapshot image is created. |
| type | string | Yes | "'image/png'" | The format of the image to create, usually `image/png` or `image/jpeg`. |
| encoderOptions | number | Yes | 0.92 | The image quality, between 0 and 1. Used for image formats with lossy compression, such as `image/jpeg`. |

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - This WebGL Renderer.

> Source: [src/renderer/canvas/CanvasRenderer.js#L603](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L603)  
> Since: 3.16.0

---

## snapshotCanvas

### <instance> snapshotCanvas(canvas, callback, [getPixel], [x], [y], [width], [height], [type], [encoderOptions])

**Description:**

Takes a snapshot of the given area of the given canvas.

Unlike the other snapshot methods, this one is processed immediately and doesn't wait for the next render.

Snapshots work by creating an Image object from the canvas data, this is a blocking process, which gets

more expensive the larger the canvas size gets, so please be careful how you employ this in your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| canvas | HTMLCanvasElement | No |  | The canvas to grab from. |
| --- | --- | --- | --- | --- |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](../typedef/types-renderer-snapshot.md) | No |  | The Function to invoke after the snapshot image is created. |
| getPixel | boolean | Yes | false | Grab a single pixel as a Color object, or an area as an Image object? |
| x | number | Yes | 0 | The x coordinate to grab from. |
| y | number | Yes | 0 | The y coordinate to grab from. |
| width | number | Yes | "canvas.width" | The width of the area to grab. |
| height | number | Yes | "canvas.height" | The height of the area to grab. |
| type | string | Yes | "'image/png'" | The format of the image to create, usually `image/png` or `image/jpeg`. |
| encoderOptions | number | Yes | 0.92 | The image quality, between 0 and 1. Used for image formats with lossy compression, such as `image/jpeg`. |

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - This Canvas Renderer.

> Source: [src/renderer/canvas/CanvasRenderer.js#L538](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L538)  
> Since: 3.19.0

---

## snapshotPixel

### <instance> snapshotPixel(x, y, callback)

**Description:**

Schedules a snapshot of the given pixel from the game viewport to be taken after the current frame is rendered.

To capture the whole game viewport see the `snapshot` method. To capture a specific area, see `snapshotArea`.

Only one snapshot can be active *per frame*. If you have already called `snapshotArea`, for example, then

calling this method will override it.

Unlike the other two snapshot methods, this one will return a `Color` object containing the color data for

the requested pixel. It doesn't need to create an internal Canvas or Image object, so is a lot faster to execute,

using less memory.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the pixel to get. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the pixel to get. |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](../typedef/types-renderer-snapshot.md) | No | The Function to invoke after the snapshot pixel data is extracted. |

**Returns:** [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) - This WebGL Renderer.

> Source: [src/renderer/canvas/CanvasRenderer.js#L643](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L643)  
> Since: 3.16.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

Internal boot handler.

**Access:** private

> Source: [src/renderer/canvas/CanvasRenderer.js#L232](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/canvas/CanvasRenderer.js#L232)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [antialias](#antialias)

    - [antialias: boolean](#antialias-boolean)
  + [blendModes](#blendmodes)

    - [blendModes: array](#blendmodes-array)
  + [config](#config)

    - [config: object](#config-object)
  + [currentContext](#currentcontext)

    - [currentContext: CanvasRenderingContext2D](#currentcontext-canvasrenderingcontext2d)
  + [drawCount](#drawcount)

    - [drawCount: number](#drawcount-number)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [gameCanvas](#gamecanvas)

    - [gameCanvas: HTMLCanvasElement](#gamecanvas-htmlcanvaselement)
  + [gameContext](#gamecontext)

    - [gameContext: CanvasRenderingContext2D](#gamecontext-canvasrenderingcontext2d)
  + [height](#height)

    - [height: number](#height-number)
  + [isBooted](#isbooted)

    - [isBooted: boolean](#isbooted-boolean)
  + [snapshotState](#snapshotstate)

    - [snapshotState: Phaser.Types.Renderer.Snapshot.SnapshotState](#snapshotstate-phasertypesrenderersnapshotsnapshotstate)
  + [type](#type)

    - [type: number](#type-number)
  + [width](#width)

    - [width: number](#width-number)
* [Private Members](#private-members)

  + [\_tempMatrix1](#_tempmatrix1)

    - [\_tempMatrix1: Phaser.GameObjects.Components.TransformMatrix](#_tempmatrix1-phasergameobjectscomponentstransformmatrix)
  + [\_tempMatrix2](#_tempmatrix2)

    - [\_tempMatrix2: Phaser.GameObjects.Components.TransformMatrix](#_tempmatrix2-phasergameobjectscomponentstransformmatrix)
  + [\_tempMatrix3](#_tempmatrix3)

    - [\_tempMatrix3: Phaser.GameObjects.Components.TransformMatrix](#_tempmatrix3-phasergameobjectscomponentstransformmatrix)
* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [batchSprite](#batchsprite)

    - [<instance> batchSprite(sprite, frame, camera, [parentTransformMatrix])](#instance-batchspritesprite-frame-camera-parenttransformmatrix)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [init](#init)

    - [<instance> init()](#instance-init)
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
  + [onResize](#onresize)

    - [<instance> onResize(gameSize, baseSize)](#instance-onresizegamesize-basesize)
  + [postRender](#postrender)

    - [<instance> postRender()](#instance-postrender)
  + [preRender](#prerender)

    - [<instance> preRender()](#instance-prerender)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [render](#render)

    - [<instance> render(scene, children, camera)](#instance-renderscene-children-camera)
  + [resetTransform](#resettransform)

    - [<instance> resetTransform()](#instance-resettransform)
  + [resize](#resize)

    - [<instance> resize([width], [height])](#instance-resizewidth-height)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha(alpha)](#instance-setalphaalpha)
  + [setBlendMode](#setblendmode)

    - [<instance> setBlendMode(blendMode)](#instance-setblendmodeblendmode)
  + [setContext](#setcontext)

    - [<instance> setContext([ctx])](#instance-setcontextctx)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [snapshot](#snapshot)

    - [<instance> snapshot(callback, [type], [encoderOptions])](#instance-snapshotcallback-type-encoderoptions)
  + [snapshotArea](#snapshotarea)

    - [<instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions])](#instance-snapshotareax-y-width-height-callback-type-encoderoptions)
  + [snapshotCanvas](#snapshotcanvas)

    - [<instance> snapshotCanvas(canvas, callback, [getPixel], [x], [y], [width], [height], [type], [encoderOptions])](#instance-snapshotcanvascanvas-callback-getpixel-x-y-width-height-type-encoderoptions)
  + [snapshotPixel](#snapshotpixel)

    - [<instance> snapshotPixel(x, y, callback)](#instance-snapshotpixelx-y-callback)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)

Back to top

©2025[Phaser](https://docs.phaser.io)