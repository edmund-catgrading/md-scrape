# TextureManager

Phaser.Textures.TextureManager

When Phaser boots it will create an instance of this Texture Manager class.

It is a global manager that handles all textures in your game. You can access it from within

a Scene via the `this.textures` property.

Its role is as a manager for all textures that your game uses. It can create, update and remove

textures globally, as well as parse texture data from external files, such as sprite sheets

and texture atlases.

Sprites and other texture-based Game Objects get their texture data directly from this class.

**Constructor**

`new TextureManager(game)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | The Phaser.Game instance this Texture Manager belongs to. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/textures/TextureManager.js#L32](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L32)  
> Since: 3.0.0

# Public Members

## game

### game: [Phaser.Game](game.md)

**Description:**

The Game that the Texture Manager belongs to.

A game will only ever have one instance of a Texture Manager.

> Source: [src/textures/TextureManager.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L63)  
> Since: 3.0.0

---

## list

### list: object

**Description:**

This object contains all Textures that belong to this Texture Manager.

Textures are identified by string-based keys, which are used as the property

within this object. Therefore, you can access any texture directly from this

object without any iteration.

You should not typically modify this object directly, but instead use the

methods provided by the Texture Manager to add and remove entries from it.

> Source: [src/textures/TextureManager.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L84)  
> Since: 3.0.0

---

## name

### name: string

**Description:**

The internal name of this manager.

> Source: [src/textures/TextureManager.js#L74](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L74)  
> Since: 3.0.0

---

## silentWarnings

### silentWarnings: boolean

**Description:**

If this flag is `true` then the Texture Manager will never emit any

warnings to the console log that report missing textures.

> Source: [src/textures/TextureManager.js#L157](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L157)  
> Since: 3.60.0

---

## stamp

### stamp: [Phaser.GameObjects.Image](gameobjects-image.md)

**Description:**

An Image Game Object that belongs to this Texture Manager.

Used as a drawing stamp within Dynamic Textures.

This is not part of the display list and doesn't render.

> Source: [src/textures/TextureManager.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L134)  
> Since: 3.60.0

---

## stampCrop

### stampCrop: [Phaser.Geom.Rectangle](geom-rectangle.md)

**Description:**

The crop Rectangle as used by the Stamp when it needs to crop itself.

> Source: [src/textures/TextureManager.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L148)  
> Since: 3.60.0

---

# Private Members

## \_pending

### \_pending: number

**Description:**

An internal tracking value used for emitting the 'READY' event after all of

the managers in the game have booted.

**Access:** private

> Source: [src/textures/TextureManager.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L122)  
> Since: 3.0.0

---

## \_tempCanvas

### \_tempCanvas: HTMLCanvasElement

**Description:**

The temporary canvas element used to save the pixel data of an arbitrary texture

during the `TextureManager.getPixel` and `getPixelAlpha` methods.

**Access:** private

> Source: [src/textures/TextureManager.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L101)  
> Since: 3.0.0

---

## \_tempContext

### \_tempContext: CanvasRenderingContext2D

**Description:**

The 2d context of the `_tempCanvas` element.

**Access:** private

> Source: [src/textures/TextureManager.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L112)  
> Since: 3.0.0

---

# Public Methods

## addAtlas

### <instance> addAtlas(key, source, data, [dataSource])

**Description:**

Adds a Texture Atlas to this Texture Manager.

In Phaser terminology, a Texture Atlas is a combination of an atlas image and a JSON data file,

such as those exported by applications like Texture Packer.

It can accept either JSON Array or JSON Hash formats, as exported by Texture Packer and similar software.

As of Phaser 3.60 you can use this method to add a atlas data to an existing Phaser Texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| source | HTMLImageElement | Array.<HTMLImageElement> | [Phaser.Textures.Texture](textures-texture.md) | No |
| data | object | Array.<object> | No | The Texture Atlas data/s. |
| dataSource | HTMLImageElement | HTMLCanvasElement | Array.<HTMLImageElement> | Array.<HTMLCanvasElement> |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

> Source: [src/textures/TextureManager.js#L799](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L799)  
> Since: 3.0.0

---

## addAtlasJSONArray

### <instance> addAtlasJSONArray(key, source, data, [dataSource])

**Description:**

Adds a Texture Atlas to this Texture Manager.

In Phaser terminology, a Texture Atlas is a combination of an atlas image and a JSON data file,

such as those exported by applications like Texture Packer.

The frame data of the atlas must be stored in an Array within the JSON.

This is known as a JSON Array in software such as Texture Packer.

As of Phaser 3.60 you can use this method to add a atlas data to an existing Phaser Texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| source | HTMLImageElement | Array.<HTMLImageElement> | [Phaser.Textures.Texture](textures-texture.md) | No |
| data | object | Array.<object> | No | The Texture Atlas data/s. |
| dataSource | HTMLImageElement | HTMLCanvasElement | Array.<HTMLImageElement> | Array.<HTMLCanvasElement> |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L832](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L832)  
> Since: 3.0.0

---

## addAtlasJSONHash

### <instance> addAtlasJSONHash(key, source, data, [dataSource])

**Description:**

Adds a Texture Atlas to this Texture Manager.

In Phaser terminology, a Texture Atlas is a combination of an atlas image and a JSON data file,

such as those exported by applications like Texture Packer.

The frame data of the atlas must be stored in an Object within the JSON.

This is known as a JSON Hash in software such as Texture Packer.

As of Phaser 3.60 you can use this method to add a atlas data to an existing Phaser Texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| source | HTMLImageElement | Array.<HTMLImageElement> | [Phaser.Textures.Texture](textures-texture.md) | No |
| data | object | Array.<object> | No | The Texture Atlas data/s. |
| dataSource | HTMLImageElement | HTMLCanvasElement | Array.<HTMLImageElement> | Array.<HTMLCanvasElement> |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L901](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L901)  
> Since: 3.0.0

---

## addAtlasXML

### <instance> addAtlasXML(key, source, data, [dataSource])

**Description:**

Adds a Texture Atlas to this Texture Manager.

In Phaser terminology, a Texture Atlas is a combination of an atlas image and a data file,

such as those exported by applications like Texture Packer.

The frame data of the atlas must be stored in an XML file.

As of Phaser 3.60 you can use this method to add a atlas data to an existing Phaser Texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| source | HTMLImageElement | [Phaser.Textures.Texture](textures-texture.md) | No | The source Image element, or a Phaser Texture. |
| data | object | No | The Texture Atlas XML data. |
| dataSource | HTMLImageElement | HTMLCanvasElement | Array.<HTMLImageElement> | Array.<HTMLCanvasElement> |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L964](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L964)  
> Since: 3.7.0

---

## addBase64

### <instance> addBase64(key, data)

**Description:**

Adds a new Texture to the Texture Manager created from the given Base64 encoded data.

It works by creating an `Image` DOM object, then setting the `src` attribute to

the given base64 encoded data. As a result, the process is asynchronous by its nature,

so be sure to listen for the events this method dispatches before using the texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| data | \* | No | The Base64 encoded data. |

**Returns:** [Phaser.Textures.TextureManager](textures-texturemanager.md) - This Texture Manager instance.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md), [Phaser.Textures.Events#event:ERROR](../event/textures-events.md), [Phaser.Textures.Events#event:LOAD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L334](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L334)  
> Since: 3.0.0

---

## addCanvas

### <instance> addCanvas(key, source, [skipCache])

**Description:**

Creates a new Canvas Texture object from an existing Canvas element

and adds it to this Texture Manager, unless `skipCache` is true.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The unique string-based key of the Texture. |
| --- | --- | --- | --- | --- |
| source | HTMLCanvasElement | No |  | The Canvas element to form the base of the new Texture. |
| skipCache | boolean | Yes | false | Skip adding this Texture into the Cache? |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - The Canvas Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L705](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L705)  
> Since: 3.0.0

---

## addCompressedTexture

### <instance> addCompressedTexture(key, textureData, [atlasData])

**Description:**

Adds a Compressed Texture to this Texture Manager.

The texture should typically have been loaded via the `CompressedTextureFile` loader,

in order to prepare the correct data object this method requires.

You can optionally also pass atlas data to this method, in which case a texture atlas

will be generated from the given compressed texture, combined with the atlas data.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| textureData | [Phaser.Types.Textures.CompressedTextureData](../typedef/types-textures.md) | No | The Compressed Texture data object. |
| atlasData | object | Yes | Optional Texture Atlas data. |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L522](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L522)  
> Since: 3.60.0

---

## addDynamicTexture

### <instance> addDynamicTexture(key, [width], [height])

**Description:**

Creates a Dynamic Texture instance and adds itself to this Texture Manager.

A Dynamic Texture is a special texture that allows you to draw textures, frames and most kind of

Game Objects directly to it.

You can take many complex objects and draw them to this one texture, which can then be used as the

base texture for other Game Objects, such as Sprites. Should you then update this texture, all

Game Objects using it will instantly be updated as well, reflecting the changes immediately.

It's a powerful way to generate dynamic textures at run-time that are WebGL friendly and don't invoke

expensive GPU uploads on each change.

See the methods available on the `DynamicTexture` class for more details.

Optionally, you can also pass a Dynamic Texture instance to this method to have

it added to the Texture Manager.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Textures.DynamicTexture](textures-dynamictexture.md) | No |  | The string-based key of this Texture. Must be unique within the Texture Manager. Or, a DynamicTexture instance. |
| --- | --- | --- | --- | --- |
| width | number | Yes | 256 | The width of this Dynamic Texture in pixels. Defaults to 256 x 256. Ignored if an instance is passed as the key. |
| height | number | Yes | 256 | The height of this Dynamic Texture in pixels. Defaults to 256 x 256. Ignored if an instance is passed as the key. |

**Returns:** [Phaser.Textures.DynamicTexture](textures-dynamictexture.md) - The Dynamic Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L742](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L742)  
> Since: 3.60.0

---

## addGLTexture

### <instance> addGLTexture(key, glTexture)

**Description:**

Takes a WebGLTextureWrapper and creates a Phaser Texture from it, which is added to the Texture Manager using the given key.

This allows you to then use the Texture as a normal texture for texture based Game Objects like Sprites.

This is a WebGL only feature.

Prior to Phaser 3.80.0, this method took a bare `WebGLTexture`

as the `glTexture` parameter. You must now wrap the `WebGLTexture` in a

`WebGLTextureWrapper` instance before passing it to this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| glTexture | [Phaser.Renderer.WebGL.Wrappers.WebGLTextureWrapper](renderer-webgl-wrappers-webgltexturewrapper.md) | No | The source Render Texture. |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L482](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L482)  
> Since: 3.19.0

---

## addImage

### <instance> addImage(key, source, [dataSource])

**Description:**

Adds a new Texture to the Texture Manager created from the given Image element.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| source | HTMLImageElement | No | The source Image element. |
| dataSource | HTMLImageElement | HTMLCanvasElement | Yes | An optional data Image element. |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L447](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L447)  
> Since: 3.0.0

---

## addListener

### <instance> addListener(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Textures.TextureManager](textures-texturemanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addRenderTexture

### <instance> addRenderTexture(key, renderTexture)

**Description:**

Adds a Render Texture to the Texture Manager using the given key.

This allows you to then use the Render Texture as a normal texture for texture based Game Objects like Sprites.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| renderTexture | [Phaser.GameObjects.RenderTexture](gameobjects-rendertexture.md) | No | The source Render Texture. |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L584](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L584)  
> Since: 3.12.0

---

## addSpriteSheet

### <instance> addSpriteSheet(key, source, config, [dataSource])

**Description:**

Adds a Sprite Sheet to this Texture Manager.

In Phaser terminology a Sprite Sheet is a texture containing different frames, but each frame is the exact

same size and cannot be trimmed or rotated. This is different to a Texture Atlas, created by tools such as

Texture Packer, and more akin with the fixed-frame exports you get from apps like Aseprite or old arcade

games.

As of Phaser 3.60 you can use this method to add a sprite sheet to an existing Phaser Texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. Give an empty string if you provide a Phaser Texture as the 2nd argument. |
| --- | --- | --- | --- |
| source | HTMLImageElement | [Phaser.Textures.Texture](textures-texture.md) | No | The source Image element, or a Phaser Texture. |
| config | [Phaser.Types.Textures.SpriteSheetConfig](../typedef/types-textures.md) | No | The configuration object for this Sprite Sheet. |
| dataSource | HTMLImageElement | HTMLCanvasElement | Yes | An optional data Image element. |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created or updated, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L1066](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1066)  
> Since: 3.0.0

---

## addSpriteSheetFromAtlas

### <instance> addSpriteSheetFromAtlas(key, config)

**Description:**

Adds a Sprite Sheet to this Texture Manager, where the Sprite Sheet exists as a Frame within a Texture Atlas.

In Phaser terminology a Sprite Sheet is a texture containing different frames, but each frame is the exact

same size and cannot be trimmed or rotated.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Textures.SpriteSheetFromAtlasConfig](../typedef/types-textures.md) | No | The configuration object for this Sprite Sheet. |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L1120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1120)  
> Since: 3.0.0

---

## addUint8Array

### <instance> addUint8Array(key, data, width, height)

**Description:**

Creates a texture from an array of colour data.

This is only available in WebGL mode.

If the dimensions provided are powers of two, the resulting texture

will be automatically set to wrap by the WebGL Renderer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| data | Uint8Array | No | The color data for the texture. |
| width | number | No | The width of the texture. |
| height | number | No | The height of the texture. |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L1179](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1179)  
> Since: 3.80.0

---

## addUnityAtlas

### <instance> addUnityAtlas(key, source, data, [dataSource])

**Description:**

Adds a Unity Texture Atlas to this Texture Manager.

In Phaser terminology, a Texture Atlas is a combination of an atlas image and a data file,

such as those exported by applications like Texture Packer or Unity.

The frame data of the atlas must be stored in a Unity YAML file.

As of Phaser 3.60 you can use this method to add a atlas data to an existing Phaser Texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| source | HTMLImageElement | No | The source Image element. |
| data | object | No | The Texture Atlas data. |
| dataSource | HTMLImageElement | HTMLCanvasElement | Array.<HTMLImageElement> | Array.<HTMLCanvasElement> |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

**Fires:** [Phaser.Textures.Events#event:ADD](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L1015](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1015)  
> Since: 3.0.0

---

## checkKey

### <instance> checkKey(key)

**Description:**

Checks the given texture key and throws a console.warn if the key is already in use, then returns false.

If you wish to avoid the console.warn then use `TextureManager.exists` instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The texture key to check. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if it's safe to use the texture key, otherwise `false`.

> Source: [src/textures/TextureManager.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L236)  
> Since: 3.7.0

---

## cloneFrame

### <instance> cloneFrame(key, frame)

**Description:**

Takes a Texture key and Frame name and returns a clone of that Frame if found.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| frame | string | number | No | The string or index of the Frame to be cloned. |

**Returns:** [Phaser.Textures.Frame](textures-frame.md) - A Clone of the given Frame.

> Source: [src/textures/TextureManager.js#L1300](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1300)  
> Since: 3.0.0

---

## create

### <instance> create(key, source, [width], [height])

**Description:**

Creates a new Texture using the given source and dimensions.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| source | HTMLImageElement | HTMLCanvasElement | Array.<HTMLImageElement> | Array.<HTMLCanvasElement> |
| width | number | Yes | The width of the Texture. This is optional and automatically derived from the source images. |
| height | number | Yes | The height of the Texture. This is optional and automatically derived from the source images. |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

> Source: [src/textures/TextureManager.js#L1218](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1218)  
> Since: 3.0.0

---

## createCanvas

### <instance> createCanvas(key, [width], [height])

**Description:**

Creates a new Texture using a blank Canvas element of the size given.

Canvas elements are automatically pooled and calling this method will

extract a free canvas from the CanvasPool, or create one if none are available.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The unique string-based key of the Texture. |
| --- | --- | --- | --- | --- |
| width | number | Yes | 256 | The width of the Canvas element. |
| height | number | Yes | 256 | The height of the Canvas element. |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - The Canvas Texture that was created, or `null` if the key is already in use.

> Source: [src/textures/TextureManager.js#L675](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L675)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys the Texture Manager and all Textures stored within it.

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/textures/TextureManager.js#L1615](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1615)  
> Since: 3.0.0

---

## each

### <instance> each(callback, scope, [args])

**Description:**

Passes all Textures to the given callback.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | EachTextureCallback | No | The callback function to be sent the Textures. |
| --- | --- | --- | --- |
| scope | object | No | The value to use as `this` when executing the callback. |
| args | \* | Yes | Additional arguments that will be passed to the callback, after the child. |

> Source: [src/textures/TextureManager.js#L1559](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1559)  
> Since: 3.0.0

---

## emit

### <instance> emit(event, [args])

**Description:**

Calls each of the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| args | \* | Yes | Additional arguments that will be passed to the event handler. |

**Returns:** boolean - `true` if the event had listeners, else `false`.

**Inherits:** [Phaser.Events.EventEmitter#emit](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L86)  
> Since: 3.0.0

---

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## exists

### <instance> exists(key)

**Description:**

Checks the given key to see if a Texture using it exists within this Texture Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |

**Returns:** boolean - Returns `true` if a Texture matching the given key exists in this Texture Manager.

> Source: [src/textures/TextureManager.js#L1245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1245)  
> Since: 3.0.0

---

## generate

### <instance> generate(key, config)

**Description:**

Creates a new Texture using the given config values.

Generated textures consist of a Canvas element to which the texture data is drawn.

Generates a texture based on the given Create configuration object.

The texture is drawn using a fixed-size indexed palette of 16 colors, where the hex value in the

data cells map to a single color. For example, if the texture config looked like this:

```
Copy
var star = [

  '.....828.....',

  '....72227....',

  '....82228....',

  '...7222227...',

  '2222222222222',

  '8222222222228',

  '.72222222227.',

  '..787777787..',

  '..877777778..',

  '.78778887787.',

  '.27887.78872.',

  '.787.....787.'

];



