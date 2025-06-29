# Types.Create

Phaser.Types.Create

## GenerateTextureCallback

### <static> GenerateTextureCallback

**Type**: function

**Member of**: Phaser.Types.Create

> Source: [src/create/typedefs/GenerateTextureConfig.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/create/typedefs/GenerateTextureConfig.js#L1)  
> Since: 3.0.0

---

## GenerateTextureConfig

### <static> GenerateTextureConfig

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | array | Yes | "[]" | An array of data, where each row is a string of single values 0-9A-F, or the period character. |
| --- | --- | --- | --- | --- |
| canvas | HTMLCanvasElement | Yes | null | The HTML Canvas to draw the texture to. |
| palette | [Phaser.Types.Create.Palette](types-create.md) | Yes | "Arne16" | The indexed palette that the data cell values map to. |
| pixelWidth | number | Yes | 1 | The width of each 'pixel' in the generated texture. |
| pixelHeight | number | Yes | 1 | The height of each 'pixel' in the generated texture. |
| resizeCanvas | boolean | Yes | true | Should the canvas be resized before the texture is drawn? |
| clearCanvas | boolean | Yes | true | Should the canvas be cleared before the texture is drawn? |
| preRender | [Phaser.Types.Create.GenerateTextureCallback](types-create.md) | Yes |  | A callback to send the canvas to prior to the texture being drawn. |
| postRender | [Phaser.Types.Create.GenerateTextureCallback](types-create.md) | Yes |  | A callback to send the canvas to after the texture has been drawn. |

**Type**: object

**Member of**: Phaser.Types.Create

> Source: [src/create/typedefs/GenerateTextureConfig.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/create/typedefs/GenerateTextureConfig.js#L9)  
> Since: 3.0.0

---

## Palette

### <static> Palette

| name | type | optional | description |
| --- | --- | --- | --- |
| 0 | string | No | Color value 1. |
| --- | --- | --- | --- |
| 1 | string | No | Color value 2. |
| 2 | string | No | Color value 3. |
| 3 | string | No | Color value 4. |
| 4 | string | No | Color value 5. |
| 5 | string | No | Color value 6. |
| 6 | string | No | Color value 7. |
| 7 | string | No | Color value 8. |
| 8 | string | No | Color value 9. |
| 9 | string | No | Color value 10. |
| A | string | No | Color value 11. |
| B | string | No | Color value 12. |
| C | string | No | Color value 13. |
| D | string | No | Color value 14. |
| E | string | No | Color value 15. |
| F | string | No | Color value 16. |

**Type**: object

**Member of**: Phaser.Types.Create

> Source: [src/create/typedefs/Palette.js#L1](https://github.com/phaserjs/phaser/blob/v3.87.0/src/create/typedefs/Palette.js#L1)  
> Since: 3.0.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Types.Create](#typescreate)

  + [GenerateTextureCallback](#generatetexturecallback)

    - [<static> GenerateTextureCallback](#static-generatetexturecallback)
  + [GenerateTextureConfig](#generatetextureconfig)

    - [<static> GenerateTextureConfig](#static-generatetextureconfig)
  + [Palette](#palette)

    - [<static> Palette](#static-palette)

Back to top

©2025[Phaser](https://docs.phaser.io)



Types.Create