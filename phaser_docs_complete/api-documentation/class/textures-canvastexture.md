# CanvasTexture

Phaser.Textures.CanvasTexture

A Canvas Texture is a special kind of Texture that is backed by an HTML Canvas Element as its source.

You can use the properties of this texture to draw to the canvas element directly, using all of the standard

canvas operations available in the browser. Any Game Object can be given this texture and will render with it.

Note: When running under WebGL the Canvas Texture needs to re-generate its base WebGLTexture and reupload it to

the GPU every time you modify it, otherwise the changes you make to this texture will not be visible. To do this

you should call `CanvasTexture.refresh()` once you are finished with your changes to the canvas. Try and keep

this to a minimum, especially on large canvas sizes, or you may inadvertently thrash the GPU by constantly uploading

texture data to it. This restriction does not apply if using the Canvas Renderer.

It starts with only one frame that covers the whole of the canvas. You can add further frames, that specify

sections of the canvas using the `add` method.

Should you need to resize the canvas use the `setSize` method so that it accurately updates all of the underlying

texture data as well. Forgetting to do this (i.e. by changing the canvas size directly from your code) could cause

graphical errors.

**Constructor**

`new CanvasTexture(manager, key, source, width, height)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| manager | [Phaser.Textures.TextureManager](textures-texturemanager.md) | No | A reference to the Texture Manager this Texture belongs to. |
| --- | --- | --- | --- |
| key | string | No | The unique string-based key of this Texture. |
| source | HTMLCanvasElement | No | The canvas element that is used as the base of this texture. |
| width | number | No | The width of the canvas. |
| height | number | No | The height of the canvas. |

---

**Scope**: static

**Extends**

> [Phaser.Textures.Texture](textures-texture.md)

> Source: [src/textures/CanvasTexture.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L14)  
> Since: 3.7.0

# Public Members

## buffer

### buffer: ArrayBuffer

**Description:**

An ArrayBuffer the same size as the context ImageData.

> Source: [src/textures/CanvasTexture.js#L145](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L145)  
> Since: 3.13.0

---

## canvas

### canvas: HTMLCanvasElement

**Description:**

The source Canvas Element.

> Source: [src/textures/CanvasTexture.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L68)  
> Since: 3.7.0

---

## context

### context: CanvasRenderingContext2D

**Description:**

The 2D Canvas Rendering Context.

> Source: [src/textures/CanvasTexture.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L78)  
> Since: 3.7.0

---

## customData

### customData: object

**Description:**

Any additional data that was set in the source JSON (if any),

or any extra data you'd like to store relating to this texture

**Inherits:** [Phaser.Textures.Texture#customData](textures-texture.md)

> Source: [src/textures/Texture.js#L97](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L97)  
> Since: 3.0.0

---

## data

### data: Uint8ClampedArray

**Description:**

A Uint8ClampedArray view into the `buffer`.

Use the `update` method to populate this when the canvas changes.

Note that this is unavailable in some browsers, such as Epic Browser, due to their security restrictions.

> Source: [src/textures/CanvasTexture.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L120)  
> Since: 3.13.0

---

## dataSource

### dataSource: array

**Description:**

An array of TextureSource data instances.

Used to store additional data images, such as normal maps or specular maps.

**Inherits:** [Phaser.Textures.Texture#dataSource](textures-texture.md)

> Source: [src/textures/Texture.js#L78](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L78)  
> Since: 3.0.0

---

## firstFrame

### firstFrame: string

**Description:**

The name of the first frame of the Texture.

**Inherits:** [Phaser.Textures.Texture#firstFrame](textures-texture.md)

> Source: [src/textures/Texture.js#L107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L107)  
> Since: 3.0.0

---

## frames

### frames: object

**Description:**

A key-value object pair associating the unique Frame keys with the Frames objects.

**Inherits:** [Phaser.Textures.Texture#frames](textures-texture.md)

> Source: [src/textures/Texture.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L88)  
> Since: 3.0.0

---

## frameTotal

### frameTotal: number

**Description:**

The total number of Frames in this Texture, including the `__BASE` frame.

A Texture will always contain at least 1 frame because every Texture contains a `__BASE` frame by default,

in addition to any extra frames that have been added to it, such as when parsing a Sprite Sheet or Texture Atlas.

**Inherits:** [Phaser.Textures.Texture#frameTotal](textures-texture.md)

> Source: [src/textures/Texture.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L116)  
> Since: 3.0.0

---

## height

### height: number

**Description:**

The height of the Canvas.

This property is read-only, if you wish to change it use the `setSize` method.

> Source: [src/textures/CanvasTexture.js#L99](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L99)  
> Since: 3.7.0

---

## imageData

### imageData: ImageData

**Description:**

The context image data.

Use the `update` method to populate this when the canvas changes.

> Source: [src/textures/CanvasTexture.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L110)  
> Since: 3.13.0

---

## key

### key: string

**Description:**

The unique string-based key of this Texture.

**Inherits:** [Phaser.Textures.Texture#key](textures-texture.md)

> Source: [src/textures/Texture.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L59)  
> Since: 3.0.0

---

## manager

### manager: [Phaser.Textures.TextureManager](textures-texturemanager.md)

**Description:**

A reference to the Texture Manager this Texture belongs to.

**Inherits:** [Phaser.Textures.Texture#manager](textures-texture.md)

> Source: [src/textures/Texture.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L50)  
> Since: 3.0.0

---

## pixels

### pixels: Uint32Array

**Description:**

An Uint32Array view into the `buffer`.

> Source: [src/textures/CanvasTexture.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L136)  
> Since: 3.13.0

---

## source

### source: Array.<[Phaser.Textures.TextureSource](textures-texturesource.md)>

**Description:**

An array of TextureSource instances.

These are unique to this Texture and contain the actual Image (or Canvas) data.

**Inherits:** [Phaser.Textures.Texture#source](textures-texture.md)

> Source: [src/textures/Texture.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L68)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The width of the Canvas.

This property is read-only, if you wish to change it use the `setSize` method.

> Source: [src/textures/CanvasTexture.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L88)  
> Since: 3.7.0

---

# Private Members

## \_source

### \_source: [Phaser.Textures.TextureSource](textures-texturesource.md)

**Description:**

A reference to the Texture Source of this Canvas.

**Access:** private

> Source: [src/textures/CanvasTexture.js#L58](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L58)  
> Since: 3.7.0

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

**Inherits:** [Phaser.Textures.Texture#add](textures-texture.md)

> Source: [src/textures/Texture.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L136)  
> Since: 3.0.0

---

## clear

### <instance> clear([x], [y], [width], [height], [update])

**Description:**

Clears the given region of this Canvas Texture, resetting it back to transparent.

If no region is given, the whole Canvas Texture is cleared.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x coordinate of the top-left of the region to clear. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y coordinate of the top-left of the region to clear. |
| width | number | Yes |  | The width of the region. |
| height | number | Yes |  | The height of the region. |
| update | boolean | Yes | true | Update the internal ImageData buffer and arrays. |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - The Canvas Texture.

> Source: [src/textures/CanvasTexture.js#L554](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L554)  
> Since: 3.7.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this Texture and releases references to its sources and frames.

**Overrides:** Phaser.Textures.Texture#destroy

> Source: [src/textures/CanvasTexture.js#L626](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L626)  
> Since: 3.16.0

---

## draw

### <instance> draw(x, y, source, [update])

**Description:**

Draws the given Image or Canvas element to this CanvasTexture, then updates the internal

ImageData buffer and arrays.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate to draw the source at. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate to draw the source at. |
| source | HTMLImageElement | HTMLCanvasElement | No |  | The element to draw to this canvas. |
| update | boolean | Yes | true | Update the internal ImageData buffer and arrays. |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - This CanvasTexture.

> Source: [src/textures/CanvasTexture.js#L213](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L213)  
> Since: 3.13.0

---

## drawFrame

### <instance> drawFrame(key, [frame], [x], [y], [update])

**Description:**

Draws the given texture frame to this CanvasTexture, then updates the internal

ImageData buffer and arrays.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The unique string-based key of the Texture. |
| --- | --- | --- | --- | --- |
| frame | string | number | Yes |  | The string-based name, or integer based index, of the Frame to get from the Texture. |
| x | number | Yes | 0 | The x coordinate to draw the source at. |
| y | number | Yes | 0 | The y coordinate to draw the source at. |
| update | boolean | Yes | true | Update the internal ImageData buffer and arrays. |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - This CanvasTexture.

> Source: [src/textures/CanvasTexture.js#L241](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L241)  
> Since: 3.16.0

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

**Inherits:** [Phaser.Textures.Texture#get](textures-texture.md)

> Source: [src/textures/Texture.js#L224](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L224)  
> Since: 3.0.0

---

## getCanvas

### <instance> getCanvas()

**Description:**

Gets the Canvas Element.

**Returns:** HTMLCanvasElement - The Canvas DOM element this texture is using.

> Source: [src/textures/CanvasTexture.js#L528](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L528)  
> Since: 3.7.0

---

## getContext

### <instance> getContext()

**Description:**

Gets the 2D Canvas Rendering Context.

**Returns:** CanvasRenderingContext2D - The Canvas Rendering Context this texture is using.

> Source: [src/textures/CanvasTexture.js#L541](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L541)  
> Since: 3.7.0

---

## getData

### <instance> getData(x, y, width, height)

**Description:**

Gets an ImageData region from this CanvasTexture from the position and size specified.

You can write this back using `CanvasTexture.putData`, or manipulate it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the top-left of the area to get the ImageData from. Must lay within the dimensions of this CanvasTexture and be an integer. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the top-left of the area to get the ImageData from. Must lay within the dimensions of this CanvasTexture and be an integer. |
| width | number | No | The width of the rectangle from which the ImageData will be extracted. Positive values are to the right, and negative to the left. |
| height | number | No | The height of the rectangle from which the ImageData will be extracted. Positive values are down, and negative are up. |

**Returns:** ImageData - The ImageData extracted from this CanvasTexture.

> Source: [src/textures/CanvasTexture.js#L360](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L360)  
> Since: 3.16.0

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

**Inherits:** [Phaser.Textures.Texture#getDataSourceImage](textures-texture.md)

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

**Inherits:** [Phaser.Textures.Texture#getFrameBounds](textures-texture.md)

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

**Inherits:** [Phaser.Textures.Texture#getFrameNames](textures-texture.md)

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

**Inherits:** [Phaser.Textures.Texture#getFramesFromTextureSource](textures-texture.md)

> Source: [src/textures/Texture.js#L284](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L284)  
> Since: 3.0.0

---

## getIndex

### <instance> getIndex(x, y)

**Description:**

Returns the Image Data index for the given pixel in this CanvasTexture.

The index can be used to read directly from the `this.data` array.

The index points to the red value in the array. The subsequent 3 indexes

point to green, blue and alpha respectively.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer. |

**Returns:** number - undefined

> Source: [src/textures/CanvasTexture.js#L480](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L480)  
> Since: 3.16.0

---

## getPixel

### <instance> getPixel(x, y, [out])

**Description:**

Get the color of a specific pixel from this texture and store it in a Color object.

If you have drawn anything to this CanvasTexture since it was created you must call `CanvasTexture.update` to refresh the array buffer,

otherwise this may return out of date color values, or worse - throw a run-time error as it tries to access an array element that doesn't exist.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer. |
| out | [Phaser.Display.Color](../namespace/display-color.md) | Yes | A Color object to store the pixel values in. If not provided a new Color object will be created. |

**Returns:** [Phaser.Display.Color](../namespace/display-color.md) - An object with the red, green, blue and alpha values set in the r, g, b and a properties.

> Source: [src/textures/CanvasTexture.js#L386](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L386)  
> Since: 3.13.0

---

## getPixels

### <instance> getPixels([x], [y], [width], [height])

**Description:**

Returns an array containing all of the pixels in the given region.

If the requested region extends outside the bounds of this CanvasTexture,

the region is truncated to fit.

If you have drawn anything to this CanvasTexture since it was created you must call `CanvasTexture.update` to refresh the array buffer,

otherwise this may return out of date color values, or worse - throw a run-time error as it tries to access an array element that doesn't exist.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x coordinate of the top-left of the region. Must lay within the dimensions of this CanvasTexture and be an integer. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y coordinate of the top-left of the region. Must lay within the dimensions of this CanvasTexture and be an integer. |
| width | number | Yes |  | The width of the region to get. Must be an integer. Defaults to the canvas width if not given. |
| height | number | Yes |  | The height of the region to get. Must be an integer. If not given will be set to the `width`. |

**Returns:** Array.<Array.<[Phaser.Types.Textures.PixelConfig](../typedef/types-textures.md)>> - A 2d array of Pixel objects.

> Source: [src/textures/CanvasTexture.js#L425](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L425)  
> Since: 3.16.0

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

**Inherits:** [Phaser.Textures.Texture#getSourceImage](textures-texture.md)

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

**Inherits:** [Phaser.Textures.Texture#getTextureSourceIndex](textures-texture.md)

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

**Inherits:** [Phaser.Textures.Texture#has](textures-texture.md)

> Source: [src/textures/Texture.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L209)  
> Since: 3.0.0

---

## putData

### <instance> putData(imageData, x, y, [dirtyX], [dirtyY], [dirtyWidth], [dirtyHeight])

**Description:**

Puts the ImageData into the context of this CanvasTexture at the given coordinates.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| imageData | ImageData | No |  | The ImageData to put at the given location. |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate to put the imageData. Must lay within the dimensions of this CanvasTexture and be an integer. |
| y | number | No |  | The y coordinate to put the imageData. Must lay within the dimensions of this CanvasTexture and be an integer. |
| dirtyX | number | Yes | 0 | Horizontal position (x coordinate) of the top-left corner from which the image data will be extracted. |
| dirtyY | number | Yes | 0 | Vertical position (x coordinate) of the top-left corner from which the image data will be extracted. |
| dirtyWidth | number | Yes |  | Width of the rectangle to be painted. Defaults to the width of the image data. |
| dirtyHeight | number | Yes |  | Height of the rectangle to be painted. Defaults to the height of the image data. |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - This CanvasTexture.

> Source: [src/textures/CanvasTexture.js#L332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L332)  
> Since: 3.16.0

---

## refresh

### <instance> refresh()

**Description:**

This should be called manually if you are running under WebGL.

It will refresh the WebGLTexture from the Canvas source. Only call this if you know that the

canvas has changed, as there is a significant GPU texture allocation cost involved in doing so.

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - This CanvasTexture.

> Source: [src/textures/CanvasTexture.js#L511](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L511)  
> Since: 3.7.0

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

**Inherits:** [Phaser.Textures.Texture#remove](textures-texture.md)

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

**Inherits:** [Phaser.Textures.Texture#setDataSource](textures-texture.md)

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

**Inherits:** [Phaser.Textures.Texture#setFilter](textures-texture.md)

> Source: [src/textures/Texture.js#L502](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/Texture.js#L502)  
> Since: 3.0.0

---

## setPixel

### <instance> setPixel(x, y, red, green, blue, [alpha])

**Description:**

Sets a pixel in the CanvasTexture to the given color and alpha values.

This is an expensive operation to run in large quantities, so use sparingly.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate of the pixel to get. Must lay within the dimensions of this CanvasTexture and be an integer. |
| red | number | No |  | The red color value. A number between 0 and 255. |
| green | number | No |  | The green color value. A number between 0 and 255. |
| blue | number | No |  | The blue color value. A number between 0 and 255. |
| alpha | number | Yes | 255 | The alpha value. A number between 0 and 255. |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - This CanvasTexture.

> Source: [src/textures/CanvasTexture.js#L291](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L291)  
> Since: 3.16.0

---

## setSize

### <instance> setSize(width, [height])

**Description:**

Changes the size of this Canvas Texture.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The new width of the Canvas. |
| --- | --- | --- | --- |
| height | number | Yes | The new height of the Canvas. If not given it will use the width as the height. |

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - The Canvas Texture.

> Source: [src/textures/CanvasTexture.js#L587](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L587)  
> Since: 3.7.0

---

## update

### <instance> update()

**Description:**

This re-creates the `imageData` from the current context.

It then re-builds the ArrayBuffer, the `data` Uint8ClampedArray reference and the `pixels` Int32Array.

Warning: This is a very expensive operation, so use it sparingly.

**Returns:** [Phaser.Textures.CanvasTexture](textures-canvastexture.md) - This CanvasTexture.

> Source: [src/textures/CanvasTexture.js#L173](https://github.com/phaserjs/phaser/blob/v3.87.0/src/textures/CanvasTexture.js#L173)  
> Since: 3.13.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [buffer](#buffer)

    - [buffer: ArrayBuffer](#buffer-arraybuffer)
  + [canvas](#canvas)

    - [canvas: HTMLCanvasElement](#canvas-htmlcanvaselement)
  + [context](#context)

    - [context: CanvasRenderingContext2D](#context-canvasrenderingcontext2d)
  + [customData](#customdata)

    - [customData: object](#customdata-object)
  + [data](#data)

    - [data: Uint8ClampedArray](#data-uint8clampedarray)
  + [dataSource](#datasource)

    - [dataSource: array](#datasource-array)
  + [firstFrame](#firstframe)

    - [firstFrame: string](#firstframe-string)
  + [frames](#frames)

    - [frames: object](#frames-object)
  + [frameTotal](#frametotal)

    - [frameTotal: number](#frametotal-number)
  + [height](#height)

    - [height: number](#height-number)
  + [imageData](#imagedata)

    - [imageData: ImageData](#imagedata-imagedata)
  + [key](#key)

    - [key: string](#key-string)
  + [manager](#manager)

    - [manager: Phaser.Textures.TextureManager](#manager-phasertexturestexturemanager)
  + [pixels](#pixels)

    - [pixels: Uint32Array](#pixels-uint32array)
  + [source](#source)

    - [source: Array.<Phaser.Textures.TextureSource>](#source-arrayphasertexturestexturesource)
  + [width](#width)

    - [width: number](#width-number)
* [Private Members](#private-members)

  + [\_source](#_source)

    - [\_source: Phaser.Textures.TextureSource](#_source-phasertexturestexturesource)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(name, sourceIndex, x, y, width, height)](#instance-addname-sourceindex-x-y-width-height)
  + [clear](#clear)

    - [<instance> clear([x], [y], [width], [height], [update])](#instance-clearx-y-width-height-update)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [draw](#draw)

    - [<instance> draw(x, y, source, [update])](#instance-drawx-y-source-update)
  + [drawFrame](#drawframe)

    - [<instance> drawFrame(key, [frame], [x], [y], [update])](#instance-drawframekey-frame-x-y-update)
  + [get](#get)

    - [<instance> get([name])](#instance-getname)
  + [getCanvas](#getcanvas)

    - [<instance> getCanvas()](#instance-getcanvas)
  + [getContext](#getcontext)

    - [<instance> getContext()](#instance-getcontext)
  + [getData](#getdata)

    - [<instance> getData(x, y, width, height)](#instance-getdatax-y-width-height)
  + [getDataSourceImage](#getdatasourceimage)

    - [<instance> getDataSourceImage([name])](#instance-getdatasourceimagename)
  + [getFrameBounds](#getframebounds)

    - [<instance> getFrameBounds([sourceIndex])](#instance-getframeboundssourceindex)
  + [getFrameNames](#getframenames)

    - [<instance> getFrameNames([includeBase])](#instance-getframenamesincludebase)
  + [getFramesFromTextureSource](#getframesfromtexturesource)

    - [<instance> getFramesFromTextureSource(sourceIndex, [includeBase])](#instance-getframesfromtexturesourcesourceindex-includebase)
  + [getIndex](#getindex)

    - [<instance> getIndex(x, y)](#instance-getindexx-y)
  + [getPixel](#getpixel)

    - [<instance> getPixel(x, y, [out])](#instance-getpixelx-y-out)
  + [getPixels](#getpixels)

    - [<instance> getPixels([x], [y], [width], [height])](#instance-getpixelsx-y-width-height)
  + [getSourceImage](#getsourceimage)

    - [<instance> getSourceImage([name])](#instance-getsourceimagename)
  + [getTextureSourceIndex](#gettexturesourceindex)

    - [<instance> getTextureSourceIndex(source)](#instance-gettexturesourceindexsource)
  + [has](#has)

    - [<instance> has(name)](#instance-hasname)
  + [putData](#putdata)

    - [<instance> putData(imageData, x, y, [dirtyX], [dirtyY], [dirtyWidth], [dirtyHeight])](#instance-putdataimagedata-x-y-dirtyx-dirtyy-dirtywidth-dirtyheight)
  + [refresh](#refresh)

    - [<instance> refresh()](#instance-refresh)
  + [remove](#remove)

    - [<instance> remove(name)](#instance-removename)
  + [setDataSource](#setdatasource)

    - [<instance> setDataSource(data)](#instance-setdatasourcedata)
  + [setFilter](#setfilter)

    - [<instance> setFilter(filterMode)](#instance-setfilterfiltermode)
  + [setPixel](#setpixel)

    - [<instance> setPixel(x, y, red, green, blue, [alpha])](#instance-setpixelx-y-red-green-blue-alpha)
  + [setSize](#setsize)

    - [<instance> setSize(width, [height])](#instance-setsizewidth-height)
  + [update](#update)

    - [<instance> update()](#instance-update)

Back to top

©2025[Phaser](https://docs.phaser.io)