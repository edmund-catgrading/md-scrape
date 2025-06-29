# Types.Textures

Phaser.Types.Textures

## CompressedTextureData

### <static> CompressedTextureData

An object containing the dimensions and mipmap data for a Compressed Texture.

| name | type | optional | description |
| --- | --- | --- | --- |
| compressed | boolean | No | Is this a compressed texture? |
| --- | --- | --- | --- |
| generateMipmap | boolean | No | Should this texture have mipmaps generated? |
| width | number | No | The width of the maximum size of the texture. |
| height | number | No | The height of the maximum size of the texture. |
| internalFormat | GLenum | No | The WebGL internal texture format. |
| mipmaps | Array.<[Phaser.Types.Textures.MipmapType](types-textures.md)> | No | An array of MipmapType objects. |

**Type**: object

**Member of**: Phaser.Types.Textures

> Source: [src/textures/typedefs/CompressedTextureData.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/typedefs/CompressedTextureData.js#L1)  
> Since: 3.60.0

---

## MipmapType

### <static> MipmapType

A Mipmap Data entry for a Compressed Texture.

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of this level of the mipmap. |
| --- | --- | --- | --- |
| height | number | No | The height of this level of the mipmap. |
| data | Uint8Array | No | The decoded pixel data. |

**Type**: object

**Member of**: Phaser.Types.Textures

> Source: [src/textures/typedefs/MipmapType.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/typedefs/MipmapType.js#L1)  
> Since: 3.60.0

---

## PixelConfig

### <static> PixelConfig

An object containing the position and color data for a single pixel in a CanvasTexture.

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x-coordinate of the pixel. |
| --- | --- | --- | --- |
| y | number | No | The y-coordinate of the pixel. |
| color | number | No | The color of the pixel, not including the alpha channel. |
| alpha | number | No | The alpha of the pixel, between 0 and 1. |

**Type**: object

**Member of**: Phaser.Types.Textures

> Source: [src/textures/typedefs/PixelConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/typedefs/PixelConfig.js#L1)  
> Since: 3.16.0

---

## SpriteSheetConfig

### <static> SpriteSheetConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| frameWidth | number | No |  | The fixed width of each frame. |
| --- | --- | --- | --- | --- |
| frameHeight | number | Yes |  | The fixed height of each frame. If not set it will use the frameWidth as the height. |
| startFrame | number | Yes | 0 | Skip a number of frames. Useful when there are multiple sprite sheets in one Texture. |
| endFrame | number | Yes | -1 | The total number of frames to extract from the Sprite Sheet. The default value of -1 means "extract all frames". |
| margin | number | Yes | 0 | If the frames have been drawn with a margin, specify the amount here. |
| spacing | number | Yes | 0 | If the frames have been drawn with spacing between them, specify the amount here. |

**Type**: object

**Member of**: Phaser.Types.Textures

> Source: [src/textures/typedefs/SpriteSheetConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/typedefs/SpriteSheetConfig.js#L1)  
> Since: 3.0.0

---

## SpriteSheetFromAtlasConfig

### <static> SpriteSheetFromAtlasConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| atlas | string | No |  | The key of the Texture Atlas in which this Sprite Sheet can be found. |
| --- | --- | --- | --- | --- |
| frame | string | No |  | The key of the Texture Atlas Frame in which this Sprite Sheet can be found. |
| frameWidth | number | No |  | The fixed width of each frame. |
| frameHeight | number | Yes |  | The fixed height of each frame. If not set it will use the frameWidth as the height. |
| startFrame | number | Yes | 0 | Skip a number of frames. Useful when there are multiple sprite sheets in one Texture. |
| endFrame | number | Yes | -1 | The total number of frames to extract from the Sprite Sheet. The default value of -1 means "extract all frames". |
| margin | number | Yes | 0 | If the frames have been drawn with a margin, specify the amount here. |
| spacing | number | Yes | 0 | If the frames have been drawn with spacing between them, specify the amount here. |

**Type**: object

**Member of**: Phaser.Types.Textures

> Source: [src/textures/typedefs/SpriteSheetFromAtlasConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/typedefs/SpriteSheetFromAtlasConfig.js#L1)  
> Since: 3.0.0

---

## StampConfig

### <static> StampConfig

An object containing the position and color data for a single pixel in a CanvasTexture.

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| alpha | number | Yes | 1 | The alpha value used by the stamp. |
| --- | --- | --- | --- | --- |
| tint | number | Yes | "0xffffff" | The tint color value used by the stamp. WebGL only. |
| angle | number | Yes | 0 | The angle of the stamp in degrees. Rotation takes place around its origin. |
| rotation | number | Yes | 0 | The rotation of the stamp in radians. Rotation takes place around its origin. |
| scale | number | Yes | 1 | Sets both the horizontal and vertical scale of the stamp with a single value. |
| scaleX | number | Yes | 1 | Set the horizontal scale of the stamp. Overrides the scale property, if provided. |
| scaleY | number | Yes | 1 | Set the vertical scale of the stamp. Overrides the scale property, if provided. |
| originX | number | Yes | 0.5 | The horizontal origin of the stamp. 0 is the left, 0.5 is the center and 1 is the right. |
| originY | number | Yes | 0.5 | The vertical origin of the stamp. 0 is the top, 0.5 is the center and 1 is the bottom. |
| blendMode | string | [Phaser.BlendModes](../namespace/blendmodes.md) | number | Yes | 0 |
| erase | boolean | Yes | false | Erase this stamp from the texture? |
| skipBatch | boolean | Yes | false | Skip beginning and ending a batch with this call. Use if this is part of a bigger batched draw. |

**Type**: object

**Member of**: Phaser.Types.Textures

> Source: [src/textures/typedefs/StampConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/typedefs/StampConfig.js#L1)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Textures](#typestextures)

  + [CompressedTextureData](#compressedtexturedata)

    - [<static> CompressedTextureData](#static-compressedtexturedata)
  + [MipmapType](#mipmaptype)

    - [<static> MipmapType](#static-mipmaptype)
  + [PixelConfig](#pixelconfig)

    - [<static> PixelConfig](#static-pixelconfig)
  + [SpriteSheetConfig](#spritesheetconfig)

    - [<static> SpriteSheetConfig](#static-spritesheetconfig)
  + [SpriteSheetFromAtlasConfig](#spritesheetfromatlasconfig)

    - [<static> SpriteSheetFromAtlasConfig](#static-spritesheetfromatlasconfig)
  + [StampConfig](#stampconfig)

    - [<static> StampConfig](#static-stampconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Textures