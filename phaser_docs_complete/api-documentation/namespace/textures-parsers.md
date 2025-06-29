# Phaser.Textures.Parsers

Scope:
static

> Source: [src/textures/parsers/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/index.js#L7)

# Static functions

## KTXParser

### <static> KTXParser(data)

**Description:**

Parses a KTX format Compressed Texture file and generates texture data suitable for WebGL from it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | ArrayBuffer | No | The data object created by the Compressed Texture File Loader. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Textures.CompressedTextureData](../typedef/types-textures.md) - The Compressed Texture data.

> Source: [src/textures/parsers/KTXParser.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/KTXParser.js#L7)  
> Since: 3.60.0

---

## PVRParser

### <static> PVRParser(data)

**Description:**

Parses a PVR format Compressed Texture file and generates texture data suitable for WebGL from it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | ArrayBuffer | No | The data object created by the Compressed Texture File Loader. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Textures.CompressedTextureData](../typedef/types-textures.md) - The Compressed Texture data.

> Source: [src/textures/parsers/PVRParser.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/PVRParser.js#L236)  
> Since: 3.60.0

---

## verifyCompressedTexture

### <static> verifyCompressedTexture(data)

**Description:**

Verify whether the given compressed texture data is valid.

Compare the dimensions of each mip layer to the rules for that

specific format.

Mip layer size is assumed to have been calculated correctly during parsing.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | [Phaser.Types.Textures.CompressedTextureData](../typedef/types-textures.md) | No | The compressed texture data to verify. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the compressed texture data is valid.

> Source: [src/textures/parsers/VerifyCompressedTexture.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/VerifyCompressedTexture.js#L9)  
> Since: 3.80.0

---

## AtlasXML

### <static> AtlasXML(texture, sourceIndex, xml)

**Description:**

Parses an XML Texture Atlas object and adds all the Frames into a Texture.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No | The Texture to add the Frames to. |
| --- | --- | --- | --- |
| sourceIndex | number | No | The index of the TextureSource. |
| xml | \* | No | The XML data. |

**Returns:** [Phaser.Textures.Texture](../class/textures-texture.md) - The Texture modified by this parser.

> Source: [src/textures/parsers/AtlasXML.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/AtlasXML.js#L7)  
> Since: 3.7.0

---

## Canvas

### <static> Canvas(texture, sourceIndex)

**Description:**

Adds a Canvas Element to a Texture.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No | The Texture to add the Frames to. |
| --- | --- | --- | --- |
| sourceIndex | number | No | The index of the TextureSource. |

**Returns:** [Phaser.Textures.Texture](../class/textures-texture.md) - The Texture modified by this parser.

> Source: [src/textures/parsers/Canvas.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/Canvas.js#L7)  
> Since: 3.0.0

---

## Image

### <static> Image(texture, sourceIndex)

**Description:**

Adds an Image Element to a Texture.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No | The Texture to add the Frames to. |
| --- | --- | --- | --- |
| sourceIndex | number | No | The index of the TextureSource. |

**Returns:** [Phaser.Textures.Texture](../class/textures-texture.md) - The Texture modified by this parser.

> Source: [src/textures/parsers/Image.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/Image.js#L7)  
> Since: 3.0.0

---

## JSONArray

### <static> JSONArray(texture, sourceIndex, json)

**Description:**

Parses a Texture Atlas JSON Array and adds the Frames to the Texture.

JSON format expected to match that defined by Texture Packer, with the frames property containing an array of Frames.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No | The Texture to add the Frames to. |
| --- | --- | --- | --- |
| sourceIndex | number | No | The index of the TextureSource. |
| json | object | No | The JSON data. |

**Returns:** [Phaser.Textures.Texture](../class/textures-texture.md) - The Texture modified by this parser.

> Source: [src/textures/parsers/JSONArray.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/JSONArray.js#L9)  
> Since: 3.0.0

---

## JSONHash

### <static> JSONHash(texture, sourceIndex, json)

**Description:**

Parses a Texture Atlas JSON Hash and adds the Frames to the Texture.

JSON format expected to match that defined by Texture Packer, with the frames property containing an object of Frames.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No | The Texture to add the Frames to. |
| --- | --- | --- | --- |
| sourceIndex | number | No | The index of the TextureSource. |
| json | object | No | The JSON data. |

**Returns:** [Phaser.Textures.Texture](../class/textures-texture.md) - The Texture modified by this parser.

> Source: [src/textures/parsers/JSONHash.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/JSONHash.js#L9)  
> Since: 3.0.0

---

## SpriteSheet

### <static> SpriteSheet(texture, sourceIndex, x, y, width, height, config, config.frameWidth, [config.frameHeight], [config.startFrame], [config.endFrame], [config.margin], [config.spacing])

**Description:**

Parses a Sprite Sheet and adds the Frames to the Texture.

In Phaser terminology a Sprite Sheet is a texture containing different frames, but each frame is the exact

same size and cannot be trimmed or rotated.

**Access:** private

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No |  | The Texture to add the Frames to. |
| --- | --- | --- | --- | --- |
| sourceIndex | number | No |  | The index of the TextureSource. |
| x | number | No |  | The top-left coordinate of the Sprite Sheet. Defaults to zero. Used when extracting sheets from atlases. |
| y | number | No |  | The top-left coordinate of the Sprite Sheet. Defaults to zero. Used when extracting sheets from atlases. |
| width | number | No |  | The width of the source image. |
| height | number | No |  | The height of the source image. |
| config | object | No |  | An object describing how to parse the Sprite Sheet. |
| config.frameWidth | number | No |  | Width in pixels of a single frame in the sprite sheet. |
| config.frameHeight | number | Yes |  | Height in pixels of a single frame in the sprite sheet. Defaults to frameWidth if not provided. |
| config.startFrame | number | Yes | 0 | The frame to start extracting from. Defaults to zero. |
| config.endFrame | number | Yes | -1 | The frame to finish extracting at. Defaults to -1, which means 'all frames'. |
| config.margin | number | Yes | 0 | If the frames have been drawn with a margin, specify the amount here. |
| config.spacing | number | Yes | 0 | If the frames have been drawn with spacing between them, specify the amount here. |

**Returns:** [Phaser.Textures.Texture](../class/textures-texture.md) - The Texture modified by this parser.

> Source: [src/textures/parsers/SpriteSheet.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/SpriteSheet.js#L9)  
> Since: 3.0.0

---

## SpriteSheetFromAtlas

### <static> SpriteSheetFromAtlas(texture, frame, config, config.frameWidth, [config.frameHeight], [config.startFrame], [config.endFrame], [config.margin], [config.spacing])

**Description:**

Parses a Sprite Sheet and adds the Frames to the Texture, where the Sprite Sheet is stored as a frame within an Atlas.

In Phaser terminology a Sprite Sheet is a texture containing different frames, but each frame is the exact

same size and cannot be trimmed or rotated.

**Access:** private

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No |  | The Texture to add the Frames to. |
| --- | --- | --- | --- | --- |
| frame | [Phaser.Textures.Frame](../class/textures-frame.md) | No |  | The Frame that contains the Sprite Sheet. |
| config | object | No |  | An object describing how to parse the Sprite Sheet. |
| config.frameWidth | number | No |  | Width in pixels of a single frame in the sprite sheet. |
| config.frameHeight | number | Yes |  | Height in pixels of a single frame in the sprite sheet. Defaults to frameWidth if not provided. |
| config.startFrame | number | Yes | 0 | Index of the start frame in the sprite sheet |
| config.endFrame | number | Yes | -1 | Index of the end frame in the sprite sheet. -1 mean all the rest of the frames |
| config.margin | number | Yes | 0 | If the frames have been drawn with a margin, specify the amount here. |
| config.spacing | number | Yes | 0 | If the frames have been drawn with spacing between them, specify the amount here. |

**Returns:** [Phaser.Textures.Texture](../class/textures-texture.md) - The Texture modified by this parser.

> Source: [src/textures/parsers/SpriteSheetFromAtlas.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/SpriteSheetFromAtlas.js#L9)  
> Since: 3.0.0

---

## UnityYAML

### <static> UnityYAML(texture, sourceIndex, yaml)

**Description:**

Parses a Unity YAML File and creates Frames in the Texture.

For more details about Sprite Meta Data see <https://docs.unity3d.com/ScriptReference/SpriteMetaData.html>

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| texture | [Phaser.Textures.Texture](../class/textures-texture.md) | No | The Texture to add the Frames to. |
| --- | --- | --- | --- |
| sourceIndex | number | No | The index of the TextureSource. |
| yaml | object | No | The YAML data. |

**Returns:** [Phaser.Textures.Texture](../class/textures-texture.md) - The Texture modified by this parser.

> Source: [src/textures/parsers/UnityYAML.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/parsers/UnityYAML.js#L38)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [KTXParser](#ktxparser)

    - [<static> KTXParser(data)](#static-ktxparserdata)
  + [PVRParser](#pvrparser)

    - [<static> PVRParser(data)](#static-pvrparserdata)
  + [verifyCompressedTexture](#verifycompressedtexture)

    - [<static> verifyCompressedTexture(data)](#static-verifycompressedtexturedata)
  + [AtlasXML](#atlasxml)

    - [<static> AtlasXML(texture, sourceIndex, xml)](#static-atlasxmltexture-sourceindex-xml)
  + [Canvas](#canvas)

    - [<static> Canvas(texture, sourceIndex)](#static-canvastexture-sourceindex)
  + [Image](#image)

    - [<static> Image(texture, sourceIndex)](#static-imagetexture-sourceindex)
  + [JSONArray](#jsonarray)

    - [<static> JSONArray(texture, sourceIndex, json)](#static-jsonarraytexture-sourceindex-json)
  + [JSONHash](#jsonhash)

    - [<static> JSONHash(texture, sourceIndex, json)](#static-jsonhashtexture-sourceindex-json)
  + [SpriteSheet](#spritesheet)

    - [<static> SpriteSheet(texture, sourceIndex, x, y, width, height, config, config.frameWidth, [config.frameHeight], [config.startFrame], [config.endFrame], [config.margin], [config.spacing])](#static-spritesheettexture-sourceindex-x-y-width-height-config-configframewidth-configframeheight-configstartframe-configendframe-configmargin-configspacing)
  + [SpriteSheetFromAtlas](#spritesheetfromatlas)

    - [<static> SpriteSheetFromAtlas(texture, frame, config, config.frameWidth, [config.frameHeight], [config.startFrame], [config.endFrame], [config.margin], [config.spacing])](#static-spritesheetfromatlastexture-frame-config-configframewidth-configframeheight-configstartframe-configendframe-configmargin-configspacing)
  + [UnityYAML](#unityyaml)

    - [<static> UnityYAML(texture, sourceIndex, yaml)](#static-unityyamltexture-sourceindex-yaml)

Back to top

©2025[Phaser](https://docs.phaser.io)