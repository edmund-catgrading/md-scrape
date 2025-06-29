# InputPlugin

Phaser.Input.InputPlugin

The Input Plugin belongs to a Scene and handles all input related events and operations for it.

You can access it from within a Scene using `this.input`.

It emits events directly. For example, you can do:

```
Copy
this.input.on('pointerdown', callback, context);


```

To listen for a pointer down event anywhere on the game canvas.

Game Objects can be enabled for input by calling their `setInteractive` method. After which they

will directly emit input events:

```
Copy
var sprite = this.add.sprite(x, y, texture);

sprite.setInteractive();

sprite.on('pointerdown', callback, context);


```

There are lots of game configuration options available relating to input.

See the [Input Config object](code Phaser.Types.Core.InputConfig) for more details, including how to deal with Phaser

listening for input events outside of the canvas, how to set a default number of pointers, input

capture settings and more.

Please also see the Input examples and tutorials for further information.

**Incorrect input coordinates with Angular**

If you are using Phaser within Angular, and use nglf or the router, to make the component in which the Phaser game resides

change state (i.e. appear or disappear) then you'll need to notify the Scale Manager about this, as Angular will mess with

the DOM in a way in which Phaser can't detect directly. Call `this.scale.updateBounds()` as part of your game init in order

to refresh the canvas DOM bounds values, which Phaser uses for input point position calculations.

**Constructor**

