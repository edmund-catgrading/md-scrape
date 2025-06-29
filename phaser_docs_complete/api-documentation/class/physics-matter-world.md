# World

Phaser.Physics.Matter.World

The Matter World class is responsible for managing one single instance of a Matter Physics World for Phaser.

Access this via `this.matter.world` from within a Scene.

This class creates a Matter JS World Composite along with the Matter JS Engine during instantiation. It also

handles delta timing, bounds, body and constraint creation and debug drawing.

If you wish to access the Matter JS World object directly, see the `localWorld` property.

If you wish to access the Matter Engine directly, see the `engine` property.

This class is an Event Emitter and will proxy *all* Matter JS events, as they are received.

**Constructor**

`new World(scene, config)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to which this Matter World instance belongs. |
| --- | --- | --- | --- |
| config | [Phaser.Types.Physics.Matter.MatterWorldConfig](../typedef/types-physics-matter.md) | No | The Matter World configuration object. |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/physics/matter-js/World.js#L24](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L24)  
> Since: 3.0.0

# Public Members

## autoUpdate

### autoUpdate: boolean

**Description:**

Automatically call Engine.update every time the game steps.

If you disable this then you are responsible for calling `World.step` directly from your game.

If you call `set60Hz` or `set30Hz` then `autoUpdate` is reset to `true`.

> Source: [src/physics/matter-js/World.js#L185](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L185)  
> Since: 3.4.0

---

## debugConfig

### debugConfig: [Phaser.Types.Physics.Matter.MatterDebugConfig](../typedef/types-physics-matter.md)

**Description:**

The debug configuration object.

The values stored in this object are read from the Matter World Config `debug` property.

When a new Body or Constraint is *added to the World*, they are given the values stored in this object,

unless they have their own `render` object set that will override them.

Note that while you can modify the values of properties in this object at run-time, it will not change

any of the Matter objects *already added*. It will only impact objects newly added to the world, or one

that is removed and then re-added at a later time.

> Source: [src/physics/matter-js/World.js#L218](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L218)  
> Since: 3.22.0

---

## debugGraphic

### debugGraphic: [Phaser.GameObjects.Graphics](gameobjects-graphics.md)

**Description:**

An instance of the Graphics object the debug bodies are drawn to, if enabled.

> Source: [src/physics/matter-js/World.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L209)  
> Since: 3.0.0

---

## drawDebug

### drawDebug: boolean

**Description:**

A flag that controls if the debug graphics will be drawn to or not.

> Source: [src/physics/matter-js/World.js#L199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L199)  
> Since: 3.0.0

---

## enabled

### enabled: boolean

**Description:**

A flag that toggles if the world is enabled or not.

> Source: [src/physics/matter-js/World.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L104)  
> Since: 3.0.0

---

## engine

### engine: MatterJS.Engine

**Description:**

An instance of the MatterJS Engine.

> Source: [src/physics/matter-js/World.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L66)  
> Since: 3.0.0

---

## getDelta

### getDelta: function

**Description:**

This function is called every time the core game loop steps, which is bound to the

Request Animation Frame frequency unless otherwise modified.

The function is passed two values: `time` and `delta`, both of which come from the game step values.

It must return a number. This number is used as the delta value passed to Matter.Engine.update.

You can override this function with your own to define your own timestep.

If you need to update the Engine multiple times in a single game step then call

`World.update` as many times as required. Each call will trigger the `getDelta` function.

If you wish to have full control over when the Engine updates then see the property `autoUpdate`.

You can also adjust the number of iterations that Engine.update performs.

Use the Scene Matter Physics config object to set the following properties:

positionIterations (defaults to 6)

velocityIterations (defaults to 4)

constraintIterations (defaults to 2)

Adjusting these values can help performance in certain situations, depending on the physics requirements

of your game.

> Source: [src/physics/matter-js/World.js#L114](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L114)  
> Since: 3.4.0

---

## localWorld

### localWorld: MatterJS.World

**Description:**

A `World` composite object that will contain all simulated bodies and constraints.

> Source: [src/physics/matter-js/World.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L75)  
> Since: 3.0.0

---

## runner

### runner: [Phaser.Types.Physics.Matter.MatterRunnerConfig](../typedef/types-physics-matter.md)

**Description:**

The Matter JS Runner Configuration object.

This object is populated via the Matter Configuration object's `runner` property and is

updated constantly during the game step.

> Source: [src/physics/matter-js/World.js#L159](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L159)  
> Since: 3.22.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene to which this Matter World instance belongs.

> Source: [src/physics/matter-js/World.js#L57](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L57)  
> Since: 3.0.0

---

## walls

### walls: [Phaser.Types.Physics.Matter.MatterWalls](../typedef/types-physics-matter.md)

**Description:**

An object containing the 4 wall bodies that bound the physics world.

> Source: [src/physics/matter-js/World.js#L95](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L95)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(object)

**Description:**

Adds a Matter JS object, or array of objects, to the world.

The objects should be valid Matter JS entities, such as a Body, Composite or Constraint.

Triggers `beforeAdd` and `afterAdd` events.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object | object | Array.<object> | No | Can be single object, or an array, and can be a body, composite or constraint. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World object.

> Source: [src/physics/matter-js/World.js#L973](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L973)  
> Since: 3.0.0

---

## addListener

### <instance> addListener(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## convertTilemapLayer

### <instance> convertTilemapLayer(tilemapLayer, [options])

**Description:**

Adds `MatterTileBody` instances for all the colliding tiles within the given tilemap layer.

Set the appropriate tiles in your layer to collide before calling this method!

If you modify the map after calling this method, i.e. via a function like `putTileAt` then

you should call the `Phaser.Physics.Matter.World.convertTiles` function directly, passing

it an array of the tiles you've added to your map.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tilemapLayer | [Phaser.Tilemaps.TilemapLayer](tilemaps-tilemaplayer.md) | No | An array of tiles. |
| --- | --- | --- | --- |
| options | object | Yes | Options to be passed to the MatterTileBody constructor. {@see Phaser.Physics.Matter.TileBody} |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World object.

> Source: [src/physics/matter-js/World.js#L1048](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1048)  
> Since: 3.0.0

---

## convertTiles

### <instance> convertTiles(tiles, [options])

**Description:**

Creates `MatterTileBody` instances for all of the given tiles. This creates bodies regardless of whether the

tiles are set to collide or not, or if they have a body already, or not.

If you wish to pass an array of tiles that may already have bodies, you should filter the array before hand.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| tiles | Array.<[Phaser.Tilemaps.Tile](tilemaps-tile.md)> | No | An array of tiles. |
| --- | --- | --- | --- |
| options | object | Yes | Options to be passed to the MatterTileBody constructor. {@see Phaser.Physics.Matter.TileBody} |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World object.

> Source: [src/physics/matter-js/World.js#L1075](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1075)  
> Since: 3.0.0

---

## create

### <instance> create(x, y, width, height, options)

**Description:**

Creates a rectangle Matter body and adds it to the world.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal position of the body in the world. |
| --- | --- | --- | --- |
| y | number | No | The vertical position of the body in the world. |
| width | number | No | The width of the body. |
| height | number | No | The height of the body. |
| options | object | No | Optional Matter configuration object. |

**Returns:** MatterJS.BodyType - The Matter.js body that was created.

> Source: [src/physics/matter-js/World.js#L950](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L950)  
> Since: 3.0.0

---

## createDebugGraphic

### <instance> createDebugGraphic()

**Description:**

Creates a Phaser.GameObjects.Graphics object that is used to render all of the debug bodies and joints to.

This method is called automatically by the constructor, if debugging has been enabled.

The created Graphics object is automatically added to the Scene at 0x0 and given a depth of `Number.MAX_VALUE`,

so it renders above all else in the Scene.

The Graphics object is assigned to the `debugGraphic` property of this class and `drawDebug` is enabled.

**Returns:** [Phaser.GameObjects.Graphics](gameobjects-graphics.md) - The newly created Graphics object.

> Source: [src/physics/matter-js/World.js#L878](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L878)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Will remove all Matter physics event listeners and clear the matter physics world,

engine and any debug graphics, if any.

After destroying the world it cannot be re-used again.

**Overrides:** Phaser.Events.EventEmitter#destroy

> Source: [src/physics/matter-js/World.js#L2308](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L2308)  
> Since: 3.0.0

---

## disableGravity

### <instance> disableGravity()

**Description:**

Sets the world gravity and gravity scale to 0.

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World object.

> Source: [src/physics/matter-js/World.js#L906](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L906)  
> Since: 3.0.0

---

## emit

### <instance> emit(event, [args])

**Description:**

Calls each of the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| args | \* | Yes | Additional arguments that will be passed to the event handler. |

**Returns:** boolean - `true` if the event had listeners, else `false`.

**Inherits:** [Phaser.Events.EventEmitter#emit](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L86)  
> Since: 3.0.0

---

## eventNames

### <instance> eventNames()

**Description:**

Return an array listing the events for which the emitter has registered listeners.

**Returns:** Array.<(string | symbol)> - undefined

**Inherits:** [Phaser.Events.EventEmitter#eventNames](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L55)  
> Since: 3.0.0

---

## getAllBodies

### <instance> getAllBodies()

**Description:**

Returns all the bodies in the Matter World, including all bodies in children, recursively.

**Returns:** Array.<MatterJS.BodyType> - An array of all the Matter JS Bodies in this World.

> Source: [src/physics/matter-js/World.js#L1362](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1362)  
> Since: 3.22.0

---

## getAllComposites

### <instance> getAllComposites()

**Description:**

Returns all the composites in the Matter World, including all composites in children, recursively.

**Returns:** Array.<MatterJS.CompositeType> - An array of all the Matter JS Composites in this World.

> Source: [src/physics/matter-js/World.js#L1388](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1388)  
> Since: 3.22.0

---

## getAllConstraints

### <instance> getAllConstraints()

**Description:**

Returns all the constraints in the Matter World, including all constraints in children, recursively.

**Returns:** Array.<MatterJS.ConstraintType> - An array of all the Matter JS Constraints in this World.

> Source: [src/physics/matter-js/World.js#L1375](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1375)  
> Since: 3.22.0

---

## has

### <instance> has(body)

**Description:**

Returns `true` if the given body can be found within the World.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | MatterJS.Body | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Matter Body, or Game Object, to search for within the world. |
| --- | --- | --- | --- |

**Returns:** Array.<MatterJS.BodyType> - An array of all the Matter JS Bodies in this World.

> Source: [src/physics/matter-js/World.js#L1345](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1345)  
> Since: 3.22.0

---

## listenerCount

### <instance> listenerCount(event)

**Description:**

Return the number of listeners listening to a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** number - The number of listeners.

**Inherits:** [Phaser.Events.EventEmitter#listenerCount](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L75)  
> Since: 3.0.0

---

## listeners

### <instance> listeners(event)

**Description:**

Return the listeners registered for a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |

**Returns:** Array.<function()> - The registered listeners.

**Inherits:** [Phaser.Events.EventEmitter#listeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L64](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L64)  
> Since: 3.0.0

---

## nextCategory

### <instance> nextCategory()

**Description:**

Returns the next unique category bitfield (starting after the initial default category 0x0001).

There are 32 available.

**Returns:** number - Unique category bitfield

> Source: [src/physics/matter-js/World.js#L1120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1120)  
> Since: 3.0.0

---

## nextGroup

### <instance> nextGroup([isNonColliding])

**Description:**

Returns the next unique group index for which bodies will collide.

If `isNonColliding` is `true`, returns the next unique group index for which bodies will not collide.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| isNonColliding | boolean | Yes | false | If `true`, returns the next unique group index for which bodies will *not* collide. |
| --- | --- | --- | --- | --- |

**Returns:** number - Unique category bitfield

> Source: [src/physics/matter-js/World.js#L1104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1104)  
> Since: 3.0.0

---

## off

### <instance> off(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#off](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L151](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L151)  
> Since: 3.0.0

---

## on

### <instance> on(event, fn, [context])

**Description:**

Add a listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#on](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L98)  
> Since: 3.0.0

---

## once

### <instance> once(event, fn, [context])

**Description:**

Add a one-time listener for a given event.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| event | string | symbol | No |  | The event name. |
| --- | --- | --- | --- | --- |
| fn | function | No |  | The listener function. |
| context | \* | Yes | "this" | The context to invoke the listener with. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## pause

### <instance> pause()

**Description:**

Pauses this Matter World instance and sets `enabled` to `false`.

A paused world will not run any simulations for the duration it is paused.

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World object.

**Fires:** [Phaser.Physics.Matter.Events#event:PAUSE](../event/physics-matter-events.md)

> Source: [src/physics/matter-js/World.js#L1134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1134)  
> Since: 3.0.0

---

## remove

### <instance> remove(object, [deep])

**Description:**

Removes a Matter JS object, or array of objects, from the world.

The objects should be valid Matter JS entities, such as a Body, Composite or Constraint.

Triggers `beforeRemove` and `afterRemove` events.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| object | object | Array.<object> | No |  | Can be single object, or an array, and can be a body, composite or constraint. |
| --- | --- | --- | --- | --- |
| deep | boolean | Yes | false | Optionally search the objects children and recursively remove those as well. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World object.

> Source: [src/physics/matter-js/World.js#L994](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L994)  
> Since: 3.0.0

---

## removeAllListeners

### <instance> removeAllListeners([event])

**Description:**

Remove all listeners, or those of the specified event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | Yes | The event name. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeConstraint

### <instance> removeConstraint(constraint, [deep])

**Description:**

Removes a Matter JS constraint, or array of constraints, from the world.

Triggers `beforeRemove` and `afterRemove` events.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| constraint | MatterJS.ConstraintType | Array.<MatterJS.ConstraintType> | No |  | A Matter JS Constraint, or an array of constraints, to be removed. |
| --- | --- | --- | --- | --- |
| deep | boolean | Yes | false | Optionally search the objects children and recursively remove those as well. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World object.

> Source: [src/physics/matter-js/World.js#L1028](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1028)  
> Since: 3.0.0

---

## removeListener

### <instance> removeListener(event, [fn], [context], [once])

**Description:**

Remove the listeners of a given event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | string | symbol | No | The event name. |
| --- | --- | --- | --- |
| fn | function | Yes | Only remove the listeners that match this function. |
| context | \* | Yes | Only remove the listeners that have this context. |
| once | boolean | Yes | Only remove one-time listeners. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## renderBody

### <instance> renderBody(body, graphics, showInternalEdges, [lineColor], [lineOpacity], [lineThickness], [fillColor], [fillOpacity])

**Description:**

Renders a single Matter Body to the given Phaser Graphics Game Object.

This method is used internally by the Matter Debug Renderer, but is also exposed publically should

you wish to render a Body to your own Graphics instance.

If you don't wish to render a line around the body, set the `lineColor` parameter to `null`.

Equally, if you don't wish to render a fill, set the `fillColor` parameter to `null`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| body | MatterJS.BodyType | No |  | The Matter Body to be rendered. |
| --- | --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No |  | The Graphics object to render to. |
| showInternalEdges | boolean | No |  | Render internal edges of the polygon? |
| lineColor | number | Yes |  | The line color. |
| lineOpacity | number | Yes |  | The line opacity, between 0 and 1. |
| lineThickness | number | Yes | 1 | The line thickness. |
| fillColor | number | Yes |  | The fill color. |
| fillOpacity | number | Yes |  | The fill opacity, between 0 and 1. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World instance for method chaining.

> Source: [src/physics/matter-js/World.js#L1951](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1951)  
> Since: 3.22.0

---

## renderBodyAxes

### <instance> renderBodyAxes(bodies, graphics, showAxes, lineColor, lineOpacity)

**Description:**

Renders either all axes, or a single axis indicator, for an array of Bodies, to the given Graphics instance.

The debug renderer calls this method if the `showAxes` or `showAngleIndicator` config values are set.

This method is used internally by the Matter Debug Renderer, but is also exposed publically should

you wish to render bounds to your own Graphics instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | array | No | An array of bodies from the localWorld. |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Graphics object to render to. |
| showAxes | boolean | No | If `true` it will render all body axes. If `false` it will render a single axis indicator. |
| lineColor | number | No | The line color. |
| lineOpacity | number | No | The line opacity, between 0 and 1. |

> Source: [src/physics/matter-js/World.js#L1742](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1742)  
> Since: 3.22.0

---

## renderBodyBounds

### <instance> renderBodyBounds(bodies, graphics, lineColor, lineOpacity)

**Description:**

Renders the bounds of an array of Bodies to the given Graphics instance.

If the body is a compound body, it will render the bounds for the parent compound.

The debug renderer calls this method if the `showBounds` config value is set.

This method is used internally by the Matter Debug Renderer, but is also exposed publically should

you wish to render bounds to your own Graphics instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | array | No | An array of bodies from the localWorld. |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Graphics object to render to. |
| lineColor | number | No | The line color. |
| lineOpacity | number | No | The line opacity, between 0 and 1. |

> Source: [src/physics/matter-js/World.js#L1678](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1678)  
> Since: 3.22.0

---

## renderBodyVelocity

### <instance> renderBodyVelocity(bodies, graphics, lineColor, lineOpacity, lineThickness)

**Description:**

Renders a velocity indicator for an array of Bodies, to the given Graphics instance.

The debug renderer calls this method if the `showVelocity` config value is set.

This method is used internally by the Matter Debug Renderer, but is also exposed publically should

you wish to render bounds to your own Graphics instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | array | No | An array of bodies from the localWorld. |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Graphics object to render to. |
| lineColor | number | No | The line color. |
| lineOpacity | number | No | The line opacity, between 0 and 1. |
| lineThickness | number | No | The line thickness. |

> Source: [src/physics/matter-js/World.js#L1819](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1819)  
> Since: 3.22.0

---

## renderCollisions

### <instance> renderCollisions(pairs, graphics, lineColor)

**Description:**

Renders the list of collision points and normals to the given Graphics instance.

The debug renderer calls this method if the `showCollisions` config value is set.

This method is used internally by the Matter Debug Renderer, but is also exposed publically should

you wish to render the Grid to your own Graphics instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pairs | Array.<MatterJS.Pair> | No | An array of Matter Pairs to be rendered. |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Graphics object to render to. |
| lineColor | number | No | The line color. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World instance for method chaining.

> Source: [src/physics/matter-js/World.js#L1581](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1581)  
> Since: 3.22.0

---

## renderConstraint

### <instance> renderConstraint(constraint, graphics, lineColor, lineOpacity, lineThickness, pinSize, anchorColor, anchorSize)

**Description:**

Renders a single Matter Constraint, such as a Pin or a Spring, to the given Phaser Graphics Game Object.

This method is used internally by the Matter Debug Renderer, but is also exposed publically should

you wish to render a Constraint to your own Graphics instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| constraint | MatterJS.ConstraintType | No | The Matter Constraint to render. |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Graphics object to render to. |
| lineColor | number | No | The line color. |
| lineOpacity | number | No | The line opacity, between 0 and 1. |
| lineThickness | number | No | The line thickness. |
| pinSize | number | No | If this constraint is a pin, this sets the size of the pin circle. |
| anchorColor | number | No | The color used when rendering this constraints anchors. Set to `null` to not render anchors. |
| anchorSize | number | No | The size of the anchor circle, if this constraint has anchors and is rendering them. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World instance for method chaining.

> Source: [src/physics/matter-js/World.js#L2169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L2169)  
> Since: 3.22.0

---

## renderConvexHull

### <instance> renderConvexHull(body, graphics, hullColor, [lineThickness])

**Description:**

Renders the Convex Hull for a single Matter Body to the given Phaser Graphics Game Object.

This method is used internally by the Matter Debug Renderer, but is also exposed publically should

you wish to render a Body hull to your own Graphics instance.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| body | MatterJS.BodyType | No |  | The Matter Body to be rendered. |
| --- | --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No |  | The Graphics object to render to. |
| hullColor | number | No |  | The color used to render the hull. |
| lineThickness | number | Yes | 1 | The hull line thickness. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World instance for method chaining.

> Source: [src/physics/matter-js/World.js#L2091](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L2091)  
> Since: 3.22.0

---

## renderGrid

### <instance> renderGrid(grid, graphics, lineColor, lineOpacity)

**Description:**

Renders the Engine Broadphase Controller Grid to the given Graphics instance.

The debug renderer calls this method if the `showBroadphase` config value is set.

This method is used internally by the Matter Debug Renderer, but is also exposed publically should

you wish to render the Grid to your own Graphics instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| grid | MatterJS.Grid | No | The Matter Grid to be rendered. |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Graphics object to render to. |
| lineColor | number | No | The line color. |
| lineOpacity | number | No | The line opacity, between 0 and 1. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World instance for method chaining.

> Source: [src/physics/matter-js/World.js#L1466](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1466)  
> Since: 3.22.0

---

## renderSeparations

### <instance> renderSeparations(pairs, graphics, lineColor)

**Description:**

Renders the list of Pair separations to the given Graphics instance.

The debug renderer calls this method if the `showSeparations` config value is set.

This method is used internally by the Matter Debug Renderer, but is also exposed publically should

you wish to render the Grid to your own Graphics instance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pairs | Array.<MatterJS.Pair> | No | An array of Matter Pairs to be rendered. |
| --- | --- | --- | --- |
| graphics | [Phaser.GameObjects.Graphics](gameobjects-graphics.md) | No | The Graphics object to render to. |
| lineColor | number | No | The line color. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World instance for method chaining.

> Source: [src/physics/matter-js/World.js#L1512](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1512)  
> Since: 3.22.0

---

## resetCollisionIDs

### <instance> resetCollisionIDs()

**Description:**

Resets the internal collision IDs that Matter.JS uses for Body collision groups.

You should call this before destroying your game if you need to restart the game

again on the same page, without first reloading the page. Or, if you wish to

consistently destroy a Scene that contains Matter.js and then run it again

later in the same game.

> Source: [src/physics/matter-js/World.js#L2265](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L2265)  
> Since: 3.17.0

---

## resume

### <instance> resume()

**Description:**

Resumes this Matter World instance from a paused state and sets `enabled` to `true`.

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World object.

**Fires:** [Phaser.Physics.Matter.Events#event:RESUME](../event/physics-matter-events.md)

> Source: [src/physics/matter-js/World.js#L1154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1154)  
> Since: 3.0.0

---

## setBodyRenderStyle

### <instance> setBodyRenderStyle(body, [lineColor], [lineOpacity], [lineThickness], [fillColor], [fillOpacity])

**Description:**

Sets the debug render style for the given Matter Body.

If you are using this on a Phaser Game Object, such as a Matter Sprite, then pass in the body property

to this method, not the Game Object itself.

If you wish to skip a parameter, so it retains its current value, pass `false` for it.

If you wish to reset the Body render colors to the defaults found in the World Debug Config, then call

this method with just the `body` parameter provided and no others.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| body | MatterJS.BodyType | No | The Matter Body to set the render style on. |
| --- | --- | --- | --- |
| lineColor | number | Yes | The line color. If `null` it will use the World Debug Config value. |
| lineOpacity | number | Yes | The line opacity, between 0 and 1. If `null` it will use the World Debug Config value. |
| lineThickness | number | Yes | The line thickness. If `null` it will use the World Debug Config value. |
| fillColor | number | Yes | The fill color. If `null` it will use the World Debug Config value. |
| fillOpacity | number | Yes | The fill opacity, between 0 and 1. If `null` it will use the World Debug Config value. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World instance for method chaining.

> Source: [src/physics/matter-js/World.js#L384](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L384)  
> Since: 3.22.0

---

## setBounds

### <instance> setBounds([x], [y], [width], [height], [thickness], [left], [right], [top], [bottom])

**Description:**

Sets the bounds of the Physics world to match the given world pixel dimensions.

You can optionally set which 'walls' to create: left, right, top or bottom.

If none of the walls are given it will default to use the walls settings it had previously.

I.e. if you previously told it to not have the left or right walls, and you then adjust the world size

the newly created bounds will also not have the left and right walls.

Explicitly state them in the parameters to override this.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The x coordinate of the top-left corner of the bounds. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The y coordinate of the top-left corner of the bounds. |
| width | number | Yes |  | The width of the bounds. |
| height | number | Yes |  | The height of the bounds. |
| thickness | number | Yes | 64 | The thickness of each wall, in pixels. |
| left | boolean | Yes | true | If true will create the left bounds wall. |
| right | boolean | Yes | true | If true will create the right bounds wall. |
| top | boolean | Yes | true | If true will create the top bounds wall. |
| bottom | boolean | Yes | true | If true will create the bottom bounds wall. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World object.

> Source: [src/physics/matter-js/World.js#L792](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L792)  
> Since: 3.0.0

---

## setCompositeRenderStyle

### <instance> setCompositeRenderStyle(composite)

**Description:**

Sets the debug render style for the children of the given Matter Composite.

Composites themselves do not render, but they can contain bodies, constraints and other composites that may do.

So the children of this composite are passed to the `setBodyRenderStyle`, `setCompositeRenderStyle` and

`setConstraintRenderStyle` methods accordingly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| composite | MatterJS.CompositeType | No | The Matter Composite to set the render style on. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World instance for method chaining.

> Source: [src/physics/matter-js/World.js#L334](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L334)  
> Since: 3.22.0

---

## setConstraintRenderStyle

### <instance> setConstraintRenderStyle(constraint, [lineColor], [lineOpacity], [lineThickness], [pinSize], [anchorColor], [anchorSize])

**Description:**

Sets the debug render style for the given Matter Constraint.

If you are using this on a Phaser Game Object, then pass in the body property

to this method, not the Game Object itself.

If you wish to skip a parameter, so it retains its current value, pass `false` for it.

If you wish to reset the Constraint render colors to the defaults found in the World Debug Config, then call

this method with just the `constraint` parameter provided and no others.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| constraint | MatterJS.ConstraintType | No | The Matter Constraint to set the render style on. |
| --- | --- | --- | --- |
| lineColor | number | Yes | The line color. If `null` it will use the World Debug Config value. |
| lineOpacity | number | Yes | The line opacity, between 0 and 1. If `null` it will use the World Debug Config value. |
| lineThickness | number | Yes | The line thickness. If `null` it will use the World Debug Config value. |
| pinSize | number | Yes | If this constraint is a pin, this sets the size of the pin circle. If `null` it will use the World Debug Config value. |
| anchorColor | number | Yes | The color used when rendering this constraints anchors. If `null` it will use the World Debug Config value. |
| anchorSize | number | Yes | The size of the anchor circle, if this constraint has anchors. If `null` it will use the World Debug Config value. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World instance for method chaining.

> Source: [src/physics/matter-js/World.js#L470](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L470)  
> Since: 3.22.0

---

## setEventsProxy

### <instance> setEventsProxy()

**Description:**

This internal method acts as a proxy between all of the Matter JS events and then re-emits them

via this class.

> Source: [src/physics/matter-js/World.js#L581](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L581)  
> Since: 3.0.0

---

## setGravity

### <instance> setGravity([x], [y], [scale])

**Description:**

Sets the worlds gravity to the values given.

Gravity effects all bodies in the world, unless they have the `ignoreGravity` flag set.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The world gravity x component. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 1 | The world gravity y component. |
| scale | number | Yes | 0.001 | The gravity scale factor. |

**Returns:** [Phaser.Physics.Matter.World](physics-matter-world.md) - This Matter World object.

> Source: [src/physics/matter-js/World.js#L923](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L923)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

Will remove all Matter physics event listeners and clear the matter physics world,

engine and any debug graphics, if any.

**Overrides:** Phaser.Events.EventEmitter#shutdown

> Source: [src/physics/matter-js/World.js#L2285](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L2285)  
> Since: 3.0.0

---

## step

### <instance> step([delta])

**Description:**

Manually advances the physics simulation by one iteration.

You can optionally pass in the `delta` and `correction` values to be used by Engine.update.

If undefined they use the Matter defaults of 60Hz and no correction.

Calling `step` directly bypasses any checks of `enabled` or `autoUpdate`.

It also ignores any custom `getDelta` functions, as you should be passing the delta

value in to this call.

You can adjust the number of iterations that Engine.update performs internally.

Use the Scene Matter Physics config object to set the following properties:

positionIterations (defaults to 6)

velocityIterations (defaults to 4)

constraintIterations (defaults to 2)

Adjusting these values can help performance in certain situations, depending on the physics requirements

of your game.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| delta | number | Yes | 16.666 | The delta value. |
| --- | --- | --- | --- | --- |

> Source: [src/physics/matter-js/World.js#L1288](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1288)  
> Since: 3.4.0

---

## update

### <instance> update(time, delta)

**Description:**

The internal update method. This is called automatically by the parent Scene.

Moves the simulation forward in time by delta ms. Uses `World.correction` value as an optional number that

specifies the time correction factor to apply to the update. This can help improve the accuracy of the

simulation in cases where delta is changing between updates. The value of correction is defined as `delta / lastDelta`,

i.e. the percentage change of delta over the last step. Therefore the value is always 1 (no correction) when

delta is constant (or when no correction is desired, which is the default).

See the paper on Time Corrected Verlet for more information.

Triggers `beforeUpdate` and `afterUpdate` events. Triggers `collisionStart`, `collisionActive` and `collisionEnd` events.

If the World is paused, `update` is still run, but exits early and does not update the Matter Engine.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/physics/matter-js/World.js#L1174](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1174)  
> Since: 3.0.0

---

## update30Hz

### <instance> update30Hz()

**Description:**

Runs the Matter Engine.update at a fixed timestep of 30Hz.

**Returns:** number - The delta value to be passed to Engine.update.

> Source: [src/physics/matter-js/World.js#L1332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1332)  
> Since: 3.4.0

---

## update60Hz

### <instance> update60Hz()

**Description:**

Runs the Matter Engine.update at a fixed timestep of 60Hz.

**Returns:** number - The delta value to be passed to Engine.update.

> Source: [src/physics/matter-js/World.js#L1319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1319)  
> Since: 3.4.0

---

## updateWall

### <instance> updateWall(add, [position], [x], [y], [width], [height])

**Description:**

Updates the 4 rectangle bodies that were created, if `setBounds` was set in the Matter config, to use

the new positions and sizes. This method is usually only called internally via the `setBounds` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| add | boolean | No | `true` if the walls are being added or updated, `false` to remove them from the world. |
| --- | --- | --- | --- |
| position | string | Yes | Either `left`, `right`, `top` or `bottom`. Only optional if `add` is `false`. |
| x | number | Yes | The horizontal position to place the walls at. Only optional if `add` is `false`. |
| y | number | Yes | The vertical position to place the walls at. Only optional if `add` is `false`. |
| width | number | Yes | The width of the walls, in pixels. Only optional if `add` is `false`. |
| height | number | Yes | The height of the walls, in pixels. Only optional if `add` is `false`. |

> Source: [src/physics/matter-js/World.js#L836](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L836)  
> Since: 3.0.0

---

# Private Methods

## postUpdate

### <instance> postUpdate()

**Description:**

Handles the rendering of bodies and debug information to the debug Graphics object, if enabled.

This method is called automatically by the Scene after all processing has taken place.

**Access:** private

> Source: [src/physics/matter-js/World.js#L1401](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1401)  
> Since: 3.0.0

---

## renderBodies

### <instance> renderBodies(bodies)

**Description:**

Renders the given array of Bodies to the debug graphics instance.

Called automatically by the `postUpdate` method.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| bodies | array | No | An array of bodies from the localWorld. |
| --- | --- | --- | --- |

> Source: [src/physics/matter-js/World.js#L1861](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L1861)  
> Since: 3.14.0

---

## renderJoints

### <instance> renderJoints()

**Description:**

Renders all of the constraints in the world (unless they are specifically set to invisible).

Called automatically by the `postUpdate` method.

**Access:** private

> Source: [src/physics/matter-js/World.js#L2138](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/World.js#L2138)  
> Since: 3.14.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [autoUpdate](#autoupdate)

    - [autoUpdate: boolean](#autoupdate-boolean)
  + [debugConfig](#debugconfig)

    - [debugConfig: Phaser.Types.Physics.Matter.MatterDebugConfig](#debugconfig-phasertypesphysicsmattermatterdebugconfig)
  + [debugGraphic](#debuggraphic)

    - [debugGraphic: Phaser.GameObjects.Graphics](#debuggraphic-phasergameobjectsgraphics)
  + [drawDebug](#drawdebug)

    - [drawDebug: boolean](#drawdebug-boolean)
  + [enabled](#enabled)

    - [enabled: boolean](#enabled-boolean)
  + [engine](#engine)

    - [engine: MatterJS.Engine](#engine-matterjsengine)
  + [getDelta](#getdelta)

    - [getDelta: function](#getdelta-function)
  + [localWorld](#localworld)

    - [localWorld: MatterJS.World](#localworld-matterjsworld)
  + [runner](#runner)

    - [runner: Phaser.Types.Physics.Matter.MatterRunnerConfig](#runner-phasertypesphysicsmattermatterrunnerconfig)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [walls](#walls)

    - [walls: Phaser.Types.Physics.Matter.MatterWalls](#walls-phasertypesphysicsmattermatterwalls)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(object)](#instance-addobject)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [convertTilemapLayer](#converttilemaplayer)

    - [<instance> convertTilemapLayer(tilemapLayer, [options])](#instance-converttilemaplayertilemaplayer-options)
  + [convertTiles](#converttiles)

    - [<instance> convertTiles(tiles, [options])](#instance-converttilestiles-options)
  + [create](#create)

    - [<instance> create(x, y, width, height, options)](#instance-createx-y-width-height-options)
  + [createDebugGraphic](#createdebuggraphic)

    - [<instance> createDebugGraphic()](#instance-createdebuggraphic)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [disableGravity](#disablegravity)

    - [<instance> disableGravity()](#instance-disablegravity)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [getAllBodies](#getallbodies)

    - [<instance> getAllBodies()](#instance-getallbodies)
  + [getAllComposites](#getallcomposites)

    - [<instance> getAllComposites()](#instance-getallcomposites)
  + [getAllConstraints](#getallconstraints)

    - [<instance> getAllConstraints()](#instance-getallconstraints)
  + [has](#has)

    - [<instance> has(body)](#instance-hasbody)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [nextCategory](#nextcategory)

    - [<instance> nextCategory()](#instance-nextcategory)
  + [nextGroup](#nextgroup)

    - [<instance> nextGroup([isNonColliding])](#instance-nextgroupisnoncolliding)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [pause](#pause)

    - [<instance> pause()](#instance-pause)
  + [remove](#remove)

    - [<instance> remove(object, [deep])](#instance-removeobject-deep)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeConstraint](#removeconstraint)

    - [<instance> removeConstraint(constraint, [deep])](#instance-removeconstraintconstraint-deep)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [renderBody](#renderbody)

    - [<instance> renderBody(body, graphics, showInternalEdges, [lineColor], [lineOpacity], [lineThickness], [fillColor], [fillOpacity])](#instance-renderbodybody-graphics-showinternaledges-linecolor-lineopacity-linethickness-fillcolor-fillopacity)
  + [renderBodyAxes](#renderbodyaxes)

    - [<instance> renderBodyAxes(bodies, graphics, showAxes, lineColor, lineOpacity)](#instance-renderbodyaxesbodies-graphics-showaxes-linecolor-lineopacity)
  + [renderBodyBounds](#renderbodybounds)

    - [<instance> renderBodyBounds(bodies, graphics, lineColor, lineOpacity)](#instance-renderbodyboundsbodies-graphics-linecolor-lineopacity)
  + [renderBodyVelocity](#renderbodyvelocity)

    - [<instance> renderBodyVelocity(bodies, graphics, lineColor, lineOpacity, lineThickness)](#instance-renderbodyvelocitybodies-graphics-linecolor-lineopacity-linethickness)
  + [renderCollisions](#rendercollisions)

    - [<instance> renderCollisions(pairs, graphics, lineColor)](#instance-rendercollisionspairs-graphics-linecolor)
  + [renderConstraint](#renderconstraint)

    - [<instance> renderConstraint(constraint, graphics, lineColor, lineOpacity, lineThickness, pinSize, anchorColor, anchorSize)](#instance-renderconstraintconstraint-graphics-linecolor-lineopacity-linethickness-pinsize-anchorcolor-anchorsize)
  + [renderConvexHull](#renderconvexhull)

    - [<instance> renderConvexHull(body, graphics, hullColor, [lineThickness])](#instance-renderconvexhullbody-graphics-hullcolor-linethickness)
  + [renderGrid](#rendergrid)

    - [<instance> renderGrid(grid, graphics, lineColor, lineOpacity)](#instance-rendergridgrid-graphics-linecolor-lineopacity)
  + [renderSeparations](#renderseparations)

    - [<instance> renderSeparations(pairs, graphics, lineColor)](#instance-renderseparationspairs-graphics-linecolor)
  + [resetCollisionIDs](#resetcollisionids)

    - [<instance> resetCollisionIDs()](#instance-resetcollisionids)
  + [resume](#resume)

    - [<instance> resume()](#instance-resume)
  + [setBodyRenderStyle](#setbodyrenderstyle)

    - [<instance> setBodyRenderStyle(body, [lineColor], [lineOpacity], [lineThickness], [fillColor], [fillOpacity])](#instance-setbodyrenderstylebody-linecolor-lineopacity-linethickness-fillcolor-fillopacity)
  + [setBounds](#setbounds)

    - [<instance> setBounds([x], [y], [width], [height], [thickness], [left], [right], [top], [bottom])](#instance-setboundsx-y-width-height-thickness-left-right-top-bottom)
  + [setCompositeRenderStyle](#setcompositerenderstyle)

    - [<instance> setCompositeRenderStyle(composite)](#instance-setcompositerenderstylecomposite)
  + [setConstraintRenderStyle](#setconstraintrenderstyle)

    - [<instance> setConstraintRenderStyle(constraint, [lineColor], [lineOpacity], [lineThickness], [pinSize], [anchorColor], [anchorSize])](#instance-setconstraintrenderstyleconstraint-linecolor-lineopacity-linethickness-pinsize-anchorcolor-anchorsize)
  + [setEventsProxy](#seteventsproxy)

    - [<instance> setEventsProxy()](#instance-seteventsproxy)
  + [setGravity](#setgravity)

    - [<instance> setGravity([x], [y], [scale])](#instance-setgravityx-y-scale)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [step](#step)

    - [<instance> step([delta])](#instance-stepdelta)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)
  + [update30Hz](#update30hz)

    - [<instance> update30Hz()](#instance-update30hz)
  + [update60Hz](#update60hz)

    - [<instance> update60Hz()](#instance-update60hz)
  + [updateWall](#updatewall)

    - [<instance> updateWall(add, [position], [x], [y], [width], [height])](#instance-updatewalladd-position-x-y-width-height)
* [Private Methods](#private-methods)

  + [postUpdate](#postupdate)

    - [<instance> postUpdate()](#instance-postupdate)
  + [renderBodies](#renderbodies)

    - [<instance> renderBodies(bodies)](#instance-renderbodiesbodies)
  + [renderJoints](#renderjoints)

    - [<instance> renderJoints()](#instance-renderjoints)

Back to top

©2025[Phaser](https://docs.phaser.io)