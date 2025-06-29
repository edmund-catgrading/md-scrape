# InputManager

Phaser.Input.InputManager

The Input Manager is responsible for handling the pointer related systems in a single Phaser Game instance.

Based on the Game Config it will create handlers for mouse and touch support.

Keyboard and Gamepad are plugins, handled directly by the InputPlugin class.

It then manages the events, pointer creation and general hit test related operations.

You rarely need to interact with the Input Manager directly, and as such, all of its properties and methods

should be considered private. Instead, you should use the Input Plugin, which is a Scene level system, responsible

for dealing with all input events for a Scene.

**Constructor**

`new InputManager(game, config)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| game | [Phaser.Game](game.md) | No | The Game instance that owns the Input Manager. |
| --- | --- | --- | --- |
| config | object | No | The Input Configuration object, as set in the Game Config. |

---

**Scope**: static

> Source: [src/input/InputManager.js#L19](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L19)  
> Since: 3.0.0

# Public Members

## activePointer

### activePointer: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

The most recently active Pointer object.

If you've only 1 Pointer in your game then this will accurately be either the first finger touched, or the mouse.

If your game doesn't need to support multi-touch then you can safely use this property in all of your game

code and it will adapt to be either the mouse or the touch, based on device.

> Source: [src/input/InputManager.js#L200](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L200)  
> Since: 3.0.0

---

## canvas

### canvas: HTMLCanvasElement

**Description:**

The Canvas that is used for all DOM event input listeners.

> Source: [src/input/InputManager.js#L68](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L68)  
> Since: 3.0.0

---

## config

### config: [Phaser.Core.Config](core-config.md)

**Description:**

The Game Configuration object, as set during the game boot.

> Source: [src/input/InputManager.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L77)  
> Since: 3.0.0

---

## defaultCursor

### defaultCursor: string

**Description:**

The default CSS cursor to be used when interacting with your game.

See the `setDefaultCursor` method for more details.

> Source: [src/input/InputManager.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L116)  
> Since: 3.10.0

---

## enabled

### enabled: boolean

**Description:**

If set, the Input Manager will run its update loop every frame.

> Source: [src/input/InputManager.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L86)  
> Since: 3.0.0

---

## events

### events: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

The Event Emitter instance that the Input Manager uses to emit events from.

> Source: [src/input/InputManager.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L96)  
> Since: 3.0.0

---

## game

### game: [Phaser.Game](game.md)

**Description:**

The Game instance that owns the Input Manager.

A Game only maintains on instance of the Input Manager at any time.

> Source: [src/input/InputManager.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L47)  
> Since: 3.0.0

---

## globalTopOnly

### globalTopOnly: boolean

**Description:**

If the top-most Scene in the Scene List receives an input it will stop input from

propagating any lower down the scene list, i.e. if you have a UI Scene at the top

and click something on it, that click will not then be passed down to any other

Scene below. Disable this to have input events passed through all Scenes, all the time.

> Source: [src/input/InputManager.js#L214](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L214)  
> Since: 3.0.0

---

## isOver

### isOver: boolean

**Description:**

Are any mouse or touch pointers currently over the game canvas?

This is updated automatically by the canvas over and out handlers.

> Source: [src/input/InputManager.js#L105](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L105)  
> Since: 3.16.0

---

## keyboard

### keyboard: [Phaser.Input.Keyboard.KeyboardManager](input-keyboard-keyboardmanager.md)

**Description:**

A reference to the Keyboard Manager class, if enabled via the `input.keyboard` Game Config property.

> Source: [src/input/InputManager.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L127)  
> Since: 3.16.0

---

## mouse

### mouse: [Phaser.Input.Mouse.MouseManager](input-mouse-mousemanager.md)

**Description:**

A reference to the Mouse Manager class, if enabled via the `input.mouse` Game Config property.

> Source: [src/input/InputManager.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L136)  
> Since: 3.0.0

---

## mousePointer

### mousePointer: [Phaser.Input.Pointer](input-pointer.md)

**Description:**

The mouse has its own unique Pointer object, which you can reference directly if making a *desktop specific game*.

If you are supporting both desktop and touch devices then do not use this property, instead use `activePointer`

which will always map to the most recently interacted pointer.

> Source: [src/input/InputManager.js#L189](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L189)  
> Since: 3.10.0

---

## pointers

### pointers: Array.<[Phaser.Input.Pointer](input-pointer.md)>

**Description:**

An array of Pointers that have been added to the game.

The first entry is reserved for the Mouse Pointer, the rest are Touch Pointers.

By default there is 1 touch pointer enabled. If you need more use the `addPointer` method to start them,

or set the `input.activePointers` property in the Game Config.

> Source: [src/input/InputManager.js#L154](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L154)  
> Since: 3.10.0

---

## pointersTotal

### pointersTotal: number

**Description:**

The number of touch objects activated and being processed each update.

You can change this by either calling `addPointer` at run-time, or by

setting the `input.activePointers` property in the Game Config.

> Source: [src/input/InputManager.js#L167](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L167)  
> Since: 3.10.0

---

## scaleManager

### scaleManager: [Phaser.Scale.ScaleManager](scale-scalemanager.md)

**Description:**

A reference to the global Game Scale Manager.

Used for all bounds checks and pointer scaling.

> Source: [src/input/InputManager.js#L58](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L58)  
> Since: 3.16.0

---

## time

### time: number

**Description:**

The time this Input Manager was last updated.

This value is populated by the Game Step each frame.

> Source: [src/input/InputManager.js#L227](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L227)  
> Since: 3.16.2

---

## touch

### touch: [Phaser.Input.Touch.TouchManager](input-touch-touchmanager.md)

**Description:**

A reference to the Touch Manager class, if enabled via the `input.touch` Game Config property.

> Source: [src/input/InputManager.js#L145](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L145)  
> Since: 3.0.0

---

# Private Members

## \_tempHitTest

### \_tempHitTest: array

**Description:**

A re-cycled array to store hit results in.

**Access:** private

> Source: [src/input/InputManager.js#L248](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L248)  
> Since: 3.0.0

---

## \_tempMatrix

### \_tempMatrix: [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md)

**Description:**

A re-cycled matrix used in hit test calculations.

**Access:** private

> Source: [src/input/InputManager.js#L259](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L259)  
> Since: 3.4.0

---

## \_tempMatrix2

### \_tempMatrix2: [Phaser.GameObjects.Components.TransformMatrix](gameobjects-components-transformmatrix.md)

**Description:**

A re-cycled matrix used in hit test calculations.

**Access:** private

> Source: [src/input/InputManager.js#L269](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L269)  
> Since: 3.12.0

---

## \_tempPoint

### \_tempPoint: Object

**Description:**

A re-cycled point-like object to store hit test values in.

**Access:** private

> Source: [src/input/InputManager.js#L238](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L238)  
> Since: 3.0.0

---

## \_tempSkip

### \_tempSkip: boolean

**Description:**

An internal private var that records Scenes aborting event processing.

**Access:** private

> Source: [src/input/InputManager.js#L279](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L279)  
> Since: 3.18.0

---

## mousePointerContainer

### mousePointerContainer: Array.<[Phaser.Input.Pointer](input-pointer.md)>

**Description:**

An internal private array that avoids needing to create a new array on every DOM mouse event.

**Access:** private

> Source: [src/input/InputManager.js#L289](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L289)  
> Since: 3.18.0

---

# Public Methods

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

> Source: [src/input/InputManager.js#L466](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L466)  
> Since: 3.10.0

---

## boot

### <instance> boot()

**Description:**

The Boot handler is called by Phaser.Game when it first starts up.

The renderer is available by now.

**Access:** protected

**Fires:** [Phaser.Input.Events#event:MANAGER\_BOOT](../event/input-events.md)

> Source: [src/input/InputManager.js#L302](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L302)  
> Since: 3.0.0

---

## destroy

### <instance> destroy()

**Description:**

Destroys the Input Manager and all of its systems.

There is no way to recover from doing this.

> Source: [src/input/InputManager.js#L1057](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L1057)  
> Since: 3.0.0

---

## hitTest

### <instance> hitTest(pointer, gameObjects, camera, [output])

**Description:**

Performs a hit test using the given Pointer and camera, against an array of interactive Game Objects.

The Game Objects are culled against the camera, and then the coordinates are translated into the local camera space

and used to determine if they fall within the remaining Game Objects hit areas or not.

If nothing is matched an empty array is returned.

This method is called automatically by InputPlugin.hitTestPointer and doesn't usually need to be invoked directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to test against. |
| --- | --- | --- | --- |
| gameObjects | array | No | An array of interactive Game Objects to check. |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera which is being tested against. |
| output | array | Yes | An array to store the results in. If not given, a new empty array is created. |

**Returns:** array - An array of the Game Objects that were hit during this hit test.

> Source: [src/input/InputManager.js#L868](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L868)  
> Since: 3.0.0

---

## pointWithinHitArea

### <instance> pointWithinHitArea(gameObject, x, y)

**Description:**

Checks if the given x and y coordinate are within the hit area of the Game Object.

This method assumes that the coordinate values have already been translated into the space of the Game Object.

If the coordinates are within the hit area they are set into the Game Objects Input `localX` and `localY` properties.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The interactive Game Object to check against. |
| --- | --- | --- | --- |
| x | number | No | The translated x coordinate for the hit test. |
| y | number | No | The translated y coordinate for the hit test. |

**Returns:** boolean - `true` if the coordinates were inside the Game Objects hit area, otherwise `false`.

> Source: [src/input/InputManager.js#L947](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L947)  
> Since: 3.0.0

---

## pointWithinInteractiveObject

### <instance> pointWithinInteractiveObject(object, x, y)

**Description:**

Checks if the given x and y coordinate are within the hit area of the Interactive Object.

This method assumes that the coordinate values have already been translated into the space of the Interactive Object.

If the coordinates are within the hit area they are set into the Interactive Objects Input `localX` and `localY` properties.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| object | [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md) | No | The Interactive Object to check against. |
| --- | --- | --- | --- |
| x | number | No | The translated x coordinate for the hit test. |
| y | number | No | The translated y coordinate for the hit test. |

**Returns:** boolean - `true` if the coordinates were inside the Game Objects hit area, otherwise `false`.

> Source: [src/input/InputManager.js#L984](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L984)  
> Since: 3.0.0

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

> Source: [src/input/InputManager.js#L390](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L390)  
> Since: 3.10.0

---

## transformPointer

### <instance> transformPointer(pointer, pageX, pageY, wasMove)

**Description:**

Transforms the pageX and pageY values of a Pointer into the scaled coordinate space of the Input Manager.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](input-pointer.md) | No | The Pointer to transform the values for. |
| --- | --- | --- | --- |
| pageX | number | No | The Page X value. |
| pageY | number | No | The Page Y value. |
| wasMove | boolean | No | Are we transforming the Pointer from a move event, or an up / down event? |

> Source: [src/input/InputManager.js#L1017](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L1017)  
> Since: 3.10.0

---

## updateInputPlugins

### <instance> updateInputPlugins(type, pointers)

**Description:**

Internal method that gets a list of all the active Input Plugins in the game

and updates each of them in turn, in reverse order (top to bottom), to allow

for DOM top-level event handling simulation.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| type | number | No | The type of event to process. |
| --- | --- | --- | --- |
| pointers | Array.<[Phaser.Input.Pointer](input-pointer.md)> | No | An array of Pointers on which the event occurred. |

> Source: [src/input/InputManager.js#L513](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L513)  
> Since: 3.16.0

---

# Private Methods

## inputCandidate

### <instance> inputCandidate(gameObject, camera)

**Description:**

Checks if the given Game Object should be considered as a candidate for input or not.

Checks if the Game Object has an input component that is enabled, that it will render,

and finally, if it has a parent, that the parent parent, or any ancestor, is visible or not.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](gameobjects-gameobject.md) | No | The Game Object to test. |
| --- | --- | --- | --- |
| camera | [Phaser.Cameras.Scene2D.Camera](cameras-scene2d-camera.md) | No | The Camera which is being tested against. |

**Returns:** boolean - `true` if the Game Object should be considered for input, otherwise `false`.

> Source: [src/input/InputManager.js#L823](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L823)  
> Since: 3.10.0

---

## onMouseDown

### <instance> onMouseDown(event)

**Description:**

Processes a mouse down event, as passed in by the MouseManager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | MouseEvent | No | The native DOM Mouse event. |
| --- | --- | --- | --- |

> Source: [src/input/InputManager.js#L718](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L718)  
> Since: 3.18.0

---

## onMouseMove

### <instance> onMouseMove(event)

**Description:**

Processes a mouse move event, as passed in by the MouseManager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | MouseEvent | No | The native DOM Mouse event. |
| --- | --- | --- | --- |

> Source: [src/input/InputManager.js#L740](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L740)  
> Since: 3.18.0

---

## onMouseUp

### <instance> onMouseUp(event)

**Description:**

Processes a mouse up event, as passed in by the MouseManager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | MouseEvent | No | The native DOM Mouse event. |
| --- | --- | --- | --- |

> Source: [src/input/InputManager.js#L762](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L762)  
> Since: 3.18.0

---

## onMouseWheel

### <instance> onMouseWheel(event)

**Description:**

Processes a mouse wheel event, as passed in by the MouseManager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | WheelEvent | No | The native DOM Wheel event. |
| --- | --- | --- | --- |

> Source: [src/input/InputManager.js#L784](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L784)  
> Since: 3.18.0

---

## onPointerLockChange

### <instance> onPointerLockChange(event)

**Description:**

Processes a pointer lock change event, as passed in by the MouseManager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | MouseEvent | No | The native DOM Mouse event. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Input.Events#event:POINTERLOCK\_CHANGE](../event/input-events.md)

> Source: [src/input/InputManager.js#L804](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L804)  
> Since: 3.19.0

---

## onTouchCancel

### <instance> onTouchCancel(event)

**Description:**

Processes a touch cancel event, as passed in by the TouchManager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | TouchEvent | No | The native DOM Touch event. |
| --- | --- | --- | --- |

> Source: [src/input/InputManager.js#L682](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L682)  
> Since: 3.18.0

---

## onTouchEnd

### <instance> onTouchEnd(event)

**Description:**

Processes a touch end event, as passed in by the TouchManager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | TouchEvent | No | The native DOM Touch event. |
| --- | --- | --- | --- |

> Source: [src/input/InputManager.js#L646](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L646)  
> Since: 3.18.0

---

## onTouchMove

### <instance> onTouchMove(event)

**Description:**

Processes a touch move event, as passed in by the TouchManager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | TouchEvent | No | The native DOM Touch event. |
| --- | --- | --- | --- |

> Source: [src/input/InputManager.js#L589](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L589)  
> Since: 3.18.0

---

## onTouchStart

### <instance> onTouchStart(event)

**Description:**

Processes a touch start event, as passed in by the TouchManager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | TouchEvent | No | The native DOM Touch event. |
| --- | --- | --- | --- |

> Source: [src/input/InputManager.js#L551](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L551)  
> Since: 3.18.0

---

## preRender

### <instance> preRender()

**Description:**

Internal update, called automatically by the Game Step right at the start.

**Access:** private

> Source: [src/input/InputManager.js#L361](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L361)  
> Since: 3.18.0

---

## resetCursor

### <instance> resetCursor(interactiveObject, [forceReset])

**Description:**

Called by the InputPlugin when processing over and out events.

Tells the Input Manager to clear the hand cursor, if set, during its postUpdate step.

**Access:** private

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| interactiveObject | [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md) | No |  | The Interactive Object that called this method. Pass `null` if you just want to set the force value. |
| --- | --- | --- | --- | --- |
| forceReset | boolean | Yes | false | Should the reset happen regardless of the object's cursor state? Default false. |

> Source: [src/input/InputManager.js#L446](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L446)  
> Since: 3.10.0

---

## setCanvasOut

### <instance> setCanvasOut(event)

**Description:**

Internal canvas state change, called automatically by the Mouse Manager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | MouseEvent | TouchEvent | No | The DOM Event. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Input.Events#event:GAME\_OUT](../event/input-events.md)

> Source: [src/input/InputManager.js#L344](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L344)  
> Since: 3.16.0

---

## setCanvasOver

### <instance> setCanvasOver(event)

**Description:**

Internal canvas state change, called automatically by the Mouse Manager.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | MouseEvent | TouchEvent | No | The DOM Event. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Input.Events#event:GAME\_OVER](../event/input-events.md)

> Source: [src/input/InputManager.js#L327](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L327)  
> Since: 3.16.0

---

## setCursor

### <instance> setCursor(interactiveObject)

**Description:**

Called by the InputPlugin when processing over and out events.

Tells the Input Manager to set a custom cursor during its postUpdate step.

<https://developer.mozilla.org/en-US/docs/Web/CSS/cursor>

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| interactiveObject | [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md) | No | The Interactive Object that called this method. |
| --- | --- | --- | --- |

> Source: [src/input/InputManager.js#L425](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/InputManager.js#L425)  
> Since: 3.10.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [activePointer](#activepointer)

    - [activePointer: Phaser.Input.Pointer](#activepointer-phaserinputpointer)
  + [canvas](#canvas)

    - [canvas: HTMLCanvasElement](#canvas-htmlcanvaselement)
  + [config](#config)

    - [config: Phaser.Core.Config](#config-phasercoreconfig)
  + [defaultCursor](#defaultcursor)

    - [defaultCursor: string](#defaultcursor-string)
  + [enabled](#enabled)

    - [enabled: boolean](#enabled-boolean)
  + [events](#events)

    - [events: Phaser.Events.EventEmitter](#events-phasereventseventemitter)
  + [game](#game)

    - [game: Phaser.Game](#game-phasergame)
  + [globalTopOnly](#globaltoponly)

    - [globalTopOnly: boolean](#globaltoponly-boolean)
  + [isOver](#isover)

    - [isOver: boolean](#isover-boolean)
  + [keyboard](#keyboard)

    - [keyboard: Phaser.Input.Keyboard.KeyboardManager](#keyboard-phaserinputkeyboardkeyboardmanager)
  + [mouse](#mouse)

    - [mouse: Phaser.Input.Mouse.MouseManager](#mouse-phaserinputmousemousemanager)
  + [mousePointer](#mousepointer)

    - [mousePointer: Phaser.Input.Pointer](#mousepointer-phaserinputpointer)
  + [pointers](#pointers)

    - [pointers: Array.<Phaser.Input.Pointer>](#pointers-arrayphaserinputpointer)
  + [pointersTotal](#pointerstotal)

    - [pointersTotal: number](#pointerstotal-number)
  + [scaleManager](#scalemanager)

    - [scaleManager: Phaser.Scale.ScaleManager](#scalemanager-phaserscalescalemanager)
  + [time](#time)

    - [time: number](#time-number)
  + [touch](#touch)

    - [touch: Phaser.Input.Touch.TouchManager](#touch-phaserinputtouchtouchmanager)
* [Private Members](#private-members)

  + [\_tempHitTest](#_temphittest)

    - [\_tempHitTest: array](#_temphittest-array)
  + [\_tempMatrix](#_tempmatrix)

    - [\_tempMatrix: Phaser.GameObjects.Components.TransformMatrix](#_tempmatrix-phasergameobjectscomponentstransformmatrix)
  + [\_tempMatrix2](#_tempmatrix2)

    - [\_tempMatrix2: Phaser.GameObjects.Components.TransformMatrix](#_tempmatrix2-phasergameobjectscomponentstransformmatrix)
  + [\_tempPoint](#_temppoint)

    - [\_tempPoint: Object](#_temppoint-object)
  + [\_tempSkip](#_tempskip)

    - [\_tempSkip: boolean](#_tempskip-boolean)
  + [mousePointerContainer](#mousepointercontainer)

    - [mousePointerContainer: Array.<Phaser.Input.Pointer>](#mousepointercontainer-arrayphaserinputpointer)
* [Public Methods](#public-methods)

  + [addPointer](#addpointer)

    - [<instance> addPointer([quantity])](#instance-addpointerquantity)
  + [boot](#boot)

    - [<instance> boot()](#instance-boot)
  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [hitTest](#hittest)

    - [<instance> hitTest(pointer, gameObjects, camera, [output])](#instance-hittestpointer-gameobjects-camera-output)
  + [pointWithinHitArea](#pointwithinhitarea)

    - [<instance> pointWithinHitArea(gameObject, x, y)](#instance-pointwithinhitareagameobject-x-y)
  + [pointWithinInteractiveObject](#pointwithininteractiveobject)

    - [<instance> pointWithinInteractiveObject(object, x, y)](#instance-pointwithininteractiveobjectobject-x-y)
  + [setDefaultCursor](#setdefaultcursor)

    - [<instance> setDefaultCursor(cursor)](#instance-setdefaultcursorcursor)
  + [transformPointer](#transformpointer)

    - [<instance> transformPointer(pointer, pageX, pageY, wasMove)](#instance-transformpointerpointer-pagex-pagey-wasmove)
  + [updateInputPlugins](#updateinputplugins)

    - [<instance> updateInputPlugins(type, pointers)](#instance-updateinputpluginstype-pointers)
* [Private Methods](#private-methods)

  + [inputCandidate](#inputcandidate)

    - [<instance> inputCandidate(gameObject, camera)](#instance-inputcandidategameobject-camera)
  + [onMouseDown](#onmousedown)

    - [<instance> onMouseDown(event)](#instance-onmousedownevent)
  + [onMouseMove](#onmousemove)

    - [<instance> onMouseMove(event)](#instance-onmousemoveevent)
  + [onMouseUp](#onmouseup)

    - [<instance> onMouseUp(event)](#instance-onmouseupevent)
  + [onMouseWheel](#onmousewheel)

    - [<instance> onMouseWheel(event)](#instance-onmousewheelevent)
  + [onPointerLockChange](#onpointerlockchange)

    - [<instance> onPointerLockChange(event)](#instance-onpointerlockchangeevent)
  + [onTouchCancel](#ontouchcancel)

    - [<instance> onTouchCancel(event)](#instance-ontouchcancelevent)
  + [onTouchEnd](#ontouchend)

    - [<instance> onTouchEnd(event)](#instance-ontouchendevent)
  + [onTouchMove](#ontouchmove)

    - [<instance> onTouchMove(event)](#instance-ontouchmoveevent)
  + [onTouchStart](#ontouchstart)

    - [<instance> onTouchStart(event)](#instance-ontouchstartevent)
  + [preRender](#prerender)

    - [<instance> preRender()](#instance-prerender)
  + [resetCursor](#resetcursor)

    - [<instance> resetCursor(interactiveObject, [forceReset])](#instance-resetcursorinteractiveobject-forcereset)
  + [setCanvasOut](#setcanvasout)

    - [<instance> setCanvasOut(event)](#instance-setcanvasoutevent)
  + [setCanvasOver](#setcanvasover)

    - [<instance> setCanvasOver(event)](#instance-setcanvasoverevent)
  + [setCursor](#setcursor)

    - [<instance> setCursor(interactiveObject)](#instance-setcursorinteractiveobject)

Back to top

©2025[Phaser](https://docs.phaser.io)