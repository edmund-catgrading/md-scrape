# Graphics

A Guide to the Phaser Graphics Game Object

A Graphics object is a way to draw primitive shapes to your game. Primitives include forms of geometry, such as Rectangles, Circles, and Polygons. They also include lines, arcs and curves. When you initially create a Graphics object it will be empty. To draw to it you must first specify a line style or fill style (or both), draw shapes using paths, and finally fill or stroke them.

```
Copygraphics.lineStyle(5, 0xff00ff, 1.0);
graphics.beginPath();
graphics.moveTo(100, 100);
graphics.lineTo(200, 200);
graphics.closePath();
graphics.strokePath();

```

There are also many helpful methods that draw and fill/stroke common shapes for you.

```
Copygraphics.lineStyle(5, 0xff00ff, 1.0);
graphics.fillStyle(0xffffff, 1.0);
graphics.fillRect(50, 50, 400, 200);
graphics.strokeRect(50, 50, 400, 200);

```

When a Graphics object is rendered it will render differently based on if the game is running under Canvas or WebGL. Under Canvas it will use the HTML Canvas context drawing operations to draw the path. Under WebGL the graphics data is decomposed into polygons. Both of these are expensive processes, especially with complex shapes.

If your Graphics object doesn't change much (or at all) once you've drawn your shape to it, then you will help performance by calling Phaser.GameObjects.Graphics#generateTexture. This will 'bake' the Graphics object into a Texture, and return it. You can then use this Texture for Sprites or other display objects. If your Graphics object updates frequently then you should avoid doing this, as it will constantly generate new textures, which will consume memory.

As you can tell, Graphics objects are a bit of a trade-off. While they are extremely useful, you need to be careful in their complexity and quantity of them in your game.

## Basic usage

### Add graphics object

```
Copyvar graphics = this.add.graphics();

```

or

```
Copyvar graphics = this.add.graphics({
  x: 0,
  y: 0,

  // lineStyle: {
  //     width: 1,
  //     color: 0xffffff,
  //     alpha: 1
  // },
  // fillStyle: {
  //     color: 0xffffff,
  //     alpha: 1
  // },

  add: true,
});

```

### Custom class

* Define class

  ```
  Copyclass MyGraphics extends Phaser.GameObjects.Graphics {
    constructor(scene, options) {
      super(scene, options);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar graphics = new MyGraphics(this, options);

  ```

## Drawing commands

### Set line and fill style

* Set default line style and fill style

  ```
  Copygraphics.setDefaultStyles({
    lineStyle: {
      width: 1,
      color: 0xffffff,
      alpha: 1,
    },
    fillStyle: {
      color: 0xffffff,
      alpha: 1,
    },
  });

  ```
* Set line style

  ```
  Copygraphics.lineStyle(lineWidth, color, alpha); // color: 0xRRGGBB

  ```
* Set fill style

  + Fill color

    ```
    Copygraphics.fillStyle(color, alpha); // color: 0xRRGGBB

    ```
  + Fill gradient color (WebGL only)

    ```
    Copygraphics.fillGradientStyle(
      topLeft,
      topRight,
      bottomLeft,
      bottomRight,
      alpha
    ); // alpha= 1
    // graphics.fillGradientStyle(topLeft, topRight, bottomLeft, bottomRight, alphaTopLeft, alphaTopRight, alphaBottomLeft, alphaBottomRight);

    ```

    - `topLeft` : The tint being applied to the top-left of the Game Object.
    - `topRight` : The tint being applied to the top-right of the Game Object.
    - `bottomLeft` : The tint being applied to the bottom-left of the Game Object.
    - `bottomRight` : The tint being applied to the bottom-right of the Game Object.
    - `alphaTopLeft` : The top left alpha value.
    - `alphaTopRight` : The top right alpha value.
    - `alphaBottomLeft` : The bottom left alpha value.
    - `alphaBottomRight` : The bottom right alpha value.

### Clear/Erase all drawings

```
Copygraphics.clear();

```

### Drawing paths

```
Copygraphics.beginPath();
graphics.closePath();
graphics.fillPath(); // = graphics.fill()
graphics.strokePath(); // = graphics.stroke()

```

### Drawing rectangles

```
Copygraphics.fillRectShape(rect); // rect: {x, y, width, height}
graphics.fillRect(x, y, width, height);
graphics.strokeRectShape(rect); // rect: {x, y, width, height}
graphics.strokeRect(x, y, width, height);

```

### Drawing rounded rectangles

```
Copygraphics.fillRoundedRect(x, y, width, height, radius);
graphics.strokeRoundedRect(x, y, width, height, radius);

```

* `radius` : number or an object `{tl, tr, bl, br}`,
  + Positive value : Convex corner.
  + Negative value : Concave corner.

### Drawing triangles

```
Copygraphics.fillTriangleShape(triangle); // triangle: {x1, y1, x2, y2, x3, y3}
graphics.fillTriangle(x1, y1, x2, y2, x3, y3);
graphics.strokeTriangleShape(triangle); // triangle: {x1, y1, x2, y2, x3, y3}
graphics.strokeTriangle(x1, y1, x2, y2, x3, y3);

```

