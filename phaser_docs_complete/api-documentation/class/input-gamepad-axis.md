# Axis

Phaser.Input.Gamepad.Axis

Contains information about a specific Gamepad Axis.

Axis objects are created automatically by the Gamepad as they are needed.

**Constructor**

`new Axis(pad, index)`

**Parameters**

| name | type | optional | description |
| --- | --- | --- | --- |
| pad | [Phaser.Input.Gamepad.Gamepad](input-gamepad-gamepad.md) | No | A reference to the Gamepad that this Axis belongs to. |
| --- | --- | --- | --- |
| index | number | No | The index of this Axis. |

---

**Scope**: static

> Source: [src/input/gamepad/Axis.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Axis.js#L9)  
> Since: 3.0.0

# Public Members

## events

### events: [Phaser.Events.EventEmitter](events-eventemitter.md)

**Description:**

An event emitter to use to emit the axis events.

> Source: [src/input/gamepad/Axis.js#L37](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Axis.js#L37)  
> Since: 3.0.0

---

## index

### index: number

**Description:**

The index of this Axis.

> Source: [src/input/gamepad/Axis.js#L46](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Axis.js#L46)  
> Since: 3.0.0

---

## pad

### pad: [Phaser.Input.Gamepad.Gamepad](input-gamepad-gamepad.md)

**Description:**

A reference to the Gamepad that this Axis belongs to.

> Source: [src/input/gamepad/Axis.js#L28](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Axis.js#L28)  
> Since: 3.0.0

---

## threshold

### threshold: number

**Description:**

Movement tolerance threshold below which axis values are ignored in `getValue`.

> Source: [src/input/gamepad/Axis.js#L66](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Axis.js#L66)  
> Since: 3.0.0

---

## value

### value: number

**Description:**

The raw axis value, between -1 and 1 with 0 being dead center.

Use the method `getValue` to get a normalized value with the threshold applied.

> Source: [src/input/gamepad/Axis.js#L55](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Axis.js#L55)  
> Since: 3.0.0

---

# Public Methods

## destroy

### <instance> destroy()

**Description:**

Destroys this Axis instance and releases external references it holds.

> Source: [src/input/gamepad/Axis.js#L105](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Axis.js#L105)  
> Since: 3.10.0

---

## getValue

### <instance> getValue()

**Description:**

Applies the `threshold` value to the axis and returns it.

**Returns:** number - The axis value, adjusted for the movement threshold.

> Source: [src/input/gamepad/Axis.js#L92](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Axis.js#L92)  
> Since: 3.0.0

---

# Private Methods

## update

### <instance> update(value)

**Description:**

Internal update handler for this Axis.

Called automatically by the Gamepad as part of its update.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| value | number | No | The value of the axis movement. |
| --- | --- | --- | --- |

> Source: [src/input/gamepad/Axis.js#L77](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/gamepad/Axis.js#L77)  
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
  + [threshold](#threshold)

    - [threshold: number](#threshold-number)
  + [value](#value)

    - [value: number](#value-number)
* [Public Methods](#public-methods)

  + [destroy](#destroy)

    - [<instance> destroy()](#instance-destroy)
  + [getValue](#getvalue)

    - [<instance> getValue()](#instance-getvalue)
* [Private Methods](#private-methods)

  + [update](#update)

    - [<instance> update(value)](#instance-updatevalue)

Back to top

©2025[Phaser](https://docs.phaser.io)