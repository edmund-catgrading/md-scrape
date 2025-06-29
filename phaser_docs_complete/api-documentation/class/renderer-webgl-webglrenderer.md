# WebGLRenderer

Phaser.Renderer.WebGL.WebGLRenderer

WebGLRenderer is a class that contains the needed functionality to keep the

WebGLRenderingContext state clean. The main idea of the WebGLRenderer is to keep track of

any context change that happens for WebGL rendering inside of Phaser. This means

if raw webgl functions are called outside the WebGLRenderer of the Phaser WebGL

rendering ecosystem they might pollute the current WebGLRenderingContext state producing

unexpected behavior. It's recommended that WebGL interaction is done through

WebGLRenderer and/or WebGLPipeline.

**Constructor**

`new WebGLRenderer(game)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | The Game instance which owns this WebGL Renderer. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/renderer/webgl/WebGLRenderer.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L45)  
> Since: 3.0.0

# Public Methods

## addBlendMode

### <instance> addBlendMode(func, equation)

**Description:**

Creates a new custom blend mode for the renderer.

See <https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Constants#Blending_modes>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| func | Array.<GLenum> | No | An array containing the WebGL functions to use for the source and the destination blending factors, respectively. See the possible constants for {@link WebGLRenderingContext#blendFunc()}. |
| --- | --- | --- | --- |
| equation | GLenum | No | The equation to use for combining the RGB and alpha components of a new pixel with a rendered one. See the possible constants for {@link WebGLRenderingContext#blendEquation()}. |

**Returns:** number - The index of the new blend mode, used for referencing it in the future.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1845](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1845)  
> Since: 3.0.0

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

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## beginBitmapMask

### <instance> beginBitmapMask(mask, camera)

**Description:**

Binds necessary resources and renders the mask to a separated framebuffer.

The framebuffer for the masked object is also bound for further use.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mask | [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) | No | The BitmapMask instance that called beginMask. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The camera rendering the current mask. |

> Source: [src/renderer/webgl/WebGLRenderer.js#L2260](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2260)  
> Since: 3.60.0

---

## beginCapture

### <instance> beginCapture([width], [height])

**Description:**

Binds the WebGL Renderers Render Target, so all drawn content is now redirected to it.

Make sure to call `endCapture` when you are finished.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | Yes | Optional new width of the Render Target. |
| --- | --- | --- | --- |
| height | number | Yes | Optional new height of the Render Target. |

> Source: [src/renderer/webgl/WebGLRenderer.js#L1366](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1366)  
> Since: 3.50.0

---

## canvasToTexture

### <instance> canvasToTexture(srcCanvas, [dstTexture], [noRepeat], [flipY])

**Description:**

Creates a new WebGL Texture based on the given Canvas Element.

If the `dstTexture` parameter is given, the WebGL Texture is updated, rather than created fresh.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| srcCanvas | HTMLCanvasElement | No |  | The Canvas to create the WebGL Texture from |
| --- | --- | --- | --- | --- |
| dstTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | Yes |  | The destination WebGLTextureWrapper to set. |
| noRepeat | boolean | Yes | false | Should this canvas be allowed to set `REPEAT` (such as for Text objects?) |
| flipY | boolean | Yes | false | Should the WebGL Texture set `UNPACK_MULTIPLY_FLIP_Y`? |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) - The newly created, or updated, WebGLTextureWrapper.

> Source: [src/renderer/webgl/WebGLRenderer.js#L3045](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L3045)  
> Since: 3.0.0

---

## captureFrame

### <instance> captureFrame([quickCapture], [fullCapture])

**Description:**

This method is only available in the Debug Build of Phaser, or a build with the

`WEBGL_DEBUG` flag set in the Webpack Config.

Phaser v3.60 Debug has a build of Spector.js embedded in it, which is a WebGL inspector

that allows for live inspection of your WebGL calls. Although it's easy to add the Spector

extension to a desktop browsr, by embedding it in Phaser we can make it available in mobile

browsers too, making it a powerful tool for debugging WebGL games on mobile devices where

extensions are not permitted.

See <https://github.com/BabylonJS/Spector.js> for more details.

This method will capture the current WebGL frame and send it to the Spector.js tool for inspection.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| quickCapture | boolean | Yes | false | If `true` thumbnails are not captured in order to speed up the capture. |
| --- | --- | --- | --- | --- |
| fullCapture | boolean | Yes | false | If `true` all details are captured. |

> Source: [src/renderer/webgl/WebGLRenderer.js#L1139](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1139)  
> Since: 3.60.0

---

## captureNextFrame

### <instance> captureNextFrame()

**Description:**

This method is only available in the Debug Build of Phaser, or a build with the

`WEBGL_DEBUG` flag set in the Webpack Config.

Phaser v3.60 Debug has a build of Spector.js embedded in it, which is a WebGL inspector

that allows for live inspection of your WebGL calls. Although it's easy to add the Spector

extension to a desktop browsr, by embedding it in Phaser we can make it available in mobile

browsers too, making it a powerful tool for debugging WebGL games on mobile devices where

extensions are not permitted.

See <https://github.com/BabylonJS/Spector.js> for more details.

This method will capture the next WebGL frame and send it to the Spector.js tool for inspection.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1172)  
> Since: 3.60.0

---

## clearStencilMask

### <instance> clearStencilMask()

**Description:**

Disables the STENCIL\_TEST but does not change the status

of the current stencil mask.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2833](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2833)  
> Since: 3.60.0

---

## createAttribLocation

### <instance> createAttribLocation(program, name)

**Description:**

Creates a WebGLAttribLocationWrapper instance based on the given WebGLProgramWrapper and attribute name.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](renderer-webgl-wrappers-webglprogramwrapper.md) | No | The WebGLProgramWrapper instance. |
| --- | --- | --- | --- |
| name | string | No | The name of the attribute. |

> Source: [src/renderer/webgl/WebGLRenderer.js#L2377](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2377)  
> Since: 3.80.0

---

## createCanvasTexture

### <instance> createCanvasTexture(srcCanvas, [noRepeat], [flipY])

**Description:**

Creates a new WebGL Texture based on the given Canvas Element.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| srcCanvas | HTMLCanvasElement | No |  | The Canvas to create the WebGL Texture from. |
| --- | --- | --- | --- | --- |
| noRepeat | boolean | Yes | false | Should this canvas be allowed to set `REPEAT` (such as for Text objects?) |
| flipY | boolean | Yes | false | Should the WebGL Texture set `UNPACK_MULTIPLY_FLIP_Y`? |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) - The newly created WebGLTextureWrapper.

> Source: [src/renderer/webgl/WebGLRenderer.js#L3099](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L3099)  
> Since: 3.20.0

---

## createFramebuffer

### <instance> createFramebuffer(width, height, renderTexture, [addDepthStencilBuffer])

**Description:**

Creates a WebGL Framebuffer object and optionally binds a depth stencil render buffer.

This will unbind any currently bound framebuffer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| width | number | No |  | If `addDepthStencilBuffer` is true, this controls the width of the depth stencil. |
| --- | --- | --- | --- | --- |
| height | number | No |  | If `addDepthStencilBuffer` is true, this controls the height of the depth stencil. |
| renderTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No |  | The color texture where the color pixels are written. |
| addDepthStencilBuffer | boolean | Yes | false | Create a Renderbuffer for the depth stencil? |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md) - Wrapped framebuffer which is safe to use with the renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2235](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2235)  
> Since: 3.0.0

---

## createIndexBuffer

### <instance> createIndexBuffer(initialDataOrSize, bufferUsage)

**Description:**

Wrapper for creating a vertex buffer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| initialDataOrSize | ArrayBuffer | No | Either ArrayBuffer or an integer indicating the size of the vbo. |
| --- | --- | --- | --- |
| bufferUsage | number | No | How the buffer is used. gl.DYNAMIC\_DRAW, gl.STATIC\_DRAW or gl.STREAM\_DRAW. |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](renderer-webgl-wrappers-webglbufferwrapper.md) - Wrapped index buffer

> Source: [src/renderer/webgl/WebGLRenderer.js#L2409](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2409)  
> Since: 3.0.0

---

## createProgram

### <instance> createProgram(vertexShader, fragmentShader)

**Description:**

Creates a WebGLProgram instance based on the given vertex and fragment shader source.

Then compiles, attaches and links the program before wrapping and returning it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| vertexShader | string | No | The vertex shader source code as a single string. |
| --- | --- | --- | --- |
| fragmentShader | string | No | The fragment shader source code as a single string. |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](renderer-webgl-wrappers-webglprogramwrapper.md) - The wrapped, linked WebGLProgram created from the given shader source.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2338](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2338)  
> Since: 3.0.0

---

## createTemporaryTextures

### <instance> createTemporaryTextures()

**Description:**

Create temporary WebGL textures to stop WebGL errors on macOS.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1115](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1115)  
> Since: 3.60.0

---

## createTexture2D

### <instance> createTexture2D(mipLevel, minFilter, magFilter, wrapT, wrapS, format, pixels, width, height, [pma], [forceSize], [flipY])

**Description:**

A wrapper for creating a WebGLTextureWrapper. If no pixel data is passed it will create an empty texture.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| mipLevel | number | No |  | Mip level of the texture. |
| --- | --- | --- | --- | --- |
| minFilter | number | No |  | Filtering of the texture. |
| magFilter | number | No |  | Filtering of the texture. |
| wrapT | number | No |  | Wrapping mode of the texture. |
| wrapS | number | No |  | Wrapping mode of the texture. |
| format | number | No |  | Which format does the texture use. |
| pixels | object | No |  | pixel data. |
| width | number | No |  | Width of the texture in pixels. If not supplied, it must be derived from `pixels`. |
| height | number | No |  | Height of the texture in pixels. If not supplied, it must be derived from `pixels`. |
| pma | boolean | Yes | true | Does the texture have premultiplied alpha? |
| forceSize | boolean | Yes | false | If `true` it will use the width and height passed to this method, regardless of the pixels dimension. |
| flipY | boolean | Yes | false | Sets the `UNPACK_FLIP_Y_WEBGL` flag the WebGL Texture uses during upload. |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) - The WebGLTextureWrapper that was created.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2202)  
> Since: 3.0.0

---

## createTextureFromSource

### <instance> createTextureFromSource(source, width, height, scaleMode, [forceClamp])

**Description:**

Creates a texture from an image source. If the source is not valid it creates an empty texture.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| source | object | No |  | The source of the texture. |
| --- | --- | --- | --- | --- |
| width | number | No |  | The width of the texture. |
| height | number | No |  | The height of the texture. |
| scaleMode | number | No |  | The scale mode to be used by the texture. |
| forceClamp | boolean | Yes | false | Force the texture to use the CLAMP\_TO\_EDGE wrap mode, even if a power of two? |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) - The WebGLTextureWrapper that was created, or `null` if it couldn't be created.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2143](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2143)  
> Since: 3.0.0

---

## createUint8ArrayTexture

### <instance> createUint8ArrayTexture(data, width, height)

**Description:**

Create a WebGLTexture from a Uint8Array.

The Uint8Array is assumed to be RGBA values, one byte per color component.

The texture will be filtered with `gl.NEAREST` and will not be mipped.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | Uint8Array | No | The Uint8Array to create the texture from. |
| --- | --- | --- | --- |
| width | number | No | The width of the texture. |
| height | number | No | The height of the texture. |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) - The newly created WebGLTextureWrapper.

> Source: [src/renderer/webgl/WebGLRenderer.js#L3235](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L3235)  
> Since: 3.80.0

---

## createUniformLocation

### <instance> createUniformLocation(program, name)

**Description:**

Creates a WebGLUniformLocationWrapper instance based on the given WebGLProgramWrapper and uniform name.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](renderer-webgl-wrappers-webglprogramwrapper.md) | No | The WebGLProgramWrapper instance. |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform. |

> Source: [src/renderer/webgl/WebGLRenderer.js#L2393](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2393)  
> Since: 3.80.0

---

## createVertexBuffer

### <instance> createVertexBuffer(initialDataOrSize, bufferUsage)

**Description:**

Wrapper for creating a vertex buffer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| initialDataOrSize | ArrayBuffer | No | It's either ArrayBuffer or an integer indicating the size of the vbo |
| --- | --- | --- | --- |
| bufferUsage | number | No | How the buffer is used. gl.DYNAMIC\_DRAW, gl.STATIC\_DRAW or gl.STREAM\_DRAW |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](renderer-webgl-wrappers-webglbufferwrapper.md) - Wrapped vertex buffer

> Source: [src/renderer/webgl/WebGLRenderer.js#L2358](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2358)  
> Since: 3.0.0

---

## createVideoTexture

### <instance> createVideoTexture(srcVideo, [noRepeat], [flipY])

**Description:**

Creates a new WebGL Texture based on the given HTML Video Element.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| srcVideo | HTMLVideoElement | No |  | The Video to create the WebGL Texture from |
| --- | --- | --- | --- | --- |
| noRepeat | boolean | Yes | false | Should this canvas be allowed to set `REPEAT`? |
| flipY | boolean | Yes | false | Should the WebGL Texture set `UNPACK_MULTIPLY_FLIP_Y`? |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) - The newly created WebGLTextureWrapper.

> Source: [src/renderer/webgl/WebGLRenderer.js#L3194](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L3194)  
> Since: 3.20.0

---

## deleteAttribLocation

### <instance> deleteAttribLocation(attrib)

**Description:**

Deletes a WebGLAttribLocation from the GL instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| attrib | [Phaser.Renderer.WebGL.Wrappers.WebGLAttribLocationWrapper](renderer-webgl-wrappers-webglattriblocationwrapper.md) | No | The attrib location to be deleted. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/WebGLRenderer.js#L2492](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2492)  
> Since: 3.80.0

---

## deleteBuffer

### <instance> deleteBuffer(vertexBuffer)

**Description:**

Deletes a WebGLBuffer from the GL instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| vertexBuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](renderer-webgl-wrappers-webglbufferwrapper.md) | No | The WebGLBuffer to be deleted. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2528](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2528)  
> Since: 3.0.0

---

## deleteFramebuffer

### <instance> deleteFramebuffer(framebuffer)

**Description:**

Deletes a Framebuffer from the GL instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| framebuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md) | null | No | The Framebuffer to be deleted. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2449](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2449)  
> Since: 3.0.0

---

## deleteProgram

### <instance> deleteProgram(program)

**Description:**

Deletes a WebGLProgram from the GL instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](renderer-webgl-wrappers-webglprogramwrapper.md) | No | The shader program to be deleted. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2471](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2471)  
> Since: 3.0.0

---

## deleteTexture

### <instance> deleteTexture(texture)

**Description:**

Removes a texture from the GPU.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No | The WebGL Texture to be deleted. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2428](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2428)  
> Since: 3.0.0

---

## deleteUniformLocation

### <instance> deleteUniformLocation(uniform)

**Description:**

Deletes a WebGLUniformLocation from the GL instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| uniform | [Phaser.Renderer.WebGL.Wrappers.WebGLUniformLocationWrapper](renderer-webgl-wrappers-webgluniformlocationwrapper.md) | No | The uniform location to be deleted. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/WebGLRenderer.js#L2510](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2510)  
> Since: 3.80.0

---

## destroy

### <instance> destroy()

**Description:**

Destroy this WebGLRenderer, cleaning up all related resources such as pipelines, native textures, etc.

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/renderer/webgl/WebGLRenderer.js#L3319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L3319)  
> Since: 3.0.0

---

## dispatchContextLost

### <instance> dispatchContextLost(event)

**Description:**

This method is called when the WebGL context is lost. By default this is bound to the property `WebGLRenderer.contextLostHandler`.

If you override the context loss handler via the `setContextHandlers` method then be sure to invoke this method in due course.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | WebGLContextEvent | No | The WebGL context lost Event. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/WebGLRenderer.js#L1011](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1011)  
> Since: 3.85.0

---

## dispatchContextRestored

### <instance> dispatchContextRestored(event)

**Description:**

This method is called when the WebGL context is restored. By default this is bound to the property `WebGLRenderer.contextRestoredHandler`.

If you override the context restored handler via the `setContextHandlers` method then be sure to invoke this method in due course.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | WebGLContextEvent | No | The WebGL context restored Event. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/WebGLRenderer.js#L1034](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1034)  
> Since: 3.85.0

---

## drawBitmapMask

### <instance> drawBitmapMask(mask, camera, bitmapMaskPipeline)

**Description:**

Binds necessary resources and renders the mask to a separated framebuffer.

The framebuffer for the masked object is also bound for further use.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mask | [Phaser.Display.Masks.BitmapMask](display-masks-bitmapmask.md) | No | The BitmapMask instance that called beginMask. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The camera rendering the current mask. |
| bitmapMaskPipeline | [Phaser.Renderer.WebGL.Pipelines.BitmapMaskPipeline](renderer-webgl-pipelines-bitmapmaskpipeline.md) | No | The BitmapMask Pipeline instance that is requesting the draw. |

> Source: [src/renderer/webgl/WebGLRenderer.js#L2288](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2288)  
> Since: 3.60.0

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

## endCapture

### <instance> endCapture()

**Description:**

Unbinds the WebGL Renderers Render Target and returns it, stopping any further content being drawn to it.

If the viewport or scissors were modified during the capture, you should reset them by calling

`resetViewport` and `resetScissor` accordingly.

**Returns:** [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) - A reference to the WebGL Renderer Render Target.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1387](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1387)  
> Since: 3.50.0

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

## flush

### <instance> flush()

**Description:**

Flushes the current pipeline if the pipeline is bound

> Source: [src/renderer/webgl/WebGLRenderer.js#L1633](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1633)  
> Since: 3.0.0

---

## getAspectRatio

### <instance> getAspectRatio()

**Description:**

Gets the aspect ratio of the WebGLRenderer dimensions.

**Returns:** number - The aspect ratio of the WebGLRenderer dimensions.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1543](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1543)  
> Since: 3.50.0

---

## getCompressedTextureName

### <instance> getCompressedTextureName(baseFormat, [format])

**Description:**

Returns a compressed texture format GLenum name based on the given format.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| baseFormat | string | No | The Base Format to check. |
| --- | --- | --- | --- |
| format | GLenum | Yes | An optional GLenum format to check within the base format. |

**Returns:** string - The compressed texture format name, as a string.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1492](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1492)  
> Since: 3.60.0

---

## getCompressedTextures

### <instance> getCompressedTextures()

**Description:**

Determines which compressed texture formats this browser and device supports.

Called automatically as part of the WebGL Renderer init process. If you need to investigate

which formats it supports, see the `Phaser.Renderer.WebGL.WebGLRenderer#compression` property instead.