### Drawing points

```
Copygraphics.fillPointShape(point, size); // point: {x, y}
graphics.fillPoint(x, y, size);

```

### Drawing lines

```
Copygraphics.strokeLineShape(line); // line: {x1, y1, x2, y2}
graphics.lineBetween(x1, y1, x2, y2);
graphics.lineTo(x, y);
graphics.moveTo(x, y);

```

### Drawing a series of lines

```
Copygraphics.strokePoints(points, closeShape, closePath, endIndex); // points: [{x, y}, ...]
graphics.fillPoints(points, closeShape, closePath, endIndex); // points: [{x, y}, ...]

```

* `points` : Array of `{x, y}`
* `closeShape` : When `true`, the shape is closed by joining the last point to the first point.
* `closePath` : When `true`, the path is closed before being stroked.
* `endIndex` : The index of `points` to stop drawing at. Defaults to `points.length`.

### Drawing circles

```
Copygraphics.fillCircleShape(circle); // circle: {x, y, radius}
graphics.fillCircle(x, y, radius);
graphics.strokeCircleShape(circle); // circle: {x, y, radius}
graphics.strokeCircle(x, y, radius);

```

Draw or fill circle shape by points.

### Drawing ellipses

```
Copygraphics.strokeEllipseShape(ellipse, smoothness); // ellipse: Phaser.Geom.Ellipse
graphics.strokeEllipse(x, y, width, height, smoothness);
graphics.fillEllipseShape(ellipse, smoothness); // ellipse: Phaser.Geom.Ellipse
graphics.fillEllipse(x, y, width, height, smoothness);

```

Draw or fill ellipse shape by points.

### Drawing arcs

```
Copygraphics.arc(x, y, radius, startAngle, endAngle, anticlockwise);
graphics.arc(x, y, radius, startAngle, endAngle, anticlockwise, overshoot);

```

Draw arc curve by points.

### Drawing pie-chart slices

```
Copygraphics.slice(x, y, radius, startAngle, endAngle, anticlockwise);
graphics.slice(x, y, radius, startAngle, endAngle, anticlockwise, overshoot);

```

Draw pie-chart slice shape by points.

Fill this shape

```
Copygraphics.fillPath();

```

### Clear pattern

```
Copygraphics.setTexture();

```

### Transfer

```
Copygraphics.save();
graphics.restore();
graphics.translateCanvas(x, y);
graphics.scaleCanvas(x, y);
graphics.rotateCanvas(radians);

```

### Generate texture

```
Copygraphics.generateTexture(key, width, height); // key: texture key

```

### Create mask

```
Copyvar mask = graphics.createGeometryMask();

```

## Shapes

### Arc

Draws an arc shape. You can control the start and end angles of the arc, as well as if the angles are winding clockwise or anti-clockwise. The default settings renders a complete circle.

#### Create shape

```
Copyvar arc = this.add.arc(
  x,
  y,
  radius,
  startAngle,
  endAngle,
  anticlockwise,
  fillColor
);
// var arc = this.add.arc(x, y, radius, startAngle, endAngle, anticlockwise, fillColor, fillAlpha);

```

#### Custom class

* Define class

  ```
  Copyclass MyArc extends Phaser.GameObjects.Arc {
    constructor(
      scene,
      x,
      y,
      radius,
      startAngle,
      endAngle,
      anticlockwise,
      fillColor
    ) {
      super(
        scene,
        x,
        y,
        radius,
        startAngle,
        endAngle,
        anticlockwise,
        fillColor
      );
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar arc = new MyArc(
    scene,
    x,
    y,
    radius,
    startAngle,
    endAngle,
    anticlockwise,
    fillColor
  );

  ```

#### Color

* Fill color

  + Get

    ```
    Copyvar color = arc.fillColor;
    var alpha = arc.fillAlpha;

    ```
  + Set

    ```
    Copyarc.setFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copyarc.setFillStyle();

    ```
* Stroke color

  + Get

    ```
    Copyvar color = arc.strokeColor;

    ```
  + Set

    ```
    Copyarc.setStrokeStyle(lineWidth, color, alpha);

    ```
  + Clear

    ```
    Copyarc.setStrokeStyle();

    ```

!!! warning "No tint methods"
Uses `arc.setFillStyle(color, alpha)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = arc.alpha;

  ```
* Set

  ```
  Copyarc.setAlpha(alpha);
  // arc.alpha = alpha;

  ```

#### Angle

* Start angle, in degrees.

  + Get

    ```
    Copyvar startAngle = arc.startAngle;

    ```
  + Set

    ```
    Copyarc.setStartAngle(startAngle);
    // arc.setStartAngle(startAngle, anticlockwise);

    ```

    or

    ```
    Copyarc.startAngle = startAngle;

    ```
