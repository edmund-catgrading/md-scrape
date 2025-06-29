# Types.GameObjects.NineSlice

Phaser.Types.GameObjects.NineSlice

## NineSliceConfig

### <static> NineSliceConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| key | string | [Phaser.Textures.Texture](../class/textures-texture.md) | Yes |  | The key, or instance of the Texture this Game Object will use to render with, as stored in the Texture Manager. |
| --- | --- | --- | --- | --- |
| frame | string | number | Yes |  | An optional frame from the Texture this Game Object is rendering with. |
| width | number | Yes | 256 | The width of the Nine Slice Game Object. You can adjust the width post-creation. |
| height | number | Yes | 256 | The height of the Nine Slice Game Object. If this is a 3 slice object the height will be fixed to the height of the texture and cannot be changed. |
| leftWidth | number | Yes | 10 | The size of the left vertical column (A). |
| rightWidth | number | Yes | 10 | The size of the right vertical column (B). |
| topHeight | number | Yes | 0 | The size of the top horiztonal row (C). Set to zero or undefined to create a 3 slice object. |
| bottomHeight | number | Yes | 0 | The size of the bottom horiztonal row (D). Set to zero or undefined to create a 3 slice object. |

**Type**: object

**Member of**: Phaser.Types.GameObjects.NineSlice

> Source: [src/gameobjects/nineslice/typedefs/NineSliceConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/gameobjects/nineslice/typedefs/NineSliceConfig.js#L1)  
> Since: 3.60.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.GameObjects.NineSlice](#typesgameobjectsnineslice)

  + [NineSliceConfig](#ninesliceconfig)

    - [<static> NineSliceConfig](#static-ninesliceconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.GameObjects.NineSlice