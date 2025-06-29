# Types.Renderer.WebGL

Phaser.Types.Renderer.WebGL

## RenderTargetConfig

### <static> RenderTargetConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| scale | number | Yes | 1 | A value between 0 and 1. Controls the size of this Render Target in relation to the Renderer. A value of 1 matches it. 0.5 makes the Render Target half the size of the renderer, etc. |
| --- | --- | --- | --- | --- |
| minFilter | number | Yes | 0 | The minFilter mode of the texture. 0 is `LINEAR`, 1 is `NEAREST`. |
| autoClear | boolean | Yes | true | Controls if this Render Target is automatically cleared (via `gl.COLOR_BUFFER_BIT`) during the bind. |
| autoResize | boolean | Yes | false | Controls if this Render Target is automatically resized when the Renderer resizes. |
| width | number | Yes |  | The width of the Render Target. This is optional. If given it overrides the `scale` property. |
| height | number | Yes | "width" | The height of the Render Target. This is optional. If not given, it will be set to the same as the `width` value. |

**Type**: object

**Member of**: Phaser.Types.Renderer.WebGL

> Source: [src/renderer/webgl/typedefs/RenderTargetConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/typedefs/RenderTargetConfig.js#L1)  
> Since: 3.50.0

---

## WebGLConst

### <static> WebGLConst

| name | type | optional | description |
| --- | --- | --- | --- |
| enum | GLenum | No | The data type of the attribute, i.e. `gl.BYTE`, `gl.SHORT`, `gl.UNSIGNED_BYTE`, `gl.FLOAT`, etc. |
| --- | --- | --- | --- |
| size | number | No | The size, in bytes, of the data type. |

**Type**: object

**Member of**: Phaser.Types.Renderer.WebGL

> Source: [src/renderer/webgl/typedefs/WebGLConst.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/typedefs/WebGLConst.js#L1)  
> Since: 3.50.0

---

## WebGLPipelineAttribute

### <static> WebGLPipelineAttribute

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the attribute as defined in the vertex shader. |
| --- | --- | --- | --- |
| size | number | No | The number of components in the attribute, i.e. 1 for a float, 2 for a vec2, 3 for a vec3, etc. |
| type | GLenum | No | The data type of the attribute. Either `gl.BYTE`, `gl.SHORT`, `gl.UNSIGNED_BYTE`, `gl.UNSIGNED_SHORT` or `gl.FLOAT`. |
| offset | number | No | The offset, in bytes, of this attribute data in the vertex array. Equivalent to `offsetof(vertex, attrib)` in C. |
| normalized | boolean | No | Should the attribute data be normalized? |
| enabled | boolean | No | You should set this to `false` by default. The pipeline will enable it on boot. |
| location | number | [Phaser.Renderer.WebGL.Wrappers.WebGLAttribLocationWrapper](../class/renderer-webgl-wrappers-webglattriblocationwrapper.md) | No | You should set this to `-1` by default. The pipeline will set it on boot. |

**Type**: object

**Member of**: Phaser.Types.Renderer.WebGL

> Source: [src/renderer/webgl/typedefs/WebGLPipelineAttribute.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/typedefs/WebGLPipelineAttribute.js#L1)  
> Since: 3.50.0

---

## WebGLPipelineAttributeConfig

### <static> WebGLPipelineAttributeConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| name | string | No |  | The name of the attribute as defined in the vertex shader. |
| --- | --- | --- | --- | --- |
| size | number | No |  | The number of components in the attribute, i.e. 1 for a float, 2 for a vec2, 3 for a vec3, etc. |
| type | [Phaser.Types.Renderer.WebGL.WebGLConst](types-renderer-webgl.md) | No |  | The data type of the attribute, one of the `WEBGL_CONST` values, i.e. `WEBGL_CONST.FLOAT`, `WEBGL_CONST.UNSIGNED_BYTE`, etc. |
| normalized | boolean | Yes | false | Should the attribute data be normalized? |

**Type**: object

**Member of**: Phaser.Types.Renderer.WebGL

> Source: [src/renderer/webgl/typedefs/WebGLPipelineAttributeConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/typedefs/WebGLPipelineAttributeConfig.js#L1)  
> Since: 3.50.0

---

## WebGLPipelineBatchEntry

### <static> WebGLPipelineBatchEntry

| name | type | optional | description |
| --- | --- | --- | --- |
| start | number | No | The vertext count this batch entry starts from. |
| --- | --- | --- | --- |
| count | number | No | The total number of vertices in this batch entry. |
| unit | number | No | The current texture unit of the batch entry. |
| maxUnit | number | No | The maximum number of texture units in this batch entry. |
| texture | Array.<[Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](../class/renderer-webgl-wrappers-webgltexturewrapper.md)> | No | An array of WebGLTextureWrapper references used in this batch entry. |

**Type**: object

**Member of**: Phaser.Types.Renderer.WebGL

> Source: [src/renderer/webgl/typedefs/WebGLPipelineBatchEntry.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/typedefs/WebGLPipelineBatchEntry.js#L1)  
> Since: 3.60.0

---

## WebGLPipelineConfig

### <static> WebGLPipelineConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| game | [Phaser.Game](../class/game.md) | No |  | The Phaser.Game instance that owns this pipeline. |
| --- | --- | --- | --- | --- |
| name | string | Yes |  | The name of the pipeline. |
| topology | GLenum | Yes | "gl.TRIANGLES" | How the primitives are rendered. The default value is GL\_TRIANGLES. Here is the full list of rendering primitives: (<https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/Constants>). |
| vertShader | string | Yes |  | The source code, as a string, for the vertex shader. If you need to assign multiple shaders, see the `shaders` property. |
| fragShader | string | Yes |  | The source code, as a string, for the fragment shader. Can include `%count%` and `%forloop%` declarations for multi-texture support. If you need to assign multiple shaders, see the `shaders` property. |
| batchSize | number | Yes |  | The number of quads to hold in the batch. Defaults to `RenderConfig.batchSize`. This amount \* 6 gives the vertex capacity. |
| vertexSize | number | Yes |  | The size, in bytes, of a single entry in the vertex buffer. Defaults to Float32Array.BYTES\_PER\_ELEMENT \* 6 + Uint8Array.BYTES\_PER\_ELEMENT \* 4. |
| vertices | Array.<number> | Float32Array | Yes |  | An optional Array or Typed Array of pre-calculated vertices data that is copied into the vertex data. |
| attributes | Array.<[Phaser.Types.Renderer.WebGL.WebGLPipelineAttributeConfig](types-renderer-webgl.md)> | Yes |  | An array of shader attribute data. All shaders bound to this pipeline must use the same attributes. |
| shaders | Array.<[Phaser.Types.Renderer.WebGL.WebGLPipelineShaderConfig](types-renderer-webgl.md)> | Yes |  | An array of shaders, all of which are created for this one pipeline. Uses the `vertShader`, `fragShader`, `attributes` and `uniforms` properties of this object as defaults. |
| forceZero | boolean | Yes | false | Force the shader to use just a single sampler2d? Set for anything that extends the Single Pipeline. |
| renderTarget | boolean | number | Array.<[Phaser.Types.Renderer.WebGL.RenderTargetConfig](types-renderer-webgl.md)> | Yes |  |
| resizeUniform | string | Yes | "''" | If the WebGL renderer resizes, this uniform will be set with the new width and height values as part of the pipeline resize call. |

**Type**: object

**Member of**: Phaser.Types.Renderer.WebGL

> Source: [src/renderer/webgl/typedefs/WebGLPipelineConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/typedefs/WebGLPipelineConfig.js#L1)  
> Since: 3.50.0

---

## WebGLPipelineShaderConfig

### <static> WebGLPipelineShaderConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | Yes | The name of the shader. Doesn't have to be unique, but makes shader look-up easier if it is. |
| --- | --- | --- | --- |
| vertShader | string | Yes | The source code, as a string, for the vertex shader. If not given, uses the `Phaser.Types.Renderer.WebGL.WebGLPipelineConfig.vertShader` property instead. |
| fragShader | string | Yes | The source code, as a string, for the fragment shader. Can include `%count%` and `%forloop%` declarations for multi-texture support. If not given, uses the `Phaser.Types.Renderer.WebGL.WebGLPipelineConfig.fragShader` property instead. |
| attributes | Array.<[Phaser.Types.Renderer.WebGL.WebGLPipelineAttributeConfig](types-renderer-webgl.md)> | Yes | An array of shader attribute data. All shaders bound to this pipeline must use the same attributes. |

**Type**: object

**Member of**: Phaser.Types.Renderer.WebGL

> Source: [src/renderer/webgl/typedefs/WebGLPipelineShaderConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/typedefs/WebGLPipelineShaderConfig.js#L1)  
> Since: 3.50.0

---

## WebGLPipelineUniformsConfig

### <static> WebGLPipelineUniformsConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of the uniform as defined in the shader. |
| --- | --- | --- | --- |
| location | number | No | The location of the uniform. |
| setter | function | No | The setter function called on the WebGL context to set the uniform value. |
| value1 | number | Yes | The first cached value of the uniform. |
| value2 | number | Yes | The first cached value of the uniform. |
| value3 | number | Yes | The first cached value of the uniform. |
| value4 | number | Yes | The first cached value of the uniform. |

**Type**: object

**Member of**: Phaser.Types.Renderer.WebGL

> Source: [src/renderer/webgl/typedefs/WebGLPipelineUniformsConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/typedefs/WebGLPipelineUniformsConfig.js#L1)  
> Since: 3.55.1

---

## WebGLTextureCompression

### <static> WebGLTextureCompression

| name | type | optional | description |
| --- | --- | --- | --- |
| ASTC | object | undefined | No | Indicates if ASTC compression is supported (mostly iOS). |
| --- | --- | --- | --- |
| ATC | object | undefined | No | Indicates if ATC compression is supported. |
| BPTC | object | undefined | No | Indicates if BPTC compression is supported. |
| ETC | object | undefined | No | Indicates if ETC compression is supported (mostly Android). |
| ETC1 | object | undefined | No | Indicates if ETC1 compression is supported (mostly Android). |
| IMG | object | undefined | No | Indicates the browser supports true color images (all browsers). |
| PVRTC | object | undefined | No | Indicates if PVRTC compression is supported (mostly iOS). |
| RGTC | object | undefined | No | Indicates if RGTC compression is supported (mostly iOS). |
| S3TC | object | undefined | No | Indicates if S3TC compression is supported on current device (mostly Windows). |
| S3TCSRGB | object | undefined | No | Indicates if S3TCSRGB compression is supported on current device (mostly Windows). |

**Type**: object

**Member of**: Phaser.Types.Renderer.WebGL

> Source: [src/renderer/webgl/typedefs/WebGLTextureCompression.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/typedefs/WebGLTextureCompression.js#L1)  
> Since: 3.55.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Renderer.WebGL](#typesrendererwebgl)

  + [RenderTargetConfig](#rendertargetconfig)

    - [<static> RenderTargetConfig](#static-rendertargetconfig)
  + [WebGLConst](#webglconst)

    - [<static> WebGLConst](#static-webglconst)
  + [WebGLPipelineAttribute](#webglpipelineattribute)

    - [<static> WebGLPipelineAttribute](#static-webglpipelineattribute)
  + [WebGLPipelineAttributeConfig](#webglpipelineattributeconfig)

    - [<static> WebGLPipelineAttributeConfig](#static-webglpipelineattributeconfig)
  + [WebGLPipelineBatchEntry](#webglpipelinebatchentry)

    - [<static> WebGLPipelineBatchEntry](#static-webglpipelinebatchentry)
  + [WebGLPipelineConfig](#webglpipelineconfig)

    - [<static> WebGLPipelineConfig](#static-webglpipelineconfig)
  + [WebGLPipelineShaderConfig](#webglpipelineshaderconfig)

    - [<static> WebGLPipelineShaderConfig](#static-webglpipelineshaderconfig)
  + [WebGLPipelineUniformsConfig](#webglpipelineuniformsconfig)

    - [<static> WebGLPipelineUniformsConfig](#static-webglpipelineuniformsconfig)
  + [WebGLTextureCompression](#webgltexturecompression)

    - [<static> WebGLTextureCompression](#static-webgltexturecompression)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Renderer.WebGL