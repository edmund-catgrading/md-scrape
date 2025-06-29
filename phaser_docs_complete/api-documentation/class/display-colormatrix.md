# ColorMatrix

Phaser.Display.ColorMatrix

The ColorMatrix class creates a 5x4 matrix that can be used in shaders and graphics

operations. It provides methods required to modify the color values, such as adjusting

the brightness, setting a sepia tone, hue rotation and more.

Use the method `getData` to return a Float32Array containing the current color values.

**Scope**: static

> Source: [src/display/ColorMatrix.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L11)  
> Since: 3.50.0

# Public Members

## alpha

### alpha: number

**Description:**

The value that determines how much of the original color is used

when mixing the colors. A value between 0 (all original) and 1 (all final)

> Source: [src/display/ColorMatrix.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L40)  
> Since: 3.50.0

---

# Private Members

## \_dirty

### \_dirty: boolean

**Description:**

Is the ColorMatrix array dirty?

**Access:** private

> Source: [src/display/ColorMatrix.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L50)  
> Since: 3.50.0

---

## \_matrix

### \_matrix: Float32Array

**Description:**

Internal ColorMatrix array.

**Access:** private

> Source: [src/display/ColorMatrix.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L30)  
> Since: 3.50.0

---

## data

### data: Float32Array

**Description:**

The matrix data as a Float32Array.

Returned by the `getData` method.

**Access:** private

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

> Source: [src/display/ColorMatrix.js#L332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L332)  
> Since: 3.50.0

---

## getData

### <instance> getData()

**Description:**

Gets the ColorMatrix as a Float32Array.

Can be used directly as a 1fv shader uniform value.

**Returns:** Float32Array - The ColorMatrix as a Float32Array.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

> Source: [src/display/ColorMatrix.js#L475](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L475)  
> Since: 3.50.0

---

## reset

### <instance> reset()

**Description:**

Resets the ColorMatrix to default values and also resets

the `alpha` property back to 1.

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

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

**Returns:** [Phaser.Display.ColorMatrix](display-colormatrix.md) - This ColorMatrix instance.

> Source: [src/display/ColorMatrix.js#L424](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L424)  
> Since: 3.50.0

---

# Constants:

# Public Members

## BLACK\_WHITE

### BLACK\_WHITE: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for black\_white operations.

> Source: [src/display/ColorMatrix.js#L575](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L575)  
> Since: 3.60.0

---

## BROWN

### BROWN: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for brown operations.

> Source: [src/display/ColorMatrix.js#L625](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L625)  
> Since: 3.60.0

---

## DESATURATE\_LUMINANCE

### DESATURATE\_LUMINANCE: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for desatured luminance operations.

> Source: [src/display/ColorMatrix.js#L595](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L595)  
> Since: 3.60.0

---

## KODACHROME

### KODACHROME: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for kodachrome operations.

> Source: [src/display/ColorMatrix.js#L645](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L645)  
> Since: 3.60.0

---

## LSD

### LSD: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for lsd operations.

> Source: [src/display/ColorMatrix.js#L615](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L615)  
> Since: 3.60.0

---

## NEGATIVE

### NEGATIVE: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for negative operations.

> Source: [src/display/ColorMatrix.js#L585](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L585)  
> Since: 3.60.0

---

## POLAROID

### POLAROID: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for polaroid shift operations.

> Source: [src/display/ColorMatrix.js#L665](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L665)  
> Since: 3.60.0

---

## SEPIA

### SEPIA: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for sepia operations.

> Source: [src/display/ColorMatrix.js#L605](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L605)  
> Since: 3.60.0

---

## SHIFT\_BGR

### SHIFT\_BGR: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for shift BGR operations.

> Source: [src/display/ColorMatrix.js#L675](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L675)  
> Since: 3.60.0

---

## TECHNICOLOR

### TECHNICOLOR: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for technicolor operations.

> Source: [src/display/ColorMatrix.js#L655](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L655)  
> Since: 3.60.0

---

## VINTAGE

### VINTAGE: Array.<number>

**Description:**

A constant array used by the ColorMatrix class for vintage pinhole operations.

> Source: [src/display/ColorMatrix.js#L635](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/ColorMatrix.js#L635)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [alpha](#alpha)

    - [alpha: number](#alpha-number)
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
* [Constants:](#constants)
* [Public Members](#public-members-1)

  + [BLACK\_WHITE](#black_white)

    - [BLACK\_WHITE: Array.<number>](#black_white-arraynumber)
  + [BROWN](#brown-1)

    - [BROWN: Array.<number>](#brown-arraynumber)
  + [DESATURATE\_LUMINANCE](#desaturate_luminance)

    - [DESATURATE\_LUMINANCE: Array.<number>](#desaturate_luminance-arraynumber)
  + [KODACHROME](#kodachrome-1)

    - [KODACHROME: Array.<number>](#kodachrome-arraynumber)
  + [LSD](#lsd-1)

    - [LSD: Array.<number>](#lsd-arraynumber)
  + [NEGATIVE](#negative-1)

    - [NEGATIVE: Array.<number>](#negative-arraynumber)
  + [POLAROID](#polaroid-1)

    - [POLAROID: Array.<number>](#polaroid-arraynumber)
  + [SEPIA](#sepia-1)

    - [SEPIA: Array.<number>](#sepia-arraynumber)
  + [SHIFT\_BGR](#shift_bgr)

    - [SHIFT\_BGR: Array.<number>](#shift_bgr-arraynumber)
  + [TECHNICOLOR](#technicolor-1)

    - [TECHNICOLOR: Array.<number>](#technicolor-arraynumber)
  + [VINTAGE](#vintage)

    - [VINTAGE: Array.<number>](#vintage-arraynumber)

Back to top

©2025[Phaser](https://docs.phaser.io)



ColorMatrix