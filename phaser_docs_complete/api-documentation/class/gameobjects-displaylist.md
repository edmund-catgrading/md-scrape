# DisplayList

Phaser.GameObjects.DisplayList

The Display List plugin.

Display Lists belong to a Scene and maintain the list of Game Objects to render every frame.

Some of these Game Objects may also be part of the Scene's [Update List](Phaser.GameObjects.UpdateList.md), for updating.

**Constructor**

`new DisplayList(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene that this Display List belongs to. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> Phaser.Structs.List.<Phaser.GameObjects.GameObject>

> Source: [src/gameobjects/DisplayList.js#L14](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L14)  
> Since: 3.0.0

# Public Members

## events

### events: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

The Scene's Event Emitter.

> Source: [src/gameobjects/DisplayList.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L68)  
> Since: 3.50.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene that this Display List belongs to.

> Source: [src/gameobjects/DisplayList.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L50)  
> Since: 3.0.0

---

## sortChildrenFlag

### sortChildrenFlag: boolean

**Description:**

The flag the determines whether Game Objects should be sorted when `depthSort()` is called.

> Source: [src/gameobjects/DisplayList.js#L40](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L40)  
> Since: 3.0.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

The Scene's Systems.

> Source: [src/gameobjects/DisplayList.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L59)  
> Since: 3.0.0

---

# Public Methods

## depthSort

### <instance> depthSort()

**Description:**

Immediately sorts the display list if the flag is set.

> Source: [src/gameobjects/DisplayList.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L180)  
> Since: 3.0.0

---

## getChildren

### <instance> getChildren()

**Description:**

Returns an array which contains all objects currently on the Display List.

This is a reference to the main list array, not a copy of it, so be careful not to modify it.

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - The group members.

> Source: [src/gameobjects/DisplayList.js#L212](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L212)  
> Since: 3.12.0

---

## queueDepthSort

### <instance> queueDepthSort()

**Description:**

Force a sort of the display list on the next call to depthSort.

> Source: [src/gameobjects/DisplayList.js#L169](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L169)  
> Since: 3.0.0

---

## sortByDepth

### <instance> sortByDepth(childA, childB)

**Description:**

Compare the depth of two Game Objects.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| childA | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The first Game Object. |
| --- | --- | --- | --- |
| childB | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The second Game Object. |

**Returns:** number - The difference between the depths of each Game Object.

> Source: [src/gameobjects/DisplayList.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L196)  
> Since: 3.0.0

---

# Private Methods

## addChildCallback

### <instance> addChildCallback(gameObject)

**Description:**

Internal method called from `List.addCallback`.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that was added to the list. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scenes.Events#event:ADDED\_TO\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:ADDED\_TO\_SCENE](../event/gameobjects-events.md)

> Source: [src/gameobjects/DisplayList.js#L98](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L98)  
> Since: 3.50.0

---

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

> Source: [src/gameobjects/DisplayList.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L85)  
> Since: 3.5.1

---

## destroy

### <instance> destroy()

**Description:**

The Scene that owns this plugin is being destroyed.

We need to shutdown and then kill off all external references.

**Access:** private

> Source: [src/gameobjects/DisplayList.js#L247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L247)  
> Since: 3.0.0

---

## removeChildCallback

### <instance> removeChildCallback(gameObject)

**Description:**

Internal method called from `List.removeCallback`.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object that was removed from the list. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scenes.Events#event:REMOVED\_FROM\_SCENE](../event/scenes-events.md), [Phaser.GameObjects.Events#event:REMOVED\_FROM\_SCENE](../event/gameobjects-events.md)

> Source: [src/gameobjects/DisplayList.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L133)  
> Since: 3.50.0

---

## shutdown

### <instance> shutdown()

**Description:**

The Scene that owns this plugin is shutting down.

We need to kill and reset all internal properties as well as stop listening to Scene events.

**Access:** private

> Source: [src/gameobjects/DisplayList.js#L226](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L226)  
> Since: 3.0.0

---

## start

### <instance> start()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

> Source: [src/gameobjects/DisplayList.js#L155](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/DisplayList.js#L155)  
> Since: 3.5.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [events](#events)

    - [events: Phaser.Events.EventEmitter](#events-phasereventseventemitter)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [sortChildrenFlag](#sortchildrenflag)

    - [sortChildrenFlag: boolean](#sortchildrenflag-boolean)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
* [Public Methods](#public-methods)

  + [depthSort](#depthsort)

    - [<instance> depthSort()](#instance-depthsort)
  + [getChildren](#getchildren)

    - [<instance> getChildren()](#instance-getchildren)
  + [queueDepthSort](#queuedepthsort)

    - [<instance> queueDepthSort()](#instance-queuedepthsort)
  + [sortByDepth](#sortbydepth)

    - [<instance> sortByDepth(childA, childB)](#instance-sortbydepthchilda-childb)
* [Private Methods](#private-methods)

  + [addChildCallback](#addchildcallback)

    - [<instance> addChildCallback(gameObject)](#instance-addchildcallbackgameobject)
  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [removeChildCallback](#removechildcallback)

    - [<instance> removeChildCallback(gameObject)](#instance-removechildcallbackgameobject)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [start](#start)

    - [<instance> start()](#instance-start)

Back to top

©2025[Phaser](https://docs.phaser.io)