# Matrix4

Phaser.Math.Matrix4

A four-dimensional matrix.

Adapted from [gl-matrix](https://github.com/toji/gl-matrix) by toji

and [vecmath](https://github.com/mattdesl/vecmath) by mattdesl

**Constructor**

`new Matrix4([m])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| m | [Phaser.Math.Matrix4](math-matrix4.md) | Yes | Optional Matrix4 to copy values from. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/math/Matrix4.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L15)  
> Since: 3.0.0

# Public Members

## val

### val: Float32Array

**Description:**

The matrix values.

> Source: [src/math/Matrix4.js#L35](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L35)  
> Since: 3.0.0

---

# Public Methods

## adjoint

### <instance> adjoint()

**Description:**

Calculate the adjoint, or adjugate, of this Matrix.

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L418](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L418)  
> Since: 3.0.0

---

## clone

### <instance> clone()

**Description:**

Make a clone of this Matrix4.

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - A clone of this Matrix4.

> Source: [src/math/Matrix4.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L56)  
> Since: 3.0.0

---

## copy

### <instance> copy(src)

**Description:**

Copy the values of a given Matrix into this Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix to copy the values from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L133)  
> Since: 3.0.0

---

## determinant

### <instance> determinant()

**Description:**

Calculate the determinant of this Matrix.

**Returns:** number - The determinant of this Matrix.

> Source: [src/math/Matrix4.js#L470](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L470)  
> Since: 3.0.0

---

## fromArray

### <instance> fromArray(a)

**Description:**

Set the values of this Matrix from the given array.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | Array.<number> | No | The array to copy the values from. Must have at least 16 elements. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L150](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L150)  
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

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1105](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1105)  
> Since: 3.0.0

---

## fromRotationTranslation

### <instance> fromRotationTranslation(q, v)

**Description:**

Set the values of this Matrix from the given rotation Quaternion and translation Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| q | [Phaser.Math.Quaternion](math-quaternion.md) | No | The Quaternion to set rotation from. |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | No | The Vector to set translation from. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1047](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1047)  
> Since: 3.0.0

---

## fromRotationXYTranslation

### <instance> fromRotationXYTranslation(rotation, position, translateFirst)

**Description:**

Takes the rotation and position vectors and builds this Matrix4 from them.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rotation | [Phaser.Math.Vector3](math-vector3.md) | No | The rotation vector. |
| --- | --- | --- | --- |
| position | [Phaser.Math.Vector3](math-vector3.md) | No | The position vector. |
| translateFirst | boolean | No | Should the operation translate then rotate (`true`), or rotate then translate? (`false`) |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1670](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1670)  
> Since: 3.50.0

---

## frustum

### <instance> frustum(left, right, bottom, top, near, far)

**Description:**

Generate a frustum matrix with the given bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| left | number | No | The left bound of the frustum. |
| --- | --- | --- | --- |
| right | number | No | The right bound of the frustum. |
| bottom | number | No | The bottom bound of the frustum. |
| top | number | No | The top bound of the frustum. |
| near | number | No | The near bound of the frustum. |
| far | number | No | The far bound of the frustum. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1161)  
> Since: 3.0.0

---

## getInverse

### <instance> getInverse(m)

**Description:**

Copies the given Matrix4 into this Matrix and then inverses it.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| m | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to invert into this Matrix4. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L324)  
> Since: 3.50.0

---

## getMaxScaleOnAxis

### <instance> getMaxScaleOnAxis()

**Description:**

Returns the maximum axis scale from this Matrix4.

**Returns:** number - The maximum axis scale.

> Source: [src/math/Matrix4.js#L1741](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1741)  
> Since: 3.50.0

---

## identity

### <instance> identity()

**Description:**

Reset this Matrix to an identity (default) matrix.

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L276)  
> Since: 3.0.0

---

## invert

### <instance> invert()

**Description:**

Invert this Matrix.

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L341](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L341)  
> Since: 3.0.0

---

## lookAt

### <instance> lookAt(eye, center, up)

**Description:**

Generate a look-at matrix with the given eye position, focal point, and up axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| eye | [Phaser.Math.Vector3](math-vector3.md) | No | Position of the viewer |
| --- | --- | --- | --- |
| center | [Phaser.Math.Vector3](math-vector3.md) | No | Point the viewer is looking at |
| up | [Phaser.Math.Vector3](math-vector3.md) | No | vec3 pointing up. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1393](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1393)  
> Since: 3.0.0

---

## lookAtRH

### <instance> lookAtRH(eye, target, up)

**Description:**

Generate a right-handed look-at matrix with the given eye position, target and up axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| eye | [Phaser.Math.Vector3](math-vector3.md) | No | Position of the viewer. |
| --- | --- | --- | --- |
| target | [Phaser.Math.Vector3](math-vector3.md) | No | Point the viewer is looking at. |
| up | [Phaser.Math.Vector3](math-vector3.md) | No | vec3 pointing up. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1333](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1333)  
> Since: 3.50.0

---

## makeRotationAxis

### <instance> makeRotationAxis(axis, angle)

**Description:**

Derive a rotation matrix around the given axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| axis | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No | The rotation axis. |
| --- | --- | --- | --- |
| angle | number | No | The rotation angle in radians. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L814](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L814)  
> Since: 3.0.0

---

## multiply

### <instance> multiply(src)

**Description:**

Multiply this Matrix by the given Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix to multiply this Matrix by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L519](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L519)  
> Since: 3.0.0

---

## multiplyLocal

### <instance> multiplyLocal(src)

**Description:**

Multiply the values of this Matrix4 by those given in the `src` argument.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Matrix4](math-matrix4.md) | No | The source Matrix4 that this Matrix4 is multiplied by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L599](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L599)  
> Since: 3.0.0

---

## multiplyMatrices

### <instance> multiplyMatrices(a, b)

**Description:**

Multiplies the two given Matrix4 objects and stores the results in this Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| a | [Phaser.Math.Matrix4](math-matrix4.md) | No | The first Matrix4 to multiply. |
| --- | --- | --- | --- |
| b | [Phaser.Math.Matrix4](math-matrix4.md) | No | The second Matrix4 to multiply. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L654](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L654)  
> Since: 3.50.0

---

## multiplyToMat4

### <instance> multiplyToMat4(src, out)

**Description:**

Multiplies this Matrix4 by the given `src` Matrix4 and stores the results in the `out` Matrix4.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to multiply with this one. |
| --- | --- | --- | --- |
| out | [Phaser.Math.Matrix4](math-matrix4.md) | No | The receiving Matrix. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This `out` Matrix4.

> Source: [src/math/Matrix4.js#L1597](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1597)  
> Since: 3.50.0

---

## ortho

### <instance> ortho(left, right, bottom, top, near, far)

**Description:**

Generate an orthogonal projection matrix with the given bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| left | number | No | The left bound of the frustum. |
| --- | --- | --- | --- |
| right | number | No | The right bound of the frustum. |
| bottom | number | No | The bottom bound of the frustum. |
| top | number | No | The top bound of the frustum. |
| near | number | No | The near bound of the frustum. |
| far | number | No | The far bound of the frustum. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1284](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1284)  
> Since: 3.0.0

---

## perspective

### <instance> perspective(fovy, aspect, near, far)

**Description:**

Generate a perspective projection matrix with the given bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fovy | number | No | Vertical field of view in radians |
| --- | --- | --- | --- |
| aspect | number | No | Aspect ratio. Typically viewport width /height. |
| near | number | No | Near bound of the frustum. |
| far | number | No | Far bound of the frustum. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1205)  
> Since: 3.0.0

---

## perspectiveLH

### <instance> perspectiveLH(width, height, near, far)

**Description:**

Generate a perspective projection matrix with the given bounds.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of the frustum. |
| --- | --- | --- | --- |
| height | number | No | The height of the frustum. |
| near | number | No | Near bound of the frustum. |
| far | number | No | Far bound of the frustum. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1246](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1246)  
> Since: 3.0.0

---

## premultiply

### <instance> premultiply(m)

**Description:**

Multiplies the given Matrix4 object with this Matrix.

This is the same as calling `multiplyMatrices(m, this)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| m | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix4 to multiply with this one. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L637](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L637)  
> Since: 3.50.0

---

## rotate

### <instance> rotate(rad, axis)

**Description:**

Apply a rotation transformation to this Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rad | number | No | The angle in radians to rotate by. |
| --- | --- | --- | --- |
| axis | [Phaser.Math.Vector3](math-vector3.md) | No | The axis to rotate upon. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L846](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L846)  
> Since: 3.0.0