this.textures.generate('star', { data: star, pixelWidth: 4 });


```

Then it would generate a texture that is 52 x 48 pixels in size, because each cell of the data array

represents 1 pixel multiplied by the `pixelWidth` value. The cell values, such as `8`, maps to color

number 8 in the palette. If a cell contains a period character `.` then it is transparent.

The default palette is Arne16, but you can specify your own using the `palette` property.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Create.GenerateTextureConfig](../typedef/types-create.md) | No | The configuration object needed to generate the texture. |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture that was created, or `null` if the key is already in use.

> Source: [src/textures/TextureManager.js#L614](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L614)  
> Since: 3.0.0

---

## get

### <instance> get(key)

**Description:**

Returns a Texture from the Texture Manager that matches the given key.

If the key is `undefined` it will return the `__DEFAULT` Texture.

If the key is an instance of a Texture, it will return the instance.

If the key is an instance of a Frame, it will return the frames parent Texture instance.

Finally, if the key is given, but not found, and not a Texture or Frame instance, it will return the `__MISSING` Texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Textures.Texture](textures-texture.md) | [Phaser.Textures.Frame](textures-frame.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Textures.Texture](textures-texture.md) - The Texture matching the given key.

> Source: [src/textures/TextureManager.js#L1260](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1260)  
> Since: 3.0.0

---

## getBase64

### <instance> getBase64(key, [frame], [type], [encoderOptions])

**Description:**

Gets an existing texture frame and converts it into a base64 encoded image and returns the base64 data.

You can also provide the image type and encoder options.

This will only work with bitmap based texture frames, such as those created from Texture Atlases.

It will not work with GL Texture objects, such as Shaders, or Render Textures. For those please

see the WebGL Snapshot function instead.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The unique string-based key of the Texture. |
| --- | --- | --- | --- | --- |
| frame | string | number | Yes |  | The string-based name, or integer based index, of the Frame to get from the Texture. |
| type | string | Yes | "'image/png'" | A DOMString indicating the image format. The default format type is image/png. |
| encoderOptions | number | Yes | 0.92 | A Number between 0 and 1 indicating the image quality to use for image formats that use lossy compression such as image/jpeg and image/webp. If this argument is anything else, the default value for image quality is used. The default value is 0.92. Other arguments are ignored. |

**Returns:** string - The base64 encoded data, or an empty string if the texture frame could not be found.

> Source: [src/textures/TextureManager.js#L382](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L382)  
> Since: 3.12.0

---

## getFrame

### <instance> getFrame(key, [frame])

**Description:**

Takes a Texture key and Frame name and returns a reference to that Frame, if found.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| --- | --- | --- | --- |
| frame | string | number | Yes | The string-based name, or integer based index, of the Frame to get from the Texture. |

**Returns:** [Phaser.Textures.Frame](textures-frame.md) - A Texture Frame object.

> Source: [src/textures/TextureManager.js#L1319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1319)  
> Since: 3.0.0

---

## getPixel

### <instance> getPixel(x, y, key, [frame])

**Description:**

Given a Texture and an `x` and `y` coordinate this method will return a new

Color object that has been populated with the color and alpha values of the pixel

at that location in the Texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the pixel within the Texture. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the pixel within the Texture. |
| key | string | No | The unique string-based key of the Texture. |
| frame | string | number | Yes | The string or index of the Frame. |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - A Color object populated with the color values of the requested pixel,

or `null` if the coordinates were out of bounds.

> Source: [src/textures/TextureManager.js#L1408](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1408)  
> Since: 3.0.0

---

## getPixelAlpha

### <instance> getPixelAlpha(x, y, key, [frame])

**Description:**

Given a Texture and an `x` and `y` coordinate this method will return a value between 0 and 255

corresponding to the alpha value of the pixel at that location in the Texture. If the coordinate

is out of bounds it will return null.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the pixel within the Texture. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the pixel within the Texture. |
| key | string | No | The unique string-based key of the Texture. |
| frame | string | number | Yes | The string or index of the Frame. |

**Returns:** number - A value between 0 and 255, or `null` if the coordinates were out of bounds.

> Source: [src/textures/TextureManager.js#L1455](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1455)  
> Since: 3.10.0

---

## getTextureKeys

### <instance> getTextureKeys()

**Description:**

Returns an array with all of the keys of all Textures in this Texture Manager.

The output array will exclude the `__DEFAULT`, `__MISSING`, `__WHITE`, and `__NORMAL` keys.

**Returns:** Array.<string> - An array containing all of the Texture keys stored in this Texture Manager.

> Source: [src/textures/TextureManager.js#L1384](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1384)  
> Since: 3.0.0

---

## listenerCount

### <instance> listenerCount(event)

**Description:**

Return the number of listeners listening to a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** number - The number of listeners.

**Inherits:** [Phaser.Events.EventEmitter#listenerCount](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L75)  
> Since: 3.0.0

---

## listeners

### <instance> listeners(event)

**Description:**

Return the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** Array.<function()> - The registered listeners.

**Inherits:** [Phaser.Events.EventEmitter#listeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L64)  
> Since: 3.0.0

---

## off

### <instance> off(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Textures.TextureManager](textures-texturemanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#off](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L151)  
> Since: 3.0.0

---

## on

### <instance> on(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Textures.TextureManager](textures-texturemanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## once

### <instance> once(event, fn, [context])

**Description:**

Add a one-time listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Textures.TextureManager](textures-texturemanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## parseFrame

### <instance> parseFrame(key)

**Description:**

Parses the 'key' parameter and returns a Texture Frame instance.

It can accept the following formats:

1. A string
2. An array where the elements are: [ key, [frame] ]
3. An object with the properties: { key, [frame] }
4. A Texture instance - which returns the default frame from the Texture
5. A Frame instance - returns itself

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | array | object | [Phaser.Textures.Texture](textures-texture.md) |
| --- | --- | --- | --- |

**Returns:** [Phaser.Textures.Frame](textures-frame.md) - A Texture Frame object, if found, or undefined if not.

> Source: [src/textures/TextureManager.js#L1338](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1338)  
> Since: 3.60.0

---

## remove

### <instance> remove(key)

**Description:**

Removes a Texture from the Texture Manager and destroys it. This will immediately

clear all references to it from the Texture Manager, and if it has one, destroy its

WebGLTexture. This will emit a `removetexture` event.

Note: If you have any Game Objects still using this texture they will start throwing

errors the next time they try to render. Make sure that removing the texture is the final

step when clearing down to avoid this.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Textures.Texture](textures-texture.md) | No | The key of the Texture to remove, or a reference to it. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Textures.TextureManager](textures-texturemanager.md) - The Texture Manager.

**Fires:** [Phaser.Textures.Events#event:REMOVE](../event/textures-events.md)

> Source: [src/textures/TextureManager.js#L264](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L264)  
> Since: 3.7.0

---

## removeAllListeners

### <instance> removeAllListeners([event])

**Description:**

Remove all listeners, or those of the specified event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | Yes | The event name. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Textures.TextureManager](textures-texturemanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeKey

### <instance> removeKey(key)

**Description:**

Removes a key from the Texture Manager but does not destroy the Texture that was using the key.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key to remove from the texture list. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Textures.TextureManager](textures-texturemanager.md) - The Texture Manager.

> Source: [src/textures/TextureManager.js#L314](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L314)  
> Since: 3.17.0

---

## removeListener

### <instance> removeListener(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Textures.TextureManager](textures-texturemanager.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## renameTexture

### <instance> renameTexture(currentKey, newKey)

**Description:**

Changes the key being used by a Texture to the new key provided.

The old key is removed, allowing it to be re-used.

Game Objects are linked to Textures by a reference to the Texture object, so

all existing references will be retained.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| currentKey | string | No | The current string-based key of the Texture you wish to rename. |
| --- | --- | --- | --- |
| newKey | string | No | The new unique string-based key to use for the Texture. |

**Returns:** boolean - `true` if the Texture key was successfully renamed, otherwise `false`.

> Source: [src/textures/TextureManager.js#L1525](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1525)  
> Since: 3.12.0

---

## resetStamp

### <instance> resetStamp([alpha], [tint])

**Description:**

Resets the internal Stamp object, ready for drawing and returns it.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| alpha | number | Yes | 1 | The alpha to use. |
| --- | --- | --- | --- | --- |
| tint | number | Yes | "0xffffff" | WebGL only. The tint color to use. |

**Returns:** [Phaser.GameObjects.Image](gameobjects-image.md) - A reference to the Stamp Game Object.

> Source: [src/textures/TextureManager.js#L1586](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1586)  
> Since: 3.60.0

---

## setTexture

### <instance> setTexture(gameObject, key, [frame])

**Description:**

Sets the given Game Objects `texture` and `frame` properties so that it uses

the Texture and Frame specified in the `key` and `frame` arguments to this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object the texture would be set on. |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of the Texture. |
| frame | string | number | Yes | The string or index of the Frame. |

**Returns:** [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) - The Game Object the texture was set on.

> Source: [src/textures/TextureManager.js#L1501](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L1501)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

The Boot Handler called by Phaser.Game when it first starts up.

**Access:** private

> Source: [src/textures/TextureManager.js#L171](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L171)  
> Since: 3.0.0

---

## updatePending

### <instance> updatePending()

**Description:**

After 'onload' or 'onerror' invoked twice, emit 'ready' event.

**Access:** private

> Source: [src/textures/TextureManager.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/TextureManager.js#L216)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [list](#list)

    - [list: object](#list-object)
  + [name](#name)

    - [name: string](#name-string)
  + [silentWarnings](#silentwarnings)

    - [silentWarnings: boolean](#silentwarnings-boolean)
  + [stamp](#stamp)

    - [stamp: Phaser.GameObjects.Image](#stamp-phasergameobjectsimage)
  + [stampCrop](#stampcrop)

    - [stampCrop: Phaser.Geom.Rectangle](#stampcrop-phasergeomrectangle)
* [Private Members](#private-members)

  + [\_pending](#_pending)

    - [\_pending: number](#_pending-number)
  + [\_tempCanvas](#_tempcanvas)

    - [\_tempCanvas: HTMLCanvasElement](#_tempcanvas-htmlcanvaselement)
  + [\_tempContext](#_tempcontext)

    - [\_tempContext: CanvasRenderingContext2D](#_tempcontext-canvasrenderingcontext2d)
* [Public Methods](#public-methods)

  + [addAtlas](#addatlas)

    - [<instance> addAtlas(key, source, data, [dataSource])](#instance-addatlaskey-source-data-datasource)
  + [addAtlasJSONArray](#addatlasjsonarray)

    - [<instance> addAtlasJSONArray(key, source, data, [dataSource])](#instance-addatlasjsonarraykey-source-data-datasource)
  + [addAtlasJSONHash](#addatlasjsonhash)

    - [<instance> addAtlasJSONHash(key, source, data, [dataSource])](#instance-addatlasjsonhashkey-source-data-datasource)
  + [addAtlasXML](#addatlasxml)

    - [<instance> addAtlasXML(key, source, data, [dataSource])](#instance-addatlasxmlkey-source-data-datasource)
  + [addBase64](#addbase64)

    - [<instance> addBase64(key, data)](#instance-addbase64key-data)
  + [addCanvas](#addcanvas)

    - [<instance> addCanvas(key, source, [skipCache])](#instance-addcanvaskey-source-skipcache)
  + [addCompressedTexture](#addcompressedtexture)

    - [<instance> addCompressedTexture(key, textureData, [atlasData])](#instance-addcompressedtexturekey-texturedata-atlasdata)
  + [addDynamicTexture](#adddynamictexture)

    - [<instance> addDynamicTexture(key, [width], [height])](#instance-adddynamictexturekey-width-height)
  + [addGLTexture](#addgltexture)

    - [<instance> addGLTexture(key, glTexture)](#instance-addgltexturekey-gltexture)
  + [addImage](#addimage)

    - [<instance> addImage(key, source, [dataSource])](#instance-addimagekey-source-datasource)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addRenderTexture](#addrendertexture)

    - [<instance> addRenderTexture(key, renderTexture)](#instance-addrendertexturekey-rendertexture)
  + [addSpriteSheet](#addspritesheet)

    - [<instance> addSpriteSheet(key, source, config, [dataSource])](#instance-addspritesheetkey-source-config-datasource)
  + [addSpriteSheetFromAtlas](#addspritesheetfromatlas)

    - [<instance> addSpriteSheetFromAtlas(key, config)](#instance-addspritesheetfromatlaskey-config)
  + [addUint8Array](#adduint8array)

    - [<instance> addUint8Array(key, data, width, height)](#instance-adduint8arraykey-data-width-height)
  + [addUnityAtlas](#addunityatlas)

    - [<instance> addUnityAtlas(key, source, data, [dataSource])](#instance-addunityatlaskey-source-data-datasource)
  + [checkKey](#checkkey)

    - [<instance> checkKey(key)](#instance-checkkeykey)
  + [cloneFrame](#cloneframe)

    - [<instance> cloneFrame(key, frame)](#instance-cloneframekey-frame)
  + [create](#create)

    - [<instance> create(key, source, [width], [height])](#instance-createkey-source-width-height)
  + [createCanvas](#createcanvas)

    - [<instance> createCanvas(key, [width], [height])](#instance-createcanvaskey-width-height)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [each](#each)

    - [<instance> each(callback, scope, [args])](#instance-eachcallback-scope-args)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [exists](#exists)

    - [<instance> exists(key)](#instance-existskey)
  + [generate](#generate)

    - [<instance> generate(key, config)](#instance-generatekey-config)
  + [get](#get)

    - [<instance> get(key)](#instance-getkey)
  + [getBase64](#getbase64)

    - [<instance> getBase64(key, [frame], [type], [encoderOptions])](#instance-getbase64key-frame-type-encoderoptions)
  + [getFrame](#getframe)

    - [<instance> getFrame(key, [frame])](#instance-getframekey-frame)
  + [getPixel](#getpixel)

    - [<instance> getPixel(x, y, key, [frame])](#instance-getpixelx-y-key-frame)
  + [getPixelAlpha](#getpixelalpha)

    - [<instance> getPixelAlpha(x, y, key, [frame])](#instance-getpixelalphax-y-key-frame)
  + [getTextureKeys](#gettexturekeys)

    - [<instance> getTextureKeys()](#instance-gettexturekeys)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [parseFrame](#parseframe)

    - [<instance> parseFrame(key)](#instance-parseframekey)
  + [remove](#remove)

    - [<instance> remove(key)](#instance-removekey)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeKey](#removekey)

    - [<instance> removeKey(key)](#instance-removekeykey)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [renameTexture](#renametexture)

    - [<instance> renameTexture(currentKey, newKey)](#instance-renametexturecurrentkey-newkey)
  + [resetStamp](#resetstamp)

    - [<instance> resetStamp([alpha], [tint])](#instance-resetstampalpha-tint)
  + [setTexture](#settexture)

    - [<instance> setTexture(gameObject, key, [frame])](#instance-settexturegameobject-key-frame)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [updatePending](#updatepending)

    - [<instance> updatePending()](#instance-updatepending)

Back to top

©2025[Phaser](https://docs.phaser.io)