**Returns:** [Phaser.Types.Renderer.WebGL.WebGLTextureCompression](../typedef/types-renderer-webgl.md) - The compression object.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1442](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1442)  
> Since: 3.60.0

---

## getExtension

### <instance> getExtension(extensionName)

**Description:**

Loads a WebGL extension

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| extensionName | string | No | The name of the extension to load. |
| --- | --- | --- | --- |

**Returns:** object - WebGL extension if the extension is supported

> Source: [src/renderer/webgl/WebGLRenderer.js#L1611](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1611)  
> Since: 3.0.0

---

## getFps

### <instance> getFps()

**Description:**

This method is only available in the Debug Build of Phaser, or a build with the

`WEBGL_DEBUG` flag set in the Webpack Config.

Phaser v3.60 Debug has a build of Spector.js embedded in it, which is a WebGL inspector

that allows for live inspection of your WebGL calls. Although it's easy to add the Spector

extension to a desktop browsr, by embedding it in Phaser we can make it available in mobile

browsers too, making it a powerful tool for debugging WebGL games on mobile devices where

extensions are not permitted.

See <https://github.com/BabylonJS/Spector.js> for more details.

This method will return the current FPS of the WebGL canvas.

**Returns:** number - The current FPS of the WebGL canvas.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1199)  
> Since: 3.60.0

---

## getMaxTextureSize

### <instance> getMaxTextureSize()

**Description:**

Returns the largest texture size (either width or height) that can be created.

Note that VRAM may not allow a texture of any given size, it just expresses

hardware / driver support for a given size.

**Returns:** number - The maximum supported texture size.

