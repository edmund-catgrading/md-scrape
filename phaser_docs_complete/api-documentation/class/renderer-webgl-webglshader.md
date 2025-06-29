# WebGLShader

Phaser.Renderer.WebGL.WebGLShader

Instances of the WebGLShader class belong to the WebGL Pipeline classes. When the pipeline is

created it will create an instance of this class for each one of its shaders, as defined in

the pipeline configuration.

This class encapsulates everything needed to manage a shader in a pipeline, including the

shader attributes and uniforms, as well as lots of handy methods such as `set2f`, for setting

uniform values on this shader.

Typically, you do not create an instance of this class directly, as it works in unison with

the pipeline to which it belongs. You can gain access to this class via a pipeline's `shaders`

array, post-creation.

**Constructor**

`new WebGLShader(pipeline, name, vertexShader, fragmentShader, attributes)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| pipeline | [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md) | No | The WebGLPipeline to which this Shader belongs. |
| --- | --- | --- | --- |
| name | string | No | The name of this Shader. |
| vertexShader | string | No | The vertex shader source code as a single string. |
| fragmentShader | string | No | The fragment shader source code as a single string. |
| attributes | Array.<[Phaser.Types.Renderer.WebGL.WebGLPipelineAttributeConfig](../typedef/types-renderer-webgl.md)> | No | An array of attributes. |

---

**Scope**: static

> Source: [src/renderer/webgl/WebGLShader.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L12)  
> Since: 3.50.0

# Public Members

## attributes

### attributes: Array.<[Phaser.Types.Renderer.WebGL.WebGLPipelineAttribute](../typedef/types-renderer-webgl.md)>

**Description:**

Array of objects that describe the vertex attributes.

> Source: [src/renderer/webgl/WebGLShader.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L108)  
> Since: 3.50.0

---

## fragSrc

### fragSrc: string

**Description:**

The fragment shader source code.

> Source: [src/renderer/webgl/WebGLShader.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L81)  
> Since: 3.60.0

---

## gl

### gl: WebGLRenderingContext

**Description:**

A reference to the WebGL Rendering Context the WebGL Renderer is using.

> Source: [src/renderer/webgl/WebGLShader.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L72)  
> Since: 3.50.0

---

## name

### name: string

**Description:**

The name of this shader.

> Source: [src/renderer/webgl/WebGLShader.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L54)  
> Since: 3.50.0

---

## pipeline

### pipeline: [Phaser.Renderer.WebGL.WebGLPipeline](renderer-webgl-webglpipeline.md)

**Description:**

A reference to the WebGLPipeline that owns this Shader.

A Shader class can only belong to a single pipeline.

> Source: [src/renderer/webgl/WebGLShader.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L43)  
> Since: 3.50.0

---

## program

### program: [Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](renderer-webgl-wrappers-webglprogramwrapper.md)

**Description:**

The WebGLProgram created from the vertex and fragment shaders.

> Source: [src/renderer/webgl/WebGLShader.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L99)  
> Since: 3.50.0

---

## renderer

### renderer: [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md)

**Description:**

A reference to the WebGLRenderer instance.

> Source: [src/renderer/webgl/WebGLShader.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L63)  
> Since: 3.50.0

---

## uniforms

### uniforms: [Phaser.Types.Renderer.WebGL.WebGLPipelineUniformsConfig](../typedef/types-renderer-webgl.md)

**Description:**

The active uniforms that this shader has.

This is an object that maps the uniform names to their WebGL location and cached values.

It is populated automatically via the `createUniforms` method.

> Source: [src/renderer/webgl/WebGLShader.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L150)  
> Since: 3.50.0

---

## vertexComponentCount

### vertexComponentCount: number

**Description:**

The amount of vertex attribute components of 32 bit length.

> Source: [src/renderer/webgl/WebGLShader.js#L117](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L117)  
> Since: 3.50.0

---

## vertexSize

### vertexSize: number

**Description:**

The size, in bytes, of a single vertex.

This is derived by adding together all of the vertex attributes.

For example, the Multi Pipeline has the following attributes:

inPosition - (size 2 x gl.FLOAT) = 8

inTexCoord - (size 2 x gl.FLOAT) = 8

inTexId - (size 1 x gl.FLOAT) = 4

inTintEffect - (size 1 x gl.FLOAT) = 4

inTint - (size 4 x gl.UNSIGNED\_BYTE) = 4

The total, in this case, is 8 + 8 + 4 + 4 + 4 = 28.

This is calculated automatically during the `createAttributes` method.

> Source: [src/renderer/webgl/WebGLShader.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L126)  
> Since: 3.50.0

---

## vertSrc

### vertSrc: string

**Description:**

The vertex shader source code.

> Source: [src/renderer/webgl/WebGLShader.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L90)  
> Since: 3.60.0

---

# Public Methods

## bind

### <instance> bind([setAttributes], [flush])

**Description:**

Sets the program this shader uses as being the active shader in the WebGL Renderer.

This method is called every time the parent pipeline is made the current active pipeline.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| setAttributes | boolean | Yes | false | Should the vertex attribute pointers be set? |
| --- | --- | --- | --- | --- |
| flush | boolean | Yes | false | Flush the pipeline before binding this shader? |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L229](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L229)  
> Since: 3.50.0

---

## createAttributes

### <instance> createAttributes(attributes)

**Description:**

Takes the vertex attributes config and parses it, creating the resulting array that is stored

in this shaders `attributes` property, calculating the offset, normalization and location

in the process.

Calling this method resets `WebGLShader.attributes`, `WebGLShader.vertexSize` and

`WebGLShader.vertexComponentCount`.

It is called automatically when this class is created, but can be called manually if required.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| attributes | Array.<[Phaser.Types.Renderer.WebGL.WebGLPipelineAttributeConfig](../typedef/types-renderer-webgl.md)> | No | An array of attributes configs. |
| --- | --- | --- | --- |

> Source: [src/renderer/webgl/WebGLShader.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L167)  
> Since: 3.50.0

---

## createProgram

### <instance> createProgram([vertSrc], [fragSrc])

**Description:**

This method will create the Shader Program on the current GL context.

If a program already exists, it will be destroyed and the new one will take its place.

After the program is created the uniforms will be reset and

this shader will be rebound.

This is a very expensive process and if your shader is referenced elsewhere in

your game those references may then be lost, so be sure to use this carefully.

However, if you need to update say the fragment shader source, then you can pass

the new source into this method and it'll rebuild the program using it. If you

don't want to change the vertex shader src, pass `undefined` as the parameter.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| vertSrc | string | Yes | The source code of the vertex shader. If not given, uses the source already defined in this Shader. |
| --- | --- | --- | --- |
| fragSrc | string | Yes | The source code of the fragment shader. If not given, uses the source already defined in this Shader. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L1172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L1172)  
> Since: 3.60.0

---

## createUniforms

### <instance> createUniforms()

**Description:**

Sets up the `WebGLShader.uniforms` object, populating it with the names

and locations of the shader uniforms this shader requires.

It works by first calling `gl.getProgramParameter(program.webGLProgram, gl.ACTIVE_UNIFORMS)` to

find out how many active uniforms this shader has. It then iterates through them,

calling `gl.getActiveUniform` to get the WebGL Active Info from each one. Finally,

the name and location are stored in the local array.

This method is called automatically when this class is created.

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L353](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L353)  
> Since: 3.50.0

---

## destroy

### <instance> destroy()

**Description:**

Removes all external references from this class and deletes the WebGL program from the WebGL context.

Does not remove this shader from the parent pipeline.

> Source: [src/renderer/webgl/WebGLShader.js#L1215](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L1215)  
> Since: 3.50.0

---

## hasUniform

### <instance> hasUniform(name)

**Description:**

Checks to see if the given uniform name exists and is active in this shader.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to check for. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the uniform exists, otherwise `false`.

> Source: [src/renderer/webgl/WebGLShader.js#L469](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L469)  
> Since: 3.50.0

---

## rebind

### <instance> rebind()

**Description:**

Sets the program this shader uses as being the active shader in the WebGL Renderer.

Then resets all of the attribute pointers.

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L262)  
> Since: 3.50.0

---

## resetUniform

### <instance> resetUniform(name)

**Description:**

Resets the cached values of the given uniform.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to reset. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L484](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L484)  
> Since: 3.50.0

---

## set1f

### <instance> set1f(name, x)

**Description:**

Sets a 1f uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new value of the `float` uniform. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L739](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L739)  
> Since: 3.50.0

---

## set1fv

### <instance> set1fv(name, arr)

**Description:**

Sets a 1fv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L833](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L833)  
> Since: 3.50.0

---

## set1i

### <instance> set1i(name, x)

**Description:**

Sets a 1i uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new value of the `int` uniform. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L1009](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L1009)  
> Since: 3.50.0

---

## set1iv

### <instance> set1iv(name, arr)

**Description:**

Sets a 1iv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L921](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L921)  
> Since: 3.50.0

---

## set2f

### <instance> set2f(name, x, y)

**Description:**

Sets a 2f uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new X component of the `vec2` uniform. |
| y | number | No | The new Y component of the `vec2` uniform. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L761](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L761)  
> Since: 3.50.0

---

## set2fv

### <instance> set2fv(name, arr)

**Description:**

Sets a 2fv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L855](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L855)  
> Since: 3.50.0

---

## set2i

### <instance> set2i(name, x, y)

**Description:**

Sets a 2i uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new X component of the `ivec2` uniform. |
| y | number | No | The new Y component of the `ivec2` uniform. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L1031](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L1031)  
> Since: 3.50.0

---

## set2iv

### <instance> set2iv(name, arr)

**Description:**

Sets a 2iv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L943](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L943)  
> Since: 3.50.0

---

## set3f

### <instance> set3f(name, x, y, z)

**Description:**

Sets a 3f uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new X component of the `vec3` uniform. |
| y | number | No | The new Y component of the `vec3` uniform. |
| z | number | No | The new Z component of the `vec3` uniform. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L784](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L784)  
> Since: 3.50.0

---

## set3fv

### <instance> set3fv(name, arr)

**Description:**

Sets a 3fv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L877](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L877)  
> Since: 3.50.0

---

## set3i

### <instance> set3i(name, x, y, z)

**Description:**

Sets a 3i uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | The new X component of the `ivec3` uniform. |
| y | number | No | The new Y component of the `ivec3` uniform. |
| z | number | No | The new Z component of the `ivec3` uniform. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L1054](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L1054)  
> Since: 3.50.0

---

## set3iv

### <instance> set3iv(name, arr)

**Description:**

Sets a 3iv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L965](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L965)  
> Since: 3.50.0

---

## set4f

### <instance> set4f(name, x, y, z, w)

**Description:**

Sets a 4f uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | X component of the uniform |
| y | number | No | Y component of the uniform |
| z | number | No | Z component of the uniform |
| w | number | No | W component of the uniform |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L808](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L808)  
> Since: 3.50.0

---

## set4fv

### <instance> set4fv(name, arr)

**Description:**

Sets a 4fv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L899](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L899)  
> Since: 3.50.0

---

## set4i

### <instance> set4i(name, x, y, z, w)

**Description:**

Sets a 4i uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| x | number | No | X component of the uniform |
| y | number | No | Y component of the uniform |
| z | number | No | Z component of the uniform |
| w | number | No | W component of the uniform |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L1078](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L1078)  
> Since: 3.50.0

---

## set4iv

### <instance> set4iv(name, arr)

**Description:**

Sets a 4iv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| arr | Array.<number> | Float32Array | No | The new value to be used for the uniform variable. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L987](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L987)  
> Since: 3.50.0

---

## setAttribPointers

### <instance> setAttribPointers([reset])

**Description:**

Sets the vertex attribute pointers.

This should only be called after the vertex buffer has been bound.

It is called automatically during the `bind` method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| reset | boolean | Yes | false | Reset the vertex attribute locations? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L281](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L281)  
> Since: 3.50.0

---

## setBoolean

### <instance> setBoolean(name, value)

**Description:**

Sets a boolean uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| value | boolean | No | The new value of the `boolean` uniform. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L717](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L717)  
> Since: 3.60.0

---

## setMatrix2fv

### <instance> setMatrix2fv(name, transpose, matrix)

**Description:**

Sets a matrix 2fv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| transpose | boolean | No | Whether to transpose the matrix. Should be `false`. |
| matrix | Array.<number> | Float32Array | No | The new values for the `mat2` uniform. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L1103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L1103)  
> Since: 3.50.0

---

## setMatrix3fv

### <instance> setMatrix3fv(name, transpose, matrix)

**Description:**

Sets a matrix 3fv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| transpose | boolean | No | Whether to transpose the matrix. Should be `false`. |
| matrix | Float32Array | No | The new values for the `mat3` uniform. |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L1126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L1126)  
> Since: 3.50.0

---

## setMatrix4fv

### <instance> setMatrix4fv(name, transpose, matrix)

**Description:**

Sets a matrix 4fv uniform value based on the given name on this shader.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform to set. |
| --- | --- | --- | --- |
| transpose | boolean | No | Should the matrix be transpose |
| matrix | Float32Array | No | Matrix data |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L1149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L1149)  
> Since: 3.50.0

---

## setUniform1

### <instance> setUniform1(setter, name, value1, [skipCheck])

**Description:**

Sets the given uniform value/s based on the name and GL function.

This method is called internally by other methods such as `set1f` and `set3iv`.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| setter | function | No |  | The GL function to call. |
| --- | --- | --- | --- | --- |
| name | string | No |  | The name of the uniform to set. |
| value1 | boolean | number | Array.<number> | Float32Array | No |
| skipCheck | boolean | Yes | false | Skip the value comparison? |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L509](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L509)  
> Since: 3.50.0

---

## setUniform2

### <instance> setUniform2(setter, name, value1, value2, [skipCheck])

**Description:**

Sets the given uniform value/s based on the name and GL function.

This method is called internally by other methods such as `set1f` and `set3iv`.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| setter | function | No |  | The GL function to call. |
| --- | --- | --- | --- | --- |
| name | string | No |  | The name of the uniform to set. |
| value1 | boolean | number | Array.<number> | Float32Array | No |
| value2 | boolean | number | Array.<number> | Float32Array | No |
| skipCheck | boolean | Yes | false | Skip the value comparison? |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L558](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L558)  
> Since: 3.50.0

---

## setUniform3

### <instance> setUniform3(setter, name, value1, value2, value3, [skipCheck])

**Description:**

Sets the given uniform value/s based on the name and GL function.

This method is called internally by other methods such as `set1f` and `set3iv`.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| setter | function | No |  | The GL function to call. |
| --- | --- | --- | --- | --- |
| name | string | No |  | The name of the uniform to set. |
| value1 | boolean | number | Array.<number> | Float32Array | No |
| value2 | boolean | number | Array.<number> | Float32Array | No |
| value3 | boolean | number | Array.<number> | Float32Array | No |
| skipCheck | boolean | Yes | false | Skip the value comparison? |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L609](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L609)  
> Since: 3.50.0

---

## setUniform4

### <instance> setUniform4(setter, name, value1, value2, value3, value4, [skipCheck])

**Description:**

Sets the given uniform value/s based on the name and GL function.

This method is called internally by other methods such as `set1f` and `set3iv`.

The uniform is only set if the value/s given are different to those previously set.

This method works by first setting this shader as being the current shader within the

WebGL Renderer, if it isn't already. It also sets this shader as being the current

one within the pipeline it belongs to.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| setter | function | No |  | The GL function to call. |
| --- | --- | --- | --- | --- |
| name | string | No |  | The name of the uniform to set. |
| value1 | boolean | number | Array.<number> | Float32Array | No |
| value2 | boolean | number | Array.<number> | Float32Array | No |
| value3 | boolean | number | Array.<number> | Float32Array | No |
| value4 | boolean | number | Array.<number> | Float32Array | No |
| skipCheck | boolean | Yes | false | Skip the value comparison? |

**Returns:** [Phaser.Renderer.WebGL.WebGLShader](renderer-webgl-webglshader.md) - This WebGLShader instance.

> Source: [src/renderer/webgl/WebGLShader.js#L662](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L662)  
> Since: 3.50.0

---

## syncUniforms

### <instance> syncUniforms()

**Description:**

Repopulate uniforms on the GPU.

This is called automatically by the pipeline when the context is

lost and then recovered. By the time this method is called,

the WebGL resources are already recreated, so we just need to

re-populate them.

> Source: [src/renderer/webgl/WebGLShader.js#L442](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/WebGLShader.js#L442)  
> Since: 3.80.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [attributes](#attributes)

    - [attributes: Array.<Phaser.Types.Renderer.WebGL.WebGLPipelineAttribute>](#attributes-arrayphasertypesrendererwebglwebglpipelineattribute)
  + [fragSrc](#fragsrc)

    - [fragSrc: string](#fragsrc-string)
  + [gl](#gl)

    - [gl: WebGLRenderingContext](#gl-webglrenderingcontext)
  + [name](#name)

    - [name: string](#name-string)
  + [pipeline](#pipeline)

    - [pipeline: Phaser.Renderer.WebGL.WebGLPipeline](#pipeline-phaserrendererwebglwebglpipeline)
  + [program](#program)

    - [program: Phaser.Renderer.WebGL.Wrappers.WebGLProgramWrapper](#program-phaserrendererwebglwrapperswebglprogramwrapper)
  + [renderer](#renderer)

    - [renderer: Phaser.Renderer.WebGL.WebGLRenderer](#renderer-phaserrendererwebglwebglrenderer)
  + [uniforms](#uniforms)

    - [uniforms: Phaser.Types.Renderer.WebGL.WebGLPipelineUniformsConfig](#uniforms-phasertypesrendererwebglwebglpipelineuniformsconfig)
  + [vertexComponentCount](#vertexcomponentcount)

    - [vertexComponentCount: number](#vertexcomponentcount-number)
  + [vertexSize](#vertexsize)

    - [vertexSize: number](#vertexsize-number)
  + [vertSrc](#vertsrc)

    - [vertSrc: string](#vertsrc-string)
* [Public Methods](#public-methods)

  + [bind](#bind)

    - [<instance> bind([setAttributes], [flush])](#instance-bindsetattributes-flush)
  + [createAttributes](#createattributes)

    - [<instance> createAttributes(attributes)](#instance-createattributesattributes)
  + [createProgram](#createprogram)

    - [<instance> createProgram([vertSrc], [fragSrc])](#instance-createprogramvertsrc-fragsrc)
  + [createUniforms](#createuniforms)

    - [<instance> createUniforms()](#instance-createuniforms)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [hasUniform](#hasuniform)

    - [<instance> hasUniform(name)](#instance-hasuniformname)
  + [rebind](#rebind)

    - [<instance> rebind()](#instance-rebind)
  + [resetUniform](#resetuniform)

    - [<instance> resetUniform(name)](#instance-resetuniformname)
  + [set1f](#set1f)

    - [<instance> set1f(name, x)](#instance-set1fname-x)
  + [set1fv](#set1fv)

    - [<instance> set1fv(name, arr)](#instance-set1fvname-arr)
  + [set1i](#set1i)

    - [<instance> set1i(name, x)](#instance-set1iname-x)
  + [set1iv](#set1iv)

    - [<instance> set1iv(name, arr)](#instance-set1ivname-arr)
  + [set2f](#set2f)

    - [<instance> set2f(name, x, y)](#instance-set2fname-x-y)
  + [set2fv](#set2fv)

    - [<instance> set2fv(name, arr)](#instance-set2fvname-arr)
  + [set2i](#set2i)

    - [<instance> set2i(name, x, y)](#instance-set2iname-x-y)
  + [set2iv](#set2iv)

    - [<instance> set2iv(name, arr)](#instance-set2ivname-arr)
  + [set3f](#set3f)

    - [<instance> set3f(name, x, y, z)](#instance-set3fname-x-y-z)
  + [set3fv](#set3fv)

    - [<instance> set3fv(name, arr)](#instance-set3fvname-arr)
  + [set3i](#set3i)

    - [<instance> set3i(name, x, y, z)](#instance-set3iname-x-y-z)
  + [set3iv](#set3iv)

    - [<instance> set3iv(name, arr)](#instance-set3ivname-arr)
  + [set4f](#set4f)

    - [<instance> set4f(name, x, y, z, w)](#instance-set4fname-x-y-z-w)
  + [set4fv](#set4fv)

    - [<instance> set4fv(name, arr)](#instance-set4fvname-arr)
  + [set4i](#set4i)

    - [<instance> set4i(name, x, y, z, w)](#instance-set4iname-x-y-z-w)
  + [set4iv](#set4iv)

    - [<instance> set4iv(name, arr)](#instance-set4ivname-arr)
  + [setAttribPointers](#setattribpointers)

    - [<instance> setAttribPointers([reset])](#instance-setattribpointersreset)
  + [setBoolean](#setboolean)

    - [<instance> setBoolean(name, value)](#instance-setbooleanname-value)
  + [setMatrix2fv](#setmatrix2fv)

    - [<instance> setMatrix2fv(name, transpose, matrix)](#instance-setmatrix2fvname-transpose-matrix)
  + [setMatrix3fv](#setmatrix3fv)

    - [<instance> setMatrix3fv(name, transpose, matrix)](#instance-setmatrix3fvname-transpose-matrix)
  + [setMatrix4fv](#setmatrix4fv)

    - [<instance> setMatrix4fv(name, transpose, matrix)](#instance-setmatrix4fvname-transpose-matrix)
  + [setUniform1](#setuniform1)

    - [<instance> setUniform1(setter, name, value1, [skipCheck])](#instance-setuniform1setter-name-value1-skipcheck)
  + [setUniform2](#setuniform2)

    - [<instance> setUniform2(setter, name, value1, value2, [skipCheck])](#instance-setuniform2setter-name-value1-value2-skipcheck)
  + [setUniform3](#setuniform3)

    - [<instance> setUniform3(setter, name, value1, value2, value3, [skipCheck])](#instance-setuniform3setter-name-value1-value2-value3-skipcheck)
  + [setUniform4](#setuniform4)

    - [<instance> setUniform4(setter, name, value1, value2, value3, value4, [skipCheck])](#instance-setuniform4setter-name-value1-value2-value3-value4-skipcheck)
  + [syncUniforms](#syncuniforms)

    - [<instance> syncUniforms()](#instance-syncuniforms)

Back to top

©2025[Phaser](https://docs.phaser.io)