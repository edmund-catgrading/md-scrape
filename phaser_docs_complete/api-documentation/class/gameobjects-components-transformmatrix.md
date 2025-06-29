# TransformMatrix

Phaser.GameObjects.Components.TransformMatrix

A Matrix used for display transformations for rendering.

It is represented like so:

```
Copy
| a | c | tx |

| b | d | ty |

| 0 | 0 | 1  |


```

**Constructor**

`new TransformMatrix([a], [b], [c], [d], [tx], [ty])`

**Parameters**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| a | number | Yes | 1 | The Scale X value. |
| --- | --- | --- | --- | --- |
| b | number | Yes | 0 | The Skew Y value. |
| c | number | Yes | 0 | The Skew X value. |
| d | number | Yes | 1 | The Scale Y value. |
| tx | number | Yes | 0 | The Translate X value. |
| ty | number | Yes | 0 | The Translate Y value. |

---

**Scope**: static

> Source: [src/gameobjects/components/TransformMatrix.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L11)  
> Since: 3.0.0

# Public Members

## a

### a: number

**Description:**

The Scale X value.

> Source: [src/gameobjects/components/TransformMatrix.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L82)  
> Since: 3.4.0

---

## b

### b: number

**Description:**

The Skew Y value.

> Source: [src/gameobjects/components/TransformMatrix.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L103)  
> Since: 3.4.0

---

## c

### c: number

**Description:**

The Skew X value.

> Source: [src/gameobjects/components/TransformMatrix.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L124)  
> Since: 3.4.0

---

## d

### d: number

**Description:**

The Scale Y value.

> Source: [src/gameobjects/components/TransformMatrix.js#L145](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L145)  
> Since: 3.4.0

---

## decomposedMatrix

### decomposedMatrix: object

**Description:**

The decomposed matrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L57)  
> Since: 3.0.0

---

## e

### e: number

**Description:**

The Translate X value.

> Source: [src/gameobjects/components/TransformMatrix.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L166)  
> Since: 3.11.0

---

## f

### f: number

**Description:**

The Translate Y value.

> Source: [src/gameobjects/components/TransformMatrix.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L187)  
> Since: 3.11.0

---

## matrix

### matrix: Float32Array

**Description:**

The matrix values.