---

## rotateX

### <instance> rotateX(rad)

**Description:**

Rotate this matrix on its X axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rad | number | No | The angle in radians to rotate by. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L930](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L930)  
> Since: 3.0.0

---

## rotateY

### <instance> rotateY(rad)

**Description:**

Rotate this matrix on its Y axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rad | number | No | The angle to rotate by, in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L969](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L969)  
> Since: 3.0.0

---

## rotateZ

### <instance> rotateZ(rad)

**Description:**

Rotate this matrix on its Z axis.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rad | number | No | The angle to rotate by, in radians. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1008](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1008)  
> Since: 3.0.0

---

## scale

### <instance> scale(v)

**Description:**

Apply a scale transformation to this Matrix.

Uses the `x`, `y` and `z` components of the given Vector to scale the Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No | The Vector to scale this Matrix with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L763](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L763)  
> Since: 3.0.0

---

## scaleXYZ

### <instance> scaleXYZ(x, y, z)

**Description:**

Apply a scale transformation to this Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x component. |
| --- | --- | --- | --- |
| y | number | No | The y component. |
| z | number | No | The z component. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L780](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L780)  
> Since: 3.16.0

---

## scaling

### <instance> scaling(x, y, z)

**Description:**

Set the scaling values of this Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x scaling value. |
| --- | --- | --- | --- |
| y | number | No | The y scaling value. |
| z | number | No | The z scaling value. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L250](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L250)  
> Since: 3.0.0

