# WebGLAttribLocationWrapper

Phaser.Renderer.WebGL.Wrappers.WebGLAttribLocationWrapper

Wrapper for a WebGL attribute location, containing all the information that was used to create it.

A WebGLAttribLocation should never be exposed outside the WebGLRenderer,

so the WebGLRenderer can handle context loss and other events without other systems having to be aware of it.

Always use WebGLAttribLocationWrapper instead.

**Constructor**

`new WebGLAttribLocationWrapper(gl, program, name)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| gl | WebGLRenderingContext | No | The WebGLRenderingContext to create the WebGLAttribLocation for. |
| --- | --- | --- | --- |
| program | [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](renderer-webgl-wrappers-webglprogramwrapper.md) | No | The WebGLProgram that this location refers to. This must be created first. |
| name | string | No | The name of this location, as defined in the shader source code. |

---

**Scope**: static

> Source: [src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L9)  
> Since: 3.80.0

# Public Members

## gl

### gl: WebGLRenderingContext

**Description:**

The WebGLRenderingContext that owns this location.

> Source: [src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L46)  
> Since: 3.80.0

---

## name

### name: string

**Description:**

The name of this location, as defined in the shader source code.

> Source: [src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L64)  
> Since: 3.80.0

---

## program

### program: [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](renderer-webgl-wrappers-webglprogramwrapper.md)

**Description:**

The WebGLProgram that this location refers to.

> Source: [src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L55)  
> Since: 3.80.0

---

## webGLAttribLocation

### webGLAttribLocation: GLint

**Description:**

The WebGLAttribLocation being wrapped by this class.

This property could change at any time.

Therefore, you should never store a reference to this value.

It should only be passed directly to the WebGL API for drawing.

> Source: [src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L32](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L32)  
> Since: 3.80.0

---

# Public Methods

## createResource

### <instance> createResource()

**Description:**

Creates the WebGLAttribLocation.

> Source: [src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L76)  
> Since: 3.80.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this WebGLAttribLocationWrapper.

> Source: [src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLAttribLocationWrapper.js#L102)  
> Since: 3.80.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [gl](#gl)

    - [gl: WebGLRenderingContext](#gl-webglrenderingcontext)
  + [name](#name)

    - [name: string](#name-string)
  + [program](#program)

    - [program: Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](#program-phaserrendererwebglwrapperswebglprogramwrapper)
  + [webGLAttribLocation](#webglattriblocation)

    - [webGLAttribLocation: GLint](#webglattriblocation-glint)
* [Public Methods](#public-methods)

  + [createResource](#createresource)

    - [<instance> createResource()](#instance-createresource)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)

Back to top

©2025[Phaser](https://docs.phaser.io)