* End angle, in degrees.

  + Get

    ```
    Copyvar endAngle = arc.endAngle;

    ```
  + Set

    ```
    Copyarc.seEndAngle(endAngle);

    ```

    or

    ```
    Copyarc.endAngle = endAngle;

    ```
* Anticlockwise (`true`, or `false`)

  + Get

    ```
    Copyvar anticlockwise = arc.anticlockwise;

    ```
  + Set

    ```
    Copyarc.anticlockwise = anticlockwise;

    ```

#### Radius

* Get

  ```
  Copyvar radius = arc.radius;

  ```
* Set

  ```
  Copyarc.setRadius(radius);

  ```

or

```
Copyarc.radius = radius;

```

#### Smoother arcs

Increase this value for smoother arcs, at the cost of more polygons being rendered. Default is `0.01`

* Get

  ```
  Copyvar iterations = arc.iterations;

  ```
* Set

  ```
  Copyarc.iterations = iterations;

  ```

#### Display size

* Get

  ```
  Copyvar width = arc.displayWidth;
  var height = arc.displayHeight;

  ```
* Set

  ```
  Copyarc.setDisplaySize(width, height);

  ```

  or

  ```
  Copyarc.displayWidth = width;
  arc.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = arc.createGeometryMask();

```

### Circle

Draws a circle shape.

#### Create shape object

```
Copyvar circle = this.add.circle(x, y, radius, fillColor);
// var circle = this.add.circle(x, y, radius, fillColor, fillAlpha);

```

#### Custom class

* Define class

  ```
  Copyclass MyCircle extends Phaser.GameObjects.Arc {
    constructor(scene, x, y, radius, fillColor, fillAlpha) {
      super(scene, x, y, radius, 0, 360, false, fillColor, fillAlpha);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar circle = new MyCircle(scene, x, y, radius, fillColor, fillAlpha);

  ```

#### Color

* Fill color

  + Get

    ```
    Copyvar color = circle.fillColor;
    var alpha = circle.fillAlpha;

    ```
  + Set

    ```
    Copycircle.setFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copycircle.setFillStyle();

    ```
* Stroke color

  + Get

    ```
    Copyvar color = circle.strokeColor;

    ```
  + Set

    ```
    Copycircle.setStrokeStyle(lineWidth, color, alpha);

    ```
  + Clear

    ```
    Copycircle.setStrokeStyle();

    ```

!!! warning "No tint methods"
Uses `circle.setFillStyle(color, alpha)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = circle.alpha;

  ```
* Set

  ```
  Copycircle.setAlpha(alpha);
  // circle.alpha = alpha;

  ```

#### Radius

* Radius

  + Get

    ```
    Copyvar radius = circle.radius;

    ```
  + Set

    ```
    Copycircle.setRadius(radius);

    ```

    or

    ```
    Copycircle.radius = radius;

    ```

#### Smoother arcs

Increase this value for smoother arcs, at the cost of more polygons being rendered. Default is `0.01`

* Get

  ```
  Copyvar iterations = circle.iterations;

  ```
* Set

  ```
  Copycircle.iterations = iterations;

  ```

#### Display size

* Get

  ```
  Copyvar width = circle.displayWidth;
  var height = circle.displayHeight;

  ```
* Set

  ```
  Copycircle.setDisplaySize(width, height);

  ```

  or

  ```
  Copycircle.displayWidth = width;
  circle.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = circle.createGeometryMask();

```

### Curve

Draw a curve shape.

#### Create shape object

```
Copyvar curve = this.add.curve(x, y, path, fillColor);
// var curve = this.add.curve(x, y, path, fillColor, fillAlpha);

```

* `path` : [Path object](../math.md).

#### Custom class

* Define class

  ```
  Copyclass MyCurve extends Phaser.GameObjects.Curve {
    constructor(scene, x, y, path, fillColor, fillAlpha) {
      super(scene, x, y, path, fillColor, fillAlpha);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar curve = new MyCurve(scene, x, y, path, fillColor, fillAlpha);

  ```

#### Color

* Fill color

  + Get

    ```
    Copyvar color = curve.fillColor;
    var alpha = curve.fillAlpha;

    ```
  + Set

    ```
    Copycurve.setFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copycurve.setFillStyle();

    ```
* Stroke color

  + Get

    ```
    Copyvar color = curve.strokeColor;

    ```
  + Set

    ```
    Copycurve.setStrokeStyle(lineWidth, color, alpha);

    ```
  + Clear

    ```
    Copycurve.setStrokeStyle();

    ```

!!! warning "No tint methods"
Uses `curve.setFillStyle(color, alpha)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = curve.alpha;

  ```
* Set

  ```
  Copycurve.setAlpha(alpha);
  // curve.alpha = alpha;

  ```

#### Smoothness

The number of points used when rendering it. Increase this value for smoother curves, at the cost of more polygons being rendered.

```
Copycurve.setSmoothness(smoothness);

```

or

```
Copycurve.smoothness = smoothness;

```

#### Display size

* Get

  ```
  Copyvar width = curve.displayWidth;
  var height = curve.displayHeight;

  ```