> Source: [src/renderer/webgl/WebGLRenderer.js#L3304](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L3304)  
> Since: 3.8.0

---

## hasActiveStencilMask

### <instance> hasActiveStencilMask()

**Description:**

Is there an active stencil mask?

**Returns:** boolean - `true` if there is an active stencil mask, otherwise `false`.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1769](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1769)  
> Since: 3.17.0

---

## hasExtension

### <instance> hasExtension(extensionName)

**Description:**

Checks if a WebGL extension is supported

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| extensionName | string | No | Name of the WebGL extension |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the extension is supported, otherwise `false`.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1596](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1596)  
> Since: 3.0.0

---

## init

### <instance> init(config)

**Description:**

Creates a new WebGLRenderingContext and initializes all internal state.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | object | No | The configuration object for the renderer. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L739](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L739)  
> Since: 3.0.0

---

## isNewNormalMap

### <instance> isNewNormalMap(texture, normalMap)

**Description:**

Checks to see if the given diffuse and normal map textures are already bound, or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No | The diffuse texture. |
| --- | --- | --- | --- |
| normalMap | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No | The normal map texture. |

**Returns:** boolean - Returns `false` if this combination is already set, or `true` if it's a new combination.

> Source: [src/renderer/webgl/pipelines/LightPipeline.js#L359](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/pipelines/LightPipeline.js#L359)  
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

## log

### <instance> log(arguments)

**Description:**

This method is only available in the Debug Build of Phaser, or a build with the

`WEBGL_DEBUG` flag set in the Webpack Config.

Phaser v3.60 Debug has a build of Spector.js embedded in it, which is a WebGL inspector

that allows for live inspection of your WebGL calls. Although it's easy to add the Spector

extension to a desktop browsr, by embedding it in Phaser we can make it available in mobile

browsers too, making it a powerful tool for debugging WebGL games on mobile devices where

extensions are not permitted.

See <https://github.com/BabylonJS/Spector.js> for more details.

This method adds a command with the name value in the list. This can be filtered in the search.

All logs can be filtered searching for "LOG".

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| arguments | \* | No | The arguments to log to Spector. |
| --- | --- | --- | --- |

**Returns:** string - The current log.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1226](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1226)  
> Since: 3.60.0

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

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - `this`.

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

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - `this`.

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

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - `this`.

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
| baseSize | [Phaser.Structs.Size](structs-size.md) | No | The base Size object. The game dimensions. The canvas width / height values match this. |

> Source: [src/renderer/webgl/WebGLRenderer.js#L1348](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1348)  
> Since: 3.16.0

---

## popFramebuffer

### <instance> popFramebuffer([updateScissor], [setViewport])

**Description:**

Pops the previous framebuffer from the fbo stack and sets it.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| updateScissor | boolean | Yes | false | If a framebuffer is given, set the gl scissor to match the frame buffer size? Or, if `null` given, pop the scissor from the stack. |
| --- | --- | --- | --- | --- |
| setViewport | boolean | Yes | true | Should the WebGL viewport be set? |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md) - The Framebuffer that was set, or `null` if there aren't any more in the stack.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2034](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2034)  
> Since: 3.50.0

---

## popScissor

### <instance> popScissor()

**Description:**

Pops the last scissor state and sets it.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1745](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1745)  
> Since: 3.0.0

---

## postRender

### <instance> postRender()

**Description:**

The post-render step happens after all Cameras in all Scenes have been rendered.

**Fires:** [Phaser.Renderer.Events#event:POST\_RENDER](../event/renderer-events.md)

> Source: [src/renderer/webgl/WebGLRenderer.js#L2808](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2808)  
> Since: 3.0.0

---

## postRenderCamera

### <instance> postRenderCamera(camera)

**Description:**

Controls the post-render operations for the given camera.

Renders the foreground camera effects like flash and fading, then resets the current scissor state.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera to post-render. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/WebGLRenderer.js#L2615](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2615)  
> Since: 3.0.0

---

## preRender

### <instance> preRender()

**Description:**

Clears the current vertex buffer and updates pipelines.

**Fires:** [Phaser.Renderer.Events#event:PRE\_RENDER\_CLEAR](../event/renderer-events.md), [Phaser.Renderer.Events#event:PRE\_RENDER](../event/renderer-events.md)

> Source: [src/renderer/webgl/WebGLRenderer.js#L2654](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2654)  
> Since: 3.0.0

---

## preRenderCamera

### <instance> preRenderCamera(camera)

**Description:**

Controls the pre-render operations for the given camera.

Handles any clipping needed by the camera and renders the background color if a color is visible.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera to pre-render. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/WebGLRenderer.js#L2546](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2546)  
> Since: 3.0.0

---

## pushFramebuffer

### <instance> pushFramebuffer(framebuffer, [updateScissor], [setViewport], [texture], [clear])

**Description:**

Pushes a new framebuffer onto the FBO stack and makes it the currently bound framebuffer.

If there was another framebuffer already bound it will force a pipeline flush.

Call `popFramebuffer` to remove it again.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| framebuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md) | No |  | The framebuffer that needs to be bound. |
| --- | --- | --- | --- | --- |
| updateScissor | boolean | Yes | false | Set the gl scissor to match the frame buffer size? Or, if `null` given, pop the scissor from the stack. |
| setViewport | boolean | Yes | true | Should the WebGL viewport be set? |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | Yes | null | Bind the given frame buffer texture? |
| clear | boolean | Yes | false | Clear the frame buffer after binding? |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1913](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1913)  
> Since: 3.50.0

---

## pushScissor

### <instance> pushScissor(x, y, width, height, [drawingBufferHeight])

**Description:**

Pushes a new scissor state. This is used to set nested scissor states.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the scissor. |
| --- | --- | --- | --- |
| y | number | No | The y position of the scissor. |
| width | number | No | The width of the scissor. |
| height | number | No | The height of the scissor. |
| drawingBufferHeight | number | Yes | Optional drawingBufferHeight override value. |

**Returns:** Array.<number> - An array containing the scissor values.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1644](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1644)  
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

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeBlendMode

### <instance> removeBlendMode(index)

**Description:**

Removes a custom blend mode from the renderer.

Any Game Objects still using this blend mode will error, so be sure to clear them first.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the custom blend mode to be removed. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1892](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1892)  
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

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - `this`.

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

> Source: [src/renderer/webgl/WebGLRenderer.js#L2701](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2701)  
> Since: 3.0.0

---

## resetProgram

### <instance> resetProgram()

**Description:**

Rebinds whatever program `WebGLRenderer.currentProgram` is set as, without

changing anything, or flushing.

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2127)  
> Since: 3.50.0

---

## resetProjectionMatrix

### <instance> resetProjectionMatrix()

**Description:**

Resets the Projection Matrix back to this renderers width and height.

This is called during `endCapture`, should the matrix have been changed

as a result of the capture process.

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1580](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1580)  
> Since: 3.50.0

---

## resetScissor

### <instance> resetScissor()

**Description:**

Resets the gl scissor state to be whatever the current scissor is, if there is one, without

modifying the scissor stack.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1716](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1716)  
> Since: 3.50.0

---

## resetViewport

### <instance> resetViewport()

**Description:**

Resets the gl viewport to the current renderer dimensions.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1785](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1785)  
> Since: 3.50.0

---

## resize

### <instance> resize([width], [height])

**Description:**

Resizes the drawing buffer to match that required by the Scale Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | Yes | The new width of the renderer. |
| --- | --- | --- | --- |
| height | number | Yes | The new height of the renderer. |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

**Fires:** [Phaser.Renderer.Events#event:RESIZE](../event/renderer-events.md)

> Source: [src/renderer/webgl/WebGLRenderer.js#L1407](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1407)  
> Since: 3.0.0

---

## restoreFramebuffer

### <instance> restoreFramebuffer([updateScissor], [setViewport])

**Description:**

Restores the previous framebuffer from the fbo stack and sets it.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| updateScissor | boolean | Yes | false | If a framebuffer is given, set the gl scissor to match the frame buffer size? Or, if `null` given, pop the scissor from the stack. |
| --- | --- | --- | --- | --- |
| setViewport | boolean | Yes | true | Should the WebGL viewport be set? |

> Source: [src/renderer/webgl/WebGLRenderer.js#L2068](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2068)  
> Since: 3.60.0

---

## restoreStencilMask

### <instance> restoreStencilMask()

**Description:**

Restores the current stencil function to the one that was in place

before `clearStencilMask` was called.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2845](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2845)  
> Since: 3.60.0

---

## setBlendMode

### <instance> setBlendMode(blendModeId, [force])

**Description:**

Sets the blend mode to the value given.

If the current blend mode is different from the one given, the pipeline is flushed and the new

blend mode is enabled.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| blendModeId | number | No |  | The blend mode to be set. Can be a `BlendModes` const or an integer value. |
| --- | --- | --- | --- | --- |
| force | boolean | Yes | false | Force the blend mode to be set, regardless of the currently set blend mode. |

**Returns:** boolean - `true` if the blend mode was changed as a result of this call, forcing a flush, otherwise `false`.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1800](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1800)  
> Since: 3.0.0

---

## setContextHandlers

### <instance> setContextHandlers([contextLost], [contextRestored])

**Description:**

Sets the handlers that are called when WebGL context is lost or restored by the browser.

The default handlers are referenced via the properties `WebGLRenderer.contextLostHandler` and `WebGLRenderer.contextRestoredHandler`.

By default, these map to the methods `WebGLRenderer.dispatchContextLost` and `WebGLRenderer.dispatchContextRestored`.

You can override these handlers with your own via this method.

If you do override them, make sure that your handlers invoke the methods `WebGLRenderer.dispatchContextLost` and `WebGLRenderer.dispatchContextRestored` in due course, otherwise the renderer will not be able to restore itself fully.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| contextLost | function | Yes | Custom handler for responding to the WebGL context lost event. Set as `undefined` to use the default handler. |
| --- | --- | --- | --- |
| contextRestored | function | Yes | Custom handler for responding to the WebGL context restored event. Set as `undefined` to use the default handler. |

> Source: [src/renderer/webgl/WebGLRenderer.js#L959](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L959)  
> Since: 3.85.0

---

## setExtensions

### <instance> setExtensions()

**Description:**

Queries the GL context to get the supported extensions.

Then sets them into the `supportedExtensions`, `instancedArraysExtension` and `vaoExtension` properties.

Called automatically during the `init` method.

> Source: [src/renderer/webgl/WebGLRenderer.js#L932](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L932)  
> Since: 3.85.2

---

## setFramebuffer

### <instance> setFramebuffer(framebuffer, [updateScissor], [setViewport], [texture], [clear])

**Description:**

Sets the given framebuffer as the active and currently bound framebuffer.

If there was another framebuffer already bound it will force a pipeline flush.

Typically, you should call `pushFramebuffer` instead of this method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| framebuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md) | null | No |  | The framebuffer that needs to be bound, or `null` to bind back to the default framebuffer. |
| --- | --- | --- | --- | --- |
| updateScissor | boolean | Yes | false | If a framebuffer is given, set the gl scissor to match the frame buffer size? Or, if `null` given, pop the scissor from the stack. |
| setViewport | boolean | Yes | true | Should the WebGL viewport be set? |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | Yes | null | Bind the given frame buffer texture? |
| clear | boolean | Yes | false | Clear the frame buffer after binding? |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1943](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1943)  
> Since: 3.0.0

---

## setProgram

### <instance> setProgram(program)

**Description:**

Binds a shader program.

If there was a different program already bound it will force a pipeline flush first.

If the same program given to this method is already set as the current program, no change

will take place and this method will return `false`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](renderer-webgl-wrappers-webglprogramwrapper.md) | No | The program that needs to be bound. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the given program was bound, otherwise `false`.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2096](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2096)  
> Since: 3.0.0

