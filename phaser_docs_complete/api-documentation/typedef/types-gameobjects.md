# Types.GameObjects

Phaser.Types.GameObjects

## DecomposeMatrixResults

### <static> DecomposeMatrixResults

| name | type | optional | description |
| --- | --- | --- | --- |
| translateX | number | No | The translated x value. |
| --- | --- | --- | --- |
| translateY | number | No | The translated y value. |
| rotation | number | No | The rotation value. |
| scaleX | number | No | The scale x value. |
| scaleY | number | No | The scale y value. |

**Type**: object

**Member of**: Phaser.Types.GameObjects

> Source: [src/gameobjects/typedefs/DecomposeMatrixResults.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/typedefs/DecomposeMatrixResults.js#L1)  
> Since: 3.60.0

---

## Face

### <static> Face

| name | type | optional | description |
| --- | --- | --- | --- |
| vertex1 | [Phaser.Types.GameObjects.Vertex](types-gameobjects.md) | No | The first face vertex. |
| --- | --- | --- | --- |
| vertex2 | [Phaser.Types.GameObjects.Vertex](types-gameobjects.md) | No | The second face vertex. |
| vertex3 | [Phaser.Types.GameObjects.Vertex](types-gameobjects.md) | No | The third face vertex. |
| isCounterClockwise | boolean | No | Are the vertices counter-clockwise? |

**Type**: object

**Member of**: Phaser.Types.GameObjects

> Source: [src/gameobjects/typedefs/Face.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/typedefs/Face.js#L1)  
> Since: 3.50.0

---

## GameObjectConfig

### <static> GameObjectConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| x | number | object | Yes | 0 | The x position of the Game Object. |
| --- | --- | --- | --- | --- |
| y | number | object | Yes | 0 | The y position of the Game Object. |
| depth | number | Yes | 0 | The depth of the GameObject. |
| flipX | boolean | Yes | false | The horizontally flipped state of the Game Object. |
| flipY | boolean | Yes | false | The vertically flipped state of the Game Object. |
| scale | number | object | Yes | null | The scale of the GameObject. |
| scrollFactor | number | object | Yes | null | The scroll factor of the GameObject. |
| rotation | number | object | Yes | 0 | The rotation angle of the Game Object, in radians. |
| angle | number | object | Yes | null | The rotation angle of the Game Object, in degrees. |
| alpha | number | object | Yes | 1 | The alpha (opacity) of the Game Object. |
| origin | number | object | Yes | null | The origin of the Game Object. |
| scaleMode | number | Yes | "ScaleModes.DEFAULT" | The scale mode of the GameObject. |
| blendMode | number | Yes | "BlendModes.DEFAULT" | The blend mode of the GameObject. |
| visible | boolean | Yes | true | The visible state of the Game Object. |
| add | boolean | Yes | true | Add the GameObject to the scene. |

**Type**: object

**Member of**: Phaser.Types.GameObjects

> Source: [src/gameobjects/typedefs/GameObjectConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/typedefs/GameObjectConfig.js#L1)  
> Since: 3.0.0

---

## GetCalcMatrixResults

### <static> GetCalcMatrixResults

| name | type | optional | description |
| --- | --- | --- | --- |
| camera | [Phaser.GameObjects.Components.TransformMatrix](../class/gameobjects-components-transformmatrix.md) | No | The calculated Camera matrix. |
| --- | --- | --- | --- |
| sprite | [Phaser.GameObjects.Components.TransformMatrix](../class/gameobjects-components-transformmatrix.md) | No | The calculated Sprite (Game Object) matrix. |
| calc | [Phaser.GameObjects.Components.TransformMatrix](../class/gameobjects-components-transformmatrix.md) | No | The calculated results matrix, factoring all others in. |

**Type**: object

**Member of**: Phaser.Types.GameObjects

> Source: [src/gameobjects/typedefs/GetCalcMatrixResults.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/typedefs/GetCalcMatrixResults.js#L1)  
> Since: 3.50.0

---

## JSONGameObject

### <static> JSONGameObject

| name | type | optional | description |
| --- | --- | --- | --- |
| name | string | No | The name of this Game Object. |
| --- | --- | --- | --- |
| type | string | No | A textual representation of this Game Object, i.e. `sprite`. |
| x | number | No | The x position of this Game Object. |
| y | number | No | The y position of this Game Object. |
| scale | object | No | The scale of this Game Object |
| scale.x | number | No | The horizontal scale of this Game Object. |
| scale.y | number | No | The vertical scale of this Game Object. |
| origin | object | No | The origin of this Game Object. |
| origin.x | number | No | The horizontal origin of this Game Object. |
| origin.y | number | No | The vertical origin of this Game Object. |
| flipX | boolean | No | The horizontally flipped state of the Game Object. |
| flipY | boolean | No | The vertically flipped state of the Game Object. |
| rotation | number | No | The angle of this Game Object in radians. |
| alpha | number | No | The alpha value of the Game Object. |
| visible | boolean | No | The visible state of the Game Object. |
| scaleMode | number | No | The Scale Mode being used by this Game Object. |
| blendMode | number | string | No | Sets the Blend Mode being used by this Game Object. |
| textureKey | string | No | The texture key of this Game Object. |
| frameKey | string | No | The frame key of this Game Object. |
| data | object | No | The data of this Game Object. |

**Type**: object

**Member of**: Phaser.Types.GameObjects

> Source: [src/gameobjects/typedefs/JSONGameObject.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/typedefs/JSONGameObject.js#L1)  
> Since: 3.0.0

---

## Vertex

### <static> Vertex

| name | type | optional | description |
| --- | --- | --- | --- |
| x | number | No | The x coordinate of the vertex. |
| --- | --- | --- | --- |
| y | number | No | The y coordinate of the vertex. |
| z | number | No | The z coordinate of the vertex. |
| normalX | number | No | The x normal of the vertex. |
| normalY | number | No | The y normal of the vertex. |
| normalZ | number | No | The z normal of the vertex. |
| u | number | No | UV u texture coordinate of the vertex. |
| v | number | No | UV v texture coordinate of the vertex. |
| alpha | number | No | The alpha value of the vertex. |

**Type**: object

**Member of**: Phaser.Types.GameObjects

> Source: [src/gameobjects/typedefs/Vertex.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/typedefs/Vertex.js#L1)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.GameObjects](#typesgameobjects)

  + [DecomposeMatrixResults](#decomposematrixresults)

    - [<static> DecomposeMatrixResults](#static-decomposematrixresults)
  + [Face](#face)

    - [<static> Face](#static-face)
  + [GameObjectConfig](#gameobjectconfig)

    - [<static> GameObjectConfig](#static-gameobjectconfig)
  + [GetCalcMatrixResults](#getcalcmatrixresults)

    - [<static> GetCalcMatrixResults](#static-getcalcmatrixresults)
  + [JSONGameObject](#jsongameobject)

    - [<static> JSONGameObject](#static-jsongameobject)
  + [Vertex](#vertex)

    - [<static> Vertex](#static-vertex)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.GameObjects