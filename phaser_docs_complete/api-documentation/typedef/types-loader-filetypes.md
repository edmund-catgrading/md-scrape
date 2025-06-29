# Types.Loader.FileTypes

Phaser.Types.Loader.FileTypes

## AsepriteFileConfig

### <static> AsepriteFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Texture Manager. |
| --- | --- | --- | --- | --- |
| textureURL | string | Yes |  | The absolute or relative URL to load the texture image file from. |
| textureExtension | string | Yes | "'png'" | The default file extension to use for the image texture if no url is provided. |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the texture image file. |
| atlasURL | object | string | Yes |  | The absolute or relative URL to load the atlas json file from. Or, a well formed JSON object to use instead. |
| atlasExtension | string | Yes | "'json'" | The default file extension to use for the atlas json if no url is provided. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the atlas json file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/AsepriteFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/AsepriteFileConfig.js#L1)

---

## AtlasJSONFileConfig

### <static> AtlasJSONFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Texture Manager. |
| --- | --- | --- | --- | --- |
| textureURL | string | Yes |  | The absolute or relative URL to load the texture image file from. |
| textureExtension | string | Yes | "'png'" | The default file extension to use for the image texture if no url is provided. |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the texture image file. |
| normalMap | string | Yes |  | The filename of an associated normal map. It uses the same path and url to load as the texture image. |
| atlasURL | object | string | Yes |  | The absolute or relative URL to load the atlas json file from. Or, a well formed JSON object to use instead. |
| atlasExtension | string | Yes | "'json'" | The default file extension to use for the atlas json if no url is provided. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the atlas json file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/AtlasJSONFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/AtlasJSONFileConfig.js#L1)

---

## AtlasXMLFileConfig

### <static> AtlasXMLFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Texture Manager. |
| --- | --- | --- | --- | --- |
| textureURL | string | Yes |  | The absolute or relative URL to load the texture image file from. |
| textureExtension | string | Yes | "'png'" | The default file extension to use for the image texture if no url is provided. |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the texture image file. |
| normalMap | string | Yes |  | The filename of an associated normal map. It uses the same path and url to load as the texture image. |
| atlasURL | string | Yes |  | The absolute or relative URL to load the atlas xml file from. |
| atlasExtension | string | Yes | "'xml'" | The default file extension to use for the atlas xml if no url is provided. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the atlas xml file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/AtlasXMLFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/AtlasXMLFileConfig.js#L1)

---

## AudioFileConfig

### <static> AudioFileConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the file. Must be unique within the Loader and Audio Cache. |
| --- | --- | --- | --- |
| url | string | Array.<string> | [Phaser.Types.Loader.FileTypes.AudioFileURLConfig](types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.AudioFileURLConfig](types-loader-filetypes.md)> |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes | Extra XHR Settings specifically for this file. |
| context | AudioContext | Yes | The optional AudioContext this file will use to process itself. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/AudioFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/AudioFileConfig.js#L1)

---

## AudioFileURLConfig

### <static> AudioFileURLConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| type | string | No | The audio file format. See property names in {@link Phaser.Device.Audio}. |
| --- | --- | --- | --- |
| url | string | No | The absolute or relative URL of the audio file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/AudioFileURLConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/AudioFileURLConfig.js#L1)

---

## AudioSpriteFileConfig

### <static> AudioSpriteFileConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the file. Must be unique within both the Loader and the Audio Cache. |
| --- | --- | --- | --- |
| jsonURL | string | No | The absolute or relative URL to load the json file from. Or a well formed JSON object to use instead. |
| jsonXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes | Extra XHR Settings specifically for the json file. |
| audioURL | Object | Yes | The absolute or relative URL to load the audio file from. |
| audioConfig | any | Yes | The audio configuration options. |
| audioXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes | Extra XHR Settings specifically for the audio file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/AudioSpriteFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/AudioSpriteFileConfig.js#L1)

---

## BinaryFileConfig

### <static> BinaryFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Binary Cache. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'bin'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |
| dataType | any | Yes |  | Optional type to cast the binary file to once loaded. For example, `Uint8Array`. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/BinaryFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/BinaryFileConfig.js#L1)

