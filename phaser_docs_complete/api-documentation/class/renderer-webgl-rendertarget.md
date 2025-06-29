# RenderTarget

Phaser.Renderer.WebGL.RenderTarget

A Render Target encapsulates a WebGL framebuffer and the WebGL Texture that displays it.

Instances of this class are typically created by, and belong to WebGL Pipelines, however

other Game Objects and classes can take advantage of Render Targets as well.

**Constructor**

`new RenderTarget(renderer, width, height, [scale], [minFilter], [autoClear], [autoResize], [addDepthBuffer], [forceClamp])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| renderer | [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) | No |  | A reference to the WebGLRenderer. |
| --- | --- | --- | --- | --- |
| width | number | No |  | The width of this Render Target. |
| height | number | No |  | The height of this Render Target. |
| scale | number | Yes | 1 | A value between 0 and 1. Controls the size of this Render Target in relation to the Renderer. |
| minFilter | number | Yes | 0 | The minFilter mode of the texture when created. 0 is `LINEAR`, 1 is `NEAREST`. |
| autoClear | boolean | Yes | true | Automatically clear this framebuffer when bound? |
| autoResize | boolean | Yes | false | Automatically resize this Render Target if the WebGL Renderer resizes? |
| addDepthBuffer | boolean | Yes | true | Add a DEPTH\_STENCIL and attachment to this Render Target? |
| forceClamp | boolean | Yes | true | Force the texture to use the CLAMP\_TO\_EDGE wrap mode, even if a power of two? |

---

**Scope**: static

> Source: [src/renderer/webgl/RenderTarget.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L10)  
> Since: 3.50.0

# Public Members

## autoClear

### autoClear: boolean

**Description:**

Controls if this Render Target is automatically cleared (via `gl.COLOR_BUFFER_BIT`)

during the `RenderTarget.bind` method.

If you need more control over how, or if, the target is cleared, you can disable

this via the config on creation, or even toggle it directly at runtime.

> Source: [src/renderer/webgl/RenderTarget.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L116)  
> Since: 3.50.0

---

## autoResize

### autoResize: boolean

**Description:**

Does this Render Target automatically resize when the WebGL Renderer does?

Modify this property via the `setAutoResize` method.

> Source: [src/renderer/webgl/RenderTarget.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L129)  
> Since: 3.50.0

---

## destroy

### destroy

**Description:**

Removes all external references from this class and deletes the

WebGL framebuffer and texture instances.

Does not remove this Render Target from the parent pipeline.

> Source: [src/renderer/webgl/RenderTarget.js#L420](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L420)  
> Since: 3.50.0

---

## forceClamp

### forceClamp: boolean

**Description:**

Force the WebGL Texture to use the CLAMP\_TO\_EDGE wrap mode, even if a power of two?

If `false` it will use `gl.REPEAT` instead, which may be required for some effects, such

as using this Render Target as a texture for a Shader.

> Source: [src/renderer/webgl/RenderTarget.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L151)  
> Since: 3.60.0

---

## framebuffer

### framebuffer: [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md)

**Description:**

The Framebuffer of this Render Target.

This is created in the `RenderTarget.resize` method.

> Source: [src/renderer/webgl/RenderTarget.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L54)  
> Since: 3.50.0

---

## hasDepthBuffer

### hasDepthBuffer: boolean

**Description:**

Does this Render Target have a Depth Buffer?

> Source: [src/renderer/webgl/RenderTarget.js#L141](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L141)  
> Since: 3.60.0

---

## height

### height: number

**Description:**

The height of the texture.

> Source: [src/renderer/webgl/RenderTarget.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L86)  
> Since: 3.50.0

---

## minFilter

### minFilter: number

**Description:**

The minFilter mode of the texture. 0 is `LINEAR`, 1 is `NEAREST`.

> Source: [src/renderer/webgl/RenderTarget.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L107)  
> Since: 3.50.0

---

## renderer

### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md)

**Description:**

A reference to the WebGLRenderer instance.

> Source: [src/renderer/webgl/RenderTarget.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L45)  
> Since: 3.50.0

---

## scale

### scale: number

**Description:**

A value between 0 and 1. Controls the size of this Render Target in relation to the Renderer.

A value of 1 matches it. 0.5 makes the Render Target half the size of the renderer, etc.

> Source: [src/renderer/webgl/RenderTarget.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L96)  
> Since: 3.50.0

---

## texture

### texture: [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md)

**Description:**

The WebGLTextureWrapper of this Render Target.

This is created in the `RenderTarget.resize` method.

> Source: [src/renderer/webgl/RenderTarget.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L65)  
> Since: 3.50.0

---

## unbind

### unbind

**Description:**

Unbinds this Render Target and optionally flushes the WebGL Renderer first.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| flush | boolean | Yes | false | Flush the WebGL Renderer before unbinding? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](renderer-webgl-wrappers-webglframebufferwrapper.md) - The Framebuffer that was set, or `null` if there aren't any more in the stack.

> Source: [src/renderer/webgl/RenderTarget.js#L396](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L396)  
> Since: 3.50.0

---

## width

### width: number

**Description:**

The width of the texture.

> Source: [src/renderer/webgl/RenderTarget.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L76)  
> Since: 3.50.0

---

# Public Methods

## adjustViewport

### <instance> adjustViewport()

**Description:**

Adjusts the GL viewport to match the width and height of this Render Target.

Also disables `SCISSOR_TEST`.

> Source: [src/renderer/webgl/RenderTarget.js#L341](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L341)  
> Since: 3.50.0

---

## bind

### <instance> bind([adjustViewport], [width], [height])

**Description:**

Pushes this Render Target as the current frame buffer of the renderer.

If `autoClear` is set, then clears the texture.

If `adjustViewport` is `true` then it will flush the renderer and then adjust the GL viewport.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| adjustViewport | boolean | Yes | false | Adjust the GL viewport by calling `RenderTarget.adjustViewport` ? |
| --- | --- | --- | --- | --- |
| width | number | Yes |  | Optional new width of this Render Target. |
| height | number | Yes |  | Optional new height of this Render Target. |

> Source: [src/renderer/webgl/RenderTarget.js#L292](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L292)  
> Since: 3.50.0

---

## clear

### <instance> clear([x], [y], [width], [height])

**Description:**

Clears a portion or everything from this Render Target. To clear an area,

specify the `x`, `y`, `width` and `height`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The left coordinate of the fill rectangle. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The top coordinate of the fill rectangle. |
| width | number | Yes | "this.width" | The width of the fill rectangle. |
| height | number | Yes | "this.height" | The height of the fill rectangle. |

> Source: [src/renderer/webgl/RenderTarget.js#L358](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L358)  
> Since: 3.50.0

---

## init

### <instance> init(width, height)

**Description:**

Sets up this Render Target to the given width and height, creating a new

frame buffer and texture. This method is called automatically by the constructor

and at no other time.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of this Render Target. |
| --- | --- | --- | --- |
| height | number | No | The new height of this Render Target. |

> Source: [src/renderer/webgl/RenderTarget.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L176)  
> Since: 3.86.0

---

## resize

### <instance> resize(width, height)

**Description:**

Resizes this Render Target as long as the given width and height are different

to the current width and height.

Deletes both the frame buffer and texture, if they exist and then re-creates

them using the new sizes.

This method is called automatically by the pipeline during its resize handler.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of this Render Target. |
| --- | --- | --- | --- |
| height | number | No | The new height of this Render Target. |

**Returns:** [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) - This RenderTarget instance.

> Source: [src/renderer/webgl/RenderTarget.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L227)  
> Since: 3.50.0

---

## setAutoResize

### <instance> setAutoResize(autoResize)

**Description:**

Sets if this Render Target should automatically resize when the WebGL Renderer

emits a resize event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| autoResize | boolean | No | Automatically resize this Render Target when the WebGL Renderer resizes? |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.RenderTarget](renderer-webgl-rendertarget.md) - This RenderTarget instance.

> Source: [src/renderer/webgl/RenderTarget.js#L198](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L198)  
> Since: 3.50.0

---

## willResize

### <instance> willResize(width, height)

**Description:**

Checks if this Render Target will resize, or not, if given the new

width and height values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of this Render Target. |
| --- | --- | --- | --- |
| height | number | No | The new height of this Render Target. |

**Returns:** boolean - `true` if the Render Target will resize, otherwise `false`.

> Source: [src/renderer/webgl/RenderTarget.js#L264](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/RenderTarget.js#L264)  
> Since: 3.70.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [autoClear](#autoclear)

    - [autoClear: boolean](#autoclear-boolean)
  + [autoResize](#autoresize)

    - [autoResize: boolean](#autoresize-boolean)
  + [destroy](#destroy)

    - [destroy](#destroy-1)
  + [forceClamp](#forceclamp)

    - [forceClamp: boolean](#forceclamp-boolean)
  + [framebuffer](#framebuffer)

    - [framebuffer: Phaser.Renderer.WebGL.Wrappers.WebGLFramebufferWrapper](#framebuffer-phaserrendererwebglwrapperswebglframebufferwrapper)
  + [hasDepthBuffer](#hasdepthbuffer)

    - [hasDepthBuffer: boolean](#hasdepthbuffer-boolean)
  + [height](#height)

    - [height: number](#height-number)
  + [minFilter](#minfilter)

    - [minFilter: number](#minfilter-number)
  + [renderer](#renderer)

    - [renderer: Phaser.Renderer.WebGL.WebGLRenderer](#renderer-phaserrendererwebglwebglrenderer)
  + [scale](#scale)

    - [scale: number](#scale-number)
  + [texture](#texture)

    - [texture: Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](#texture-phaserrendererwebglwrapperswebgltexturewrapper)
  + [unbind](#unbind)

    - [unbind](#unbind-1)
  + [width](#width)

    - [width: number](#width-number)
* [Public Methods](#public-methods)

  + [adjustViewport](#adjustviewport)

    - [<instance> adjustViewport()](#instance-adjustviewport)
  + [bind](#bind)

    - [<instance> bind([adjustViewport], [width], [height])](#instance-bindadjustviewport-width-height)
  + [clear](#clear)

    - [<instance> clear([x], [y], [width], [height])](#instance-clearx-y-width-height)
  + [init](#init)

    - [<instance> init(width, height)](#instance-initwidth-height)
  + [resize](#resize)

    - [<instance> resize(width, height)](#instance-resizewidth-height)
  + [setAutoResize](#setautoresize)

    - [<instance> setAutoResize(autoResize)](#instance-setautoresizeautoresize)
  + [willResize](#willresize)

    - [<instance> willResize(width, height)](#instance-willresizewidth-height)

Back to top

©2025[Phaser](https://docs.phaser.io)