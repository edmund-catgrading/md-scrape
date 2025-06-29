# PointLightPipeline

Phaser.Renderer.WebGL.Pipelines.PointLightPipeline

The Point Light Pipeline handles rendering the Point Light Game Objects in WebGL.

The fragment shader it uses can be found in `shaders/src/PointLight.frag`.

The vertex shader it uses can be found in `shaders/src/PointLight.vert`.

The default shader attributes for this pipeline are:

`inPosition` (vec2)

`inLightPosition` (vec2)

`inLightRadius` (float)

`inLightAttenuation` (float)

`inLightColor` (vec4)

The default shader uniforms for this pipeline are:

`uProjectionMatrix` (mat4)

`uResolution` (vec2)

`uCameraZoom` (sampler2D)

**Constructor**

`new PointLightPipeline(config)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Renderer.WebGL.WebGLPipelineConfig](../typedef/types-renderer-webgl.md) | No | The configuration options for this pipeline. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/pipelines/PointLightPipeline.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/PointLightPipeline.js#L13)  
> Since: 3.50.0

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

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addTextureToBatch

### <instance> addTextureToBatch(texture)

**Description:**

Adds the given texture to the current WebGL Pipeline Batch Entry and

increases the batch entry unit and maxUnit values by 1.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No | The texture assigned to this batch entry. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#addTextureToBatch](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L818](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L818)  
> Since: 3.60.0

---

## batchLightVert

### <instance> batchLightVert(x, y, lightX, lightY, radius, attenuation, r, g, b, a)

**Description:**

Adds a single Point Light vertex to the current vertex buffer and increments the

`vertexCount` property by 1.

This method is called directly by `batchPointLight`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The vertex x position. |
| --- | --- | --- | --- |
| y | number | No | The vertex y position. |
| lightX | number | No | The horizontal center of the light. |
| lightY | number | No | The vertical center of the light. |
| radius | number | No | The radius of the light. |
| attenuation | number | No | The attenuation of the light. |
| r | number | No | The red color channel of the light. |
| g | number | No | The green color channel of the light. |
| b | number | No | The blue color channel of the light. |
| a | number | No | The alpha color channel of the light. |

> Source: [src/renderer/webgl/pipelines/PointLightPipeline.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/PointLightPipeline.js#L133)  
> Since: 3.50.0

---

## batchPointLight

### <instance> batchPointLight(light, camera, x0, y0, x1, y1, x2, y2, x3, y3, lightX, lightY)

**Description:**

Adds a Point Light Game Object to the batch, flushing if required.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| light | [Phaser.GameObjects.PointLight](gameobjects-pointlight.md) | No | The Point Light Game Object. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The camera rendering the Point Light. |
| x0 | number | No | The top-left x position. |
| y0 | number | No | The top-left y position. |
| x1 | number | No | The bottom-left x position. |
| y1 | number | No | The bottom-left y position. |
| x2 | number | No | The bottom-right x position. |
| y2 | number | No | The bottom-right y position. |
| x3 | number | No | The top-right x position. |
| y3 | number | No | The top-right y position. |
| lightX | number | No | The horizontal center of the light. |
| lightY | number | No | The vertical center of the light. |

> Source: [src/renderer/webgl/pipelines/PointLightPipeline.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/PointLightPipeline.js#L82)  
> Since: 3.50.0

---

## batchQuad

### <instance> batchQuad(gameObject, x0, y0, x1, y1, x2, y2, x3, y3, u0, v0, u1, v1, tintTL, tintTR, tintBL, tintBR, tintEffect, [texture], [unit])

**Description:**

Adds the vertices data into the batch and flushes if full.

Assumes 6 vertices in the following arrangement:

```
Copy
0----3

|\  B|

| \  |

|  \ |

| A \|

|    \

1----2


```

Where tx0/ty0 = 0, tx1/ty1 = 1, tx2/ty2 = 2 and tx3/ty3 = 3

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | null | No |  | The Game Object, if any, drawing this quad. |
| --- | --- | --- | --- | --- |
| x0 | number | No |  | The top-left x position. |
| y0 | number | No |  | The top-left y position. |
| x1 | number | No |  | The bottom-left x position. |
| y1 | number | No |  | The bottom-left y position. |
| x2 | number | No |  | The bottom-right x position. |
| y2 | number | No |  | The bottom-right y position. |
| x3 | number | No |  | The top-right x position. |
| y3 | number | No |  | The top-right y position. |
| u0 | number | No |  | UV u0 value. |
| v0 | number | No |  | UV v0 value. |
| u1 | number | No |  | UV u1 value. |
| v1 | number | No |  | UV v1 value. |
| tintTL | number | No |  | The top-left tint color value. |
| tintTR | number | No |  | The top-right tint color value. |
| tintBL | number | No |  | The bottom-left tint color value. |
| tintBR | number | No |  | The bottom-right tint color value. |
| tintEffect | number | boolean | No |  | The tint effect for the shader to use. |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | Yes |  | Texture that will be assigned to the current batch if a flush occurs. |
| unit | number | Yes | 0 | Texture unit to which the texture needs to be bound. |

**Returns:** boolean - `true` if this method caused the batch to flush, otherwise `false`.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#batchQuad](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1704](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1704)  
> Since: 3.50.0

---

## batchTri

### <instance> batchTri(gameObject, x1, y1, x2, y2, x3, y3, u0, v0, u1, v1, tintTL, tintTR, tintBL, tintEffect, [texture], [unit])

**Description:**

Adds the vertices data into the batch and flushes if full.

Assumes 3 vertices in the following arrangement:

```
Copy
0

|\

| \

|  \

|   \

|    \

1-----2


