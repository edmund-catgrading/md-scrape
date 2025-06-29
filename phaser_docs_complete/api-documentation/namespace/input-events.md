# Phaser.Input.Events

Scope:
static

> Source: [src/input/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/index.js#L7)

# Static functions

## BOOT

### BOOT

**Description:**

The Input Plugin Boot Event.

This internal event is dispatched by the Input Plugin when it boots, signalling to all of its systems to create themselves.

> Source: [src/input/events/BOOT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/BOOT_EVENT.js#L7)  
> Since: 3.0.0

---

## DESTROY

### DESTROY

**Description:**

The Input Plugin Destroy Event.

This internal event is dispatched by the Input Plugin when it is destroyed, signalling to all of its systems to destroy themselves.

> Source: [src/input/events/DESTROY\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/DESTROY_EVENT.js#L7)  
> Since: 3.0.0

---

## DRAG

### DRAG

**Description:**

The Pointer Drag Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer moves while dragging a Game Object.

Listen to this event from within a Scene using: `this.input.on('drag', listener)`.

A Pointer can only drag a single Game Object at once.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_DRAG`](Phaser.Input.Events.md) event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The interactive Game Object that this pointer is dragging. |
| dragX | number | No | The x coordinate where the Pointer is currently dragging the Game Object, in world space. |
| dragY | number | No | The y coordinate where the Pointer is currently dragging the Game Object, in world space. |

> Source: [src/input/events/DRAG\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/DRAG_EVENT.js#L7)  
> Since: 3.0.0

---

## DRAG\_END

### DRAG\_END

**Description:**

The Pointer Drag End Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer stops dragging a Game Object.

Listen to this event from within a Scene using: `this.input.on('dragend', listener)`.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_DRAG_END`](Phaser.Input.Events.md) event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The interactive Game Object that this pointer stopped dragging. |
| dropped | boolean | No | Whether the Game Object was dropped onto a target. |

> Source: [src/input/events/DRAG\_END\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/DRAG_END_EVENT.js#L7)  
> Since: 3.0.0

---

## DRAG\_ENTER

### DRAG\_ENTER

**Description:**

The Pointer Drag Enter Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer drags a Game Object into a Drag Target.

Listen to this event from within a Scene using: `this.input.on('dragenter', listener)`.

A Pointer can only drag a single Game Object at once.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_DRAG_ENTER`](Phaser.Input.Events.md) event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The interactive Game Object that this pointer is dragging. |
| target | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The drag target that this pointer has moved into. |

> Source: [src/input/events/DRAG\_ENTER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/DRAG_ENTER_EVENT.js#L7)  
> Since: 3.0.0

---

## DRAG\_LEAVE

### DRAG\_LEAVE

**Description:**

The Pointer Drag Leave Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer drags a Game Object out of a Drag Target.

Listen to this event from within a Scene using: `this.input.on('dragleave', listener)`.

A Pointer can only drag a single Game Object at once.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_DRAG_LEAVE`](Phaser.Input.Events.md) event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The interactive Game Object that this pointer is dragging. |
| target | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The drag target that this pointer has left. |

> Source: [src/input/events/DRAG\_LEAVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/DRAG_LEAVE_EVENT.js#L7)  
> Since: 3.0.0

---

## DRAG\_OVER

### DRAG\_OVER

**Description:**

The Pointer Drag Over Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer drags a Game Object over a Drag Target.

When the Game Object first enters the drag target it will emit a `dragenter` event. If it then moves while within

the drag target, it will emit this event instead.

Listen to this event from within a Scene using: `this.input.on('dragover', listener)`.

A Pointer can only drag a single Game Object at once.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_DRAG_OVER`](Phaser.Input.Events.md) event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The interactive Game Object that this pointer is dragging. |
| target | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The drag target that this pointer has moved over. |

> Source: [src/input/events/DRAG\_OVER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/DRAG_OVER_EVENT.js#L7)  
> Since: 3.0.0

---

## DRAG\_START

### DRAG\_START

**Description:**

The Pointer Drag Start Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer starts to drag any Game Object.

Listen to this event from within a Scene using: `this.input.on('dragstart', listener)`.

A Pointer can only drag a single Game Object at once.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_DRAG_START`](Phaser.Input.Events.md) event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The interactive Game Object that this pointer is dragging. |

> Source: [src/input/events/DRAG\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/DRAG_START_EVENT.js#L7)  
> Since: 3.0.0

---

## DROP

### DROP

**Description:**

The Pointer Drop Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer drops a Game Object on a Drag Target.

Listen to this event from within a Scene using: `this.input.on('drop', listener)`.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_DROP`](Phaser.Input.Events.md) event instead.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The interactive Game Object that this pointer was dragging. |
| target | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Drag Target the `gameObject` has been dropped on. |

> Source: [src/input/events/DROP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/DROP_EVENT.js#L7)  
> Since: 3.0.0

---

## GAME\_OUT

### GAME\_OUT

**Description:**

The Input Plugin Game Out Event.

This event is dispatched by the Input Plugin if the active pointer leaves the game canvas and is now

outside of it, elsewhere on the web page.

Listen to this event from within a Scene using: `this.input.on('gameout', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| event | MouseEvent | TouchEvent | No | The DOM Event that triggered the canvas out. |

> Source: [src/input/events/GAME\_OUT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAME_OUT_EVENT.js#L7)  
> Since: 3.16.1

---

## GAME\_OVER

### GAME\_OVER

**Description:**

The Input Plugin Game Over Event.

This event is dispatched by the Input Plugin if the active pointer enters the game canvas and is now

over of it, having previously been elsewhere on the web page.

Listen to this event from within a Scene using: `this.input.on('gameover', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| event | MouseEvent | TouchEvent | No | The DOM Event that triggered the canvas over. |

> Source: [src/input/events/GAME\_OVER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAME_OVER_EVENT.js#L7)  
> Since: 3.16.1

---

## GAMEOBJECT\_DOWN

### GAMEOBJECT\_DOWN

**Description:**

The Game Object Down Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer is pressed down on *any* interactive Game Object.

Listen to this event from within a Scene using: `this.input.on('gameobjectdown', listener)`.

To receive this event, the Game Objects must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_POINTER_DOWN`](Phaser.Input.Events.md) event instead.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_DOWN`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_DOWN`](Phaser.Input.Events.md)
3. [`POINTER_DOWN`](Phaser.Input.Events.md) or [`POINTER_DOWN_OUTSIDE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object the pointer was pressed down on. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_DOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_DOWN_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_DRAG

### GAMEOBJECT\_DRAG

**Description:**

The Game Object Drag Event.

This event is dispatched by an interactive Game Object if a pointer moves while dragging it.

Listen to this event from a Game Object using: `gameObject.on('drag', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive and enabled for drag.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| dragX | number | No | The x coordinate where the Pointer is currently dragging the Game Object, in world space. |
| dragY | number | No | The y coordinate where the Pointer is currently dragging the Game Object, in world space. |

> Source: [src/input/events/GAMEOBJECT\_DRAG\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_DRAG_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_DRAG\_END

### GAMEOBJECT\_DRAG\_END

**Description:**

The Game Object Drag End Event.

This event is dispatched by an interactive Game Object if a pointer stops dragging it.

Listen to this event from a Game Object using: `gameObject.on('dragend', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive and enabled for drag.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| dragX | number | No | The x coordinate where the Pointer stopped dragging the Game Object, in world space. |
| dragY | number | No | The y coordinate where the Pointer stopped dragging the Game Object, in world space. |
| dropped | boolean | No | Whether the Game Object was dropped onto a target. |

> Source: [src/input/events/GAMEOBJECT\_DRAG\_END\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_DRAG_END_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_DRAG\_ENTER

### GAMEOBJECT\_DRAG\_ENTER

**Description:**

The Game Object Drag Enter Event.

This event is dispatched by an interactive Game Object if a pointer drags it into a drag target.

Listen to this event from a Game Object using: `gameObject.on('dragenter', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive and enabled for drag.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| target | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The drag target that this pointer has moved into. |

> Source: [src/input/events/GAMEOBJECT\_DRAG\_ENTER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_DRAG_ENTER_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_DRAG\_LEAVE

### GAMEOBJECT\_DRAG\_LEAVE

**Description:**

The Game Object Drag Leave Event.

This event is dispatched by an interactive Game Object if a pointer drags it out of a drag target.

Listen to this event from a Game Object using: `gameObject.on('dragleave', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive and enabled for drag.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| target | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The drag target that this pointer has left. |

> Source: [src/input/events/GAMEOBJECT\_DRAG\_LEAVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_DRAG_LEAVE_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_DRAG\_OVER

### GAMEOBJECT\_DRAG\_OVER

**Description:**

The Game Object Drag Over Event.

This event is dispatched by an interactive Game Object if a pointer drags it over a drag target.

When the Game Object first enters the drag target it will emit a `dragenter` event. If it then moves while within

the drag target, it will emit this event instead.

Listen to this event from a Game Object using: `gameObject.on('dragover', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive and enabled for drag.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| target | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The drag target that this pointer has moved over. |

> Source: [src/input/events/GAMEOBJECT\_DRAG\_OVER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_DRAG_OVER_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_DRAG\_START

### GAMEOBJECT\_DRAG\_START

**Description:**

The Game Object Drag Start Event.

This event is dispatched by an interactive Game Object if a pointer starts to drag it.

Listen to this event from a Game Object using: `gameObject.on('dragstart', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive and enabled for drag.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

There are lots of useful drag related properties that are set within the Game Object when dragging occurs.

For example, `gameObject.input.dragStartX`, `dragStartY` and so on.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| dragX | number | No | The x coordinate where the Pointer is currently dragging the Game Object, in world space. |
| dragY | number | No | The y coordinate where the Pointer is currently dragging the Game Object, in world space. |

> Source: [src/input/events/GAMEOBJECT\_DRAG\_START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_DRAG_START_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_DROP

### GAMEOBJECT\_DROP

**Description:**

The Game Object Drop Event.

This event is dispatched by an interactive Game Object if a pointer drops it on a Drag Target.

Listen to this event from a Game Object using: `gameObject.on('drop', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive and enabled for drag.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| target | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Drag Target the `gameObject` has been dropped on. |

> Source: [src/input/events/GAMEOBJECT\_DROP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_DROP_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_MOVE

### GAMEOBJECT\_MOVE

**Description:**

The Game Object Move Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer is moved across *any* interactive Game Object.

Listen to this event from within a Scene using: `this.input.on('gameobjectmove', listener)`.

To receive this event, the Game Objects must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_POINTER_MOVE`](Phaser.Input.Events.md) event instead.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_MOVE`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_MOVE`](Phaser.Input.Events.md)
3. [`POINTER_MOVE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object the pointer was moved on. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_MOVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_MOVE_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_OUT

### GAMEOBJECT\_OUT

**Description:**

The Game Object Out Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer moves out of *any* interactive Game Object.

Listen to this event from within a Scene using: `this.input.on('gameobjectout', listener)`.

To receive this event, the Game Objects must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_POINTER_OUT`](Phaser.Input.Events.md) event instead.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_OUT`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_OUT`](Phaser.Input.Events.md)
3. [`POINTER_OUT`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

If the pointer leaves the game canvas itself, it will not trigger an this event. To handle those cases,

please listen for the [`GAME_OUT`](Phaser.Input.Events.md) event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object the pointer moved out of. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_OUT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_OUT_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_OVER

### GAMEOBJECT\_OVER

**Description:**

The Game Object Over Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer moves over *any* interactive Game Object.

Listen to this event from within a Scene using: `this.input.on('gameobjectover', listener)`.

To receive this event, the Game Objects must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_POINTER_OVER`](Phaser.Input.Events.md) event instead.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_OVER`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_OVER`](Phaser.Input.Events.md)
3. [`POINTER_OVER`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object the pointer moved over. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_OVER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_OVER_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_POINTER\_DOWN

### GAMEOBJECT\_POINTER\_DOWN

**Description:**

The Game Object Pointer Down Event.

This event is dispatched by an interactive Game Object if a pointer is pressed down on it.

Listen to this event from a Game Object using: `gameObject.on('pointerdown', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_DOWN`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_DOWN`](Phaser.Input.Events.md)
3. [`POINTER_DOWN`](Phaser.Input.Events.md) or [`POINTER_DOWN_OUTSIDE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| localX | number | No | The x coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position. |
| localY | number | No | The y coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_POINTER\_DOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_POINTER_DOWN_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_POINTER\_MOVE

### GAMEOBJECT\_POINTER\_MOVE

**Description:**

The Game Object Pointer Move Event.

This event is dispatched by an interactive Game Object if a pointer is moved while over it.

Listen to this event from a Game Object using: `gameObject.on('pointermove', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_MOVE`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_MOVE`](Phaser.Input.Events.md)
3. [`POINTER_MOVE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| localX | number | No | The x coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position. |
| localY | number | No | The y coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_POINTER\_MOVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_POINTER_MOVE_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_POINTER\_OUT

### GAMEOBJECT\_POINTER\_OUT

**Description:**

The Game Object Pointer Out Event.

This event is dispatched by an interactive Game Object if a pointer moves out of it.

Listen to this event from a Game Object using: `gameObject.on('pointerout', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_OUT`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_OUT`](Phaser.Input.Events.md)
3. [`POINTER_OUT`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

If the pointer leaves the game canvas itself, it will not trigger an this event. To handle those cases,

please listen for the [`GAME_OUT`](Phaser.Input.Events.md) event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_POINTER\_OUT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_POINTER_OUT_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_POINTER\_OVER

### GAMEOBJECT\_POINTER\_OVER

**Description:**

The Game Object Pointer Over Event.

This event is dispatched by an interactive Game Object if a pointer moves over it.

Listen to this event from a Game Object using: `gameObject.on('pointerover', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_OVER`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_OVER`](Phaser.Input.Events.md)
3. [`POINTER_OVER`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| localX | number | No | The x coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position. |
| localY | number | No | The y coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_POINTER\_OVER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_POINTER_OVER_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_POINTER\_UP

### GAMEOBJECT\_POINTER\_UP

**Description:**

The Game Object Pointer Up Event.

This event is dispatched by an interactive Game Object if a pointer is released while over it.

Listen to this event from a Game Object using: `gameObject.on('pointerup', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_UP`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_UP`](Phaser.Input.Events.md)
3. [`POINTER_UP`](Phaser.Input.Events.md) or [`POINTER_UP_OUTSIDE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| localX | number | No | The x coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position. |
| localY | number | No | The y coordinate that the Pointer interacted with this object on, relative to the Game Object's top-left position. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_POINTER\_UP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_POINTER_UP_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_POINTER\_WHEEL

### GAMEOBJECT\_POINTER\_WHEEL

**Description:**

The Game Object Pointer Wheel Event.

This event is dispatched by an interactive Game Object if a pointer has its wheel moved while over it.

Listen to this event from a Game Object using: `gameObject.on('wheel', listener)`.

Note that the scope of the listener is automatically set to be the Game Object instance itself.

To receive this event, the Game Object must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_WHEEL`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_WHEEL`](Phaser.Input.Events.md)
3. [`POINTER_WHEEL`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| deltaX | number | No | The horizontal scroll amount that occurred due to the user moving a mouse wheel or similar input device. |
| deltaY | number | No | The vertical scroll amount that occurred due to the user moving a mouse wheel or similar input device. This value will typically be less than 0 if the user scrolls up and greater than zero if scrolling down. |
| deltaZ | number | No | The z-axis scroll amount that occurred due to the user moving a mouse wheel or similar input device. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_POINTER\_WHEEL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_POINTER_WHEEL_EVENT.js#L7)  
> Since: 3.18.0

---

## GAMEOBJECT\_UP

### GAMEOBJECT\_UP

**Description:**

The Game Object Up Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer is released while over *any* interactive Game Object.

Listen to this event from within a Scene using: `this.input.on('gameobjectup', listener)`.

To receive this event, the Game Objects must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_POINTER_UP`](Phaser.Input.Events.md) event instead.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_UP`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_UP`](Phaser.Input.Events.md)
3. [`POINTER_UP`](Phaser.Input.Events.md) or [`POINTER_UP_OUTSIDE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object the pointer was over when released. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_UP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_UP_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEOBJECT\_WHEEL

### GAMEOBJECT\_WHEEL

**Description:**

The Game Object Wheel Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer has its wheel moved while over *any* interactive Game Object.

Listen to this event from within a Scene using: `this.input.on('gameobjectwheel', listener)`.

To receive this event, the Game Objects must have been set as interactive.

See [GameObject.setInteractive](Phaser.GameObjects.GameObject.md) for more details.

To listen for this event from a *specific* Game Object, use the [`GAMEOBJECT_POINTER_WHEEL`](Phaser.Input.Events.md) event instead.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_WHEEL`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_WHEEL`](Phaser.Input.Events.md)
3. [`POINTER_WHEEL`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object the pointer was over when the wheel changed. |
| deltaX | number | No | The horizontal scroll amount that occurred due to the user moving a mouse wheel or similar input device. |
| deltaY | number | No | The vertical scroll amount that occurred due to the user moving a mouse wheel or similar input device. This value will typically be less than 0 if the user scrolls up and greater than zero if scrolling down. |
| deltaZ | number | No | The z-axis scroll amount that occurred due to the user moving a mouse wheel or similar input device. |
| event | [Phaser.Types.Input.EventData](../typedef/types-input.md) | No | The Phaser input event. You can call `stopPropagation()` to halt it from going any further in the event flow. |

> Source: [src/input/events/GAMEOBJECT\_WHEEL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/GAMEOBJECT_WHEEL_EVENT.js#L7)  
> Since: 3.18.0

---

## MANAGER\_BOOT

### MANAGER\_BOOT

**Description:**

The Input Manager Boot Event.

This internal event is dispatched by the Input Manager when it boots.

> Source: [src/input/events/MANAGER\_BOOT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/MANAGER_BOOT_EVENT.js#L7)  
> Since: 3.0.0

---

## MANAGER\_PROCESS

### MANAGER\_PROCESS

**Description:**

The Input Manager Process Event.

This internal event is dispatched by the Input Manager when not using the legacy queue system,

and it wants the Input Plugins to update themselves.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/input/events/MANAGER\_PROCESS\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/MANAGER_PROCESS_EVENT.js#L7)  
> Since: 3.0.0

---

## MANAGER\_UPDATE

### MANAGER\_UPDATE

**Description:**

The Input Manager Update Event.

This internal event is dispatched by the Input Manager as part of its update step.

> Source: [src/input/events/MANAGER\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/MANAGER_UPDATE_EVENT.js#L7)  
> Since: 3.0.0

---

## POINTER\_DOWN

### POINTER\_DOWN

**Description:**

The Pointer Down Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer is pressed down anywhere.

Listen to this event from within a Scene using: `this.input.on('pointerdown', listener)`.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_DOWN`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_DOWN`](Phaser.Input.Events.md)
3. [`POINTER_DOWN`](Phaser.Input.Events.md) or [`POINTER_DOWN_OUTSIDE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| currentlyOver | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array containing all interactive Game Objects that the pointer was over when the event was created. |

> Source: [src/input/events/POINTER\_DOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/POINTER_DOWN_EVENT.js#L7)  
> Since: 3.0.0

---

## POINTER\_DOWN\_OUTSIDE

### POINTER\_DOWN\_OUTSIDE

**Description:**

The Pointer Down Outside Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer is pressed down anywhere outside of the game canvas.

Listen to this event from within a Scene using: `this.input.on('pointerdownoutside', listener)`.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_DOWN`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_DOWN`](Phaser.Input.Events.md)
3. [`POINTER_DOWN`](Phaser.Input.Events.md) or [`POINTER_DOWN_OUTSIDE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |

> Source: [src/input/events/POINTER\_DOWN\_OUTSIDE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/POINTER_DOWN_OUTSIDE_EVENT.js#L7)  
> Since: 3.16.1

---

## POINTER\_MOVE

### POINTER\_MOVE

**Description:**

The Pointer Move Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer is moved anywhere.

Listen to this event from within a Scene using: `this.input.on('pointermove', listener)`.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_MOVE`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_MOVE`](Phaser.Input.Events.md)
3. [`POINTER_MOVE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| currentlyOver | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array containing all interactive Game Objects that the pointer was over when the event was created. |

> Source: [src/input/events/POINTER\_MOVE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/POINTER_MOVE_EVENT.js#L7)  
> Since: 3.0.0

---

## POINTER\_OUT

### POINTER\_OUT

**Description:**

The Pointer Out Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer moves out of any interactive Game Object.

Listen to this event from within a Scene using: `this.input.on('pointerout', listener)`.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_OUT`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_OUT`](Phaser.Input.Events.md)
3. [`POINTER_OUT`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

If the pointer leaves the game canvas itself, it will not trigger an this event. To handle those cases,

please listen for the [`GAME_OUT`](Phaser.Input.Events.md) event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| justOut | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array containing all interactive Game Objects that the pointer moved out of when the event was created. |

> Source: [src/input/events/POINTER\_OUT\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/POINTER_OUT_EVENT.js#L7)  
> Since: 3.0.0

---

## POINTER\_OVER

### POINTER\_OVER

**Description:**

The Pointer Over Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer moves over any interactive Game Object.

Listen to this event from within a Scene using: `this.input.on('pointerover', listener)`.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_OVER`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_OVER`](Phaser.Input.Events.md)
3. [`POINTER_OVER`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| justOver | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array containing all interactive Game Objects that the pointer moved over when the event was created. |

> Source: [src/input/events/POINTER\_OVER\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/POINTER_OVER_EVENT.js#L7)  
> Since: 3.0.0

---

## POINTER\_UP

### POINTER\_UP

**Description:**

The Pointer Up Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer is released anywhere.

Listen to this event from within a Scene using: `this.input.on('pointerup', listener)`.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_UP`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_UP`](Phaser.Input.Events.md)
3. [`POINTER_UP`](Phaser.Input.Events.md) or [`POINTER_UP_OUTSIDE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| currentlyOver | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array containing all interactive Game Objects that the pointer was over when the event was created. |

> Source: [src/input/events/POINTER\_UP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/POINTER_UP_EVENT.js#L7)  
> Since: 3.0.0

---

## POINTER\_UP\_OUTSIDE

### POINTER\_UP\_OUTSIDE

**Description:**

The Pointer Up Outside Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer is released anywhere outside of the game canvas.

Listen to this event from within a Scene using: `this.input.on('pointerupoutside', listener)`.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_UP`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_UP`](Phaser.Input.Events.md)
3. [`POINTER_UP`](Phaser.Input.Events.md) or [`POINTER_UP_OUTSIDE`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |

> Source: [src/input/events/POINTER\_UP\_OUTSIDE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/POINTER_UP_OUTSIDE_EVENT.js#L7)  
> Since: 3.16.1

---

## POINTER\_WHEEL

### POINTER\_WHEEL

**Description:**

The Pointer Wheel Input Event.

This event is dispatched by the Input Plugin belonging to a Scene if a pointer has its wheel updated.

Listen to this event from within a Scene using: `this.input.on('wheel', listener)`.

The event hierarchy is as follows:

1. [`GAMEOBJECT_POINTER_WHEEL`](Phaser.Input.Events.md)
2. [`GAMEOBJECT_WHEEL`](Phaser.Input.Events.md)
3. [`POINTER_WHEEL`](Phaser.Input.Events.md)

With the top event being dispatched first and then flowing down the list. Note that higher-up event handlers can stop

the propagation of this event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pointer | [Phaser.Input.Pointer](../class/input-pointer.md) | No | The Pointer responsible for triggering this event. |
| --- | --- | --- | --- |
| currentlyOver | Array.<[Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md)> | No | An array containing all interactive Game Objects that the pointer was over when the event was created. |
| deltaX | number | No | The horizontal scroll amount that occurred due to the user moving a mouse wheel or similar input device. |
| deltaY | number | No | The vertical scroll amount that occurred due to the user moving a mouse wheel or similar input device. This value will typically be less than 0 if the user scrolls up and greater than zero if scrolling down. |
| deltaZ | number | No | The z-axis scroll amount that occurred due to the user moving a mouse wheel or similar input device. |

> Source: [src/input/events/POINTER\_WHEEL\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/POINTER_WHEEL_EVENT.js#L7)  
> Since: 3.18.0

---

## POINTERLOCK\_CHANGE

### POINTERLOCK\_CHANGE

**Description:**

The Input Manager Pointer Lock Change Event.

This event is dispatched by the Input Manager when it is processing a native Pointer Lock Change DOM Event.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | Event | No | The native DOM Event. |
| --- | --- | --- | --- |
| locked | boolean | No | The locked state of the Mouse Pointer. |

> Source: [src/input/events/POINTERLOCK\_CHANGE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/POINTERLOCK_CHANGE_EVENT.js#L7)  
> Since: 3.0.0

---

## PRE\_UPDATE

### PRE\_UPDATE

**Description:**

The Input Plugin Pre-Update Event.

This internal event is dispatched by the Input Plugin at the start of its `preUpdate` method.

This hook is designed specifically for input plugins, but can also be listened to from user-land code.

> Source: [src/input/events/PRE\_UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/PRE_UPDATE_EVENT.js#L7)  
> Since: 3.0.0

---

## SHUTDOWN

### SHUTDOWN

**Description:**

The Input Plugin Shutdown Event.

This internal event is dispatched by the Input Plugin when it shuts down, signalling to all of its systems to shut themselves down.

> Source: [src/input/events/SHUTDOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/SHUTDOWN_EVENT.js#L7)  
> Since: 3.0.0

---

## START

### START

**Description:**

The Input Plugin Start Event.

This internal event is dispatched by the Input Plugin when it has finished setting-up,

signalling to all of its internal systems to start.

> Source: [src/input/events/START\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/START_EVENT.js#L7)  
> Since: 3.0.0

---

## UPDATE

### UPDATE

**Description:**

The Input Plugin Update Event.

This internal event is dispatched by the Input Plugin at the start of its `update` method.

This hook is designed specifically for input plugins, but can also be listened to from user-land code.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| time | number | No | The current time. Either a High Resolution Timer value if it comes from Request Animation Frame, or Date.now if using SetTimeout. |
| --- | --- | --- | --- |
| delta | number | No | The delta time in ms since the last frame. This is a smoothed and capped value based on the FPS rate. |

> Source: [src/input/events/UPDATE\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/events/UPDATE_EVENT.js#L7)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [BOOT](#boot)

    - [BOOT](#boot-1)
  + [DESTROY](#destroy)

    - [DESTROY](#destroy-1)
  + [DRAG](#drag)

    - [DRAG](#drag-1)
  + [DRAG\_END](#drag_end)

    - [DRAG\_END](#drag_end-1)
  + [DRAG\_ENTER](#drag_enter)

    - [DRAG\_ENTER](#drag_enter-1)
  + [DRAG\_LEAVE](#drag_leave)

    - [DRAG\_LEAVE](#drag_leave-1)
  + [DRAG\_OVER](#drag_over)

    - [DRAG\_OVER](#drag_over-1)
  + [DRAG\_START](#drag_start)

    - [DRAG\_START](#drag_start-1)
  + [DROP](#drop)

    - [DROP](#drop-1)
  + [GAME\_OUT](#game_out)

    - [GAME\_OUT](#game_out-1)
  + [GAME\_OVER](#game_over)

    - [GAME\_OVER](#game_over-1)
  + [GAMEOBJECT\_DOWN](#gameobject_down)

    - [GAMEOBJECT\_DOWN](#gameobject_down-1)
  + [GAMEOBJECT\_DRAG](#gameobject_drag)

    - [GAMEOBJECT\_DRAG](#gameobject_drag-1)
  + [GAMEOBJECT\_DRAG\_END](#gameobject_drag_end)

    - [GAMEOBJECT\_DRAG\_END](#gameobject_drag_end-1)
  + [GAMEOBJECT\_DRAG\_ENTER](#gameobject_drag_enter)

    - [GAMEOBJECT\_DRAG\_ENTER](#gameobject_drag_enter-1)
  + [GAMEOBJECT\_DRAG\_LEAVE](#gameobject_drag_leave)

    - [GAMEOBJECT\_DRAG\_LEAVE](#gameobject_drag_leave-1)
  + [GAMEOBJECT\_DRAG\_OVER](#gameobject_drag_over)

    - [GAMEOBJECT\_DRAG\_OVER](#gameobject_drag_over-1)
  + [GAMEOBJECT\_DRAG\_START](#gameobject_drag_start)

    - [GAMEOBJECT\_DRAG\_START](#gameobject_drag_start-1)
  + [GAMEOBJECT\_DROP](#gameobject_drop)

    - [GAMEOBJECT\_DROP](#gameobject_drop-1)
  + [GAMEOBJECT\_MOVE](#gameobject_move)

    - [GAMEOBJECT\_MOVE](#gameobject_move-1)
  + [GAMEOBJECT\_OUT](#gameobject_out)

    - [GAMEOBJECT\_OUT](#gameobject_out-1)
  + [GAMEOBJECT\_OVER](#gameobject_over)

    - [GAMEOBJECT\_OVER](#gameobject_over-1)
  + [GAMEOBJECT\_POINTER\_DOWN](#gameobject_pointer_down)

    - [GAMEOBJECT\_POINTER\_DOWN](#gameobject_pointer_down-1)
  + [GAMEOBJECT\_POINTER\_MOVE](#gameobject_pointer_move)

    - [GAMEOBJECT\_POINTER\_MOVE](#gameobject_pointer_move-1)
  + [GAMEOBJECT\_POINTER\_OUT](#gameobject_pointer_out)

    - [GAMEOBJECT\_POINTER\_OUT](#gameobject_pointer_out-1)
  + [GAMEOBJECT\_POINTER\_OVER](#gameobject_pointer_over)

    - [GAMEOBJECT\_POINTER\_OVER](#gameobject_pointer_over-1)
  + [GAMEOBJECT\_POINTER\_UP](#gameobject_pointer_up)

    - [GAMEOBJECT\_POINTER\_UP](#gameobject_pointer_up-1)
  + [GAMEOBJECT\_POINTER\_WHEEL](#gameobject_pointer_wheel)

    - [GAMEOBJECT\_POINTER\_WHEEL](#gameobject_pointer_wheel-1)
  + [GAMEOBJECT\_UP](#gameobject_up)

    - [GAMEOBJECT\_UP](#gameobject_up-1)
  + [GAMEOBJECT\_WHEEL](#gameobject_wheel)

    - [GAMEOBJECT\_WHEEL](#gameobject_wheel-1)
  + [MANAGER\_BOOT](#manager_boot)

    - [MANAGER\_BOOT](#manager_boot-1)
  + [MANAGER\_PROCESS](#manager_process)

    - [MANAGER\_PROCESS](#manager_process-1)
  + [MANAGER\_UPDATE](#manager_update)

    - [MANAGER\_UPDATE](#manager_update-1)
  + [POINTER\_DOWN](#pointer_down)

    - [POINTER\_DOWN](#pointer_down-1)
  + [POINTER\_DOWN\_OUTSIDE](#pointer_down_outside)

    - [POINTER\_DOWN\_OUTSIDE](#pointer_down_outside-1)
  + [POINTER\_MOVE](#pointer_move)

    - [POINTER\_MOVE](#pointer_move-1)
  + [POINTER\_OUT](#pointer_out)

    - [POINTER\_OUT](#pointer_out-1)
  + [POINTER\_OVER](#pointer_over)

    - [POINTER\_OVER](#pointer_over-1)
  + [POINTER\_UP](#pointer_up)

    - [POINTER\_UP](#pointer_up-1)
  + [POINTER\_UP\_OUTSIDE](#pointer_up_outside)

    - [POINTER\_UP\_OUTSIDE](#pointer_up_outside-1)
  + [POINTER\_WHEEL](#pointer_wheel)

    - [POINTER\_WHEEL](#pointer_wheel-1)
  + [POINTERLOCK\_CHANGE](#pointerlock_change)

    - [POINTERLOCK\_CHANGE](#pointerlock_change-1)
  + [PRE\_UPDATE](#pre_update)

    - [PRE\_UPDATE](#pre_update-1)
  + [SHUTDOWN](#shutdown)

    - [SHUTDOWN](#shutdown-1)
  + [START](#start)

    - [START](#start-1)
  + [UPDATE](#update)

    - [UPDATE](#update-1)

Back to top

©2025[Phaser](https://docs.phaser.io)