---

## BitmapFontFileConfig

### <static> BitmapFontFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Texture Manager. |
| --- | --- | --- | --- | --- |
| textureURL | string | Yes |  | The absolute or relative URL to load the texture image file from. |
| textureExtension | string | Yes | "'png'" | The default file extension to use for the image texture if no url is provided. |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the texture image file. |
| normalMap | string | Yes |  | The filename of an associated normal map. It uses the same path and url to load as the texture image. |
| fontDataURL | string | Yes |  | The absolute or relative URL to load the font data xml file from. |
| fontDataExtension | string | Yes | "'xml'" | The default file extension to use for the font data xml if no url is provided. |
| fontDataXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the font data xml file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/BitmapFontFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/BitmapFontFileConfig.js#L1)

---

## CompressedTextureFileEntry

### <static> CompressedTextureFileEntry

| name | type | optional | description |
| --- | --- | --- | --- |
| format | string | Yes | The texture compression base format that the browser must support in order to load this file. Can be any of: 'ETC', 'ETC1', 'ATC', 'ASTC', 'BPTC', 'RGTC', 'PVRTC', 'S3TC', 'S3TCSRGB' or the fallback format of 'IMG'. |
| --- | --- | --- | --- |
| type | string | Yes | The container format, either PVR or KTX. If not given it will try to extract it from the textureURL extension. |
| textureURL | string | Yes | The URL of the compressed texture file to load. |
| atlasURL | string | Yes | Optional URL of a texture atlas JSON data file. If not given, the texture will be loaded as a single image. |
| multiAtlasURL | string | Yes | Optional URL of a multi-texture atlas JSON data file as created by Texture Packer Pro. |
| multiPath | string | Yes | Optional path to use when loading the textures defined in the multi atlas data. |
| multiBaseURL | string | Yes | Optional Base URL to use when loading the textures defined in the multi atlas data. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/CompressedTextureFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/CompressedTextureFileConfig.js#L1)

---

## CompressedTextureFileConfig

### <static> CompressedTextureFileConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| ETC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes | The string, or file entry object, for an ETC format texture. |
| --- | --- | --- | --- |
| ETC1 | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes | The string, or file entry object, for an ETC1 format texture. |
| ATC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes | The string, or file entry object, for an ATC format texture. |
| ASTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes | The string, or file entry object, for an ASTC format texture. |
| BPTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes | The string, or file entry object, for an BPTC format texture. |
| RGTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes | The string, or file entry object, for an RGTC format texture. |
| PVRTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes | The string, or file entry object, for an PVRTC format texture. |
| S3TC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes | The string, or file entry object, for an S3TC format texture. |
| S3TCSRGB | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes | The string, or file entry object, for an S3TCSRGB format texture. |
| IMG | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes | The string, or file entry object, for the fallback image file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/CompressedTextureFileConfig.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/CompressedTextureFileConfig.js#L13)

---

## CSSFileConfig

### <static> CSSFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within the Loader. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'css'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/CSSFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/CSSFileConfig.js#L1)

---

## FontFileConfig

### <static> FontFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within the Loader. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'js'" | The default file extension to use if no url is provided. |
| type | string | Yes | "'script'" | The script type. Should be either 'script' for classic JavaScript, or 'module' if the file contains an exported module. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/FontFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/FontFileConfig.js#L1)

---

## GLSLFileConfig

### <static> GLSLFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Text Cache. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| shaderType | string | Yes | "'fragment'" | The type of shader. Either `fragment` for a fragment shader, or `vertex` for a vertex shader. This is ignored if you load a shader bundle. |
| extension | string | Yes | "'glsl'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/GLSLFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/GLSLFileConfig.js#L1)

---

## HTMLFileConfig

### <static> HTMLFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Text Cache. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'html'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/HTMLFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/HTMLFileConfig.js#L1)

---

## HTMLTextureFileConfig