> Source: [src/gameobjects/components/TransformMatrix.js#L48](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L48)  
> Since: 3.0.0

---

## quad

### quad: Float32Array

**Description:**

The temporary quad value cache.

> Source: [src/gameobjects/components/TransformMatrix.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L72)  
> Since: 3.60.0

---

## rotation

### rotation: number

**Description:**

The rotation of the Matrix. Value is in radians.

> Source: [src/gameobjects/components/TransformMatrix.js#L250](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L250)  
> Since: 3.4.0

---

## rotationNormalized

### rotationNormalized: number

**Description:**

The rotation of the Matrix, normalized to be within the Phaser right-handed

clockwise rotation space. Value is in radians.

> Source: [src/gameobjects/components/TransformMatrix.js#L267](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L267)  
> Since: 3.19.0

---

## scaleX

### scaleX: number

**Description:**

The decomposed horizontal scale of the Matrix. This value is always positive.

> Source: [src/gameobjects/components/TransformMatrix.js#L307](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L307)  
> Since: 3.4.0

---

## scaleY

### scaleY: number

**Description:**

The decomposed vertical scale of the Matrix. This value is always positive.

> Source: [src/gameobjects/components/TransformMatrix.js#L324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L324)  
> Since: 3.4.0

---

## tx

### tx: number

**Description:**

The Translate X value.

> Source: [src/gameobjects/components/TransformMatrix.js#L208](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L208)  
> Since: 3.4.0

---

## ty

### ty: number

**Description:**

The Translate Y value.

> Source: [src/gameobjects/components/TransformMatrix.js#L229](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L229)  
> Since: 3.4.0

---

# Public Methods

## applyInverse

### <instance> applyInverse(x, y, [output])

**Description:**

Takes the `x` and `y` values and returns a new position in the `output` vector that is the inverse of

the current matrix with its transformation applied.

Can be used to translate points from world to local space.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x position to translate. |
| --- | --- | --- | --- |
| y | number | No | The y position to translate. |
| output | [Phaser.Math.Vector2](math-vector2.md) | Yes | A Vector2, or point-like object, to store the results in. |

**Returns:** [Phaser.Math.Vector2](math-vector2.md) - The coordinates, inverse-transformed through this matrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L870](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L870)  
> Since: 3.12.0

---

## applyITRS

### <instance> applyITRS(x, y, rotation, scaleX, scaleY)

**Description:**

Apply the identity, translate, rotate and scale operations on the Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal translation. |
| --- | --- | --- | --- |
| y | number | No | The vertical translation. |
| rotation | number | No | The angle of rotation in radians. |
| scaleX | number | No | The horizontal scale. |
| scaleY | number | No | The vertical scale. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L836](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L836)  
> Since: 3.0.0

---

## copyFrom

### <instance> copyFrom(src)

**Description:**

Set the values of this Matrix to copy those of the matrix given.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | The source Matrix to copy from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L628](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L628)  
> Since: 3.11.0

---

## copyFromArray

### <instance> copyFromArray(src)

**Description:**

Set the values of this Matrix to copy those of the array given.

Where array indexes 0, 1, 2, 3, 4 and 5 are mapped to a, b, c, d, e and f.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | array | No | The array of values to set into this matrix. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L652](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L652)  
> Since: 3.11.0

---

## copyToArray

### <instance> copyToArray([out])

**Description:**

Copy the values in this Matrix to the array given.

Where array indexes 0, 1, 2, 3, 4 and 5 are mapped to a, b, c, d, e and f.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| out | array | Yes | The array to copy the matrix values in to. |
| --- | --- | --- | --- |

**Returns:** array - An array where elements 0 to 5 contain the values from this matrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L715](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L715)  
> Since: 3.12.0

---

## copyToContext

### <instance> copyToContext(ctx)

**Description:**

Copy the values from this Matrix to the given Canvas Rendering Context.

This will use the Context.transform method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ctx | CanvasRenderingContext2D | No | The Canvas Rendering Context to copy the matrix values to. |
| --- | --- | --- | --- |

**Returns:** CanvasRenderingContext2D - The Canvas Rendering Context.

> Source: [src/gameobjects/components/TransformMatrix.js#L677](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L677)  
> Since: 3.12.0

---

## decomposeMatrix

### <instance> decomposeMatrix()

**Description:**

Decompose this Matrix into its translation, scale and rotation values using QR decomposition.

The result must be applied in the following order to reproduce the current matrix:

translate -> rotate -> scale

**Returns:** [Phaser.Types.GameObjects.DecomposeMatrixResults](../typedef/types-gameobjects.md) - The decomposed Matrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L777](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L777)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys this Transform Matrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L1094](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L1094)  
> Since: 3.4.0

---

## getCSSMatrix

### <instance> getCSSMatrix()

**Description:**

Returns a string that can be used in a CSS Transform call as a `matrix` property.

**Returns:** string - A string containing the CSS Transform matrix values.

> Source: [src/gameobjects/components/TransformMatrix.js#L1079](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L1079)  
> Since: 3.12.0

---

## getX

### <instance> getX(x, y)

**Description:**

Returns the X component of this matrix multiplied by the given values.

This is the same as `x * a + y * c + e`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x value. |
| --- | --- | --- | --- |
| y | number | No | The y value. |

**Returns:** number - The calculated x value.

> Source: [src/gameobjects/components/TransformMatrix.js#L993](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L993)  
> Since: 3.12.0

---

## getXRound

### <instance> getXRound(x, y, [round])

**Description:**

Returns the X component of this matrix multiplied by the given values.

This is the same as `x * a + y * c + e`, optionally passing via `Math.round`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x value. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y value. |
| round | boolean | Yes | false | Math.round the resulting value? |

**Returns:** number - The calculated x value.

> Source: [src/gameobjects/components/TransformMatrix.js#L1027](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L1027)  
> Since: 3.50.0

---

## getY

### <instance> getY(x, y)

**Description:**

Returns the Y component of this matrix multiplied by the given values.

This is the same as `x * b + y * d + f`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x value. |
| --- | --- | --- | --- |
| y | number | No | The y value. |

**Returns:** number - The calculated y value.

> Source: [src/gameobjects/components/TransformMatrix.js#L1010](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L1010)  
> Since: 3.12.0

---

## getYRound

### <instance> getYRound(x, y, [round])

**Description:**

Returns the Y component of this matrix multiplied by the given values.

This is the same as `x * b + y * d + f`, optionally passing via `Math.round`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x value. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y value. |
| round | boolean | Yes | false | Math.round the resulting value? |

**Returns:** number - The calculated y value.

> Source: [src/gameobjects/components/TransformMatrix.js#L1053](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L1053)  
> Since: 3.50.0

---

## invert

### <instance> invert()

**Description:**

Invert the Matrix.

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L597](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L597)  
> Since: 3.0.0

---

## loadIdentity

### <instance> loadIdentity()

**Description:**

Reset the Matrix to an identity matrix.

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L341](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L341)  
> Since: 3.0.0

---

## multiply

### <instance> multiply(rhs, [out])

**Description:**

Multiply this Matrix by the given Matrix.

If an `out` Matrix is given then the results will be stored in it.

If it is not given, this matrix will be updated in place instead.

Use an `out` Matrix if you do not wish to mutate this matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rhs | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | The Matrix to multiply by. |
| --- | --- | --- | --- |
| out | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | Yes | An optional Matrix to store the results in. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md), [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - Either this TransformMatrix, or the `out` Matrix, if given in the arguments.

> Source: [src/gameobjects/components/TransformMatrix.js#L437](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L437)  
> Since: 3.0.0

---

## multiplyWithOffset

### <instance> multiplyWithOffset(src, offsetX, offsetY)

**Description:**

Multiply this Matrix by the matrix given, including the offset.

The offsetX is added to the tx value: `offsetX * a + offsetY * c + tx`.

The offsetY is added to the ty value: `offsetY * b + offsetY * d + ty`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) | No | The source Matrix to copy from. |
| --- | --- | --- | --- |
| offsetX | number | No | Horizontal offset to factor in to the multiplication. |
| offsetY | number | No | Vertical offset to factor in to the multiplication. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L483](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L483)  
> Since: 3.11.0

---

## rotate

### <instance> rotate(angle)

**Description:**

Rotate the Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| angle | number | No | The angle of rotation in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L407](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L407)  
> Since: 3.0.0

---

## scale

### <instance> scale(x, y)

**Description:**

Scale the Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal scale value. |
| --- | --- | --- | --- |
| y | number | No | The vertical scale value. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L384](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L384)  
> Since: 3.0.0

---

## setQuad

### <instance> setQuad(x, y, xw, yh, [roundPixels], [quad])

**Description:**

Performs the 8 calculations required to create the vertices of

a quad based on this matrix and the given x/y/xw/yh values.

The result is stored in `TransformMatrix.quad`, which is returned

from this method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x value. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y value. |
| xw | number | No |  | The xw value. |
| yh | number | No |  | The yh value. |
| roundPixels | boolean | Yes | false | Pass the results via Math.round? |
| quad | Float32Array | Yes |  | Optional Float32Array to store the results in. Otherwises uses the local quad array. |

**Returns:** Float32Array - The quad Float32Array.

> Source: [src/gameobjects/components/TransformMatrix.js#L906](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L906)  
> Since: 3.60.0

---

## setToContext

### <instance> setToContext(ctx)

**Description:**

Copy the values from this Matrix to the given Canvas Rendering Context.

This will use the Context.setTransform method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| ctx | CanvasRenderingContext2D | No | The Canvas Rendering Context to copy the matrix values to. |
| --- | --- | --- | --- |

**Returns:** CanvasRenderingContext2D - The Canvas Rendering Context.

> Source: [src/gameobjects/components/TransformMatrix.js#L697](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L697)  
> Since: 3.12.0

---

## setTransform

### <instance> setTransform(a, b, c, d, tx, ty)

**Description:**

Set the values of this Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | number | No | The Scale X value. |
| --- | --- | --- | --- |
| b | number | No | The Shear Y value. |
| c | number | No | The Shear X value. |
| d | number | No | The Scale Y value. |
| tx | number | No | The Translate X value. |
| ty | number | No | The Translate Y value. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L748](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L748)  
> Since: 3.0.0

---

## transform

### <instance> transform(a, b, c, d, tx, ty)

**Description:**

Transform the Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | number | No | The Scale X value. |
| --- | --- | --- | --- |
| b | number | No | The Shear Y value. |
| c | number | No | The Shear X value. |
| d | number | No | The Scale Y value. |
| tx | number | No | The Translate X value. |
| ty | number | No | The Translate Y value. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L530](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L530)  
> Since: 3.0.0

---

## transformPoint

### <instance> transformPoint(x, y, [point])

**Description:**

Transform a point in to the local space of this Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the point to transform. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the point to transform. |
| point | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes | Optional Point object to store the transformed coordinates in. |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The Point containing the transformed coordinates.

> Source: [src/gameobjects/components/TransformMatrix.js#L566](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L566)  
> Since: 3.0.0

---

## translate

### <instance> translate(x, y)

**Description:**

Translate the Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal translation value. |
| --- | --- | --- | --- |
| y | number | No | The vertical translation value. |

**Returns:** [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md) - This TransformMatrix.

> Source: [src/gameobjects/components/TransformMatrix.js#L363](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/TransformMatrix.js#L363)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [a](#a)

    - [a: number](#a-number)
  + [b](#b)

    - [b: number](#b-number)
  + [c](#c)

    - [c: number](#c-number)
  + [d](#d)

    - [d: number](#d-number)
  + [decomposedMatrix](#decomposedmatrix)

    - [decomposedMatrix: object](#decomposedmatrix-object)
  + [e](#e)

    - [e: number](#e-number)
  + [f](#f)

    - [f: number](#f-number)
  + [matrix](#matrix)

    - [matrix: Float32Array](#matrix-float32array)
  + [quad](#quad)

    - [quad: Float32Array](#quad-float32array)
  + [rotation](#rotation)

    - [rotation: number](#rotation-number)
  + [rotationNormalized](#rotationnormalized)

    - [rotationNormalized: number](#rotationnormalized-number)
  + [scaleX](#scalex)

    - [scaleX: number](#scalex-number)
  + [scaleY](#scaley)

    - [scaleY: number](#scaley-number)
  + [tx](#tx)

    - [tx: number](#tx-number)
  + [ty](#ty)

    - [ty: number](#ty-number)
* [Public Methods](#public-methods)

  + [applyInverse](#applyinverse)

    - [<instance> applyInverse(x, y, [output])](#instance-applyinversex-y-output)
  + [applyITRS](#applyitrs)

    - [<instance> applyITRS(x, y, rotation, scaleX, scaleY)](#instance-applyitrsx-y-rotation-scalex-scaley)
  + [copyFrom](#copyfrom)

    - [<instance> copyFrom(src)](#instance-copyfromsrc)
  + [copyFromArray](#copyfromarray)

    - [<instance> copyFromArray(src)](#instance-copyfromarraysrc)
  + [copyToArray](#copytoarray)

    - [<instance> copyToArray([out])](#instance-copytoarrayout)
  + [copyToContext](#copytocontext)

    - [<instance> copyToContext(ctx)](#instance-copytocontextctx)
  + [decomposeMatrix](#decomposematrix)

    - [<instance> decomposeMatrix()](#instance-decomposematrix)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [getCSSMatrix](#getcssmatrix)

    - [<instance> getCSSMatrix()](#instance-getcssmatrix)
  + [getX](#getx)

    - [<instance> getX(x, y)](#instance-getxx-y)
  + [getXRound](#getxround)

    - [<instance> getXRound(x, y, [round])](#instance-getxroundx-y-round)
  + [getY](#gety)

    - [<instance> getY(x, y)](#instance-getyx-y)
  + [getYRound](#getyround)

    - [<instance> getYRound(x, y, [round])](#instance-getyroundx-y-round)
  + [invert](#invert)

    - [<instance> invert()](#instance-invert)
  + [loadIdentity](#loadidentity)

    - [<instance> loadIdentity()](#instance-loadidentity)
  + [multiply](#multiply)

    - [<instance> multiply(rhs, [out])](#instance-multiplyrhs-out)
  + [multiplyWithOffset](#multiplywithoffset)

    - [<instance> multiplyWithOffset(src, offsetX, offsetY)](#instance-multiplywithoffsetsrc-offsetx-offsety)
  + [rotate](#rotate)

    - [<instance> rotate(angle)](#instance-rotateangle)
  + [scale](#scale)

    - [<instance> scale(x, y)](#instance-scalex-y)
  + [setQuad](#setquad)

    - [<instance> setQuad(x, y, xw, yh, [roundPixels], [quad])](#instance-setquadx-y-xw-yh-roundpixels-quad)
  + [setToContext](#settocontext)

    - [<instance> setToContext(ctx)](#instance-settocontextctx)
  + [setTransform](#settransform)

    - [<instance> setTransform(a, b, c, d, tx, ty)](#instance-settransforma-b-c-d-tx-ty)
  + [transform](#transform)

    - [<instance> transform(a, b, c, d, tx, ty)](#instance-transforma-b-c-d-tx-ty)
  + [transformPoint](#transformpoint)

    - [<instance> transformPoint(x, y, [point])](#instance-transformpointx-y-point)
  + [translate](#translate)

    - [<instance> translate(x, y)](#instance-translatex-y)

Back to top

©2025[Phaser](https://docs.phaser.io)