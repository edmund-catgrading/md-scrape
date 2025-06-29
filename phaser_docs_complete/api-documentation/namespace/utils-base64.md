# Phaser.Utils.Base64

Scope:
static

> Source: [src/utils/base64/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/base64/index.js#L7)

# Static functions

## ArrayBufferToBase64

### <static> ArrayBufferToBase64(arrayBuffer, [mediaType])

**Description:**

Converts an ArrayBuffer into a base64 string.

The resulting string can optionally be a data uri if the `mediaType` argument is provided.

See <https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs> for more details.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| arrayBuffer | ArrayBuffer | No | The Array Buffer to encode. |
| --- | --- | --- | --- |
| mediaType | string | Yes | An optional media type, i.e. `audio/ogg` or `image/jpeg`. If included the resulting string will be a data URI. |

**Returns:** string - The base64 encoded Array Buffer.

> Source: [src/utils/base64/ArrayBufferToBase64.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/base64/ArrayBufferToBase64.js#L10)  
> Since: 3.18.0

---

## Base64ToArrayBuffer

### <static> Base64ToArrayBuffer(base64)

**Description:**

Converts a base64 string, either with or without a data uri, into an Array Buffer.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| base64 | string | No | The base64 string to be decoded. Can optionally contain a data URI header, which will be stripped out prior to decoding. |
| --- | --- | --- | --- |

**Returns:** ArrayBuffer - An ArrayBuffer decoded from the base64 data.

> Source: [src/utils/base64/Base64ToArrayBuffer.js#L18](https://github.com/phaserjs/phaser/blob/v3.87.0/src/utils/base64/Base64ToArrayBuffer.js#L18)  
> Since: 3.18.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [ArrayBufferToBase64](#arraybuffertobase64)

    - [<static> ArrayBufferToBase64(arrayBuffer, [mediaType])](#static-arraybuffertobase64arraybuffer-mediatype)
  + [Base64ToArrayBuffer](#base64toarraybuffer)

    - [<static> Base64ToArrayBuffer(base64)](#static-base64toarraybufferbase64)

Back to top

©2025[Phaser](https://docs.phaser.io)