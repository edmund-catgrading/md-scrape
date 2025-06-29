# Phaser.Physics.Matter.PhysicsEditorParser

Scope:
static

> Source: [src/physics/matter-js/PhysicsEditorParser.js#L15](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/PhysicsEditorParser.js#L15)  
> Since: 3.10.0

# Static functions

## parseBody

### <static> parseBody(x, y, config, [options])

**Description:**

Parses a body element exported by PhysicsEditor.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The horizontal world location of the body. |
| --- | --- | --- | --- |
| y | number | No | The vertical world location of the body. |
| config | object | No | The body configuration and fixture (child body) definitions, as exported by PhysicsEditor. |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** MatterJS.BodyType - A compound Matter JS Body.

> Source: [src/physics/matter-js/PhysicsEditorParser.js#L24](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/PhysicsEditorParser.js#L24)  
> Since: 3.10.0

---

## parseFixture

### <static> parseFixture(fixtureConfig)

**Description:**

Parses an element of the "fixtures" list exported by PhysicsEditor

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| fixtureConfig | object | No | The fixture object to parse. |
| --- | --- | --- | --- |

**Returns:** Array.<MatterJS.BodyType> - - An array of Matter JS Bodies.

> Source: [src/physics/matter-js/PhysicsEditorParser.js#L70](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/PhysicsEditorParser.js#L70)  
> Since: 3.10.0

---

## parseVertices

### <static> parseVertices(vertexSets, [options])

**Description:**

Parses the "vertices" lists exported by PhysicsEditor.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| vertexSets | array | No | The vertex lists to parse. |
| --- | --- | --- | --- |
| options | [Phaser.Types.Physics.Matter.MatterBodyConfig](../typedef/types-physics-matter.md) | Yes | An optional Body configuration object that is used to set initial Body properties on creation. |

**Returns:** Array.<MatterJS.BodyType> - - An array of Matter JS Bodies.

> Source: [src/physics/matter-js/PhysicsEditorParser.js#L104](https://github.com/phaserjs/phaser/blob/v3.87.0/src/physics/matter-js/PhysicsEditorParser.js#L104)  
> Since: 3.10.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)

  + [parseBody](#parsebody)

    - [<static> parseBody(x, y, config, [options])](#static-parsebodyx-y-config-options)
  + [parseFixture](#parsefixture)

    - [<static> parseFixture(fixtureConfig)](#static-parsefixturefixtureconfig)
  + [parseVertices](#parsevertices)

    - [<static> parseVertices(vertexSets, [options])](#static-parseverticesvertexsets-options)

Back to top

©2025[Phaser](https://docs.phaser.io)