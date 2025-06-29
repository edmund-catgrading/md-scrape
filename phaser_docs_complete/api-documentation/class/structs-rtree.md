# RTree

Phaser.Structs.RTree

RBush is a high-performance JavaScript library for 2D spatial indexing of points and rectangles.

It's based on an optimized R-tree data structure with bulk insertion support.

Spatial index is a special data structure for points and rectangles that allows you to perform queries like

"all items within this bounding box" very efficiently (e.g. hundreds of times faster than looping over all items).

This version of RBush uses a fixed min/max accessor structure of `[ '.left', '.top', '.right', '.bottom' ]`.

This is to avoid the eval like function creation that the original library used, which caused CSP policy violations.

rbush is forked from <https://github.com/mourner/rbush> by Vladimir Agafonkin

**Scope**: static

> Source: [src/structs/RTree.js#L10](https://github.com/phaserjs/phaser/blob/v3.87.0/src/structs/RTree.js#L10)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [RTree](#rtree)

Back to top

©2025[Phaser](https://docs.phaser.io)