`new InputPlugin(scene)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| scene | [Phaser.Scene](scene.md) | No | A reference to the Scene that this Input Plugin is responsible for. |
| --- | --- | --- | --- |

---

**Scope**: static

**Extends**

> [Phaser.Events.EventEmitter](events-eventemitter.md)

> Source: [src/input/InputPlugin.js#L29](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L29)  
> Since: 3.0.0

# Public Members

## activePointer

### activePointer: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

The current active input Pointer.

> Source: [src/input/InputPlugin.js#L3271](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3271)  
> Since: 3.0.0

---

## cameras

### cameras: [Phaser.Cameras.Scene2D.CameraManager](cameras-scene2d-cameramanager.md)

**Description:**

A reference to the Scene Cameras Manager. This property is set during the `boot` method.

> Source: [src/input/InputPlugin.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L149)  
> Since: 3.0.0

---

## displayList

### displayList: [Phaser.GameObjects.DisplayList](gameobjects-displaylist.md)

**Description:**

A reference to the Scene Display List. This property is set during the `boot` method.

> Source: [src/input/InputPlugin.js#L140](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L140)  
> Since: 3.0.0

---

## dragDistanceThreshold

### dragDistanceThreshold: number

**Description:**

The distance, in pixels, a pointer has to move while being held down, before it thinks it is being dragged.

> Source: [src/input/InputPlugin.js#L247](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L247)  
> Since: 3.0.0

---

## dragTimeThreshold

### dragTimeThreshold: number

**Description:**

The amount of time, in ms, a pointer has to be held down before it thinks it is dragging.

The default polling rate is to poll only on move so once the time threshold is reached the

drag event will not start until you move the mouse. If you want it to start immediately

when the time threshold is reached, you must increase the polling rate by calling

[`setPollAlways`](Phaser.Input.InputPlugin.md) or

[`setPollRate`](Phaser.Input.InputPlugin.md).

> Source: [src/input/InputPlugin.js#L257](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L257)  
> Since: 3.0.0

---

## enabled

### enabled: boolean

**Description:**

If `true` this Input Plugin will process DOM input events.

> Source: [src/input/InputPlugin.js#L130](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L130)  
> Since: 3.5.0

---

## gamepad

### gamepad: [Phaser.Input.Gamepad.GamepadPlugin](input-gamepad-gamepadplugin.md)

**Description:**

An instance of the Gamepad Plugin class, if enabled via the `input.gamepad` Scene or Game Config property.

Use this to create access Gamepads connected to the browser and respond to gamepad buttons.

> Source: [src/input/gamepad/GamepadPlugin.js#L630](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/GamepadPlugin.js#L630)  
> Since: 3.10.0

---

## isOver

### isOver: boolean

**Description:**

Are any mouse or touch pointers currently over the game canvas?

> Source: [src/input/InputPlugin.js#L3235](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3235)  
> Since: 3.16.0

---

## keyboard

### keyboard: [Phaser.Input.Keyboard.KeyboardPlugin](input-keyboard-keyboardplugin.md)

**Description:**

An instance of the Keyboard Plugin class, if enabled via the `input.keyboard` Scene or Game Config property.

Use this to create Key objects and listen for keyboard specific events.

> Source: [src/input/keyboard/KeyboardPlugin.js#L946](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/KeyboardPlugin.js#L946)  
> Since: 3.10.0

---

## manager

### manager: [Phaser.Input.InputManager](input-inputmanager.md)

**Description:**

A reference to the Game Input Manager.

> Source: [src/input/InputPlugin.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L111)  
> Since: 3.0.0

---

## mouse

### mouse: [Phaser.Input.Mouse.MouseManager](input-mouse-mousemanager.md)

**Description:**

A reference to the Mouse Manager.

This property is only set if Mouse support has been enabled in your Game Configuration file.

If you just wish to get access to the mouse pointer, use the `mousePointer` property instead.

> Source: [src/input/InputPlugin.js#L161](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L161)  
> Since: 3.0.0

---

## mousePointer

### mousePointer: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

The mouse has its own unique Pointer object, which you can reference directly if making a *desktop specific game*.

If you are supporting both desktop and touch devices then do not use this property, instead use `activePointer`

which will always map to the most recently interacted pointer.

> Source: [src/input/InputPlugin.js#L3252](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3252)  
> Since: 3.10.0

---

## pointer1

### pointer1: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

A touch-based Pointer object.

This will be `undefined` by default unless you add a new Pointer using `addPointer`.

> Source: [src/input/InputPlugin.js#L3288](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3288)  
> Since: 3.10.0

---

## pointer10

### pointer10: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

A touch-based Pointer object.

This will be `undefined` by default unless you add a new Pointer using `addPointer`.

> Source: [src/input/InputPlugin.js#L3450](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3450)  
> Since: 3.10.0

---

## pointer2

### pointer2: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

A touch-based Pointer object.

This will be `undefined` by default unless you add a new Pointer using `addPointer`.

> Source: [src/input/InputPlugin.js#L3306](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3306)  
> Since: 3.10.0

---

## pointer3

### pointer3: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

A touch-based Pointer object.

This will be `undefined` by default unless you add a new Pointer using `addPointer`.

> Source: [src/input/InputPlugin.js#L3324](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3324)  
> Since: 3.10.0

---

## pointer4

### pointer4: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

A touch-based Pointer object.

This will be `undefined` by default unless you add a new Pointer using `addPointer`.

> Source: [src/input/InputPlugin.js#L3342](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3342)  
> Since: 3.10.0

---

## pointer5

### pointer5: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

A touch-based Pointer object.

This will be `undefined` by default unless you add a new Pointer using `addPointer`.

> Source: [src/input/InputPlugin.js#L3360](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3360)  
> Since: 3.10.0

---

## pointer6

### pointer6: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

A touch-based Pointer object.

This will be `undefined` by default unless you add a new Pointer using `addPointer`.

> Source: [src/input/InputPlugin.js#L3378](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3378)  
> Since: 3.10.0

---

## pointer7

### pointer7: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

A touch-based Pointer object.

This will be `undefined` by default unless you add a new Pointer using `addPointer`.

> Source: [src/input/InputPlugin.js#L3396](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3396)  
> Since: 3.10.0

---

## pointer8

### pointer8: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

A touch-based Pointer object.

This will be `undefined` by default unless you add a new Pointer using `addPointer`.

> Source: [src/input/InputPlugin.js#L3414](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3414)  
> Since: 3.10.0

---

## pointer9

### pointer9: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

A touch-based Pointer object.

This will be `undefined` by default unless you add a new Pointer using `addPointer`.

> Source: [src/input/InputPlugin.js#L3432](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3432)  
> Since: 3.10.0

---

## pollRate

### pollRate: number

**Description:**

How often should the Pointers be checked?

The value is a time, given in ms, and is the time that must have elapsed between game steps before

the Pointers will be polled again. When a pointer is polled it runs a hit test to see which Game

Objects are currently below it, or being interacted with it.

Pointers will *always* be checked if they have been moved by the user, or press or released.

This property only controls how often they will be polled if they have not been updated.

You should set this if you want to have Game Objects constantly check against the pointers, even

if the pointer didn't itself move.

Set to 0 to poll constantly. Set to -1 to only poll on user movement.

> Source: [src/input/InputPlugin.js#L187](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L187)  
> Since: 3.0.0

---

## scene

### scene: [Phaser.Scene](scene.md)

**Description:**

A reference to the Scene that this Input Plugin is responsible for.

> Source: [src/input/InputPlugin.js#L84](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L84)  
> Since: 3.0.0

---

## settings

### settings: [Phaser.Types.Scenes.SettingsObject](../typedef/types-scenes.md)

**Description:**

A reference to the Scene Systems Settings.

> Source: [src/input/InputPlugin.js#L102](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L102)  
> Since: 3.5.0

---

## systems

### systems: [Phaser.Scenes.Systems](scenes-systems.md)

**Description:**

A reference to the Scene Systems class.

> Source: [src/input/InputPlugin.js#L93](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L93)  
> Since: 3.0.0

---

## topOnly

### topOnly: boolean

**Description:**

When set to `true` (the default) the Input Plugin will emulate DOM behavior by only emitting events from

the top-most Game Objects in the Display List.

If set to `false` it will emit events from all Game Objects below a Pointer, not just the top one.

> Source: [src/input/InputPlugin.js#L174](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L174)  
> Since: 3.0.0

---

## x

### x: number

**Description:**

The x coordinates of the ActivePointer based on the first camera in the camera list.

This is only safe to use if your game has just 1 non-transformed camera and doesn't use multi-touch.

> Source: [src/input/InputPlugin.js#L3199](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3199)  
> Since: 3.0.0

---

## y

### y: number

**Description:**

The y coordinates of the ActivePointer based on the first camera in the camera list.

This is only safe to use if your game has just 1 non-transformed camera and doesn't use multi-touch.

> Source: [src/input/InputPlugin.js#L3217](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3217)  
> Since: 3.0.0

---

# Private Members

## \_drag

### \_drag: Object

**Description:**

A list of all Interactive Objects currently considered as being 'draggable' by any pointer, indexed by pointer ID.

**Access:** private

> Source: [src/input/InputPlugin.js#L339](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L339)  
> Since: 3.0.0

---

## \_draggable

### \_draggable: Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)>

**Description:**

A list of all Game Objects that have been enabled for dragging.

**Access:** private

> Source: [src/input/InputPlugin.js#L328](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L328)  
> Since: 3.0.0

---

## \_dragState

### \_dragState: Array.<number>

**Description:**

A array containing the dragStates, for this Scene, index by the Pointer ID.

**Access:** private

> Source: [src/input/InputPlugin.js#L349](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L349)  
> Since: 3.16.0

---

## \_eventContainer

### \_eventContainer: [Phaser.Types.Input.EventData](../typedef/types-input.md)

**Description:**

Internal event propagation callback container.

**Access:** private

> Source: [src/input/InputPlugin.js#L222](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L222)  
> Since: 3.13.0

---

## \_eventData

### \_eventData: object

**Description:**

Internal event propagation data object.

**Access:** private

> Source: [src/input/InputPlugin.js#L237](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L237)  
> Since: 3.13.0

---

## \_list

### \_list: Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)>

**Description:**

A list of all Game Objects that have been set to be interactive in the Scene this Input Plugin is managing.

**Access:** private

> Source: [src/input/InputPlugin.js#L295](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L295)  
> Since: 3.0.0

---

## \_over

### \_over: Object

**Description:**

A list of all Interactive Objects currently considered as being 'over' by any pointer, indexed by pointer ID.

**Access:** private

> Source: [src/input/InputPlugin.js#L359](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L359)  
> Since: 3.0.0

---

## \_pendingInsertion

### \_pendingInsertion: Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)>

**Description:**

Objects waiting to be inserted to the list on the next call to 'begin'.

**Access:** private

> Source: [src/input/InputPlugin.js#L306](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L306)  
> Since: 3.0.0

---

## \_pendingRemoval

### \_pendingRemoval: Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)>

**Description:**

Objects waiting to be removed from the list on the next call to 'begin'.

**Access:** private

> Source: [src/input/InputPlugin.js#L317](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L317)  
> Since: 3.0.0

---

## \_pollTimer

### \_pollTimer: number

**Description:**

Internal poll timer value.

**Access:** private

> Source: [src/input/InputPlugin.js#L209](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L209)  
> Since: 3.0.0

---

## \_temp

### \_temp: array

**Description:**

Used to temporarily store the results of the Hit Test

**Access:** private

> Source: [src/input/InputPlugin.js#L273](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L273)  
> Since: 3.0.0

---

## \_tempZones

### \_tempZones: array

**Description:**

Used to temporarily store the results of the Hit Test dropZones

**Access:** private

> Source: [src/input/InputPlugin.js#L284](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L284)  
> Since: 3.0.0

---

## \_updatedThisFrame

### \_updatedThisFrame: boolean

**Description:**

Internal property that tracks frame event state.

**Access:** private

> Source: [src/input/InputPlugin.js#L379](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L379)  
> Since: 3.18.0

---

## \_validTypes

### \_validTypes: Array.<string>

**Description:**

A list of valid DOM event types.

**Access:** private

> Source: [src/input/InputPlugin.js#L369](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L369)  
> Since: 3.0.0

---

## pluginEvents

### pluginEvents: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

Internal event queue used for plugins only.

**Access:** private

> Source: [src/input/InputPlugin.js#L120](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L120)  
> Since: 3.10.0

---

# Public Methods

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

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#addListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L111](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L111)  
> Since: 3.0.0

---

## addPointer

### <instance> addPointer([quantity])

**Description:**

Adds new Pointer objects to the Input Manager.

By default Phaser creates 2 pointer objects: `mousePointer` and `pointer1`.

You can create more either by calling this method, or by setting the `input.activePointers` property

in the Game Config, up to a maximum of 10 pointers.

The first 10 pointers are available via the `InputPlugin.pointerX` properties, once they have been added

via this method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| quantity | number | Yes | 1 | The number of new Pointers to create. A maximum of 10 is allowed in total. |
| --- | --- | --- | --- | --- |

**Returns:** Array.<[Phaser.Input.Pointer](input-pointer.md)> - An array containing all of the new Pointer objects that were created.

> Source: [src/input/InputPlugin.js#L3011](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3011)  
> Since: 3.10.0

---

## clear

### <instance> clear(gameObject, [skipQueue])

**Description:**

Clears a Game Object so it no longer has an Interactive Object associated with it.

The Game Object is then queued for removal from the Input Plugin on the next update.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object that will have its Interactive Object removed. |
| --- | --- | --- | --- | --- |
| skipQueue | boolean | Yes | false | Skip adding this Game Object into the removal queue? |

**Returns:** [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) - The Game Object that had its Interactive Object removed.

> Source: [src/input/InputPlugin.js#L797](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L797)  
> Since: 3.0.0

---

## disable

### <instance> disable(gameObject, [resetCursor])

**Description:**

Disables Input on a single Game Object.

An input disabled Game Object still retains its Interactive Object component and can be re-enabled

at any time, by passing it to `InputPlugin.enable`.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object to have its input system disabled. |
| --- | --- | --- | --- | --- |
| resetCursor | boolean | Yes | false | Reset the cursor to the default? |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This Input Plugin.

> Source: [src/input/InputPlugin.js#L847](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L847)  
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

## enable

### <instance> enable(gameObject, [hitArea], [hitAreaCallback], [dropZone])

**Description:**

Enable a Game Object for interaction.

If the Game Object already has an Interactive Object component, it is enabled and returned.

Otherwise, a new Interactive Object component is created and assigned to the Game Object's `input` property.

Input works by using hit areas, these are nearly always geometric shapes, such as rectangles or circles, that act as the hit area

for the Game Object. However, you can provide your own hit area shape and callback, should you wish to handle some more advanced

input detection.

If no arguments are provided it will try and create a rectangle hit area based on the texture frame the Game Object is using. If

this isn't a texture-bound object, such as a Graphics or BitmapText object, this will fail, and you'll need to provide a specific

shape for it to use.

You can also provide an Input Configuration Object as the only argument to this method.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object to be enabled for input. |
| --- | --- | --- | --- | --- |
| hitArea | [Phaser.Types.Input.InputConfiguration](../typedef/types-input.md) | any | Yes |  | Either an input configuration object, or a geometric shape that defines the hit area for the Game Object. If not specified a Rectangle will be used. |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes |  | The 'contains' function to invoke to check if the pointer is within the hit area. |
| dropZone | boolean | Yes | false | Is this Game Object a drop zone or not? |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This Input Plugin.

> Source: [src/input/InputPlugin.js#L903](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L903)  
> Since: 3.0.0

---

## enableDebug

### <instance> enableDebug(gameObject, [color])

**Description:**

Creates an Input Debug Shape for the given Game Object.

The Game Object must have *already* been enabled for input prior to calling this method.

This is intended to assist you during development and debugging.

Debug Shapes can only be created for Game Objects that are using standard Phaser Geometry for input,

including: Circle, Ellipse, Line, Polygon, Rectangle and Triangle.

Game Objects that are using their automatic hit areas are using Rectangles by default, so will also work.

The Debug Shape is created and added to the display list and is then kept in sync with the Game Object

it is connected with. Should you need to modify it yourself, such as to hide it, you can access it via

the Game Object property: `GameObject.input.hitAreaDebug`.

Calling this method on a Game Object that already has a Debug Shape will first destroy the old shape,

before creating a new one. If you wish to remove the Debug Shape entirely, you should call the

method `InputPlugin.removeDebug`.

Note that the debug shape will only show the outline of the input area. If the input test is using a

pixel perfect check, for example, then this is not displayed. If you are using a custom shape, that

doesn't extend one of the base Phaser Geometry objects, as your hit area, then this method will not

work.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object to create the input debug shape for. |
| --- | --- | --- | --- | --- |
| color | number | Yes | "0x00ff00" | The outline color of the debug shape. |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This Input Plugin.

> Source: [src/input/InputPlugin.js#L2608](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2608)  
> Since: 3.19.0

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

## forceDownState

### <instance> forceDownState(pointer, gameObject)

**Description:**

This method will force the given Game Object into the 'down' input state.

This will check to see if the Game Object is enabled for input, and if so,

it will emit the `GAMEOBJECT_POINTER_DOWN` event for it. If that doesn't change

the input state, it will then emit the `GAMEOBJECT_DOWN` event.

The Game Object is not checked against the Pointer to see if it can enter this state,

that is up to you to do before calling this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The pointer to use when setting the state. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to have its state set. |

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_DOWN](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_DOWN](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L2080](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2080)  
> Since: 3.85.0

---

## forceOutState

### <instance> forceOutState(pointer, gameObject)

**Description:**

This method will force the given Game Object into the 'out' input state.

This will check to see if the Game Object is enabled for input, and if so,

it will emit the `GAMEOBJECT_POINTER_OUT` event for it. If that doesn't change

the input state, it will then emit the `GAMEOBJECT_OUT` event.

The Game Object is not checked against the Pointer to see if it can enter this state,

that is up to you to do before calling this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The pointer to use when setting the state. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to have its state set. |

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_OUT](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_OUT](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L2149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2149)  
> Since: 3.85.0

---

## forceOverState

### <instance> forceOverState(pointer, gameObject)

**Description:**

This method will force the given Game Object into the 'over' input state.

This will check to see if the Game Object is enabled for input, and if so,

it will emit the `GAMEOBJECT_POINTER_OVER` event for it. If that doesn't change

the input state, it will then emit the `GAMEOBJECT_OVER` event.

The Game Object is not checked against the Pointer to see if it can enter this state,

that is up to you to do before calling this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The pointer to use when setting the state. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to have its state set. |

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_OVER](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_OVER](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L2126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2126)  
> Since: 3.85.0

---

## forceState

### <instance> forceState(pointer, gameObject, gameObjectEvent, inputPluginEvent, [setCursor])

**Description:**

This method will force the given Game Object into the given input state.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No |  | The pointer to use when setting the state. |
| --- | --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No |  | The Game Object to have its state set. |
| gameObjectEvent | string | No |  | The event to emit on the Game Object. |
| inputPluginEvent | string | No |  | The event to emit on the Input Plugin. |
| setCursor | boolean | Yes | false | Should the cursor be set to the Game Object's cursor? |

> Source: [src/input/InputPlugin.js#L2172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2172)  
> Since: 3.85.0

---

## forceUpState

### <instance> forceUpState(pointer, gameObject)

**Description:**

This method will force the given Game Object into the 'up' input state.

This will check to see if the Game Object is enabled for input, and if so,

it will emit the `GAMEOBJECT_POINTER_UP` event for it. If that doesn't change

the input state, it will then emit the `GAMEOBJECT_UP` event.

The Game Object is not checked against the Pointer to see if it can enter this state,

that is up to you to do before calling this method.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The pointer to use when setting the state. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to have its state set. |

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_UP](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_UP](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L2103](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2103)  
> Since: 3.85.0

---

## getDragState

### <instance> getDragState(pointer)

**Description:**

Returns the drag state of the given Pointer for this Input Plugin.

The state will be one of the following:

0 = Not dragging anything

1 = Primary button down and objects below, so collect a draglist

2 = Pointer being checked if meets drag criteria

3 = Pointer meets criteria, notify the draglist

4 = Pointer actively dragging the draglist and has moved

5 = Pointer actively dragging but has been released, notify draglist

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to get the drag state for. |
| --- | --- | --- | --- |

**Returns:** number - The drag state of the given Pointer.

> Source: [src/input/InputPlugin.js#L1085](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1085)  
> Since: 3.16.0

---

## hitTestPointer

### <instance> hitTestPointer(pointer)

**Description:**

Takes the given Pointer and performs a hit test against it, to see which interactive Game Objects

it is currently above.

The hit test is performed against which-ever Camera the Pointer is over. If it is over multiple

cameras, it starts checking the camera at the top of the camera list, and if nothing is found, iterates down the list.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to check against the Game Objects. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - An array of all the interactive Game Objects the Pointer was above.

> Source: [src/input/InputPlugin.js#L953](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L953)  
> Since: 3.0.0

---

## isActive

### <instance> isActive()

**Description:**

Checks to see if the Input Manager, this plugin and the Scene to which it belongs are all active and input enabled.

**Returns:** boolean - `true` if the plugin and the Scene it belongs to is active.

> Source: [src/input/InputPlugin.js#L528](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L528)  
> Since: 3.10.0

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

## makePixelPerfect

### <instance> makePixelPerfect([alphaTolerance])

**Description:**

Creates a function that can be passed to `setInteractive`, `enable` or `setHitArea` that will handle

pixel-perfect input detection on an Image or Sprite based Game Object, or any custom class that extends them.

The following will create a sprite that is clickable on any pixel that has an alpha value >= 1.

```
Copy
this.add.sprite(x, y, key).setInteractive(this.input.makePixelPerfect());


