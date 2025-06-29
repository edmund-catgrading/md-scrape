# Light

Phaser.GameObjects.Light

A 2D Light.

These are created by the [Phaser.GameObjects.LightsManager](Phaser.GameObjects.LightsManager.md), available from within a scene via `this.lights`.

Any Game Objects using the Light2D pipeline will then be affected by these Lights as long as they have a normal map.

They can also simply be used to represent a point light for your own purposes.

Lights cannot be added to Containers. They are designed to exist in the root of a Scene.

**Constructor**

`new Light(x, y, radius, r, g, b, intensity)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of the light. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of the light. |
| radius | number | No | The radius of the light. |
| r | number | No | The red color of the light. A value between 0 and 1. |
| g | number | No | The green color of the light. A value between 0 and 1. |
| b | number | No | The blue color of the light. A value between 0 and 1. |
| intensity | number | No | The intensity of the light. |

---

**Scope**: static

**Extends**

> [Phaser.Geom.Circle](geom-circle.md)  
> [Phaser.GameObjects.Components.Origin](../namespace/gameobjects-components-origin.md)  
> [Phaser.GameObjects.Components.ScrollFactor](../namespace/gameobjects-components-scrollfactor.md)  
> [Phaser.GameObjects.Components.Visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/lights/Light.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L13)  
> Since: 3.0.0

# Public Members

## bottom

### bottom: number

**Description:**

The bottom position of the Circle.

**Inherits:** [Phaser.Geom.Circle#bottom](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L346](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L346)  
> Since: 3.0.0

---

## cameraFilter

### cameraFilter: number

**Description:**

A bitmask that controls if this Game Object is drawn by a Camera or not.

Not usually set directly, instead call `Camera.ignore`, however you can

set this property directly using the Camera.id property:

> Source: [src/gameobjects/lights/Light.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L89)  
> Since: 3.0.0

---

## color

### color: [Phaser.Display.RGB](display-rgb.md)

**Description:**

The color of the light.

> Source: [src/gameobjects/lights/Light.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L59)  
> Since: 3.50.0

---

## diameter

### diameter: number

**Description:**

The diameter of the Circle.

**Inherits:** [Phaser.Geom.Circle#diameter](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L261](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L261)  
> Since: 3.0.0

---

## displayHeight

### displayHeight: number

**Description:**

The height of this Light Game Object. This is the same as `Light.diameter`.

> Source: [src/gameobjects/lights/Light.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L130)  
> Since: 3.60.0

---

## displayOriginX

### displayOriginX: number

**Description:**

The horizontal display origin of this Game Object.

The origin is a normalized value between 0 and 1.

The displayOrigin is a pixel value, based on the size of the Game Object combined with the origin.

**Inherits:** [Phaser.GameObjects.Components.Origin#displayOriginX](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L64)  
> Since: 3.0.0

---

## displayOriginY

### displayOriginY: number

**Description:**

The vertical display origin of this Game Object.

The origin is a normalized value between 0 and 1.

The displayOrigin is a pixel value, based on the size of the Game Object combined with the origin.

**Inherits:** [Phaser.GameObjects.Components.Origin#displayOriginY](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L88)  
> Since: 3.0.0

---

## displayWidth

### displayWidth: number

**Description:**

The width of this Light Game Object. This is the same as `Light.diameter`.

> Source: [src/gameobjects/lights/Light.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L109)  
> Since: 3.60.0

---

## height

### height: number

**Description:**

The height of this Light Game Object. This is the same as `Light.diameter`.

> Source: [src/gameobjects/lights/Light.js#L172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L172)  
> Since: 3.60.0

---

## intensity

### intensity: number

**Description:**

The intensity of the light.

> Source: [src/gameobjects/lights/Light.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L68)  
> Since: 3.50.0

---

## left

### left: number

**Description:**

The left position of the Circle.

**Inherits:** [Phaser.Geom.Circle#left](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L283](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L283)  
> Since: 3.0.0

---

## originX

### originX: number

**Description:**

The horizontal origin of this Game Object.

The origin maps the relationship between the size and position of the Game Object.

The default value is 0.5, meaning all Game Objects are positioned based on their center.

Setting the value to 0 means the position now relates to the left of the Game Object.

Set this value with `setOrigin()`.

**Inherits:** [Phaser.GameObjects.Components.Origin#originX](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L30](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L30)  
> Since: 3.0.0

---

## originY

### originY: number

**Description:**

The vertical origin of this Game Object.

The origin maps the relationship between the size and position of the Game Object.

The default value is 0.5, meaning all Game Objects are positioned based on their center.

Setting the value to 0 means the position now relates to the top of the Game Object.

Set this value with `setOrigin()`.

**Inherits:** [Phaser.GameObjects.Components.Origin#originY](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L45)  
> Since: 3.0.0

---

## radius

### radius: number

**Description:**

The radius of the Circle.

**Inherits:** [Phaser.Geom.Circle#radius](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L239](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L239)  
> Since: 3.0.0

---

## renderFlags

### renderFlags: number

**Description:**

The flags that are compared against `RENDER_MASK` to determine if this Game Object will render or not.

The bits are 0001 | 0010 | 0100 | 1000 set by the components Visible, Alpha, Transform and Texture respectively.

If those components are not used by your custom class then you can use this bitmask as you wish.

> Source: [src/gameobjects/lights/Light.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L77)  
> Since: 3.0.0

---

## right

### right: number

**Description:**

The right position of the Circle.

**Inherits:** [Phaser.Geom.Circle#right](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L304](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L304)  
> Since: 3.0.0

---

## scrollFactorX

### scrollFactorX: number

**Description:**

The horizontal scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#scrollFactorX](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L16)  
> Since: 3.0.0

---

## scrollFactorY

### scrollFactorY: number

**Description:**

The vertical scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#scrollFactorY](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L40)  
> Since: 3.0.0

---

## top

### top: number

**Description:**

The top position of the Circle.

**Inherits:** [Phaser.Geom.Circle#top](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L325](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L325)  
> Since: 3.0.0

---

## type

### type: number

**Description:**

The geometry constant type of this object: `GEOM_CONST.CIRCLE`.

Used for fast type comparisons.

**Inherits:** [Phaser.Geom.Circle#type](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L41](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L41)  
> Since: 3.19.0

---

## visible

### visible: boolean

**Description:**

The visible state of the Game Object.

An invisible Game Object will skip rendering, but will still process update logic.

**Inherits:** [Phaser.GameObjects.Components.Visible#visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L31)  
> Since: 3.0.0

---

## width

### width: number

**Description:**

The width of this Light Game Object. This is the same as `Light.diameter`.

> Source: [src/gameobjects/lights/Light.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L151)  
> Since: 3.60.0

---

## x

### x: number

**Description:**

The x position of the center of the circle.

**Inherits:** [Phaser.Geom.Circle#x](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L52](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L52)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y position of the center of the circle.

**Inherits:** [Phaser.Geom.Circle#y](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L62](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L62)  
> Since: 3.0.0

---

# Private Members

## \_diameter

### \_diameter: number

**Description:**

The internal diameter of the circle.

**Access:** private

**Inherits:** [Phaser.Geom.Circle#\_diameter](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L82)  
> Since: 3.0.0

---

## \_originComponent

### \_originComponent: boolean

**Description:**

A property indicating that a Game Object has this component.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Origin#\_originComponent](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L19)  
> Since: 3.2.0

---

## \_radius

### \_radius: number

**Description:**

The internal radius of the circle.

**Access:** private

**Inherits:** [Phaser.Geom.Circle#\_radius](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L72)  
> Since: 3.0.0

---

## \_visible

### \_visible: boolean

**Description:**

Private internal value. Holds the visible value.

**Access:** private

**Inherits:** [Phaser.GameObjects.Components.Visible#\_visible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L20](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L20)  
> Since: 3.0.0

---

# Public Methods

## contains

### <instance> contains(x, y)

**Description:**

Check to see if the Circle contains the given x / y coordinates.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate to check within the circle. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate to check within the circle. |

**Returns:** boolean - True if the coordinates are within the circle, otherwise false.

**Inherits:** [Phaser.Geom.Circle#contains](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L93)  
> Since: 3.0.0

---

## getPoint

### <instance> getPoint(position, [out])

**Description:**

Returns a Point object containing the coordinates of a point on the circumference of the Circle

based on the given angle normalized to the range 0 to 1. I.e. a value of 0.5 will give the point

at 180 degrees around the circle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| position | number | No | A value between 0 and 1, where 0 equals 0 degrees, 0.5 equals 180 degrees and 1 equals 360 around the circle. |
| --- | --- | --- | --- |
| out | [Phaser.Geom.Point](geom-point.md) | object | Yes | An object to store the return values in. If not given a Point object will be created. |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point, or point-like object, containing the coordinates of the point around the circle.

**Inherits:** [Phaser.Geom.Circle#getPoint](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L109)  
> Since: 3.0.0

---

## getPoints

### <instance> getPoints(quantity, [stepRate], [output])

**Description:**

Returns an array of Point objects containing the coordinates of the points around the circumference of the Circle,

based on the given quantity or stepRate values.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| quantity | number | No | The amount of points to return. If a falsey value the quantity will be derived from the `stepRate` instead. |
| --- | --- | --- | --- |
| stepRate | number | Yes | Sets the quantity by getting the circumference of the circle and dividing it by the stepRate. |
| output | array | Array.<[Phaser.Geom.Point](geom-point.md)> | Yes | An array to insert the points in to. If not provided a new array will be created. |

**Returns:** array, Array.<[Phaser.Geom.Point](geom-point.md)> - An array of Point objects pertaining to the points around the circumference of the circle.

**Inherits:** [Phaser.Geom.Circle#getPoints](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L129](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L129)  
> Since: 3.0.0

---

## getRandomPoint

### <instance> getRandomPoint([point])

**Description:**

Returns a uniformly distributed random point from anywhere within the Circle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Geom.Point](geom-point.md) | object | Yes | A Point or point-like object to set the random `x` and `y` values in. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Geom.Point](geom-point.md), object - A Point object with the random values set in the `x` and `y` properties.

**Inherits:** [Phaser.Geom.Circle#getRandomPoint](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L149)  
> Since: 3.0.0

---

## isEmpty

### <instance> isEmpty()

**Description:**

Checks to see if the Circle is empty: has a radius of zero.

**Returns:** boolean - True if the Circle is empty, otherwise false.

**Inherits:** [Phaser.Geom.Circle#isEmpty](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L226](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L226)  
> Since: 3.0.0

---

## setColor

### <instance> setColor(rgb)

**Description:**

Set the color of the light from a single integer RGB value.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| rgb | number | No | The integer RGB color of the light. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Light object.

> Source: [src/gameobjects/lights/Light.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L209)  
> Since: 3.0.0

---

## setDisplayOrigin

### <instance> setDisplayOrigin([x], [y])

**Description:**

Sets the display origin of this Game Object.

The difference between this and setting the origin is that you can use pixel values for setting the display origin.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal display origin value. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical display origin value. If not defined it will be set to the value of `x`. |

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setDisplayOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L159)  
> Since: 3.0.0

---

## setEmpty

### <instance> setEmpty()

**Description:**

Sets this Circle to be empty with a radius of zero.

Does not change its position.

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Circle object.

**Inherits:** [Phaser.Geom.Circle#setEmpty](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L188](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L188)  
> Since: 3.0.0

---

## setIntensity

### <instance> setIntensity(intensity)

**Description:**

Set the intensity of the light.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| intensity | number | No | The intensity of the light. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Light object.

> Source: [src/gameobjects/lights/Light.js#L228](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L228)  
> Since: 3.0.0

---

## setOrigin

### <instance> setOrigin([x], [y])

**Description:**

Sets the origin of this Game Object.

The values are given in the range 0 to 1.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0.5 | The horizontal origin value. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical origin value. If not defined it will be set to the value of `x`. |

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L112)  
> Since: 3.0.0

---

## setOriginFromFrame

### <instance> setOriginFromFrame()

**Description:**

Sets the origin of this Game Object based on the Pivot values in its Frame.

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#setOriginFromFrame](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L136)  
> Since: 3.0.0

---

## setPosition

### <instance> setPosition([x], [y])

**Description:**

Sets the position of this Circle.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of the center of the circle. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y position of the center of the circle. |

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Circle object.

**Inherits:** [Phaser.Geom.Circle#setPosition](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L205](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L205)  
> Since: 3.0.0

---

## setRadius

### <instance> setRadius(radius)

**Description:**

Set the radius of the light.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| radius | number | No | The radius of the light. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Light object.

> Source: [src/gameobjects/lights/Light.js#L245](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L245)  
> Since: 3.0.0

---

## setScrollFactor

### <instance> setScrollFactor(x, [y])

**Description:**

Sets the scroll factor of this Game Object.

The scroll factor controls the influence of the movement of a Camera upon this Game Object.

When a camera scrolls it will change the location at which this Game Object is rendered on-screen.

It does not change the Game Objects actual position values.

A value of 1 means it will move exactly in sync with a camera.

A value of 0 means it will not move at all, even if the camera moves.

Other values control the degree to which the camera movement is mapped to this Game Object.

Please be aware that scroll factor values other than 1 are not taken in to consideration when

calculating physics collisions. Bodies always collide based on their world position, but changing

the scroll factor is a visual adjustment to where the textures are rendered, which can offset

them from physics bodies if not accounted for in your code.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The horizontal scroll factor of this Game Object. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The vertical scroll factor of this Game Object. If not set it will use the `x` value. |

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.ScrollFactor#setScrollFactor](../namespace/gameobjects-components-scrollfactor.md)

> Source: [src/gameobjects/components/ScrollFactor.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/ScrollFactor.js#L64)  
> Since: 3.0.0

---

## setTo

### <instance> setTo([x], [y], [radius])

**Description:**

Sets the x, y and radius of this circle.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x position of the center of the circle. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y position of the center of the circle. |
| radius | number | Yes | 0 | The radius of the circle. |

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Circle object.

**Inherits:** [Phaser.Geom.Circle#setTo](geom-circle.md)

> Source: [src/geom/circle/Circle.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/circle/Circle.js#L166)  
> Since: 3.0.0

---

## setVisible

### <instance> setVisible(value)

**Description:**

Sets the visibility of this Game Object.

An invisible Game Object will skip rendering, but will still process update logic.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The visible state of the Game Object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Visible#setVisible](../namespace/gameobjects-components-visible.md)

> Source: [src/gameobjects/components/Visible.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Visible.js#L63)  
> Since: 3.0.0

---

## updateDisplayOrigin

### <instance> updateDisplayOrigin()

**Description:**

Updates the Display Origin cached values internally stored on this Game Object.

You don't usually call this directly, but it is exposed for edge-cases where you may.

**Returns:** [Phaser.GameObjects.Light](gameobjects-light.md) - This Game Object instance.

**Inherits:** [Phaser.GameObjects.Components.Origin#updateDisplayOrigin](../namespace/gameobjects-components-origin.md)

> Source: [src/gameobjects/components/Origin.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/components/Origin.js#L182)  
> Since: 3.0.0

---

## willRender

### <instance> willRender(camera)

**Description:**

Compares the renderMask with the renderFlags to see if this Game Object will render or not.

Also checks the Game Object against the given Cameras exclusion list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera to check against this Game Object. |
| --- | --- | --- | --- |

**Returns:** boolean - True if the Game Object should be rendered, otherwise false.

> Source: [src/gameobjects/lights/Light.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L193)  
> Since: 3.50.0

---

# Constants:

# Public Members

## RENDER\_MASK

### RENDER\_MASK: number

**Description:**

The bitmask that `GameObject.renderFlags` is compared against to determine if the Game Object will render or not.

> Source: [src/gameobjects/lights/Light.js#L264](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/lights/Light.js#L264)

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [bottom](#bottom)

    - [bottom: number](#bottom-number)
  + [cameraFilter](#camerafilter)

    - [cameraFilter: number](#camerafilter-number)
  + [color](#color)

    - [color: Phaser.Display.RGB](#color-phaserdisplayrgb)
  + [diameter](#diameter)

    - [diameter: number](#diameter-number)
  + [displayHeight](#displayheight)

    - [displayHeight: number](#displayheight-number)
  + [displayOriginX](#displayoriginx)

    - [displayOriginX: number](#displayoriginx-number)
  + [displayOriginY](#displayoriginy)

    - [displayOriginY: number](#displayoriginy-number)
  + [displayWidth](#displaywidth)

    - [displayWidth: number](#displaywidth-number)
  + [height](#height)

    - [height: number](#height-number)
  + [intensity](#intensity)

    - [intensity: number](#intensity-number)
  + [left](#left)

    - [left: number](#left-number)
  + [originX](#originx)

    - [originX: number](#originx-number)
  + [originY](#originy)

    - [originY: number](#originy-number)
  + [radius](#radius)

    - [radius: number](#radius-number)
  + [renderFlags](#renderflags)

    - [renderFlags: number](#renderflags-number)
  + [right](#right)

    - [right: number](#right-number)
  + [scrollFactorX](#scrollfactorx)

    - [scrollFactorX: number](#scrollfactorx-number)
  + [scrollFactorY](#scrollfactory)

    - [scrollFactorY: number](#scrollfactory-number)
  + [top](#top)

    - [top: number](#top-number)
  + [type](#type)

    - [type: number](#type-number)
  + [visible](#visible)

    - [visible: boolean](#visible-boolean)
  + [width](#width)

    - [width: number](#width-number)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Private Members](#private-members)

  + [\_diameter](#_diameter)

    - [\_diameter: number](#_diameter-number)
  + [\_originComponent](#_origincomponent)

    - [\_originComponent: boolean](#_origincomponent-boolean)
  + [\_radius](#_radius)

    - [\_radius: number](#_radius-number)
  + [\_visible](#_visible)

    - [\_visible: boolean](#_visible-boolean)
* [Public Methods](#public-methods)

  + [contains](#contains)

    - [<instance> contains(x, y)](#instance-containsx-y)
  + [getPoint](#getpoint)

    - [<instance> getPoint(position, [out])](#instance-getpointposition-out)
  + [getPoints](#getpoints)

    - [<instance> getPoints(quantity, [stepRate], [output])](#instance-getpointsquantity-steprate-output)
  + [getRandomPoint](#getrandompoint)

    - [<instance> getRandomPoint([point])](#instance-getrandompointpoint)
  + [isEmpty](#isempty)

    - [<instance> isEmpty()](#instance-isempty)
  + [setColor](#setcolor)

    - [<instance> setColor(rgb)](#instance-setcolorrgb)
  + [setDisplayOrigin](#setdisplayorigin)

    - [<instance> setDisplayOrigin([x], [y])](#instance-setdisplayoriginx-y)
  + [setEmpty](#setempty)

    - [<instance> setEmpty()](#instance-setempty)
  + [setIntensity](#setintensity)

    - [<instance> setIntensity(intensity)](#instance-setintensityintensity)
  + [setOrigin](#setorigin)

    - [<instance> setOrigin([x], [y])](#instance-setoriginx-y)
  + [setOriginFromFrame](#setoriginfromframe)

    - [<instance> setOriginFromFrame()](#instance-setoriginfromframe)
  + [setPosition](#setposition)

    - [<instance> setPosition([x], [y])](#instance-setpositionx-y)
  + [setRadius](#setradius)

    - [<instance> setRadius(radius)](#instance-setradiusradius)
  + [setScrollFactor](#setscrollfactor)

    - [<instance> setScrollFactor(x, [y])](#instance-setscrollfactorx-y)
  + [setTo](#setto)

    - [<instance> setTo([x], [y], [radius])](#instance-settox-y-radius)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value)](#instance-setvisiblevalue)
  + [updateDisplayOrigin](#updatedisplayorigin)

    - [<instance> updateDisplayOrigin()](#instance-updatedisplayorigin)
  + [willRender](#willrender)

    - [<instance> willRender(camera)](#instance-willrendercamera)
* [Constants:](#constants)
* [Public Members](#public-members-1)

  + [RENDER\_MASK](#render_mask)

    - [RENDER\_MASK: number](#render_mask-number)

Back to top

©2025[Phaser](https://docs.phaser.io)