---

## setProjectionMatrix

### <instance> setProjectionMatrix(width, height)

**Description:**

Sets the Projection Matrix of this renderer to the given dimensions.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of the Projection Matrix. |
| --- | --- | --- | --- |
| height | number | No | The new height of the Projection Matrix. |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1556](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1556)  
> Since: 3.50.0

---

## setScissor

### <instance> setScissor(x, y, width, height, [drawingBufferHeight])

**Description:**

Sets the current scissor state.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the scissor. |
| --- | --- | --- | --- |
| y | number | No | The y position of the scissor. |
| width | number | No | The width of the scissor. |
| height | number | No | The height of the scissor. |
| drawingBufferHeight | number | Yes | Optional drawingBufferHeight override value. |

> Source: [src/renderer/webgl/WebGLRenderer.js#L1675](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1675)  
> Since: 3.0.0

---

## setTextureFilter

### <instance> setTextureFilter(texture, filter)

**Description:**

Sets the minification and magnification filter for a texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No | The texture to set the filter for. |
| --- | --- | --- | --- |
| filter | number | No | The filter to set. 0 for linear filtering, 1 for nearest neighbor (blocky) filtering. |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGL Renderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L3266](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L3266)  
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

## snapshot

### <instance> snapshot(callback, [type], [encoderOptions])

**Description:**

Schedules a snapshot of the entire game viewport to be taken after the current frame is rendered.

To capture a specific area see the `snapshotArea` method. To capture a specific pixel, see `snapshotPixel`.

Only one snapshot can be active *per frame*. If you have already called `snapshotPixel`, for example, then

calling this method will override it.

Snapshots work by using the WebGL `readPixels` feature to grab every pixel from the frame buffer into an ArrayBufferView.

It then parses this, copying the contents to a temporary Canvas and finally creating an Image object from it,

which is the image returned to the callback provided. All in all, this is a computationally expensive and blocking process,

which gets more expensive the larger the canvas size gets, so please be careful how you employ this in your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](../typedef/types-renderer-snapshot.md) | No |  | The Function to invoke after the snapshot image is created. |
| --- | --- | --- | --- | --- |
| type | string | Yes | "'image/png'" | The format of the image to create, usually `image/png` or `image/jpeg`. |
| encoderOptions | number | Yes | 0.92 | The image quality, between 0 and 1. Used for image formats with lossy compression, such as `image/jpeg`. |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGL Renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2877](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2877)  
> Since: 3.0.0

---

## snapshotArea

### <instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions])

**Description:**

Schedules a snapshot of the given area of the game viewport to be taken after the current frame is rendered.

To capture the whole game viewport see the `snapshot` method. To capture a specific pixel, see `snapshotPixel`.

Only one snapshot can be active *per frame*. If you have already called `snapshotPixel`, for example, then

calling this method will override it.

Snapshots work by using the WebGL `readPixels` feature to grab every pixel from the frame buffer into an ArrayBufferView.

It then parses this, copying the contents to a temporary Canvas and finally creating an Image object from it,

which is the image returned to the callback provided. All in all, this is a computationally expensive and blocking process,

which gets more expensive the larger the canvas size gets, so please be careful how you employ this in your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate to grab from. This is based on the game viewport, not the world. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate to grab from. This is based on the game viewport, not the world. |
| width | number | No |  | The width of the area to grab. |
| height | number | No |  | The height of the area to grab. |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](../typedef/types-renderer-snapshot.md) | No |  | The Function to invoke after the snapshot image is created. |
| type | string | Yes | "'image/png'" | The format of the image to create, usually `image/png` or `image/jpeg`. |
| encoderOptions | number | Yes | 0.92 | The image quality, between 0 and 1. Used for image formats with lossy compression, such as `image/jpeg`. |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGL Renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2904](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2904)  
> Since: 3.16.0

---

## snapshotFramebuffer

### <instance> snapshotFramebuffer(framebuffer, bufferWidth, bufferHeight, callback, [getPixel], [x], [y], [width], [height], [type], [encoderOptions])

**Description:**

Takes a snapshot of the given area of the given frame buffer.

Unlike the other snapshot methods, this one is processed immediately and doesn't wait for the next render.

Snapshots work by using the WebGL `readPixels` feature to grab every pixel from the frame buffer into an ArrayBufferView.

It then parses this, copying the contents to a temporary Canvas and finally creating an Image object from it,

which is the image returned to the callback provided. All in all, this is a computationally expensive and blocking process,

which gets more expensive the larger the canvas size gets, so please be careful how you employ this in your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| framebuffer | [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md) | No |  | The framebuffer to grab from. |
| --- | --- | --- | --- | --- |
| bufferWidth | number | No |  | The width of the framebuffer. |
| bufferHeight | number | No |  | The height of the framebuffer. |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](../typedef/types-renderer-snapshot.md) | No |  | The Function to invoke after the snapshot image is created. |
| getPixel | boolean | Yes | false | Grab a single pixel as a Color object, or an area as an Image object? |
| x | number | Yes | 0 | The x coordinate to grab from. This is based on the framebuffer, not the world. |
| y | number | Yes | 0 | The y coordinate to grab from. This is based on the framebuffer, not the world. |
| width | number | Yes | "bufferWidth" | The width of the area to grab. |
| height | number | Yes | "bufferHeight" | The height of the area to grab. |
| type | string | Yes | "'image/png'" | The format of the image to create, usually `image/png` or `image/jpeg`. |
| encoderOptions | number | Yes | 0.92 | The image quality, between 0 and 1. Used for image formats with lossy compression, such as `image/jpeg`. |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGL Renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2976](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2976)  
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
| x | number | No | The x coordinate of the pixel to get. This is based on the game viewport, not the world. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the pixel to get. This is based on the game viewport, not the world. |
| callback | [Phaser.Types.Renderer.Snapshot.SnapshotCallback](../typedef/types-renderer-snapshot.md) | No | The Function to invoke after the snapshot pixel data is extracted. |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGL Renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L2946](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2946)  
> Since: 3.16.0

---

## startCapture

### <instance> startCapture([commandCount], [quickCapture], [fullCapture])

**Description:**

This method is only available in the Debug Build of Phaser, or a build with the

`WEBGL_DEBUG` flag set in the Webpack Config.

Phaser v3.60 Debug has a build of Spector.js embedded in it, which is a WebGL inspector

that allows for live inspection of your WebGL calls. Although it's easy to add the Spector

extension to a desktop browsr, by embedding it in Phaser we can make it available in mobile

browsers too, making it a powerful tool for debugging WebGL games on mobile devices where

extensions are not permitted.

See <https://github.com/BabylonJS/Spector.js> for more details.

This method will start a capture on the Phaser canvas. The capture will stop once it reaches

the number of commands specified as a parameter, or after 10 seconds. If quick capture is true,

the thumbnails are not captured in order to speed up the capture.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| commandCount | number | Yes | 0 | The number of commands to capture. If zero it will capture for 10 seconds. |
| --- | --- | --- | --- | --- |
| quickCapture | boolean | Yes | false | If `true` thumbnails are not captured in order to speed up the capture. |
| fullCapture | boolean | Yes | false | If `true` all details are captured. |

> Source: [src/renderer/webgl/WebGLRenderer.js#L1258](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1258)  
> Since: 3.60.0

---

## stopCapture

### <instance> stopCapture()

**Description:**

This method is only available in the Debug Build of Phaser, or a build with the

`WEBGL_DEBUG` flag set in the Webpack Config.

Phaser v3.60 Debug has a build of Spector.js embedded in it, which is a WebGL inspector

that allows for live inspection of your WebGL calls. Although it's easy to add the Spector

extension to a desktop browsr, by embedding it in Phaser we can make it available in mobile

browsers too, making it a powerful tool for debugging WebGL games on mobile devices where

extensions are not permitted.

See <https://github.com/BabylonJS/Spector.js> for more details.

This method will stop the current capture and returns the result in JSON. It displays the

result if the UI has been displayed. This returns undefined if the capture has not been completed

or did not find any commands.

**Returns:** object - The current capture.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1295)  
> Since: 3.60.0

---

## supportsCompressedTexture

### <instance> supportsCompressedTexture(baseFormat, [format])

**Description:**

Checks if the given compressed texture format is supported, or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| baseFormat | string | No | The Base Format to check. |
| --- | --- | --- | --- |
| format | GLenum | Yes | An optional GLenum format to check within the base format. |

**Returns:** boolean - True if the format is supported, otherwise false.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1513](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1513)  
> Since: 3.60.0

---

## updateBlendMode

### <instance> updateBlendMode(index, func, equation)

