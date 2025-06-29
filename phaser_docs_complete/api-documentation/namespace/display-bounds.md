# Phaser.Display.Bounds

Scope:
static

> Source: [src/display/bounds/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/index.js#L7)

# Static functions

## CenterOn

### <static> CenterOn(gameObject, x, y)

**Description:**

Positions the Game Object so that it is centered on the given coordinates.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| x | number | No | The horizontal coordinate to position the Game Object on. |
| y | number | No | The vertical coordinate to position the Game Object on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/CenterOn.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/CenterOn.js#L10)  
> Since: 3.0.0

---

## GetBottom

### <static> GetBottom(gameObject)

**Description:**

Returns the bottom coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The bottom coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetBottom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetBottom.js#L7)  
> Since: 3.0.0

---

## GetBounds

### <static> GetBounds(gameObject, [output])

**Description:**

Returns the unrotated bounds of the Game Object as a rectangle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |
| output | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | object | Yes | An object to store the values in. If not provided a new Rectangle will be created. |

**Returns:** [Phaser.Geom.Rectangle](../class/geom-rectangle.md), object - - The bounds of the Game Object.

> Source: [src/display/bounds/GetBounds.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetBounds.js#L13)  
> Since: 3.24.0

---

## GetCenterX

### <static> GetCenterX(gameObject)

**Description:**

Returns the center x coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The center x coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetCenterX.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetCenterX.js#L7)  
> Since: 3.0.0

---

## GetCenterY

### <static> GetCenterY(gameObject)

**Description:**

Returns the center y coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The center y coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetCenterY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetCenterY.js#L7)  
> Since: 3.0.0

---

## GetLeft

### <static> GetLeft(gameObject)

**Description:**

Returns the left coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The left coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetLeft.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetLeft.js#L7)  
> Since: 3.0.0

---

## GetOffsetX

### <static> GetOffsetX(gameObject)

**Description:**

Returns the amount the Game Object is visually offset from its x coordinate.

This is the same as `width * origin.x`.

This value will only be > 0 if `origin.x` is not equal to zero.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The horizontal offset of the Game Object.

> Source: [src/display/bounds/GetOffsetX.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetOffsetX.js#L7)  
> Since: 3.0.0

---

## GetOffsetY

### <static> GetOffsetY(gameObject)

**Description:**

Returns the amount the Game Object is visually offset from its y coordinate.

This is the same as `width * origin.y`.

This value will only be > 0 if `origin.y` is not equal to zero.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The vertical offset of the Game Object.

> Source: [src/display/bounds/GetOffsetY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetOffsetY.js#L7)  
> Since: 3.0.0

---

## GetRight

### <static> GetRight(gameObject)

**Description:**

Returns the right coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The right coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetRight.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetRight.js#L7)  
> Since: 3.0.0

---

## GetTop

### <static> GetTop(gameObject)

**Description:**

Returns the top coordinate from the bounds of the Game Object.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to get the bounds value from. |
| --- | --- | --- | --- |

**Returns:** number - The top coordinate of the bounds of the Game Object.

> Source: [src/display/bounds/GetTop.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/GetTop.js#L7)  
> Since: 3.0.0

---

## SetBottom

### <static> SetBottom(gameObject, value)

**Description:**

Positions the Game Object so that the bottom of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| value | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetBottom.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetBottom.js#L7)  
> Since: 3.0.0

---

## SetCenterX

### <static> SetCenterX(gameObject, x)

**Description:**

Positions the Game Object so that the center top of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| x | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetCenterX.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetCenterX.js#L7)  
> Since: 3.0.0

---

## SetCenterY

### <static> SetCenterY(gameObject, y)

**Description:**

Positions the Game Object so that the center top of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| y | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetCenterY.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetCenterY.js#L7)  
> Since: 3.0.0

---

## SetLeft

### <static> SetLeft(gameObject, value)

**Description:**

Positions the Game Object so that the left of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| value | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetLeft.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetLeft.js#L7)  
> Since: 3.0.0

---

## SetRight

### <static> SetRight(gameObject, value)

**Description:**

Positions the Game Object so that the left of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| value | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetRight.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetRight.js#L7)  
> Since: 3.0.0

---

## SetTop

### <static> SetTop(gameObject, value)

**Description:**

Positions the Game Object so that the top of its bounds aligns with the given coordinate.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object that will be re-positioned. |
| --- | --- | --- | --- |
| value | number | No | The coordinate to position the Game Object bounds on. |

**Returns:** [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The Game Object that was positioned.

> Source: [src/display/bounds/SetTop.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/display/bounds/SetTop.js#L7)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [CenterOn](#centeron)

    - [<static> CenterOn(gameObject, x, y)](#static-centerongameobject-x-y)
  + [GetBottom](#getbottom)

    - [<static> GetBottom(gameObject)](#static-getbottomgameobject)
  + [GetBounds](#getbounds)

    - [<static> GetBounds(gameObject, [output])](#static-getboundsgameobject-output)
  + [GetCenterX](#getcenterx)

    - [<static> GetCenterX(gameObject)](#static-getcenterxgameobject)
  + [GetCenterY](#getcentery)

    - [<static> GetCenterY(gameObject)](#static-getcenterygameobject)
  + [GetLeft](#getleft)

    - [<static> GetLeft(gameObject)](#static-getleftgameobject)
  + [GetOffsetX](#getoffsetx)

    - [<static> GetOffsetX(gameObject)](#static-getoffsetxgameobject)
  + [GetOffsetY](#getoffsety)

    - [<static> GetOffsetY(gameObject)](#static-getoffsetygameobject)
  + [GetRight](#getright)

    - [<static> GetRight(gameObject)](#static-getrightgameobject)
  + [GetTop](#gettop)

    - [<static> GetTop(gameObject)](#static-gettopgameobject)
  + [SetBottom](#setbottom)

    - [<static> SetBottom(gameObject, value)](#static-setbottomgameobject-value)
  + [SetCenterX](#setcenterx)

    - [<static> SetCenterX(gameObject, x)](#static-setcenterxgameobject-x)
  + [SetCenterY](#setcentery)

    - [<static> SetCenterY(gameObject, y)](#static-setcenterygameobject-y)
  + [SetLeft](#setleft)

    - [<static> SetLeft(gameObject, value)](#static-setleftgameobject-value)
  + [SetRight](#setright)

    - [<static> SetRight(gameObject, value)](#static-setrightgameobject-value)
  + [SetTop](#settop)

    - [<static> SetTop(gameObject, value)](#static-settopgameobject-value)

Back to top

©2025[Phaser](https://docs.phaser.io)