* Set

  ```
  Copycurve.setDisplaySize(width, height);

  ```

  or

  ```
  Copycurve.displayWidth = width;
  curve.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = curve.createGeometryMask();

```

### Ellipse

Draw an ellipse shape.

#### Create shape object

```
Copyvar ellipse = this.add.ellipse(x, y, width, height, fillColor);
// var ellipse = this.add.ellipse(x, y, width, height, fillColor, fillAlpha);

```

#### Custom class

* Define class

  ```
  Copyclass MyEllipse extends Phaser.GameObjects.Ellipse {
    constructor(scene, x, y, width, height, fillColor, fillAlpha) {
      super(scene, x, y, width, height, fillColor, fillAlpha);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar ellipse = new MyEllipse(scene, x, y, width, height, fillColor, fillAlpha);

  ```

#### Color

* Fill color

  + Get

    ```
    Copyvar color = ellipse.fillColor;
    var alpha = ellipse.fillAlpha;

    ```
  + Set

    ```
    Copyellipse.setFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copyellipse.setFillStyle();

    ```
* Stroke color

  + Get

    ```
    Copyvar color = ellipse.strokeColor;

    ```
  + Set

    ```
    Copyellipse.setStrokeStyle(lineWidth, color, alpha);

    ```
  + Clear

    ```
    Copyellipse.setStrokeStyle();

    ```

!!! warning "No tint methods"
Uses `ellipse.setFillStyle(color, alpha)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = ellipse.alpha;

  ```
* Set

  ```
  Copyellipse.setAlpha(alpha);
  // ellipse.alpha = alpha;

  ```

#### Size

* Get

  ```
  Copyvar width = ellipse.width;
  var height = ellipse.height;

  ```
* Set

  ```
  Copyellipse.setSize(width, height);

  ```

#### Display size

* Get

  ```
  Copyvar width = ellipse.displayWidth;
  var height = ellipse.displayHeight;

  ```
* Set

  ```
  Copyellipse.setDisplaySize(width, height);

  ```

  or

  ```
  Copyellipse.displayWidth = width;
  ellipse.displayHeight = height;

  ```

#### Smoothness

The number of points used when rendering it. Increase this value for smoother curves, at the cost of more polygons being rendered.

```
Copyellipse.setSmoothness(smoothness);

```

or

```
Copyellipse.smoothness = smoothness;

```

#### Create mask

```
Copyvar mask = ellipse.createGeometryMask();

```

### Grid

Draw a grid shape.

#### Create shape object

```
Copyvar grid = this.add.grid(
  x,
  y,
  width,
  height,
  cellWidth,
  cellHeight,
  fillColor,
  fillAlpha,
  outlineFillColor,
  outlineFillAlpha
);

```

#### Custom class

* Define class

  ```
  Copyclass MyGrid extends Phaser.GameObjects.Grid {
    constructor(
      scene,
      x,
      y,
      width,
      height,
      cellWidth,
      cellHeight,
      fillColor,
      fillAlpha,
      outlineFillColor,
      outlineFillAlpha
    ) {
      super(
        scene,
        x,
        y,
        width,
        height,
        cellWidth,
        cellHeight,
        fillColor,
        fillAlpha,
        outlineFillColor,
        outlineFillAlpha
      );
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar grid = new MyGrid(
    scene,
    x,
    y,
    width,
    height,
    cellWidth,
    cellHeight,
    fillColor,
    fillAlpha,
    outlineFillColor,
    outlineFillAlpha
  );

  ```

#### Color

* Fill color

  + Get

    ```
    Copyvar color = grid.fillColor;
    var alpha = grid.fillAlpha;

    ```
  + Set

    ```
    Copygrid.setFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copygrid.setFillStyle();

    ```
* Stroke color

  + Get

    ```
    Copyvar color = grid.strokeColor;

    ```
  + Set

    ```
    Copygrid.setStrokeStyle(lineWidth, color, alpha);

    ```
  + Clear

    ```
    Copygrid.setStrokeStyle();

    ```
* Alternating color

  + Get

    ```
    Copyvar color = grid.altFillColor;

    ```
  + Set

    ```
    Copygrid.setAltFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copygrid.setAltFillStyle();

    ```
* Outline color

  + Get

    ```
    Copyvar color = grid.outlineFillColor;

    ```
  + Set

    ```
    Copygrid.setOutlineStyle(color, alpha;

    ```
  + Clear

    ```
    Copygrid.setOutlineStyle();

    ```

!!! warning "No tint methods"
Uses `grid.setFillStyle(color, alpha)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = grid.alpha;

  ```
* Set

  ```
  Copygrid.setAlpha(alpha);
  // grid.alpha = alpha;

  ```

#### Display size

* Get

  ```
  Copyvar width = grid.displayWidth;
  var height = grid.displayHeight;

  ```
* Set

  ```
  Copygrid.setDisplaySize(width, height);

  ```

  or

  ```
  Copygrid.displayWidth = width;
  grid.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = grid.createGeometryMask();

```