---

## set

### <instance> set(src)

**Description:**

This method is an alias for `Matrix4.copy`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| src | [Phaser.Math.Matrix4](math-matrix4.md) | No | The Matrix to set the values of this Matrix's from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L69)  
> Since: 3.0.0

---

## setValues

### <instance> setValues(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33)

**Description:**

Sets all values of this Matrix4.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| m00 | number | No | The m00 value. |
| --- | --- | --- | --- |
| m01 | number | No | The m01 value. |
| m02 | number | No | The m02 value. |
| m03 | number | No | The m03 value. |
| m10 | number | No | The m10 value. |
| m11 | number | No | The m11 value. |
| m12 | number | No | The m12 value. |
| m13 | number | No | The m13 value. |
| m20 | number | No | The m20 value. |
| m21 | number | No | The m21 value. |
| m22 | number | No | The m22 value. |
| m23 | number | No | The m23 value. |
| m30 | number | No | The m30 value. |
| m31 | number | No | The m31 value. |
| m32 | number | No | The m32 value. |
| m33 | number | No | The m33 value. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4 instance.

> Source: [src/math/Matrix4.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L84)  
> Since: 3.50.0

---

## setWorldMatrix

### <instance> setWorldMatrix(rotation, position, scale, [viewMatrix], [projectionMatrix])

**Description:**

Generate a world matrix from the given rotation, position, scale, view matrix and projection matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rotation | [Phaser.Math.Vector3](math-vector3.md) | No | The rotation of the world matrix. |
| --- | --- | --- | --- |
| position | [Phaser.Math.Vector3](math-vector3.md) | No | The position of the world matrix. |
| scale | [Phaser.Math.Vector3](math-vector3.md) | No | The scale of the world matrix. |
| viewMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | Yes | The view matrix. |
| projectionMatrix | [Phaser.Math.Matrix4](math-matrix4.md) | Yes | The projection matrix. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1560](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1560)  
> Since: 3.0.0

---

## transform

### <instance> transform(position, scale, rotation)

**Description:**

Generates a transform matrix based on the given position, scale and rotation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| position | [Phaser.Math.Vector3](math-vector3.md) | No | The position vector. |
| --- | --- | --- | --- |
| scale | [Phaser.Math.Vector3](math-vector3.md) | No | The scale vector. |
| rotation | [Phaser.Math.Quaternion](math-quaternion.md) | No | The rotation quaternion. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L180)  
> Since: 3.50.0

---

## translate

### <instance> translate(v)

**Description:**

Translate this Matrix using the given Vector.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| v | [Phaser.Math.Vector3](math-vector3.md) | [Phaser.Math.Vector4](math-vector4.md) | No | The Vector to translate this Matrix with. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L724](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L724)  
> Since: 3.0.0

---

## translateXYZ

### <instance> translateXYZ(x, y, z)

**Description:**

Translate this Matrix using the given values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x component. |
| --- | --- | --- | --- |
| y | number | No | The y component. |
| z | number | No | The z component. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L739](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L739)  
> Since: 3.16.0

---

## transpose

### <instance> transpose()

**Description:**

Transpose this Matrix.

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L289](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L289)  
> Since: 3.0.0

---

## xyz

### <instance> xyz(x, y, z)

**Description:**

Set the `x`, `y` and `z` values of this Matrix.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x value. |
| --- | --- | --- | --- |
| y | number | No | The y value. |
| z | number | No | The z value. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L225](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L225)  
> Since: 3.0.0

---

## yawPitchRoll

### <instance> yawPitchRoll(yaw, pitch, roll)

**Description:**

Set the values of this matrix from the given `yaw`, `pitch` and `roll` values.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| yaw | number | No | The yaw value. |
| --- | --- | --- | --- |
| pitch | number | No | The pitch value. |
| roll | number | No | The roll value. |

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L1499](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L1499)  
> Since: 3.0.0

---

## zero

### <instance> zero()

**Description:**

Reset this Matrix.

Sets all values to `0`.

**Returns:** [Phaser.Math.Matrix4](math-matrix4.md) - This Matrix4.