### <static> HTMLTextureFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Texture Manager. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'html'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |
| width | number | Yes | 512 | The width of the texture the HTML will be rendered to. |
| height | number | Yes | 512 | The height of the texture the HTML will be rendered to. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/HTMLTextureFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/HTMLTextureFileConfig.js#L1)

---

## ImageFileConfig

### <static> ImageFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Texture Manager. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'png'" | The default file extension to use if no url is provided. |
| normalMap | string | Yes |  | The filename of an associated normal map. It uses the same path and url to load as the image. |
| frameConfig | [Phaser.Types.Loader.FileTypes.ImageFrameConfig](types-loader-filetypes.md) | Yes |  | The frame configuration object. Only provided for, and used by, Sprite Sheets. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/ImageFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/ImageFileConfig.js#L1)

---

## ImageFrameConfig

### <static> ImageFrameConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| frameWidth | number | No |  | The width of the frame in pixels. |
| --- | --- | --- | --- | --- |
| frameHeight | number | Yes |  | The height of the frame in pixels. Uses the `frameWidth` value if not provided. |
| startFrame | number | Yes | 0 | The first frame to start parsing from. |
| endFrame | number | Yes |  | The frame to stop parsing at. If not provided it will calculate the value based on the image and frame dimensions. |
| margin | number | Yes | 0 | The margin in the image. This is the space around the edge of the frames. |
| spacing | number | Yes | 0 | The spacing between each frame in the image. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/ImageFrameConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/ImageFrameConfig.js#L1)

---

## JSONFileConfig

### <static> JSONFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the JSON Cache. |
| --- | --- | --- | --- | --- |
| url | string | any | Yes |  | The absolute or relative URL to load the file from. Or can be a ready formed JSON object, in which case it will be directly added to the Cache. |
| extension | string | Yes | "'json'" | The default file extension to use if no url is provided. |
| dataKey | string | Yes |  | If specified instead of the whole JSON file being parsed and added to the Cache, only the section corresponding to this property key will be added. If the property you want to extract is nested, use periods to divide it. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/JSONFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/JSONFileConfig.js#L1)

---

## MultiAtlasFileConfig

### <static> MultiAtlasFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Texture Manager. |
| --- | --- | --- | --- | --- |
| atlasURL | string | Yes |  | The absolute or relative URL to load the multi atlas json file from. Or, a well formed JSON object. |
| url | string | Yes |  | An alias for 'atlasURL'. If given, it overrides anything set in 'atlasURL'. |
| atlasExtension | string | Yes | "'json'" | The default file extension to use for the atlas json if no url is provided. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the atlas json file. |
| path | string | Yes |  | Optional path to use when loading the textures defined in the atlas data. |
| baseURL | string | Yes |  | Optional Base URL to use when loading the textures defined in the atlas data. |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the texture files. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/MultiAtlasFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/MultiAtlasFileConfig.js#L1)

---

## MultiScriptFileConfig

### <static> MultiScriptFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within the Loader. |
| --- | --- | --- | --- | --- |
| url | Array.<string> | Yes |  | An array of absolute or relative URLs to load the script files from. They are processed in the order given in the array. |
| extension | string | Yes | "'js'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for these files. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/MultiScriptFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/MultiScriptFileConfig.js#L1)

---

## OBJFileConfig

### <static> OBJFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the OBJ Cache. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load this file from. If undefined or `null` it will be set to `<key>.obj`, i.e. if `key` was "alien" then the URL will be "alien.obj". |
| extension | string | Yes | "'obj'" | The default file extension to use if no url is provided. |
| flipUV | boolean | Yes |  | Flip the UV coordinates stored in the model data? |
| matURL | string | Yes |  | An optional absolute or relative URL to the object material file from. If undefined or `null`, no material file will be loaded. |
| matExtension | string | Yes | "'mat'" | The default material file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/OBJFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/OBJFileConfig.js#L1)

---

## PackFileConfig

### <static> PackFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the JSON Cache. |
| --- | --- | --- | --- | --- |
| url | string | any | Yes |  | The absolute or relative URL to load the file from. Or can be a ready formed JSON object, in which case it will be directly processed. |
| extension | string | Yes | "'json'" | The default file extension to use if no url is provided. |
| dataKey | string | Yes |  | If specified instead of the whole JSON file being parsed, only the section corresponding to this property key will be added. If the property you want to extract is nested, use periods to divide it. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/PackFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/PackFileConfig.js#L1)

