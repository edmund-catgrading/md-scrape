# Texture

Phaser.Textures.Texture

A Texture consists of a source, usually an Image from the Cache, and a collection of Frames.

The Frames represent the different areas of the Texture. For example a texture atlas

may have many Frames, one for each element within the atlas. Where-as a single image would have

just one frame, that encompasses the whole image.

Every Texture, no matter where it comes from, always has at least 1 frame called the `__BASE` frame.

This frame represents the entirety of the source image.

Textures are managed by the global TextureManager. This is a singleton class that is

responsible for creating and delivering Textures and their corresponding Frames to Game Objects.

Sprites and other Game Objects get the texture data they need from the TextureManager.

**Constructor**

`new Texture(manager, key, source, [width], [height])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| manager | [Phaser.Textures.TextureManager](textures-texturemanager.md) | No | A reference to the Texture Manager this Texture belongs to. |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of this Texture. |
| source | HTMLImageElement | HTMLCanvasElement | Array.<HTMLImageElement> | Array.<HTMLCanvasElement> |
| width | number | Yes | The width of the Texture. This is optional and automatically derived from the source images. |
| height | number | Yes | The height of the Texture. This is optional and automatically derived from the source images. |

---

**Scope**: static

> Source: [src/textures/Texture.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L13)  
> Since: 3.0.0

# Public Members

## customData

### customData: object

**Description:**

Any additional data that was set in the source JSON (if any),

or any extra data you'd like to store relating to this texture

> Source: [src/textures/Texture.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L97)  
> Since: 3.0.0

---

## dataSource

### dataSource: array

**Description:**

An array of TextureSource data instances.

Used to store additional data images, such as normal maps or specular maps.

> Source: [src/textures/Texture.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L78)  
> Since: 3.0.0

---

## firstFrame

### firstFrame: string

**Description:**

The name of the first frame of the Texture.

> Source: [src/textures/Texture.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L107)  
> Since: 3.0.0

---

## frames

### frames: object

**Description:**

A key-value object pair associating the unique Frame keys with the Frames objects.

> Source: [src/textures/Texture.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L88)  
> Since: 3.0.0

---

## frameTotal

### frameTotal: number

**Description:**

The total number of Frames in this Texture, including the `__BASE` frame.

A Texture will always contain at least 1 frame because every Texture contains a `__BASE` frame by default,

in addition to any extra frames that have been added to it, such as when parsing a Sprite Sheet or Texture Atlas.

> Source: [src/textures/Texture.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L116)  
> Since: 3.0.0

---

## key

### key: string

**Description:**

The unique string-based key of this Texture.

> Source: [src/textures/Texture.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L59)  
> Since: 3.0.0

---

## manager

### manager: [Phaser.Textures.TextureManager](textures-texturemanager.md)

**Description:**

A reference to the Texture Manager this Texture belongs to.

> Source: [src/textures/Texture.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L50)  
> Since: 3.0.0

---

## source

### source: Array.<[Phaser.Textures.TextureSource](textures-texturesource.md)>

**Description:**

An array of TextureSource instances.

These are unique to this Texture and contain the actual Image (or Canvas) data.

> Source: [src/textures/Texture.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L68)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(name, sourceIndex, x, y, width, height)

**Description:**

Adds a new Frame to this Texture.

A Frame is a rectangular region of a TextureSource with a unique index or string-based key.

The name given must be unique within this Texture. If it already exists, this method will return `null`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | number | string | No | The name of this Frame. The name is unique within the Texture. |
| --- | --- | --- | --- |
| sourceIndex | number | No | The index of the TextureSource that this Frame is a part of. |
| x | number | No | The x coordinate of the top-left of this Frame. |
| y | number | No | The y coordinate of the top-left of this Frame. |
| width | number | No | The width of this Frame. |
| height | number | No | The height of this Frame. |

**Returns:** [Phaser.Textures.Frame](textures-frame.md) - The Frame that was added to this Texture, or `null` if the given name already exists.

> Source: [src/textures/Texture.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L136)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this Texture and releases references to its sources and frames.

> Source: [src/textures/Texture.js#L531](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L531)  
> Since: 3.0.0

---

## get

### <instance> get([name])

**Description:**

Gets a Frame from this Texture based on either the key or the index of the Frame.

In a Texture Atlas Frames are typically referenced by a key.

In a Sprite Sheet Frames are referenced by an index.

Passing no value for the name returns the base texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | number | Yes | The string-based name, or integer based index, of the Frame to get from this Texture. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Textures.Frame](textures-frame.md) - The Texture Frame.

> Source: [src/textures/Texture.js#L224](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L224)  
> Since: 3.0.0

---

## getDataSourceImage

### <instance> getDataSourceImage([name])

**Description:**

Given a Frame name, return the data source image it uses to render with.

You can use this to get the normal map for an image for example.

This will return the actual DOM Image.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | number | Yes | The string-based name, or integer based index, of the Frame to get from this Texture. |
| --- | --- | --- | --- |

**Returns:** HTMLImageElement, HTMLCanvasElement - The DOM Image or Canvas Element.

> Source: [src/textures/Texture.js#L439](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L439)  
> Since: 3.7.0

---

## getFrameBounds

### <instance> getFrameBounds([sourceIndex])

**Description:**

Based on the given Texture Source Index, this method will get all of the Frames using

that source and then work out the bounds that they encompass, returning them in an object.

This is useful if this Texture is, for example, a sprite sheet within an Atlas, and you

need to know the total bounds of the sprite sheet.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| sourceIndex | number | Yes | 0 | The index of the TextureSource to get the Frame bounds from. |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.Types.Math.RectangleLike](../typedef/types-math.md) - An object containing the bounds of the Frames using the given Texture Source Index.

> Source: [src/textures/Texture.js#L319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L319)  
> Since: 3.80.0

---

## getFrameNames

### <instance> getFrameNames([includeBase])

**Description:**

Returns an array with all of the names of the Frames in this Texture.

Useful if you want to randomly assign a Frame to a Game Object, as you can

pick a random element from the returned array.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| includeBase | boolean | Yes | false | Include the `__BASE` Frame in the output array? |
| --- | --- | --- | --- | --- |

**Returns:** Array.<string> - An array of all Frame names in this Texture.

> Source: [src/textures/Texture.js#L374](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L374)  
> Since: 3.0.0

---

## getFramesFromTextureSource

### <instance> getFramesFromTextureSource(sourceIndex, [includeBase])

**Description:**

Returns an array of all the Frames in the given TextureSource.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| sourceIndex | number | No |  | The index of the TextureSource to get the Frames from. |
| --- | --- | --- | --- | --- |
| includeBase | boolean | Yes | false | Include the `__BASE` Frame in the output array? |

**Returns:** Array.<[Phaser.Textures.Frame](textures-frame.md)> - An array of Texture Frames.

> Source: [src/textures/Texture.js#L284](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L284)  
> Since: 3.0.0

---

## getSourceImage

### <instance> getSourceImage([name])

**Description:**

Given a Frame name, return the source image it uses to render with.

This will return the actual DOM Image or Canvas element.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | number | Yes | The string-based name, or integer based index, of the Frame to get from this Texture. |
| --- | --- | --- | --- |

**Returns:** HTMLImageElement, HTMLCanvasElement, [Phaser.GameObjects.RenderTexture](gameobjects-rendertexture.md) - The DOM Image, Canvas Element or Render Texture.

> Source: [src/textures/Texture.js#L406](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L406)  
> Since: 3.0.0

---

## getTextureSourceIndex

### <instance> getTextureSourceIndex(source)

**Description:**

Takes the given TextureSource and returns the index of it within this Texture.

If it's not in this Texture, it returns -1.

Unless this Texture has multiple TextureSources, such as with a multi-atlas, this

method will always return zero or -1.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| source | [Phaser.Textures.TextureSource](textures-texturesource.md) | No | The TextureSource to check. |
| --- | --- | --- | --- |

**Returns:** number - The index of the TextureSource within this Texture, or -1 if not in this Texture.

> Source: [src/textures/Texture.js#L258](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L258)  
> Since: 3.0.0

---

## has

### <instance> has(name)

**Description:**

Checks to see if a Frame matching the given key exists within this Texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The key of the Frame to check for. |
| --- | --- | --- | --- |

**Returns:** boolean - True if a Frame with the matching key exists in this Texture.

> Source: [src/textures/Texture.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L209)  
> Since: 3.0.0

---

## remove

### <instance> remove(name)

**Description:**

Removes the given Frame from this Texture. The Frame is destroyed immediately.

Any Game Objects using this Frame should stop using it *before* you remove it,

as it does not happen automatically.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The key of the Frame to remove. |
| --- | --- | --- | --- |

**Returns:** boolean - True if a Frame with the matching key was removed from this Texture.

> Source: [src/textures/Texture.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L180)  
> Since: 3.19.0

---

## setDataSource

### <instance> setDataSource(data)

**Description:**

Adds a data source image to this Texture.

An example of a data source image would be a normal map, where all of the Frames for this Texture

equally apply to the normal map.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | HTMLImageElement | HTMLCanvasElement | Array.<HTMLImageElement> | Array.<HTMLCanvasElement> |
| --- | --- | --- | --- |

> Source: [src/textures/Texture.js#L476](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L476)  
> Since: 3.0.0

---

## setFilter

### <instance> setFilter(filterMode)

**Description:**

Sets the Filter Mode for this Texture.

The mode can be either Linear, the default, or Nearest.

For pixel-art you should use Nearest.

The mode applies to the entire Texture, not just a specific Frame of it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| filterMode | [Phaser.Textures.FilterMode](../namespace/textures-filtermode.md) | No | The Filter Mode. |
| --- | --- | --- | --- |

> Source: [src/textures/Texture.js#L502](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L502)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [customData](#customdata)

    - [customData: object](#customdata-object)
  + [dataSource](#datasource)

    - [dataSource: array](#datasource-array)
  + [firstFrame](#firstframe)

    - [firstFrame: string](#firstframe-string)
  + [frames](#frames)

    - [frames: object](#frames-object)
  + [frameTotal](#frametotal)

    - [frameTotal: number](#frametotal-number)
  + [key](#key)

    - [key: string](#key-string)
  + [manager](#manager)

    - [manager: Phaser.Textures.TextureManager](#manager-phasertexturestexturemanager)
  + [source](#source)

    - [source: Array.<Phaser.Textures.TextureSource>](#source-arrayphasertexturestexturesource)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(name, sourceIndex, x, y, width, height)](#instance-addname-sourceindex-x-y-width-height)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [get](#get)

    - [<instance> get([name])](#instance-getname)
  + [getDataSourceImage](#getdatasourceimage)

    - [<instance> getDataSourceImage([name])](#instance-getdatasourceimagename)
  + [getFrameBounds](#getframebounds)

    - [<instance> getFrameBounds([sourceIndex])](#instance-getframeboundssourceindex)
  + [getFrameNames](#getframenames)

    - [<instance> getFrameNames([includeBase])](#instance-getframenamesincludebase)
  + [getFramesFromTextureSource](#getframesfromtexturesource)

    - [<instance> getFramesFromTextureSource(sourceIndex, [includeBase])](#instance-getframesfromtexturesourcesourceindex-includebase)
  + [getSourceImage](#getsourceimage)

    - [<instance> getSourceImage([name])](#instance-getsourceimagename)
  + [getTextureSourceIndex](#gettexturesourceindex)

    - [<instance> getTextureSourceIndex(source)](#instance-gettexturesourceindexsource)
  + [has](#has)

    - [<instance> has(name)](#instance-hasname)
  + [remove](#remove)

    - [<instance> remove(name)](#instance-removename)
  + [setDataSource](#setdatasource)

    - [<instance> setDataSource(data)](#instance-setdatasourcedata)
  + [setFilter](#setfilter)

    - [<instance> setFilter(filterMode)](#instance-setfilterfiltermode)

Back to top

©2025[Phaser](https://docs.phaser.io)



Texture