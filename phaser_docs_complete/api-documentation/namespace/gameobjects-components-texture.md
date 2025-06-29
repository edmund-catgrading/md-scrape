# Phaser.GameObjects.Components.Texture

Scope:
static

> Source: [src/gameobjects/components/Texture.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L12)  
> Since: 3.0.0

# Static functions

## frame

### frame: [Phaser.Textures.Frame](../class/textures-frame.md)

**Description:**

The Texture Frame this Game Object is using to render with.

> Source: [src/gameobjects/components/Texture.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L30)  
> Since: 3.0.0

---

## texture

### texture: [Phaser.Textures.Texture](../class/textures-texture.md), [Phaser.Textures.CanvasTexture](../class/textures-canvastexture.md)

**Description:**

The Texture this Game Object is using to render with.

> Source: [src/gameobjects/components/Texture.js#L21](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L21)  
> Since: 3.0.0

---

## isCropped

### isCropped: boolean

**Description:**

Internal flag. Not to be set by this Game Object.

**Access:** private

> Source: [src/gameobjects/components/Texture.js#L39](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L39)  
> Since: 3.11.0

---

# Static functions

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

**Returns:** [Phaser.GameObjects.Components.Texture](gameobjects-components-texture.md) - This Game Object instance.

> Source: [src/gameobjects/components/Texture.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L75)  
> Since: 3.0.0

---

## setTexture

### <instance> setTexture(key, [frame], [updateSize], [updateOrigin])

**Description:**

Sets the texture and frame this Game Object will use to render with.

Textures are referenced by their string-based keys, as stored in the Texture Manager.

Calling this method will modify the `width` and `height` properties of your Game Object.

It will also change the `origin` if the Frame has a custom pivot point, as exported from packages like Texture Packer.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Textures.Texture](../class/textures-texture.md) | No |  | The key of the texture to be used, as stored in the Texture Manager, or a Texture instance. |
| --- | --- | --- | --- | --- |
| frame | string | number | Yes |  | The name or index of the frame within the Texture. |
| updateSize | boolean | Yes | true | Should this call adjust the size of the Game Object? |
| updateOrigin | boolean | Yes | true | Should this call change the origin of the Game Object? |

**Returns:** [Phaser.GameObjects.Components.Texture](gameobjects-components-texture.md) - This Game Object instance.

> Source: [src/gameobjects/components/Texture.js#L49](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Texture.js#L49)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [frame](#frame)

    - [frame: Phaser.Textures.Frame](#frame-phasertexturesframe)
  + [texture](#texture)

    - [texture: Phaser.Textures.Texture, Phaser.Textures.CanvasTexture](#texture-phasertexturestexture-phasertexturescanvastexture)
  + [isCropped](#iscropped)

    - [isCropped: boolean](#iscropped-boolean)
* [Static functions](#static-functions-1)

  + [setFrame](#setframe)

    - [<instance> setFrame(frame, [updateSize], [updateOrigin])](#instance-setframeframe-updatesize-updateorigin)
  + [setTexture](#settexture)

    - [<instance> setTexture(key, [frame], [updateSize], [updateOrigin])](#instance-settexturekey-frame-updatesize-updateorigin)

Back to top

©2025[Phaser](https://docs.phaser.io)