---

## PackFileSection

### <static> PackFileSection

| name | type | optional | description |
| --- | --- | --- | --- |
| files | Array.<[Phaser.Types.Loader.FileConfig](types-loader.md)> | No | The files to load. See {@link Phaser.Types.Loader.FileTypes}. |
| --- | --- | --- | --- |
| baseURL | string | Yes | A URL used to resolve paths in `files`. Example: '<http://labs.phaser.io/assets/>'. |
| defaultType | string | Yes | The default {@link Phaser.Types.Loader.FileConfig} `type`. |
| path | string | Yes | A URL path used to resolve relative paths in `files`. Example: 'images/sprites/'. |
| prefix | string | Yes | An optional prefix that is automatically prepended to each file key. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/PackFileSection.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/PackFileSection.js#L1)

---

## PluginFileConfig

### <static> PluginFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within the Loader. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'js'" | The default file extension to use if no url is provided. |
| start | boolean | Yes | false | Automatically start the plugin after loading? |
| mapping | string | Yes |  | If this plugin is to be injected into the Scene, this is the property key used. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/PluginFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/PluginFileConfig.js#L1)

---

## SceneFileConfig

### <static> SceneFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Text Cache. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'js'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/SceneFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/SceneFileConfig.js#L1)

---

## ScenePluginFileConfig

### <static> ScenePluginFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within the Loader. |
| --- | --- | --- | --- | --- |
| url | string | function | Yes |  | The absolute or relative URL to load the file from. Or, a Scene Plugin. |
| extension | string | Yes | "'js'" | The default file extension to use if no url is provided. |
| systemKey | string | Yes |  | If this plugin is to be added to Scene.Systems, this is the property key for it. |
| sceneKey | string | Yes |  | If this plugin is to be added to the Scene, this is the property key for it. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/ScenePluginFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/ScenePluginFileConfig.js#L1)

---

## ScriptFileConfig

### <static> ScriptFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within the Loader. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'js'" | The default file extension to use if no url is provided. |
| type | string | Yes | "'script'" | The script type. Should be either 'script' for classic JavaScript, or 'module' if the file contains an exported module. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/ScriptFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/ScriptFileConfig.js#L1)

---

## SpriteSheetFileConfig

### <static> SpriteSheetFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Texture Manager. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'png'" | The default file extension to use if no url is provided. |
| normalMap | string | Yes |  | The filename of an associated normal map. It uses the same path and url to load as the image. |
| frameConfig | [Phaser.Types.Loader.FileTypes.ImageFrameConfig](types-loader-filetypes.md) | Yes |  | The frame configuration object. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/SpriteSheetFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/SpriteSheetFileConfig.js#L1)

---

## SVGFileConfig

### <static> SVGFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Texture Manager. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'svg'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |
| svgConfig | [Phaser.Types.Loader.FileTypes.SVGSizeConfig](types-loader-filetypes.md) | Yes |  | The svg size configuration object. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/SVGFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/SVGFileConfig.js#L1)

---

## SVGSizeConfig

### <static> SVGSizeConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | Yes | An optional width. The SVG will be resized to this size before being rendered to a texture. |
| --- | --- | --- | --- |
| height | number | Yes | An optional height. The SVG will be resized to this size before being rendered to a texture. |
| scale | number | Yes | An optional scale. If given it overrides the width / height properties. The SVG is scaled by the scale factor before being rendered to a texture. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/SVGSizeConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/SVGSizeConfig.js#L1)

---

## TextFileConfig

### <static> TextFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Text Cache. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'txt'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/TextFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/TextFileConfig.js#L1)

---

## TilemapCSVFileConfig

### <static> TilemapCSVFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Tilemap Cache. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'csv'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/TilemapCSVFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/TilemapCSVFileConfig.js#L1)

---

## TilemapImpactFileConfig