### IsoBox

An IsoBox is an 'isometric' rectangle. Each face of it has a different fill color. You can set the color of the top, left and right faces of the rectangle respectively. You can also choose which of the faces are rendered via the `showTop`, `showLeft` and `showRight` properties.

You cannot view an IsoBox from under-neath, however you can change the 'angle' by setting the `projection` property.

#### Create shape object

```
Copyvar isoBox = this.add.isobox(
  x,
  y,
  width,
  height,
  fillTop,
  fillLeft,
  fillRight
);

```

#### Custom class

* Define class

  ```
  Copyclass MyIsoBox extends Phaser.GameObjects.IsoBox {
    constructor(scene, x, y, width, height, fillTop, fillLeft, fillRight) {
      super(scene, x, y, width, height, fillTop, fillLeft, fillRight);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar isoBox = new MyIsoBox(
    scene,
    x,
    y,
    width,
    height,
    fillTop,
    fillLeft,
    fillRight
  );

  ```

#### Set color

* Fill color

  ```
  CopyisoBox.setFillStyle(fillTop, fillLeft, fillRight);

  ```
* Show face

  ```
  CopyisoBox.setFaces(showTop, showLeft, showRight);

  ```

  + `showTop`, `showLeft`, `showRight`: Set `true` to show that face

!!! warning "No tint methods"
Uses `isoBox.setFillStyle(fillTop, fillLeft, fillRight)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = isoBox.alpha;

  ```
* Set

  ```
  CopyisoBox.setAlpha(alpha);
  // isoBox.alpha = alpha;

  ```

#### Projection

The `projection` level of the iso box. Change this to change the 'angle' at which you are looking at the box.

* Get

  ```
  Copyvar projection = isoBox.projection;

  ```
* Set

  ```
  CopyisoBox.setProjection(value);

  ```

  or

  ```
  CopyisoBox.projection = value;

  ```

#### Display size

* Get

  ```
  Copyvar width = isoBox.displayWidth;
  var height = isoBox.displayHeight;

  ```
* Set

  ```
  CopyisoBox.setDisplaySize(width, height);

  ```

  or

  ```
  CopyisoBox.displayWidth = width;
  isoBox.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = isoBox.createGeometryMask();

```

### IsoTriangle

An IsoTriangle is an 'isometric' triangle. Think of it like a pyramid. Each face has a different fill color. You can set the color of the top, left and right faces of the triangle respectively You can also choose which of the faces are rendered via the `showTop`, `showLeft` and `showRight` properties.

You cannot view an IsoTriangle from under-neath, however you can change the 'angle' by setting the `projection` property. The `reversed` property controls if the IsoTriangle is rendered upside down or not.

#### Create shape object

```
Copyvar isoTriangle = this.add.isotriangle(
  x,
  y,
  width,
  height,
  reversed,
  fillTop,
  fillLeft,
  fillRight
);

```

#### Custom class

* Define class

  ```
  Copyclass MyIsoTriangle extends Phaser.GameObjects.IsoTriangle {
    constructor(
      scene,
      x,
      y,
      width,
      height,
      reversed,
      fillTop,
      fillLeft,
      fillRight
    ) {
      super(scene, x, y, width, height, reversed, fillTop, fillLeft, fillRight);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar isoTriangle = new MyIsoTriangle(
    scene,
    x,
    y,
    width,
    height,
    reversed,
    fillTop,
    fillLeft,
    fillRight
  );

  ```

#### Set color

* Fill color

  ```
  CopyisoTriangle.setFillStyle(fillTop, fillLeft, fillRight);

  ```
* Show face

  ```
  CopyisoTriangle.setFaces(showTop, showLeft, showRight);

  ```

  + `showTop`, `showLeft`, `showRight`: Set `true` to show that face

!!! warning "No tint methods"
Uses `isoTriangle.setFillStyle(fillTop, fillLeft, fillRight)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = isoTriangle.alpha;

  ```
* Set

  ```
  CopyisoTriangle.setAlpha(alpha);
  // isoTriangle.alpha = alpha;

  ```

#### Projection

The `projection` level of the iso box. Change this to change the 'angle' at which you are looking at the box.

* Get

  ```
  Copyvar projection = isoTriangle.projection;

  ```
* Set

  ```
  CopyisoTriangle.setProjection(value);

  ```

  or

  ```
  CopyisoTriangle.projection = value;

  ```

#### Reverse

* Get

  ```
  Copyvar isReversed = isoTriangle.isReversed;

  ```
* Set

  ```
  CopyisoTriangle.setReversed(reversed);

  ```

  or

  ```
  CopyisoTriangle.reversed = reversed;

  ```

  + Set `true` to render upside down.

#### Display size

* Get

  ```
  Copyvar width = isoTriangle.displayWidth;
  var height = isoTriangle.displayHeight;

  ```
* Set

  ```
  CopyisoTriangle.setDisplaySize(width, height);

  ```

  or

  ```
  CopyisoTriangle.displayWidth = width;
  isoTriangle.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = isoTriangle.createGeometryMask();

```