**Description:**

Updates the function bound to a given custom blend mode.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the custom blend mode. |
| --- | --- | --- | --- |
| func | function | No | The function to use for the blend mode. |
| equation | function | No | The equation to use for the blend mode. |

**Returns:** [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) - This WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLRenderer.js#L1865](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1865)  
> Since: 3.0.0

---

## updateCanvasTexture

### <instance> updateCanvasTexture(srcCanvas, dstTexture, [flipY], [noRepeat])

**Description:**

Updates a WebGL Texture based on the given Canvas Element.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| srcCanvas | HTMLCanvasElement | No |  | The Canvas to update the WebGL Texture from. |
| --- | --- | --- | --- | --- |
| dstTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No |  | The destination WebGLTextureWrapper to update. |
| flipY | boolean | Yes | false | Should the WebGL Texture set `UNPACK_MULTIPLY_FLIP_Y`? |
| noRepeat | boolean | Yes | false | Should this canvas be allowed to set `REPEAT` (such as for Text objects?) |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) - The updated WebGLTextureWrapper. This is the same wrapper object as `dstTexture`.

> Source: [src/renderer/webgl/WebGLRenderer.js#L3119](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L3119)  
> Since: 3.20.0

---

## updateVideoTexture

### <instance> updateVideoTexture(srcVideo, dstTexture, [flipY], [noRepeat])

**Description:**

Updates a WebGL Texture based on the given HTML Video Element.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| srcVideo | HTMLVideoElement | No |  | The Video to update the WebGL Texture with. |
| --- | --- | --- | --- | --- |
| dstTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No |  | The destination WebGLTextureWrapper to update. |
| flipY | boolean | Yes | false | Should the WebGL Texture set `UNPACK_MULTIPLY_FLIP_Y`? |
| noRepeat | boolean | Yes | false | Should this canvas be allowed to set `REPEAT`? |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) - The updated WebGLTextureWrapper. This is the same wrapper object as `dstTexture`.

> Source: [src/renderer/webgl/WebGLRenderer.js#L3214](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L3214)  
> Since: 3.20.0

---

## videoToTexture

### <instance> videoToTexture(srcVideo, [dstTexture], [noRepeat], [flipY])

**Description:**

Creates or updates a WebGL Texture based on the given HTML Video Element.

If the `dstTexture` parameter is given, the WebGL Texture is updated, rather than created fresh.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| srcVideo | HTMLVideoElement | No |  | The Video to create the WebGL Texture from |
| --- | --- | --- | --- | --- |
| dstTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | Yes |  | The destination WebGLTextureWrapper to set. |
| noRepeat | boolean | Yes | false | Should this canvas be allowed to set `REPEAT`? |
| flipY | boolean | Yes | false | Should the WebGL Texture set `UNPACK_MULTIPLY_FLIP_Y`? |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) - The newly created, or updated, WebGLTextureWrapper.

