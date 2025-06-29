# Matrix3

Phaser.Math.Matrix3

A three-dimensional matrix.

Defaults to the identity matrix when instantiated.

**Constructor**

`new Matrix3([m])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| m | [Phaser.Math.Matrix3](math-matrix3.md) | Yes | Optional Matrix3 to copy values from. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/math/Matrix3.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L12)  
> Since: 3.0.0

# Public Members

## val

### val: Float32Array

**Description:**

The matrix values.

> Source: [src/math/Matrix3.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L31)  
> Since: 3.0.0

---

# Public Methods

## adjoint

### <instance> adjoint()

**Description:**

Calculate the adjoint, or adjugate, of this Matrix.

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L262](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L262)  
> Since: 3.0.0

---

## clone

### <instance> clone()

**Description:**

Make a clone of this Matrix3.

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - A clone of this Matrix3.

> Source: [src/math/Matrix3.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L52)  
> Since: 3.0.0

---

## copy

### <instance> copy(src)

**Description:**

Copy the values of a given Matrix into this Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Matrix3](math-matrix3.md) | No | The Matrix to copy the values from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L80)  
> Since: 3.0.0

---

## determinant

### <instance> determinant()

**Description:**

Calculate the determinant of this Matrix.

**Returns:** number - The determinant of this Matrix.

> Source: [src/math/Matrix3.js#L297](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L297)  
> Since: 3.0.0

---

## fromArray

### <instance> fromArray(a)

**Description:**

Set the values of this Matrix from the given array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | array | No | The array to copy the values from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L136)  
> Since: 3.0.0

---

## fromMat4

### <instance> fromMat4(m)

**Description:**

Copy the values of a given Matrix4 into this Matrix3.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| m | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to copy the values from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L108](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L108)  
> Since: 3.0.0

---

## fromQuat

### <instance> fromQuat(q)

**Description:**

Set the values of this Matrix from the given Quaternion.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| q | [Phaser.Math.Quaternion](math-quaternion.md) | No | The Quaternion to set the values of this Matrix from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L460](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L460)  
> Since: 3.0.0

---

## identity

### <instance> identity()

**Description:**

Reset this Matrix to an identity (default) matrix.

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L163](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L163)  
> Since: 3.0.0

---

## invert

### <instance> invert()

**Description:**

Invert this Matrix.

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L213](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L213)  
> Since: 3.0.0

---

## multiply

### <instance> multiply(src)

**Description:**

Multiply this Matrix by the given Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Matrix3](math-matrix3.md) | No | The Matrix to multiply this Matrix by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L322](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L322)  
> Since: 3.0.0

---

## normalFromMat4

### <instance> normalFromMat4(m)

**Description:**

Set the values of this Matrix3 to be normalized from the given Matrix4.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| m | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to normalize the values from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L510](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L510)  
> Since: 3.0.0

---

## rotate

### <instance> rotate(rad)

**Description:**

Apply a rotation transformation to this Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rad | number | No | The angle in radians to rotate by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L396](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L396)  
> Since: 3.0.0

---

## scale

### <instance> scale(v)

**Description:**

Apply a scale transformation to this Matrix.

Uses the `x` and `y` components of the given Vector to scale the Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L431](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L431)  
> Since: 3.0.0

---

## set

### <instance> set(src)

**Description:**

This method is an alias for `Matrix3.copy`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Matrix3](math-matrix3.md) | No | The Matrix to set the values of this Matrix's from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L65)  
> Since: 3.0.0

---

## translate

### <instance> translate(v)

**Description:**

Translate this Matrix using the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L373](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L373)  
> Since: 3.0.0

---

## transpose

### <instance> transpose()

**Description:**

Transpose this Matrix.

**Returns:** [Phaser.Math.Matrix3](math-matrix3.md) - This Matrix3.

> Source: [src/math/Matrix3.js#L188](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix3.js#L188)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [val](#val)

    - [val: Float32Array](#val-float32array)
* [Public Methods](#public-methods)

  + [adjoint](#adjoint)

    - [<instance> adjoint()](#instance-adjoint)
  + [clone](#clone)

    - [<instance> clone()](#instance-clone)
  + [copy](#copy)

    - [<instance> copy(src)](#instance-copysrc)
  + [determinant](#determinant)

    - [<instance> determinant()](#instance-determinant)
  + [fromArray](#fromarray)

    - [<instance> fromArray(a)](#instance-fromarraya)
  + [fromMat4](#frommat4)

    - [<instance> fromMat4(m)](#instance-frommat4m)
  + [fromQuat](#fromquat)

    - [<instance> fromQuat(q)](#instance-fromquatq)
  + [identity](#identity)

    - [<instance> identity()](#instance-identity)
  + [invert](#invert)

    - [<instance> invert()](#instance-invert)
  + [multiply](#multiply)

    - [<instance> multiply(src)](#instance-multiplysrc)
  + [normalFromMat4](#normalfrommat4)

    - [<instance> normalFromMat4(m)](#instance-normalfrommat4m)
  + [rotate](#rotate)

    - [<instance> rotate(rad)](#instance-rotaterad)
  + [scale](#scale)

    - [<instance> scale(v)](#instance-scalev)
  + [set](#set)

    - [<instance> set(src)](#instance-setsrc)
  + [translate](#translate)

    - [<instance> translate(v)](#instance-translatev)
  + [transpose](#transpose)

    - [<instance> transpose()](#instance-transpose)

Back to top

©2025[Phaser](https://docs.phaser.io)