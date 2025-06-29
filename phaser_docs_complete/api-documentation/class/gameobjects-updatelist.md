# UpdateList

Phaser.GameObjects.UpdateList

The Update List plugin.

Update Lists belong to a Scene and maintain the list Game Objects to be updated every frame.

Some or all of these Game Objects may also be part of the Scene's [Display List](Phaser.GameObjects.DisplayList.md), for Rendering.

**Constructor**

`new UpdateList(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene that the Update List belongs to. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> Phaser.Structs.ProcessQueue.<Phaser.GameObjects.GameObject>

> Source: [src/gameobjects/UpdateList.js#L12](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L12)  
> Since: 3.0.0

# Public Members

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene that the Update List belongs to.

> Source: [src/gameobjects/UpdateList.js#L41](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L41)  
> Since: 3.0.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

The Scene's Systems.

> Source: [src/gameobjects/UpdateList.js#L50](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L50)  
> Since: 3.0.0

---

# Private Members

## \_active

### \_active: Array.<\*>

**Description:**

The `active` list is a selection of items which are considered active and should be updated.

**Access:** private

> Source: [src/gameobjects/UpdateList.js#L69](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L69)  
> Since: 3.20.0

---

## \_destroy

### \_destroy: Array.<\*>

**Description:**

The `destroy` list is a selection of items that were active and are awaiting being destroyed in the next update.

**Access:** private

> Source: [src/gameobjects/UpdateList.js#L79](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L79)  
> Since: 3.20.0

---

## \_pending

### \_pending: Array.<\*>

**Description:**

The `pending` list is a selection of items which are due to be made 'active' in the next update.

**Access:** private

> Source: [src/gameobjects/UpdateList.js#L59](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L59)  
> Since: 3.20.0

---

## \_toProcess

### \_toProcess: number

**Description:**

The total number of items awaiting processing.

**Access:** private

> Source: [src/gameobjects/UpdateList.js#L89](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L89)  
> Since: 3.0.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

The Scene that owns this plugin is being destroyed.

We need to shutdown and then kill off all external references.

> Source: [src/gameobjects/UpdateList.js#L207](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L207)  
> Since: 3.0.0

---

## sceneUpdate

### <instance> sceneUpdate(time, delta)

**Description:**

The update step.

Pre-updates every active Game Object in the list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current timestamp. |
| --- | --- | --- | --- |
| delta | number | No | The delta time elapsed since the last frame. |

> Source: [src/gameobjects/UpdateList.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L134)  
> Since: 3.20.0

---

## shutdown

### <instance> shutdown()

**Description:**

The Scene that owns this plugin is shutting down.

We need to kill and reset all internal properties as well as stop listening to Scene events.

> Source: [src/gameobjects/UpdateList.js#L161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L161)  
> Since: 3.0.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

> Source: [src/gameobjects/UpdateList.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L103)  
> Since: 3.5.1

---

## start

### <instance> start()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

> Source: [src/gameobjects/UpdateList.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/UpdateList.js#L116)  
> Since: 3.5.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
* [Private Members](#private-members)

  + [\_active](#_active)

    - [\_active: Array.<\*>](#_active-array)
  + [\_destroy](#_destroy)

    - [\_destroy: Array.<\*>](#_destroy-array)
  + [\_pending](#_pending)

    - [\_pending: Array.<\*>](#_pending-array)
  + [\_toProcess](#_toprocess)

    - [\_toProcess: number](#_toprocess-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [sceneUpdate](#sceneupdate)

    - [<instance> sceneUpdate(time, delta)](#instance-sceneupdatetime-delta)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [start](#start)

    - [<instance> start()](#instance-start)

Back to top

©2025[Phaser](https://docs.phaser.io)