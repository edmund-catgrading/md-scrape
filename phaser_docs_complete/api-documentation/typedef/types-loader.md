# Types.Loader

Phaser.Types.Loader

## FileConfig

### <static> FileConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| type | string | No |  | The name of the Loader method that loads this file, e.g., 'image', 'json', 'spritesheet'. |
| --- | --- | --- | --- | --- |
| key | string | No |  | Unique cache key (unique within its file type) |
| url | object | string | Yes |  | The URL of the file, not including baseURL. |
| path | string | Yes |  | The path of the file, not including the baseURL. |
| extension | string | Yes |  | The default extension this file uses. |
| responseType | XMLHttpRequestResponseType | Yes |  | The responseType to be used by the XHR request. |
| xhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | false | Yes | false | Custom XHR Settings specific to this file and merged with the Loader defaults. |
| config | any | Yes |  | A config object that can be used by file types to store transitional data. |
| textureURL | string | Yes |  | The absolute or relative URL to load the texture image file from. |
| textureExtension | string | Yes | "'png'" | The default file extension to use for the image texture if no url is provided. |
| textureXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the texture image file. |
| atlasURL | object | string | Yes |  | The absolute or relative URL to load the atlas json file from. Or, a well formed JSON object to use instead. |
| atlasExtension | string | Yes | "'json'" | The default file extension to use for the atlas json if no url is provided. |
| atlasXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the atlas json file. |
| normalMap | string | Yes |  | The filename of an associated normal map. It uses the same path and url to load as the texture image. |
| context | AudioContext | Yes |  | The optional AudioContext this file will use to process itself (only used by Sound objects). |
| jsonURL | string | Yes |  | The absolute or relative URL to load the json file from. Or a well formed JSON object to use instead. |
| jsonXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the json file. |
| audioURL | Object | Yes |  | The absolute or relative URL to load the audio file from. |
| audioConfig | any | Yes |  | The audio configuration options. |
| audioXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the audio file. |
| dataType | any | Yes |  | Optional type to cast the binary file to once loaded. For example, `Uint8Array`. |
| fontDataURL | string | Yes |  | The absolute or relative URL to load the font data xml file from. |
| fontDataExtension | string | Yes | "'xml'" | The default file extension to use for the font data xml if no url is provided. |
| fontDataXhrSettings | [Phaser.Types.Loader.XHRSettingsObject](types-loader.md) | Yes |  | Extra XHR Settings specifically for the font data xml file. |
| ETC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes |  | The string, or file entry object, for an ETC format texture. |
| ETC1 | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes |  | The string, or file entry object, for an ETC1 format texture. |
| ATC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes |  | The string, or file entry object, for an ATC format texture. |
| ASTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes |  | The string, or file entry object, for an ASTC format texture. |
| BPTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes |  | The string, or file entry object, for an BPTC format texture. |
| RGTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes |  | The string, or file entry object, for an RGTC format texture. |
| PVRTC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes |  | The string, or file entry object, for an PVRTC format texture. |
| S3TC | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes |  | The string, or file entry object, for an S3TC format texture. |
| S3TCSRGB | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes |  | The string, or file entry object, for an S3TCSRGB format texture. |
| IMG | [Phaser.Types.Loader.FileTypes.CompressedTextureFileEntry](types-loader-filetypes.md) | string | Yes |  | The string, or file entry object, for the fallback image file. |
| shaderType | string | Yes | "'fragment'" | The type of shader. Either `fragment` for a fragment shader, or `vertex` for a vertex shader. This is ignored if you load a shader bundle. |
| width | number | Yes | 512 | The width of the texture the HTML will be rendered to. |
| height | number | Yes | 512 | The height of the texture the HTML will be rendered to. |
| frameConfig | [Phaser.Types.Loader.FileTypes.ImageFrameConfig](types-loader-filetypes.md) | Yes |  | The frame configuration object. Only provided for, and used by, Sprite Sheets. |
| dataKey | string | Yes |  | If specified instead of the whole JSON file being parsed and added to the Cache, only the section corresponding to this property key will be added. If the property you want to extract is nested, use periods to divide it. |
| baseURL | string | Yes |  | Optional Base URL to use when loading the textures defined in the atlas data. |
| flipUV | boolean | Yes |  | Flip the UV coordinates stored in the model data? |
| matURL | string | Yes |  | An optional absolute or relative URL to the object material file from. If undefined or `null`, no material file will be loaded. |
| matExtension | string | Yes | "'mat'" | The default material file extension to use if no url is provided. |
| start | boolean | Yes | false | Automatically start the plugin after loading? |
| mapping | string | Yes |  | If this plugin is to be injected into the Scene, this is the property key used. |
| systemKey | string | Yes |  | If this plugin is to be added to Scene.Systems, this is the property key for it. |
| sceneKey | string | Yes |  | If this plugin is to be added to the Scene, this is the property key for it. |
| svgConfig | [Phaser.Types.Loader.FileTypes.SVGSizeConfig](types-loader-filetypes.md) | Yes |  | The svg size configuration object. |
| maxRetries | number | Yes | 2 | The number of times to retry the file load if it fails. |

**Type**: object

**Member of**: Phaser.Types.Loader

> Source: [src/loader/typedefs/FileConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/typedefs/FileConfig.js#L1)  
> Since: 3.0.0

---

## XHRSettingsObject

### <static> XHRSettingsObject

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| responseType | XMLHttpRequestResponseType | No |  | The response type of the XHR request, i.e. `blob`, `text`, etc. |
| --- | --- | --- | --- | --- |
| async | boolean | Yes | true | Should the XHR request use async or not? |
| user | string | Yes | "''" | Optional username for the XHR request. |
| password | string | Yes | "''" | Optional password for the XHR request. |
| timeout | number | Yes | 0 | Optional XHR timeout value. |
| headers | object | undefined | Yes |  | This value is used to populate the XHR `setRequestHeader` and is undefined by default. |
| header | string | undefined | Yes |  | This value is used to populate the XHR `setRequestHeader` and is undefined by default. |
| headerValue | string | undefined | Yes |  | This value is used to populate the XHR `setRequestHeader` and is undefined by default. |
| requestedWith | string | undefined | Yes |  | This value is used to populate the XHR `setRequestHeader` and is undefined by default. |
| overrideMimeType | string | undefined | Yes |  | Provide a custom mime-type to use instead of the default. |
| withCredentials | boolean | Yes | false | The withCredentials property indicates whether or not cross-site Access-Control requests should be made using credentials such as cookies, authorization headers or TLS client certificates. Setting withCredentials has no effect on same-site requests. |

**Type**: object

**Member of**: Phaser.Types.Loader

> Source: [src/loader/typedefs/XHRSettingsObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/loader/typedefs/XHRSettingsObject.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Loader](#typesloader)

  + [FileConfig](#fileconfig)

    - [<static> FileConfig](#static-fileconfig)
  + [XHRSettingsObject](#xhrsettingsobject)

    - [<static> XHRSettingsObject](#static-xhrsettingsobject)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Loader