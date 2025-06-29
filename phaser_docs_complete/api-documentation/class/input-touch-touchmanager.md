# TouchManager

Phaser.Input.Touch.TouchManager

The Touch Manager is a helper class that belongs to the Input Manager.

Its role is to listen for native DOM Touch Events and then pass them onto the Input Manager for further processing.

You do not need to create this class directly, the Input Manager will create an instance of it automatically.

**Constructor**

`new TouchManager(inputManager)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| inputManager | [Phaser.Input.InputManager](input-inputmanager.md) | No | A reference to the Input Manager. |
| --- | --- | --- | --- |

---

**Scope**: static

> Source: [src/input/touch/TouchManager.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L15)  
> Since: 3.0.0

# Public Members

## capture

### capture: boolean

**Description:**

If true the DOM events will have event.preventDefault applied to them, if false they will propagate fully.

> Source: [src/input/touch/TouchManager.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L45)  
> Since: 3.0.0

---

## enabled

### enabled: boolean

**Description:**

A boolean that controls if the Touch Manager is enabled or not.

Can be toggled on the fly.

> Source: [src/input/touch/TouchManager.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L55)  
> Since: 3.0.0

---

## isTop

### isTop: boolean

**Description:**

Are the event listeners hooked into `window.top` or `window`?

This is set during the `boot` sequence. If the browser does not have access to `window.top`,

such as in cross-origin iframe environments, this property gets set to `false` and the events

are hooked into `window` instead.

> Source: [src/input/touch/TouchManager.js#L146](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L146)  
> Since: 3.60.0

---

## manager

### manager: [Phaser.Input.InputManager](input-inputmanager.md)

**Description:**

A reference to the Input Manager.

> Source: [src/input/touch/TouchManager.js#L36](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L36)  
> Since: 3.0.0

---

## onTouchCancel

### onTouchCancel: function

**Description:**

The Touch Cancel event handler function.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/touch/TouchManager.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L126)  
> Since: 3.15.0

---

## onTouchCancelWindow

### onTouchCancelWindow: function

**Description:**

The Touch Cancel event handler function specifically for events on the Window.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/touch/TouchManager.js#L136](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L136)  
> Since: 3.18.0

---

## onTouchEnd

### onTouchEnd: function

**Description:**

The Touch End event handler function.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/touch/TouchManager.js#L106](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L106)  
> Since: 3.0.0

---

## onTouchEndWindow

### onTouchEndWindow: function

**Description:**

The Touch End event handler function specifically for events on the Window.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/touch/TouchManager.js#L116](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L116)  
> Since: 3.17.0

---

## onTouchMove

### onTouchMove: function

**Description:**

The Touch Move event handler function.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/touch/TouchManager.js#L96](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L96)  
> Since: 3.0.0

---

## onTouchStart

### onTouchStart: function

**Description:**

The Touch Start event handler function.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/touch/TouchManager.js#L76](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L76)  
> Since: 3.0.0

---

## onTouchStartWindow

### onTouchStartWindow: function

**Description:**

The Touch Start event handler function specifically for events on the Window.

Initially empty and bound in the `startListeners` method.

> Source: [src/input/touch/TouchManager.js#L86](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L86)  
> Since: 3.17.0

---

## target

### target: any

**Description:**

The Touch Event target, as defined in the Game Config.

Typically the canvas to which the game is rendering, but can be any interactive DOM element.

> Source: [src/input/touch/TouchManager.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L66)  
> Since: 3.0.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this Touch Manager instance.

> Source: [src/input/touch/TouchManager.js#L384](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L384)  
> Since: 3.0.0

---

## disableContextMenu

### <instance> disableContextMenu()

**Description:**

Attempts to disable the context menu from appearing if you touch-hold on the browser.

Works by listening for the `contextmenu` event and prevent defaulting it.

Use this if you need to disable the OS context menu on mobile.

**Returns:** [Phaser.Input.Touch.TouchManager](input-touch-touchmanager.md) - This Touch Manager instance.

> Source: [src/input/touch/TouchManager.js#L198](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L198)  
> Since: 3.20.0

---

## startListeners

### <instance> startListeners()

**Description:**

Starts the Touch Event listeners running as long as an input target is set.

This method is called automatically if Touch Input is enabled in the game config,

which it is by default. However, you can call it manually should you need to

delay input capturing until later in the game.

> Source: [src/input/touch/TouchManager.js#L221](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L221)  
> Since: 3.0.0

---

## stopListeners

### <instance> stopListeners()

**Description:**

Stops the Touch Event listeners.

This is called automatically and does not need to be manually invoked.

> Source: [src/input/touch/TouchManager.js#L358](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L358)  
> Since: 3.0.0

---

# Private Methods

## boot

### <instance> boot()

**Description:**

The Touch Manager boot process.

**Access:** private

> Source: [src/input/touch/TouchManager.js#L163](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/touch/TouchManager.js#L163)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [capture](#capture)

    - [capture: boolean](#capture-boolean)
  + [enabled](#enabled)

    - [enabled: boolean](#enabled-boolean)
  + [isTop](#istop)

    - [isTop: boolean](#istop-boolean)
  + [manager](#manager)

    - [manager: Phaser.Input.InputManager](#manager-phaserinputinputmanager)
  + [onTouchCancel](#ontouchcancel)

    - [onTouchCancel: function](#ontouchcancel-function)
  + [onTouchCancelWindow](#ontouchcancelwindow)

    - [onTouchCancelWindow: function](#ontouchcancelwindow-function)
  + [onTouchEnd](#ontouchend)

    - [onTouchEnd: function](#ontouchend-function)
  + [onTouchEndWindow](#ontouchendwindow)

    - [onTouchEndWindow: function](#ontouchendwindow-function)
  + [onTouchMove](#ontouchmove)

    - [onTouchMove: function](#ontouchmove-function)
  + [onTouchStart](#ontouchstart)

    - [onTouchStart: function](#ontouchstart-function)
  + [onTouchStartWindow](#ontouchstartwindow)

    - [onTouchStartWindow: function](#ontouchstartwindow-function)
  + [target](#target)

    - [target: any](#target-any)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [disableContextMenu](#disablecontextmenu)

    - [<instance> disableContextMenu()](#instance-disablecontextmenu)
  + [startListeners](#startlisteners)

    - [<instance> startListeners()](#instance-startlisteners)
  + [stopListeners](#stoplisteners)

    - [<instance> stopListeners()](#instance-stoplisteners)
* [Private Methods](#private-methods)

  + [boot](#boot)

    - [<instance> boot()](#instance-boot)

Back to top

©2025[Phaser](https://docs.phaser.io)