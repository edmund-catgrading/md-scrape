# WebGLTextureWrapper

Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper

Wrapper for a WebGL texture, containing all the information that was used

to create it.

A WebGLTexture should never be exposed outside the WebGLRenderer,

so the WebGLRenderer can handle context loss and other events

without other systems having to be aware of it.

Always use WebGLTextureWrapper instead.

**Constructor**

`new WebGLTextureWrapper(gl, mipLevel, minFilter, magFilter, wrapT, wrapS, format, pixels, width, height, [pma], [forceSize], [flipY])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gl | WebGLRenderingContext | No |  | WebGL context the texture belongs to. |
| --- | --- | --- | --- | --- |
| mipLevel | number | No |  | Mip level of the texture. |
| minFilter | number | No |  | Filtering of the texture. |
| magFilter | number | No |  | Filtering of the texture. |
| wrapT | number | No |  | Wrapping mode of the texture. |
| wrapS | number | No |  | Wrapping mode of the texture. |
| format | number | No |  | Which format does the texture use. |
| pixels | object | No |  | pixel data. |
| width | number | No |  | Width of the texture in pixels. |
| height | number | No |  | Height of the texture in pixels. |
| pma | boolean | Yes | true | Does the texture have premultiplied alpha? |
| forceSize | boolean | Yes | false | If `true` it will use the width and height passed to this method, regardless of the pixels dimension. |
| flipY | boolean | Yes | false | Sets the `UNPACK_FLIP_Y_WEBGL` flag the WebGL Texture uses during upload. |

---

**Scope**: static

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L10)  
> Since: 3.80.0

# Public Members

## flipY

### flipY: boolean

**Description:**

Sets the `UNPACK_FLIP_Y_WEBGL` flag the WebGL Texture uses during upload.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L177](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L177)  
> Since: 3.80.0

---

## forceSize

### forceSize: boolean

**Description:**

Whether to use the width and height properties, regardless of pixel dimensions.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L168](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L168)  
> Since: 3.80.0

---

## format

### format: number

**Description:**

Which format does the texture use.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L123](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L123)  
> Since: 3.80.0

---

## gl

### gl: WebGLRenderingContext

**Description:**

The WebGL context this WebGLTexture belongs to.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L69)  
> Since: 3.80.0

---

## height

### height: number

**Description:**

Height of the texture in pixels.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L150)  
> Since: 3.80.0

---

## isRenderTexture

### isRenderTexture: boolean

**Description:**

Whether this is used as a RenderTexture.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L59)  
> Since: 3.80.0

---

## magFilter

### magFilter: number

**Description:**

Filtering of the texture.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L96)  
> Since: 3.80.0

---

## minFilter

### minFilter: number

**Description:**

Filtering of the texture.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L87](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L87)  
> Since: 3.80.0

---

## mipLevel

### mipLevel: number

**Description:**

Mip level of the texture.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L78)  
> Since: 3.80.0

---

## pixels

### pixels: object

**Description:**

Pixel data. This is the source data used to create the WebGLTexture.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L132)  
> Since: 3.80.0

---

## pma

### pma: boolean

**Description:**

Does the texture have premultiplied alpha?

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L159)  
> Since: 3.80.0

---

## spectorMetadata

### spectorMetadata: object

**Description:**

The `__SPECTOR_Metadata` property of the `WebGLTexture`,

used to add extra data to the debug SpectorJS integration.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L375](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L375)  
> Since: 3.80.0

---

## webGLTexture

### webGLTexture: WebGLTexture

**Description:**

The WebGLTexture that this wrapper is wrapping.

This property could change at any time.

Therefore, you should never store a reference to this value.

It should only be passed directly to the WebGL API for drawing.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L45)  
> Since: 3.80.0

---

## width

### width: number

**Description:**

Width of the texture in pixels.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L141](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L141)  
> Since: 3.80.0

---

## wrapS

### wrapS: number

**Description:**

Wrapping mode of the texture.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L114)  
> Since: 3.80.0

---

## wrapT

### wrapT: number

**Description:**

Wrapping mode of the texture.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L105](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L105)  
> Since: 3.80.0

---

# Private Members

## \_\_SPECTOR\_Metadata

### \_\_SPECTOR\_Metadata: object

**Description:**

Metadata for the SpectorJS tool, set if debug is enabled.

You should set this via the `spectorMetadata` property,

which will update the `__SPECTOR_Metadata` property on the WebGLTexture.

**Access:** private

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L186)  
> Since: 3.80.0

---

# Public Methods

## \_processTexture

### <instance> \_processTexture()

**Description:**

Set all parameters of this WebGLTexture per the stored values.

**Access:** protected

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L289](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L289)  
> Since: 3.85.0

---

## createResource

### <instance> createResource()

**Description:**

Creates a WebGLTexture from the given parameters.

This is called automatically by the constructor. It may also be

called again if the WebGLTexture needs re-creating.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L202)  
> Since: 3.80.0

---

## destroy

### <instance> destroy()

**Description:**

Deletes the WebGLTexture from the GPU, if it has not been already.

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L403](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L403)  
> Since: 3.80.0

---

## update

### <instance> update(source, width, height, flipY, wrapS, wrapT, minFilter, magFilter, format)

**Description:**

Updates the WebGLTexture from an updated source.

This should only be used when the source is a Canvas or Video element.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | object | No | The source to update the WebGLTexture with. |
| --- | --- | --- | --- |
| width | number | No | The new width of the WebGLTexture. |
| height | number | No | The new height of the WebGLTexture. |
| flipY | boolean | No | Should the WebGLTexture set `UNPACK_MULTIPLY_FLIP_Y`? |
| wrapS | number | No | The new wrapping mode for the WebGLTexture. |
| wrapT | number | No | The new wrapping mode for the WebGLTexture. |
| minFilter | number | No | The new minification filter for the WebGLTexture. |
| magFilter | number | No | The new magnification filter for the WebGLTexture. |
| format | number | No | The new format for the WebGLTexture. |

> Source: [src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L241](https://github.com/phaserjs/phaser/blob/v3.87.0/src/renderer/webgl/wrappers/WebGLTextureWrapper.js#L241)  
> Since: 3.80.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [flipY](#flipy)

    - [flipY: boolean](#flipy-boolean)
  + [forceSize](#forcesize)

    - [forceSize: boolean](#forcesize-boolean)
  + [format](#format)

    - [format: number](#format-number)
  + [gl](#gl)

    - [gl: WebGLRenderingContext](#gl-webglrenderingcontext)
  + [height](#height)

    - [height: number](#height-number)
  + [isRenderTexture](#isrendertexture)

    - [isRenderTexture: boolean](#isrendertexture-boolean)
  + [magFilter](#magfilter)

    - [magFilter: number](#magfilter-number)
  + [minFilter](#minfilter)

    - [minFilter: number](#minfilter-number)
  + [mipLevel](#miplevel)

    - [mipLevel: number](#miplevel-number)
  + [pixels](#pixels)

    - [pixels: object](#pixels-object)
  + [pma](#pma)

    - [pma: boolean](#pma-boolean)
  + [spectorMetadata](#spectormetadata)

    - [spectorMetadata: object](#spectormetadata-object)
  + [webGLTexture](#webgltexture)

    - [webGLTexture: WebGLTexture](#webgltexture-webgltexture)
  + [width](#width)

    - [width: number](#width-number)
  + [wrapS](#wraps)

    - [wrapS: number](#wraps-number)
  + [wrapT](#wrapt)

    - [wrapT: number](#wrapt-number)
* [Private Members](#private-members)

  + [\_\_SPECTOR\_Metadata](#__spector_metadata)

    - [\_\_SPECTOR\_Metadata: object](#__spector_metadata-object)
* [Public Methods](#public-methods)

  + [\_processTexture](#_processtexture)

    - [<instance> \_processTexture()](#instance-_processtexture)
  + [createResource](#createresource)

    - [<instance> createResource()](#instance-createresource)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [update](#update)

    - [<instance> update(source, width, height, flipY, wrapS, wrapT, minFilter, magFilter, format)](#instance-updatesource-width-height-flipy-wraps-wrapt-minfilter-magfilter-format)

Back to top

©2025[Phaser](https://docs.phaser.io)