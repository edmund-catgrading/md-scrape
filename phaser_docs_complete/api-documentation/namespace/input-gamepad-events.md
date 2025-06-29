# Phaser.Input.Gamepad.Events

Scope:
static

> Source: [src/input/gamepad/events/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/events/index.js#L7)

# Static functions

## BUTTON\_DOWN

### BUTTON\_DOWN

**Description:**

The Gamepad Button Down Event.

This event is dispatched by the Gamepad Plugin when a button has been pressed on any active Gamepad.

Listen to this event from within a Scene using: `this.input.gamepad.on('down', listener)`.

You can also listen for a DOWN event from a Gamepad instance. See the [`GAMEPAD_BUTTON_DOWN`](Phaser.Input.Gamepad.Events.md) event for details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pad | [Phaser.Input.Gamepad](input-gamepad.md) | No | A reference to the Gamepad on which the button was pressed. |
| --- | --- | --- | --- |
| button | [Phaser.Input.Gamepad.Button](../class/input-gamepad-button.md) | No | A reference to the Button which was pressed. |
| value | number | No | The value of the button at the time it was pressed. Between 0 and 1. Some Gamepads have pressure-sensitive buttons. |

> Source: [src/input/gamepad/events/BUTTON\_DOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/events/BUTTON_DOWN_EVENT.js#L7)  
> Since: 3.10.0

---

## BUTTON\_UP

### BUTTON\_UP

**Description:**

The Gamepad Button Up Event.

This event is dispatched by the Gamepad Plugin when a button has been released on any active Gamepad.

Listen to this event from within a Scene using: `this.input.gamepad.on('up', listener)`.

You can also listen for an UP event from a Gamepad instance. See the [`GAMEPAD_BUTTON_UP`](Phaser.Input.Gamepad.Events.md) event for details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pad | [Phaser.Input.Gamepad](input-gamepad.md) | No | A reference to the Gamepad on which the button was released. |
| --- | --- | --- | --- |
| button | [Phaser.Input.Gamepad.Button](../class/input-gamepad-button.md) | No | A reference to the Button which was released. |
| value | number | No | The value of the button at the time it was released. Between 0 and 1. Some Gamepads have pressure-sensitive buttons. |

> Source: [src/input/gamepad/events/BUTTON\_UP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/events/BUTTON_UP_EVENT.js#L7)  
> Since: 3.10.0

---

## CONNECTED

### CONNECTED

**Description:**

The Gamepad Connected Event.

This event is dispatched by the Gamepad Plugin when a Gamepad has been connected.

Listen to this event from within a Scene using: `this.input.gamepad.once('connected', listener)`.

Note that the browser may require you to press a button on a gamepad before it will allow you to access it,

this is for security reasons. However, it may also trust the page already, in which case you won't get the

'connected' event and instead should check `GamepadPlugin.total` to see if it thinks there are any gamepads

already connected.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pad | [Phaser.Input.Gamepad](input-gamepad.md) | No | A reference to the Gamepad which was connected. |
| --- | --- | --- | --- |
| event | Event | No | The native DOM Event that triggered the connection. |

> Source: [src/input/gamepad/events/CONNECTED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/events/CONNECTED_EVENT.js#L7)  
> Since: 3.0.0

---

## DISCONNECTED

### DISCONNECTED

**Description:**

The Gamepad Disconnected Event.

This event is dispatched by the Gamepad Plugin when a Gamepad has been disconnected.

Listen to this event from within a Scene using: `this.input.gamepad.once('disconnected', listener)`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| pad | [Phaser.Input.Gamepad](input-gamepad.md) | No | A reference to the Gamepad which was disconnected. |
| --- | --- | --- | --- |
| event | Event | No | The native DOM Event that triggered the disconnection. |

> Source: [src/input/gamepad/events/DISCONNECTED\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/events/DISCONNECTED_EVENT.js#L7)  
> Since: 3.0.0

---

## GAMEPAD\_BUTTON\_DOWN

### GAMEPAD\_BUTTON\_DOWN

**Description:**

The Gamepad Button Down Event.

This event is dispatched by a Gamepad instance when a button has been pressed on it.

Listen to this event from a Gamepad instance. Once way to get this is from the `pad1`, `pad2`, etc properties on the Gamepad Plugin:

`this.input.gamepad.pad1.on('down', listener)`.

Note that you will not receive any Gamepad button events until the browser considers the Gamepad as being 'connected'.

You can also listen for a DOWN event from the Gamepad Plugin. See the [`BUTTON_DOWN`](Phaser.Input.Gamepad.Events.md) event for details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the button that was pressed. |
| --- | --- | --- | --- |
| value | number | No | The value of the button at the time it was pressed. Between 0 and 1. Some Gamepads have pressure-sensitive buttons. |
| button | [Phaser.Input.Gamepad.Button](../class/input-gamepad-button.md) | No | A reference to the Button which was pressed. |

> Source: [src/input/gamepad/events/GAMEPAD\_BUTTON\_DOWN\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/events/GAMEPAD_BUTTON_DOWN_EVENT.js#L7)  
> Since: 3.10.0

---

## GAMEPAD\_BUTTON\_UP

### GAMEPAD\_BUTTON\_UP

**Description:**

The Gamepad Button Up Event.

This event is dispatched by a Gamepad instance when a button has been released on it.

Listen to this event from a Gamepad instance. Once way to get this is from the `pad1`, `pad2`, etc properties on the Gamepad Plugin:

`this.input.gamepad.pad1.on('up', listener)`.

Note that you will not receive any Gamepad button events until the browser considers the Gamepad as being 'connected'.

You can also listen for an UP event from the Gamepad Plugin. See the [`BUTTON_UP`](Phaser.Input.Gamepad.Events.md) event for details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| index | number | No | The index of the button that was released. |
| --- | --- | --- | --- |
| value | number | No | The value of the button at the time it was released. Between 0 and 1. Some Gamepads have pressure-sensitive buttons. |
| button | [Phaser.Input.Gamepad.Button](../class/input-gamepad-button.md) | No | A reference to the Button which was released. |

> Source: [src/input/gamepad/events/GAMEPAD\_BUTTON\_UP\_EVENT.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/events/GAMEPAD_BUTTON_UP_EVENT.js#L7)  
> Since: 3.10.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [BUTTON\_DOWN](#button_down)

    - [BUTTON\_DOWN](#button_down-1)
  + [BUTTON\_UP](#button_up)

    - [BUTTON\_UP](#button_up-1)
  + [CONNECTED](#connected)

    - [CONNECTED](#connected-1)
  + [DISCONNECTED](#disconnected)

    - [DISCONNECTED](#disconnected-1)
  + [GAMEPAD\_BUTTON\_DOWN](#gamepad_button_down)

    - [GAMEPAD\_BUTTON\_DOWN](#gamepad_button_down-1)
  + [GAMEPAD\_BUTTON\_UP](#gamepad_button_up)

    - [GAMEPAD\_BUTTON\_UP](#gamepad_button_up-1)

Back to top

©2025[Phaser](https://docs.phaser.io)