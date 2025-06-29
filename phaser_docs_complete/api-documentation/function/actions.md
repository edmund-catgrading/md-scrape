# Phaser.Actions

## AlignTo

### <static> AlignTo(items, position, [offsetX], [offsetY])

**Description:**

Takes an array of Game Objects and aligns them next to each other.

The alignment position is controlled by the `position` parameter, which should be one

of the Phaser.Display.Align constants, such as `Phaser.Display.Align.TOP_LEFT`,

`Phaser.Display.Align.TOP_CENTER`, etc.

The first item isn't moved. The second item is aligned next to the first,

then the third next to the second, and so on.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| position | number | No |  | The position to align the items with. This is an align constant, such as `Phaser.Display.Align.LEFT_CENTER`. |
| offsetX | number | Yes | 0 | Optional horizontal offset from the position. |
| offsetY | number | Yes | 0 | Optional vertical offset from the position. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/AlignTo.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/AlignTo.js#L9)  
> Since: 3.22.0

## Angle

### <static> Angle(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have a public `angle` property,

and then adds the given value to each of their `angle` properties.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `Angle(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to be added to the `angle` property. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/Angle.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/Angle.js#L9)  
> Since: 3.0.0

## Call

### <static> Call(items, callback, context)

**Description:**

Takes an array of objects and passes each of them to the given callback.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | The array of items to be updated by this action. |
| --- | --- | --- | --- |
| callback | [Phaser.Types.Actions.CallCallback](../typedef/types-actions.md) | No | The callback to be invoked. It will be passed just one argument: the item from the array. |
| context | \* | No | The scope in which the callback will be invoked. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that was passed to this Action.

> Source: [src/actions/Call.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/Call.js#L7)  
> Since: 3.0.0

## GetFirst

### <static> GetFirst(items, compare, [index])

**Description:**

Takes an array of objects and returns the first element in the array that has properties which match

all of those specified in the `compare` object. For example, if the compare object was: `{ scaleX: 0.5, alpha: 1 }`

then it would return the first item which had the property `scaleX` set to 0.5 and `alpha` set to 1.

To use this with a Group: `GetFirst(group.getChildren(), compare, index)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be searched by this action. |
| --- | --- | --- | --- | --- |
| compare | object | No |  | The comparison object. Each property in this object will be checked against the items of the array. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |

**Returns:** object, [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The first object in the array that matches the comparison object, or `null` if no match was found.

> Source: [src/actions/GetFirst.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/GetFirst.js#L7)  
> Since: 3.0.0

## GetLast

### <static> GetLast(items, compare, [index])

**Description:**

Takes an array of objects and returns the last element in the array that has properties which match

all of those specified in the `compare` object. For example, if the compare object was: `{ scaleX: 0.5, alpha: 1 }`

then it would return the last item which had the property `scaleX` set to 0.5 and `alpha` set to 1.

To use this with a Group: `GetLast(group.getChildren(), compare, index)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be searched by this action. |
| --- | --- | --- | --- | --- |
| compare | object | No |  | The comparison object. Each property in this object will be checked against the items of the array. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |

**Returns:** object, [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) - The last object in the array that matches the comparison object, or `null` if no match was found.

> Source: [src/actions/GetLast.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/GetLast.js#L7)  
> Since: 3.3.0

## GridAlign

### <static> GridAlign(items, options)

**Description:**

Takes an array of Game Objects, or any objects that have public `x` and `y` properties,

and then aligns them based on the grid configuration given to this action.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | The array of items to be updated by this action. |
| --- | --- | --- | --- |
| options | [Phaser.Types.Actions.GridAlignConfig](../typedef/types-actions.md) | No | The GridAlign Configuration object. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/GridAlign.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/GridAlign.js#L15)  
> Since: 3.0.0

## IncAlpha

### <static> IncAlpha(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have a public `alpha` property,

and then adds the given value to each of their `alpha` properties.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `IncAlpha(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to be added to the `alpha` property. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/IncAlpha.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/IncAlpha.js#L9)  
> Since: 3.0.0

## IncX

### <static> IncX(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have a public `x` property,

and then adds the given value to each of their `x` properties.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `IncX(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to be added to the `x` property. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/IncX.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/IncX.js#L9)  
> Since: 3.0.0

## IncXY

### <static> IncXY(items, x, [y], [stepX], [stepY], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have public `x` and `y` properties,

and then adds the given value to each of them.

The optional `stepX` and `stepY` properties are applied incrementally, multiplied by each item in the array.

To use this with a Group: `IncXY(group.getChildren(), x, y, stepX, stepY)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| x | number | No |  | The amount to be added to the `x` property. |
| y | number | Yes | "x" | The amount to be added to the `y` property. If `undefined` or `null` it uses the `x` value. |
| stepX | number | Yes | 0 | This is added to the `x` amount, multiplied by the iteration counter. |
| stepY | number | Yes | 0 | This is added to the `y` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/IncXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/IncXY.js#L9)  
> Since: 3.0.0

## IncY

### <static> IncY(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have a public `y` property,

and then adds the given value to each of their `y` properties.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `IncY(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to be added to the `y` property. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/IncY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/IncY.js#L9)  
> Since: 3.0.0

## PlaceOnCircle

### <static> PlaceOnCircle(items, circle, [startAngle], [endAngle])

**Description:**

Takes an array of Game Objects and positions them on evenly spaced points around the perimeter of a Circle.

If you wish to pass a `Phaser.GameObjects.Circle` Shape to this function, you should pass its `geom` property.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No |  | The Circle to position the Game Objects on. |
| startAngle | number | Yes | 0 | Optional angle to start position from, in radians. |
| endAngle | number | Yes | 6.28 | Optional angle to stop position at, in radians. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/PlaceOnCircle.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/PlaceOnCircle.js#L7)  
> Since: 3.0.0

## PlaceOnEllipse

### <static> PlaceOnEllipse(items, ellipse, [startAngle], [endAngle])

**Description:**

Takes an array of Game Objects and positions them on evenly spaced points around the perimeter of an Ellipse.

If you wish to pass a `Phaser.GameObjects.Ellipse` Shape to this function, you should pass its `geom` property.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No |  | The Ellipse to position the Game Objects on. |
| startAngle | number | Yes | 0 | Optional angle to start position from, in radians. |
| endAngle | number | Yes | 6.28 | Optional angle to stop position at, in radians. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/PlaceOnEllipse.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/PlaceOnEllipse.js#L7)  
> Since: 3.0.0

## PlaceOnLine

### <static> PlaceOnLine(items, line, [ease])

**Description:**

Positions an array of Game Objects on evenly spaced points of a Line.

If the ease parameter is supplied, it will space the points based on that easing function along the line.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The Line to position the Game Objects on. |
| ease | string | function | Yes | An optional ease to use. This can be either a string from the EaseMap, or a custom function. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/PlaceOnLine.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/PlaceOnLine.js#L10)  
> Since: 3.0.0

## PlaceOnRectangle

### <static> PlaceOnRectangle(items, rect, [shift])

**Description:**

Takes an array of Game Objects and positions them on evenly spaced points around the perimeter of a Rectangle.

Placement starts from the top-left of the rectangle, and proceeds in a clockwise direction.

If the `shift` parameter is given you can offset where placement begins.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No |  | The Rectangle to position the Game Objects on. |
| shift | number | Yes | 0 | An optional positional offset. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/PlaceOnRectangle.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/PlaceOnRectangle.js#L11)  
> Since: 3.0.0

## PlaceOnTriangle

### <static> PlaceOnTriangle(items, triangle, [stepRate])

**Description:**

Takes an array of Game Objects and positions them on evenly spaced points around the edges of a Triangle.

If you wish to pass a `Phaser.GameObjects.Triangle` Shape to this function, you should pass its `geom` property.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No |  | The Triangle to position the Game Objects on. |
| stepRate | number | Yes | 1 | An optional step rate, to increase or decrease the packing of the Game Objects on the lines. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/PlaceOnTriangle.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/PlaceOnTriangle.js#L9)  
> Since: 3.0.0

## PlayAnimation

### <static> PlayAnimation(items, key, [ignoreIfPlaying])

**Description:**

Play an animation on all Game Objects in the array that have an Animation component.

You can pass either an animation key, or an animation configuration object for more control over the playback.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Animations.Animation](../class/animations-animation.md) | [Phaser.Types.Animations.PlayAnimationConfig](../typedef/types-animations.md) | No |  |
| ignoreIfPlaying | boolean | Yes | false | If this animation is already playing then ignore this call. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/PlayAnimation.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/PlayAnimation.js#L7)  
> Since: 3.0.0

## PropertyValueInc

### <static> PropertyValueInc(items, key, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have a public property as defined in `key`,

and then adds the given value to it.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `PropertyValueInc(group.getChildren(), key, value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| key | string | No |  | The property to be updated. |
| value | number | No |  | The amount to be added to the property. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/PropertyValueInc.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/PropertyValueInc.js#L7)  
> Since: 3.3.0

## PropertyValueSet

### <static> PropertyValueSet(items, key, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have a public property as defined in `key`,

and then sets it to the given value.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `PropertyValueSet(group.getChildren(), key, value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| key | string | No |  | The property to be updated. |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/PropertyValueSet.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/PropertyValueSet.js#L7)  
> Since: 3.3.0

## RandomCircle

### <static> RandomCircle(items, circle)

**Description:**

Takes an array of Game Objects and positions them at random locations within the Circle.

If you wish to pass a `Phaser.GameObjects.Circle` Shape to this function, you should pass its `geom` property.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |
| circle | [Phaser.Geom.Circle](../class/geom-circle.md) | No | The Circle to position the Game Objects within. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/RandomCircle.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/RandomCircle.js#L9)  
> Since: 3.0.0

## RandomEllipse

### <static> RandomEllipse(items, ellipse)

**Description:**

Takes an array of Game Objects and positions them at random locations within the Ellipse.

If you wish to pass a `Phaser.GameObjects.Ellipse` Shape to this function, you should pass its `geom` property.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |
| ellipse | [Phaser.Geom.Ellipse](../class/geom-ellipse.md) | No | The Ellipse to position the Game Objects within. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/RandomEllipse.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/RandomEllipse.js#L9)  
> Since: 3.0.0

## RandomLine

### <static> RandomLine(items, line)

**Description:**

Takes an array of Game Objects and positions them at random locations on the Line.

If you wish to pass a `Phaser.GameObjects.Line` Shape to this function, you should pass its `geom` property.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |
| line | [Phaser.Geom.Line](../class/geom-line.md) | No | The Line to position the Game Objects randomly on. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/RandomLine.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/RandomLine.js#L9)  
> Since: 3.0.0

## RandomRectangle

### <static> RandomRectangle(items, rect)

**Description:**

Takes an array of Game Objects and positions them at random locations within the Rectangle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No | The Rectangle to position the Game Objects within. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/RandomRectangle.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/RandomRectangle.js#L9)  
> Since: 3.0.0

## RandomTriangle

### <static> RandomTriangle(items, triangle)

**Description:**

Takes an array of Game Objects and positions them at random locations within the Triangle.

If you wish to pass a `Phaser.GameObjects.Triangle` Shape to this function, you should pass its `geom` property.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |
| triangle | [Phaser.Geom.Triangle](../class/geom-triangle.md) | No | The Triangle to position the Game Objects within. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/RandomTriangle.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/RandomTriangle.js#L9)  
> Since: 3.0.0

## Rotate

### <static> Rotate(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have a public `rotation` property,

and then adds the given value to each of their `rotation` properties.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `Rotate(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to be added to the `rotation` property (in radians). |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/Rotate.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/Rotate.js#L9)  
> Since: 3.0.0

## RotateAround

### <static> RotateAround(items, point, angle)

**Description:**

Rotates each item around the given point by the given angle.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |
| point | object | No | Any object with public `x` and `y` properties. |
| angle | number | No | The angle to rotate by, in radians. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/RotateAround.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/RotateAround.js#L10)  
> Since: 3.0.0

## RotateAroundDistance

### <static> RotateAroundDistance(items, point, angle, distance)

**Description:**

Rotates an array of Game Objects around a point by the given angle and distance.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |
| point | object | No | Any object with public `x` and `y` properties. |
| angle | number | No | The angle to rotate by, in radians. |
| distance | number | No | The distance from the point of rotation in pixels. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/RotateAroundDistance.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/RotateAroundDistance.js#L9)  
> Since: 3.0.0

## ScaleX

### <static> ScaleX(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have a public `scaleX` property,

and then adds the given value to each of their `scaleX` properties.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `ScaleX(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to be added to the `scaleX` property. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/ScaleX.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/ScaleX.js#L9)  
> Since: 3.0.0

## ScaleXY

### <static> ScaleXY(items, scaleX, [scaleY], [stepX], [stepY], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have public `scaleX` and `scaleY` properties,

and then adds the given value to each of them.

The optional `stepX` and `stepY` properties are applied incrementally, multiplied by each item in the array.

To use this with a Group: `ScaleXY(group.getChildren(), scaleX, scaleY, stepX, stepY)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| scaleX | number | No |  | The amount to be added to the `scaleX` property. |
| scaleY | number | Yes |  | The amount to be added to the `scaleY` property. If `undefined` or `null` it uses the `scaleX` value. |
| stepX | number | Yes | 0 | This is added to the `scaleX` amount, multiplied by the iteration counter. |
| stepY | number | Yes | 0 | This is added to the `scaleY` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/ScaleXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/ScaleXY.js#L9)  
> Since: 3.0.0

## ScaleY

### <static> ScaleY(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have a public `scaleY` property,

and then adds the given value to each of their `scaleY` properties.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `ScaleY(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to be added to the `scaleY` property. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/ScaleY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/ScaleY.js#L9)  
> Since: 3.0.0

## SetAlpha

### <static> SetAlpha(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `alpha`

and then sets it to the given value.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetAlpha(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetAlpha.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetAlpha.js#L9)  
> Since: 3.0.0

## SetBlendMode

### <static> SetBlendMode(items, value, [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `blendMode`

and then sets it to the given value.

To use this with a Group: `SetBlendMode(group.getChildren(), value)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | [Phaser.BlendModes](../namespace/blendmodes.md) | string | number | No |  |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetBlendMode.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetBlendMode.js#L9)  
> Since: 3.0.0

## SetDepth

### <static> SetDepth(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `depth`

and then sets it to the given value.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetDepth(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetDepth.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetDepth.js#L9)  
> Since: 3.0.0

## SetHitArea

### <static> SetHitArea(items, [hitArea], [callback])

**Description:**

Passes all provided Game Objects to the Input Manager to enable them for input with identical areas and callbacks.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |
| hitArea | [Phaser.Types.Input.InputConfiguration](../typedef/types-input.md) | any | Yes | Either an input configuration object, or a geometric shape that defines the hit area for the Game Object. If not given it will try to create a Rectangle based on the texture frame. |
| callback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes | The callback that determines if the pointer is within the Hit Area shape or not. If you provide a shape you must also provide a callback. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/SetHitArea.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetHitArea.js#L7)  
> Since: 3.0.0

## SetOrigin

### <static> SetOrigin(items, originX, [originY], [stepX], [stepY], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public properties `originX` and `originY`

and then sets them to the given values.

The optional `stepX` and `stepY` properties are applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetOrigin(group.getChildren(), originX, originY, stepX, stepY)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| originX | number | No |  | The amount to set the `originX` property to. |
| originY | number | Yes |  | The amount to set the `originY` property to. If `undefined` or `null` it uses the `originX` value. |
| stepX | number | Yes | 0 | This is added to the `originX` amount, multiplied by the iteration counter. |
| stepY | number | Yes | 0 | This is added to the `originY` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetOrigin.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetOrigin.js#L9)  
> Since: 3.0.0

## SetRotation

### <static> SetRotation(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `rotation`

and then sets it to the given value.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetRotation(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetRotation.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetRotation.js#L9)  
> Since: 3.0.0

## SetScale

### <static> SetScale(items, scaleX, [scaleY], [stepX], [stepY], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public properties `scaleX` and `scaleY`

and then sets them to the given values.

The optional `stepX` and `stepY` properties are applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetScale(group.getChildren(), scaleX, scaleY, stepX, stepY)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| scaleX | number | No |  | The amount to set the `scaleX` property to. |
| scaleY | number | Yes |  | The amount to set the `scaleY` property to. If `undefined` or `null` it uses the `scaleX` value. |
| stepX | number | Yes | 0 | This is added to the `scaleX` amount, multiplied by the iteration counter. |
| stepY | number | Yes | 0 | This is added to the `scaleY` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetScale.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetScale.js#L9)  
> Since: 3.0.0

## SetScaleX

### <static> SetScaleX(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `scaleX`

and then sets it to the given value.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetScaleX(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetScaleX.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetScaleX.js#L9)  
> Since: 3.0.0

## SetScaleY

### <static> SetScaleY(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `scaleY`

and then sets it to the given value.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetScaleY(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetScaleY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetScaleY.js#L9)  
> Since: 3.0.0

## SetScrollFactor

### <static> SetScrollFactor(items, scrollFactorX, [scrollFactorY], [stepX], [stepY], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public properties `scrollFactorX` and `scrollFactorY`

and then sets them to the given values.

The optional `stepX` and `stepY` properties are applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetScrollFactor(group.getChildren(), scrollFactorX, scrollFactorY, stepX, stepY)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| scrollFactorX | number | No |  | The amount to set the `scrollFactorX` property to. |
| scrollFactorY | number | Yes |  | The amount to set the `scrollFactorY` property to. If `undefined` or `null` it uses the `scrollFactorX` value. |
| stepX | number | Yes | 0 | This is added to the `scrollFactorX` amount, multiplied by the iteration counter. |
| stepY | number | Yes | 0 | This is added to the `scrollFactorY` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetScrollFactor.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetScrollFactor.js#L9)  
> Since: 3.21.0

## SetScrollFactorX

### <static> SetScrollFactorX(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `scrollFactorX`

and then sets it to the given value.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetScrollFactorX(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetScrollFactorX.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetScrollFactorX.js#L9)  
> Since: 3.21.0

## SetScrollFactorY

### <static> SetScrollFactorY(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `scrollFactorY`

and then sets it to the given value.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetScrollFactorY(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetScrollFactorY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetScrollFactorY.js#L9)  
> Since: 3.21.0

## SetTint

### <static> SetTint(items, topLeft, [topRight], [bottomLeft], [bottomRight])

**Description:**

Takes an array of Game Objects, or any objects that have the public method setTint() and then updates it to the given value(s). You can specify tint color per corner or provide only one color value for `topLeft` parameter, in which case whole item will be tinted with that color.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |
| topLeft | number | No | The tint being applied to top-left corner of item. If other parameters are given no value, this tint will be applied to whole item. |
| topRight | number | Yes | The tint to be applied to top-right corner of item. |
| bottomLeft | number | Yes | The tint to be applied to the bottom-left corner of item. |
| bottomRight | number | Yes | The tint to be applied to the bottom-right corner of item. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/SetTint.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetTint.js#L7)  
> Since: 3.0.0

## SetVisible

### <static> SetVisible(items, value, [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `visible`

and then sets it to the given value.

To use this with a Group: `SetVisible(group.getChildren(), value)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | boolean | No |  | The value to set the property to. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetVisible.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetVisible.js#L9)  
> Since: 3.0.0

## SetX

### <static> SetX(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `x`

and then sets it to the given value.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetX(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetX.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetX.js#L9)  
> Since: 3.0.0

## SetXY

### <static> SetXY(items, x, [y], [stepX], [stepY], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public properties `x` and `y`

and then sets them to the given values.

The optional `stepX` and `stepY` properties are applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetXY(group.getChildren(), x, y, stepX, stepY)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| x | number | No |  | The amount to set the `x` property to. |
| y | number | Yes | "x" | The amount to set the `y` property to. If `undefined` or `null` it uses the `x` value. |
| stepX | number | Yes | 0 | This is added to the `x` amount, multiplied by the iteration counter. |
| stepY | number | Yes | 0 | This is added to the `y` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetXY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetXY.js#L9)  
> Since: 3.0.0

## SetY

### <static> SetY(items, value, [step], [index], [direction])

**Description:**

Takes an array of Game Objects, or any objects that have the public property `y`

and then sets it to the given value.

The optional `step` property is applied incrementally, multiplied by each item in the array.

To use this with a Group: `SetY(group.getChildren(), value, step)`

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | The array of items to be updated by this action. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of objects that were passed to this Action.

> Source: [src/actions/SetY.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SetY.js#L9)  
> Since: 3.0.0

## ShiftPosition

### <static> ShiftPosition(items, x, y, [direction], [output])

**Description:**

Takes an array of items, such as Game Objects, or any objects with public `x` and

`y` properties and then iterates through them. As this function iterates, it moves

the position of the current element to be that of the previous entry in the array.

This repeats until all items have been moved.

The direction controls the order of iteration. A value of 0 (the default) assumes

that the final item in the array is the 'head' item.

A direction value of 1 assumes that the first item in the array is the 'head' item.

The position of the 'head' item is set to the x/y values given to this function.

Every other item in the array is then updated, in sequence, to be that of the

previous (or next) entry in the array.

The final x/y coords are returned, or set in the 'output' Vector2.

Think of it as being like the game Snake, where the 'head' is moved and then

each body piece is moved into the space of the previous piece.

**Tags:**

* generic
* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | Array.<[Phaser.Types.Math.Vector2Like](../typedef/types-math.md)> | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | An array of Game Objects, or objects with public x and y positions. The contents of this array are updated by this Action. |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate to place the head item at. |
| y | number | No |  | The y coordinate to place the head item at. |
| direction | number | Yes | 0 | The iteration direction. 0 = first to last and 1 = last to first. |
| output | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | Yes |  | An optional Vec2Like object to store the final position in. |

**Returns:** [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) - The output vector.

> Source: [src/actions/ShiftPosition.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/ShiftPosition.js#L9)  
> Since: 3.0.0

## Shuffle

### <static> Shuffle(items)

**Description:**

Shuffles the array in place. The shuffled array is both modified and returned.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/Shuffle.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/Shuffle.js#L9)  
> Since: 3.0.0

## SmootherStep

### <static> SmootherStep(items, property, min, max, [inc])

**Description:**

Smootherstep is a sigmoid-like interpolation and clamping function.

The function depends on three parameters, the input x, the "left edge" and the "right edge", with the left edge being assumed smaller than the right edge. The function receives a real number x as an argument and returns 0 if x is less than or equal to the left edge, 1 if x is greater than or equal to the right edge, and smoothly interpolates, using a Hermite polynomial, between 0 and 1 otherwise. The slope of the smoothstep function is zero at both edges. This is convenient for creating a sequence of transitions using smoothstep to interpolate each segment as an alternative to using more sophisticated or expensive interpolation techniques.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- | --- |
| property | string | No |  | The property of the Game Object to interpolate. |
| min | number | No |  | The minimum interpolation value. |
| max | number | No |  | The maximum interpolation value. |
| inc | boolean | Yes | false | Should the values be incremented? `true` or set (`false`) |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/SmootherStep.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SmootherStep.js#L9)  
> Since: 3.0.0

## SmoothStep

### <static> SmoothStep(items, property, min, max, [inc])

**Description:**

Smoothstep is a sigmoid-like interpolation and clamping function.

The function depends on three parameters, the input x, the "left edge"

and the "right edge", with the left edge being assumed smaller than the right edge.

The function receives a real number x as an argument and returns 0 if x is less than

or equal to the left edge, 1 if x is greater than or equal to the right edge, and smoothly

interpolates, using a Hermite polynomial, between 0 and 1 otherwise. The slope of the

smoothstep function is zero at both edges.

This is convenient for creating a sequence of transitions using smoothstep to interpolate

each segment as an alternative to using more sophisticated or expensive interpolation techniques.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- | --- |
| property | string | No |  | The property of the Game Object to interpolate. |
| min | number | No |  | The minimum interpolation value. |
| max | number | No |  | The maximum interpolation value. |
| inc | boolean | Yes | false | Should the property value be incremented (`true`) or set (`false`)? |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/SmoothStep.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/SmoothStep.js#L9)  
> Since: 3.0.0

## Spread

### <static> Spread(items, property, min, max, [inc])

**Description:**

Takes an array of Game Objects and then modifies their `property` so the value equals, or is incremented, by the

calculated spread value.

The spread value is derived from the given `min` and `max` values and the total number of items in the array.

For example, to cause an array of Sprites to change in alpha from 0 to 1 you could call:

```
Copy
Phaser.Actions.Spread(itemsArray, 'alpha', 0, 1);


```

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- | --- |
| property | string | No |  | The property of the Game Object to spread. |
| min | number | No |  | The minimum value. |
| max | number | No |  | The maximum value. |
| inc | boolean | Yes | false | Should the values be incremented? `true` or set (`false`) |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that were passed to this Action.

> Source: [src/actions/Spread.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/Spread.js#L7)  
> Since: 3.0.0

## ToggleVisible

### <static> ToggleVisible(items)

**Description:**

Takes an array of Game Objects and toggles the visibility of each one.

Those previously `visible = false` will become `visible = true`, and vice versa.

**Tags:**

* generic

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/ToggleVisible.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/ToggleVisible.js#L7)  
> Since: 3.0.0

## WrapInRectangle

### <static> WrapInRectangle(items, rect, [padding])

**Description:**

Iterates through the given array and makes sure that each objects x and y

properties are wrapped to keep them contained within the given Rectangles

area.

**Tags:**

* generic

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| items | array | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No |  | An array of Game Objects. The contents of this array are updated by this Action. |
| --- | --- | --- | --- | --- |
| rect | [Phaser.Geom.Rectangle](../class/geom-rectangle.md) | No |  | The rectangle which the objects will be wrapped to remain within. |
| padding | number | Yes | 0 | An amount added to each side of the rectangle during the operation. |

**Returns:** array, Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> - The array of Game Objects that was passed to this Action.

> Source: [src/actions/WrapInRectangle.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/actions/WrapInRectangle.js#L10)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Actions](#phaseractions)

  + [AlignTo](#alignto)

    - [<static> AlignTo(items, position, [offsetX], [offsetY])](#static-aligntoitems-position-offsetx-offsety)
  + [Angle](#angle)

    - [<static> Angle(items, value, [step], [index], [direction])](#static-angleitems-value-step-index-direction)
  + [Call](#call)

    - [<static> Call(items, callback, context)](#static-callitems-callback-context)
  + [GetFirst](#getfirst)

    - [<static> GetFirst(items, compare, [index])](#static-getfirstitems-compare-index)
  + [GetLast](#getlast)

    - [<static> GetLast(items, compare, [index])](#static-getlastitems-compare-index)
  + [GridAlign](#gridalign)

    - [<static> GridAlign(items, options)](#static-gridalignitems-options)
  + [IncAlpha](#incalpha)

    - [<static> IncAlpha(items, value, [step], [index], [direction])](#static-incalphaitems-value-step-index-direction)
  + [IncX](#incx)

    - [<static> IncX(items, value, [step], [index], [direction])](#static-incxitems-value-step-index-direction)
  + [IncXY](#incxy)

    - [<static> IncXY(items, x, [y], [stepX], [stepY], [index], [direction])](#static-incxyitems-x-y-stepx-stepy-index-direction)
  + [IncY](#incy)

    - [<static> IncY(items, value, [step], [index], [direction])](#static-incyitems-value-step-index-direction)
  + [PlaceOnCircle](#placeoncircle)

    - [<static> PlaceOnCircle(items, circle, [startAngle], [endAngle])](#static-placeoncircleitems-circle-startangle-endangle)
  + [PlaceOnEllipse](#placeonellipse)

    - [<static> PlaceOnEllipse(items, ellipse, [startAngle], [endAngle])](#static-placeonellipseitems-ellipse-startangle-endangle)
  + [PlaceOnLine](#placeonline)

    - [<static> PlaceOnLine(items, line, [ease])](#static-placeonlineitems-line-ease)
  + [PlaceOnRectangle](#placeonrectangle)

    - [<static> PlaceOnRectangle(items, rect, [shift])](#static-placeonrectangleitems-rect-shift)
  + [PlaceOnTriangle](#placeontriangle)

    - [<static> PlaceOnTriangle(items, triangle, [stepRate])](#static-placeontriangleitems-triangle-steprate)
  + [PlayAnimation](#playanimation)

    - [<static> PlayAnimation(items, key, [ignoreIfPlaying])](#static-playanimationitems-key-ignoreifplaying)
  + [PropertyValueInc](#propertyvalueinc)

    - [<static> PropertyValueInc(items, key, value, [step], [index], [direction])](#static-propertyvalueincitems-key-value-step-index-direction)
  + [PropertyValueSet](#propertyvalueset)

    - [<static> PropertyValueSet(items, key, value, [step], [index], [direction])](#static-propertyvaluesetitems-key-value-step-index-direction)
  + [RandomCircle](#randomcircle)

    - [<static> RandomCircle(items, circle)](#static-randomcircleitems-circle)
  + [RandomEllipse](#randomellipse)

    - [<static> RandomEllipse(items, ellipse)](#static-randomellipseitems-ellipse)
  + [RandomLine](#randomline)

    - [<static> RandomLine(items, line)](#static-randomlineitems-line)
  + [RandomRectangle](#randomrectangle)

    - [<static> RandomRectangle(items, rect)](#static-randomrectangleitems-rect)
  + [RandomTriangle](#randomtriangle)

    - [<static> RandomTriangle(items, triangle)](#static-randomtriangleitems-triangle)
  + [Rotate](#rotate)

    - [<static> Rotate(items, value, [step], [index], [direction])](#static-rotateitems-value-step-index-direction)
  + [RotateAround](#rotatearound)

    - [<static> RotateAround(items, point, angle)](#static-rotatearounditems-point-angle)
  + [RotateAroundDistance](#rotatearounddistance)

    - [<static> RotateAroundDistance(items, point, angle, distance)](#static-rotatearounddistanceitems-point-angle-distance)
  + [ScaleX](#scalex)

    - [<static> ScaleX(items, value, [step], [index], [direction])](#static-scalexitems-value-step-index-direction)
  + [ScaleXY](#scalexy)

    - [<static> ScaleXY(items, scaleX, [scaleY], [stepX], [stepY], [index], [direction])](#static-scalexyitems-scalex-scaley-stepx-stepy-index-direction)
  + [ScaleY](#scaley)

    - [<static> ScaleY(items, value, [step], [index], [direction])](#static-scaleyitems-value-step-index-direction)
  + [SetAlpha](#setalpha)

    - [<static> SetAlpha(items, value, [step], [index], [direction])](#static-setalphaitems-value-step-index-direction)
  + [SetBlendMode](#setblendmode)

    - [<static> SetBlendMode(items, value, [index], [direction])](#static-setblendmodeitems-value-index-direction)
  + [SetDepth](#setdepth)

    - [<static> SetDepth(items, value, [step], [index], [direction])](#static-setdepthitems-value-step-index-direction)
  + [SetHitArea](#sethitarea)

    - [<static> SetHitArea(items, [hitArea], [callback])](#static-sethitareaitems-hitarea-callback)
  + [SetOrigin](#setorigin)

    - [<static> SetOrigin(items, originX, [originY], [stepX], [stepY], [index], [direction])](#static-setoriginitems-originx-originy-stepx-stepy-index-direction)
  + [SetRotation](#setrotation)

    - [<static> SetRotation(items, value, [step], [index], [direction])](#static-setrotationitems-value-step-index-direction)
  + [SetScale](#setscale)

    - [<static> SetScale(items, scaleX, [scaleY], [stepX], [stepY], [index], [direction])](#static-setscaleitems-scalex-scaley-stepx-stepy-index-direction)
  + [SetScaleX](#setscalex)

    - [<static> SetScaleX(items, value, [step], [index], [direction])](#static-setscalexitems-value-step-index-direction)
  + [SetScaleY](#setscaley)

    - [<static> SetScaleY(items, value, [step], [index], [direction])](#static-setscaleyitems-value-step-index-direction)
  + [SetScrollFactor](#setscrollfactor)

    - [<static> SetScrollFactor(items, scrollFactorX, [scrollFactorY], [stepX], [stepY], [index], [direction])](#static-setscrollfactoritems-scrollfactorx-scrollfactory-stepx-stepy-index-direction)
  + [SetScrollFactorX](#setscrollfactorx)

    - [<static> SetScrollFactorX(items, value, [step], [index], [direction])](#static-setscrollfactorxitems-value-step-index-direction)
  + [SetScrollFactorY](#setscrollfactory)

    - [<static> SetScrollFactorY(items, value, [step], [index], [direction])](#static-setscrollfactoryitems-value-step-index-direction)
  + [SetTint](#settint)

    - [<static> SetTint(items, topLeft, [topRight], [bottomLeft], [bottomRight])](#static-settintitems-topleft-topright-bottomleft-bottomright)
  + [SetVisible](#setvisible)

    - [<static> SetVisible(items, value, [index], [direction])](#static-setvisibleitems-value-index-direction)
  + [SetX](#setx)

    - [<static> SetX(items, value, [step], [index], [direction])](#static-setxitems-value-step-index-direction)
  + [SetXY](#setxy)

    - [<static> SetXY(items, x, [y], [stepX], [stepY], [index], [direction])](#static-setxyitems-x-y-stepx-stepy-index-direction)
  + [SetY](#sety)

    - [<static> SetY(items, value, [step], [index], [direction])](#static-setyitems-value-step-index-direction)
  + [ShiftPosition](#shiftposition)

    - [<static> ShiftPosition(items, x, y, [direction], [output])](#static-shiftpositionitems-x-y-direction-output)
  + [Shuffle](#shuffle)

    - [<static> Shuffle(items)](#static-shuffleitems)
  + [SmootherStep](#smootherstep)

    - [<static> SmootherStep(items, property, min, max, [inc])](#static-smootherstepitems-property-min-max-inc)
  + [SmoothStep](#smoothstep)

    - [<static> SmoothStep(items, property, min, max, [inc])](#static-smoothstepitems-property-min-max-inc)
  + [Spread](#spread)

    - [<static> Spread(items, property, min, max, [inc])](#static-spreaditems-property-min-max-inc)
  + [ToggleVisible](#togglevisible)

    - [<static> ToggleVisible(items)](#static-togglevisibleitems)
  + [WrapInRectangle](#wrapinrectangle)

    - [<static> WrapInRectangle(items, rect, [padding])](#static-wrapinrectangleitems-rect-padding)

Back to top

©2025[Phaser](https://docs.phaser.io)