```

The following will create a sprite that is clickable on any pixel that has an alpha value >= 150.

```
Copy
this.add.sprite(x, y, key).setInteractive(this.input.makePixelPerfect(150));


```

Once you have made an Interactive Object pixel perfect it impacts all input related events for it: down, up,

dragstart, drag, etc.

As a pointer interacts with the Game Object it will constantly poll the texture, extracting a single pixel from

the given coordinates and checking its color values. This is an expensive process, so should only be enabled on

Game Objects that really need it.

You cannot make non-texture based Game Objects pixel perfect. So this will not work on Graphics, BitmapText,

Render Textures, Text, Tilemaps, Containers or Particles.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| alphaTolerance | number | Yes | 1 | The alpha level that the pixel should be above to be included as a successful interaction. |
| --- | --- | --- | --- | --- |

**Returns:** function - A Pixel Perfect Handler for use as a hitArea shape callback.

> Source: [src/input/InputPlugin.js#L2291](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2291)  
> Since: 3.10.0

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

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - `this`.

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

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - `this`.

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

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#once](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L124](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L124)  
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

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeAllListeners](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L165](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L165)  
> Since: 3.0.0

---

## removeDebug

### <instance> removeDebug(gameObject)

**Description:**

Removes an Input Debug Shape from the given Game Object.

The shape is destroyed immediately and the `hitAreaDebug` property is set to `null`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to remove the input debug shape from. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This Input Plugin.

> Source: [src/input/InputPlugin.js#L2748](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2748)  
> Since: 3.19.0

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

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - `this`.

**Inherits:** [Phaser.Events.EventEmitter#removeListener](events-eventemitter.md)

> Source: [src/events/EventEmitter.js#L137](https://github.com/phaserjs/phaser/blob/v3.87.0/src/events/EventEmitter.js#L137)  
> Since: 3.0.0

---

## resetCursor

### <instance> resetCursor()

**Description:**

Forces the Input Manager to clear the custom or hand cursor, regardless of the

interactive state of any Game Objects.

> Source: [src/input/InputPlugin.js#L562](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L562)  
> Since: 3.85.0

---

## resetPointers

### <instance> resetPointers()

**Description:**

Loops through all of the Input Manager Pointer instances and calls `reset` on them.

Use this function if you find that input has been stolen from Phaser via a 3rd

party component, such as Vue, and you need to tell Phaser to reset the Pointer states.

> Source: [src/input/InputPlugin.js#L3153](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3153)  
> Since: 3.60.0

---

## setCursor

### <instance> setCursor(interactiveObject)

**Description:**

Sets a custom cursor on the parent canvas element of the game, based on the `cursor`

setting of the given Interactive Object (i.e. a Sprite).

See the CSS property `cursor` for more information on MDN:

<https://developer.mozilla.org/en-US/docs/Web/CSS/cursor>

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| interactiveObject | [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md) | No | The Interactive Object that will set the cursor on the canvas. |
| --- | --- | --- | --- |

> Source: [src/input/InputPlugin.js#L541](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L541)  
> Since: 3.85.0

---

## setDefaultCursor

### <instance> setDefaultCursor(cursor)

**Description:**

Tells the Input system to set a custom cursor.

This cursor will be the default cursor used when interacting with the game canvas.

If an Interactive Object also sets a custom cursor, this is the cursor that is reset after its use.

Any valid CSS cursor value is allowed, including paths to image files, i.e.:

```
Copy
this.input.setDefaultCursor('url(assets/cursors/sword.cur), pointer');


