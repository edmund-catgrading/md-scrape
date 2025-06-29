# BaseShader

Phaser.Display.BaseShader

A BaseShader is a small resource class that contains the data required for a WebGL Shader to be created.

It contains the raw source code to the fragment and vertex shader, as well as an object that defines

the uniforms the shader requires, if any.

BaseShaders are stored in the Shader Cache, available in a Scene via `this.cache.shaders` and are referenced

by a unique key-based string. Retrieve them via `this.cache.shaders.get(key)`.

BaseShaders are created automatically by the GLSL File Loader when loading an external shader resource.

They can also be created at runtime, allowing you to use dynamically generated shader source code.

Default fragment and vertex source is used if not provided in the constructor, setting-up a basic shader,

suitable for debug rendering.

**Constructor**

`new BaseShader(key, [fragmentSrc], [vertexSrc], [uniforms])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of this shader. Must be unique within the shader cache. |
| --- | --- | --- | --- |
| fragmentSrc | string | Yes | The fragment source for the shader. |
| vertexSrc | string | Yes | The vertex source for the shader. |
| uniforms | any | Yes | Optional object defining the uniforms the shader uses. |

---

**Scope**: static

> Source: [src/display/shader/BaseShader.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/shader/BaseShader.js#L9)  
> Since: 3.17.0

# Public Members

## fragmentSrc

### fragmentSrc: string

**Description:**

The source code, as a string, of the fragment shader being used.

> Source: [src/display/shader/BaseShader.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/shader/BaseShader.js#L90)  
> Since: 3.17.0

---

## key

### key: string

**Description:**

The key of this shader, unique within the shader cache of this Phaser game instance.

> Source: [src/display/shader/BaseShader.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/shader/BaseShader.js#L81)  
> Since: 3.17.0

---

## uniforms

### uniforms: any

**Description:**

The default uniforms for this shader.

> Source: [src/display/shader/BaseShader.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/shader/BaseShader.js#L108)  
> Since: 3.17.0

---

## vertexSrc

### vertexSrc: string

**Description:**

The source code, as a string, of the vertex shader being used.

> Source: [src/display/shader/BaseShader.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/shader/BaseShader.js#L99)  
> Since: 3.17.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [fragmentSrc](#fragmentsrc)

    - [fragmentSrc: string](#fragmentsrc-string)
  + [key](#key)

    - [key: string](#key-string)
  + [uniforms](#uniforms)

    - [uniforms: any](#uniforms-any)
  + [vertexSrc](#vertexsrc)

    - [vertexSrc: string](#vertexsrc-string)

Back to top

©2025[Phaser](https://docs.phaser.io)