> Source: [src/renderer/webgl/WebGLRenderer.js#L3140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L3140)  
> Since: 3.85.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

Internal boot handler. Calls 'boot' on each pipeline.

**Access:** private

> Source: [src/renderer/webgl/WebGLRenderer.js#L883](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L883)  
> Since: 3.11.0

---

## getCurrentStencilMask

### <instance> getCurrentStencilMask()

**Description:**

Return the current stencil mask.

**Access:** private

> Source: [src/renderer/webgl/WebGLRenderer.js#L2590](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L2590)  
> Since: 3.50.0

---

## onCapture

### <instance> onCapture(capture)

**Description:**

This method is only available in the Debug Build of Phaser, or a build with the

`WEBGL_DEBUG` flag set in the Webpack Config.

Internal onCapture handler.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| capture | object | No | The capture data. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/WebGLRenderer.js#L1324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L1324)  
> Since: 3.60.0

---

# Public Members

## blankTexture

### blankTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md)

**Description:**

A blank 32x32 transparent texture, as used by the Graphics system where needed.

This is set in the `boot` method.

> Source: [src/renderer/webgl/WebGLRenderer.js#L487](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L487)  
> Since: 3.12.0

---

## blendModes

### blendModes: array

**Description:**

An array of blend modes supported by the WebGL Renderer.

This array includes the default blend modes as well as any custom blend modes added through <#addBlendMode>.

> Source: [src/renderer/webgl/WebGLRenderer.js#L172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L172)  
> Since: 3.0.0

---

## canvas

### canvas: HTMLCanvasElement

**Description:**

The canvas which this WebGL Renderer draws to.

> Source: [src/renderer/webgl/WebGLRenderer.js#L163](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L163)  
> Since: 3.0.0

---

## compression

### compression: [Phaser.Types.Renderer.WebGL.WebGLTextureCompression](../typedef/types-renderer-webgl.md)

**Description:**

Stores the WebGL texture compression formats that this device and browser supports.

Support for using compressed texture formats was added in Phaser version 3.60.

> Source: [src/renderer/webgl/WebGLRenderer.js#L466](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L466)  
> Since: 3.8.0

---

## config

### config: object

**Description:**

The local configuration settings of this WebGL Renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L88)  
> Since: 3.0.0

---

## contextLost

### contextLost: boolean

**Description:**

This property is set to `true` if the WebGL context of the renderer is lost.

> Source: [src/renderer/webgl/WebGLRenderer.js#L184](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L184)  
> Since: 3.0.0

---

## contextLostHandler

### contextLostHandler: function

**Description:**

The handler to invoke when the context is lost.

This should not be changed and is set in the init method.

> Source: [src/renderer/webgl/WebGLRenderer.js#L358](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L358)  
> Since: 3.19.0

---

## contextRestoredHandler

### contextRestoredHandler: function

**Description:**

The handler to invoke when the context is restored.

This should not be changed and is set in the init method.

> Source: [src/renderer/webgl/WebGLRenderer.js#L368](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L368)  
> Since: 3.19.0

---

## currentBlendMode

### currentBlendMode: number

**Description:**

Current blend mode in use

> Source: [src/renderer/webgl/WebGLRenderer.js#L321](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L321)  
> Since: 3.0.0

---

## currentCameraMask

### currentCameraMask: any

**Description:**

Internal property that tracks the currently set camera mask.

> Source: [src/renderer/webgl/WebGLRenderer.js#L548](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L548)  
> Since: 3.17.0

---

## currentFramebuffer

### currentFramebuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md)

**Description:**

The currently bound framebuffer in use.

> Source: [src/renderer/webgl/WebGLRenderer.js#L292](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L292)  
> Since: 3.0.0

---

## currentMask

### currentMask: any

**Description:**

Internal property that tracks the currently set mask.

> Source: [src/renderer/webgl/WebGLRenderer.js#L539](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L539)  
> Since: 3.17.0

---

## currentProgram

### currentProgram: [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](renderer-webgl-wrappers-webglprogramwrapper.md)

**Description:**

Current WebGLProgram in use.

> Source: [src/renderer/webgl/WebGLRenderer.js#L311](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L311)  
> Since: 3.0.0

---

## currentScissor

### currentScissor: Uint32Array

**Description:**

Stores the current scissor data

> Source: [src/renderer/webgl/WebGLRenderer.js#L340](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L340)  
> Since: 3.0.0

---

## currentScissorEnabled

### currentScissorEnabled: boolean

**Description:**

Indicates if the the scissor state is enabled in WebGLRenderingContext

> Source: [src/renderer/webgl/WebGLRenderer.js#L330](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L330)  
> Since: 3.0.0

---

## currentType

### currentType: string

**Description:**

The `type` of the Game Object being currently rendered.

This can be used by advanced render functions for batching look-ahead.

> Source: [src/renderer/webgl/WebGLRenderer.js#L567](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L567)  
> Since: 3.19.0

---

## drawingBufferHeight

### drawingBufferHeight: number

**Description:**

Cached drawing buffer height to reduce gl calls.

> Source: [src/renderer/webgl/WebGLRenderer.js#L477](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L477)  
> Since: 3.11.0

---

## extensions

### extensions: object

**Description:**

The WebGL Extensions loaded into the current context.

> Source: [src/renderer/webgl/WebGLRenderer.js#L445](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L445)  
> Since: 3.0.0

---

## fboStack

### fboStack: Array.<[Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md)>

**Description:**

A stack into which the frame buffer objects are pushed and popped.

> Source: [src/renderer/webgl/WebGLRenderer.js#L302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L302)  
> Since: 3.50.0

---

## finalType

### finalType: boolean

**Description:**

Is the Game Object being currently rendered the final one in the list?

> Source: [src/renderer/webgl/WebGLRenderer.js#L597](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L597)  
> Since: 3.50.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

The Game instance which owns this WebGL Renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L108)  
> Since: 3.0.0

---

## gl

### gl: WebGLRenderingContext

**Description:**

The underlying WebGL context of the renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L398](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L398)  
> Since: 3.0.0

---

## glAttribLocationWrappers

### glAttribLocationWrappers: Array.<[Phaser.Renderer.WebGL.Wrappers.WebGLAttribLocationWrapper](renderer-webgl-wrappers-webglattriblocationwrapper.md)>

**Description:**

A list of all WebGLAttribLocationWrappers that have been created by this renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L274](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L274)  
> Since: 3.80.0

---

## glBufferWrappers

### glBufferWrappers: Array.<[Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper](renderer-webgl-wrappers-webglbufferwrapper.md)>

**Description:**

A list of all WebGLBufferWrappers that have been created by this renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L238](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L238)  
> Since: 3.80.0

---

## glFormats

### glFormats: array

**Description:**

Stores the current WebGL component formats for further use.

This array is populated in the `init` method.

> Source: [src/renderer/webgl/WebGLRenderer.js#L455](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L455)  
> Since: 3.2.0

---

## glFramebufferWrappers

### glFramebufferWrappers: Array.<[Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md)>

**Description:**

A list of all WebGLFramebufferWrappers that have been created by this renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L265](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L265)  
> Since: 3.80.0

---

## glFuncMap

### glFuncMap: any

**Description:**

Internal gl function mapping for uniform look-up.

<https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/uniform>

> Source: [src/renderer/webgl/WebGLRenderer.js#L557](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L557)  
> Since: 3.17.0

---

## glProgramWrappers

### glProgramWrappers: Array.<[Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](renderer-webgl-wrappers-webglprogramwrapper.md)>

**Description:**

A list of all WebGLProgramWrappers that have been created by this renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L247)  
> Since: 3.80.0

---

## glTextureWrappers

### glTextureWrappers: Array.<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md)>

**Description:**

A list of all WebGLTextureWrappers that have been created by this renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L256](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L256)  
> Since: 3.80.0

---

## glUniformLocationWrappers

### glUniformLocationWrappers: Array.<[Phaser.Renderer.WebGL.Wrappers.WebGLUniformLocationWrapper](renderer-webgl-wrappers-webgluniformlocationwrapper.md)>

**Description:**

A list of all WebGLUniformLocationWrappers that have been created by this renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L283)  
> Since: 3.80.0

---

## height

### height: number

**Description:**

The height of the canvas being rendered to.

This is populated in the onResize event handler.

> Source: [src/renderer/webgl/WebGLRenderer.js#L153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L153)  
> Since: 3.0.0

---

## instancedArraysExtension

### instancedArraysExtension: ANGLE\_instanced\_arrays

**Description:**

If the browser supports the `ANGLE_instanced_arrays` extension, this property will hold

a reference to the glExtension for it.

This is populated in the `setExtensions` method.

> Source: [src/renderer/webgl/WebGLRenderer.js#L419](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L419)  
> Since: 3.50.0

---

## isBooted

### isBooted: boolean

**Description:**

Has this renderer fully booted yet?

> Source: [src/renderer/webgl/WebGLRenderer.js#L646](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L646)  
> Since: 3.50.0

---

## maskCount

### maskCount: number

**Description:**

The total number of masks currently stacked.

> Source: [src/renderer/webgl/WebGLRenderer.js#L521](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L521)  
> Since: 3.17.0

---

## maskSource

### maskSource: [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md)

**Description:**

A RenderTarget used by the BitmapMask Pipeline.

This is the source, i.e. the masked Game Object itself.

> Source: [src/renderer/webgl/WebGLRenderer.js#L693](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L693)  
> Since: 3.60.0

---

## maskStack

### maskStack: Array.<[Phaser.Display.Masks.GeometryMask](display-masks-geometrymask.md)>

**Description:**

The mask stack.

> Source: [src/renderer/webgl/WebGLRenderer.js#L530](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L530)  
> Since: 3.17.0

---

## maskTarget

### maskTarget: [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md)

**Description:**

A RenderTarget used by the BitmapMask Pipeline.

This is the target, i.e. the framebuffer the masked objects are drawn to.

> Source: [src/renderer/webgl/WebGLRenderer.js#L704](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L704)  
> Since: 3.60.0

---

## maxTextures

### maxTextures: number

**Description:**

The maximum number of textures the GPU can handle. The minimum under the WebGL1 spec is 8.

This is set via the Game Config `maxTextures` property and should never be changed after boot.

> Source: [src/renderer/webgl/WebGLRenderer.js#L217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L217)  
> Since: 3.50.0

---

## mipmapFilter

### mipmapFilter: GLenum

**Description:**

The mipmap magFilter to be used when creating textures.

You can specify this as a string in the game config, i.e.:

`render: { mipmapFilter: 'NEAREST_MIPMAP_LINEAR' }`

The 6 options for WebGL1 are, in order from least to most computationally expensive:

NEAREST (for pixel art)

LINEAR (the default)

NEAREST\_MIPMAP\_NEAREST

LINEAR\_MIPMAP\_NEAREST

NEAREST\_MIPMAP\_LINEAR

LINEAR\_MIPMAP\_LINEAR

Mipmaps only work with textures that are fully power-of-two in size.

For more details see <https://webglfundamentals.org/webgl/lessons/webgl-3d-textures.html>

As of v3.60 no mipmaps will be generated unless a string is given in

the game config. This saves on VRAM use when it may not be required.

To obtain the previous result set the property to `LINEAR` in the config.

> Source: [src/renderer/webgl/WebGLRenderer.js#L606](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L606)  
> Since: 3.21.0

---

## newType

### newType: boolean

**Description:**

Is the `type` of the Game Object being currently rendered different than the

type of the object before it in the display list? I.e. it's a 'new' type.

> Source: [src/renderer/webgl/WebGLRenderer.js#L577](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L577)  
> Since: 3.19.0

---

## nextTypeMatch

### nextTypeMatch: boolean

**Description:**

Does the `type` of the next Game Object in the display list match that

of the object being currently rendered?

> Source: [src/renderer/webgl/WebGLRenderer.js#L587](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L587)  
> Since: 3.19.0

---

## normalTexture

### normalTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md)

**Description:**

A blank 1x1 #7f7fff texture, a flat normal map,

as used by the Graphics system where needed.

This is set in the `boot` method.

> Source: [src/renderer/webgl/WebGLRenderer.js#L498](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L498)  
> Since: 3.80.0

---

## pipelines

### pipelines: [Phaser.Renderer.WebGL.PipelineManager](renderer-webgl-pipelinemanager.md)

**Description:**

An instance of the Pipeline Manager class, that handles all WebGL Pipelines.

Use this to manage all of your interactions with pipelines, such as adding, getting,

setting and rendering them.

The Pipeline Manager class is created in the `init` method and then populated

with pipelines during the `boot` method.

Prior to Phaser v3.50.0 this was just a plain JavaScript object, not a class.

> Source: [src/renderer/webgl/WebGLRenderer.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L126)  
> Since: 3.50.0

---

## previousContextLostHandler

### previousContextLostHandler: function

**Description:**

The previous contextLostHandler that was in use.

This is set when `setContextHandlers` is called.

> Source: [src/renderer/webgl/WebGLRenderer.js#L378](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L378)  
> Since: 3.19.0

---

## previousContextRestoredHandler

### previousContextRestoredHandler: function

**Description:**

The previous contextRestoredHandler that was in use.

This is set when `setContextHandlers` is called.

> Source: [src/renderer/webgl/WebGLRenderer.js#L388](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L388)  
> Since: 3.19.0

---

## projectionHeight

### projectionHeight: number

**Description:**

The cached height of the Projection matrix.

> Source: [src/renderer/webgl/WebGLRenderer.js#L684](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L684)  
> Since: 3.50.0

---

## projectionMatrix

### projectionMatrix: [Phaser.Math.Matrix4](math-matrix4.md)

**Description:**

The global game Projection matrix, used by shaders as 'uProjectionMatrix' uniform.

> Source: [src/renderer/webgl/WebGLRenderer.js#L666](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L666)  
> Since: 3.50.0

---

## projectionWidth

### projectionWidth: number

**Description:**

The cached width of the Projection matrix.

> Source: [src/renderer/webgl/WebGLRenderer.js#L675](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L675)  
> Since: 3.50.0

---

## renderTarget

### renderTarget: [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md)

**Description:**

A Render Target you can use to capture the current state of the Renderer.

A Render Target encapsulates a framebuffer and texture for the WebGL Renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L655](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L655)  
> Since: 3.50.0

---

## scissorStack

### scissorStack: Uint32Array

**Description:**

Stack of scissor data

> Source: [src/renderer/webgl/WebGLRenderer.js#L349](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L349)  
> Since: 3.0.0

---

## snapshotState

### snapshotState: [Phaser.Types.Renderer.Snapshot.SnapshotState](../typedef/types-renderer-snapshot.md)

**Description:**

Details about the currently scheduled snapshot.

If a non-null `callback` is set in this object, a snapshot of the canvas will be taken after the current frame is fully rendered.

> Source: [src/renderer/webgl/WebGLRenderer.js#L194](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L194)  
> Since: 3.0.0

---

## spector

### spector: function

**Description:**

An instance of SpectorJS used for WebGL Debugging.

Only available in the Phaser Debug build.

> Source: [src/renderer/webgl/WebGLRenderer.js#L715](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L715)  
> Since: 3.60.0

---

## supportedExtensions

### supportedExtensions: Array.<string>

**Description:**

Array of strings that indicate which WebGL extensions are supported by the browser.

This is populated in the `setExtensions` method.

> Source: [src/renderer/webgl/WebGLRenderer.js#L408](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L408)  
> Since: 3.0.0

---

## textureIndexes

### textureIndexes: array

**Description:**

An array of the available WebGL texture units, used to populate the uSampler uniforms.

This array is populated during the init phase and should never be changed after boot.

> Source: [src/renderer/webgl/WebGLRenderer.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L227)  
> Since: 3.50.0

---

## type

### type: number

**Description:**

A constant which allows the renderer to be easily identified as a WebGL Renderer.

> Source: [src/renderer/webgl/WebGLRenderer.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L117)  
> Since: 3.0.0

---

## vaoExtension

### vaoExtension: OES\_vertex\_array\_object

**Description:**

If the browser supports the `OES_vertex_array_object` extension, this property will hold

a reference to the glExtension for it.

This is populated in the `setExtensions` method.

> Source: [src/renderer/webgl/WebGLRenderer.js#L432](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L432)  
> Since: 3.50.0

---

## whiteTexture

### whiteTexture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md)

**Description:**

A pure white 4x4 texture, as used by the Graphics system where needed.

This is set in the `boot` method.

> Source: [src/renderer/webgl/WebGLRenderer.js#L510](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L510)  
> Since: 3.50.0

---

## width

### width: number

**Description:**

The width of the canvas being rendered to.

This is populated in the onResize event handler.

> Source: [src/renderer/webgl/WebGLRenderer.js#L143](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L143)  
> Since: 3.0.0

---

# Private Members

## \_debugCapture

### \_debugCapture: boolean

**Description:**

Is Spector currently capturing a WebGL frame?

**Access:** private

> Source: [src/renderer/webgl/WebGLRenderer.js#L726](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L726)  
> Since: 3.60.0

---

## defaultScissor

### defaultScissor: Array.<number>

**Description:**

The default scissor, set during `preRender` and modified during `resize`.

**Access:** private

> Source: [src/renderer/webgl/WebGLRenderer.js#L636](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLRenderer.js#L636)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Methods](#public-methods)

  + [addBlendMode](#addblendmode)

    - [<instance> addBlendMode(func, equation)](#instance-addblendmodefunc-equation)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [beginBitmapMask](#beginbitmapmask)

    - [<instance> beginBitmapMask(mask, camera)](#instance-beginbitmapmaskmask-camera)
  + [beginCapture](#begincapture)

    - [<instance> beginCapture([width], [height])](#instance-begincapturewidth-height)
  + [canvasToTexture](#canvastotexture)

    - [<instance> canvasToTexture(srcCanvas, [dstTexture], [noRepeat], [flipY])](#instance-canvastotexturesrccanvas-dsttexture-norepeat-flipy)
  + [captureFrame](#captureframe)

    - [<instance> captureFrame([quickCapture], [fullCapture])](#instance-captureframequickcapture-fullcapture)
  + [captureNextFrame](#capturenextframe)

    - [<instance> captureNextFrame()](#instance-capturenextframe)
  + [clearStencilMask](#clearstencilmask)

    - [<instance> clearStencilMask()](#instance-clearstencilmask)
  + [createAttribLocation](#createattriblocation)

    - [<instance> createAttribLocation(program, name)](#instance-createattriblocationprogram-name)
  + [createCanvasTexture](#createcanvastexture)

    - [<instance> createCanvasTexture(srcCanvas, [noRepeat], [flipY])](#instance-createcanvastexturesrccanvas-norepeat-flipy)
  + [createFramebuffer](#createframebuffer)

    - [<instance> createFramebuffer(width, height, renderTexture, [addDepthStencilBuffer])](#instance-createframebufferwidth-height-rendertexture-adddepthstencilbuffer)
  + [createIndexBuffer](#createindexbuffer)

    - [<instance> createIndexBuffer(initialDataOrSize, bufferUsage)](#instance-createindexbufferinitialdataorsize-bufferusage)
  + [createProgram](#createprogram)

    - [<instance> createProgram(vertexShader, fragmentShader)](#instance-createprogramvertexshader-fragmentshader)
  + [createTemporaryTextures](#createtemporarytextures)

    - [<instance> createTemporaryTextures()](#instance-createtemporarytextures)
  + [createTexture2D](#createtexture2d)

    - [<instance> createTexture2D(mipLevel, minFilter, magFilter, wrapT, wrapS, format, pixels, width, height, [pma], [forceSize], [flipY])](#instance-createtexture2dmiplevel-minfilter-magfilter-wrapt-wraps-format-pixels-width-height-pma-forcesize-flipy)
  + [createTextureFromSource](#createtexturefromsource)

    - [<instance> createTextureFromSource(source, width, height, scaleMode, [forceClamp])](#instance-createtexturefromsourcesource-width-height-scalemode-forceclamp)
  + [createUint8ArrayTexture](#createuint8arraytexture)

    - [<instance> createUint8ArrayTexture(data, width, height)](#instance-createuint8arraytexturedata-width-height)
  + [createUniformLocation](#createuniformlocation)

    - [<instance> createUniformLocation(program, name)](#instance-createuniformlocationprogram-name)
  + [createVertexBuffer](#createvertexbuffer)

    - [<instance> createVertexBuffer(initialDataOrSize, bufferUsage)](#instance-createvertexbufferinitialdataorsize-bufferusage)
  + [createVideoTexture](#createvideotexture)

    - [<instance> createVideoTexture(srcVideo, [noRepeat], [flipY])](#instance-createvideotexturesrcvideo-norepeat-flipy)
  + [deleteAttribLocation](#deleteattriblocation)

    - [<instance> deleteAttribLocation(attrib)](#instance-deleteattriblocationattrib)
  + [deleteBuffer](#deletebuffer)

    - [<instance> deleteBuffer(vertexBuffer)](#instance-deletebuffervertexbuffer)
  + [deleteFramebuffer](#deleteframebuffer)

    - [<instance> deleteFramebuffer(framebuffer)](#instance-deleteframebufferframebuffer)
  + [deleteProgram](#deleteprogram)

    - [<instance> deleteProgram(program)](#instance-deleteprogramprogram)
  + [deleteTexture](#deletetexture)

    - [<instance> deleteTexture(texture)](#instance-deletetexturetexture)
  + [deleteUniformLocation](#deleteuniformlocation)

    - [<instance> deleteUniformLocation(uniform)](#instance-deleteuniformlocationuniform)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [dispatchContextLost](#dispatchcontextlost)

    - [<instance> dispatchContextLost(event)](#instance-dispatchcontextlostevent)
  + [dispatchContextRestored](#dispatchcontextrestored)

    - [<instance> dispatchContextRestored(event)](#instance-dispatchcontextrestoredevent)
  + [drawBitmapMask](#drawbitmapmask)

    - [<instance> drawBitmapMask(mask, camera, bitmapMaskPipeline)](#instance-drawbitmapmaskmask-camera-bitmapmaskpipeline)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [endCapture](#endcapture)

    - [<instance> endCapture()](#instance-endcapture)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [flush](#flush)

    - [<instance> flush()](#instance-flush)
  + [getAspectRatio](#getaspectratio)

    - [<instance> getAspectRatio()](#instance-getaspectratio)
  + [getCompressedTextureName](#getcompressedtexturename)

    - [<instance> getCompressedTextureName(baseFormat, [format])](#instance-getcompressedtexturenamebaseformat-format)
  + [getCompressedTextures](#getcompressedtextures)

    - [<instance> getCompressedTextures()](#instance-getcompressedtextures)
  + [getExtension](#getextension)

    - [<instance> getExtension(extensionName)](#instance-getextensionextensionname)
  + [getFps](#getfps)

    - [<instance> getFps()](#instance-getfps)
  + [getMaxTextureSize](#getmaxtexturesize)

    - [<instance> getMaxTextureSize()](#instance-getmaxtexturesize)
  + [hasActiveStencilMask](#hasactivestencilmask)

    - [<instance> hasActiveStencilMask()](#instance-hasactivestencilmask)
  + [hasExtension](#hasextension)

    - [<instance> hasExtension(extensionName)](#instance-hasextensionextensionname)
  + [init](#init)

    - [<instance> init(config)](#instance-initconfig)
  + [isNewNormalMap](#isnewnormalmap)

    - [<instance> isNewNormalMap(texture, normalMap)](#instance-isnewnormalmaptexture-normalmap)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [log](#log)

    - [<instance> log(arguments)](#instance-logarguments)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [onResize](#onresize)

    - [<instance> onResize(gameSize, baseSize)](#instance-onresizegamesize-basesize)
  + [popFramebuffer](#popframebuffer)

    - [<instance> popFramebuffer([updateScissor], [setViewport])](#instance-popframebufferupdatescissor-setviewport)
  + [popScissor](#popscissor)

    - [<instance> popScissor()](#instance-popscissor)
  + [postRender](#postrender)

    - [<instance> postRender()](#instance-postrender)
  + [postRenderCamera](#postrendercamera)

    - [<instance> postRenderCamera(camera)](#instance-postrendercameracamera)
  + [preRender](#prerender)

    - [<instance> preRender()](#instance-prerender)
  + [preRenderCamera](#prerendercamera)

    - [<instance> preRenderCamera(camera)](#instance-prerendercameracamera)
  + [pushFramebuffer](#pushframebuffer)

    - [<instance> pushFramebuffer(framebuffer, [updateScissor], [setViewport], [texture], [clear])](#instance-pushframebufferframebuffer-updatescissor-setviewport-texture-clear)
  + [pushScissor](#pushscissor)

    - [<instance> pushScissor(x, y, width, height, [drawingBufferHeight])](#instance-pushscissorx-y-width-height-drawingbufferheight)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeBlendMode](#removeblendmode)

    - [<instance> removeBlendMode(index)](#instance-removeblendmodeindex)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [render](#render)

    - [<instance> render(scene, children, camera)](#instance-renderscene-children-camera)
  + [resetProgram](#resetprogram)

    - [<instance> resetProgram()](#instance-resetprogram)
  + [resetProjectionMatrix](#resetprojectionmatrix)

    - [<instance> resetProjectionMatrix()](#instance-resetprojectionmatrix)
  + [resetScissor](#resetscissor)

    - [<instance> resetScissor()](#instance-resetscissor)
  + [resetViewport](#resetviewport)

    - [<instance> resetViewport()](#instance-resetviewport)
  + [resize](#resize)

    - [<instance> resize([width], [height])](#instance-resizewidth-height)
  + [restoreFramebuffer](#restoreframebuffer)

    - [<instance> restoreFramebuffer([updateScissor], [setViewport])](#instance-restoreframebufferupdatescissor-setviewport)
  + [restoreStencilMask](#restorestencilmask)

    - [<instance> restoreStencilMask()](#instance-restorestencilmask)
  + [setBlendMode](#setblendmode)

    - [<instance> setBlendMode(blendModeId, [force])](#instance-setblendmodeblendmodeid-force)
  + [setContextHandlers](#setcontexthandlers)

    - [<instance> setContextHandlers([contextLost], [contextRestored])](#instance-setcontexthandlerscontextlost-contextrestored)
  + [setExtensions](#setextensions)

    - [<instance> setExtensions()](#instance-setextensions)
  + [setFramebuffer](#setframebuffer)

    - [<instance> setFramebuffer(framebuffer, [updateScissor], [setViewport], [texture], [clear])](#instance-setframebufferframebuffer-updatescissor-setviewport-texture-clear)
  + [setProgram](#setprogram)

    - [<instance> setProgram(program)](#instance-setprogramprogram)
  + [setProjectionMatrix](#setprojectionmatrix)

    - [<instance> setProjectionMatrix(width, height)](#instance-setprojectionmatrixwidth-height)
  + [setScissor](#setscissor)

    - [<instance> setScissor(x, y, width, height, [drawingBufferHeight])](#instance-setscissorx-y-width-height-drawingbufferheight)
  + [setTextureFilter](#settexturefilter)

    - [<instance> setTextureFilter(texture, filter)](#instance-settexturefiltertexture-filter)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [snapshot](#snapshot)

    - [<instance> snapshot(callback, [type], [encoderOptions])](#instance-snapshotcallback-type-encoderoptions)
  + [snapshotArea](#snapshotarea)

    - [<instance> snapshotArea(x, y, width, height, callback, [type], [encoderOptions])](#instance-snapshotareax-y-width-height-callback-type-encoderoptions)
  + [snapshotFramebuffer](#snapshotframebuffer)

    - [<instance> snapshotFramebuffer(framebuffer, bufferWidth, bufferHeight, callback, [getPixel], [x], [y], [width], [height], [type], [encoderOptions])](#instance-snapshotframebufferframebuffer-bufferwidth-bufferheight-callback-getpixel-x-y-width-height-type-encoderoptions)
  + [snapshotPixel](#snapshotpixel)

    - [<instance> snapshotPixel(x, y, callback)](#instance-snapshotpixelx-y-callback)
  + [startCapture](#startcapture)

    - [<instance> startCapture([commandCount], [quickCapture], [fullCapture])](#instance-startcapturecommandcount-quickcapture-fullcapture)
  + [stopCapture](#stopcapture)

    - [<instance> stopCapture()](#instance-stopcapture)
  + [supportsCompressedTexture](#supportscompressedtexture)

    - [<instance> supportsCompressedTexture(baseFormat, [format])](#instance-supportscompressedtexturebaseformat-format)
  + [updateBlendMode](#updateblendmode)

    - [<instance> updateBlendMode(index, func, equation)](#instance-updateblendmodeindex-func-equation)
  + [updateCanvasTexture](#updatecanvastexture)

    - [<instance> updateCanvasTexture(srcCanvas, dstTexture, [flipY], [noRepeat])](#instance-updatecanvastexturesrccanvas-dsttexture-flipy-norepeat)
  + [updateVideoTexture](#updatevideotexture)

    - [<instance> updateVideoTexture(srcVideo, dstTexture, [flipY], [noRepeat])](#instance-updatevideotexturesrcvideo-dsttexture-flipy-norepeat)
  + [videoToTexture](#videototexture)

    - [<instance> videoToTexture(srcVideo, [dstTexture], [noRepeat], [flipY])](#instance-videototexturesrcvideo-dsttexture-norepeat-flipy)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [getCurrentStencilMask](#getcurrentstencilmask)

    - [<instance> getCurrentStencilMask()](#instance-getcurrentstencilmask)
  + [onCapture](#oncapture)

    - [<instance> onCapture(capture)](#instance-oncapturecapture)
* [Public Members](#public-members)

  + [blankTexture](#blanktexture)

    - [blankTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](#blanktexture-phaserrendererwebglwrapperswebgltexturewrapper)
  + [blendModes](#blendmodes)

    - [blendModes: array](#blendmodes-array)
  + [canvas](#canvas)

    - [canvas: HTMLCanvasElement](#canvas-htmlcanvaselement)
  + [compression](#compression)

    - [compression: Phaser.Types.Renderer.WebGL.WebGLTextureCompression](#compression-phasertypesrendererwebglwebgltexturecompression)
  + [config](#config)

    - [config: object](#config-object)
  + [contextLost](#contextlost)

    - [contextLost: boolean](#contextlost-boolean)
  + [contextLostHandler](#contextlosthandler)

    - [contextLostHandler: function](#contextlosthandler-function)
  + [contextRestoredHandler](#contextrestoredhandler)

    - [contextRestoredHandler: function](#contextrestoredhandler-function)
  + [currentBlendMode](#currentblendmode)

    - [currentBlendMode: number](#currentblendmode-number)
  + [currentCameraMask](#currentcameramask)

    - [currentCameraMask: any](#currentcameramask-any)
  + [currentFramebuffer](#currentframebuffer)

    - [currentFramebuffer: Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](#currentframebuffer-phaserrendererwebglwrapperswebglframebufferwrapper)
  + [currentMask](#currentmask)

    - [currentMask: any](#currentmask-any)
  + [currentProgram](#currentprogram)

    - [currentProgram: Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](#currentprogram-phaserrendererwebglwrapperswebglprogramwrapper)
  + [currentScissor](#currentscissor)

    - [currentScissor: Uint32Array](#currentscissor-uint32array)
  + [currentScissorEnabled](#currentscissorenabled)

    - [currentScissorEnabled: boolean](#currentscissorenabled-boolean)
  + [currentType](#currenttype)

    - [currentType: string](#currenttype-string)
  + [drawingBufferHeight](#drawingbufferheight)

    - [drawingBufferHeight: number](#drawingbufferheight-number)
  + [extensions](#extensions)

    - [extensions: object](#extensions-object)
  + [fboStack](#fbostack)

    - [fboStack: Array.<Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper>](#fbostack-arrayphaserrendererwebglwrapperswebglframebufferwrapper)
  + [finalType](#finaltype)

    - [finalType: boolean](#finaltype-boolean)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [gl](#gl)

    - [gl: WebGLRenderingContext](#gl-webglrenderingcontext)
  + [glAttribLocationWrappers](#glattriblocationwrappers)

    - [glAttribLocationWrappers: Array.<Phaser.Renderer.WebGL.Wrappers.WebGLAttribLocationWrapper>](#glattriblocationwrappers-arrayphaserrendererwebglwrapperswebglattriblocationwrapper)
  + [glBufferWrappers](#glbufferwrappers)

    - [glBufferWrappers: Array.<Phaser.Renderer.WebGL.Wrappers.WebGLBufferWrapper>](#glbufferwrappers-arrayphaserrendererwebglwrapperswebglbufferwrapper)
  + [glFormats](#glformats)

    - [glFormats: array](#glformats-array)
  + [glFramebufferWrappers](#glframebufferwrappers)

    - [glFramebufferWrappers: Array.<Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper>](#glframebufferwrappers-arrayphaserrendererwebglwrapperswebglframebufferwrapper)
  + [glFuncMap](#glfuncmap)

    - [glFuncMap: any](#glfuncmap-any)
  + [glProgramWrappers](#glprogramwrappers)

    - [glProgramWrappers: Array.<Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper>](#glprogramwrappers-arrayphaserrendererwebglwrapperswebglprogramwrapper)
  + [glTextureWrappers](#gltexturewrappers)

    - [glTextureWrappers: Array.<Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper>](#gltexturewrappers-arrayphaserrendererwebglwrapperswebgltexturewrapper)
  + [glUniformLocationWrappers](#gluniformlocationwrappers)

    - [glUniformLocationWrappers: Array.<Phaser.Renderer.WebGL.Wrappers.WebGLUniformLocationWrapper>](#gluniformlocationwrappers-arrayphaserrendererwebglwrapperswebgluniformlocationwrapper)
  + [height](#height)

    - [height: number](#height-number)
  + [instancedArraysExtension](#instancedarraysextension)

    - [instancedArraysExtension: ANGLE\_instanced\_arrays](#instancedarraysextension-angle_instanced_arrays)
  + [isBooted](#isbooted)

    - [isBooted: boolean](#isbooted-boolean)
  + [maskCount](#maskcount)

    - [maskCount: number](#maskcount-number)
  + [maskSource](#masksource)

    - [maskSource: Phaser.Renderer.WebGL.RenderTarget](#masksource-phaserrendererwebglrendertarget)
  + [maskStack](#maskstack)

    - [maskStack: Array.<Phaser.Display.Masks.GeometryMask>](#maskstack-arrayphaserdisplaymasksgeometrymask)
  + [maskTarget](#masktarget)

    - [maskTarget: Phaser.Renderer.WebGL.RenderTarget](#masktarget-phaserrendererwebglrendertarget)
  + [maxTextures](#maxtextures)

    - [maxTextures: number](#maxtextures-number)
  + [mipmapFilter](#mipmapfilter)

    - [mipmapFilter: GLenum](#mipmapfilter-glenum)
  + [newType](#newtype)

    - [newType: boolean](#newtype-boolean)
  + [nextTypeMatch](#nexttypematch)

    - [nextTypeMatch: boolean](#nexttypematch-boolean)
  + [normalTexture](#normaltexture)

    - [normalTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](#normaltexture-phaserrendererwebglwrapperswebgltexturewrapper)
  + [pipelines](#pipelines)

    - [pipelines: Phaser.Renderer.WebGL.PipelineManager](#pipelines-phaserrendererwebglpipelinemanager)
  + [previousContextLostHandler](#previouscontextlosthandler)

    - [previousContextLostHandler: function](#previouscontextlosthandler-function)
  + [previousContextRestoredHandler](#previouscontextrestoredhandler)

    - [previousContextRestoredHandler: function](#previouscontextrestoredhandler-function)
  + [projectionHeight](#projectionheight)

    - [projectionHeight: number](#projectionheight-number)
  + [projectionMatrix](#projectionmatrix)

    - [projectionMatrix: Phaser.Math.Matrix4](#projectionmatrix-phasermathmatrix4)
  + [projectionWidth](#projectionwidth)

    - [projectionWidth: number](#projectionwidth-number)
  + [renderTarget](#rendertarget)

    - [renderTarget: Phaser.Renderer.WebGL.RenderTarget](#rendertarget-phaserrendererwebglrendertarget)
  + [scissorStack](#scissorstack)

    - [scissorStack: Uint32Array](#scissorstack-uint32array)
  + [snapshotState](#snapshotstate)

    - [snapshotState: Phaser.Types.Renderer.Snapshot.SnapshotState](#snapshotstate-phasertypesrenderersnapshotsnapshotstate)
  + [spector](#spector)

    - [spector: function](#spector-function)
  + [supportedExtensions](#supportedextensions)

    - [supportedExtensions: Array.<string>](#supportedextensions-arraystring)
  + [textureIndexes](#textureindexes)

    - [textureIndexes: array](#textureindexes-array)
  + [type](#type)

    - [type: number](#type-number)
  + [vaoExtension](#vaoextension)

    - [vaoExtension: OES\_vertex\_array\_object](#vaoextension-oes_vertex_array_object)
  + [whiteTexture](#whitetexture)

    - [whiteTexture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](#whitetexture-phaserrendererwebglwrapperswebgltexturewrapper)
  + [width](#width)

    - [width: number](#width-number)
* [Private Members](#private-members)

  + [\_debugCapture](#_debugcapture)

    - [\_debugCapture: boolean](#_debugcapture-boolean)
  + [defaultScissor](#defaultscissor)

    - [defaultScissor: Array.<number>](#defaultscissor-arraynumber)

Back to top

©2025[Phaser](https://docs.phaser.io)