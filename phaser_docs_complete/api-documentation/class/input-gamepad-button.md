# Button

Phaser.Input.Gamepad.Button

Contains information about a specific button on a Gamepad.

Button objects are created automatically by the Gamepad as they are needed.

**Constructor**

`new Button(pad, index)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| pad | [Phaser.Input.Gamepad.Gamepad](input-gamepad-gamepad.md) | No | A reference to the Gamepad that this Button belongs to. |
| --- | --- | --- | --- |
| index | number | No | The index of this Button. |

---

**Scope**: static

> Source: [src/input/gamepad/Button.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Button.js#L10)  
> Since: 3.0.0

# Public Members

## events

### events: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

An event emitter to use to emit the button events.

> Source: [src/input/gamepad/Button.js#L38](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Button.js#L38)  
> Since: 3.0.0

---

## index

### index: number

**Description:**

The index of this Button.

> Source: [src/input/gamepad/Button.js#L47](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Button.js#L47)  
> Since: 3.0.0

---

## pad

### pad: [Phaser.Input.Gamepad.Gamepad](input-gamepad-gamepad.md)

**Description:**

A reference to the Gamepad that this Button belongs to.

> Source: [src/input/gamepad/Button.js#L29](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Button.js#L29)  
> Since: 3.0.0

---

## pressed

### pressed: boolean

**Description:**

Is the Button being pressed down or not?

> Source: [src/input/gamepad/Button.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Button.js#L77)  
> Since: 3.0.0

---

## threshold

### threshold: number

**Description:**

Can be set for analogue buttons to enable a 'pressure' threshold,

before a button is considered as being 'pressed'.

> Source: [src/input/gamepad/Button.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Button.js#L66)  
> Since: 3.0.0

---

## value

### value: number

**Description:**

Between 0 and 1.

> Source: [src/input/gamepad/Button.js#L56](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Button.js#L56)  
> Since: 3.0.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this Button instance and releases external references it holds.

> Source: [src/input/gamepad/Button.js#L126](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Button.js#L126)  
> Since: 3.10.0

---

# Private Methods

## update

### <instance> update(value)

**Description:**

Internal update handler for this Button.

Called automatically by the Gamepad as part of its update.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value of the button. Between 0 and 1. |
| --- | --- | --- | --- |

**Fires:** [Phaser.Input.Gamepad.Events#event:BUTTON\_DOWN](../event/input-gamepad-events.md), [Phaser.Input.Gamepad.Events#event:BUTTON\_UP](../event/input-gamepad-events.md), [Phaser.Input.Gamepad.Events#event:GAMEPAD\_BUTTON\_DOWN](../event/input-gamepad-events.md), [Phaser.Input.Gamepad.Events#event:GAMEPAD\_BUTTON\_UP](../event/input-gamepad-events.md)

> Source: [src/input/gamepad/Button.js#L88](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Button.js#L88)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Public Members](#public-members)

  + [events](#events)

    - [events: Phaser.Events.EventEmitter](#events-phasereventseventemitter)
  + [index](#index)

    - [index: number](#index-number)
  + [pad](#pad)

    - [pad: Phaser.Input.Gamepad.Gamepad](#pad-phaserinputgamepadgamepad)
  + [pressed](#pressed)

    - [pressed: boolean](#pressed-boolean)
  + [threshold](#threshold)

    - [threshold: number](#threshold-number)
  + [value](#value)

    - [value: number](#value-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
* [Private Methods](#private-methods)

  + [update](#update)

    - [<instance> update(value)](#instance-updatevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)