# Phaser.Input

Scope:
static

> Source: [src/input/index.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/index.js#L10)

# Static functions

* [InputManager](../class/input-inputmanager.md)
* [InputPlugin](../class/input-inputplugin.md)
* [Pointer](../class/input-pointer.md)

# Static functions

## MOUSE\_DOWN

### MOUSE\_DOWN: number

**Description:**

The mouse pointer is being held down.

> Source: [src/input/const.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/const.js#L9)  
> Since: 3.10.0

---

## MOUSE\_MOVE

### MOUSE\_MOVE: number

**Description:**

The mouse pointer is being moved.

> Source: [src/input/const.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/const.js#L18)  
> Since: 3.10.0

---

## MOUSE\_UP

### MOUSE\_UP: number

**Description:**

The mouse pointer is released.

> Source: [src/input/const.js#L27](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/const.js#L27)  
> Since: 3.10.0

---

## MOUSE\_WHEEL

### MOUSE\_WHEEL: number

**Description:**

The mouse wheel changes.

> Source: [src/input/const.js#L81](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/const.js#L81)  
> Since: 3.18.0

---

## POINTER\_LOCK\_CHANGE

### POINTER\_LOCK\_CHANGE: number

**Description:**

The pointer lock has changed.

> Source: [src/input/const.js#L63](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/const.js#L63)  
> Since: 3.10.0

---

## TOUCH\_CANCEL

### TOUCH\_CANCEL: number

**Description:**

A touch pointer has been been cancelled by the browser.

> Source: [src/input/const.js#L72](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/const.js#L72)  
> Since: 3.15.0

---

## TOUCH\_END

### TOUCH\_END: number

**Description:**

A touch pointer has been started.

> Source: [src/input/const.js#L54](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/const.js#L54)  
> Since: 3.10.0

---

## TOUCH\_MOVE

### TOUCH\_MOVE: number

**Description:**

A touch pointer has been started.

> Source: [src/input/const.js#L45](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/const.js#L45)  
> Since: 3.10.0

---

## TOUCH\_START

### TOUCH\_START: number

**Description:**

A touch pointer has been started.

> Source: [src/input/const.js#L36](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/const.js#L36)  
> Since: 3.10.0

---

# Static functions

## CreateInteractiveObject

### <static> CreateInteractiveObject(gameObject, hitArea, hitAreaCallback)

**Description:**

Creates a new Interactive Object.

This is called automatically by the Input Manager when you enable a Game Object for input.

The resulting Interactive Object is mapped to the Game Object's `input` property.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| gameObject | [Phaser.GameObjects.GameObject](../class/gameobjects-gameobject.md) | No | The Game Object to which this Interactive Object is bound. |
| --- | --- | --- | --- |
| hitArea | any | No | The hit area for this Interactive Object. Typically a geometry shape, like a Rectangle or Circle. |
| hitAreaCallback | [Phaser.Types.Input.HitAreaCallback](../typedef/types-input.md) | No | The 'contains' check callback that the hit area shape will use for all hit tests. |

**Returns:** [Phaser.Types.Input.InteractiveObject](../typedef/types-input.md) - The new Interactive Object.

> Source: [src/input/CreateInteractiveObject.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/CreateInteractiveObject.js#L7)  
> Since: 3.0.0

---

## CreatePixelPerfectHandler

### <static> CreatePixelPerfectHandler(textureManager, alphaTolerance)

**Description:**

Creates a new Pixel Perfect Handler function.

Access via `InputPlugin.makePixelPerfect` rather than calling it directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| textureManager | [Phaser.Textures.TextureManager](../class/textures-texturemanager.md) | No | A reference to the Texture Manager. |
| --- | --- | --- | --- |
| alphaTolerance | number | No | The alpha level that the pixel should be above to be included as a successful interaction. |

**Returns:** function - The new Pixel Perfect Handler function.

> Source: [src/input/CreatePixelPerfectHandler.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/CreatePixelPerfectHandler.js#L7)  
> Since: 3.10.0

---

# Static functions

* [Events](input-events.md)
* [Gamepad](input-gamepad.md)
* [InputPluginCache](input-inputplugincache.md)
* [Keyboard](input-keyboard.md)
* [Mouse](input-mouse.md)
* [Touch](input-touch.md)

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)

  + [MOUSE\_DOWN](#mouse_down)

    - [MOUSE\_DOWN: number](#mouse_down-number)
  + [MOUSE\_MOVE](#mouse_move)

    - [MOUSE\_MOVE: number](#mouse_move-number)
  + [MOUSE\_UP](#mouse_up)

    - [MOUSE\_UP: number](#mouse_up-number)
  + [MOUSE\_WHEEL](#mouse_wheel)

    - [MOUSE\_WHEEL: number](#mouse_wheel-number)
  + [POINTER\_LOCK\_CHANGE](#pointer_lock_change)

    - [POINTER\_LOCK\_CHANGE: number](#pointer_lock_change-number)
  + [TOUCH\_CANCEL](#touch_cancel)

    - [TOUCH\_CANCEL: number](#touch_cancel-number)
  + [TOUCH\_END](#touch_end)

    - [TOUCH\_END: number](#touch_end-number)
  + [TOUCH\_MOVE](#touch_move)

    - [TOUCH\_MOVE: number](#touch_move-number)
  + [TOUCH\_START](#touch_start)

    - [TOUCH\_START: number](#touch_start-number)
* [Static functions](#static-functions-2)

  + [CreateInteractiveObject](#createinteractiveobject)

    - [<static> CreateInteractiveObject(gameObject, hitArea, hitAreaCallback)](#static-createinteractiveobjectgameobject-hitarea-hitareacallback)
  + [CreatePixelPerfectHandler](#createpixelperfecthandler)

    - [<static> CreatePixelPerfectHandler(textureManager, alphaTolerance)](#static-createpixelperfecthandlertexturemanager-alphatolerance)
* [Static functions](#static-functions-3)

Back to top

©2025[Phaser](https://docs.phaser.io)