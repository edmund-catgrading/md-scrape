# StaticGroup

Phaser.Physics.Arcade.StaticGroup

An Arcade Physics Static Group object.

All Game Objects created by or added to this Group will automatically be given static Arcade Physics bodies, if they have no body.

Its dynamic counterpart is [Phaser.Physics.Arcade.Group](Phaser.Physics.Arcade.Group.md).

**Constructor**

`new StaticGroup(world, scene, [children], [config])`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| world | [Phaser.Physics.Arcade.World](physics-arcade-world.md) | No | The physics simulation. |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The scene this group belongs to. |
| children | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | [Phaser.Types.GameObjects.Group.GroupConfig](../typedef/types-gameobjects-group.md) | [Phaser.Types.GameObjects.Group.GroupCreateConfig](../typedef/types-gameobjects-group.md) | Yes |
| config | [Phaser.Types.GameObjects.Group.GroupConfig](../typedef/types-gameobjects-group.md) | [Phaser.Types.GameObjects.Group.GroupCreateConfig](../typedef/types-gameobjects-group.md) | Yes | Settings for this group. |

---

**Scope**: static

**Extends**

> [Phaser.GameObjects.Group](gameobjects-group.md)  
> [Phaser.Physics.Arcade.Components.Collision](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/StaticPhysicsGroup.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticPhysicsGroup.js#L15)  
> Since: 3.0.0

# Public Members

## active

### active: boolean

**Description:**

Whether this group runs its [Phaser.GameObjects.Group#preUpdate](gameobjects-group.md) method (which may update any members).

**Inherits:** [Phaser.GameObjects.Group#active](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L147](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L147)  
> Since: 3.0.0

---

## children

### children: Phaser.Structs.Set.<Phaser.GameObjects.GameObject>

**Description:**

Members of this group.

**Inherits:** [Phaser.GameObjects.Group#children](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L95](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L95)  
> Since: 3.0.0

---

## classType

### classType: function

**Description:**

The class to create new group members from.

**Inherits:** [Phaser.GameObjects.Group#classType](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L125](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L125)  
> Since: 3.0.0

---

## collisionCategory

### collisionCategory: number

**Description:**

The Arcade Physics Static Group Collision Category.

This can be set to any valid collision bitfield value.

See the `setCollisionCategory` method for more details.

> Source: [src/physics/arcade/StaticPhysicsGroup.js#L110](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticPhysicsGroup.js#L110)  
> Since: 3.70.0

---

## collisionMask

### collisionMask: number

**Description:**

The Arcade Physics Static Group Collision Mask.

See the `setCollidesWith` method for more details.

> Source: [src/physics/arcade/StaticPhysicsGroup.js#L123](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticPhysicsGroup.js#L123)  
> Since: 3.70.0

---

## createCallback

### createCallback: [Phaser.Types.GameObjects.Group.GroupCallback](../typedef/types-gameobjects-group.md)

**Description:**

A function to be called when adding or creating group members.

**Inherits:** [Phaser.GameObjects.Group#createCallback](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L198](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L198)  
> Since: 3.0.0

---

## createMultipleCallback

### createMultipleCallback: [Phaser.Types.GameObjects.Group.GroupMultipleCreateCallback](../typedef/types-gameobjects-group.md)

**Description:**

A function to be called when creating several group members at once.

**Inherits:** [Phaser.GameObjects.Group#createMultipleCallback](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L216)  
> Since: 3.0.0

---

## defaultFrame

### defaultFrame: string, number

**Description:**

A default texture frame to use when creating new group members.

**Inherits:** [Phaser.GameObjects.Group#defaultFrame](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L178](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L178)  
> Since: 3.0.0

---

## defaultKey

### defaultKey: string

**Description:**

A default texture key to use when creating new group members.

This is used in [Phaser.GameObjects.Group#create](gameobjects-group.md)

but not in [Phaser.GameObjects.Group#createMultiple](gameobjects-group.md).

**Inherits:** [Phaser.GameObjects.Group#defaultKey](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L166)  
> Since: 3.0.0

---

## isParent

### isParent: boolean

**Description:**

A flag identifying this object as a group.

**Inherits:** [Phaser.GameObjects.Group#isParent](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L104)  
> Since: 3.0.0

---

## maxSize

### maxSize: number

**Description:**

The maximum size of this group, if used as a pool. -1 is no limit.

**Inherits:** [Phaser.GameObjects.Group#maxSize](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L156](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L156)  
> Since: 3.0.0

---

## name

### name: string

**Description:**

The name of this group.

Empty by default and never populated by Phaser, this is left for developers to use.

**Inherits:** [Phaser.GameObjects.Group#name](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L136)  
> Since: 3.18.0

---

## physicsType

### physicsType: number

**Description:**

The scene this group belongs to.

> Source: [src/physics/arcade/StaticPhysicsGroup.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticPhysicsGroup.js#L100)  
> Since: 3.0.0

---

## removeCallback

### removeCallback: [Phaser.Types.GameObjects.Group.GroupCallback](../typedef/types-gameobjects-group.md)

**Description:**

A function to be called when removing group members.

**Inherits:** [Phaser.GameObjects.Group#removeCallback](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L207](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L207)  
> Since: 3.0.0

---

## runChildUpdate

### runChildUpdate: boolean

**Description:**

Whether to call the update method of any members.

**Inherits:** [Phaser.GameObjects.Group#runChildUpdate](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L187)  
> Since: 3.0.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

This scene this group belongs to.

**Inherits:** [Phaser.GameObjects.Group#scene](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L86)  
> Since: 3.0.0

---

## type

### type: string

**Description:**

A textual representation of this Game Object.

Used internally by Phaser but is available for your own custom classes to populate.

**Overrides:** Phaser.GameObjects.Group#type

> Source: [src/physics/arcade/StaticPhysicsGroup.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticPhysicsGroup.js#L136)  
> Since: 3.21.0

---

## world

### world: [Phaser.Physics.Arcade.World](physics-arcade-world.md)

**Description:**

The physics simulation.

> Source: [src/physics/arcade/StaticPhysicsGroup.js#L91](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticPhysicsGroup.js#L91)  
> Since: 3.0.0

---

# Private Members

## internalCreateCallback

### internalCreateCallback: [Phaser.Types.GameObjects.Group.GroupCallback](../typedef/types-gameobjects-group.md)

**Description:**

A function to be called when adding or creating group members.

For internal use only by a Group, or any class that extends it.

**Access:** private

**Inherits:** [Phaser.GameObjects.Group#internalCreateCallback](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L225](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L225)  
> Since: 3.22.0

---

## internalRemoveCallback

### internalRemoveCallback: [Phaser.Types.GameObjects.Group.GroupCallback](../typedef/types-gameobjects-group.md)

**Description:**

A function to be called when removing group members.

For internal use only by a Group, or any class that extends it.

**Access:** private

**Inherits:** [Phaser.GameObjects.Group#internalRemoveCallback](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L236](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L236)  
> Since: 3.22.0

---

# Public Methods

## add

### <instance> add(child, [addToScene])

**Description:**

Adds a Game Object to this group.

Calls [Phaser.GameObjects.Group#createCallback](gameobjects-group.md).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object to add. |
| --- | --- | --- | --- | --- |
| addToScene | boolean | Yes | false | Also add the Game Object to the scene. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#add](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L575](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L575)  
> Since: 3.0.0

---

## addCollidesWith

### <instance> addCollidesWith(category)

**Description:**

Adds the given Collision Category to the list of those that this

Arcade Physics Body will collide with.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category to add. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#addCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L60](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L60)  
> Since: 3.70.0

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

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addMultiple

### <instance> addMultiple(children, [addToScene])

**Description:**

Adds several Game Objects to this group.

Calls [Phaser.GameObjects.Group#createCallback](gameobjects-group.md).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| children | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No |  | The Game Objects to add. |
| --- | --- | --- | --- | --- |
| addToScene | boolean | Yes | false | Also add the Game Objects to the scene. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This group.

**Inherits:** [Phaser.GameObjects.Group#addMultiple](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L620](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L620)  
> Since: 3.0.0

---

## angle

### <instance> angle(value, [step])

**Description:**

Sets the angle of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the angle to, in degrees. |
| --- | --- | --- | --- | --- |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#angle](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1392](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1392)  
> Since: 3.21.0

---

## clear

### <instance> clear([removeFromScene], [destroyChild])

**Description:**

Removes all members of this Group and optionally removes them from the Scene and / or destroys them.

Does not call [Phaser.GameObjects.Group#removeCallback](gameobjects-group.md).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| removeFromScene | boolean | Yes | false | Optionally remove each Group member from the Scene. |
| --- | --- | --- | --- | --- |
| destroyChild | boolean | Yes | false | Optionally call destroy on the removed Group members. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This group.

**Inherits:** [Phaser.GameObjects.Group#clear](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L699](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L699)  
> Since: 3.0.0

---

## contains

### <instance> contains(child)

**Description:**

Tests if a Game Object is a member of this group.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | A Game Object. |
| --- | --- | --- | --- |

**Returns:** boolean - True if the Game Object is a member of this group.

**Inherits:** [Phaser.GameObjects.Group#contains](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L741](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L741)  
> Since: 3.0.0

---

## countActive

### <instance> countActive([value])

**Description:**

Counts the number of active (or inactive) group members.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | Count active (true) or inactive (false) group members. |
| --- | --- | --- | --- | --- |

**Returns:** number - The number of group members with an active state matching the `active` argument.

**Inherits:** [Phaser.GameObjects.Group#countActive](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1122)  
> Since: 3.0.0

---

## create

### <instance> create([x], [y], [key], [frame], [visible], [active])

**Description:**

Creates a new Game Object and adds it to this group, unless the group [is](gameobjects-group.md).

Calls [Phaser.GameObjects.Group#createCallback](gameobjects-group.md).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes | 0 | The horizontal position of the new Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes | 0 | The vertical position of the new Game Object in the world. |
| key | string | Yes | "defaultKey" | The texture key of the new Game Object. |
| frame | string | number | Yes | "defaultFrame" | The texture frame of the new Game Object. |
| visible | boolean | Yes | true | The {@link Phaser.GameObjects.Components.Visible#visible} state of the new Game Object. |
| active | boolean | Yes | true | The {@link Phaser.GameObjects.GameObject#active} state of the new Game Object. |

**Returns:** any - The new Game Object (usually a Sprite, etc.).

**Inherits:** [Phaser.GameObjects.Group#create](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L273](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L273)  
> Since: 3.0.0

---

## createCallbackHandler

### <instance> createCallbackHandler(child)

**Description:**

Adds a static physics body to the new group member (if it lacks one) and adds it to the simulation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The new group member. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/StaticPhysicsGroup.js#L148](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticPhysicsGroup.js#L148)  
> Since: 3.0.0

---

## createFromConfig

### <instance> createFromConfig(options)

**Description:**

A helper for [Phaser.GameObjects.Group#createMultiple](gameobjects-group.md).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| options | [Phaser.Types.GameObjects.Group.GroupCreateConfig](../typedef/types-gameobjects-group.md) | No | Creation settings. |
| --- | --- | --- | --- |

**Returns:** Array.<any> - The newly created Game Objects.

**Inherits:** [Phaser.GameObjects.Group#createFromConfig](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L359](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L359)  
> Since: 3.0.0

---

## createMultiple

### <instance> createMultiple(config)

**Description:**

Creates several Game Objects and adds them to this group.

If the group becomes [Phaser.GameObjects.Group#isFull](gameobjects-group.md), no further Game Objects are created.

Calls [Phaser.GameObjects.Group#createMultipleCallback](gameobjects-group.md) and [Phaser.GameObjects.Group#createCallback](gameobjects-group.md).

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.GameObjects.Group.GroupCreateConfig](../typedef/types-gameobjects-group.md) | Array.<[Phaser.Types.GameObjects.Group.GroupCreateConfig](../typedef/types-gameobjects-group.md)> | No | Creation settings. This can be a single configuration object or an array of such objects, which will be applied in turn. |
| --- | --- | --- | --- |

**Returns:** Array.<any> - The newly created Game Objects.

**Inherits:** [Phaser.GameObjects.Group#createMultiple](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L318](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L318)  
> Since: 3.0.0

---

## createMultipleCallbackHandler

### <instance> createMultipleCallbackHandler(entries)

**Description:**

Refreshes the group.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| entries | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | The newly created group members. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/StaticPhysicsGroup.js#L184](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticPhysicsGroup.js#L184)  
> Since: 3.0.0

---

## destroy

### <instance> destroy([destroyChildren], [removeFromScene])

**Description:**

Empties this Group of all children and removes it from the Scene.

Does not call [Phaser.GameObjects.Group#removeCallback](gameobjects-group.md).

Children of this Group will *not* be removed from the Scene by calling this method

unless you specify the `removeFromScene` parameter.

Children of this Group will also *not* be destroyed by calling this method

unless you specify the `destroyChildren` parameter.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| destroyChildren | boolean | Yes | false | Also {@link Phaser.GameObjects.GameObject#destroy} each Group member. |
| --- | --- | --- | --- | --- |
| removeFromScene | boolean | Yes | false | Optionally remove each Group member from the Scene. |

**Inherits:** [Phaser.GameObjects.Group#destroy](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1714](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1714)  
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

## get

### <instance> get([x], [y], [key], [frame], [visible])

**Description:**

Scans the group for the first member that has an [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md) state set to `false`,

assigns `x` and `y`, and returns the member.

If no inactive member is found and the group isn't full then it will create a new Game Object using `x`, `y`, `key`, `frame`, and `visible`.

The new Game Object will have its active state set to `true`.

Unless a new member is created, `key`, `frame`, and `visible` are ignored.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | Yes |  | The horizontal position of the Game Object in the world. |
| --- | --- | --- | --- | --- |
| y | number | Yes |  | The vertical position of the Game Object in the world. |
| key | string | Yes | "defaultKey" | The texture key assigned to a new Game Object (if one is created). |
| frame | string | number | Yes | "defaultFrame" | A texture frame assigned to a new Game Object (if one is created). |
| visible | boolean | Yes | true | The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created). |

**Returns:** any - The first inactive group member, or a newly created member, or null.

**Inherits:** [Phaser.GameObjects.Group#get](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1011](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1011)  
> Since: 3.0.0

---

## getChildren

### <instance> getChildren()

**Description:**

All members of the group.

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - The group members.

**Inherits:** [Phaser.GameObjects.Group#getChildren](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L756](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L756)  
> Since: 3.0.0

---

## getFirst

### <instance> getFirst([state], [createIfNull], [x], [y], [key], [frame], [visible])

**Description:**

Scans the Group, from top to bottom, for the first member that has an [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md) state matching the argument,

assigns `x` and `y`, and returns the member.

If no matching member is found and `createIfNull` is true and the group isn't full then it will create a new Game Object using `x`, `y`, `key`, `frame`, and `visible`.

Unless a new member is created, `key`, `frame`, and `visible` are ignored.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| state | boolean | Yes | false | The {@link Phaser.GameObjects.GameObject#active} value to match. |
| --- | --- | --- | --- | --- |
| createIfNull | boolean | Yes | false | Create a new Game Object if no matching members are found, using the following arguments. |
| x | number | Yes |  | The horizontal position of the Game Object in the world. |
| y | number | Yes |  | The vertical position of the Game Object in the world. |
| key | string | Yes | "defaultKey" | The texture key assigned to a new Game Object (if one is created). |
| frame | string | number | Yes | "defaultFrame" | A texture frame assigned to a new Game Object (if one is created). |
| visible | boolean | Yes | true | The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created). |

**Returns:** any - The first matching group member, or a newly created member, or null.

**Inherits:** [Phaser.GameObjects.Group#getFirst](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L806](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L806)  
> Since: 3.0.0

---

## getFirstAlive

### <instance> getFirstAlive([createIfNull], [x], [y], [key], [frame], [visible])

**Description:**

Scans the group for the first member that has an [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md) state set to `true`,

assigns `x` and `y`, and returns the member.

If no active member is found and `createIfNull` is `true` and the group isn't full then it will create a new one using `x`, `y`, `key`, `frame`, and `visible`.

Unless a new member is created, `key`, `frame`, and `visible` are ignored.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| createIfNull | boolean | Yes | false | Create a new Game Object if no matching members are found, using the following arguments. |
| --- | --- | --- | --- | --- |
| x | number | Yes |  | The horizontal position of the Game Object in the world. |
| y | number | Yes |  | The vertical position of the Game Object in the world. |
| key | string | Yes | "defaultKey" | The texture key assigned to a new Game Object (if one is created). |
| frame | string | number | Yes | "defaultFrame" | A texture frame assigned to a new Game Object (if one is created). |
| visible | boolean | Yes | true | The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created). |

**Returns:** any - The first active group member, or a newly created member, or null.

**Inherits:** [Phaser.GameObjects.Group#getFirstAlive](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1035](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1035)  
> Since: 3.0.0

---

## getFirstDead

### <instance> getFirstDead([createIfNull], [x], [y], [key], [frame], [visible])

**Description:**

Scans the group for the first member that has an [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md) state set to `false`,

assigns `x` and `y`, and returns the member.

If no inactive member is found and `createIfNull` is `true` and the group isn't full then it will create a new one using `x`, `y`, `key`, `frame`, and `visible`.

The new Game Object will have an active state set to `true`.

Unless a new member is created, `key`, `frame`, and `visible` are ignored.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| createIfNull | boolean | Yes | false | Create a new Game Object if no matching members are found, using the following arguments. |
| --- | --- | --- | --- | --- |
| x | number | Yes |  | The horizontal position of the Game Object in the world. |
| y | number | Yes |  | The vertical position of the Game Object in the world. |
| key | string | Yes | "defaultKey" | The texture key assigned to a new Game Object (if one is created). |
| frame | string | number | Yes | "defaultFrame" | A texture frame assigned to a new Game Object (if one is created). |
| visible | boolean | Yes | true | The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created). |

**Returns:** any - The first inactive group member, or a newly created member, or null.

**Inherits:** [Phaser.GameObjects.Group#getFirstDead](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1059](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1059)  
> Since: 3.0.0

---

## getFirstNth

### <instance> getFirstNth(nth, [state], [createIfNull], [x], [y], [key], [frame], [visible])

**Description:**

Scans the Group, from top to bottom, for the nth member that has an [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md) state matching the argument,

assigns `x` and `y`, and returns the member.

If no matching member is found and `createIfNull` is true and the group isn't full then it will create a new Game Object using `x`, `y`, `key`, `frame`, and `visible`.

Unless a new member is created, `key`, `frame`, and `visible` are ignored.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| nth | number | No |  | The nth matching Group member to search for. |
| --- | --- | --- | --- | --- |
| state | boolean | Yes | false | The {@link Phaser.GameObjects.GameObject#active} value to match. |
| createIfNull | boolean | Yes | false | Create a new Game Object if no matching members are found, using the following arguments. |
| x | number | Yes |  | The horizontal position of the Game Object in the world. |
| y | number | Yes |  | The vertical position of the Game Object in the world. |
| key | string | Yes | "defaultKey" | The texture key assigned to a new Game Object (if one is created). |
| frame | string | number | Yes | "defaultFrame" | A texture frame assigned to a new Game Object (if one is created). |
| visible | boolean | Yes | true | The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created). |

**Returns:** any - The first matching group member, or a newly created member, or null.

**Inherits:** [Phaser.GameObjects.Group#getFirstNth](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L831](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L831)  
> Since: 3.6.0

---

## getLast

### <instance> getLast([state], [createIfNull], [x], [y], [key], [frame], [visible])

**Description:**

Scans the Group for the last member that has an [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md) state matching the argument,

assigns `x` and `y`, and returns the member.

If no matching member is found and `createIfNull` is true and the group isn't full then it will create a new Game Object using `x`, `y`, `key`, `frame`, and `visible`.

Unless a new member is created, `key`, `frame`, and `visible` are ignored.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| state | boolean | Yes | false | The {@link Phaser.GameObjects.GameObject#active} value to match. |
| --- | --- | --- | --- | --- |
| createIfNull | boolean | Yes | false | Create a new Game Object if no matching members are found, using the following arguments. |
| x | number | Yes |  | The horizontal position of the Game Object in the world. |
| y | number | Yes |  | The vertical position of the Game Object in the world. |
| key | string | Yes | "defaultKey" | The texture key assigned to a new Game Object (if one is created). |
| frame | string | number | Yes | "defaultFrame" | A texture frame assigned to a new Game Object (if one is created). |
| visible | boolean | Yes | true | The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created). |

**Returns:** any - The first matching group member, or a newly created member, or null.

**Inherits:** [Phaser.GameObjects.Group#getLast](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L857](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L857)  
> Since: 3.6.0

---

## getLastNth

### <instance> getLastNth(nth, [state], [createIfNull], [x], [y], [key], [frame], [visible])

**Description:**

Scans the Group for the last nth member that has an [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md) state matching the argument,

assigns `x` and `y`, and returns the member.

If no matching member is found and `createIfNull` is true and the group isn't full then it will create a new Game Object using `x`, `y`, `key`, `frame`, and `visible`.

Unless a new member is created, `key`, `frame`, and `visible` are ignored.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| nth | number | No |  | The nth matching Group member to search for. |
| --- | --- | --- | --- | --- |
| state | boolean | Yes | false | The {@link Phaser.GameObjects.GameObject#active} value to match. |
| createIfNull | boolean | Yes | false | Create a new Game Object if no matching members are found, using the following arguments. |
| x | number | Yes |  | The horizontal position of the Game Object in the world. |
| y | number | Yes |  | The vertical position of the Game Object in the world. |
| key | string | Yes | "defaultKey" | The texture key assigned to a new Game Object (if one is created). |
| frame | string | number | Yes | "defaultFrame" | A texture frame assigned to a new Game Object (if one is created). |
| visible | boolean | Yes | true | The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created). |

**Returns:** any - The first matching group member, or a newly created member, or null.

**Inherits:** [Phaser.GameObjects.Group#getLastNth](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L882](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L882)  
> Since: 3.6.0

---

## getLength

### <instance> getLength()

**Description:**

The number of members of the group.

**Returns:** number - undefined

**Inherits:** [Phaser.GameObjects.Group#getLength](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L769](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L769)  
> Since: 3.0.0

---

## getMatching

### <instance> getMatching([property], [value], [startIndex], [endIndex])

**Description:**

Returns all children in this Group that match the given criteria based on the `property` and `value` arguments.

For example: `getMatching('visible', true)` would return only children that have their `visible` property set.

Optionally, you can specify a start and end index. For example if the Group has 100 elements,

and you set `startIndex` to 0 and `endIndex` to 50, it would return matches from only

the first 50.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| property | string | Yes | The property to test on each array element. |
| --- | --- | --- | --- |
| value | \* | Yes | The value to test the property against. Must pass a strict (`===`) comparison check. |
| startIndex | number | Yes | An optional start index to search from. |
| endIndex | number | Yes | An optional end index to search to. |

**Returns:** Array.<any> - An array of matching Group members. The array will be empty if nothing matched.

**Inherits:** [Phaser.GameObjects.Group#getMatching](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L782](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L782)  
> Since: 3.50.0

---

## getTotalFree

### <instance> getTotalFree()

**Description:**

The difference of [Phaser.GameObjects.Group#maxSize](gameobjects-group.md) and the number of active group members.

This represents the number of group members that could be created or reactivated before reaching the size limit.

**Returns:** number - maxSize minus the number of active group numbers; or a large number (if maxSize is -1).

**Inherits:** [Phaser.GameObjects.Group#getTotalFree](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1162](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1162)  
> Since: 3.0.0

---

## getTotalUsed

### <instance> getTotalUsed()

**Description:**

Counts the number of in-use (active) group members.

**Returns:** number - The number of group members with an active state of true.

**Inherits:** [Phaser.GameObjects.Group#getTotalUsed](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1149)  
> Since: 3.0.0

---

## incX

### <instance> incX(value, [step])

**Description:**

Adds the given value to the x of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to be added to the `x` property. |
| --- | --- | --- | --- | --- |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#incX](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1314](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1314)  
> Since: 3.21.0

---

## incXY

### <instance> incXY(x, [y], [stepX], [stepY])

**Description:**

Adds the given value to the x, y of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The amount to be added to the `x` property. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The amount to be added to the `y` property. If `undefined` or `null` it uses the `x` value. |
| stepX | number | Yes | 0 | This is added to the `x` amount, multiplied by the iteration counter. |
| stepY | number | Yes | 0 | This is added to the `y` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#incXY](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1350](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1350)  
> Since: 3.21.0

---

## incY

### <instance> incY(value, [step])

**Description:**

Adds the given value to the y of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to be added to the `y` property. |
| --- | --- | --- | --- | --- |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#incY](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1332](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1332)  
> Since: 3.21.0

---

## isFull

### <instance> isFull()

**Description:**

Whether this group's size at its [maximum](gameobjects-group.md).

**Returns:** boolean - True if the number of members equals {@link Phaser.GameObjects.Group#maxSize}.

**Inherits:** [Phaser.GameObjects.Group#isFull](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1102)  
> Since: 3.0.0

---

## kill

### <instance> kill(gameObject)

**Description:**

Deactivates a member of this group.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | A member of this group. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Group#kill](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1647](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1647)  
> Since: 3.0.0

---

## killAndHide

### <instance> killAndHide(gameObject)

**Description:**

Deactivates and hides a member of this group.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | A member of this group. |
| --- | --- | --- | --- |

**Inherits:** [Phaser.GameObjects.Group#killAndHide](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1663](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1663)  
> Since: 3.0.0

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

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - `this`.

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

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - `this`.

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

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
> Since: 3.0.0

---

## playAnimation

### <instance> playAnimation(key, [startFrame])

**Description:**

[Plays](animations-animationstate.md) an animation for all members of this group.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The string-based key of the animation to play. |
| --- | --- | --- | --- | --- |
| startFrame | string | Yes | 0 | Optionally start the animation playing from this frame index. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#playAnimation](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1084](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1084)  
> Since: 3.0.0

---

## preUpdate

### <instance> preUpdate(time, delta)

**Description:**

Updates any group members, if [Phaser.GameObjects.Group#runChildUpdate](gameobjects-group.md) is enabled.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp. |
| --- | --- | --- | --- |
| delta | number | No | The delta time elapsed since the last frame. |

**Inherits:** [Phaser.GameObjects.Group#preUpdate](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L545](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L545)  
> Since: 3.0.0

---

## propertyValueInc

### <instance> propertyValueInc(key, value, [step], [index], [direction])

**Description:**

Adds the given value to the property as defined in `key` of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The property to be updated. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#propertyValueInc](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1237)  
> Since: 3.21.0

---

## propertyValueSet

### <instance> propertyValueSet(key, value, [step], [index], [direction])

**Description:**

Sets the property as defined in `key` of each group member to the given value.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | The property to be updated. |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#propertyValueSet](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1216](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1216)  
> Since: 3.21.0

---

## refresh

### <instance> refresh()

**Description:**

Resets each Body to the position of its parent Game Object.

Body sizes aren't changed (use [Phaser.Physics.Arcade.Components.Enable#refreshBody](../namespace/physics-arcade-components-enable.md) for that).

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This group.

> Source: [src/physics/arcade/StaticPhysicsGroup.js#L199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticPhysicsGroup.js#L199)  
> Since: 3.0.0

---

## remove

### <instance> remove(child, [removeFromScene], [destroyChild])

**Description:**

Removes a member of this Group and optionally removes it from the Scene and / or destroys it.

Calls [Phaser.GameObjects.Group#removeCallback](gameobjects-group.md).

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object to remove. |
| --- | --- | --- | --- | --- |
| removeFromScene | boolean | Yes | false | Optionally remove the Group member from the Scene it belongs to. |
| destroyChild | boolean | Yes | false | Optionally call destroy on the removed Group member. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#remove](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L648](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L648)  
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

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeCallbackHandler

### <instance> removeCallbackHandler(child)

**Description:**

Disables the group member's physics body, removing it from the simulation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The group member being removed. |
| --- | --- | --- | --- |

> Source: [src/physics/arcade/StaticPhysicsGroup.js#L166](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/StaticPhysicsGroup.js#L166)  
> Since: 3.0.0

---

## removeCollidesWith

### <instance> removeCollidesWith(category)

**Description:**

Removes the given Collision Category from the list of those that this

Arcade Physics Body will collide with.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category to add. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#removeCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L80](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L80)  
> Since: 3.70.0

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

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## resetCollisionCategory

### <instance> resetCollisionCategory()

**Description:**

Resets the Collision Category and Mask back to the defaults,

which is to collide with everything.

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#resetCollisionCategory](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L130)  
> Since: 3.70.0

---

## rotate

### <instance> rotate(value, [step])

**Description:**

Sets the rotation of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the rotation to, in radians. |
| --- | --- | --- | --- | --- |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#rotate](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1410](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1410)  
> Since: 3.21.0

---

## rotateAround

### <instance> rotateAround(point, angle)

**Description:**

Rotates each group member around the given point by the given angle.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | Any object with public `x` and `y` properties. |
| --- | --- | --- | --- |
| angle | number | No | The angle to rotate by, in radians. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#rotateAround](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1428](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1428)  
> Since: 3.21.0

---

## rotateAroundDistance

### <instance> rotateAroundDistance(point, angle, distance)

**Description:**

Rotates each group member around the given point by the given angle and distance.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| point | [Phaser.Types.Math.Vector2Like](../typedef/types-math.md) | No | Any object with public `x` and `y` properties. |
| --- | --- | --- | --- |
| angle | number | No | The angle to rotate by, in radians. |
| distance | number | No | The distance from the point of rotation in pixels. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#rotateAroundDistance](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1446](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1446)  
> Since: 3.21.0

---

## scaleX

### <instance> scaleX(value, [step])

**Description:**

Sets the scaleX of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| --- | --- | --- | --- | --- |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#scaleX](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1523](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1523)  
> Since: 3.21.0

---

## scaleXY

### <instance> scaleXY(scaleX, [scaleY], [stepX], [stepY])

**Description:**

Sets the scaleX, scaleY of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| scaleX | number | No |  | The amount to be added to the `scaleX` property. |
| --- | --- | --- | --- | --- |
| scaleY | number | Yes |  | The amount to be added to the `scaleY` property. If `undefined` or `null` it uses the `scaleX` value. |
| stepX | number | Yes | 0 | This is added to the `scaleX` amount, multiplied by the iteration counter. |
| stepY | number | Yes | 0 | This is added to the `scaleY` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#scaleXY](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1559](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1559)  
> Since: 3.21.0

---

## scaleY

### <instance> scaleY(value, [step])

**Description:**

Sets the scaleY of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| --- | --- | --- | --- | --- |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#scaleY](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1541](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1541)  
> Since: 3.21.0

---

## setActive

### <instance> setActive(value)

**Description:**

Sets the `active` property of this Group.

When active, this Group runs its `preUpdate` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | True if this Group should be set as active, false if not. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setActive](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1180)  
> Since: 3.24.0

---

## setAlpha

### <instance> setAlpha(value, [step])

**Description:**

Sets the alpha of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the alpha to. |
| --- | --- | --- | --- | --- |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setAlpha](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1465](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1465)  
> Since: 3.21.0

---

## setBlendMode

### <instance> setBlendMode(value)

**Description:**

Sets the blendMode of each group member.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The amount to set the property to. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setBlendMode](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1597](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1597)  
> Since: 3.21.0

---

## setCollidesWith

### <instance> setCollidesWith(categories)

**Description:**

Sets all of the Collision Categories that this Arcade Physics Body

will collide with. You can either pass a single category value, or

an array of them.

Calling this method will reset all of the collision categories,

so only those passed to this method are enabled.

If you wish to add a new category to the existing mask, call

the `addCollisionCategory` method.

If you wish to reset the collision category and mask, call

the `resetCollisionCategory` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| categories | number | Array.<number> | No | The collision category to collide with, or an array of them. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#setCollidesWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L100](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L100)  
> Since: 3.70.0

---

## setCollisionCategory

### <instance> setCollisionCategory(category)

**Description:**

Sets the Collision Category that this Arcade Physics Body

will use in order to determine what it can collide with.

It can only have one single category assigned to it.

If you wish to reset the collision category and mask, call

the `resetCollisionCategory` method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | The collision category. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Game Object.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#setCollisionCategory](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L17)  
> Since: 3.70.0

---

## setDepth

### <instance> setDepth(value, [step])

**Description:**

Sets the depth of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| --- | --- | --- | --- | --- |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setDepth](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1579](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1579)  
> Since: 3.0.0

---

## setHitArea

### <instance> setHitArea(hitArea, hitAreaCallback)

**Description:**

Passes all group members to the Input Manager to enable them for input with identical areas and callbacks.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| hitArea | \* | No | Either an input configuration object, or a geometric shape that defines the hit area for the Game Object. If not specified a Rectangle will be used. |
| --- | --- | --- | --- |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | No | A callback to be invoked when the Game Object is interacted with. If you provide a shape you must also provide a callback. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setHitArea](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1614](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1614)  
> Since: 3.21.0

---

## setName

### <instance> setName(value)

**Description:**

Sets the `name` property of this Group.

The `name` property is not populated by Phaser and is presented for your own use.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | string | No | The name to be given to this Group. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setName](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1198](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1198)  
> Since: 3.24.0

---

## setOrigin

### <instance> setOrigin(originX, [originY], [stepX], [stepY])

**Description:**

Sets the originX, originY of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| originX | number | No |  | The amount to set the `originX` property to. |
| --- | --- | --- | --- | --- |
| originY | number | Yes |  | The amount to set the `originY` property to. If `undefined` or `null` it uses the `originX` value. |
| stepX | number | Yes | 0 | This is added to the `originX` amount, multiplied by the iteration counter. |
| stepY | number | Yes | 0 | This is added to the `originY` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setOrigin](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1503](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1503)  
> Since: 3.21.0

---

## setTint

### <instance> setTint(topLeft, [topRight], [bottomLeft], [bottomRight])

**Description:**

Sets the tint of each group member.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| topLeft | number | No | The tint being applied to top-left corner of item. If other parameters are given no value, this tint will be applied to whole item. |
| --- | --- | --- | --- |
| topRight | number | Yes | The tint to be applied to top-right corner of item. |
| bottomLeft | number | Yes | The tint to be applied to the bottom-left corner of item. |
| bottomRight | number | Yes | The tint to be applied to the bottom-right corner of item. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setTint](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1483](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1483)  
> Since: 3.21.0

---

## setVisible

### <instance> setVisible(value, [index], [direction])

**Description:**

Sets the visible of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | boolean | No |  | The value to set the property to. |
| --- | --- | --- | --- | --- |
| index | number | Yes | 0 | An optional offset to start searching from within the items array. |
| direction | number | Yes | 1 | The direction to iterate through the array. 1 is from beginning to end, -1 from end to beginning. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setVisible](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1680](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1680)  
> Since: 3.21.0

---

## setX

### <instance> setX(value, [step])

**Description:**

Sets the x of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| --- | --- | --- | --- | --- |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setX](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1258](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1258)  
> Since: 3.21.0

---

## setXY

### <instance> setXY(x, [y], [stepX], [stepY])

**Description:**

Sets the x, y of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The amount to set the `x` property to. |
| --- | --- | --- | --- | --- |
| y | number | Yes | "x" | The amount to set the `y` property to. If `undefined` or `null` it uses the `x` value. |
| stepX | number | Yes | 0 | This is added to the `x` amount, multiplied by the iteration counter. |
| stepY | number | Yes | 0 | This is added to the `y` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setXY](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1294](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1294)  
> Since: 3.21.0

---

## setY

### <instance> setY(value, [step])

**Description:**

Sets the y of each group member.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| value | number | No |  | The amount to set the property to. |
| --- | --- | --- | --- | --- |
| step | number | Yes | 0 | This is added to the `value` amount, multiplied by the iteration counter. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#setY](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1276](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1276)  
> Since: 3.21.0

---

## shiftPosition

### <instance> shiftPosition(x, y, [direction])

**Description:**

Iterate through the group members changing the position of each element to be that of the element that came before

it in the array (or after it if direction = 1)

The first group member position is set to x/y.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | No |  | The x coordinate to place the first item in the array at. |
| --- | --- | --- | --- | --- |
| y | number | No |  | The y coordinate to place the first item in the array at. |
| direction | number | Yes | 0 | The iteration direction. 0 = first to last and 1 = last to first. |

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#shiftPosition](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1370](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1370)  
> Since: 3.21.0

---

## shuffle

### <instance> shuffle()

**Description:**

Shuffles the group members in place.

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#shuffle](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1632](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1632)  
> Since: 3.21.0

---

## shutdown

### <instance> shutdown()

**Description:**

Removes all listeners.

**Inherits:** [Phaser.Events.EventEmitter#shutdown](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L31](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L31)  
> Since: 3.0.0

---

## toggleVisible

### <instance> toggleVisible()

**Description:**

Toggles (flips) the visible state of each member of this group.

**Returns:** [Phaser.Physics.Arcade.StaticGroup](physics-arcade-staticgroup.md) - This Group object.

**Inherits:** [Phaser.GameObjects.Group#toggleVisible](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L1699](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L1699)  
> Since: 3.0.0

---

## willCollideWith

### <instance> willCollideWith(category)

**Description:**

Checks to see if the given Collision Category will collide with

this Arcade Physics object or not.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| category | number | No | Collision category value to test. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the given category will collide with this object, otherwise `false`.

**Inherits:** [Phaser.Physics.Arcade.Components.Collision#willCollideWith](../namespace/physics-arcade-components-collision.md)

> Source: [src/physics/arcade/components/Collision.js#L42](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/arcade/components/Collision.js#L42)  
> Since: 3.70.0

---

# Private Methods

## getHandler

### <instance> getHandler(forwards, nth, [state], [createIfNull], [x], [y], [key], [frame], [visible])

**Description:**

Scans the group for the last member that has an [Phaser.GameObjects.GameObject#active](gameobjects-gameobject.md) state matching the argument,

assigns `x` and `y`, and returns the member.

If no matching member is found and `createIfNull` is true and the group isn't full then it will create a new Game Object using `x`, `y`, `key`, `frame`, and `visible`.

Unless a new member is created, `key`, `frame`, and `visible` are ignored.

**Access:** private

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| forwards | boolean | No |  | Search front to back or back to front? |
| --- | --- | --- | --- | --- |
| nth | number | No |  | Stop matching after nth successful matches. |
| state | boolean | Yes | false | The {@link Phaser.GameObjects.GameObject#active} value to match. |
| createIfNull | boolean | Yes | false | Create a new Game Object if no matching members are found, using the following arguments. |
| x | number | Yes |  | The horizontal position of the Game Object in the world. |
| y | number | Yes |  | The vertical position of the Game Object in the world. |
| key | string | Yes | "defaultKey" | The texture key assigned to a new Game Object (if one is created). |
| frame | string | number | Yes | "defaultFrame" | A texture frame assigned to a new Game Object (if one is created). |
| visible | boolean | Yes | true | The {@link Phaser.GameObjects.Components.Visible#visible} state of a new Game Object (if one is created). |

**Returns:** any - The first matching group member, or a newly created member, or null.

**Inherits:** [Phaser.GameObjects.Group#getHandler](gameobjects-group.md)

> Source: [src/gameobjects/group/Group.js#L908](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/group/Group.js#L908)  
> Since: 3.6.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [active](#active)

    - [active: boolean](#active-boolean)
  + [children](#children)

    - [children: Phaser.Structs.Set.<Phaser.GameObjects.GameObject>](#children-phaserstructssetphasergameobjectsgameobject)
  + [classType](#classtype)

    - [classType: function](#classtype-function)
  + [collisionCategory](#collisioncategory)

    - [collisionCategory: number](#collisioncategory-number)
  + [collisionMask](#collisionmask)

    - [collisionMask: number](#collisionmask-number)
  + [createCallback](#createcallback)

    - [createCallback: Phaser.Types.GameObjects.Group.GroupCallback](#createcallback-phasertypesgameobjectsgroupgroupcallback)
  + [createMultipleCallback](#createmultiplecallback)

    - [createMultipleCallback: Phaser.Types.GameObjects.Group.GroupMultipleCreateCallback](#createmultiplecallback-phasertypesgameobjectsgroupgroupmultiplecreatecallback)
  + [defaultFrame](#defaultframe)

    - [defaultFrame: string, number](#defaultframe-string-number)
  + [defaultKey](#defaultkey)

    - [defaultKey: string](#defaultkey-string)
  + [isParent](#isparent)

    - [isParent: boolean](#isparent-boolean)
  + [maxSize](#maxsize)

    - [maxSize: number](#maxsize-number)
  + [name](#name)

    - [name: string](#name-string)
  + [physicsType](#physicstype)

    - [physicsType: number](#physicstype-number)
  + [removeCallback](#removecallback)

    - [removeCallback: Phaser.Types.GameObjects.Group.GroupCallback](#removecallback-phasertypesgameobjectsgroupgroupcallback)
  + [runChildUpdate](#runchildupdate)

    - [runChildUpdate: boolean](#runchildupdate-boolean)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [type](#type)

    - [type: string](#type-string)
  + [world](#world)

    - [world: Phaser.Physics.Arcade.World](#world-phaserphysicsarcadeworld)
* [Private Members](#private-members)

  + [internalCreateCallback](#internalcreatecallback)

    - [internalCreateCallback: Phaser.Types.GameObjects.Group.GroupCallback](#internalcreatecallback-phasertypesgameobjectsgroupgroupcallback)
  + [internalRemoveCallback](#internalremovecallback)

    - [internalRemoveCallback: Phaser.Types.GameObjects.Group.GroupCallback](#internalremovecallback-phasertypesgameobjectsgroupgroupcallback)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(child, [addToScene])](#instance-addchild-addtoscene)
  + [addCollidesWith](#addcollideswith)

    - [<instance> addCollidesWith(category)](#instance-addcollideswithcategory)
  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addMultiple](#addmultiple)

    - [<instance> addMultiple(children, [addToScene])](#instance-addmultiplechildren-addtoscene)
  + [angle](#angle)

    - [<instance> angle(value, [step])](#instance-anglevalue-step)
  + [clear](#clear)

    - [<instance> clear([removeFromScene], [destroyChild])](#instance-clearremovefromscene-destroychild)
  + [contains](#contains)

    - [<instance> contains(child)](#instance-containschild)
  + [countActive](#countactive)

    - [<instance> countActive([value])](#instance-countactivevalue)
  + [create](#create)

    - [<instance> create([x], [y], [key], [frame], [visible], [active])](#instance-createx-y-key-frame-visible-active)
  + [createCallbackHandler](#createcallbackhandler)

    - [<instance> createCallbackHandler(child)](#instance-createcallbackhandlerchild)
  + [createFromConfig](#createfromconfig)

    - [<instance> createFromConfig(options)](#instance-createfromconfigoptions)
  + [createMultiple](#createmultiple)

    - [<instance> createMultiple(config)](#instance-createmultipleconfig)
  + [createMultipleCallbackHandler](#createmultiplecallbackhandler)

    - [<instance> createMultipleCallbackHandler(entries)](#instance-createmultiplecallbackhandlerentries)
  + [destroy](#destroy)

    - [<instance> destroy([destroyChildren], [removeFromScene])](#instance-destroydestroychildren-removefromscene)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [get](#get)

    - [<instance> get([x], [y], [key], [frame], [visible])](#instance-getx-y-key-frame-visible)
  + [getChildren](#getchildren)

    - [<instance> getChildren()](#instance-getchildren)
  + [getFirst](#getfirst)

    - [<instance> getFirst([state], [createIfNull], [x], [y], [key], [frame], [visible])](#instance-getfirststate-createifnull-x-y-key-frame-visible)
  + [getFirstAlive](#getfirstalive)

    - [<instance> getFirstAlive([createIfNull], [x], [y], [key], [frame], [visible])](#instance-getfirstalivecreateifnull-x-y-key-frame-visible)
  + [getFirstDead](#getfirstdead)

    - [<instance> getFirstDead([createIfNull], [x], [y], [key], [frame], [visible])](#instance-getfirstdeadcreateifnull-x-y-key-frame-visible)
  + [getFirstNth](#getfirstnth)

    - [<instance> getFirstNth(nth, [state], [createIfNull], [x], [y], [key], [frame], [visible])](#instance-getfirstnthnth-state-createifnull-x-y-key-frame-visible)
  + [getLast](#getlast)

    - [<instance> getLast([state], [createIfNull], [x], [y], [key], [frame], [visible])](#instance-getlaststate-createifnull-x-y-key-frame-visible)
  + [getLastNth](#getlastnth)

    - [<instance> getLastNth(nth, [state], [createIfNull], [x], [y], [key], [frame], [visible])](#instance-getlastnthnth-state-createifnull-x-y-key-frame-visible)
  + [getLength](#getlength)

    - [<instance> getLength()](#instance-getlength)
  + [getMatching](#getmatching)

    - [<instance> getMatching([property], [value], [startIndex], [endIndex])](#instance-getmatchingproperty-value-startindex-endindex)
  + [getTotalFree](#gettotalfree)

    - [<instance> getTotalFree()](#instance-gettotalfree)
  + [getTotalUsed](#gettotalused)

    - [<instance> getTotalUsed()](#instance-gettotalused)
  + [incX](#incx)

    - [<instance> incX(value, [step])](#instance-incxvalue-step)
  + [incXY](#incxy)

    - [<instance> incXY(x, [y], [stepX], [stepY])](#instance-incxyx-y-stepx-stepy)
  + [incY](#incy)

    - [<instance> incY(value, [step])](#instance-incyvalue-step)
  + [isFull](#isfull)

    - [<instance> isFull()](#instance-isfull)
  + [kill](#kill)

    - [<instance> kill(gameObject)](#instance-killgameobject)
  + [killAndHide](#killandhide)

    - [<instance> killAndHide(gameObject)](#instance-killandhidegameobject)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [playAnimation](#playanimation)

    - [<instance> playAnimation(key, [startFrame])](#instance-playanimationkey-startframe)
  + [preUpdate](#preupdate)

    - [<instance> preUpdate(time, delta)](#instance-preupdatetime-delta)
  + [propertyValueInc](#propertyvalueinc)

    - [<instance> propertyValueInc(key, value, [step], [index], [direction])](#instance-propertyvalueinckey-value-step-index-direction)
  + [propertyValueSet](#propertyvalueset)

    - [<instance> propertyValueSet(key, value, [step], [index], [direction])](#instance-propertyvaluesetkey-value-step-index-direction)
  + [refresh](#refresh)

    - [<instance> refresh()](#instance-refresh)
  + [remove](#remove)

    - [<instance> remove(child, [removeFromScene], [destroyChild])](#instance-removechild-removefromscene-destroychild)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeCallbackHandler](#removecallbackhandler)

    - [<instance> removeCallbackHandler(child)](#instance-removecallbackhandlerchild)
  + [removeCollidesWith](#removecollideswith)

    - [<instance> removeCollidesWith(category)](#instance-removecollideswithcategory)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [resetCollisionCategory](#resetcollisioncategory)

    - [<instance> resetCollisionCategory()](#instance-resetcollisioncategory)
  + [rotate](#rotate)

    - [<instance> rotate(value, [step])](#instance-rotatevalue-step)
  + [rotateAround](#rotatearound)

    - [<instance> rotateAround(point, angle)](#instance-rotatearoundpoint-angle)
  + [rotateAroundDistance](#rotatearounddistance)

    - [<instance> rotateAroundDistance(point, angle, distance)](#instance-rotatearounddistancepoint-angle-distance)
  + [scaleX](#scalex)

    - [<instance> scaleX(value, [step])](#instance-scalexvalue-step)
  + [scaleXY](#scalexy)

    - [<instance> scaleXY(scaleX, [scaleY], [stepX], [stepY])](#instance-scalexyscalex-scaley-stepx-stepy)
  + [scaleY](#scaley)

    - [<instance> scaleY(value, [step])](#instance-scaleyvalue-step)
  + [setActive](#setactive)

    - [<instance> setActive(value)](#instance-setactivevalue)
  + [setAlpha](#setalpha)

    - [<instance> setAlpha(value, [step])](#instance-setalphavalue-step)
  + [setBlendMode](#setblendmode)

    - [<instance> setBlendMode(value)](#instance-setblendmodevalue)
  + [setCollidesWith](#setcollideswith)

    - [<instance> setCollidesWith(categories)](#instance-setcollideswithcategories)
  + [setCollisionCategory](#setcollisioncategory)

    - [<instance> setCollisionCategory(category)](#instance-setcollisioncategorycategory)
  + [setDepth](#setdepth)

    - [<instance> setDepth(value, [step])](#instance-setdepthvalue-step)
  + [setHitArea](#sethitarea)

    - [<instance> setHitArea(hitArea, hitAreaCallback)](#instance-sethitareahitarea-hitareacallback)
  + [setName](#setname)

    - [<instance> setName(value)](#instance-setnamevalue)
  + [setOrigin](#setorigin)

    - [<instance> setOrigin(originX, [originY], [stepX], [stepY])](#instance-setoriginoriginx-originy-stepx-stepy)
  + [setTint](#settint)

    - [<instance> setTint(topLeft, [topRight], [bottomLeft], [bottomRight])](#instance-settinttopleft-topright-bottomleft-bottomright)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value, [index], [direction])](#instance-setvisiblevalue-index-direction)
  + [setX](#setx)

    - [<instance> setX(value, [step])](#instance-setxvalue-step)
  + [setXY](#setxy)

    - [<instance> setXY(x, [y], [stepX], [stepY])](#instance-setxyx-y-stepx-stepy)
  + [setY](#sety)

    - [<instance> setY(value, [step])](#instance-setyvalue-step)
  + [shiftPosition](#shiftposition)

    - [<instance> shiftPosition(x, y, [direction])](#instance-shiftpositionx-y-direction)
  + [shuffle](#shuffle)

    - [<instance> shuffle()](#instance-shuffle)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [toggleVisible](#togglevisible)

    - [<instance> toggleVisible()](#instance-togglevisible)
  + [willCollideWith](#willcollidewith)

    - [<instance> willCollideWith(category)](#instance-willcollidewithcategory)
* [Private Methods](#private-methods)

  + [getHandler](#gethandler)

    - [<instance> getHandler(forwards, nth, [state], [createIfNull], [x], [y], [key], [frame], [visible])](#instance-gethandlerforwards-nth-state-createifnull-x-y-key-frame-visible)

Back to top

©2025[Phaser](https://docs.phaser.io)