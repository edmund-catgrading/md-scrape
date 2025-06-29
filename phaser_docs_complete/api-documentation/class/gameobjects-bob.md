# Bob

Phaser.GameObjects.Bob

A Bob Game Object.

A Bob belongs to a Blitter Game Object. The Blitter is responsible for managing and rendering this object.

A Bob has a position, alpha value and a frame from a texture that it uses to render with. You can also toggle

the flipped and visible state of the Bob. The Frame the Bob uses to render can be changed dynamically, but it

must be a Frame within the Texture used by the parent Blitter.

Bob positions are relative to the Blitter parent. So if you move the Blitter parent, all Bob children will

have their positions impacted by this change as well.

You can manipulate Bob objects directly from your game code, but the creation and destruction of them should be

handled via the Blitter parent.

**Constructor**

`new Bob(blitter, x, y, frame, visible)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| blitter | [Phaser.GameObjects.Blitter](gameobjects-blitter.md) | No | The parent Blitter object is responsible for updating this Bob. |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of this Game Object in the world, relative to the parent Blitter position. |
| y | number | No | The vertical position of this Game Object in the world, relative to the parent Blitter position. |
| frame | string | number | No | The Frame this Bob will render with, as defined in the Texture the parent Blitter is using. |
| visible | boolean | No | Should the Bob render visible or not to start with? |

---

**Scope**: static

> Source: [src/gameobjects/blitter/Bob.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L10)  
> Since: 3.0.0

# Public Members

## alpha

### alpha: number

**Description:**

The alpha value of the Bob, between 0 and 1.

A Bob with alpha 0 will skip rendering.

> Source: [src/gameobjects/blitter/Bob.js#L409](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L409)  
> Since: 3.0.0

---

## data

### data: object

**Description:**

A blank object which can be used to store data related to this Bob in.

> Source: [src/gameobjects/blitter/Bob.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L81)  
> Since: 3.0.0

---

## flipX

### flipX: boolean

**Description:**

The horizontally flipped state of the Bob.

A Bob that is flipped horizontally will render inversed on the horizontal axis.

Flipping always takes place from the middle of the texture.

> Source: [src/gameobjects/blitter/Bob.js#L122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L122)  
> Since: 3.0.0

---

## flipY

### flipY: boolean

**Description:**

The vertically flipped state of the Bob.

A Bob that is flipped vertically will render inversed on the vertical axis (i.e. upside down)

Flipping always takes place from the middle of the texture.

> Source: [src/gameobjects/blitter/Bob.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L133)  
> Since: 3.0.0

---

## frame

### frame: [Phaser.Textures.Frame](textures-frame.md)

**Description:**

The frame that the Bob uses to render with.

To change the frame use the `Bob.setFrame` method.

**Access:** protected

> Source: [src/gameobjects/blitter/Bob.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L70)  
> Since: 3.0.0

---

## parent

### parent: [Phaser.GameObjects.Blitter](gameobjects-blitter.md)

**Description:**

The Blitter object that this Bob belongs to.

> Source: [src/gameobjects/blitter/Bob.js#L43](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L43)  
> Since: 3.0.0

---

## tint

### tint: number

**Description:**

The tint value of this Bob.

> Source: [src/gameobjects/blitter/Bob.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L91)  
> Since: 3.20.0

---

## visible

### visible: boolean

**Description:**

The visible state of the Bob.

An invisible Bob will skip rendering.

> Source: [src/gameobjects/blitter/Bob.js#L385](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L385)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x position of this Bob, relative to the x position of the Blitter.

> Source: [src/gameobjects/blitter/Bob.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L52)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of this Bob, relative to the y position of the Blitter.

> Source: [src/gameobjects/blitter/Bob.js#L61](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L61)  
> Since: 3.0.0

---

# Private Members

## \_alpha

### \_alpha: number

**Description:**

The alpha value of this Bob.

**Access:** private

> Source: [src/gameobjects/blitter/Bob.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L111)  
> Since: 3.0.0

---

## \_visible

### \_visible: boolean

**Description:**

The visible state of this Bob.

**Access:** private

> Source: [src/gameobjects/blitter/Bob.js#L101](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L101)  
> Since: 3.0.0

---

## hasTransformComponent

### hasTransformComponent: boolean

**Description:**

Private read-only property used to allow Bobs to have physics bodies.

**Access:** private

> Source: [src/gameobjects/blitter/Bob.js#L144](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L144)  
> Since: 3.60.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this Bob instance.

Removes itself from the Blitter and clears the parent, frame and data properties.

> Source: [src/gameobjects/blitter/Bob.js#L367](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L367)  
> Since: 3.0.0

---

## reset

### <instance> reset(x, y, [frame])

**Description:**

Resets this Bob.

Changes the position to the values given, and optionally changes the frame.

Also resets the flipX and flipY values, sets alpha back to 1 and visible to true.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the Bob. Bob coordinate are relative to the position of the Blitter object. |
| --- | --- | --- | --- |
| y | number | No | The y position of the Bob. Bob coordinate are relative to the position of the Blitter object. |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | Yes |

**Returns:** [Phaser.GameObjects.Bob](gameobjects-bob.md) - This Bob Game Object.

> Source: [src/gameobjects/blitter/Bob.js#L202](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L202)  
> Since: 3.0.0

---

## resetFlip

### <instance> resetFlip()

**Description:**

Resets the horizontal and vertical flipped state of this Bob back to their default un-flipped state.

**Returns:** [Phaser.GameObjects.Bob](gameobjects-bob.md) - This Bob Game Object.

> Source: [src/gameobjects/blitter/Bob.js#L186](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L186)  
> Since: 3.0.0

---

## setAlpha

### <instance> setAlpha(value)

**Description:**

Set the Alpha level of this Bob. The alpha controls the opacity of the Game Object as it renders.

Alpha values are provided as a float between 0, fully transparent, and 1, fully opaque.

A Bob with alpha 0 will skip rendering.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The alpha value used for this Bob. Between 0 and 1. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Bob](gameobjects-bob.md) - This Bob Game Object.

> Source: [src/gameobjects/blitter/Bob.js#L330](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L330)  
> Since: 3.0.0

---

## setFlip

### <instance> setFlip(x, y)

**Description:**

Sets the horizontal and vertical flipped state of this Bob.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | boolean | No | The horizontal flipped state. `false` for no flip, or `true` to be flipped. |
| --- | --- | --- | --- |
| y | boolean | No | The horizontal flipped state. `false` for no flip, or `true` to be flipped. |

**Returns:** [Phaser.GameObjects.Bob](gameobjects-bob.md) - This Bob Game Object.

> Source: [src/gameobjects/blitter/Bob.js#L292](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L292)  
> Since: 3.0.0

---

## setFlipX

### <instance> setFlipX(value)

**Description:**

Sets the horizontal flipped state of this Bob.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The flipped state. `false` for no flip, or `true` to be flipped. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Bob](gameobjects-bob.md) - This Bob Game Object.

> Source: [src/gameobjects/blitter/Bob.js#L258](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L258)  
> Since: 3.0.0

---

## setFlipY

### <instance> setFlipY(value)

**Description:**

Sets the vertical flipped state of this Bob.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The flipped state. `false` for no flip, or `true` to be flipped. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Bob](gameobjects-bob.md) - This Bob Game Object.

> Source: [src/gameobjects/blitter/Bob.js#L275](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L275)  
> Since: 3.0.0

---

## setFrame

### <instance> setFrame([frame])

**Description:**

Changes the Texture Frame being used by this Bob.

The frame must be part of the Texture the parent Blitter is using.

If no value is given it will use the default frame of the Blitter parent.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| frame | string | number | [Phaser.Textures.Frame](textures-frame.md) | Yes |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Bob](gameobjects-bob.md) - This Bob Game Object.

> Source: [src/gameobjects/blitter/Bob.js#L156](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L156)  
> Since: 3.0.0

---

## setPosition

### <instance> setPosition(x, y)

**Description:**

Changes the position of this Bob to the values given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position of the Bob. Bob coordinate are relative to the position of the Blitter object. |
| --- | --- | --- | --- |
| y | number | No | The y position of the Bob. Bob coordinate are relative to the position of the Blitter object. |

**Returns:** [Phaser.GameObjects.Bob](gameobjects-bob.md) - This Bob Game Object.

> Source: [src/gameobjects/blitter/Bob.js#L239](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L239)  
> Since: 3.20.0

---

## setTint

### <instance> setTint(value)

**Description:**

Sets the tint of this Bob.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The tint value used for this Bob. Between 0 and 0xffffff. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Bob](gameobjects-bob.md) - This Bob Game Object.

> Source: [src/gameobjects/blitter/Bob.js#L350](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L350)  
> Since: 3.20.0

---

## setVisible

### <instance> setVisible(value)

**Description:**

Sets the visibility of this Bob.

An invisible Bob will skip rendering.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The visible state of the Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Bob](gameobjects-bob.md) - This Bob Game Object.

> Source: [src/gameobjects/blitter/Bob.js#L311](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/blitter/Bob.js#L311)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [data](#data)

    - [data: object](#data-object)
  + [flipX](#flipx)

    - [flipX: boolean](#flipx-boolean)
  + [flipY](#flipy)

    - [flipY: boolean](#flipy-boolean)
  + [frame](#frame)

    - [frame: Phaser.Textures.Frame](#frame-phasertexturesframe)
  + [parent](#parent)

    - [parent: Phaser.GameObjects.Blitter](#parent-phasergameobjectsblitter)
  + [tint](#tint)

    - [tint: number](#tint-number)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Private Members](#private-members)

  + [\_alpha](#_alpha)

    - [\_alpha: number](#_alpha-number)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
  + [hasTransformComponent](#hastransformcomponent)

    - [hasTransformComponent: boolean](#hastransformcomponent-boolean)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [reset](#reset)

    - [<instance> reset(x, y, [frame])](#instance-resetx-y-frame)
  + [resetFlip](#resetflip)

    - [<instance> resetFlip()](#instance-resetflip)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha(value)](#instance-setalphavalue)
  + [setFlip](#setflip)

    - [<instance> setFlip(x, y)](#instance-setflipx-y)
  + [setFlipX](#setflipx)

    - [<instance> setFlipX(value)](#instance-setflipxvalue)
  + [setFlipY](#setflipy)

    - [<instance> setFlipY(value)](#instance-setflipyvalue)
  + [setFrame](#setframe)

    - [<instance> setFrame([frame])](#instance-setframeframe)
  + [setPosition](#setposition)

    - [<instance> setPosition(x, y)](#instance-setpositionx-y)
  + [setTint](#settint)

    - [<instance> setTint(value)](#instance-settintvalue)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value)](#instance-setvisiblevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)