### Line

A Line Shape allows you to draw a line between two points in your game. You can control the stroke color and thickness of the line. In WebGL only you can also specify a different thickness for the start and end of the line, allowing you to render lines that taper-off.

If you need to draw multiple lines in a sequence you may wish to use the [Polygon Shape](#polygon) instead.

#### Create shape object

```
Copyvar line = this.add.line(x, y, x1, y1, x2, y2, strokeColor);
// var line = this.add.line(x, y, x1, y1, x2, y2, strokeColor, strokeAlpha);

```

#### Custom class

* Define class

  ```
  Copyclass MyCurve extends Phaser.GameObjects.Line {
    constructor(scene, x, y, x1, y1, x2, y2, strokeColor) {
      super(scene, x, y, x1, y1, x2, y2, strokeColor);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar line = new MyLine(scene, x, y, x1, y1, x2, y2, strokeColor);

  ```

#### Set color

* Fill color

  + Get

    ```
    Copyvar color = line.fillColor;
    var alpha = line.fillAlpha;

    ```
  + Set

    ```
    Copyline.setFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copyline.setFillStyle();

    ```
* Stroke color

  + Get

    ```
    Copyvar color = line.strokeColor;

    ```
  + Set

    ```
    Copyline.setStrokeStyle(lineWidth, color, alpha);

    ```
  + Clear

    ```
    Copyline.setStrokeStyle();

    ```

!!! warning "No tint methods"
Uses `line.setFillStyle(color, alpha)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = line.alpha;

  ```
* Set

  ```
  Copyline.setAlpha(alpha);
  // line.alpha = alpha;

  ```

#### Set end points

```
Copyline.setTo(x1, y1, x2, y2);

```

#### Line width

```
Copyline.setLineWidth(startWidth, endWidth);

```

* `endWidth` : The end width of the line. Only used in WebGL.

#### Display size

* Get

  ```
  Copyvar width = line.displayWidth;
  var height = line.displayHeight;

  ```
* Set

  ```
  Copyline.setDisplaySize(width, height);

  ```

  or

  ```
  Copyline.displayWidth = width;
  line.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = line.createGeometryMask();

```

### Polygon

The Polygon Shape is created by providing a list of points, which are then used to create an internal Polygon geometry object. The points can be set from a variety of formats:

* A string containing paired values separated by a single space: `'40 0 40 20 100 20 100 80 40 80 40 100 0 50'`
* An array of Point or Vector2 objects: `[new Phaser.Math.Vector2(x1, y1), ...]`
* An array of objects with public x/y properties: `[obj1, obj2, ...]`
* An array of paired numbers that represent point coordinates: `[x1,y1, x2,y2, ...]`
* An array of arrays with two elements representing x/y coordinates: `[[x1, y1], [x2, y2], ...]`

By default the `x` and `y` coordinates of this Shape refer to the center of it. However, depending on the coordinates of the points provided, the final shape may be rendered offset from its origin.

Note: The method `getBounds` will return incorrect bounds if any of the points in the Polygon are negative. If this is the case, please use the function `Phaser.Geom.Polygon.GetAABB(polygon.geom)` instead and then adjust the returned Rectangle position accordingly.

#### Create shape object

```
Copyvar polygon = this.add.polygon(x, y, points, fillColor);
// var polygon = this.add.polygon(x, y, points, fillColor, fillAlpha);

```

* `points` :
  + An array of number : `[x0, y0, x1, y1, ...]`
  + An array of points : `[{x:x0, y:y0}, {x:x1, y:y1}, ...]`
  + A string : `'x0 y0 x1 y1 ...'`

!!! note
Shift given points to align position **(0, 0)**

#### Custom class

* Define class

  ```
  Copyclass MyPolygon extends Phaser.GameObjects.Polygon {
    constructor(scene, x, y, points, fillColor) {
      super(scene, x, y, points, fillColor);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar polygon = new MyPolygon(scene, x, y, points, fillColor);

  ```

#### Color

* Fill color

  + Get

    ```
    Copyvar color = polygon.fillColor;
    var alpha = polygon.fillAlpha;

    ```
  + Set

    ```
    Copypolygon.setFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copypolygon.setFillStyle();

    ```
* Stroke color

  + Get

    ```
    Copyvar color = polygon.strokeColor;

    ```
  + Set

    ```
    Copypolygon.setStrokeStyle(lineWidth, color, alpha);

    ```
  + Clear

    ```
    Copypolygon.setStrokeStyle();

    ```

!!! warning "No tint methods"
Uses `polygon.setFillStyle(color, alpha)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = polygon.alpha;

  ```
* Set

  ```
  Copypolygon.setAlpha(alpha);
  // polygon.alpha = alpha;

  ```

#### Smooth

Smooths the polygon over the number of iterations specified.

```
Copypolygon.smooth(iterations);

```

#### Set points

```
Copypolygon.setTo(points);

```

* `point` :
  + A string containing paired values separated by a single space : `'40 0 40 20 100 20 100 80 40 80 40 100 0 50'`
  + An array of Point objects : `[new Phaser.Point(x1, y1), ...]`
  + An array of objects with public x/y properties : `[obj1, obj2, ...]`
  + An array of paired numbers that represent point coordinates : `[x1,y1, x2,y2, ...]`
  + An array of arrays with two elements representing x/y coordinates : `[[x1, y1], [x2, y2], ...]`

#### Display size

* Get

  ```
  Copyvar width = polygon.displayWidth;
  var height = polygon.displayHeight;

  ```
* Set

  ```
  Copypolygon.setDisplaySize(width, height);

  ```

  or

  ```
  Copypolygon.displayWidth = width;
  polygon.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = polygon.createGeometryMask();

```

### Rectangle

Draw a rectangle shape.

#### Create shape object

```
Copyvar rect = this.add.rectangle(x, y, width, height, fillColor);
// var rect = this.add.rectangle(x, y, width, height, fillColor, fillAlpha);

```

#### Custom class

* Define class

  ```
  Copyclass MyRectangle extends Phaser.GameObjects.Rectangle {
    constructor(scene, x, y, width, height, fillColor) {
      super(scene, x, y, width, height, fillColor);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar rect = new MyRectangle(scene, x, y, width, height, fillColor);

  ```

#### Color

* Fill color

  + Get

    ```
    Copyvar color = rect.fillColor;
    var alpha = rect.fillAlpha;

    ```
  + Set

    ```
    Copyrect.setFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copyrect.setFillStyle();

    ```
* Stroke color

  + Get

    ```
    Copyvar color = rect.strokeColor;

    ```
  + Set

    ```
    Copyrect.setStrokeStyle(lineWidth, color, alpha);

    ```
  + Clear

    ```
    Copyrect.setStrokeStyle();

    ```

!!! warning "No tint methods"
Uses `rect.setFillStyle(color, alpha)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = rect.alpha;

  ```
* Set

  ```
  Copyrect.setAlpha(alpha);
  // rect.alpha = alpha;

  ```

#### Size

* Get

  ```
  Copyvar width = rect.width;
  var height = rect.height;

  ```
* Set

  ```
  Copyrect.setSize(width, height);

  ```

  or

  ```
  Copyrect.width = width;
  rect.height = height;

  ```

#### Display size

* Get

  ```
  Copyvar width = rect.displayWidth;
  var height = rect.displayHeight;

  ```
* Set

  ```
  Copyrect.setDisplaySize(width, height);

  ```

  or

  ```
  Copyrect.displayWidth = width;
  rect.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = rect.createGeometryMask();

```

### Star

Draw a star shape. You can control several aspects of it including the number of points that constitute the star. The default is 5. If you change it to 4 it will render as a diamond. If you increase them, you'll get a more spiky star shape.

You can also control the inner and outer radius, which is how 'long' each point of the star is. Modify these values to create more interesting shapes.

#### Create shape object

```
Copyvar star = this.add.star(x, y, points, innerRadius, outerRadius, fillColor);
// var star = this.add.star(x, y, points, innerRadius, outerRadius, fillColor, fillAlpha);

```

* `points` : The number of points on the star. Default is 5.
* `innerRadius` : The inner radius of the star. Default is 32.
* `outerRadius` : The outer radius of the star. Default is 64.

#### Custom class

* Define class

  ```
  Copyclass MyStar extends Phaser.GameObjects.Star {
    constructor(scene, x, y, points, innerRadius, outerRadius, fillColor) {
      super(scene, x, y, points, innerRadius, outerRadius, fillColor);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar star = new MyStar(
    scene,
    x,
    y,
    points,
    innerRadius,
    outerRadius,
    fillColor
  );

  ```

#### Color

* Fill color

  + Get

    ```
    Copyvar color = star.fillColor;
    var alpha = star.fillAlpha;

    ```
  + Set

    ```
    Copystar.setFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copystar.setFillStyle();

    ```
* Stroke color

  + Get

    ```
    Copyvar color = star.strokeColor;

    ```
  + Set

    ```
    Copystar.setStrokeStyle(lineWidth, color, alpha);

    ```
  + Clear

    ```
    Copystar.setStrokeStyle();

    ```

!!! warning "No tint methods"
Uses `star.setFillStyle(color, alpha)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = star.alpha;

  ```
* Set

  ```
  Copystar.setAlpha(alpha);
  // star.alpha = alpha;

  ```

#### Radius

* Inner radius

  + Get

    ```
    Copyvar innerRadius = star.innerRadius;

    ```
  + Set

    ```
    Copystar.setInnerRadius(innerRadius);

    ```

    or

    ```
    Copystar.innerRadius = innerRadius;

    ```
* Outer radius

  + Get

    ```
    Copyvar outerRadius = star.outerRadius;

    ```
  + Set

    ```
    Copystar.setOuterRadius(outerRadius);

    ```

    or

    ```
    Copystar.outerRadius = outerRadius;

    ```
* Points

  + Get

    ```
    Copyvar points = star.points;

    ```
  + Set

    ```
    Copystar.setPoints(points);

    ```

    or

    ```
    Copystar.points = points;

    ```

#### Display size

* Get

  ```
  Copyvar width = star.displayWidth;
  var height = star.displayHeight;

  ```
* Set

  ```
  Copystar.setDisplaySize(width, height);

  ```

  or

  ```
  Copystar.displayWidth = width;
  star.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = star.createGeometryMask();

```

### Triangle

Draw a triangle shape. The Triangle consists of 3 lines, joining up to form a triangular shape. You can control the position of each point of these lines. The triangle is always closed and cannot have an open face. If you require that, use a Polygon.

#### Create shape object

```
Copyvar triangle = this.add.triangle(x, y, x1, y1, x2, y2, x3, y3, fillColor);
// var triangle = this.add.triangle(x, y, x1, y1, x2, y2, x3, y3, fillColor, fillAlpha);

```

#### Custom class

* Define class

  ```
  Copyclass MyTriangle extends Phaser.GameObjects.Triangle {
    constructor(scene, x, y, x1, y1, x2, y2, x3, y3, fillColor) {
      super(scene, x, y, x1, y1, x2, y2, x3, y3, fillColor);
      // ...
      this.add.existing(this);
    }
    // ...

    // preUpdate(time, delta) {}
  }

  ```

  + `this.add.existing(gameObject)` : Adds an existing Game Object to this Scene.
    - If the Game Object renders, it will be added to the Display List.
    - If it has a `preUpdate` method, it will be added to the Update List.
* Create instance

  ```
  Copyvar triangle = new MyTriangle(scene, x, y, x1, y1, x2, y2, x3, y3, fillColor);

  ```

#### Color

* Fill color

  + Get

    ```
    Copyvar color = triangle.fillColor;
    var alpha = triangle.fillAlpha;

    ```
  + Set

    ```
    Copytriangle.setFillStyle(color, alpha);

    ```
  + Clear

    ```
    Copytriangle.setFillStyle();

    ```
* Stroke color

  + Get

    ```
    Copyvar color = triangle.strokeColor;

    ```
  + Set

    ```
    Copytriangle.setStrokeStyle(lineWidth, color, alpha);

    ```
  + Clear

    ```
    Copytriangle.setStrokeStyle();

    ```

!!! warning "No tint methods"
Uses `triangle.setFillStyle(color, alpha)` to change color.

#### Alpha

* Get

  ```
  Copyvar alpha = triangle.alpha;

  ```
* Set

  ```
  Copytriangle.setAlpha(alpha);
  // triangle.alpha = alpha;

  ```

#### Set vertices

```
Copytriangle.setTo(x1, y1, x2, y2, x3, y3);

```

#### Triangle width

```
Copytriangle.setLineWidth(startWidth, endWidth);

```

* `endWidth` : The end width of the triangle. Only used in WebGL.

#### Display size

* Get

  ```
  Copyvar width = triangle.displayWidth;
  var height = triangle.displayHeight;

  ```
* Set

  ```
  Copytriangle.setDisplaySize(width, height);

  ```

  or

  ```
  Copytriangle.displayWidth = width;
  triangle.displayHeight = height;

  ```

#### Create mask

```
Copyvar mask = triangle.createGeometryMask();

```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Dom Element](dom-element.md)

