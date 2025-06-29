# ScenePlugin

Phaser.Scenes.ScenePlugin

The Scene Plugin is the main interface to the Scene Manager and allows you to control

any Scene running in your game. You should always use this plugin. By default, it is

mapped to the Scene property `this.scene`. Meaning, from within a Scene, you can call

methods such as `this.scene.start()`.

Note that nearly all methods in this class are run on a queue-basis and not

immediately. For example, calling `this.scene.launch('SceneB')` will try to

launch SceneB when the Scene Manager next updates, which is at the start of the game

step. All operations are queued and run in the order in which they are invoked here.

**Constructor**

`new ScenePlugin(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | The Scene that this ScenePlugin belongs to. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/scene/ScenePlugin.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L13)  
> Since: 3.0.0

# Public Members

## key

### key: string

**Description:**

The key of the Scene this ScenePlugin belongs to.

> Source: [src/scene/ScenePlugin.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L65)  
> Since: 3.0.0

---

## manager

### manager: [Phaser.Scenes.SceneManager](scenes-scenemanager.md)

**Description:**

The Game's SceneManager.

> Source: [src/scene/ScenePlugin.js#L74](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L74)  
> Since: 3.0.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

The Scene that this ScenePlugin belongs to.

> Source: [src/scene/ScenePlugin.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L38)  
> Since: 3.0.0

---

## settings

### settings: [Phaser.Types.Scenes.SettingsObject](../typedef/types-scenes.md)

**Description:**

The settings of the Scene this ScenePlugin belongs to.

> Source: [src/scene/ScenePlugin.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L56)  
> Since: 3.0.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

The Scene Systems instance of the Scene that this ScenePlugin belongs to.

> Source: [src/scene/ScenePlugin.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L47)  
> Since: 3.0.0

---

## transitionProgress

### transitionProgress: number

**Description:**

If this Scene is currently transitioning to another, this holds

the current percentage of the transition progress, between 0 and 1.

> Source: [src/scene/ScenePlugin.js#L83](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L83)  
> Since: 3.5.0

---

# Private Members

## \_duration

### \_duration: number

**Description:**

Transition duration.

**Access:** private

> Source: [src/scene/ScenePlugin.js#L113](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L113)  
> Since: 3.5.0

---

## \_elapsed

### \_elapsed: number

**Description:**

Transition elapsed timer.

**Access:** private

> Source: [src/scene/ScenePlugin.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L93)  
> Since: 3.5.0

---

## \_onUpdate

### \_onUpdate: function

**Description:**

Transition callback.

**Access:** private

> Source: [src/scene/ScenePlugin.js#L123](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L123)  
> Since: 3.5.0

---

## \_onUpdateScope

### \_onUpdateScope: object

**Description:**

Transition callback scope.

**Access:** private

> Source: [src/scene/ScenePlugin.js#L133](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L133)  
> Since: 3.5.0

---

## \_target

### \_target: [Phaser.Scene](scene.md)

**Description:**

Transition elapsed timer.

**Access:** private

> Source: [src/scene/ScenePlugin.js#L103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L103)  
> Since: 3.5.0

---

## \_willRemove

### \_willRemove: boolean

**Description:**

Will this Scene be removed from the Scene Manager after the transition completes?

**Access:** private

> Source: [src/scene/ScenePlugin.js#L153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L153)  
> Since: 3.5.0

---

## \_willSleep

### \_willSleep: boolean

**Description:**

Will this Scene sleep (true) after the transition, or stop (false)

**Access:** private

> Source: [src/scene/ScenePlugin.js#L143](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L143)  
> Since: 3.5.0

---

# Public Methods

## add

### <instance> add(key, sceneConfig, [autoStart], [data])

**Description:**

Add the Scene into the Scene Manager and start it if 'autoStart' is true or the Scene config 'active' property is set.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | No |  | A unique key used to reference the Scene, i.e. `MainMenu` or `Level1`. |
| --- | --- | --- | --- | --- |
| sceneConfig | [Phaser.Types.Scenes.SceneType](../typedef/types-scenes.md) | No |  | The config for the Scene |
| autoStart | boolean | Yes | false | If `true` the Scene will be started immediately after being added. |
| data | object | Yes |  | Optional data object. This will be set as `Scene.settings.data` and passed to `Scene.init`, and `Scene.create`. |

**Returns:** [Phaser.Scene](scene.md) - The added Scene, if it was added immediately, otherwise `null`.

> Source: [src/scene/ScenePlugin.js#L447](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L447)  
> Since: 3.0.0

---

## bringToTop

### <instance> bringToTop([key])

**Description:**

Brings a Scene to the top of the Scenes list.

This means it will render above all other Scenes.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to move. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L969](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L969)  
> Since: 3.0.0

---

## get

### <instance> get(key)

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
| key | string | [Phaser.Scene](scene.md) | No | The Scene to retrieve. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scene](scene.md) - The Scene.

> Source: [src/scene/ScenePlugin.js#L1017](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L1017)  
> Since: 3.0.0

---

## getIndex

### <instance> getIndex([key])

**Description:**

Retrieves the numeric index of a Scene in the Scenes list.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to get the index of. |
| --- | --- | --- | --- |

**Returns:** number - The index of the Scene.

> Source: [src/scene/ScenePlugin.js#L1062](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L1062)  
> Since: 3.7.0

---

## getStatus

### <instance> getStatus(key)

**Description:**

Return the status of the Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to get the status from. |
| --- | --- | --- | --- |

**Returns:** number - The Scene status. This maps to the `Phaser.Scene` constants, such as `Phaser.Scene.LOADING`.

> Source: [src/scene/ScenePlugin.js#L1039](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L1039)  
> Since: 3.60.0

---

## isActive

### <instance> isActive([key])

**Description:**

Checks if the given Scene is running or not?

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to check. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the Scene is running, or `null` if no matching Scene was found.

> Source: [src/scene/ScenePlugin.js#L751](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L751)  
> Since: 3.0.0

---

## isPaused

### <instance> isPaused([key])

**Description:**

Checks if the given Scene is paused or not?

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to check. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the Scene is paused, or `null` if no matching Scene was found.

> Source: [src/scene/ScenePlugin.js#L771](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L771)  
> Since: 3.17.0

---

## isSleeping

### <instance> isSleeping([key])

**Description:**

Checks if the given Scene is sleeping or not?

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to check. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the Scene is sleeping, or `null` if no matching Scene was found.

> Source: [src/scene/ScenePlugin.js#L731](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L731)  
> Since: 3.0.0

---

## isVisible

### <instance> isVisible([key])

**Description:**

Checks if the given Scene is visible or not?

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to check. |
| --- | --- | --- | --- |

**Returns:** boolean - Whether the Scene is visible, or `null` if no matching Scene was found.

> Source: [src/scene/ScenePlugin.js#L791](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L791)  
> Since: 3.0.0

---

## launch

### <instance> launch(key, [data])

**Description:**

Launch the given Scene and run it in parallel with this one.

This will happen at the next Scene Manager update, not immediately.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to launch. |
| --- | --- | --- | --- |
| data | object | Yes | The Scene data. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L465](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L465)  
> Since: 3.0.0

---

## moveAbove

### <instance> moveAbove(keyA, [keyB])

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
| keyA | string | [Phaser.Scene](scene.md) | No | The Scene that Scene B will be moved to be above. |
| --- | --- | --- | --- |
| keyB | string | [Phaser.Scene](scene.md) | Yes | The Scene to be moved. If none is given it defaults to this Scene. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L839](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L839)  
> Since: 3.2.0

---

## moveBelow

### <instance> moveBelow(keyA, [keyB])

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
| keyA | string | [Phaser.Scene](scene.md) | No | The Scene that Scene B will be moved to be below. |
| --- | --- | --- | --- |
| keyB | string | [Phaser.Scene](scene.md) | Yes | The Scene to be moved. If none is given it defaults to this Scene. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L868](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L868)  
> Since: 3.2.0

---

## moveDown

### <instance> moveDown([key])

**Description:**

Moves a Scene down one position in the Scenes list.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to move. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L947](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L947)  
> Since: 3.0.0

---

## moveUp

### <instance> moveUp([key])

**Description:**

Moves a Scene up one position in the Scenes list.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to move. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L925](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L925)  
> Since: 3.0.0

---

## pause

### <instance> pause([key], [data])

**Description:**

Pause the Scene - this stops the update step from happening but it still renders.

This will happen at the next Scene Manager update, not immediately.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to pause. |
| --- | --- | --- | --- |
| data | object | Yes | An optional data object that will be passed to the Scene and emitted in its pause event. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L523](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L523)  
> Since: 3.0.0

---

## remove

### <instance> remove([key])

**Description:**

Removes a Scene from the SceneManager.

The Scene is removed from the local scenes array, it's key is cleared from the keys

cache and Scene.Systems.destroy is then called on it.

If the SceneManager is processing the Scenes when this method is called it will

queue the operation for the next update sequence.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to be removed. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L897](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L897)  
> Since: 3.2.0

---

## restart

### <instance> restart([data])

**Description:**

Restarts this Scene.

This will happen at the next Scene Manager update, not immediately.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | object | Yes | The Scene data. If no value is given it will not overwrite any previous data that may exist. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L222](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L222)  
> Since: 3.4.0

---

## resume

### <instance> resume([key], [data])

**Description:**

Resume the Scene - starts the update loop again.

This will happen at the next Scene Manager update, not immediately.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to resume. |
| --- | --- | --- | --- |
| data | object | Yes | An optional data object that will be passed to the Scene and emitted in its resume event. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L548](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L548)  
> Since: 3.0.0

---

## run

### <instance> run(key, [data])

**Description:**

Runs the given Scene, but does not change the state of this Scene.

This will happen at the next Scene Manager update, not immediately.

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
| data | object | Yes | A data object that will be passed to the Scene and emitted in its ready, wake, or resume events. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L491](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L491)  
> Since: 3.10.0

---

## sendToBack

### <instance> sendToBack([key])

**Description:**

Sends a Scene to the back of the Scenes list.

This means it will render below all other Scenes.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to move. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L993](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L993)  
> Since: 3.0.0

---

## setActive

### <instance> setActive(value, [key], [data])

**Description:**

Sets the active state of the given Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | If `true` the Scene will be resumed. If `false` it will be paused. |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to set the active state of. |
| data | object | Yes | An optional data object that will be passed to the Scene and emitted with its events. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L674](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L674)  
> Since: 3.0.0

---

## setVisible

### <instance> setVisible(value, [key])

**Description:**

Sets the visible state of the given Scene.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | The visible value. |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to set the visible state for. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L703](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L703)  
> Since: 3.0.0

---

## sleep

### <instance> sleep([key], [data])

**Description:**

Makes the Scene sleep (no update, no render) but doesn't shutdown.

This will happen at the next Scene Manager update, not immediately.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to put to sleep. |
| --- | --- | --- | --- |
| data | object | Yes | An optional data object that will be passed to the Scene and emitted in its sleep event. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L573](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L573)  
> Since: 3.0.0

---

## start

### <instance> start([key], [data])

**Description:**

Shutdown this Scene and run the given one.

This will happen at the next Scene Manager update, not immediately.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to start. |
| --- | --- | --- | --- |
| data | object | Yes | The Scene data. If no value is given it will not overwrite any previous data that may exist. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L196](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L196)  
> Since: 3.0.0

---

## stop

### <instance> stop([key], [data])

**Description:**

Shutdown the Scene, clearing display list, timers, etc.

This happens at the next Scene Manager update, not immediately.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to stop. |
| --- | --- | --- | --- |
| data | any | Yes | Optional data object to pass to Scene.Systems.shutdown. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L649](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L649)  
> Since: 3.0.0

---

## swapPosition

### <instance> swapPosition(keyA, [keyB])

**Description:**

Swaps the position of two scenes in the Scenes list.

This controls the order in which they are rendered and updated.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| keyA | string | [Phaser.Scene](scene.md) | No | The first Scene to swap. |
| --- | --- | --- | --- |
| keyB | string | [Phaser.Scene](scene.md) | Yes | The second Scene to swap. If none is given it defaults to this Scene. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L811](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L811)  
> Since: 3.2.0

---

## switch

### <instance> switch(key, [data])

**Description:**

Makes this Scene sleep then starts the Scene given.

This will happen at the next Scene Manager update, not immediately.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | No | The Scene to start. |
| --- | --- | --- | --- |
| data | any | Yes | Optional data object to pass to either the Scene `wake` or `start` method. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L623](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L623)  
> Since: 3.0.0

---

## transition

### <instance> transition(config)

**Description:**

This will start a transition from the current Scene to the target Scene given.

The target Scene cannot be the same as the current Scene.

The transition will last for the duration specified in milliseconds.

You can have the target Scene moved above or below this one in the display list.

You can specify an update callback. This callback will be invoked *every frame* for the duration

of the transition.

This Scene can either be sent to sleep at the end of the transition, or stopped. The default is to stop.

There are also 5 transition related events: This scene will emit the event `transitionout` when

the transition begins, which is typically the frame after calling this method.

The target Scene will emit the event `transitioninit` when that Scene's `init` method is called.

It will then emit the event `transitionstart` when its `create` method is called.

If the Scene was sleeping and has been woken up, it will emit the event `transitionwake` instead of these two,

as the Scenes `init` and `create` methods are not invoked when a Scene wakes up.

When the duration of the transition has elapsed it will emit the event `transitioncomplete`.

These events are cleared of all listeners when the Scene shuts down, but not if it is sent to sleep.

It's important to understand that the duration of the transition begins the moment you call this method.

If the Scene you are transitioning to includes delayed processes, such as waiting for files to load, the

time still counts down even while that is happening. If the game itself pauses, or something else causes

this Scenes update loop to stop, then the transition will also pause for that duration. There are

checks in place to prevent you accidentally stopping a transitioning Scene but if you've got code to

override this understand that until the target Scene completes it might never be unlocked for input events.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Scenes.SceneTransitionConfig](../typedef/types-scenes.md) | No | The transition configuration object. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` is the transition was started, otherwise `false`.