### <static> TilemapImpactFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Tilemap Cache. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'json'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/TilemapImpactFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/TilemapImpactFileConfig.js#L1)

---

## TilemapJSONFileConfig

### <static> TilemapJSONFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Tilemap Cache. |
| --- | --- | --- | --- | --- |
| url | object | string | Yes |  | The absolute or relative URL to load the file from. Or, a well formed JSON object. |
| extension | string | Yes | "'json'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/TilemapJSONFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/TilemapJSONFileConfig.js#L1)

---

## UnityAtlasFileConfig

### <static> UnityAtlasFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Texture Manager. |
| --- | --- | --- | --- | --- |
| textureURL | string | Yes |  | The absolute or relative URL to load the texture image file from. |
| textureExtension | string | Yes | "'png'" | The default file extension to use for the image texture if no url is provided. |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the texture image file. |
| normalMap | string | Yes |  | The filename of an associated normal map. It uses the same path and url to load as the texture image. |
| atlasURL | string | Yes |  | The absolute or relative URL to load the atlas data file from. |
| atlasExtension | string | Yes | "'txt'" | The default file extension to use for the atlas data if no url is provided. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the atlas data file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/UnityAtlasFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/UnityAtlasFileConfig.js#L1)

---

## VideoFileConfig

### <static> VideoFileConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Types.Loader.FileTypes.VideoFileConfig](types-loader-filetypes.md) | No | The key to use for this file, or a file configuration object. |
| --- | --- | --- | --- |
| url | string | Array.<string> | [Phaser.Types.Loader.FileTypes.VideoFileURLConfig](types-loader-filetypes.md) | Array.<[Phaser.Types.Loader.FileTypes.VideoFileURLConfig](types-loader-filetypes.md)> |
| noAudio | boolean | Yes | Does the video have an audio track? If not you can enable auto-playing on it. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/VideoFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/VideoFileConfig.js#L1)

---

## VideoFileURLConfig

### <static> VideoFileURLConfig

| name | type | optional | description |
| --- | --- | --- | --- |
| type | string | No | The video file format. See property names in {@link Phaser.Device.Video}. |
| --- | --- | --- | --- |
| url | string | No | The absolute or relative URL of the video file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/VideoFileURLConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/VideoFileURLConfig.js#L1)

---

## XMLFileConfig

### <static> XMLFileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The key of the file. Must be unique within both the Loader and the Text Cache. |
| --- | --- | --- | --- | --- |
| url | string | Yes |  | The absolute or relative URL to load the file from. |
| extension | string | Yes | "'xml'" | The default file extension to use if no url is provided. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for this file. |

**Type**: object

**Member of**: Phaser.Types.Loader.FileTypes

