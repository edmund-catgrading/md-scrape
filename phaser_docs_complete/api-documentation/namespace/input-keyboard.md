# Phaser.Input.Keyboard

Scope:
static

> Source: [src/input/keyboard/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/index.js#L7)

# Static functions

* [Key](../class/input-keyboard-key.md)
* [KeyboardManager](../class/input-keyboard-keyboardmanager.md)
* [KeyboardPlugin](../class/input-keyboard-keyboardplugin.md)
* [KeyCombo](../class/input-keyboard-keycombo.md)

# Static functions

## DownDuration

### <static> DownDuration(key, [duration])

**Description:**

Returns `true` if the Key was pressed down within the `duration` value given, based on the current

game clock time. Or `false` if it either isn't down, or was pressed down longer ago than the given duration.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | No |  | The Key object to test. |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 50 | The duration, in ms, within which the key must have been pressed down. |

**Returns:** boolean - `true` if the Key was pressed down within `duration` ms ago, otherwise `false`.

> Source: [src/input/keyboard/keys/DownDuration.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/DownDuration.js#L7)  
> Since: 3.0.0

---

## JustDown

### <static> JustDown(key)

**Description:**

The justDown value allows you to test if this Key has just been pressed down or not.

When you check this value it will return `true` if the Key is down, otherwise `false`.

You can only call justDown once per key press. It will only return `true` once, until the Key is released and pressed down again.

This allows you to use it in situations where you want to check if this key is down without using an event, such as in a core game loop.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | No | The Key to check to see if it's just down or not. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the Key was just pressed, otherwise `false`.

> Source: [src/input/keyboard/keys/JustDown.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/JustDown.js#L7)  
> Since: 3.0.0

---

## JustUp

### <static> JustUp(key)

**Description:**

The justUp value allows you to test if this Key has just been released or not.

When you check this value it will return `true` if the Key is up, otherwise `false`.

You can only call JustUp once per key release. It will only return `true` once, until the Key is pressed down and released again.

This allows you to use it in situations where you want to check if this key is up without using an event, such as in a core game loop.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | No | The Key to check to see if it's just up or not. |
| --- | --- | --- | --- |

**Returns:** boolean - `true` if the Key was just released, otherwise `false`.

> Source: [src/input/keyboard/keys/JustUp.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/JustUp.js#L7)  
> Since: 3.0.0

---

## UpDuration

### <static> UpDuration(key, [duration])

**Description:**

Returns `true` if the Key was released within the `duration` value given, based on the current

game clock time. Or returns `false` if it either isn't up, or was released longer ago than the given duration.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | [Phaser.Input.Keyboard.Key](../class/input-keyboard-key.md) | No |  | The Key object to test. |
| --- | --- | --- | --- | --- |
| duration | number | Yes | 50 | The duration, in ms, within which the key must have been released. |

**Returns:** boolean - `true` if the Key was released within `duration` ms ago, otherwise `false`.

> Source: [src/input/keyboard/keys/UpDuration.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/keys/UpDuration.js#L7)  
> Since: 3.0.0

---

## AdvanceKeyCombo

### <static> AdvanceKeyCombo(event, combo)

**Description:**

Used internally by the KeyCombo class.

Return `true` if it reached the end of the combo, `false` if not.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native Keyboard Event. |
| --- | --- | --- | --- |
| combo | [Phaser.Input.Keyboard.KeyCombo](../class/input-keyboard-keycombo.md) | No | The KeyCombo object to advance. |

**Returns:** boolean - `true` if it reached the end of the combo, `false` if not.

> Source: [src/input/keyboard/combo/AdvanceKeyCombo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/combo/AdvanceKeyCombo.js#L7)  
> Since: 3.0.0

---

## ProcessKeyCombo

### <static> ProcessKeyCombo(event, combo)

**Description:**

Used internally by the KeyCombo class.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| event | KeyboardEvent | No | The native Keyboard Event. |
| --- | --- | --- | --- |
| combo | [Phaser.Input.Keyboard.KeyCombo](../class/input-keyboard-keycombo.md) | No | The KeyCombo object to be processed. |

**Returns:** boolean - `true` if the combo was matched, otherwise `false`.

> Source: [src/input/keyboard/combo/ProcessKeyCombo.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/combo/ProcessKeyCombo.js#L9)  
> Since: 3.0.0

---

## ResetKeyCombo

### <static> ResetKeyCombo(combo)

**Description:**

Used internally by the KeyCombo class.

**Access:** private

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| combo | [Phaser.Input.Keyboard.KeyCombo](../class/input-keyboard-keycombo.md) | No | The KeyCombo to reset. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Input.Keyboard.KeyCombo](../class/input-keyboard-keycombo.md) - The KeyCombo.

> Source: [src/input/keyboard/combo/ResetKeyCombo.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/input/keyboard/combo/ResetKeyCombo.js#L7)  
> Since: 3.0.0

---

# Static functions

* [Events](input-keyboard-events.md)
* [KeyCodes](input-keyboard-keycodes.md)

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)

  + [DownDuration](#downduration)

    - [<static> DownDuration(key, [duration])](#static-downdurationkey-duration)
  + [JustDown](#justdown)

    - [<static> JustDown(key)](#static-justdownkey)
  + [JustUp](#justup)

    - [<static> JustUp(key)](#static-justupkey)
  + [UpDuration](#upduration)

    - [<static> UpDuration(key, [duration])](#static-updurationkey-duration)
  + [AdvanceKeyCombo](#advancekeycombo)

    - [<static> AdvanceKeyCombo(event, combo)](#static-advancekeycomboevent-combo)
  + [ProcessKeyCombo](#processkeycombo)

    - [<static> ProcessKeyCombo(event, combo)](#static-processkeycomboevent-combo)
  + [ResetKeyCombo](#resetkeycombo)

    - [<static> ResetKeyCombo(combo)](#static-resetkeycombocombo)
* [Static functions](#static-functions-2)

Back to top

©2025[Phaser](https://docs.phaser.io)