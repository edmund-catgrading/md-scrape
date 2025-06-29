# Phaser.Utils.String

Scope:
static

> Source: [src/utils/string/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/index.js#L7)

# Static functions

## Format

### <static> Format(string, values)

**Description:**

Takes a string and replaces instances of markers with values in the given array.

The markers take the form of `%1`, `%2`, etc. I.e.:

`Format("The %1 is worth %2 gold", [ 'Sword', 500 ])`

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| string | string | No | The string containing the replacement markers. |
| --- | --- | --- | --- |
| values | array | No | An array containing values that will replace the markers. If no value exists an empty string is inserted instead. |

**Returns:** string - The string containing replaced values.

> Source: [src/utils/string/Format.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/Format.js#L7)  
> Since: 3.0.0

---

## Pad

### <static> Pad(str, [len], [pad], [dir])

**Description:**

Takes the given string and pads it out, to the length required, using the character

specified. For example if you need a string to be 6 characters long, you can call:

`pad('bob', 6, '-', 2)`

This would return: `bob---` as it has padded it out to 6 characters, using the `-` on the right.

You can also use it to pad numbers (they are always returned as strings):

`pad(512, 6, '0', 1)`

Would return: `000512` with the string padded to the left.

If you don't specify a direction it'll pad to both sides:

`pad('c64', 7, '*')`

Would return: `**c64**`

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| str | string | number | object | No |  |
| --- | --- | --- | --- | --- |
| len | number | Yes | 0 | The number of characters to be added. |
| pad | string | Yes | "" "" | The string to pad it out with (defaults to a space). |
| dir | number | Yes | 3 | The direction dir = 1 (left), 2 (right), 3 (both). |

**Returns:** string - The padded string.

> Source: [src/utils/string/Pad.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/Pad.js#L7)  
> Since: 3.0.0

---

## RemoveAt

### <static> RemoveAt(string, index)

**Description:**

Takes a string and removes the character at the given index.

The index is zero based.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| string | string | No | The string to be worked on. |
| --- | --- | --- | --- |
| index | number | No | The index of the character to be removed. This value is zero-based. |

**Returns:** string - The modified string.

> Source: [src/utils/string/RemoveAt.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/RemoveAt.js#L7)  
> Since: 3.50.0

---

## Reverse

### <static> Reverse(string)

**Description:**

Takes the given string and reverses it, returning the reversed string.

For example if given the string `Atari 520ST` it would return `TS025 iratA`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| string | string | No | The string to be reversed. |
| --- | --- | --- | --- |

**Returns:** string - The reversed string.

> Source: [src/utils/string/Reverse.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/Reverse.js#L7)  
> Since: 3.0.0

---

## UppercaseFirst

### <static> UppercaseFirst(str)

**Description:**

Capitalizes the first letter of a string if there is one.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| str | string | No | The string to capitalize. |
| --- | --- | --- | --- |

**Returns:** string - A new string, same as the first, but with the first letter capitalized.

> Source: [src/utils/string/UppercaseFirst.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/UppercaseFirst.js#L7)  
> Since: 3.0.0

---

## UUID

### <static> UUID()

**Description:**

Creates and returns an RFC4122 version 4 compliant UUID.

The string is in the form: `xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx` where each `x` is replaced with a random

hexadecimal digit from 0 to f, and `y` is replaced with a random hexadecimal digit from 8 to b.

**Returns:** string - The UUID string.

> Source: [src/utils/string/UUID.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/string/UUID.js#L7)  
> Since: 3.12.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [Format](#format)

    - [<static> Format(string, values)](#static-formatstring-values)
  + [Pad](#pad)

    - [<static> Pad(str, [len], [pad], [dir])](#static-padstr-len-pad-dir)
  + [RemoveAt](#removeat)

    - [<static> RemoveAt(string, index)](#static-removeatstring-index)
  + [Reverse](#reverse)

    - [<static> Reverse(string)](#static-reversestring)
  + [UppercaseFirst](#uppercasefirst)

    - [<static> UppercaseFirst(str)](#static-uppercasefirststr)
  + [UUID](#uuid)

    - [<static> UUID()](#static-uuid)

Back to top

©2025[Phaser](https://docs.phaser.io)