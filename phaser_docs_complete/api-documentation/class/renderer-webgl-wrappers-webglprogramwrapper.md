# WebGLProgramWrapper

Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper

Wrapper for a WebGL program, containing all the information that was used to create it.

A WebGLProgram should never be exposed outside the WebGLRenderer, so the WebGLRenderer

can handle context loss and other events without other systems having to be aware of it.

Always use WebGLProgramWrapper instead.

**Constructor**

`new WebGLProgramWrapper(gl, vertexSource, fragmentShader)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| gl | WebGLRenderingContext | No | The WebGLRenderingContext to create the WebGLProgram for. |
| --- | --- | --- | --- |
| vertexSource | string | No | The vertex shader source code as a string. |
| fragmentShader | string | No | The fragment shader source code as a string. |

---

**Scope**: static

> Source: [src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L9)  
> Since: 3.80.0

# Public Members

## fragmentSource

### fragmentSource: string

**Description:**

The fragment shader source code as a string.

> Source: [src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L64)  
> Since: 3.80.0

---

## gl

### gl: WebGLRenderingContext

**Description:**

The WebGLRenderingContext that owns this WebGLProgram.

> Source: [src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L46)  
> Since: 3.80.0

---

## vertexSource

### vertexSource: string

**Description:**

The vertex shader source code as a string.

> Source: [src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L55)  
> Since: 3.80.0

---

## webGLProgram

### webGLProgram: WebGLProgram

**Description:**

The WebGLProgram being wrapped by this class.

This property could change at any time.

Therefore, you should never store a reference to this value.

It should only be passed directly to the WebGL API for drawing.

> Source: [src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L32](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L32)  
> Since: 3.80.0

---

# Public Methods

## createResource

### <instance> createResource()

**Description:**

Creates a WebGLProgram from the given vertex and fragment shaders.

This is called automatically by the constructor. It may also be

called again if the WebGLProgram needs re-creating.

> Source: [src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L76)  
> Since: 3.80.0

---

## destroy

### <instance> destroy()

**Description:**

Remove this WebGLProgram from the GL context.

> Source: [src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L135](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLProgramWrapper.js#L135)  
> Since: 3.80.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [fragmentSource](#fragmentsource)

    - [fragmentSource: string](#fragmentsource-string)
  + [gl](#gl)

    - [gl: WebGLRenderingContext](#gl-webglrenderingcontext)
  + [vertexSource](#vertexsource)

    - [vertexSource: string](#vertexsource-string)
  + [webGLProgram](#webglprogram)

    - [webGLProgram: WebGLProgram](#webglprogram-webglprogram)
* [Public Methods](#public-methods)

  + [createResource](#createresource)

    - [<instance> createResource()](#instance-createresource)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)

Back to top

©2025[Phaser](https://docs.phaser.io)