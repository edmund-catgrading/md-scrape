# Phaser.GameObjects.Components.TextureCrop

Scope:
static

> Source: [src/gameobjects/components/TextureCrop.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L12)  
> Since: 3.0.0

# Static functions

## frame

### frame: [Phaser.Textures.Frame](../class/textures-frame.md)

**Description:**

The Texture Frame this Game Object is using to render with.

> Source: [src/gameobjects/components/TextureCrop.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L30)  
> Since: 3.0.0

---

## isCropped

### isCropped: boolean

**Description:**

A boolean flag indicating if this Game Object is being cropped or not.

You can toggle this at any time after `setCrop` has been called, to turn cropping on or off.

Equally, calling `setCrop` with no arguments will reset the crop and disable it.

> Source: [src/gameobjects/components/TextureCrop.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L39)  
> Since: 3.11.0

---

## texture

### texture: [Phaser.Textures.Texture](../class/textures-texture.md), [Phaser.Textures.CanvasTexture](../class/textures-canvastexture.md)

**Description:**

The Texture this Game Object is using to render with.

> Source: [src/gameobjects/components/TextureCrop.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L21)  
> Since: 3.0.0

---

# Static functions

## setCrop

### <instance> setCrop([x], [y], [width], [height])

**Description:**

Applies a crop to a texture based Game Object, such as a Sprite or Image.

The crop is a rectangle that limits the area of the texture frame that is visible during rendering.

Cropping a Game Object does not change its size, dimensions, physics body or hit area, it just

changes what is shown when rendered.

The crop size as well as coordinates can not exceed the the size of the texture frame.

The crop coordinates are relative to the texture frame, not the Game Object, meaning 0 x 0 is the top-left.

Therefore, if you had a Game Object that had an 800x600 sized texture, and you wanted to show only the left

half of it, you could call `setCrop(0, 0, 400, 600)`.

It is also scaled to match the Game Object scale automatically. Therefore a crop rectangle of 100x50 would crop

an area of 200x100 when applied to a Game Object that had a scale factor of 2.

You can either pass in numeric values directly, or you can provide a single Rectangle object as the first argument.

Call this method with no arguments at all to reset the crop, or toggle the property `isCropped` to `false`.

You should do this if the crop rectangle becomes the same size as the frame itself, as it will allow

the renderer to skip several internal calculations.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | Yes | The x coordinate to start the crop from. Cannot be negative or exceed the Frame width. Or a Phaser.Geom.Rectangle object, in which case the rest of the arguments are ignored. |
| --- | --- | --- | --- |
| y | number | Yes | The y coordinate to start the crop from. Cannot be negative or exceed the Frame height. |
| width | number | Yes | The width of the crop rectangle in pixels. Cannot exceed the Frame width. |
| height | number | Yes | The height of the crop rectangle in pixels. Cannot exceed the Frame height. |

**Returns:** [Phaser.GameObjects.Components.TextureCrop](gameobjects-components-texturecrop.md) - This Game Object instance.

> Source: [src/gameobjects/components/TextureCrop.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L50)  
> Since: 3.11.0

---

## setFrame

### <instance> setFrame(frame, [updateSize], [updateOrigin])

**Description:**

Sets the frame this Game Object will use to render with.

If you pass a string or index then the Frame has to belong to the current Texture being used

by this Game Object.

If you pass a Frame instance, then the Texture being used by this Game Object will also be updated.

Calling `setFrame` will modify the `width` and `height` properties of your Game Object.

It will also change the `origin` if the Frame has a custom pivot point, as exported from packages like Texture Packer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| frame | string | number | [Phaser.Textures.Frame](../class/textures-frame.md) | No |  |
| --- | --- | --- | --- | --- |
| updateSize | boolean | Yes | true | Should this call adjust the size of the Game Object? |
| updateOrigin | boolean | Yes | true | Should this call adjust the origin of the Game Object? |

**Returns:** [Phaser.GameObjects.Components.TextureCrop](gameobjects-components-texturecrop.md) - This Game Object instance.

> Source: [src/gameobjects/components/TextureCrop.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L130)  
> Since: 3.0.0

---

## setTexture

### <instance> setTexture(key, [frame])

**Description:**

Sets the texture and frame this Game Object will use to render with.

Textures are referenced by their string-based keys, as stored in the Texture Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the texture to be used, as stored in the Texture Manager. |
| --- | --- | --- | --- |
| frame | string | number | Yes | The name or index of the frame within the Texture. |

**Returns:** [Phaser.GameObjects.Components.TextureCrop](gameobjects-components-texturecrop.md) - This Game Object instance.

> Source: [src/gameobjects/components/TextureCrop.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L110)  
> Since: 3.0.0

---

## resetCropObject

### <instance> resetCropObject()

**Description:**

Internal method that returns a blank, well-formed crop object for use by a Game Object.

**Access:** private

**Returns:** object - The crop object.

> Source: [src/gameobjects/components/TextureCrop.js#L201](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TextureCrop.js#L201)  
> Since: 3.12.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [frame](#frame)

    - [frame: Phaser.Textures.Frame](#frame-phasertexturesframe)
  + [isCropped](#iscropped)

    - [isCropped: boolean](#iscropped-boolean)
  + [texture](#texture)

    - [texture: Phaser.Textures.Texture, Phaser.Textures.CanvasTexture](#texture-phasertexturestexture-phasertexturescanvastexture)
* [Static functions](#static-functions-1)

  + [setCrop](#setcrop)

    - [<instance> setCrop([x], [y], [width], [height])](#instance-setcropx-y-width-height)
  + [setFrame](#setframe)

    - [<instance> setFrame(frame, [updateSize], [updateOrigin])](#instance-setframeframe-updatesize-updateorigin)
  + [setTexture](#settexture)

    - [<instance> setTexture(key, [frame])](#instance-settexturekey-frame)
  + [resetCropObject](#resetcropobject)

    - [<instance> resetCropObject()](#instance-resetcropobject)

Back to top

©2025[Phaser](https://docs.phaser.io)