[Group](group.md)

On this page

* [Graphics](#graphics)

  + [Basic usage](#basic-usage)

    - [Add graphics object](#add-graphics-object)
    - [Custom class](#custom-class)
  + [Drawing commands](#drawing-commands)

    - [Set line and fill style](#set-line-and-fill-style)
    - [Clear/Erase all drawings](#clearerase-all-drawings)
    - [Drawing paths](#drawing-paths)
    - [Drawing rectangles](#drawing-rectangles)
    - [Drawing rounded rectangles](#drawing-rounded-rectangles)
    - [Drawing triangles](#drawing-triangles)
    - [Drawing points](#drawing-points)
    - [Drawing lines](#drawing-lines)
    - [Drawing a series of lines](#drawing-a-series-of-lines)
    - [Drawing circles](#drawing-circles)
    - [Drawing ellipses](#drawing-ellipses)
    - [Drawing arcs](#drawing-arcs)
    - [Drawing pie-chart slices](#drawing-pie-chart-slices)
    - [Clear pattern](#clear-pattern)
    - [Transfer](#transfer)
    - [Generate texture](#generate-texture)
    - [Create mask](#create-mask)
  + [Shapes](#shapes)

    - [Arc](#arc)
    - [Circle](#circle)
    - [Curve](#curve)
    - [Ellipse](#ellipse)
    - [Grid](#grid)
    - [IsoBox](#isobox)
    - [IsoTriangle](#isotriangle)
    - [Line](#line)
    - [Polygon](#polygon)
    - [Rectangle](#rectangle)
    - [Star](#star)
    - [Triangle](#triangle)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../../index.md)