> Source: [src/loader/filetypes/typedefs/XMLFileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/filetypes/typedefs/XMLFileConfig.js#L1)

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Loader.FileTypes](#typesloaderfiletypes)

  + [AsepriteFileConfig](#asepritefileconfig)

    - [<static> AsepriteFileConfig](#static-asepritefileconfig)
  + [AtlasJSONFileConfig](#atlasjsonfileconfig)

    - [<static> AtlasJSONFileConfig](#static-atlasjsonfileconfig)
  + [AtlasXMLFileConfig](#atlasxmlfileconfig)

    - [<static> AtlasXMLFileConfig](#static-atlasxmlfileconfig)
  + [AudioFileConfig](#audiofileconfig)

    - [<static> AudioFileConfig](#static-audiofileconfig)
  + [AudioFileURLConfig](#audiofileurlconfig)

    - [<static> AudioFileURLConfig](#static-audiofileurlconfig)
  + [AudioSpriteFileConfig](#audiospritefileconfig)

    - [<static> AudioSpriteFileConfig](#static-audiospritefileconfig)
  + [BinaryFileConfig](#binaryfileconfig)

    - [<static> BinaryFileConfig](#static-binaryfileconfig)
  + [BitmapFontFileConfig](#bitmapfontfileconfig)

    - [<static> BitmapFontFileConfig](#static-bitmapfontfileconfig)
  + [CompressedTextureFileEntry](#compressedtexturefileentry)

    - [<static> CompressedTextureFileEntry](#static-compressedtexturefileentry)
  + [CompressedTextureFileConfig](#compressedtexturefileconfig)

    - [<static> CompressedTextureFileConfig](#static-compressedtexturefileconfig)
  + [CSSFileConfig](#cssfileconfig)

    - [<static> CSSFileConfig](#static-cssfileconfig)
  + [FontFileConfig](#fontfileconfig)

    - [<static> FontFileConfig](#static-fontfileconfig)
  + [GLSLFileConfig](#glslfileconfig)

    - [<static> GLSLFileConfig](#static-glslfileconfig)
  + [HTMLFileConfig](#htmlfileconfig)

    - [<static> HTMLFileConfig](#static-htmlfileconfig)
  + [HTMLTextureFileConfig](#htmltexturefileconfig)

    - [<static> HTMLTextureFileConfig](#static-htmltexturefileconfig)
  + [ImageFileConfig](#imagefileconfig)

    - [<static> ImageFileConfig](#static-imagefileconfig)
  + [ImageFrameConfig](#imageframeconfig)

    - [<static> ImageFrameConfig](#static-imageframeconfig)
  + [JSONFileConfig](#jsonfileconfig)

    - [<static> JSONFileConfig](#static-jsonfileconfig)
  + [MultiAtlasFileConfig](#multiatlasfileconfig)

    - [<static> MultiAtlasFileConfig](#static-multiatlasfileconfig)
  + [MultiScriptFileConfig](#multiscriptfileconfig)

    - [<static> MultiScriptFileConfig](#static-multiscriptfileconfig)
  + [OBJFileConfig](#objfileconfig)

    - [<static> OBJFileConfig](#static-objfileconfig)
  + [PackFileConfig](#packfileconfig)

    - [<static> PackFileConfig](#static-packfileconfig)
  + [PackFileSection](#packfilesection)

    - [<static> PackFileSection](#static-packfilesection)
  + [PluginFileConfig](#pluginfileconfig)

    - [<static> PluginFileConfig](#static-pluginfileconfig)
  + [SceneFileConfig](#scenefileconfig)

    - [<static> SceneFileConfig](#static-scenefileconfig)
  + [ScenePluginFileConfig](#scenepluginfileconfig)

    - [<static> ScenePluginFileConfig](#static-scenepluginfileconfig)
  + [ScriptFileConfig](#scriptfileconfig)

    - [<static> ScriptFileConfig](#static-scriptfileconfig)
  + [SpriteSheetFileConfig](#spritesheetfileconfig)

    - [<static> SpriteSheetFileConfig](#static-spritesheetfileconfig)
  + [SVGFileConfig](#svgfileconfig)

    - [<static> SVGFileConfig](#static-svgfileconfig)
  + [SVGSizeConfig](#svgsizeconfig)

    - [<static> SVGSizeConfig](#static-svgsizeconfig)
  + [TextFileConfig](#textfileconfig)

    - [<static> TextFileConfig](#static-textfileconfig)
  + [TilemapCSVFileConfig](#tilemapcsvfileconfig)

    - [<static> TilemapCSVFileConfig](#static-tilemapcsvfileconfig)
  + [TilemapImpactFileConfig](#tilemapimpactfileconfig)

    - [<static> TilemapImpactFileConfig](#static-tilemapimpactfileconfig)
  + [TilemapJSONFileConfig](#tilemapjsonfileconfig)

    - [<static> TilemapJSONFileConfig](#static-tilemapjsonfileconfig)
  + [UnityAtlasFileConfig](#unityatlasfileconfig)

    - [<static> UnityAtlasFileConfig](#static-unityatlasfileconfig)
  + [VideoFileConfig](#videofileconfig)

    - [<static> VideoFileConfig](#static-videofileconfig)
  + [VideoFileURLConfig](#videofileurlconfig)

    - [<static> VideoFileURLConfig](#static-videofileurlconfig)
  + [XMLFileConfig](#xmlfileconfig)

    - [<static> XMLFileConfig](#static-xmlfileconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Loader.FileTypes