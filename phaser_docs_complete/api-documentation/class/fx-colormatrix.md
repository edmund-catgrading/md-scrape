# ColorMatrix

Phaser.FX.ColorMatrix

The ColorMatrix FX Controller.

This FX controller manages the color matrix effect for a Game Object.

The color matrix effect is a visual technique that involves manipulating the colors of an image

or scene using a mathematical matrix. This process can adjust hue, saturation, brightness, and contrast,

allowing developers to create various stylistic appearances or mood settings within the game.

Common applications include simulating different lighting conditions, applying color filters,

or achieving a specific visual style.

A ColorMatrix effect is added to a Game Object via the FX component:

```
Copy
const sprite = this.add.sprite();



sprite.preFX.addColorMatrix();

sprite.postFX.addColorMatrix();


```

**Constructor**

`new ColorMatrix(gameObject)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | A reference to the Game Object that has this fx. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Display.ColorMatrix](display-colormatrix.md)

> Source: [src/fx/ColorMatrix.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/ColorMatrix.js#L11)  
> Since: 3.60.0

# Public Members

## active

### active: boolean

**Description:**

Toggle this boolean to enable or disable this effect,

without removing and adding it from the Game Object.

> Source: [src/fx/ColorMatrix.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/ColorMatrix.js#L68)  
> Since: 3.60.0

---

## alpha

### alpha: number

**Description:**

The value that determines how much of the original color is used

when mixing the colors. A value between 0 (all original) and 1 (all final)

**Inherits:** [Phaser.Display.ColorMatrix#alpha](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L40)  
> Since: 3.50.0

---

## gameObject

### gameObject: [Phaser.GameObjects.GameObject](gameobjects-gameobject.md)

**Description:**

A reference to the Game Object that owns this effect.

> Source: [src/fx/ColorMatrix.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/ColorMatrix.js#L59)  
> Since: 3.60.0

---

## type

### type: number

**Description:**

The FX\_CONST type of this effect.

> Source: [src/fx/ColorMatrix.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/fx/ColorMatrix.js#L50)  
> Since: 3.60.0

---

# Private Members

## \_dirty

### \_dirty: boolean

**Description:**

Is the ColorMatrix array dirty?

**Access:** private

**Inherits:** [Phaser.Display.ColorMatrix#\_dirty](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L50)  
> Since: 3.50.0

---

## \_matrix

### \_matrix: Float32Array

**Description:**

Internal ColorMatrix array.

**Access:** private

**Inherits:** [Phaser.Display.ColorMatrix#\_matrix](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L30)  
> Since: 3.50.0

---

## data

### data: Float32Array

**Description:**

The matrix data as a Float32Array.

Returned by the `getData` method.

**Access:** private

**Inherits:** [Phaser.Display.ColorMatrix#data](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L60)  
> Since: 3.50.0

---

# Public Methods

## blackWhite

### <instance> blackWhite([multiply])

**Description:**

Sets this ColorMatrix to be black and white.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#blackWhite](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L271](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L271)  
> Since: 3.50.0

---

## brightness

### <instance> brightness([value], [multiply])

**Description:**

Changes the brightness of this ColorMatrix by the given amount.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The amount of brightness to apply to this ColorMatrix. Between 0 (black) and 1. |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#brightness](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L150)  
> Since: 3.50.0

---

## brown

### <instance> brown([multiply])

**Description:**

Applies a brown tone to this ColorMatrix.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#brown](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L407](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L407)  
> Since: 3.50.0

---

## contrast

### <instance> contrast([value], [multiply])

**Description:**

Change the contrast of this ColorMatrix by the amount given.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The amount of contrast to apply to this ColorMatrix. |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#contrast](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L288](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L288)  
> Since: 3.50.0

---

## desaturateLuminance

### <instance> desaturateLuminance([multiply])

**Description:**

Apply a desaturated luminance to this ColorMatrix.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#desaturateLuminance](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L332)  
> Since: 3.50.0

---

## getData

### <instance> getData()

**Description:**

Gets the ColorMatrix as a Float32Array.

Can be used directly as a 1fv shader uniform value.

**Returns:** Float32Array - The ColorMatrix as a Float32Array.

**Inherits:** [Phaser.Display.ColorMatrix#getData](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L121](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L121)  
> Since: 3.50.0

---

## grayscale

### <instance> grayscale([value], [multiply])

**Description:**

Sets this ColorMatrix to be grayscale.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 1 | The grayscale scale (0 is black). |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#grayscale](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L252)  
> Since: 3.50.0

---

## hue

### <instance> hue([rotation], [multiply])

**Description:**

Rotates the hues of this ColorMatrix by the value given.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| rotation | number | Yes | 0 | The amount of hue rotation to apply to this ColorMatrix, in degrees. |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#hue](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L220](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L220)  
> Since: 3.50.0

---

## kodachrome

### <instance> kodachrome([multiply])

**Description:**

Applies a kodachrome color effect to this ColorMatrix.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#kodachrome](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L441](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L441)  
> Since: 3.50.0

---

## lsd

### <instance> lsd([multiply])

**Description:**

Applies a trippy color tone to this ColorMatrix.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#lsd](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L390](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L390)  
> Since: 3.50.0

---

## multiply

### <instance> multiply(a, [multiply])

**Description:**

Multiplies the two given matrices.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| a | Array.<number> | No |  | The 5x4 array to multiply with ColorMatrix.\_matrix. |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#multiply](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L509](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L509)  
> Since: 3.50.0

---

## negative

### <instance> negative([multiply])

**Description:**

Converts this ColorMatrix to have negative values.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#negative](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L315](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L315)  
> Since: 3.50.0

---

## night

### <instance> night([intensity], [multiply])

**Description:**

Applies a night vision tone to this ColorMatrix.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| intensity | number | Yes | 0.1 | The intensity of this effect. |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#night](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L366](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L366)  
> Since: 3.50.0

---

## polaroid

### <instance> polaroid([multiply])

**Description:**

Applies a polaroid color effect to this ColorMatrix.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#polaroid](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L475](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L475)  
> Since: 3.50.0

---

## reset

### <instance> reset()

**Description:**

Resets the ColorMatrix to default values and also resets

the `alpha` property back to 1.

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#reset](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L94](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L94)  
> Since: 3.50.0

---

## saturate

### <instance> saturate([value], [multiply])

**Description:**

Changes the saturation of this ColorMatrix by the given amount.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | Yes | 0 | The amount of saturation to apply to this ColorMatrix. |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#saturate](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L176)  
> Since: 3.50.0

---

## saturation

### <instance> saturation([multiply])

**Description:**

Desaturates this ColorMatrix (removes color from it).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#saturation](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L203](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L203)  
> Since: 3.50.0

---

## sepia

### <instance> sepia([multiply])

**Description:**

Applies a sepia tone to this ColorMatrix.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#sepia](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L349](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L349)  
> Since: 3.50.0

---

## set

### <instance> set(value)

**Description:**

Sets this ColorMatrix from the given array of color values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | Array.<number> | Float32Array | No | The ColorMatrix values to set. Must have 20 elements. |
| --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#set](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L75)  
> Since: 3.50.0

---

## shiftToBGR

### <instance> shiftToBGR([multiply])

**Description:**

Shifts the values of this ColorMatrix into BGR order.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#shiftToBGR](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L492](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L492)  
> Since: 3.50.0

---

## technicolor

### <instance> technicolor([multiply])

**Description:**

Applies a technicolor color effect to this ColorMatrix.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#technicolor](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L458](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L458)  
> Since: 3.50.0

---

## vintagePinhole

### <instance> vintagePinhole([multiply])

**Description:**

Applies a vintage pinhole color effect to this ColorMatrix.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| multiply | boolean | Yes | false | Multiply the resulting ColorMatrix (`true`), or set it (`false`) ? |
| --- | --- | --- | --- | --- |

**Returns:** [Phaser.FX.ColorMatrix](fx-colormatrix.md) - This ColorMatrix instance.

**Inherits:** [Phaser.Display.ColorMatrix#vintagePinhole](display-colormatrix.md)

> Source: [src/display/ColorMatrix.js#L424](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L424)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
  + [gameObject](#gameobject)

    - [gameObject: Phaser.GameObjects.GameObject](#gameobject-phasergameobjectsgameobject)
  + [type](#type)

    - [type: number](#type-number)
* [Private Members](#private-members)

  + [\_dirty](#_dirty)

    - [\_dirty: boolean](#_dirty-boolean)
  + [\_matrix](#_matrix)

    - [\_matrix: Float32Array](#_matrix-float32array)
  + [data](#data)

    - [data: Float32Array](#data-float32array)
* [Public Methods](#public-methods)

  + [blackWhite](#blackwhite)

    - [<instance> blackWhite([multiply])](#instance-blackwhitemultiply)
  + [brightness](#brightness)

    - [<instance> brightness([value], [multiply])](#instance-brightnessvalue-multiply)
  + [brown](#brown)

    - [<instance> brown([multiply])](#instance-brownmultiply)
  + [contrast](#contrast)

    - [<instance> contrast([value], [multiply])](#instance-contrastvalue-multiply)
  + [desaturateLuminance](#desaturateluminance)

    - [<instance> desaturateLuminance([multiply])](#instance-desaturateluminancemultiply)
  + [getData](#getdata)

    - [<instance> getData()](#instance-getdata)
  + [grayscale](#grayscale)

    - [<instance> grayscale([value], [multiply])](#instance-grayscalevalue-multiply)
  + [hue](#hue)

    - [<instance> hue([rotation], [multiply])](#instance-huerotation-multiply)
  + [kodachrome](#kodachrome)

    - [<instance> kodachrome([multiply])](#instance-kodachromemultiply)
  + [lsd](#lsd)

    - [<instance> lsd([multiply])](#instance-lsdmultiply)
  + [multiply](#multiply)

    - [<instance> multiply(a, [multiply])](#instance-multiplya-multiply)
  + [negative](#negative)

    - [<instance> negative([multiply])](#instance-negativemultiply)
  + [night](#night)

    - [<instance> night([intensity], [multiply])](#instance-nightintensity-multiply)
  + [polaroid](#polaroid)

    - [<instance> polaroid([multiply])](#instance-polaroidmultiply)
  + [reset](#reset)

    - [<instance> reset()](#instance-reset)
  + [saturate](#saturate)

    - [<instance> saturate([value], [multiply])](#instance-saturatevalue-multiply)
  + [saturation](#saturation)

    - [<instance> saturation([multiply])](#instance-saturationmultiply)
  + [sepia](#sepia)

    - [<instance> sepia([multiply])](#instance-sepiamultiply)
  + [set](#set)

    - [<instance> set(value)](#instance-setvalue)
  + [shiftToBGR](#shifttobgr)

    - [<instance> shiftToBGR([multiply])](#instance-shifttobgrmultiply)
  + [technicolor](#technicolor)

    - [<instance> technicolor([multiply])](#instance-technicolormultiply)
  + [vintagePinhole](#vintagepinhole)

    - [<instance> vintagePinhole([multiply])](#instance-vintagepinholemultiply)

Back to top

©2025[Phaser](https://docs.phaser.io)