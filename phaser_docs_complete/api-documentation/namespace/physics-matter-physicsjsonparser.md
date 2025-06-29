# Phaser.Physics.Matter.PhysicsJSONParser

Scope:
static

> Source: [src/physics/matter-js/PhysicsJSONParser.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/PhysicsJSONParser.js#L10)  
> Since: 3.22.0

# Static functions

## parseBody

### <static> parseBody(x, y, config, [options])

**Description:**

Parses a body element from the given JSON data.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal world location of the body. |
| --- | --- | --- | --- |
| y | number | No | The vertical world location of the body. |
| config | object | No | The body configuration data. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** MatterJS.BodyType - A Matter JS Body.

> Source: [src/physics/matter-js/PhysicsJSONParser.js#L53](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/PhysicsJSONParser.js#L53)  
> Since: 3.22.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [parseBody](#parsebody)

    - [<static> parseBody(x, y, config, [options])](#static-parsebodyx-y-config-options)

Back to top

©2025[Phaser](https://docs.phaser.io)