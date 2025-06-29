# Vector4

Phaser.Math.Vector4

A representation of a vector in 4D space.

A four-component vector.

**Constructor**

`new Vector4([x], [y], [z], [w])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | Yes | The x component. |
| --- | --- | --- | --- |
| y | number | Yes | The y component. |
| z | number | Yes | The z component. |
| w | number | Yes | The w component. |

---

**Scope**: static

> Source: [src/math/Vector4.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L12)  
> Since: 3.0.0

# Public Members

## w

### w: number

**Description:**

The w component of this Vector.

> Source: [src/math/Vector4.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L64)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x component of this Vector.

> Source: [src/math/Vector4.js#L34](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L34)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y component of this Vector.

> Source: [src/math/Vector4.js#L44](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L44)  
> Since: 3.0.0

---

## z

### z: number

**Description:**

The z component of this Vector.

> Source: [src/math/Vector4.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L54)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(v)

**Description:**

Add a given Vector to this Vector. Addition is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L173](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L173)  
> Since: 3.0.0

---

## clone

### <instance> clone()

**Description:**

Make a clone of this Vector4.

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - A clone of this Vector4.

> Source: [src/math/Vector4.js#L90](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L90)  
> Since: 3.0.0

---

## copy

### <instance> copy(src)

**Description:**

Copy the components of a given Vector into this Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Vector4](math-vector4.md) | No | The Vector to copy the components from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L103)  
> Since: 3.0.0

---

## distance

### <instance> distance(v)

**Description:**

Calculate the distance between this Vector and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No |
| --- | --- | --- | --- |

**Returns:** number - The distance from this Vector to the given Vector.

> Source: [src/math/Vector4.js#L389](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L389)  
> Since: 3.0.0

---

## distanceSq

### <instance> distanceSq(v)

**Description:**

Calculate the distance between this Vector and the given Vector, squared.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No |
| --- | --- | --- | --- |

**Returns:** number - The distance from this Vector to the given Vector, squared.

> Source: [src/math/Vector4.js#L409](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L409)  
> Since: 3.0.0

---

## divide

### <instance> divide(v)

**Description:**

Perform a component-wise division between this Vector and the given Vector.

Divides this Vector by the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L367](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L367)  
> Since: 3.0.0

---

## dot

### <instance> dot(v)

**Description:**

Calculate the dot product of this Vector and the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector4](math-vector4.md) | No | The Vector4 to dot product with this Vector4. |
| --- | --- | --- | --- |

**Returns:** number - The dot product of this Vector and the given Vector.

> Source: [src/math/Vector4.js#L300](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L300)  
> Since: 3.0.0

---

## equals

### <instance> equals(v)

**Description:**

Check whether this Vector is equal to a given Vector.

Performs a strict quality check against each Vector's components.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector4](math-vector4.md) | No | The vector to check equality with. |
| --- | --- | --- | --- |

**Returns:** boolean - A boolean indicating whether the two Vectors are equal or not.

> Source: [src/math/Vector4.js#L123](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L123)  
> Since: 3.0.0

---

## length

### <instance> length()

**Description:**

Calculate the length (or magnitude) of this Vector.

**Returns:** number - The length of this Vector.

> Source: [src/math/Vector4.js#L233](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L233)  
> Since: 3.0.0

---

## lengthSq

### <instance> lengthSq()

**Description:**

Calculate the length of this Vector squared.

**Returns:** number - The length of this Vector, squared.

> Source: [src/math/Vector4.js#L251](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L251)  
> Since: 3.0.0

---

## lerp

### <instance> lerp(v, [t])

**Description:**

Linearly interpolate between this Vector and the given Vector.

Interpolates this Vector towards the given Vector.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| v | [Phaser.Math.Vector4](math-vector4.md) | No |  | The Vector4 to interpolate towards. |
| --- | --- | --- | --- | --- |
| t | number | Yes | 0 | The interpolation percentage, between 0 and 1. |

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L315](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L315)  
> Since: 3.0.0

---

## multiply

### <instance> multiply(v)

**Description:**

Perform a component-wise multiplication between this Vector and the given Vector.

Multiplies this Vector by the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L345](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L345)  
> Since: 3.0.0

---

## negate

### <instance> negate()

**Description:**

Negate the `x`, `y`, `z` and `w` components of this Vector.

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L429](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L429)  
> Since: 3.0.0

---

## normalize

### <instance> normalize()

**Description:**

Normalize this Vector.

Makes the vector a unit length vector (magnitude of 1) in the same direction.

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L269](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L269)  
> Since: 3.0.0

---

## reset

### <instance> reset()

**Description:**

Make this Vector the zero vector (0, 0, 0, 0).

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L507](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L507)  
> Since: 3.0.0

---

## scale

### <instance> scale(scale)

**Description:**

Scale this Vector by the given value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scale | number | No | The value to scale this Vector by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L213](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L213)  
> Since: 3.0.0

---

## set

### <instance> set(x, y, z, w)

**Description:**

Set the `x`, `y`, `z` and `w` components of the this Vector to the given `x`, `y`, `z` and `w` values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | object | No | The x value to set for this Vector, or an object containing x, y, z and w components. |
| --- | --- | --- | --- |
| y | number | No | The y value to set for this Vector. |
| z | number | No | The z value to set for this Vector. |
| w | number | No | The z value to set for this Vector. |

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L140)  
> Since: 3.0.0

---

## subtract

### <instance> subtract(v)

**Description:**

Subtract the given Vector from this Vector. Subtraction is component-wise.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector2](math-vector2.md) | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L193)  
> Since: 3.0.0

---

## transformMat4

### <instance> transformMat4(mat)

**Description:**

Transform this Vector with the given Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mat | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to transform this Vector4 with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L447](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L447)  
> Since: 3.0.0

---

## transformQuat

### <instance> transformQuat(q)

**Description:**

Transform this Vector with the given Quaternion.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| q | [Phaser.Math.Quaternion](math-quaternion.md) | No | The Quaternion to transform this Vector with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Vector4](math-vector4.md) - This Vector4.

> Source: [src/math/Vector4.js#L473](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Vector4.js#L473)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [w](#w)

    - [w: number](#w-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
  + [z](#z)

    - [z: number](#z-number)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(v)](#instance-addv)
  + [clone](#clone)

    - [<instance> clone()](#instance-clone)
  + [copy](#copy)

    - [<instance> copy(src)](#instance-copysrc)
  + [distance](#distance)

    - [<instance> distance(v)](#instance-distancev)
  + [distanceSq](#distancesq)

    - [<instance> distanceSq(v)](#instance-distancesqv)
  + [divide](#divide)

    - [<instance> divide(v)](#instance-dividev)
  + [dot](#dot)

    - [<instance> dot(v)](#instance-dotv)
  + [equals](#equals)

    - [<instance> equals(v)](#instance-equalsv)
  + [length](#length)

    - [<instance> length()](#instance-length)
  + [lengthSq](#lengthsq)

    - [<instance> lengthSq()](#instance-lengthsq)
  + [lerp](#lerp)

    - [<instance> lerp(v, [t])](#instance-lerpv-t)
  + [multiply](#multiply)

    - [<instance> multiply(v)](#instance-multiplyv)
  + [negate](#negate)

    - [<instance> negate()](#instance-negate)
  + [normalize](#normalize)

    - [<instance> normalize()](#instance-normalize)
  + [reset](#reset)

    - [<instance> reset()](#instance-reset)
  + [scale](#scale)

    - [<instance> scale(scale)](#instance-scalescale)
  + [set](#set)

    - [<instance> set(x, y, z, w)](#instance-setx-y-z-w)
  + [subtract](#subtract)

    - [<instance> subtract(v)](#instance-subtractv)
  + [transformMat4](#transformmat4)

    - [<instance> transformMat4(mat)](#instance-transformmat4mat)
  + [transformQuat](#transformquat)

    - [<instance> transformQuat(q)](#instance-transformquatq)

Back to top

©2025[Phaser](https://docs.phaser.io)