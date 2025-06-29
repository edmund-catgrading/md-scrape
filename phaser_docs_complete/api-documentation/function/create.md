# Phaser.Create

## GenerateTexture

### <static> GenerateTexture(config)

**Description:**

Generates a texture based on the given Create configuration object.

The texture is drawn using a fixed-size indexed palette of 16 colors, where the hex value in the

data cells map to a single color. For example, if the texture config looked like this:

```
Copy
var star = [

  '.....828.....',

  '....72227....',

  '....82228....',

  '...7222227...',

  '2222222222222',

  '8222222222228',

  '.72222222227.',

  '..787777787..',

  '..877777778..',

  '.78778887787.',

  '.27887.78872.',

  '.787.....787.'

];



this.textures.generate('star', { data: star, pixelWidth: 4 });


```

Then it would generate a texture that is 52 x 48 pixels in size, because each cell of the data array

represents 1 pixel multiplied by the `pixelWidth` value. The cell values, such as `8`, maps to color

number 8 in the palette. If a cell contains a period character `.` then it is transparent.

The default palette is Arne16, but you can specify your own using the `palette` property.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Create.GenerateTextureConfig](../typedef/types-create.md) | No | The Generate Texture Configuration object. |
| --- | --- | --- | --- |

**Returns:** HTMLCanvasElement - An HTMLCanvasElement which contains the generated texture drawn to it.

> Source: [src/create/GenerateTexture.js#L11](https://github.com/phaserjs/phaser/blob/v3.87.0/src/create/GenerateTexture.js#L11)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.Create](#phasercreate)

  + [GenerateTexture](#generatetexture)

    - [<static> GenerateTexture(config)](#static-generatetextureconfig)

Back to top

©2025[Phaser](https://docs.phaser.io)