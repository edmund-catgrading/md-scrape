# Phaser.Geom.Mesh

Scope:
static

> Source: [src/geom/mesh/index.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/index.js#L7)

# Static functions

* [Face](../class/geom-mesh-face.md)
* [Vertex](../class/geom-mesh-vertex.md)

# Static functions

## GenerateGridVerts

### <static> GenerateGridVerts(config)

**Description:**

Creates a grid of vertices based on the given configuration object and optionally adds it to a Mesh.

The size of the grid is given in pixels. An example configuration may be:

`{ width: 256, height: 256, widthSegments: 2, heightSegments: 2, tile: true }`

This will create a grid 256 x 256 pixels in size, split into 2 x 2 segments, with

the texture tiling across the cells.

You can split the grid into segments both vertically and horizontally. This will

generate two faces per grid segment as a result.

The `tile` parameter allows you to control if the tile will repeat across the grid

segments, or be displayed in full.

If adding this grid to a Mesh you can offset the grid via the `x` and `y` properties.

UV coordinates are generated based on the given texture and frame in the config. For

example, no frame is given, the UVs will be in the range 0 to 1. If a frame is given,

such as from a texture atlas, the UVs will be generated within the range of that frame.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| config | [Phaser.Types.Geom.Mesh.GenerateGridConfig](../typedef/types-geom-mesh.md) | No | A Grid configuration object. |
| --- | --- | --- | --- |

**Returns:** [Phaser.Types.Geom.Mesh.GenerateGridVertsResult](../typedef/types-geom-mesh.md) - A Grid Result object, containing the generated vertices and indicies.

> Source: [src/geom/mesh/GenerateGridVerts.js#L17](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/GenerateGridVerts.js#L17)  
> Since: 3.50.0

---

## GenerateObjVerts

### <static> GenerateObjVerts(data, [mesh], [scale], [x], [y], [z], [rotateX], [rotateY], [rotateZ], [zIsUp])

**Description:**

This method will return an object containing Face and Vertex instances, generated

from the parsed triangulated OBJ Model data given to this function.

The obj data should have been parsed in advance via the ParseObj function:

```
Copy
var data = Phaser.Geom.Mesh.ParseObj(rawData, flipUV);



var results = GenerateObjVerts(data);


```

Alternatively, you can parse obj files loaded via the OBJFile loader:

```
Copy
preload ()

{

  this.load.obj('alien', 'assets/3d/alien.obj);

}



var results = GenerateObjVerts(this.cache.obj.get('alien));


```

Make sure your 3D package has triangulated the model data prior to exporting it.

You can use the data returned by this function to populate the vertices of a Mesh Game Object.

You may add multiple models to a single Mesh, although they will act as one when

moved or rotated. You can scale the model data, should it be too small (or large) to visualize.

You can also offset the model via the `x`, `y` and `z` parameters.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | [Phaser.Types.Geom.Mesh.OBJData](../typedef/types-geom-mesh.md) | No |  | The parsed OBJ model data. |
| --- | --- | --- | --- | --- |
| mesh | [Phaser.GameObjects.Mesh](../class/gameobjects-mesh.md) | Yes |  | An optional Mesh Game Object. If given, the generated Faces will be automatically added to this Mesh. Set to `null` to skip. |
| scale | number | Yes | 1 | An amount to scale the model data by. Use this if the model has exported too small, or large, to see. |
| x | number | Yes | 0 | Translate the model x position by this amount. |
| y | number | Yes | 0 | Translate the model y position by this amount. |
| z | number | Yes | 0 | Translate the model z position by this amount. |
| rotateX | number | Yes | 0 | Rotate the model on the x axis by this amount, in radians. |
| rotateY | number | Yes | 0 | Rotate the model on the y axis by this amount, in radians. |
| rotateZ | number | Yes | 0 | Rotate the model on the z axis by this amount, in radians. |
| zIsUp | boolean | Yes | true | Is the z axis up (true), or is y axis up (false)? |

**Returns:** [Phaser.Types.Geom.Mesh.GenerateVertsResult](../typedef/types-geom-mesh.md) - The parsed Face and Vertex objects.

> Source: [src/geom/mesh/GenerateObjVerts.js#L16](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/GenerateObjVerts.js#L16)  
> Since: 3.50.0

---

## GenerateVerts

### <static> GenerateVerts(vertices, uvs, [indicies], [containsZ], [normals], [colors], [alphas], [flipUV])

**Description:**

Generates a set of Face and Vertex objects by parsing the given data.

This method will take vertex data in one of two formats, based on the `containsZ` parameter.

If your vertex data are `x`, `y` pairs, then `containsZ` should be `false` (this is the default)

If your vertex data is groups of `x`, `y` and `z` values, then the `containsZ` parameter must be true.

The `uvs` parameter is a numeric array consisting of `u` and `v` pairs.

The `normals` parameter is a numeric array consisting of `x`, `y` vertex normal values and, if `containsZ` is true, `z` values as well.

The `indicies` parameter is an optional array that, if given, is an indexed list of vertices to be added.

The `colors` parameter is an optional array, or single value, that if given sets the color of each vertex created.

The `alphas` parameter is an optional array, or single value, that if given sets the alpha of each vertex created.

When providing indexed data it is assumed that *all* of the arrays are indexed, not just the vertices.

The following example will create a 256 x 256 sized quad using an index array:

```
Copy
const vertices = [

  -128, 128,

  128, 128,

  -128, -128,

  128, -128

];



const uvs = [

  0, 1,

  1, 1,

  0, 0,

  1, 0

];



const indices = [ 0, 2, 1, 2, 3, 1 ];



GenerateVerts(vertices, uvs, indicies);


```

If the data is not indexed, it's assumed that the arrays all contain sequential data.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| vertices | Array.<number> | No |  | The vertices array. Either `xy` pairs, or `xyz` if the `containsZ` parameter is `true`. |
| --- | --- | --- | --- | --- |
| uvs | Array.<number> | No |  | The UVs pairs array. |
| indicies | Array.<number> | Yes |  | Optional vertex indicies array. If you don't have one, pass `null` or an empty array. |
| containsZ | boolean | Yes | false | Does the vertices data include a `z` component? |
| normals | Array.<number> | Yes |  | Optional vertex normals array. If you don't have one, pass `null` or an empty array. |
| colors | number | Array.<number> | Yes | "0xffffff" | An array of colors, one per vertex, or a single color value applied to all vertices. |
| alphas | number | Array.<number> | Yes | 1 | An array of alpha values, one per vertex, or a single alpha value applied to all vertices. |
| flipUV | boolean | Yes | false | Flip the UV coordinates? |

**Returns:** [Phaser.Types.Geom.Mesh.GenerateVertsResult](../typedef/types-geom-mesh.md) - The parsed Face and Vertex objects.

> Source: [src/geom/mesh/GenerateVerts.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/GenerateVerts.js#L10)  
> Since: 3.50.0

---

## ParseObj

### <static> ParseObj(data, [flipUV])

**Description:**

Parses a Wavefront OBJ File, extracting the models from it and returning them in an array.

The model data *must* be triangulated for a Mesh Game Object to be able to render it.

**Parameters:**

| name | type | optional | default | description |
| --- | --- | --- | --- | --- |
| data | string | No |  | The OBJ File data as a raw string. |
| --- | --- | --- | --- | --- |
| flipUV | boolean | Yes | true | Flip the UV coordinates? |

**Returns:** [Phaser.Types.Geom.Mesh.OBJData](../typedef/types-geom-mesh.md) - The parsed model and material data.

> Source: [src/geom/mesh/ParseObj.js#L226](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/ParseObj.js#L226)  
> Since: 3.50.0

---

## ParseObjMaterial

### <static> ParseObjMaterial(mtl)

**Description:**

Takes a Wavefront Material file and extracts the diffuse reflectivity of the named

materials, converts them to integer color values and returns them.

This is used internally by the `addOBJ` and `addModel` methods, but is exposed for

public consumption as well.

Note this only works with diffuse values, specified in the `Kd r g b` format, where

`g` and `b` are optional, but `r` is required. It does not support spectral rfl files,

or any other material statement (such as `Ka` or `Ks`)

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| mtl | string | No | The OBJ MTL file as a raw string, i.e. loaded via `this.load.text`. |
| --- | --- | --- | --- |

**Returns:** object - The parsed material colors, where each property of the object matches the material name.

> Source: [src/geom/mesh/ParseObjMaterial.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/ParseObjMaterial.js#L9)  
> Since: 3.50.0

---

## RotateFace

### <static> RotateFace(face, angle, [cx], [cy])

**Description:**

Rotates the vertices of a Face to the given angle.

The actual vertex positions are adjusted, not their transformed positions.

Therefore, this updates the vertex data directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| face | [Phaser.Geom.Mesh.Face](../class/geom-mesh-face.md) | No | The Face to rotate. |
| --- | --- | --- | --- |
| angle | number | No | The angle to rotate to, in radians. |
| cx | number | Yes | An optional center of rotation. If not given, the Face in-center is used. |
| cy | number | Yes | An optional center of rotation. If not given, the Face in-center is used. |

> Source: [src/geom/mesh/RotateFace.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/geom/mesh/RotateFace.js#L7)  
> Since: 3.50.0

---

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Static functions](#static-functions)
* [Static functions](#static-functions-1)

  + [GenerateGridVerts](#generategridverts)

    - [<static> GenerateGridVerts(config)](#static-generategridvertsconfig)
  + [GenerateObjVerts](#generateobjverts)

    - [<static> GenerateObjVerts(data, [mesh], [scale], [x], [y], [z], [rotateX], [rotateY], [rotateZ], [zIsUp])](#static-generateobjvertsdata-mesh-scale-x-y-z-rotatex-rotatey-rotatez-zisup)
  + [GenerateVerts](#generateverts)

    - [<static> GenerateVerts(vertices, uvs, [indicies], [containsZ], [normals], [colors], [alphas], [flipUV])](#static-generatevertsvertices-uvs-indicies-containsz-normals-colors-alphas-flipuv)
  + [ParseObj](#parseobj)

    - [<static> ParseObj(data, [flipUV])](#static-parseobjdata-flipuv)
  + [ParseObjMaterial](#parseobjmaterial)

    - [<static> ParseObjMaterial(mtl)](#static-parseobjmaterialmtl)
  + [RotateFace](#rotateface)

    - [<static> RotateFace(face, angle, [cx], [cy])](#static-rotatefaceface-angle-cx-cy)

Back to top

©2025[Phaser](https://docs.phaser.io)