**Fires:** [Phaser.Scenes.Events#event:TRANSITION\_OUT](../event/scenes-events.md)

> Source: [src/scene/ScenePlugin.js#L244](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L244)  
> Since: 3.5.0

---

## wake

### <instance> wake([key], [data])

**Description:**

Makes the Scene wake-up (starts update and render)

This will happen at the next Scene Manager update, not immediately.

**Tags:**

* generic
* genericUse

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | string | [Phaser.Scene](scene.md) | Yes | The Scene to wake up. |
| --- | --- | --- | --- |
| data | object | Yes | An optional data object that will be passed to the Scene and emitted in its wake event. |

**Returns:** [Phaser.Scenes.ScenePlugin](scenes-sceneplugin.md) - This Scene Plugin instance.

> Source: [src/scene/ScenePlugin.js#L598](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L598)  
> Since: 3.0.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

> Source: [src/scene/ScenePlugin.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L167)  
> Since: 3.0.0

---

## checkValidTransition

### <instance> checkValidTransition(target)

**Description:**

Checks to see if this Scene can transition to the target Scene or not.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| target | [Phaser.Scene](scene.md) | No | The Scene to test against. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if this Scene can transition, otherwise `false`.

> Source: [src/scene/ScenePlugin.js#L356](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L356)  
> Since: 3.5.0

---

## destroy

### <instance> destroy()

**Description:**

The Scene that owns this plugin is being destroyed.

We need to shutdown and then kill off all external references.

**Access:** private

> Source: [src/scene/ScenePlugin.js#L1099](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L1099)  
> Since: 3.0.0

---

## pluginStart

### <instance> pluginStart()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

> Source: [src/scene/ScenePlugin.js#L180](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L180)  
> Since: 3.5.0

---

## shutdown

### <instance> shutdown()

**Description:**

The Scene that owns this plugin is shutting down.

We need to kill and reset all internal properties as well as stop listening to Scene events.

**Access:** private

> Source: [src/scene/ScenePlugin.js#L1082](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L1082)  
> Since: 3.0.0

---

## step

### <instance> step(time, delta)

**Description:**

A single game step. This is only called if the parent Scene is transitioning

out to another Scene.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/scene/ScenePlugin.js#L378](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L378)  
> Since: 3.5.0

---

## transitionComplete

### <instance> transitionComplete()

**Description:**

Called by `step` when the transition out of this scene to another is over.

**Access:** private

**Fires:** [Phaser.Scenes.Events#event:TRANSITION\_COMPLETE](../event/scenes-events.md)

> Source: [src/scene/ScenePlugin.js#L406](https://github.com/phaserjs/phaser/blob/v3.87.0/src/scene/ScenePlugin.js#L406)  
> Since: 3.5.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [key](#key)

    - [key: string](#key-string)
  + [manager](#manager)

    - [manager: Phaser.Scenes.SceneManager](#manager-phaserscenesscenemanager)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [settings](#settings)

    - [settings: Phaser.Types.Scenes.SettingsObject](#settings-phasertypesscenessettingsobject)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
  + [transitionProgress](#transitionprogress)

    - [transitionProgress: number](#transitionprogress-number)
* [Private Members](#private-members)

  + [\_duration](#_duration)

    - [\_duration: number](#_duration-number)
  + [\_elapsed](#_elapsed)

    - [\_elapsed: number](#_elapsed-number)
  + [\_onUpdate](#_onupdate)

    - [\_onUpdate: function](#_onupdate-function)
  + [\_onUpdateScope](#_onupdatescope)

    - [\_onUpdateScope: object](#_onupdatescope-object)
  + [\_target](#_target)

    - [\_target: Phaser.Scene](#_target-phaserscene)
  + [\_willRemove](#_willremove)

    - [\_willRemove: boolean](#_willremove-boolean)
  + [\_willSleep](#_willsleep)

    - [\_willSleep: boolean](#_willsleep-boolean)
* [Public Methods](#public-methods)

  + [add](#add)

    - [<instance> add(key, sceneConfig, [autoStart], [data])](#instance-addkey-sceneconfig-autostart-data)
  + [bringToTop](#bringtotop)

    - [<instance> bringToTop([key])](#instance-bringtotopkey)
  + [get](#get)

    - [<instance> get(key)](#instance-getkey)
  + [getIndex](#getindex)

    - [<instance> getIndex([key])](#instance-getindexkey)
  + [getStatus](#getstatus)

    - [<instance> getStatus(key)](#instance-getstatuskey)
  + [isActive](#isactive)

    - [<instance> isActive([key])](#instance-isactivekey)
  + [isPaused](#ispaused)

    - [<instance> isPaused([key])](#instance-ispausedkey)
  + [isSleeping](#issleeping)

    - [<instance> isSleeping([key])](#instance-issleepingkey)
  + [isVisible](#isvisible)

    - [<instance> isVisible([key])](#instance-isvisiblekey)
  + [launch](#launch)

    - [<instance> launch(key, [data])](#instance-launchkey-data)
  + [moveAbove](#moveabove)

    - [<instance> moveAbove(keyA, [keyB])](#instance-moveabovekeya-keyb)
  + [moveBelow](#movebelow)

    - [<instance> moveBelow(keyA, [keyB])](#instance-movebelowkeya-keyb)
  + [moveDown](#movedown)

    - [<instance> moveDown([key])](#instance-movedownkey)
  + [moveUp](#moveup)

    - [<instance> moveUp([key])](#instance-moveupkey)
  + [pause](#pause)

    - [<instance> pause([key], [data])](#instance-pausekey-data)
  + [remove](#remove)

    - [<instance> remove([key])](#instance-removekey)
  + [restart](#restart)

    - [<instance> restart([data])](#instance-restartdata)
  + [resume](#resume)

    - [<instance> resume([key], [data])](#instance-resumekey-data)
  + [run](#run)

    - [<instance> run(key, [data])](#instance-runkey-data)
  + [sendToBack](#sendtoback)

    - [<instance> sendToBack([key])](#instance-sendtobackkey)
  + [setActive](#setactive)

    - [<instance> setActive(value, [key], [data])](#instance-setactivevalue-key-data)
  + [setVisible](#setvisible)

    - [<instance> setVisible(value, [key])](#instance-setvisiblevalue-key)
  + [sleep](#sleep)

    - [<instance> sleep([key], [data])](#instance-sleepkey-data)
  + [start](#start)

    - [<instance> start([key], [data])](#instance-startkey-data)
  + [stop](#stop)

    - [<instance> stop([key], [data])](#instance-stopkey-data)
  + [swapPosition](#swapposition)

    - [<instance> swapPosition(keyA, [keyB])](#instance-swappositionkeya-keyb)
  + [switch](#switch)

    - [<instance> switch(key, [data])](#instance-switchkey-data)
  + [transition](#transition)

    - [<instance> transition(config)](#instance-transitionconfig)
  + [wake](#wake)

    - [<instance> wake([key], [data])](#instance-wakekey-data)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [checkValidTransition](#checkvalidtransition)

    - [<instance> checkValidTransition(target)](#instance-checkvalidtransitiontarget)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [pluginStart](#pluginstart)

    - [<instance> pluginStart()](#instance-pluginstart)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [step](#step)

    - [<instance> step(time, delta)](#instance-steptime-delta)
  + [transitionComplete](#transitioncomplete)

    - [<instance> transitionComplete()](#instance-transitioncomplete)

Back to top

©2025[Phaser](https://docs.phaser.io)