> Source: [src/math/Matrix4.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/math/Matrix4.js#L165)  
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
  + [fromQuat](#fromquat)

    - [<instance> fromQuat(q)](#instance-fromquatq)
  + [fromRotationTranslation](#fromrotationtranslation)

    - [<instance> fromRotationTranslation(q, v)](#instance-fromrotationtranslationq-v)
  + [fromRotationXYTranslation](#fromrotationxytranslation)

    - [<instance> fromRotationXYTranslation(rotation, position, translateFirst)](#instance-fromrotationxytranslationrotation-position-translatefirst)
  + [frustum](#frustum)

    - [<instance> frustum(left, right, bottom, top, near, far)](#instance-frustumleft-right-bottom-top-near-far)
  + [getInverse](#getinverse)

    - [<instance> getInverse(m)](#instance-getinversem)
  + [getMaxScaleOnAxis](#getmaxscaleonaxis)

    - [<instance> getMaxScaleOnAxis()](#instance-getmaxscaleonaxis)
  + [identity](#identity)

    - [<instance> identity()](#instance-identity)
  + [invert](#invert)

    - [<instance> invert()](#instance-invert)
  + [lookAt](#lookat)

    - [<instance> lookAt(eye, center, up)](#instance-lookateye-center-up)
  + [lookAtRH](#lookatrh)

    - [<instance> lookAtRH(eye, target, up)](#instance-lookatrheye-target-up)
  + [makeRotationAxis](#makerotationaxis)

    - [<instance> makeRotationAxis(axis, angle)](#instance-makerotationaxisaxis-angle)
  + [multiply](#multiply)

    - [<instance> multiply(src)](#instance-multiplysrc)
  + [multiplyLocal](#multiplylocal)

    - [<instance> multiplyLocal(src)](#instance-multiplylocalsrc)
  + [multiplyMatrices](#multiplymatrices)

    - [<instance> multiplyMatrices(a, b)](#instance-multiplymatricesa-b)
  + [multiplyToMat4](#multiplytomat4)

    - [<instance> multiplyToMat4(src, out)](#instance-multiplytomat4src-out)
  + [ortho](#ortho)

    - [<instance> ortho(left, right, bottom, top, near, far)](#instance-ortholeft-right-bottom-top-near-far)
  + [perspective](#perspective)

    - [<instance> perspective(fovy, aspect, near, far)](#instance-perspectivefovy-aspect-near-far)
  + [perspectiveLH](#perspectivelh)

    - [<instance> perspectiveLH(width, height, near, far)](#instance-perspectivelhwidth-height-near-far)
  + [premultiply](#premultiply)

    - [<instance> premultiply(m)](#instance-premultiplym)
  + [rotate](#rotate)

    - [<instance> rotate(rad, axis)](#instance-rotaterad-axis)
  + [rotateX](#rotatex)

    - [<instance> rotateX(rad)](#instance-rotatexrad)
  + [rotateY](#rotatey)

    - [<instance> rotateY(rad)](#instance-rotateyrad)
  + [rotateZ](#rotatez)

    - [<instance> rotateZ(rad)](#instance-rotatezrad)
  + [scale](#scale)

    - [<instance> scale(v)](#instance-scalev)
  + [scaleXYZ](#scalexyz)

    - [<instance> scaleXYZ(x, y, z)](#instance-scalexyzx-y-z)
  + [scaling](#scaling)

    - [<instance> scaling(x, y, z)](#instance-scalingx-y-z)
  + [set](#set)

    - [<instance> set(src)](#instance-setsrc)
  + [setValues](#setvalues)

    - [<instance> setValues(m00, m01, m02, m03, m10, m11, m12, m13, m20, m21, m22, m23, m30, m31, m32, m33)](#instance-setvaluesm00-m01-m02-m03-m10-m11-m12-m13-m20-m21-m22-m23-m30-m31-m32-m33)
  + [setWorldMatrix](#setworldmatrix)

    - [<instance> setWorldMatrix(rotation, position, scale, [viewMatrix], [projectionMatrix])](#instance-setworldmatrixrotation-position-scale-viewmatrix-projectionmatrix)
  + [transform](#transform)

    - [<instance> transform(position, scale, rotation)](#instance-transformposition-scale-rotation)
  + [translate](#translate)

    - [<instance> translate(v)](#instance-translatev)
  + [translateXYZ](#translatexyz)

    - [<instance> translateXYZ(x, y, z)](#instance-translatexyzx-y-z)
  + [transpose](#transpose)

    - [<instance> transpose()](#instance-transpose)
  + [xyz](#xyz)

    - [<instance> xyz(x, y, z)](#instance-xyzx-y-z)
  + [yawPitchRoll](#yawpitchroll)

    - [<instance> yawPitchRoll(yaw, pitch, roll)](#instance-yawpitchrollyaw-pitch-roll)
  + [zero](#zero)

    - [<instance> zero()](#instance-zero)

Back to top

©2025[Phaser](https://docs.phaser.io)