```

Please read about the differences between browsers when it comes to the file formats and sizes they support:

<https://developer.mozilla.org/en-US/docs/Web/CSS/cursor>

<https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_User_Interface/Using_URL_values_for_the_cursor_property>

It's up to you to pick a suitable cursor format that works across the range of browsers you need to support.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| cursor | string | No | The CSS to be used when setting the default cursor. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This Input instance.

> Source: [src/input/InputPlugin.js#L3034](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3034)  
> Since: 3.10.0

---

## setDraggable

### <instance> setDraggable(gameObjects, [value])

**Description:**

Sets the draggable state of the given array of Game Objects.

They can either be set to be draggable, or can have their draggable state removed by passing `false`.

A Game Object will not fire drag events unless it has been specifically enabled for drag.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| gameObjects | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No |  | An array of Game Objects to change the draggable state on. |
| --- | --- | --- | --- | --- |
| value | boolean | Yes | true | Set to `true` if the Game Objects should be made draggable, `false` if they should be unset. |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2246](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2246)  
> Since: 3.0.0

---

## setDragState

### <instance> setDragState(pointer, state)

**Description:**

Sets the drag state of the given Pointer for this Input Plugin.

The state must be one of the following values:

0 = Not dragging anything

1 = Primary button down and objects below, so collect a draglist

2 = Pointer being checked if meets drag criteria

3 = Pointer meets criteria, notify the draglist

4 = Pointer actively dragging the draglist and has moved

5 = Pointer actively dragging but has been released, notify draglist

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to set the drag state for. |
| --- | --- | --- | --- |
| state | number | No | The drag state value. An integer between 0 and 5. |

> Source: [src/input/InputPlugin.js#L1109](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1109)  
> Since: 3.16.0

---

## setGlobalTopOnly

### <instance> setGlobalTopOnly(value)

**Description:**

When set to `true` the global Input Manager will emulate DOM behavior by only emitting events from

the top-most Scene in the Scene List. By default, if a Scene receives an input event it will then stop the event

from flowing down to any Scenes below it in the Scene list. To disable this behavior call this method with `false`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | Set to `true` to stop processing input events on the Scene that receives it, or `false` to let the event continue down the Scene list. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2832](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2832)  
> Since: 3.0.0

---

## setHitArea

### <instance> setHitArea(gameObjects, [hitArea], [hitAreaCallback])

**Description:**

Sets the hit area for the given array of Game Objects.

A hit area is typically one of the geometric shapes Phaser provides, such as a `Phaser.Geom.Rectangle`

or `Phaser.Geom.Circle`. However, it can be any object as long as it works with the provided callback.

If no hit area is provided a Rectangle is created based on the size of the Game Object, if possible

to calculate.

The hit area callback is the function that takes an `x` and `y` coordinate and returns a boolean if

those values fall within the area of the shape or not. All of the Phaser geometry objects provide this,

such as `Phaser.Geom.Rectangle.Contains`.

A hit area callback can be supplied to the `hitArea` parameter without using the `hitAreaCallback` parameter.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObjects | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of Game Objects to set the hit area on. |
| --- | --- | --- | --- |
| hitArea | [Phaser.Types.Input.InputConfiguration](../typedef/types-input.md) | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | any | Yes |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes | The 'contains' function to invoke to check if the pointer is within the hit area. |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2333](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2333)  
> Since: 3.0.0

---

## setHitAreaCircle

### <instance> setHitAreaCircle(gameObjects, x, y, radius, [callback])

**Description:**

Sets the hit area for an array of Game Objects to be a `Phaser.Geom.Circle` shape, using

the given coordinates and radius to control its position and size.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObjects | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of Game Objects to set as having a circle hit area. |
| --- | --- | --- | --- |
| x | number | No | The center of the circle. |
| y | number | No | The center of the circle. |
| radius | number | No | The radius of the circle. |
| callback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes | The hit area callback. If undefined it uses Circle.Contains. |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2449](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2449)  
> Since: 3.0.0

---

## setHitAreaEllipse

### <instance> setHitAreaEllipse(gameObjects, x, y, width, height, [callback])

**Description:**

Sets the hit area for an array of Game Objects to be a `Phaser.Geom.Ellipse` shape, using

the given coordinates and dimensions to control its position and size.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObjects | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of Game Objects to set as having an ellipse hit area. |
| --- | --- | --- | --- |
| x | number | No | The center of the ellipse. |
| y | number | No | The center of the ellipse. |
| width | number | No | The width of the ellipse. |
| height | number | No | The height of the ellipse. |
| callback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes | The hit area callback. If undefined it uses Ellipse.Contains. |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2473](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2473)  
> Since: 3.0.0

---

## setHitAreaFromTexture

### <instance> setHitAreaFromTexture(gameObjects, [callback])

**Description:**

Sets the hit area for an array of Game Objects to be a `Phaser.Geom.Rectangle` shape, using

the Game Objects texture frame to define the position and size of the hit area.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObjects | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of Game Objects to set as having an ellipse hit area. |
| --- | --- | --- | --- |
| callback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes | The hit area callback. If undefined it uses Rectangle.Contains. |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2498](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2498)  
> Since: 3.0.0

---

## setHitAreaRectangle

### <instance> setHitAreaRectangle(gameObjects, x, y, width, height, [callback])

**Description:**

Sets the hit area for an array of Game Objects to be a `Phaser.Geom.Rectangle` shape, using

the given coordinates and dimensions to control its position and size.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObjects | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of Game Objects to set as having a rectangular hit area. |
| --- | --- | --- | --- |
| x | number | No | The top-left of the rectangle. |
| y | number | No | The top-left of the rectangle. |
| width | number | No | The width of the rectangle. |
| height | number | No | The height of the rectangle. |
| callback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes | The hit area callback. If undefined it uses Rectangle.Contains. |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2556](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2556)  
> Since: 3.0.0

---

## setHitAreaTriangle

### <instance> setHitAreaTriangle(gameObjects, x1, y1, x2, y2, x3, y3, [callback])

**Description:**

Sets the hit area for an array of Game Objects to be a `Phaser.Geom.Triangle` shape, using

the given coordinates to control the position of its points.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObjects | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of Game Objects to set as having a triangular hit area. |
| --- | --- | --- | --- |
| x1 | number | No | The x coordinate of the first point of the triangle. |
| y1 | number | No | The y coordinate of the first point of the triangle. |
| x2 | number | No | The x coordinate of the second point of the triangle. |
| y2 | number | No | The y coordinate of the second point of the triangle. |
| x3 | number | No | The x coordinate of the third point of the triangle. |
| y3 | number | No | The y coordinate of the third point of the triangle. |
| callback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | Yes | The hit area callback. If undefined it uses Triangle.Contains. |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2581](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2581)  
> Since: 3.0.0

---

## setPollAlways

### <instance> setPollAlways()

**Description:**

Sets the Pointers to always poll.

When a pointer is polled it runs a hit test to see which Game Objects are currently below it,

or being interacted with it, regardless if the Pointer has actually moved or not.

You should enable this if you want objects in your game to fire over / out events, and the objects

are constantly moving, but the pointer may not have. Polling every frame has additional computation

costs, especially if there are a large number of interactive objects in your game.

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2777](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2777)  
> Since: 3.0.0

---

## setPollOnMove

### <instance> setPollOnMove()

**Description:**

Sets the Pointers to only poll when they are moved or updated.

When a pointer is polled it runs a hit test to see which Game Objects are currently below it,

or being interacted with it.

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2797](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2797)  
> Since: 3.0.0

---

## setPollRate

### <instance> setPollRate(value)

**Description:**

Sets the poll rate value. This is the amount of time that should have elapsed before a pointer

will be polled again. See the `setPollAlways` and `setPollOnMove` methods.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The amount of time, in ms, that should elapsed before re-polling the pointers. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2813](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2813)  
> Since: 3.0.0

---

## setTopOnly

### <instance> setTopOnly(value)

**Description:**

When set to `true` this Input Plugin will emulate DOM behavior by only emitting events from

the top-most Game Objects in the Display List.

If set to `false` it will emit events from all Game Objects below a Pointer, not just the top one.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | boolean | No | `true` to only include the top-most Game Object, or `false` to include all Game Objects in a hit test. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2851](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2851)  
> Since: 3.0.0

---

## sortDropZones

### <instance> sortDropZones(gameObjects)

**Description:**

Given an array of Drop Zone Game Objects, sort the array and return it,

so that the objects are in depth index order with the lowest at the bottom.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObjects | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of Game Objects to be sorted. |
| --- | --- | --- | --- |

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - The sorted array of Game Objects.

> Source: [src/input/InputPlugin.js#L2901](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2901)  
> Since: 3.52.0

---

## sortGameObjects

### <instance> sortGameObjects(gameObjects, pointer)

**Description:**

Given an array of Game Objects and a Pointer, sort the array and return it,

so that the objects are in render order with the lowest at the bottom.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObjects | Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> | No | An array of Game Objects to be sorted. |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to check against the Game Objects. |

**Returns:** Array.<[Phaser.GameObjects.GameObject](gameobjects-gameobject.md)> - The sorted array of Game Objects.

> Source: [src/input/InputPlugin.js#L2871](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2871)  
> Since: 3.0.0

---

## stopPropagation

### <instance> stopPropagation()

**Description:**

This method should be called from within an input event handler, such as `pointerdown`.

When called, it stops the Input Manager from allowing *this specific event* to be processed by any other Scene

not yet handled in the scene list.

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2993](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2993)  
> Since: 3.0.0

---

## updatePoll

### <instance> updatePoll(time, delta)

**Description:**

This is called automatically by the Input Manager.

It emits events for plugins to listen to and also handles polling updates, if enabled.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

**Returns:** boolean - `true` if the plugin and the Scene it belongs to is active.

> Source: [src/input/InputPlugin.js#L577](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L577)  
> Since: 3.18.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

This method is called automatically, only once, when the Scene is first created.

Do not invoke it directly.

**Access:** private

**Fires:** [Phaser.Input.Events#event:BOOT](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L393](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L393)  
> Since: 3.5.1

---

## destroy

### <instance> destroy()

**Description:**

The Scene that owns this plugin is being destroyed.

We need to shutdown and then kill off all external references.

**Access:** private

**Overrides:** Phaser.Events.EventEmitter#destroy

**Fires:** [Phaser.Input.Events#event:DESTROY](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L3172](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3172)  
> Since: 3.0.0

---

## onGameOut

### <instance> onGameOut()

**Description:**

Game Out handler.

**Access:** private

**Fires:** [Phaser.Input.Events#event:GAME\_OUT](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L462](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L462)  
> Since: 3.16.2

---

## onGameOver

### <instance> onGameOver()

**Description:**

Game Over handler.

**Access:** private

**Fires:** [Phaser.Input.Events#event:GAME\_OVER](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L446](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L446)  
> Since: 3.16.2

---

## preUpdate

### <instance> preUpdate()

**Description:**

The pre-update handler is responsible for checking the pending removal and insertion lists and

deleting old Game Objects.

**Access:** private

**Fires:** [Phaser.Input.Events#event:PRE\_UPDATE](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L478](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L478)  
> Since: 3.0.0

---

## processDownEvents

### <instance> processDownEvents(pointer)

**Description:**

An internal method that handles the Pointer down event.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer being tested. |
| --- | --- | --- | --- |

**Returns:** number - The total number of objects interacted with.

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_DOWN](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_DOWN](../event/input-events.md), [Phaser.Input.Events#event:POINTER\_DOWN](../event/input-events.md), [Phaser.Input.Events#event:POINTER\_DOWN\_OUTSIDE](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L1006](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1006)  
> Since: 3.0.0

---

## processDragDownEvent

### <instance> processDragDownEvent(pointer)

**Description:**

Processes a 'drag down' event for the given pointer. Checks the pointer state, builds-up the drag list

and prepares them all for interaction.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to process the drag event on. |
| --- | --- | --- | --- |

**Returns:** number - The number of items that were collected on the drag list.

> Source: [src/input/InputPlugin.js#L1225](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1225)  
> Since: 3.18.0

---

## processDragMoveEvent

### <instance> processDragMoveEvent(pointer)

**Description:**

Processes a 'drag move' event for the given pointer.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to process the drag event on. |
| --- | --- | --- | --- |

**Returns:** number - The number of items that were updated by this drag event.

**Fires:** [Phaser.Input.Events#event:DRAG\_ENTER](../event/input-events.md), [Phaser.Input.Events#event:DRAG](../event/input-events.md), [Phaser.Input.Events#event:DRAG\_LEAVE](../event/input-events.md), [Phaser.Input.Events#event:DRAG\_OVER](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_DRAG\_ENTER](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_DRAG](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_DRAG\_LEAVE](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_DRAG\_OVER](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L1298](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1298)  
> Since: 3.18.0

---

## processDragStartList

### <instance> processDragStartList(pointer)

**Description:**

Processes the drag list for the given pointer and dispatches the start events for each object on it.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to process the drag event on. |
| --- | --- | --- | --- |

**Returns:** number - The number of items that DRAG\_START was called on.

**Fires:** [Phaser.Input.Events#event:DRAG\_START](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_DRAG\_START](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L1168](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1168)  
> Since: 3.18.0

---

## processDragThresholdEvent

### <instance> processDragThresholdEvent(pointer, time)

**Description:**

Checks to see if a Pointer is ready to drag the objects below it, based on either a distance

or time threshold.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to check the drag thresholds on. |
| --- | --- | --- | --- |
| time | number | No | The current time. |

> Source: [src/input/InputPlugin.js#L1132](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1132)  
> Since: 3.18.0

---

## processDragUpEvent

### <instance> processDragUpEvent(pointer)

**Description:**

Processes a 'drag down' event for the given pointer. Checks the pointer state, builds-up the drag list

and prepares them all for interaction.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to process the drag event on. |
| --- | --- | --- | --- |

**Returns:** number - The number of items that were updated by this drag event.

**Fires:** [Phaser.Input.Events#event:DRAG\_END](../event/input-events.md), [Phaser.Input.Events#event:DROP](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_DRAG\_END](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_DROP](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L1448](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1448)  
> Since: 3.18.0

---

## processMoveEvents

### <instance> processMoveEvents(pointer)

**Description:**

An internal method that handles the Pointer movement event.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The pointer to check for events against. |
| --- | --- | --- | --- |

**Returns:** number - The total number of objects interacted with.

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_MOVE](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_MOVE](../event/input-events.md), [Phaser.Input.Events#event:POINTER\_MOVE](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L1522](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1522)  
> Since: 3.0.0

---

## processOutEvents

### <instance> processOutEvents(pointer)

**Description:**

An internal method that handles the Pointer out events.

This is called when a touch input leaves the canvas, as it can never be 'over' in this case.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The pointer to check for events against. |
| --- | --- | --- | --- |

**Returns:** number - The total number of objects interacted with.

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_OUT](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_OUT](../event/input-events.md), [Phaser.Input.Events#event:POINTER\_OUT](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L1743](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1743)  
> Since: 3.18.0

---

## processOverEvents

### <instance> processOverEvents(pointer)

**Description:**

An internal method that handles the Pointer over events.

This is called when a touch input hits the canvas, having previously been off of it.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The pointer to check for events against. |
| --- | --- | --- | --- |

**Returns:** number - The total number of objects interacted with.

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_OVER](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_OVER](../event/input-events.md), [Phaser.Input.Events#event:POINTER\_OVER](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L1661](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1661)  
> Since: 3.18.0

---

## processOverOutEvents

### <instance> processOverOutEvents(pointer)

**Description:**

An internal method that handles the Pointer over and out events.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The pointer to check for events against. |
| --- | --- | --- | --- |

**Returns:** number - The total number of objects interacted with.

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_OVER](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_OVER](../event/input-events.md), [Phaser.Input.Events#event:POINTER\_OVER](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_OUT](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_OUT](../event/input-events.md), [Phaser.Input.Events#event:POINTER\_OUT](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L1824](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1824)  
> Since: 3.0.0

---

## processUpEvents

### <instance> processUpEvents(pointer)

**Description:**

An internal method that handles the Pointer up events.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The pointer to check for events against. |
| --- | --- | --- | --- |

**Returns:** number - The total number of objects interacted with.

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_UP](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_UP](../event/input-events.md), [Phaser.Input.Events#event:POINTER\_UP](../event/input-events.md), [Phaser.Input.Events#event:POINTER\_UP\_OUTSIDE](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L2006](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2006)  
> Since: 3.0.0

---

## processWheelEvent

### <instance> processWheelEvent(pointer)

**Description:**

An internal method that handles a mouse wheel event.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The pointer to check for events against. |
| --- | --- | --- | --- |

**Returns:** number - The total number of objects interacted with.

**Fires:** [Phaser.Input.Events#event:GAMEOBJECT\_POINTER\_WHEEL](../event/input-events.md), [Phaser.Input.Events#event:GAMEOBJECT\_WHEEL](../event/input-events.md), [Phaser.Input.Events#event:POINTER\_WHEEL](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L1592](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L1592)  
> Since: 3.18.0

---

## queueForInsertion

### <instance> queueForInsertion(child)

**Description:**

Queues a Game Object for insertion into this Input Plugin on the next update.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to add. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2207](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2207)  
> Since: 3.0.0

---

## queueForRemoval

### <instance> queueForRemoval(child)

**Description:**

Queues a Game Object for removal from this Input Plugin on the next update.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| child | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to remove. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.InputPlugin](input-inputplugin.md) - This InputPlugin object.

> Source: [src/input/InputPlugin.js#L2228](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2228)  
> Since: 3.0.0

---

## shutdown

### <instance> shutdown()

**Description:**

The Scene that owns this plugin is shutting down.

We need to kill and reset all internal properties as well as stop listening to Scene events.

**Access:** private

**Overrides:** Phaser.Events.EventEmitter#shutdown

**Fires:** [Phaser.Input.Events#event:SHUTDOWN](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L3107](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3107)  
> Since: 3.0.0

---

## sortDropZoneHandler

### <instance> sortDropZoneHandler(childA, childB)

**Description:**

Return the child lowest down the display list (with the smallest index)

Will iterate through all parent containers, if present.

Prior to version 3.52.0 this method was called `sortHandlerGO`.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| childA | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The first Game Object to compare. |
| --- | --- | --- | --- |
| childB | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The second Game Object to compare. |

**Returns:** number - Returns either a negative or positive integer, or zero if they match.

> Source: [src/input/InputPlugin.js#L2924](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L2924)  
> Since: 3.52.0

---

## start

### <instance> start()

**Description:**

This method is called automatically by the Scene when it is starting up.

It is responsible for creating local systems, properties and listening for Scene events.

Do not invoke it directly.

**Access:** private

**Fires:** [Phaser.Input.Events#event:START](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L414](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L414)  
> Since: 3.5.0

---

## transitionComplete

### <instance> transitionComplete()

**Description:**

The Scene that owns this plugin has finished transitioning in.

**Access:** private

> Source: [src/input/InputPlugin.js#L3080](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3080)  
> Since: 3.5.0

---

## transitionIn

### <instance> transitionIn()

**Description:**

The Scene that owns this plugin is transitioning in.

**Access:** private

> Source: [src/input/InputPlugin.js#L3068](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3068)  
> Since: 3.5.0

---

## transitionOut

### <instance> transitionOut()

**Description:**

The Scene that owns this plugin is transitioning out.

**Access:** private

> Source: [src/input/InputPlugin.js#L3095](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L3095)  
> Since: 3.5.0

---

## update

### <instance> update(type, pointers)

**Description:**

This method is called when a DOM Event is received by the Input Manager. It handles dispatching the events

to relevant input enabled Game Objects in this scene.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| type | number | No | The type of event to process. |
| --- | --- | --- | --- |
| pointers | Array.<[Phaser.Input.Pointer](input-pointer.md)> | No | An array of Pointers on which the event occurred. |

**Returns:** boolean - `true` if this Scene has captured the input events from all other Scenes, otherwise `false`.

**Fires:** [Phaser.Input.Events#event:UPDATE](../event/input-events.md)

> Source: [src/input/InputPlugin.js#L695](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputPlugin.js#L695)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [activePointer](#activepointer)

    - [activePointer: Phaser.Input.Pointer](#activepointer-phaserinputpointer)
  + [cameras](#cameras)

    - [cameras: Phaser.Cameras.Scene2D.CameraManager](#cameras-phasercamerasscene2dcameramanager)
  + [displayList](#displaylist)

    - [displayList: Phaser.GameObjects.DisplayList](#displaylist-phasergameobjectsdisplaylist)
  + [dragDistanceThreshold](#dragdistancethreshold)

    - [dragDistanceThreshold: number](#dragdistancethreshold-number)
  + [dragTimeThreshold](#dragtimethreshold)

    - [dragTimeThreshold: number](#dragtimethreshold-number)
  + [enabled](#enabled)

    - [enabled: boolean](#enabled-boolean)
  + [gamepad](#gamepad)

    - [gamepad: Phaser.Input.Gamepad.GamepadPlugin](#gamepad-phaserinputgamepadgamepadplugin)
  + [isOver](#isover)

    - [isOver: boolean](#isover-boolean)
  + [keyboard](#keyboard)

    - [keyboard: Phaser.Input.Keyboard.KeyboardPlugin](#keyboard-phaserinputkeyboardkeyboardplugin)
  + [manager](#manager)

    - [manager: Phaser.Input.InputManager](#manager-phaserinputinputmanager)
  + [mouse](#mouse)

    - [mouse: Phaser.Input.Mouse.MouseManager](#mouse-phaserinputmousemousemanager)
  + [mousePointer](#mousepointer)

    - [mousePointer: Phaser.Input.Pointer](#mousepointer-phaserinputpointer)
  + [pointer1](#pointer1)

    - [pointer1: Phaser.Input.Pointer](#pointer1-phaserinputpointer)
  + [pointer10](#pointer10)

    - [pointer10: Phaser.Input.Pointer](#pointer10-phaserinputpointer)
  + [pointer2](#pointer2)

    - [pointer2: Phaser.Input.Pointer](#pointer2-phaserinputpointer)
  + [pointer3](#pointer3)

    - [pointer3: Phaser.Input.Pointer](#pointer3-phaserinputpointer)
  + [pointer4](#pointer4)

    - [pointer4: Phaser.Input.Pointer](#pointer4-phaserinputpointer)
  + [pointer5](#pointer5)

    - [pointer5: Phaser.Input.Pointer](#pointer5-phaserinputpointer)
  + [pointer6](#pointer6)

    - [pointer6: Phaser.Input.Pointer](#pointer6-phaserinputpointer)
  + [pointer7](#pointer7)

    - [pointer7: Phaser.Input.Pointer](#pointer7-phaserinputpointer)
  + [pointer8](#pointer8)

    - [pointer8: Phaser.Input.Pointer](#pointer8-phaserinputpointer)
  + [pointer9](#pointer9)

    - [pointer9: Phaser.Input.Pointer](#pointer9-phaserinputpointer)
  + [pollRate](#pollrate)

    - [pollRate: number](#pollrate-number)
  + [scene](#scene)

    - [scene: Phaser.Scene](#scene-phaserscene)
  + [settings](#settings)

    - [settings: Phaser.Types.Scenes.SettingsObject](#settings-phasertypesscenessettingsobject)
  + [systems](#systems)

    - [systems: Phaser.Scenes.Systems](#systems-phaserscenessystems)
  + [topOnly](#toponly)

    - [topOnly: boolean](#toponly-boolean)
  + [x](#x)

    - [x: number](#x-number)
  + [y](#y)

    - [y: number](#y-number)
* [Private Members](#private-members)

  + [\_drag](#_drag)

    - [\_drag: Object](#_drag-object)
  + [\_draggable](#_draggable)

    - [\_draggable: Array.<Phaser.GameObjects.GameObject>](#_draggable-arrayphasergameobjectsgameobject)
  + [\_dragState](#_dragstate)

    - [\_dragState: Array.<number>](#_dragstate-arraynumber)
  + [\_eventContainer](#_eventcontainer)

    - [\_eventContainer: Phaser.Types.Input.EventData](#_eventcontainer-phasertypesinputeventdata)
  + [\_eventData](#_eventdata)

    - [\_eventData: object](#_eventdata-object)
  + [\_list](#_list)

    - [\_list: Array.<Phaser.GameObjects.GameObject>](#_list-arrayphasergameobjectsgameobject)
  + [\_over](#_over)

    - [\_over: Object](#_over-object)
  + [\_pendingInsertion](#_pendinginsertion)

    - [\_pendingInsertion: Array.<Phaser.GameObjects.GameObject>](#_pendinginsertion-arrayphasergameobjectsgameobject)
  + [\_pendingRemoval](#_pendingremoval)

    - [\_pendingRemoval: Array.<Phaser.GameObjects.GameObject>](#_pendingremoval-arrayphasergameobjectsgameobject)
  + [\_pollTimer](#_polltimer)

    - [\_pollTimer: number](#_polltimer-number)
  + [\_temp](#_temp)

    - [\_temp: array](#_temp-array)
  + [\_tempZones](#_tempzones)

    - [\_tempZones: array](#_tempzones-array)
  + [\_updatedThisFrame](#_updatedthisframe)

    - [\_updatedThisFrame: boolean](#_updatedthisframe-boolean)
  + [\_validTypes](#_validtypes)

    - [\_validTypes: Array.<string>](#_validtypes-arraystring)
  + [pluginEvents](#pluginevents)

    - [pluginEvents: Phaser.Events.EventEmitter](#pluginevents-phasereventseventemitter)
* [Public Methods](#public-methods)

  + [addListener](#addlistener)

    - [<instance> addListener(event, fn, [context])](#instance-addlistenerevent-fn-context)
  + [addPointer](#addpointer)

    - [<instance> addPointer([quantity])](#instance-addpointerquantity)
  + [clear](#clear)

    - [<instance> clear(gameObject, [skipQueue])](#instance-cleargameobject-skipqueue)
  + [disable](#disable)

    - [<instance> disable(gameObject, [resetCursor])](#instance-disablegameobject-resetcursor)
  + [emit](#emit)

    - [<instance> emit(event, [args])](#instance-emitevent-args)
  + [enable](#enable)

    - [<instance> enable(gameObject, [hitArea], [hitAreaCallback], [dropZone])](#instance-enablegameobject-hitarea-hitareacallback-dropzone)
  + [enableDebug](#enabledebug)

    - [<instance> enableDebug(gameObject, [color])](#instance-enabledebuggameobject-color)
  + [eventNames](#eventnames)

    - [<instance> eventNames()](#instance-eventnames)
  + [forceDownState](#forcedownstate)

    - [<instance> forceDownState(pointer, gameObject)](#instance-forcedownstatepointer-gameobject)
  + [forceOutState](#forceoutstate)

    - [<instance> forceOutState(pointer, gameObject)](#instance-forceoutstatepointer-gameobject)
  + [forceOverState](#forceoverstate)

    - [<instance> forceOverState(pointer, gameObject)](#instance-forceoverstatepointer-gameobject)
  + [forceState](#forcestate)

    - [<instance> forceState(pointer, gameObject, gameObjectEvent, inputPluginEvent, [setCursor])](#instance-forcestatepointer-gameobject-gameobjectevent-inputpluginevent-setcursor)
  + [forceUpState](#forceupstate)

    - [<instance> forceUpState(pointer, gameObject)](#instance-forceupstatepointer-gameobject)
  + [getDragState](#getdragstate)

    - [<instance> getDragState(pointer)](#instance-getdragstatepointer)
  + [hitTestPointer](#hittestpointer)

    - [<instance> hitTestPointer(pointer)](#instance-hittestpointerpointer)
  + [isActive](#isactive)

    - [<instance> isActive()](#instance-isactive)
  + [listenerCount](#listenercount)

    - [<instance> listenerCount(event)](#instance-listenercountevent)
  + [listeners](#listeners)

    - [<instance> listeners(event)](#instance-listenersevent)
  + [makePixelPerfect](#makepixelperfect)

    - [<instance> makePixelPerfect([alphaTolerance])](#instance-makepixelperfectalphatolerance)
  + [off](#off)

    - [<instance> off(event, [fn], [context], [once])](#instance-offevent-fn-context-once)
  + [on](#on)

    - [<instance> on(event, fn, [context])](#instance-onevent-fn-context)
  + [once](#once)

    - [<instance> once(event, fn, [context])](#instance-onceevent-fn-context)
  + [removeAllListeners](#removealllisteners)

    - [<instance> removeAllListeners([event])](#instance-removealllistenersevent)
  + [removeDebug](#removedebug)

    - [<instance> removeDebug(gameObject)](#instance-removedebuggameobject)
  + [removeListener](#removelistener)

    - [<instance> removeListener(event, [fn], [context], [once])](#instance-removelistenerevent-fn-context-once)
  + [resetCursor](#resetcursor)

    - [<instance> resetCursor()](#instance-resetcursor)
  + [resetPointers](#resetpointers)

    - [<instance> resetPointers()](#instance-resetpointers)
  + [setCursor](#setcursor)

    - [<instance> setCursor(interactiveObject)](#instance-setcursorinteractiveobject)
  + [setDefaultCursor](#setdefaultcursor)

    - [<instance> setDefaultCursor(cursor)](#instance-setdefaultcursorcursor)
  + [setDraggable](#setdraggable)

    - [<instance> setDraggable(gameObjects, [value])](#instance-setdraggablegameobjects-value)
  + [setDragState](#setdragstate)

    - [<instance> setDragState(pointer, state)](#instance-setdragstatepointer-state)
  + [setGlobalTopOnly](#setglobaltoponly)

    - [<instance> setGlobalTopOnly(value)](#instance-setglobaltoponlyvalue)
  + [setHitArea](#sethitarea)

    - [<instance> setHitArea(gameObjects, [hitArea], [hitAreaCallback])](#instance-sethitareagameobjects-hitarea-hitareacallback)
  + [setHitAreaCircle](#sethitareacircle)

    - [<instance> setHitAreaCircle(gameObjects, x, y, radius, [callback])](#instance-sethitareacirclegameobjects-x-y-radius-callback)
  + [setHitAreaEllipse](#sethitareaellipse)

    - [<instance> setHitAreaEllipse(gameObjects, x, y, width, height, [callback])](#instance-sethitareaellipsegameobjects-x-y-width-height-callback)
  + [setHitAreaFromTexture](#sethitareafromtexture)

    - [<instance> setHitAreaFromTexture(gameObjects, [callback])](#instance-sethitareafromtexturegameobjects-callback)
  + [setHitAreaRectangle](#sethitarearectangle)

    - [<instance> setHitAreaRectangle(gameObjects, x, y, width, height, [callback])](#instance-sethitarearectanglegameobjects-x-y-width-height-callback)
  + [setHitAreaTriangle](#sethitareatriangle)

    - [<instance> setHitAreaTriangle(gameObjects, x1, y1, x2, y2, x3, y3, [callback])](#instance-sethitareatrianglegameobjects-x1-y1-x2-y2-x3-y3-callback)
  + [setPollAlways](#setpollalways)

    - [<instance> setPollAlways()](#instance-setpollalways)
  + [setPollOnMove](#setpollonmove)

    - [<instance> setPollOnMove()](#instance-setpollonmove)
  + [setPollRate](#setpollrate)

    - [<instance> setPollRate(value)](#instance-setpollratevalue)
  + [setTopOnly](#settoponly)

    - [<instance> setTopOnly(value)](#instance-settoponlyvalue)
  + [sortDropZones](#sortdropzones)

    - [<instance> sortDropZones(gameObjects)](#instance-sortdropzonesgameobjects)
  + [sortGameObjects](#sortgameobjects)

    - [<instance> sortGameObjects(gameObjects, pointer)](#instance-sortgameobjectsgameobjects-pointer)
  + [stopPropagation](#stoppropagation)

    - [<instance> stopPropagation()](#instance-stoppropagation)
  + [updatePoll](#updatepoll)

    - [<instance> updatePoll(time, delta)](#instance-updatepolltime-delta)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [onGameOut](#ongameout)

    - [<instance> onGameOut()](#instance-ongameout)
  + [onGameOver](#ongameover)

    - [<instance> onGameOver()](#instance-ongameover)
  + [preUpdate](#preupdate)

    - [<instance> preUpdate()](#instance-preupdate)
  + [processDownEvents](#processdownevents)

    - [<instance> processDownEvents(pointer)](#instance-processdowneventspointer)
  + [processDragDownEvent](#processdragdownevent)

    - [<instance> processDragDownEvent(pointer)](#instance-processdragdowneventpointer)
  + [processDragMoveEvent](#processdragmoveevent)

    - [<instance> processDragMoveEvent(pointer)](#instance-processdragmoveeventpointer)
  + [processDragStartList](#processdragstartlist)

    - [<instance> processDragStartList(pointer)](#instance-processdragstartlistpointer)
  + [processDragThresholdEvent](#processdragthresholdevent)

    - [<instance> processDragThresholdEvent(pointer, time)](#instance-processdragthresholdeventpointer-time)
  + [processDragUpEvent](#processdragupevent)

    - [<instance> processDragUpEvent(pointer)](#instance-processdragupeventpointer)
  + [processMoveEvents](#processmoveevents)

    - [<instance> processMoveEvents(pointer)](#instance-processmoveeventspointer)
  + [processOutEvents](#processoutevents)

    - [<instance> processOutEvents(pointer)](#instance-processouteventspointer)
  + [processOverEvents](#processoverevents)

    - [<instance> processOverEvents(pointer)](#instance-processovereventspointer)
  + [processOverOutEvents](#processoveroutevents)

    - [<instance> processOverOutEvents(pointer)](#instance-processoverouteventspointer)
  + [processUpEvents](#processupevents)

    - [<instance> processUpEvents(pointer)](#instance-processupeventspointer)
  + [processWheelEvent](#processwheelevent)

    - [<instance> processWheelEvent(pointer)](#instance-processwheeleventpointer)
  + [queueForInsertion](#queueforinsertion)

    - [<instance> queueForInsertion(child)](#instance-queueforinsertionchild)
  + [queueForRemoval](#queueforremoval)

    - [<instance> queueForRemoval(child)](#instance-queueforremovalchild)
  + [shutdown](#shutdown)

    - [<instance> shutdown()](#instance-shutdown)
  + [sortDropZoneHandler](#sortdropzonehandler)

    - [<instance> sortDropZoneHandler(childA, childB)](#instance-sortdropzonehandlerchilda-childb)
  + [start](#start)

    - [<instance> start()](#instance-start)
  + [transitionComplete](#transitioncomplete)

    - [<instance> transitionComplete()](#instance-transitioncomplete)
  + [transitionIn](#transitionin)

    - [<instance> transitionIn()](#instance-transitionin)
  + [transitionOut](#transitionout)

    - [<instance> transitionOut()](#instance-transitionout)
  + [update](#update)

    - [<instance> update(type, pointers)](#instance-updatetype-pointers)

Back to top

©2025[Phaser](https://docs.phaser.io)