```

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | null | No |  | The Game Object, if any, drawing this quad. |
| --- | --- | --- | --- | --- |
| x1 | number | No |  | The bottom-left x position. |
| y1 | number | No |  | The bottom-left y position. |
| x2 | number | No |  | The bottom-right x position. |
| y2 | number | No |  | The bottom-right y position. |
| x3 | number | No |  | The top-right x position. |
| y3 | number | No |  | The top-right y position. |
| u0 | number | No |  | UV u0 value. |
| v0 | number | No |  | UV v0 value. |
| u1 | number | No |  | UV u1 value. |
| v1 | number | No |  | UV v1 value. |
| tintTL | number | No |  | The top-left tint color value. |
| tintTR | number | No |  | The top-right tint color value. |
| tintBL | number | No |  | The bottom-left tint color value. |
| tintEffect | number | boolean | No |  | The tint effect for the shader to use. |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | Yes |  | Texture that will be assigned to the current batch if a flush occurs. |
| unit | number | Yes | 0 | Texture unit to which the texture needs to be bound. |

**Returns:** boolean - `true` if this method caused the batch to flush, otherwise `false`.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#batchTri](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1827](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1827)  
> Since: 3.50.0

---

## batchVert

### <instance> batchVert(x, y, u, v, unit, tintEffect, tint)

**Description:**

Adds a single vertex to the current vertex buffer and increments the

`vertexCount` property by 1.

This method is called directly by `batchTri` and `batchQuad`.

It does not perform any batch limit checking itself, so if you need to call

this method directly, do so in the same way that `batchQuad` does, for example.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The vertex x position. |
| --- | --- | --- | --- |
| y | number | No | The vertex y position. |
| u | number | No | UV u value. |
| v | number | No | UV v value. |
| unit | number | No | Texture unit to which the texture needs to be bound. |
| tintEffect | number | boolean | No | The tint effect for the shader to use. |
| tint | number | No | The tint color value. |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#batchVert](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1664](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1664)  
> Since: 3.50.0

---

## bind

### <instance> bind([currentShader])

**Description:**

This method is called every time the Pipeline Manager makes this pipeline the currently active one.

It binds the resources and shader needed for this pipeline, including setting the vertex buffer

and attribute pointers.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| currentShader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set as being current. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Fires:** [Phaser.Renderer.WebGL.Pipelines.Events#event:BIND](../event/renderer-webgl-pipelines-events.md)

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#bind](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1120)  
> Since: 3.0.0

---

## bindRenderTarget

### <instance> bindRenderTarget([target], [unit])

**Description:**

Activates the given Render Target texture and binds it to the

requested WebGL texture slot.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | Yes |  | The Render Target to activate and bind. |
| --- | --- | --- | --- | --- |
| unit | number | Yes | 0 | The WebGL texture ID to activate. Defaults to `gl.TEXTURE0`. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGL Pipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#bindRenderTarget](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2013](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2013)  
> Since: 3.50.0

---

## bindTexture

### <instance> bindTexture([target], [unit])

**Description:**

Activates the given WebGL Texture and binds it to the requested texture slot.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| target | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | Yes |  | Texture to activate and bind. |
| --- | --- | --- | --- | --- |
| unit | number | Yes | 0 | The WebGL texture ID to activate. Defaults to `gl.TEXTURE0`. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGL Pipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#bindTexture](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1989](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1989)  
> Since: 3.50.0

---

## boot

### <instance> boot()

**Description:**

Called when the Game has fully booted and the Renderer has finished setting up.

By this stage all Game level systems are now in place. You can perform any final tasks that the

pipeline may need, that relies on game systems such as the Texture Manager being ready.

**Fires:** [Phaser.Renderer.WebGL.Pipelines.Events#event:BOOT](../event/renderer-webgl-pipelines-events.md)

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#boot](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L463](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L463)  
> Since: 3.11.0

---

## createBatch

### <instance> createBatch(texture)

**Description:**

Creates a new WebGL Pipeline Batch Entry, sets the texture unit as zero

and pushes the entry into the batch.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No | The texture assigned to this batch entry. |
| --- | --- | --- | --- |

**Returns:** number - The texture unit that was bound.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#createBatch](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L789](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L789)  
> Since: 3.60.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys all shader instances, removes all object references and nulls all external references.

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Fires:** [Phaser.Renderer.WebGL.Pipelines.Events#event:DESTROY](../event/renderer-webgl-pipelines-events.md)

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#destroy](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2605](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2605)  
> Since: 3.0.0

---

## drawFillRect

### <instance> drawFillRect(x, y, width, height, color, alpha, [texture], [flipUV])

**Description:**

Pushes a filled rectangle into the vertex batch.

The dimensions are run through `Math.floor` before the quad is generated.

Rectangle has no transform values and isn't transformed into the local space.

Used for directly batching untransformed rectangles, such as Camera background colors.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | Horizontal top left coordinate of the rectangle. |
| --- | --- | --- | --- | --- |
| y | number | No |  | Vertical top left coordinate of the rectangle. |
| width | number | No |  | Width of the rectangle. |
| height | number | No |  | Height of the rectangle. |
| color | number | No |  | Color of the rectangle to draw. |
| alpha | number | No |  | Alpha value of the rectangle to draw. |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | Yes |  | texture that will be assigned to the current batch if a flush occurs. |
| flipUV | boolean | Yes | true | Flip the vertical UV coordinates of the texture before rendering? |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#drawFillRect](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1921](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1921)  
> Since: 3.50.0

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

## flipProjectionMatrix

### <instance> flipProjectionMatrix([flipY])

**Description:**

Adjusts this pipelines ortho Projection Matrix to flip the y

and bottom values. Call with 'false' as the parameter to flip

them back again.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| flipY | boolean | Yes | true | Flip the y and bottom values? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#flipProjectionMatrix](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1059](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1059)  
> Since: 3.60.0

---

## flush

### <instance> flush([isPostFlush])

**Description:**

Uploads the vertex data and emits a draw call for the current batch of vertices.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| isPostFlush | boolean | Yes | false | Was this flush invoked as part of a post-process, or not? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Fires:** [Phaser.Renderer.WebGL.Pipelines.Events#event:BEFORE\_FLUSH](../event/renderer-webgl-pipelines-events.md), [Phaser.Renderer.WebGL.Pipelines.Events#event:AFTER\_FLUSH](../event/renderer-webgl-pipelines-events.md)

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#flush](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1370](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1370)  
> Since: 3.0.0

---

## getShaderByName

### <instance> getShaderByName(name)

**Description:**

Searches all shaders in this pipeline for one matching the given name, then returns it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The index of the shader to set. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - The WebGLShader instance, if found.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#getShaderByName](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L662](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L662)  
> Since: 3.50.0

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

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - `this`.

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

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## onActive

### <instance> onActive(currentShader)

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called every time the Pipeline Manager makes this the active pipeline. It is called

at the end of the `WebGLPipeline.bind` method, after the current shader has been set. The current

shader is passed to this hook.

For example, if a display list has 3 Sprites in it that all use the same pipeline, this hook will

only be called for the first one, as the 2nd and 3rd Sprites do not cause the pipeline to be changed.

If you need to listen for that event instead, use the `onBind` hook.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| currentShader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | No | The shader that was set as current. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onActive](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1478](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1478)  
> Since: 3.50.0

---

## onAfterFlush

### <instance> onAfterFlush([isPostFlush])

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called immediately after this pipeline has finished flushing its batch.

It is called after the `gl.drawArrays` call.

You can perform additional post-render effects, but be careful not to call `flush`

on this pipeline from within this method, or you'll cause an infinite loop.

To apply changes pre-render, see `onBeforeFlush`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| isPostFlush | boolean | Yes | false | Was this flush invoked as part of a post-process, or not? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onAfterFlush](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1643](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1643)  
> Since: 3.50.0

---

## onBatch

### <instance> onBatch([gameObject])

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called every time the `batchQuad` or `batchTri` methods are called. If this was

as a result of a Game Object, then the Game Object reference is passed to this hook too.

This hook is called *after* the quad (or tri) has been added to the batch, so you can safely

call 'flush' from within this.

Note that Game Objects may call `batchQuad` or `batchTri` multiple times for a single draw,

for example the Graphics Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Yes | The Game Object that invoked this pipeline, if any. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onBatch](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1532](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1532)  
> Since: 3.50.0

---

## onBeforeFlush

### <instance> onBeforeFlush([isPostFlush])

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called every time this pipeline is asked to flush its batch.

It is called immediately before the `gl.bufferData` and `gl.drawArrays` calls are made, so you can

perform any final pre-render modifications. To apply changes post-render, see `onAfterFlush`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| isPostFlush | boolean | Yes | false | Was this flush invoked as part of a post-process, or not? |
| --- | --- | --- | --- | --- |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onBeforeFlush](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1626](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1626)  
> Since: 3.50.0

---

## onBind

### <instance> onBind([gameObject])

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called every time a **Game Object** asks the Pipeline Manager to use this pipeline,

even if the pipeline is already active.

Unlike the `onActive` method, which is only called when the Pipeline Manager makes this pipeline

active, this hook is called for every Game Object that requests use of this pipeline, allowing you to

perform per-object set-up, such as loading shader uniform data.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Yes | The Game Object that invoked this pipeline, if any. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onBind](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1499](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1499)  
> Since: 3.50.0

---

## onBoot

### <instance> onBoot()

**Description:**

This method is called once when this pipeline has finished being set-up

at the end of the boot process. By the time this method is called, all

of the shaders are ready and configured.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onBoot](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L599](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L599)  
> Since: 3.50.0

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

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## onDraw

### <instance> onDraw(renderTarget, [swapTarget])

**Description:**

This method is only used by Sprite FX and Post FX Pipelines and those that extend from them.

This method is called every time the `postBatch` method is called and is passed a

reference to the current render target.

At the very least a Post FX Pipeline should call `this.bindAndDraw(renderTarget)`,

however, you can do as much additional processing as you like in this method if

you override it from within your own pipelines.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderTarget | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | No | The Render Target. |
| --- | --- | --- | --- |
| swapTarget | [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) | Yes | A Swap Render Target, useful for double-buffer effects. Only set by SpriteFX Pipelines. |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onDraw](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1335](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1335)  
> Since: 3.50.0

---

## onPostBatch

### <instance> onPostBatch([gameObject])

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called immediately after a **Game Object** has been added to the batch.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Yes | The Game Object that invoked this pipeline, if any. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onPostBatch](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1567](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1567)  
> Since: 3.50.0

---

## onPostRender

### <instance> onPostRender()

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called *once per frame*, after all rendering has happened and snapshots have been taken.

It is called at the very end of the rendering process, once all Cameras, for all Scenes, have

been rendered.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onPostRender](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1611](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1611)  
> Since: 3.50.0

---

## onPreBatch

### <instance> onPreBatch([gameObject])

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called immediately before a **Game Object** is about to add itself to the batch.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Yes | The Game Object that invoked this pipeline, if any. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onPreBatch](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1553](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1553)  
> Since: 3.50.0

---

## onPreRender

### <instance> onPreRender()

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called once per frame, right before anything has been rendered, but after the canvas

has been cleared. If this pipeline has a render target, it will also have been cleared by this point.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onPreRender](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1581](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1581)  
> Since: 3.50.0

---

## onRebind

### <instance> onRebind()

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called when the Pipeline Manager needs to rebind this pipeline. This happens after a

pipeline has been cleared, usually when passing control over to a 3rd party WebGL library, like Spine,

and then returing to Phaser again.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onRebind](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1518](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1518)  
> Since: 3.50.0

---

## onRender

### <instance> onRender(scene, camera)

**Description:**

By default this is an empty method hook that you can override and use in your own custom pipelines.

This method is called *once per frame*, by every Camera in a Scene that wants to render.

It is called at the start of the rendering process, before anything has been drawn to the Camera.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene being rendered. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Scene Camera being rendered with. |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onRender](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1594](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1594)  
> Since: 3.50.0

---

## onResize

### <instance> onResize(width, height)

**Description:**

This method is called once when this pipeline has finished being set-up

at the end of the boot process. By the time this method is called, all

of the shaders are ready and configured. It's also called if the renderer

changes size.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of this WebGL Pipeline. |
| --- | --- | --- | --- |
| height | number | No | The new height of this WebGL Pipeline. |

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#onResize](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L611](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L611)  
> Since: 3.50.0

---

## postBatch

### <instance> postBatch([gameObject])

**Description:**

This method is called as a result of the `WebGLPipeline.batchQuad` method, right after a quad

belonging to a Game Object has been added to the batch. When this is called, the

renderer has just performed a flush.

It calls the `onDraw` hook followed by the `onPostBatch` hook, which can be used to perform

additional Post FX Pipeline processing.

It is also called as part of the `PipelineManager.postBatch` method when processing Post FX Pipelines.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Game Object or Camera that invoked this pipeline, if any. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#postBatch](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1309](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1309)  
> Since: 3.50.0

---

## preBatch

### <instance> preBatch([gameObject])

**Description:**

This method is called as a result of the `WebGLPipeline.batchQuad` method, right before a quad

belonging to a Game Object is about to be added to the batch. When this is called, the

renderer has just performed a flush. It will bind the current render target, if any are set

and finally call the `onPreBatch` hook.

It is also called as part of the `PipelineManager.preBatch` method when processing Post FX Pipelines.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | Yes | The Game Object or Camera that invoked this pipeline, if any. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#preBatch](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1282](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1282)  
> Since: 3.50.0

---

## pushBatch

### <instance> pushBatch(texture)

**Description:**

Takes the given WebGLTextureWrapper and determines what to do with it.

If there is no current batch (i.e. after a flush) it will create a new

batch from it.

If the texture is already bound, it will return the current texture unit.

If the texture already exists in the current batch, the unit gets reset

to match it.

If the texture cannot be found in the current batch, and it supports

multiple textures, it's added into the batch and the unit indexes are

advanced.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No | The texture assigned to this batch entry. |
| --- | --- | --- | --- |

**Returns:** number - The texture unit that was bound.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#pushBatch](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L839](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L839)  
> Since: 3.60.0

---

## rebind

### <instance> rebind([currentShader])

**Description:**

This method is called every time the Pipeline Manager rebinds this pipeline.

It resets all shaders this pipeline uses, setting their attributes again.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| currentShader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set as being current. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Fires:** [Phaser.Renderer.WebGL.Pipelines.Events#event:REBIND](../event/renderer-webgl-pipelines-events.md)

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#rebind](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1169)  
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

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - `this`.

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

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## resize

### <instance> resize(width, height)

**Description:**

Resizes the properties used to describe the viewport.

This method is called automatically by the renderer during its resize handler.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of this WebGL Pipeline. |
| --- | --- | --- | --- |
| height | number | No | The new height of this WebGL Pipeline. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Fires:** [Phaser.Renderer.WebGL.Pipelines.Events#event:RESIZE](../event/renderer-webgl-pipelines-events.md)

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#resize](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L966](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L966)  
> Since: 3.0.0

---

## restoreContext

### <instance> restoreContext()

**Description:**

This method is called if the WebGL context is lost and restored.

It ensures that uniforms are synced back to the GPU

for all shaders in this pipeline.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#restoreContext](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1214](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1214)  
> Since: 3.80.0

---

## set1f

### <instance> set1f(name, x, [shader])

**Description:**

Sets a 1f uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new value of the `float` uniform. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set1f](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2077](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2077)  
> Since: 3.50.0

---

## set1fv

### <instance> set1fv(name, arr, [shader])

**Description:**

Sets a 1fv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set1fv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2191](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2191)  
> Since: 3.50.0

---

## set1i

### <instance> set1i(name, x, [shader])

**Description:**

Sets a 1i uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new value of the `int` uniform. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set1i](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2407](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2407)  
> Since: 3.50.0

---

## set1iv

### <instance> set1iv(name, arr, [shader])

**Description:**

Sets a 1iv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set1iv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2299](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2299)  
> Since: 3.50.0

---

## set2f

### <instance> set2f(name, x, y, [shader])

**Description:**

Sets a 2f uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new X component of the `vec2` uniform. |
| y | number | No | The new Y component of the `vec2` uniform. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set2f](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2104)  
> Since: 3.50.0

---

## set2fv

### <instance> set2fv(name, arr, [shader])

**Description:**

Sets a 2fv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set2fv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2218](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2218)  
> Since: 3.50.0

---

## set2i

### <instance> set2i(name, x, y, [shader])

**Description:**

Sets a 2i uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new X component of the `ivec2` uniform. |
| y | number | No | The new Y component of the `ivec2` uniform. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set2i](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2434](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2434)  
> Since: 3.50.0

---

## set2iv

### <instance> set2iv(name, arr, [shader])

**Description:**

Sets a 2iv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set2iv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2326](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2326)  
> Since: 3.50.0

---

## set3f

### <instance> set3f(name, x, y, z, [shader])

**Description:**

Sets a 3f uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new X component of the `vec3` uniform. |
| y | number | No | The new Y component of the `vec3` uniform. |
| z | number | No | The new Z component of the `vec3` uniform. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set3f](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2132)  
> Since: 3.50.0

---

## set3fv

### <instance> set3fv(name, arr, [shader])

**Description:**

Sets a 3fv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set3fv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2245)  
> Since: 3.50.0

---

## set3i

### <instance> set3i(name, x, y, z, [shader])

**Description:**

Sets a 3i uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new X component of the `ivec3` uniform. |
| y | number | No | The new Y component of the `ivec3` uniform. |
| z | number | No | The new Z component of the `ivec3` uniform. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set3i](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2462](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2462)  
> Since: 3.50.0

---

## set3iv

### <instance> set3iv(name, arr, [shader])

**Description:**

Sets a 3iv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set3iv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2353](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2353)  
> Since: 3.50.0

---

## set4f

### <instance> set4f(name, x, y, z, w, [shader])

**Description:**

Sets a 4f uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | X component of the uniform |
| y | number | No | Y component of the uniform |
| z | number | No | Z component of the uniform |
| w | number | No | W component of the uniform |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set4f](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2161)  
> Since: 3.50.0

---

## set4fv

### <instance> set4fv(name, arr, [shader])

**Description:**

Sets a 4fv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set4fv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2272)  
> Since: 3.50.0

---

## set4i

### <instance> set4i(name, x, y, z, w, [shader])

**Description:**

Sets a 4i uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | X component of the uniform. |
| y | number | No | Y component of the uniform. |
| z | number | No | Z component of the uniform. |
| w | number | No | W component of the uniform. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set4i](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2491](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2491)  
> Since: 3.50.0

---

## set4iv

### <instance> set4iv(name, arr, [shader])

**Description:**

Sets a 4iv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#set4iv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2380](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2380)  
> Since: 3.50.0

---

## setBoolean

### <instance> setBoolean(name, value, [shader])

**Description:**

Sets a boolean uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| value | boolean | No | The new value of the `boolean` uniform. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setBoolean](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2050](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2050)  
> Since: 3.60.0

---

## setGameObject

### <instance> setGameObject(gameObject, [frame])

**Description:**

Custom pipelines can use this method in order to perform any required pre-batch tasks

for the given Game Object. It must return the texture unit the Game Object was assigned.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object being rendered or added to the batch. |
| --- | --- | --- | --- |
| frame | [Phaser.Textures.Frame](textures-frame.md) | Yes | Optional frame to use. Can override that of the Game Object. |

**Returns:** number - The texture unit the Game Object has been assigned.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setGameObject](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L912](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L912)  
> Since: 3.50.0

---

## setMatrix2fv

### <instance> setMatrix2fv(name, transpose, matrix, [shader])

**Description:**

Sets a matrix 2fv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| transpose | boolean | No | Whether to transpose the matrix. Should be `false`. |
| matrix | Array.<number> | Float32Array | No | The new values for the `mat2` uniform. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setMatrix2fv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2521](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2521)  
> Since: 3.50.0

---

## setMatrix3fv

### <instance> setMatrix3fv(name, transpose, matrix, [shader])

**Description:**

Sets a matrix 3fv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| transpose | boolean | No | Whether to transpose the matrix. Should be `false`. |
| matrix | Float32Array | No | The new values for the `mat3` uniform. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setMatrix3fv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2549](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2549)  
> Since: 3.50.0

---

## setMatrix4fv

### <instance> setMatrix4fv(name, transpose, matrix, [shader])

**Description:**

Sets a matrix 4fv uniform value based on the given name on the currently set shader.

The current shader is bound, before the uniform is set, making it active within the

WebGLRenderer. This means you can safely call this method from a location such as

a Scene `create` or `update` method. However, when working within a Shader file

directly, use the `WebGLShader` method equivalent instead, to avoid the program

being set.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| transpose | boolean | No | Whether to transpose the matrix. Should be `false`. |
| matrix | Float32Array | No | The matrix data. If using a Matrix4 this should be the `Matrix4.val` property. |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setMatrix4fv](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2577](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2577)  
> Since: 3.50.0

---

## setProjectionMatrix

### <instance> setProjectionMatrix(width, height)

**Description:**

Adjusts this pipelines ortho Projection Matrix to use the given dimensions

and resets the `uProjectionMatrix` uniform on all bound shaders.

This method is called automatically by the renderer during its resize handler.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of this WebGL Pipeline. |
| --- | --- | --- | --- |
| height | number | No | The new height of this WebGL Pipeline. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setProjectionMatrix](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1011](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1011)  
> Since: 3.50.0

---

## setShader

### <instance> setShader(shader, [setAttributes], [vertexBuffer])

**Description:**

Sets the currently active shader within this pipeline.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | No |  | The shader to set as being current. |
| --- | --- | --- | --- | --- |
| setAttributes | boolean | Yes | false | Should the vertex attribute pointers be set? |
| vertexBuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](renderer-webgl-wrappers-webglbufferwrapper.md) | Yes |  | The vertex buffer to be set before the shader is bound. Defaults to the one owned by this pipeline. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setShader](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L627](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L627)  
> Since: 3.50.0

---

## setShadersFromConfig

### <instance> setShadersFromConfig(config)

**Description:**

Destroys all shaders currently set in the `WebGLPipeline.shaders` array and then parses the given

`config` object, extracting the shaders from it, creating `WebGLShader` instances and finally

setting them into the `shaders` array of this pipeline.

This is a destructive process. Be very careful when you call it, should you need to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Renderer.WebGL.WebGLPipelineConfig](../typedef/types-renderer-webgl.md) | No | The configuration object for this WebGL Pipeline. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setShadersFromConfig](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L685](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L685)  
> Since: 3.50.0

---

## setTexture2D

### <instance> setTexture2D([texture])

**Description:**

Sets the texture to be bound to the next available texture unit and returns

the unit id.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | Yes | Texture that will be assigned to the current batch. If not given uses `whiteTexture`. |
| --- | --- | --- | --- |

**Returns:** number - The assigned texture unit.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setTexture2D](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1971](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1971)  
> Since: 3.50.0

---

## setTime

### <instance> setTime(name, [shader])

**Description:**

Sets the current duration into a 1f uniform value based on the given name.

This can be used for mapping time uniform values, such as `iTime`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| shader | [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) | Yes | The shader to set the value on. If not given, the `currentShader` is used. |

**Returns:** [Phaser.Renderer.WebGL.Pipelines.PointLightPipeline](renderer-webgl-pipelines-pointlightpipeline.md) - This WebGLPipeline instance.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setTime](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L2030](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L2030)  
> Since: 3.50.0

---

## setVertexBuffer

### <instance> setVertexBuffer([buffer])

**Description:**

Binds the vertex buffer to be the active ARRAY\_BUFFER on the WebGL context.

It first checks to see if it's already set as the active buffer and only

binds itself if not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| buffer | [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](renderer-webgl-wrappers-webglbufferwrapper.md) | Yes | The Vertex Buffer to be bound. Defaults to the one owned by this pipeline. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the vertex buffer was bound, or `false` if it was already bound.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#setVertexBuffer](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1251)  
> Since: 3.50.0

---

## shouldFlush

### <instance> shouldFlush([amount])

**Description:**

Check if the current batch of vertices is full.

You can optionally provide an `amount` parameter. If given, it will check if the batch

needs to flush *if* the `amount` is added to it. This allows you to test if you should

flush before populating the batch.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| amount | number | Yes | 0 | Will the batch need to flush if this many vertices are added to it? |
| --- | --- | --- | --- | --- |

**Returns:** boolean - `true` if the current batch should be flushed, otherwise `false`.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#shouldFlush](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L931](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L931)  
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

## unbind

### <instance> unbind()

**Description:**

This method is called every time the Pipeline Manager deactivates this pipeline, swapping from

it to another one. This happens after a call to `flush` and before the new pipeline is bound.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#unbind](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1355](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1355)  
> Since: 3.50.0

---

## updateProjectionMatrix

### <instance> updateProjectionMatrix()

**Description:**

Adjusts this pipelines ortho Projection Matrix to match that of the global

WebGL Renderer Projection Matrix.

This method is called automatically by the Pipeline Manager when this

pipeline is set.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#updateProjectionMatrix](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L1096](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L1096)  
> Since: 3.50.0

---

## vertexAvailable

### <instance> vertexAvailable()

**Description:**

Returns the number of vertices that can be added to the current batch before

it will trigger a flush to happen.

**Returns:** number - The number of vertices that can still be added to the current batch before it will flush.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#vertexAvailable](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L952](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L952)  
> Since: 3.60.0

---

# Public Members

## active

### active: boolean

**Description:**

Indicates if the current pipeline is active, or not.

Toggle this property to enable or disable a pipeline from rendering anything.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#active](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L234](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L234)  
> Since: 3.10.0

---

## activeBuffer

### activeBuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](renderer-webgl-wrappers-webglbufferwrapper.md)

**Description:**

The currently active WebGLBuffer.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#activeBuffer](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L187)  
> Since: 3.60.0

---

## activeTextures

### activeTextures: Array.<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md)>

**Description:**

The currently active WebGLTextures, used as part of the batch process.

Reset to empty as part of the bind method.

Treat this array as read-only.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#activeTextures](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L438](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L438)  
> Since: 3.60.0

---

## batch

### batch: Array.<[Phaser.Types.Renderer.WebGL.WebGLPipelineBatchEntry](../typedef/types-renderer-webgl.md)>

**Description:**

The temporary Pipeline batch. This array contains the batch entries for

the current frame, which is a package of textures and vertex offsets used

for drawing. This package is built dynamically as the frame is built

and cleared during the flush method.

Treat this array and all of its contents as read-only.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#batch](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L387)  
> Since: 3.60.0

---

## bytes

### bytes: Uint8Array

**Description:**

Uint8 view to the `vertexData` ArrayBuffer. Used for uploading vertex buffer resources to the GPU.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#bytes](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L207](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L207)  
> Since: 3.0.0

---

## config

### config: [Phaser.Types.Renderer.WebGL.WebGLPipelineConfig](../typedef/types-renderer-webgl.md)

**Description:**

The configuration object that was used to create this pipeline.

Treat this object as 'read only', because changing it post-creation will not

impact this pipeline in any way. However, it is used internally for cloning

and post-boot set-up.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#config](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L361](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L361)  
> Since: 3.50.0

---

## currentBatch

### currentBatch: [Phaser.Types.Renderer.WebGL.WebGLPipelineBatchEntry](../typedef/types-renderer-webgl.md)

**Description:**

The most recently created Pipeline batch entry.

Reset to null as part of the flush method.

Treat this value as read-only.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#currentBatch](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L401](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L401)  
> Since: 3.60.0

---

## currentRenderTarget

### currentRenderTarget: [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md)

**Description:**

A reference to the currently bound Render Target instance from the `WebGLPipeline.renderTargets` array.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#currentRenderTarget](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L298](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L298)  
> Since: 3.50.0

---

## currentShader

### currentShader: [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md)

**Description:**

A reference to the currently bound WebGLShader instance from the `WebGLPipeline.shaders` array.

For lots of pipelines, this is the only shader, so it is a quick way to reference it without

an array look-up.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#currentShader](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L322](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L322)  
> Since: 3.50.0

---

## currentTexture

### currentTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md)

**Description:**

The most recently bound texture, used as part of the batch process.

Reset to null as part of the flush method.

Treat this value as read-only.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#currentTexture](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L414](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L414)  
> Since: 3.60.0

---

## currentUnit

### currentUnit: number

**Description:**

Holds the most recently assigned texture unit.

Treat this value as read-only.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#currentUnit](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L427](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L427)  
> Since: 3.50.0

---

## forceZero

### forceZero: boolean

**Description:**

Some pipelines require the forced use of texture zero (like the light pipeline).

This property should be set when that is the case.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#forceZero](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L245)  
> Since: 3.50.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

The Phaser Game instance to which this pipeline is bound.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#game](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L74](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L74)  
> Since: 3.0.0

---

## gl

### gl: WebGLRenderingContext

**Description:**

The WebGL context this WebGL Pipeline uses.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#gl](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L104)  
> Since: 3.0.0

---

## glReset

### glReset: boolean

**Description:**

Has the GL Context been reset to the Phaser defaults since the last time

this pipeline was bound? This is set automatically when the Pipeline Manager

resets itself, usually after handing off to a 3rd party renderer like Spine.

You should treat this property as read-only.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#glReset](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L374](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L374)  
> Since: 3.53.0

---

## hasBooted

### hasBooted: boolean

**Description:**

Indicates if this pipeline has booted or not.

A pipeline boots only when the Game instance itself, and all associated systems, is

fully ready.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#hasBooted](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L256](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L256)  
> Since: 3.50.0

---

## height

### height: number

**Description:**

Height of the current viewport.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#height](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L131](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L131)  
> Since: 3.0.0

---

## isPostFX

### isPostFX: boolean

**Description:**

Indicates if this is a Post FX Pipeline, or not.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#isPostFX](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L269](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L269)  
> Since: 3.50.0

---

## isPreFX

### isPreFX: boolean

**Description:**

Indicates if this is a Pre FX Pipeline, or not.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#isPreFX](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L279](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L279)  
> Since: 3.60.0

---

## manager

### manager: [Phaser.Renderer.WebGL.PipelineManager](renderer-webgl-pipelinemanager.md)

**Description:**

A reference to the WebGL Pipeline Manager.

This is initially undefined and only set when this pipeline is added

to the manager.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#manager](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L92)  
> Since: 3.50.0

---

## name

### name: string

**Description:**

Name of the pipeline. Used for identification and setting from Game Objects.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#name](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L65)  
> Since: 3.0.0

---

## projectionHeight

### projectionHeight: number

**Description:**

The cached height of the Projection matrix.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#projectionHeight](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L352](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L352)  
> Since: 3.50.0

---

## projectionMatrix

### projectionMatrix: [Phaser.Math.Matrix4](math-matrix4.md)

**Description:**

The Projection matrix, used by shaders as 'uProjectionMatrix' uniform.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#projectionMatrix](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L334](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L334)  
> Since: 3.50.0

---

## projectionWidth

### projectionWidth: number

**Description:**

The cached width of the Projection matrix.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#projectionWidth](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L343](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L343)  
> Since: 3.50.0

---

## renderer

### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md)

**Description:**

The WebGL Renderer instance to which this pipeline is bound.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#renderer](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L83](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L83)  
> Since: 3.0.0

---

## renderTargets

### renderTargets: Array.<[Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md)>

**Description:**

An array of RenderTarget instances that belong to this pipeline.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#renderTargets](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L289](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L289)  
> Since: 3.50.0

---

## resizeUniform

### resizeUniform: string

**Description:**

If the WebGL Renderer changes size, this uniform will be set with the new width and height values

as part of the pipeline resize method. Various built-in pipelines, such as the MultiPipeline, set

this property automatically to `uResolution`.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#resizeUniform](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L451](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L451)  
> Since: 3.80.0

---

## shaders

### shaders: Array.<[Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md)>

**Description:**

An array of all the WebGLShader instances that belong to this pipeline.

Shaders manage their own attributes and uniforms, but share the same vertex data buffer,

which belongs to this pipeline.

Shaders are set in a call to the `setShadersFromConfig` method, which happens automatically,

but can also be called at any point in your game. See the method documentation for details.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#shaders](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L307](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L307)  
> Since: 3.50.0

---

## topology

### topology: GLenum

**Description:**

The primitive topology which the pipeline will use to submit draw calls.

Defaults to GL\_TRIANGLES if not otherwise set in the config.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#topology](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L196)  
> Since: 3.0.0

---

## vertexBuffer

### vertexBuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](renderer-webgl-wrappers-webglbufferwrapper.md)

**Description:**

The WebGLBuffer that holds the vertex data.

Created from the `vertexData` ArrayBuffer. If `vertices` are set in the config, a `STATIC_DRAW` buffer

is created. If not, a `DYNAMIC_DRAW` buffer is created.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#vertexBuffer](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L174](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L174)  
> Since: 3.0.0

---

## vertexCapacity

### vertexCapacity: number

**Description:**

The total number of vertices that this pipeline batch can hold before it will flush.

This defaults to `renderer batchSize * 6`, where `batchSize` is defined in the Renderer Game Config.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#vertexCapacity](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L150)  
> Since: 3.0.0

---

## vertexCount

### vertexCount: number

**Description:**

The current number of vertices that have been added to the pipeline batch.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#vertexCount](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L140)  
> Since: 3.0.0

---

## vertexData

### vertexData: ArrayBuffer

**Description:**

Raw byte buffer of vertices.

Either set via the config object `vertices` property, or generates a new Array Buffer of

size `vertexCapacity * vertexSize`.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#vertexData](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L161)  
> Since: 3.0.0

---

## vertexViewF32

### vertexViewF32: Float32Array

**Description:**

Float32 view of the array buffer containing the pipeline's vertices.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#vertexViewF32](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L216)  
> Since: 3.0.0

---

## vertexViewU32

### vertexViewU32: Uint32Array

**Description:**

Uint32 view of the array buffer containing the pipeline's vertices.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#vertexViewU32](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L225](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L225)  
> Since: 3.0.0

---

## view

### view: HTMLCanvasElement

**Description:**

The canvas which this WebGL Pipeline renders to.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#view](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L113)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

Width of the current viewport.

**Inherits:** [Phaser.Renderer.WebGL.WebGLPipeline#width](renderer-webgl-webglpipeline.md)

> Source: [src/renderer/webgl/WebGLPipeline.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLPipeline.js#L122)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addTextureToBatch](#addtexturetobatch)

    - [<instance> addTextureToBatch(texture)](#instance-addtexturetobatchtexture)
  + [batchLightVert](#batchlightvert)

    - [<instance> batchLightVert(x, y, lightX, lightY, radius, attenuation, r, g, b, a)](#instance-batchlightvertx-y-lightx-lighty-radius-attenuation-r-g-b-a)
  + [batchPointLight](#batchpointlight)

    - [<instance> batchPointLight(light, camera, x0, y0, x1, y1, x2, y2, x3, y3, lightX, lightY)](#instance-batchpointlightlight-camera-x0-y0-x1-y1-x2-y2-x3-y3-lightx-lighty)
  + [batchQuad](#batchquad)

    - [<instance> batchQuad(gameObject, x0, y0, x1, y1, x2, y2, x3, y3, u0, v0, u1, v1, tintTL, tintTR, tintBL, tintBR, tintEffect, [texture], [unit])](#instance-batchquadgameobject-x0-y0-x1-y1-x2-y2-x3-y3-u0-v0-u1-v1-tinttl-tinttr-tintbl-tintbr-tinteffect-texture-unit)
  + [batchTri](#batchtri)

    - [<instance> batchTri(gameObject, x1, y1, x2, y2, x3, y3, u0, v0, u1, v1, tintTL, tintTR, tintBL, tintEffect, [texture], [unit])](#instance-batchtrigameobject-x1-y1-x2-y2-x3-y3-u0-v0-u1-v1-tinttl-tinttr-tintbl-tinteffect-texture-unit)
  + [batchVert](#batchvert)

    - [<instance> batchVert(x, y, u, v, unit, tintEffect, tint)](#instance-batchvertx-y-u-v-unit-tinteffect-tint)
  + [bind](#bind)

    - [<instance> bind([currentShader])](#instance-bindcurrentshader)
  + [bindRenderTarget](#bindrendertarget)

    - [<instance> bindRenderTarget([target], [unit])](#instance-bindrendertargettarget-unit)
  + [bindTexture](#bindtexture)

    - [<instance> bindTexture([target], [unit])](#instance-bindtexturetarget-unit)
  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [createBatch](#createbatch)

    - [<instance> createBatch(texture)](#instance-createbatchtexture)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [drawFillRect](#drawfillrect)

    - [<instance> drawFillRect(x, y, width, height, color, alpha, [texture], [flipUV])](#instance-drawfillrectx-y-width-height-color-alpha-texture-flipuv)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [flipProjectionMatrix](#flipprojectionmatrix)

    - [<instance> flipProjectionMatrix([flipY])](#instance-flipprojectionmatrixflipy)
  + [flush](#flush)

    - [<instance> flush([isPostFlush])](#instance-flushispostflush)
  + [getShaderByName](#getshaderbyname)

    - [<instance> getShaderByName(name)](#instance-getshaderbynamename)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [onActive](#onactive)

    - [<instance> onActive(currentShader)](#instance-onactivecurrentshader)
  + [onAfterFlush](#onafterflush)

    - [<instance> onAfterFlush([isPostFlush])](#instance-onafterflushispostflush)
  + [onBatch](#onbatch)

    - [<instance> onBatch([gameObject])](#instance-onbatchgameobject)
  + [onBeforeFlush](#onbeforeflush)

    - [<instance> onBeforeFlush([isPostFlush])](#instance-onbeforeflushispostflush)
  + [onBind](#onbind)

    - [<instance> onBind([gameObject])](#instance-onbindgameobject)
  + [onBoot](#onboot)

    - [<instance> onBoot()](#instance-onboot)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [onDraw](#ondraw)

    - [<instance> onDraw(renderTarget, [swapTarget])](#instance-ondrawrendertarget-swaptarget)
  + [onPostBatch](#onpostbatch)

    - [<instance> onPostBatch([gameObject])](#instance-onpostbatchgameobject)
  + [onPostRender](#onpostrender)

    - [<instance> onPostRender()](#instance-onpostrender)
  + [onPreBatch](#onprebatch)

    - [<instance> onPreBatch([gameObject])](#instance-onprebatchgameobject)
  + [onPreRender](#onprerender)

    - [<instance> onPreRender()](#instance-onprerender)
  + [onRebind](#onrebind)

    - [<instance> onRebind()](#instance-onrebind)
  + [onRender](#onrender)

    - [<instance> onRender(scene, camera)](#instance-onrenderscene-camera)
  + [onResize](#onresize)

    - [<instance> onResize(width, height)](#instance-onresizewidth-height)
  + [postBatch](#postbatch)

    - [<instance> postBatch([gameObject])](#instance-postbatchgameobject)
  + [preBatch](#prebatch)

    - [<instance> preBatch([gameObject])](#instance-prebatchgameobject)
  + [pushBatch](#pushbatch)

    - [<instance> pushBatch(texture)](#instance-pushbatchtexture)
  + [rebind](#rebind)

    - [<instance> rebind([currentShader])](#instance-rebindcurrentshader)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [resize](#resize)

    - [<instance> resize(width, height)](#instance-resizewidth-height)
  + [restoreContext](#restorecontext)

    - [<instance> restoreContext()](#instance-restorecontext)
  + [set1f](#set1f)

    - [<instance> set1f(name, x, [shader])](#instance-set1fname-x-shader)
  + [set1fv](#set1fv)

    - [<instance> set1fv(name, arr, [shader])](#instance-set1fvname-arr-shader)
  + [set1i](#set1i)

    - [<instance> set1i(name, x, [shader])](#instance-set1iname-x-shader)
  + [set1iv](#set1iv)

    - [<instance> set1iv(name, arr, [shader])](#instance-set1ivname-arr-shader)
  + [set2f](#set2f)

    - [<instance> set2f(name, x, y, [shader])](#instance-set2fname-x-y-shader)
  + [set2fv](#set2fv)

    - [<instance> set2fv(name, arr, [shader])](#instance-set2fvname-arr-shader)
  + [set2i](#set2i)

    - [<instance> set2i(name, x, y, [shader])](#instance-set2iname-x-y-shader)
  + [set2iv](#set2iv)

    - [<instance> set2iv(name, arr, [shader])](#instance-set2ivname-arr-shader)
  + [set3f](#set3f)

    - [<instance> set3f(name, x, y, z, [shader])](#instance-set3fname-x-y-z-shader)
  + [set3fv](#set3fv)

    - [<instance> set3fv(name, arr, [shader])](#instance-set3fvname-arr-shader)
  + [set3i](#set3i)

    - [<instance> set3i(name, x, y, z, [shader])](#instance-set3iname-x-y-z-shader)
  + [set3iv](#set3iv)

    - [<instance> set3iv(name, arr, [shader])](#instance-set3ivname-arr-shader)
  + [set4f](#set4f)

    - [<instance> set4f(name, x, y, z, w, [shader])](#instance-set4fname-x-y-z-w-shader)
  + [set4fv](#set4fv)

    - [<instance> set4fv(name, arr, [shader])](#instance-set4fvname-arr-shader)
  + [set4i](#set4i)

    - [<instance> set4i(name, x, y, z, w, [shader])](#instance-set4iname-x-y-z-w-shader)
  + [set4iv](#set4iv)

    - [<instance> set4iv(name, arr, [shader])](#instance-set4ivname-arr-shader)
  + [setBoolean](#setboolean)

    - [<instance> setBoolean(name, value, [shader])](#instance-setbooleanname-value-shader)
  + [setGameObject](#setgameobject)

    - [<instance> setGameObject(gameObject, [frame])](#instance-setgameobjectgameobject-frame)
  + [setMatrix2fv](#setmatrix2fv)

    - [<instance> setMatrix2fv(name, transpose, matrix, [shader])](#instance-setmatrix2fvname-transpose-matrix-shader)
  + [setMatrix3fv](#setmatrix3fv)

    - [<instance> setMatrix3fv(name, transpose, matrix, [shader])](#instance-setmatrix3fvname-transpose-matrix-shader)
  + [setMatrix4fv](#setmatrix4fv)

    - [<instance> setMatrix4fv(name, transpose, matrix, [shader])](#instance-setmatrix4fvname-transpose-matrix-shader)
  + [setProjectionMatrix](#setprojectionmatrix)

    - [<instance> setProjectionMatrix(width, height)](#instance-setprojectionmatrixwidth-height)
  + [setShader](#setshader)

    - [<instance> setShader(shader, [setAttributes], [vertexBuffer])](#instance-setshadershader-setattributes-vertexbuffer)
  + [setShadersFromConfig](#setshadersfromconfig)

    - [<instance> setShadersFromConfig(config)](#instance-setshadersfromconfigconfig)
  + [setTexture2D](#settexture2d)

    - [<instance> setTexture2D([texture])](#instance-settexture2dtexture)
  + [setTime](#settime)

    - [<instance> setTime(name, [shader])](#instance-settimename-shader)
  + [setVertexBuffer](#setvertexbuffer)

    - [<instance> setVertexBuffer([buffer])](#instance-setvertexbufferbuffer)
  + [shouldFlush](#shouldflush)

    - [<instance> shouldFlush([amount])](#instance-shouldflushamount)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [unbind](#unbind)

    - [<instance> unbind()](#instance-unbind)
  + [updateProjectionMatrix](#updateprojectionmatrix)

    - [<instance> updateProjectionMatrix()](#instance-updateprojectionmatrix)
  + [vertexAvailable](#vertexavailable)

    - [<instance> vertexAvailable()](#instance-vertexavailable)
* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [activeBuffer](#activebuffer)

    - [activeBuffer: Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](#activebuffer-phaserrendererwebglwrapperswebglbufferwrapper)
  + [activeTextures](#activetextures)

    - [activeTextures: Array.<Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper>](#activetextures-arrayphaserrendererwebglwrapperswebgltexturewrapper)
  + [batch](#batch)

    - [batch: Array.<Phaser.Types.Renderer.WebGL.WebGLPipelineBatchEntry>](#batch-arrayphasertypesrendererwebglwebglpipelinebatchentry)
  + [bytes](#bytes)

    - [bytes: Uint8Array](#bytes-uint8array)
  + [config](#config)

    - [config: Phaser.Types.Renderer.WebGL.WebGLPipelineConfig](#config-phasertypesrendererwebglwebglpipelineconfig)
  + [currentBatch](#currentbatch)

    - [currentBatch: Phaser.Types.Renderer.WebGL.WebGLPipelineBatchEntry](#currentbatch-phasertypesrendererwebglwebglpipelinebatchentry)
  + [currentRenderTarget](#currentrendertarget)

    - [currentRenderTarget: Phaser.Renderer.WebGL.RenderTarget](#currentrendertarget-phaserrendererwebglrendertarget)
  + [currentShader](#currentshader)

    - [currentShader: Phaser.Renderer.WebGL.WebGLShader](#currentshader-phaserrendererwebglwebglshader)
  + [currentTexture](#currenttexture)

    - [currentTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](#currenttexture-phaserrendererwebglwrapperswebgltexturewrapper)
  + [currentUnit](#currentunit)

    - [currentUnit: number](#currentunit-number)
  + [forceZero](#forcezero)

    - [forceZero: boolean](#forcezero-boolean)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [gl](#gl)

    - [gl: WebGLRenderingContext](#gl-webglrenderingcontext)
  + [glReset](#glreset)

    - [glReset: boolean](#glreset-boolean)
  + [hasBooted](#hasbooted)

    - [hasBooted: boolean](#hasbooted-boolean)
  + [height](#height)

    - [height: number](#height-number)
  + [isPostFX](#ispostfx)

    - [isPostFX: boolean](#ispostfx-boolean)
  + [isPreFX](#isprefx)

    - [isPreFX: boolean](#isprefx-boolean)
  + [manager](#manager)

    - [manager: Phaser.Renderer.WebGL.PipelineManager](#manager-phaserrendererwebglpipelinemanager)
  + [name](#name)

    - [name: string](#name-string)
  + [projectionHeight](#projectionheight)

    - [projectionHeight: number](#projectionheight-number)
  + [projectionMatrix](#projectionmatrix)

    - [projectionMatrix: Phaser.Math.Matrix4](#projectionmatrix-phasermathmatrix4)
  + [projectionWidth](#projectionwidth)

    - [projectionWidth: number](#projectionwidth-number)
  + [renderer](#renderer)

    - [renderer: Phaser.Renderer.WebGL.WebGLRenderer](#renderer-phaserrendererwebglwebglrenderer)
  + [renderTargets](#rendertargets)

    - [renderTargets: Array.<Phaser.Renderer.WebGL.RenderTarget>](#rendertargets-arrayphaserrendererwebglrendertarget)
  + [resizeUniform](#resizeuniform)

    - [resizeUniform: string](#resizeuniform-string)
  + [shaders](#shaders)

    - [shaders: Array.<Phaser.Renderer.WebGL.WebGLShader>](#shaders-arrayphaserrendererwebglwebglshader)
  + [topology](#topology)

    - [topology: GLenum](#topology-glenum)
  + [vertexBuffer](#vertexbuffer)

    - [vertexBuffer: Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](#vertexbuffer-phaserrendererwebglwrapperswebglbufferwrapper)
  + [vertexCapacity](#vertexcapacity)

    - [vertexCapacity: number](#vertexcapacity-number)
  + [vertexCount](#vertexcount)

    - [vertexCount: number](#vertexcount-number)
  + [vertexData](#vertexdata)

    - [vertexData: ArrayBuffer](#vertexdata-arraybuffer)
  + [vertexViewF32](#vertexviewf32)

    - [vertexViewF32: Float32Array](#vertexviewf32-float32array)
  + [vertexViewU32](#vertexviewu32)

    - [vertexViewU32: Uint32Array](#vertexviewu32-uint32array)
  + [view](#view)

    - [view: HTMLCanvasElement](#view-htmlcanvaselement)
  + [width](#width)

    - [width: number](#width-number)

Back to top

©2025[Phaser](https://docs.phaser.io)