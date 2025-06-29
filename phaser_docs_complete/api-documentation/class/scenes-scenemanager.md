# SceneManager

Phaser.Scenes.SceneManager

The Scene Manager.

The Scene Manager is a Game level system, responsible for creating, processing and updating all of the

Scenes in a Game instance.

You should not usually interact directly with the Scene Manager at all. Instead, you should use

the Scene Plugin, which is available from every Scene in your game via the `this.scene` property.

Using methods in this Scene Manager directly will break queued operations and can cause runtime

errors. Instead, go via the Scene Plugin. Every feature this Scene Manager provides is also

available via the Scene Plugin.

**Constructor**

`new SceneManager(game, sceneConfig)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | The Phaser.Game instance this Scene Manager belongs to. |
| --- | --- | --- | --- |
| sceneConfig | object | No | Scene specific configuration settings. |

---

**Scope**: static

> Source: [src/scene/SceneManager.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L17)  
> Since: 3.0.0

# Public Members

## customViewports

### customViewports: number

**Description:**

Do any of the Cameras in any of the Scenes require a custom viewport?

If not we can skip scissor tests.

> Source: [src/scene/SceneManager.js#L134](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L134)  
> Since: 3.12.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

The Game that this SceneManager belongs to.

> Source: [src/scene/SceneManager.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L45)  
> Since: 3.0.0

---

## isBooted

### isBooted: boolean

**Description:**

Has the Scene Manager properly started?

> Source: [src/scene/SceneManager.js#L123](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L123)  
> Since: 3.4.0

---

## isProcessing

### isProcessing: boolean

**Description:**

Is the Scene Manager actively processing the Scenes list?

> Source: [src/scene/SceneManager.js#L112](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L112)  
> Since: 3.0.0

---

## keys

### keys: Record.<string, [Phaser.Scene](scene.md)>

**Description:**

An object that maps the keys to the scene so we can quickly get a scene from a key without iteration.

> Source: [src/scene/SceneManager.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L54)  
> Since: 3.0.0

---

## scenes

### scenes: Array.<[Phaser.Scene](scene.md)>

**Description:**

The array in which all of the scenes are kept.

> Source: [src/scene/SceneManager.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L63)  
> Since: 3.0.0

---

## systemScene

### systemScene: [Phaser.Scene](scene.md)

**Description:**

This system Scene is created during `bootQueue` and is a default

empty Scene that lives outside of the Scene list, but can be used

by plugins and managers that need access to a live Scene, without

being tied to one.

> Source: [src/scene/SceneManager.js#L145](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L145)  
> Since: 3.60.0

---

# Private Members

## \_data

### \_data: object

**Description:**

Boot time data to merge.

**Access:** private

> Source: [src/scene/SceneManager.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L102)  
> Since: 3.4.0

---

## \_pending

### \_pending: array

**Description:**

Scenes pending to be added are stored in here until the manager has time to add it.

**Access:** private

> Source: [src/scene/SceneManager.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L72)  
> Since: 3.0.0

---

## \_queue

### \_queue: array

**Description:**

An operations queue, because we don't manipulate the scenes array during processing.

**Access:** private

> Source: [src/scene/SceneManager.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L92)  
> Since: 3.0.0

---

## \_start

### \_start: array

**Description:**

An array of scenes waiting to be started once the game has booted.

**Access:** private

> Source: [src/scene/SceneManager.js#L82](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L82)  
> Since: 3.0.0

---

# Public Methods

## add

### <instance> add(key, sceneConfig, [autoStart], [data])

**Description:**

Adds a new Scene into the SceneManager.

You must give each Scene a unique key by which you'll identify it.

The `sceneConfig` can be:

* A `Phaser.Scene` object, or an object that extends it.
* A plain JavaScript object
* A JavaScript ES6 Class that extends `Phaser.Scene`
* A JavaScript ES5 prototype based Class
* A JavaScript function

If a function is given then a new Scene will be created by calling it.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | A unique key used to reference the Scene, i.e. `MainMenu` or `Level1`. |
| --- | --- | --- | --- | --- |
| sceneConfig | [Phaser.Types.Scenes.SceneType](../typedef/types-scenes.md) | No |  | The config for the Scene |
| autoStart | boolean | Yes | false | If `true` the Scene will be started immediately after being added. |
| data | object | Yes |  | Optional data object. This will be set as `Scene.settings.data` and passed to `Scene.init`, and `Scene.create`. |

**Returns:** [Phaser.Scene](scene.md) - The added Scene, if it was added immediately, otherwise `null`.

> Source: [src/scene/SceneManager.js#L319](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L319)  
> Since: 3.0.0

---

## bringToTop

### <instance> bringToTop(key)

**Description:**

Brings a Scene to the top of the Scenes list.

This means it will render above all other Scenes.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to move. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1381](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1381)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroy this Scene Manager and all of its systems.

This process cannot be reversed.

This method is called automatically when a Phaser Game instance is destroyed.

> Source: [src/scene/SceneManager.js#L1706](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1706)  
> Since: 3.0.0

---

## dump

### <instance> dump()

**Description:**

Dumps debug information about each Scene to the developer console.

> Source: [src/scene/SceneManager.js#L1682](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1682)  
> Since: 3.2.0

---

## getAt

### <instance> getAt(index)

**Description:**

Retrieves a Scene by numeric index.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the Scene to retrieve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scene](scene.md), undefined - The Scene.

> Source: [src/scene/SceneManager.js#L1343](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1343)  
> Since: 3.0.0

---

## getIndex

### <instance> getIndex(key)

**Description:**

Retrieves the numeric index of a Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The key of the Scene. |
| --- | --- | --- | --- |

**Returns:** number - The index of the Scene.

> Source: [src/scene/SceneManager.js#L1361](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1361)  
> Since: 3.0.0

---

## getScene

### <instance> getScene(key)

**Description:**

Retrieves a Scene based on the given key.

If an actual Scene is passed to this method, it can be used to check if

its currently within the Scene Manager, or not.

**Tags:**

* generic
* genericUse
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The key of the Scene to retrieve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scene](scene.md) - The Scene, or `null` if no matching Scene was found.

> Source: [src/scene/SceneManager.js#L878](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L878)  
> Since: 3.0.0

---

## getScenes

### <instance> getScenes([isActive], [inReverse])

**Description:**

Returns an array of all the current Scenes being managed by this Scene Manager.

You can filter the output by the active state of the Scene and choose to have

the array returned in normal or reversed order.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| isActive | boolean | Yes | true | Only include Scene's that are currently active? |
| --- | --- | --- | --- | --- |
| inReverse | boolean | Yes | false | Return the array of Scenes in reverse? |

**Returns:** Array.<[Phaser.Scene](scene.md)> - An array containing all of the Scenes in the Scene Manager.

> Source: [src/scene/SceneManager.js#L840](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L840)  
> Since: 3.16.0

---

## isActive

### <instance> isActive(key)

**Description:**

Determines whether a Scene is running.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to check. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the Scene is running, or `null` if no matching Scene was found.

> Source: [src/scene/SceneManager.js#L918](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L918)  
> Since: 3.0.0

---

## isPaused

### <instance> isPaused(key)

**Description:**

Determines whether a Scene is paused.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to check. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the Scene is paused, or `null` if no matching Scene was found.

> Source: [src/scene/SceneManager.js#L943](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L943)  
> Since: 3.17.0

---

## isSleeping

### <instance> isSleeping(key)

**Description:**

Determines whether a Scene is sleeping.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to check. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the Scene is sleeping, or `null` if no matching Scene was found.

> Source: [src/scene/SceneManager.js#L993](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L993)  
> Since: 3.0.0

---

## isVisible

### <instance> isVisible(key)

**Description:**

Determines whether a Scene is visible.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to check. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the Scene is visible, or `null` if no matching Scene was found.

> Source: [src/scene/SceneManager.js#L968](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L968)  
> Since: 3.0.0

---

## moveAbove

### <instance> moveAbove(keyA, keyB)

**Description:**

Moves a Scene so it is immediately above another Scene in the Scenes list.

If the Scene is already above the other, it isn't moved.

This means it will render over the top of the other Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keyA | string | [Phaser.Scene](scene.md) | No | The Scene that Scene B will be moved above. |
| --- | --- | --- | --- |
| keyB | string | [Phaser.Scene](scene.md) | No | The Scene to be moved. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1522](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1522)  
> Since: 3.2.0

---

## moveBelow

### <instance> moveBelow(keyA, keyB)

**Description:**

Moves a Scene so it is immediately below another Scene in the Scenes list.

If the Scene is already below the other, it isn't moved.

This means it will render behind the other Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keyA | string | [Phaser.Scene](scene.md) | No | The Scene that Scene B will be moved below. |
| --- | --- | --- | --- |
| keyB | string | [Phaser.Scene](scene.md) | No | The Scene to be moved. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1568](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1568)  
> Since: 3.2.0

---

## moveDown

### <instance> moveDown(key)

**Description:**

Moves a Scene down one position in the Scenes list.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to move. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1452](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1452)  
> Since: 3.0.0

---

## moveUp

### <instance> moveUp(key)

**Description:**

Moves a Scene up one position in the Scenes list.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to move. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1487](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1487)  
> Since: 3.0.0

---

## pause

### <instance> pause(key, [data])

**Description:**

Pauses the given Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to pause. |
| --- | --- | --- | --- |
| data | object | Yes | An optional data object that will be passed to the Scene and emitted by its pause event. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1018](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1018)  
> Since: 3.0.0

---

## processQueue

### <instance> processQueue()

**Description:**

Process the Scene operations queue.

> Source: [src/scene/SceneManager.js#L268](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L268)  
> Since: 3.0.0

---

## remove

### <instance> remove(key)

**Description:**

Removes a Scene from the SceneManager.

The Scene is removed from the local scenes array, it's key is cleared from the keys

cache and Scene.Systems.destroy is then called on it.

If the SceneManager is processing the Scenes when this method is called it will

queue the operation for the next update sequence.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | A unique key used to reference the Scene, i.e. `MainMenu` or `Level1`. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L410](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L410)  
> Since: 3.2.0

---

## render

### <instance> render(renderer)

**Description:**

Renders the Scenes.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| renderer | [Phaser.Renderer.Canvas.CanvasRenderer](renderer-canvas-canvasrenderer.md) | [Phaser.Renderer.WebGL.WebGLRenderer](renderer-webgl-webglrenderer.md) | No | The renderer to use. |
| --- | --- | --- | --- |

> Source: [src/scene/SceneManager.js#L578](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L578)  
> Since: 3.0.0

---

## resume

### <instance> resume(key, [data])

**Description:**

Resumes the given Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to resume. |
| --- | --- | --- | --- |
| data | object | Yes | An optional data object that will be passed to the Scene and emitted by its resume event. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1044](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1044)  
> Since: 3.0.0

---

## run

### <instance> run(key, [data])

**Description:**

Runs the given Scene.

If the given Scene is paused, it will resume it. If sleeping, it will wake it.

If not running at all, it will be started.

Use this if you wish to open a modal Scene by calling `pause` on the current

Scene, then `run` on the modal Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to run. |
| --- | --- | --- | --- |
| data | object | Yes | A data object that will be passed to the Scene on start, wake, or resume. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1122](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1122)  
> Since: 3.10.0

---

## sendToBack

### <instance> sendToBack(key)

**Description:**

Sends a Scene to the back of the Scenes list.

This means it will render below all other Scenes.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to move. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1417](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1417)  
> Since: 3.0.0

---

## sleep

### <instance> sleep(key, [data])

**Description:**

Puts the given Scene to sleep.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to put to sleep. |
| --- | --- | --- | --- |
| data | object | Yes | An optional data object that will be passed to the Scene and emitted by its sleep event. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1070](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1070)  
> Since: 3.0.0

---

## start

### <instance> start(key, [data])

**Description:**

Starts the given Scene, if it is not starting, loading, or creating.

If the Scene is running, paused, or sleeping, it will be shutdown and then started.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to start. |
| --- | --- | --- | --- |
| data | object | Yes | Optional data object to pass to `Scene.Settings` and `Scene.init`, and `Scene.create`. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1176](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1176)  
> Since: 3.0.0

---

## stop

### <instance> stop(key, [data])

**Description:**

Stops the given Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to stop. |
| --- | --- | --- | --- |
| data | object | Yes | Optional data object to pass to Scene.shutdown. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1272)  
> Since: 3.0.0

---

## swapPosition

### <instance> swapPosition(keyA, keyB)

**Description:**

Swaps the positions of two Scenes in the Scenes list.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keyA | string | [Phaser.Scene](scene.md) | No | The first Scene to swap. |
| --- | --- | --- | --- |
| keyB | string | [Phaser.Scene](scene.md) | No | The second Scene to swap. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1642](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1642)  
> Since: 3.0.0

---

## switch

### <instance> switch(from, to, [data])

**Description:**

Sleeps one one Scene and starts the other.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| from | string | [Phaser.Scene](scene.md) | No | The Scene to sleep. |
| --- | --- | --- | --- |
| to | string | [Phaser.Scene](scene.md) | No | The Scene to start. |
| data | object | Yes | Optional data object to pass to `Scene.Settings` and `Scene.init`, and `Scene.create`. It is only passed when the scene starts for the first time. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1306](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1306)  
> Since: 3.0.0

---

## update

### <instance> update(time, delta)

**Description:**

Updates the Scenes.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | Time elapsed. |
| --- | --- | --- | --- |
| delta | number | No | Delta time from the last update. |

> Source: [src/scene/SceneManager.js#L546](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L546)  
> Since: 3.0.0

---

## wake

### <instance> wake(key, [data])

**Description:**

Awakens the given Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to wake up. |
| --- | --- | --- | --- |
| data | object | Yes | An optional data object that will be passed to the Scene and emitted by its wake event. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1096](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1096)  
> Since: 3.0.0

---

# Private Methods

## bootQueue

### <instance> bootQueue()

**Description:**

Internal first-time Scene boot handler.

**Access:** private

**Fires:** [Phaser.Core.Events#event:SYSTEM\_READY](../event/core-events.md)

> Source: [src/scene/SceneManager.js#L179](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L179)  
> Since: 3.2.0

---

## bootScene

### <instance> bootScene(scene)

**Description:**

Boot the given Scene.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to boot. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scenes.Events#event:TRANSITION\_INIT](../event/scenes-events.md)

> Source: [src/scene/SceneManager.js#L460](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L460)  
> Since: 3.0.0

---

## create

### <instance> create(scene)

**Description:**

Calls the given Scene's [Phaser.Scene#create](scene.md) method and updates its status.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene to create. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Scenes.Events#event:CREATE](../event/scenes-events.md), [Phaser.Scenes.Events#event:TRANSITION\_INIT](../event/scenes-events.md)

> Source: [src/scene/SceneManager.js#L602](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L602)  
> Since: 3.0.0

---

## createSceneFromFunction

### <instance> createSceneFromFunction(key, scene)

**Description:**

Creates and initializes a Scene from a function.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Scene. |
| --- | --- | --- | --- |
| scene | function | No | The function to create the Scene from. |

**Returns:** [Phaser.Scene](scene.md) - The created Scene.

> Source: [src/scene/SceneManager.js#L646](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L646)  
> Since: 3.0.0

---

## createSceneFromInstance

### <instance> createSceneFromInstance(key, newScene)

**Description:**

Creates and initializes a Scene instance.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Scene. |
| --- | --- | --- | --- |
| newScene | [Phaser.Scene](scene.md) | No | The Scene instance. |

**Returns:** [Phaser.Scene](scene.md) - The created Scene.

> Source: [src/scene/SceneManager.js#L690](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L690)  
> Since: 3.0.0

---

## createSceneFromObject

### <instance> createSceneFromObject(key, sceneConfig)

**Description:**

Creates and initializes a Scene from an Object definition.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key of the Scene. |
| --- | --- | --- | --- |
| sceneConfig | string | [Phaser.Types.Scenes.SettingsConfig](../typedef/types-scenes.md) | [Phaser.Types.Scenes.CreateSceneFromObjectConfig](../typedef/types-scenes.md) | No |

**Returns:** [Phaser.Scene](scene.md) - The created Scene.

> Source: [src/scene/SceneManager.js#L716](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L716)  
> Since: 3.0.0

---

## getKey

### <instance> getKey(key, sceneConfig)

**Description:**

Retrieves the key of a Scene from a Scene config.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | No | The key to check in the Scene config. |
| --- | --- | --- | --- |
| sceneConfig | [Phaser.Scene](scene.md) | [Phaser.Types.Scenes.SettingsConfig](../typedef/types-scenes.md) | function | No |

**Returns:** string - The Scene key.

> Source: [src/scene/SceneManager.js#L799](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L799)  
> Since: 3.0.0

---

## loadComplete

### <instance> loadComplete(loader)

**Description:**

Handles load completion for a Scene's Loader.

Starts the Scene that the Loader belongs to.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| loader | [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) | No | The loader that has completed loading. |
| --- | --- | --- | --- |

> Source: [src/scene/SceneManager.js#L516](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L516)  
> Since: 3.0.0

---

## payloadComplete

### <instance> payloadComplete(loader)

**Description:**

Handle payload completion for a Scene.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| loader | [Phaser.Loader.LoaderPlugin](loader-loaderplugin.md) | No | The loader that has completed loading its Scene's payload. |
| --- | --- | --- | --- |

> Source: [src/scene/SceneManager.js#L532](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L532)  
> Since: 3.0.0

---

## queueOp

### <instance> queueOp(op, keyA, [keyB], [data])

**Description:**

Queue a Scene operation for the next update.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| op | string | No | The operation to perform. |
| --- | --- | --- | --- |
| keyA | string | [Phaser.Scene](scene.md) | No | Scene A. |
| keyB | any | string | [Phaser.Scene](scene.md) | Yes |
| data | any | Yes | Optional data object to pass. |

**Returns:** [Phaser.Scenes.SceneManager](scenes-scenemanager.md) - This Scene Manager instance.

> Source: [src/scene/SceneManager.js#L1621](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/SceneManager.js#L1621)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [customViewports](#customviewports)

    - [customViewports: number](#customviewports-number)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [isBooted](#isbooted)

    - [isBooted: boolean](#isbooted-boolean)
  + [isProcessing](#isprocessing)

    - [isProcessing: boolean](#isprocessing-boolean)
  + [keys](#keys)

    - [keys: Record.<string, Phaser.Scene>](#keys-recordstring-phaserscene)
  + [scenes](#scenes)

    - [scenes: Array.<Phaser.Scene>](#scenes-arrayphaserscene)
  + [systemScene](#systemscene)

    - [systemScene: Phaser.Scene](#systemscene-phaserscene)
* [Private Members](#private-members)

  + [\_data](#_data)

    - [\_data: object](#_data-object)
  + [\_pending](#_pending)

    - [\_pending: array](#_pending-array)
  + [\_queue](#_queue)

    - [\_queue: array](#_queue-array)
  + [\_start](#_start)

    - [\_start: array](#_start-array)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(key, sceneConfig, [autoStart], [data])](#instance-addkey-sceneconfig-autostart-data)
  + [bringToTop](#bringtotop)

    - [<instance> bringToTop(key)](#instance-bringtotopkey)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [dump](#dump)

    - [<instance> dump()](#instance-dump)
  + [getAt](#getat)

    - [<instance> getAt(index)](#instance-getatindex)
  + [getIndex](#getindex)

    - [<instance> getIndex(key)](#instance-getindexkey)
  + [getScene](#getscene)

    - [<instance> getScene(key)](#instance-getscenekey)
  + [getScenes](#getscenes)

    - [<instance> getScenes([isActive], [inReverse])](#instance-getscenesisactive-inreverse)
  + [isActive](#isactive)

    - [<instance> isActive(key)](#instance-isactivekey)
  + [isPaused](#ispaused)

    - [<instance> isPaused(key)](#instance-ispausedkey)
  + [isSleeping](#issleeping)

    - [<instance> isSleeping(key)](#instance-issleepingkey)
  + [isVisible](#isvisible)

    - [<instance> isVisible(key)](#instance-isvisiblekey)
  + [moveAbove](#moveabove)

    - [<instance> moveAbove(keyA, keyB)](#instance-moveabovekeya-keyb)
  + [moveBelow](#movebelow)

    - [<instance> moveBelow(keyA, keyB)](#instance-movebelowkeya-keyb)
  + [moveDown](#movedown)

    - [<instance> moveDown(key)](#instance-movedownkey)
  + [moveUp](#moveup)

    - [<instance> moveUp(key)](#instance-moveupkey)
  + [pause](#pause)

    - [<instance> pause(key, [data])](#instance-pausekey-data)
  + [processQueue](#processqueue)

    - [<instance> processQueue()](#instance-processqueue)
  + [remove](#remove)

    - [<instance> remove(key)](#instance-removekey)
  + [render](#render)

    - [<instance> render(renderer)](#instance-renderrenderer)
  + [resume](#resume)

    - [<instance> resume(key, [data])](#instance-resumekey-data)
  + [run](#run)

    - [<instance> run(key, [data])](#instance-runkey-data)
  + [sendToBack](#sendtoback)

    - [<instance> sendToBack(key)](#instance-sendtobackkey)
  + [sleep](#sleep)

    - [<instance> sleep(key, [data])](#instance-sleepkey-data)
  + [start](#start)

    - [<instance> start(key, [data])](#instance-startkey-data)
  + [stop](#stop)

    - [<instance> stop(key, [data])](#instance-stopkey-data)
  + [swapPosition](#swapposition)

    - [<instance> swapPosition(keyA, keyB)](#instance-swappositionkeya-keyb)
  + [switch](#switch)

    - [<instance> switch(from, to, [data])](#instance-switchfrom-to-data)
  + [update](#update)

    - [<instance> update(time, delta)](#instance-updatetime-delta)
  + [wake](#wake)

    - [<instance> wake(key, [data])](#instance-wakekey-data)
* [Private Methods](#private-methods)

  + [bootQueue](#bootqueue)

    - [<instance> bootQueue()](#instance-bootqueue)
  + [bootScene](#bootscene)

    - [<instance> bootScene(scene)](#instance-bootscenescene)
  + [create](#create)

    - [<instance> create(scene)](#instance-createscene)
  + [createSceneFromFunction](#createscenefromfunction)

    - [<instance> createSceneFromFunction(key, scene)](#instance-createscenefromfunctionkey-scene)
  + [createSceneFromInstance](#createscenefrominstance)

    - [<instance> createSceneFromInstance(key, newScene)](#instance-createscenefrominstancekey-newscene)
  + [createSceneFromObject](#createscenefromobject)

    - [<instance> createSceneFromObject(key, sceneConfig)](#instance-createscenefromobjectkey-sceneconfig)
  + [getKey](#getkey)

    - [<instance> getKey(key, sceneConfig)](#instance-getkeykey-sceneconfig)
  + [loadComplete](#loadcomplete)

    - [<instance> loadComplete(loader)](#instance-loadcompleteloader)
  + [payloadComplete](#payloadcomplete)

    - [<instance> payloadComplete(loader)](#instance-payloadcompleteloader)
  + [queueOp](#queueop)

    - [<instance> queueOp(op, keyA, [keyB], [data])](#instance-queueopop-keya-keyb-data)

Back to top

©2025[Phaser](https://docs.phaser.io)