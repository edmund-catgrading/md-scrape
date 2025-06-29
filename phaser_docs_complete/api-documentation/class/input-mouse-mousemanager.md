# MouseManager

Phaser.Input.Mouse.MouseManager

The Mouse Manager is a helper class that belongs to the Input Manager.

Its role is to listen for native DOM Mouse Events and then pass them onto the Input Manager for further processing.

You do not need to create this class directly, the Input Manager will create an instance of it automatically.

**Constructor**

`new MouseManager(inputManager)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| inputManager | [Phaser.Input.InputManager](input-inputmanager.md) | No | A reference to the Input Manager. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/input/mouse/MouseManager.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L15)  
> Since: 3.0.0

# Public Members

## enabled

### enabled: boolean

**Description:**

A boolean that controls if the Mouse Manager is enabled or not.

Can be toggled on the fly.

> Source: [src/input/mouse/MouseManager.js#L85](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L85)  
> Since: 3.0.0

---

## isTop

### isTop: boolean

**Description:**

Are the event listeners hooked into `window.top` or `window`?

This is set during the `boot` sequence. If the browser does not have access to `window.top`,

such as in cross-origin iframe environments, this property gets set to `false` and the events

are hooked into `window` instead.

> Source: [src/input/mouse/MouseManager.js#L215](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L215)  
> Since: 3.50.0

---

## locked

### locked: boolean

**Description:**

If the mouse has been pointer locked successfully this will be set to true.

> Source: [src/input/mouse/MouseManager.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L106)  
> Since: 3.0.0

---

## manager

### manager: [Phaser.Input.InputManager](input-inputmanager.md)

**Description:**

A reference to the Input Manager.

> Source: [src/input/mouse/MouseManager.js#L36](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L36)  
> Since: 3.0.0

---

## onMouseDown

### onMouseDown: function

**Description:**

The Mouse Down Event handler.

This function is sent the native DOM MouseEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/mouse/MouseManager.js#L127](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L127)  
> Since: 3.10.0

---

## onMouseDownWindow

### onMouseDownWindow: function

**Description:**

The Mouse Down Event handler specifically for events on the Window.

This function is sent the native DOM MouseEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/mouse/MouseManager.js#L149](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L149)  
> Since: 3.17.0

---

## onMouseMove

### onMouseMove: function

**Description:**

The Mouse Move Event handler.

This function is sent the native DOM MouseEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/mouse/MouseManager.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L116)  
> Since: 3.10.0

---

## onMouseOut

### onMouseOut: function

**Description:**

The Mouse Out Event handler.

This function is sent the native DOM MouseEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/mouse/MouseManager.js#L182](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L182)  
> Since: 3.16.0

---

## onMouseOver

### onMouseOver: function

**Description:**

The Mouse Over Event handler.

This function is sent the native DOM MouseEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/mouse/MouseManager.js#L171](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L171)  
> Since: 3.16.0

---

## onMouseUp

### onMouseUp: function

**Description:**

The Mouse Up Event handler.

This function is sent the native DOM MouseEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/mouse/MouseManager.js#L138](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L138)  
> Since: 3.10.0

---

## onMouseUpWindow

### onMouseUpWindow: function

**Description:**

The Mouse Up Event handler specifically for events on the Window.

This function is sent the native DOM MouseEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/mouse/MouseManager.js#L160](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L160)  
> Since: 3.17.0

---

## onMouseWheel

### onMouseWheel: function

**Description:**

The Mouse Wheel Event handler.

This function is sent the native DOM MouseEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/mouse/MouseManager.js#L193](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L193)  
> Since: 3.18.0

---

## pointerLockChange

### pointerLockChange: function

**Description:**

Internal pointerLockChange handler.

This function is sent the native DOM MouseEvent.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/mouse/MouseManager.js#L204](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L204)  
> Since: 3.0.0

---

## preventDefaultDown

### preventDefaultDown: boolean

**Description:**

If `true` the DOM `mousedown` event will have `preventDefault` set.

> Source: [src/input/mouse/MouseManager.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L45)  
> Since: 3.50.0

---

## preventDefaultMove

### preventDefaultMove: boolean

**Description:**

If `true` the DOM `mousemove` event will have `preventDefault` set.

> Source: [src/input/mouse/MouseManager.js#L65](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L65)  
> Since: 3.50.0

---

## preventDefaultUp

### preventDefaultUp: boolean

**Description:**

If `true` the DOM `mouseup` event will have `preventDefault` set.

> Source: [src/input/mouse/MouseManager.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L55)  
> Since: 3.50.0

---

## preventDefaultWheel

### preventDefaultWheel: boolean

**Description:**

If `true` the DOM `wheel` event will have `preventDefault` set.

> Source: [src/input/mouse/MouseManager.js#L75](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L75)  
> Since: 3.50.0

---

## target

### target: any

**Description:**

The Mouse target, as defined in the Game Config.

Typically the canvas to which the game is rendering, but can be any interactive DOM element.

> Source: [src/input/mouse/MouseManager.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L96)  
> Since: 3.0.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this Mouse Manager instance.

> Source: [src/input/mouse/MouseManager.js#L553](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L553)  
> Since: 3.0.0

---

## disableContextMenu

### <instance> disableContextMenu()

**Description:**

Attempts to disable the context menu from appearing if you right-click on the game canvas, or specified input target.

Works by listening for the `contextmenu` event and prevent defaulting it.

Use this if you need to enable right-button mouse support in your game, and the context

menu keeps getting in the way.

**Returns:** [Phaser.Input.Mouse.MouseManager](input-mouse-mousemanager.md) - This Mouse Manager instance.

> Source: [src/input/mouse/MouseManager.js#L272](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L272)  
> Since: 3.0.0

---

## releasePointerLock

### <instance> releasePointerLock()

**Description:**

If the browser supports pointer lock, this will request that the pointer lock is released. If

the browser successfully enters a locked state, a 'POINTER\_LOCK\_CHANGE\_EVENT' will be

dispatched - from the game's input manager - with an `isPointerLocked` property.

> Source: [src/input/mouse/MouseManager.js#L329](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L329)  
> Since: 3.0.0

---

## requestPointerLock

### <instance> requestPointerLock()

**Description:**

If the browser supports it, you can request that the pointer be locked to the browser window.

This is classically known as 'FPS controls', where the pointer can't leave the browser until

the user presses an exit key.

If the browser successfully enters a locked state, a `POINTER_LOCK_CHANGE_EVENT` will be dispatched,

from the games Input Manager, with an `isPointerLocked` property.

It is important to note that pointer lock can only be enabled after an 'engagement gesture',

see: <https://w3c.github.io/pointerlock/#dfn-engagement-gesture.>

Note for Firefox: There is a bug in certain Firefox releases that cause native DOM events like

`mousemove` to fire continuously when in pointer lock mode. You can get around this by setting

`this.preventDefaultMove` to `false` in this class. You may also need to do the same for

`preventDefaultDown` and/or `preventDefaultUp`. Please test combinations of these if you encounter

the error.

> Source: [src/input/mouse/MouseManager.js#L296](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L296)  
> Since: 3.0.0

---

## startListeners

### <instance> startListeners()

**Description:**

Starts the Mouse Event listeners running.

This is called automatically and does not need to be manually invoked.

> Source: [src/input/mouse/MouseManager.js#L346](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L346)  
> Since: 3.0.0

---

## stopListeners

### <instance> stopListeners()

**Description:**

Stops the Mouse Event listeners.

This is called automatically and does not need to be manually invoked.

> Source: [src/input/mouse/MouseManager.js#L520](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L520)  
> Since: 3.0.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

The Touch Manager boot process.

**Access:** private

> Source: [src/input/mouse/MouseManager.js#L232](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/mouse/MouseManager.js#L232)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [enabled](#enabled)

    - [enabled: boolean](#enabled-boolean)
  + [isTop](#istop)

    - [isTop: boolean](#istop-boolean)
  + [locked](#locked)

    - [locked: boolean](#locked-boolean)
  + [manager](#manager)

    - [manager: Phaser.Input.InputManager](#manager-phaserinputinputmanager)
  + [onMouseDown](#onmousedown)

    - [onMouseDown: function](#onmousedown-function)
  + [onMouseDownWindow](#onmousedownwindow)

    - [onMouseDownWindow: function](#onmousedownwindow-function)
  + [onMouseMove](#onmousemove)

    - [onMouseMove: function](#onmousemove-function)
  + [onMouseOut](#onmouseout)

    - [onMouseOut: function](#onmouseout-function)
  + [onMouseOver](#onmouseover)

    - [onMouseOver: function](#onmouseover-function)
  + [onMouseUp](#onmouseup)

    - [onMouseUp: function](#onmouseup-function)
  + [onMouseUpWindow](#onmouseupwindow)

    - [onMouseUpWindow: function](#onmouseupwindow-function)
  + [onMouseWheel](#onmousewheel)

    - [onMouseWheel: function](#onmousewheel-function)
  + [pointerLockChange](#pointerlockchange)

    - [pointerLockChange: function](#pointerlockchange-function)
  + [preventDefaultDown](#preventdefaultdown)

    - [preventDefaultDown: boolean](#preventdefaultdown-boolean)
  + [preventDefaultMove](#preventdefaultmove)

    - [preventDefaultMove: boolean](#preventdefaultmove-boolean)
  + [preventDefaultUp](#preventdefaultup)

    - [preventDefaultUp: boolean](#preventdefaultup-boolean)
  + [preventDefaultWheel](#preventdefaultwheel)

    - [preventDefaultWheel: boolean](#preventdefaultwheel-boolean)
  + [target](#target)

    - [target: any](#target-any)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [disableContextMenu](#disablecontextmenu)

    - [<instance> disableContextMenu()](#instance-disablecontextmenu)
  + [releasePointerLock](#releasepointerlock)

    - [<instance> releasePointerLock()](#instance-releasepointerlock)
  + [requestPointerLock](#requestpointerlock)

    - [<instance> requestPointerLock()](#instance-requestpointerlock)
  + [startListeners](#startlisteners)

    - [<instance> startListeners()](#instance-startlisteners)
  + [stopListeners](#stoplisteners)

    - [<instance> stopListeners()](#instance-stoplisteners)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)

Back to top

©2025[Phaser](https://docs.phaser.io)