# Geometry

Geometry

Phaser has an extensive set of Geometry classes. These are used internally by the physics and input systems, but are also available for you to use in your own games. The geometry classes on offer include: Circle, Ellipse, Line, Point, Polygon, Rectangle, Triangle and the Mesh class.

Each of these classes has a set of methods and support functions that allow you to perform geometric operations on them. For example, you can check if a point is contained within a circle, get the bounds of an ellipse, or the nearest point from a line, as well as many other features.

There are also a wide range of intersection functions. You can test for conditions such as a Circle intersecting with a Rectangle, or getting the rays from a point to a polygon.

The Geometry classes are not Game Objects. You cannot add them on to the Display List. Instead, think of them as data structures that you can use to perform geometric operations on, of which most games tend to have quite a few.

## Circle

### Create circle

```
Copyvar circle = new Phaser.Geom.Circle(x, y, radius);

```

### Clone circle

```
Copyvar circle1 = Phaser.Geom.Circle.Clone(circle0);

```

### Draw on Graphics object

* Fill shape

  ```
  Copy// graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
  graphics.fillCircleShape(circle);

  ```
* Stroke shape

  ```
  Copy// graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
  graphics.strokeCircleShape(circle);

  ```

!!! note
Negative radius will be treated as positive radius. i.e. `Math.abs(radius)`

### Set circle properties

* All properties

  ```
  Copycircle.setTo(x, y, radius);

  ```

  or

  ```
  CopyPhaser.Geom.Circle.CopyFrom(source, dest);

  ```

  !!! note
  `CopyFrom` requires source and dest circles that already exist
* Position

  ```
  Copycircle.setPosition(x, y);

  ```

  or

  ```
  Copycircle.x = 0;
  circle.y = 0;

  ```

  or

  ```
  Copycircle.left = 0; // circle.x
  circle.top = 0; // circle.y
  // circle.right = 0;   // circle.x
  // circle.bottom = 0;  // circle.y

  ```

  or

  ```
  CopyPhaser.Geom.Circle.Offset(circle, dx, dy); // circle.x += dx, circle.y += dy

  ```

  or

  ```
  CopyPhaser.Geom.Circle.OffsetPoint(circle, point); // circle.x += point.x, circle.y += point.y

  ```
* Radius

  ```
  Copycircle.radius = radius;

  ```

  or

  ```
  Copycircle.diameter = diameter; // diameter = 2 * radius

  ```

### Get properties

* Position

  ```
  Copyvar x = circle.x;
  var y = circle.y;
  var top = circle.top;
  var left = circle.left;
  var right = circle.right;
  var bottom = circle.bottom;

  ```
* Radius

  ```
  Copyvar radius = circle.radius;
  // var diameter = circle.diameter;

  ```
* Bounds

  ```
  Copyvar bound = Phaser.Geom.Circle.GetBounds(circle);
  // var bound = Phaser.Geom.Circle.GetBounds(circle, bound);  // push bound

  ```

  + `bound` : `GetBounds` returns a Rectangle shape
* Area

  ```
  Copyvar area = Phaser.Geom.Circle.Area(circle);

  ```
* Circumference

  ```
  Copyvar circumference = Phaser.Geom.Circle.Circumference(circle);

  ```
* Type:

  ```
  Copyvar type = circle.type; // GEOM_CONST.CIRCLE or 0

  ```

### Point(s) & shape

* Get point at circle's edge

  ```
  Copyvar point = circle.getPoint(t);
  // var point = circle.getPoint(t, point);

  ```

  + Arguments:
    - `t` : A value between 0 and 1, where 0 equals 0 degrees, 0.5 equals 180 degrees and 1 equals 360 around the circle.
    - `point` : an existing point or returns a new point if point is not provided

  or

  ```
  Copyvar point = Phaser.Geom.Circle.CircumferencePoint(circle, angle); // angle in radians
  // var point = Phaser.Geom.Circle.CircumferencePoint(circle, angle, point);  // modify existing point or returns a new point if point is not provided

  ```
* Get a random point inside circle

  ```
  Copyvar point = circle.getRandomPoint();
  // var point = circle.getRandomPoint(point);  // modify existing point or returns a new point if point is not provided

  ```
* Get points around circle's edge.

  + Based on quantity:

  ```
  Copyvar points = circle.getPoints(quantity);
  // var points = circle.getPoints(quantity, null, pointsArray);  // If pointsArray not provided a new array will be created.

  ```

  + Based on stepRate:

  ```
  Copyvar points = circle.getPoints(false, stepRate);
  // var points = circle.getPoints(false, stepRate, pointsArray);  // If pointsArray not provided a new array will be created.

  ```

  + `pointsArray` : an existing array
  + `stepRate` : sets the quantity by getting the circumference of the circle divided by the stepRate
* Point is inside circle

  ```
  Copyvar isInside = circle.contains(x, y);

  ```

  or

  ```
  Copyvar isInside = Phaser.Geom.Circle.ContainsPoint(circle, point);

  ```
* Rectangle is inside shape

  ```
  Copyvar isInside = Phaser.Geom.Circle.ContainsRect(circle, rect); // rect : 4 points

  ```

### Empty

* Set empty

  ```
  Copycircle.setEmpty(); // circle.radius = 0

  ```
* Is empty

  ```
  Copyvar isEmpty = circle.isEmpty(); // circle.radius <= 0

  ```

### Equal

```
Copyvar isEqual = Phaser.Geom.Circle.Equals(circle0, circle1);

```

Position and radius are equal.

### Intersection

#### Circle to [circle](#circle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.CircleToCircle(circleA, circleB);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetCircleToCircle(circleA, circleB);
  // var out = Phaser.Geom.Intersects.GetCircleToCircle(circleA, circleB, out);

  ```

#### Circle to [rectangle](#rectangle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.CircleToRectangle(circle, rect);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetCircleToRectangle(circle, rect);
  // var out = Phaser.Geom.Intersects.GetCircleToRectangle(circle, rect, out);

  ```

#### Circle to [triangle](#triangle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.TriangleToCircle(triangle, circle);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetTriangleToCircle(triangle, circle);
  // var out = Phaser.Geom.Intersects.GetTriangleToCircle(triangle, circle, out);

  ```

#### Circle to [line](#line)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.LineToCircle(line, circle);
  // var result = Phaser.Geom.Intersects.LineToCircle(line, circle, nearest);

  ```

  + `nearest` : Nearest point on line.
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetLineToCircle(line, circle);
  // var out = Phaser.Geom.Intersects.GetLineToCircle(line, circle, out);

  ```

## Ellipse

### Create ellipse

```
Copyvar ellipse = new Phaser.Geom.Ellipse(x, y, width, height);

```

### Clone ellipse

```
Copyvar ellipse1 = Phaser.Geom.Ellipse.Clone(ellipse0);

```

### Draw on Graphics object

* Fill shape

  ```
  Copy// graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
  graphics.fillEllipseShape(ellipse);

  ```
* Stroke shape

  ```
  Copy// graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
  graphics.strokeEllipseShape(ellipse);

  ```

!!! note
Negative width, height will be treated as positive width, height. i.e. `Math.abs(width)`, `Math.abs(height)`

### Set properties

* All properties

  ```
  Copyellipse.setTo(x, y, width, height);

  ```

  or

  ```
  CopyPhaser.Geom.Ellipse.CopyFrom(source, dest);

  ```

  !!! note
  `CopyFrom` requires source and dest circles that already exist
* Position

  ```
  Copyellipse.setPosition(x, y);

  ```

  or

  ```
  Copyellipse.x = 0;
  ellipse.y = 0;

  ```

  or

  ```
  Copyellipse.left = 0; // ellipse.x
  ellipse.top = 0; // ellipse.y
  // ellipse.right = 0;   // ellipse.x
  // ellipse.bottom = 0;  // ellipse.y

  ```

  or

  ```
  CopyPhaser.Geom.Ellipse.Offset(ellipse, dx, dy); // ellipse.x += dx, ellipse.y += dy

  ```

  or

  ```
  CopyPhaser.Geom.Ellipse.OffsetPoint(ellipse, point); // ellipse.x += point.x, ellipse.y += point.y

  ```
* Width, height

  ```
  Copyellipse.width = width;
  ellipse.height = height;

  ```

### Get properties

* Position

  ```
  Copyvar x = ellipse.x;
  var y = ellipse.y;
  var top = ellipse.top;
  var left = ellipse.left;
  var right = ellipse.right;
  var bottom = ellipse.bottom;

  ```
* Width, height

  ```
  Copyvar width = ellipse.width;
  var height = ellipse.height;

  ```
* Bounds

  ```
  Copyvar bound = Phaser.Geom.Ellipse.GetBounds(ellipse);
  // var bound = Phaser.Geom.Ellipse.GetBounds(ellipse, bound);  // push bound

  ```

  + `bound` : `GetBounds` returns a Rectangle shape
* Area

  ```
  Copyvar area = Phaser.Geom.Ellipse.Area(ellipse);

  ```
* Circumference

  ```
  Copyvar circumference = Phaser.Geom.Ellipse.Circumference(ellipse);

  ```
* Type:

  ```
  Copyvar type = ellipse.type; // GEOM_CONST.ELLIPSE or 1

  ```

### Point(s) & shape

* Get point at shape's edge

  ```
  Copyvar point = ellipse.getPoint(t);
  // var point = ellipse.getPoint(t, point);

  ```

  + Arguments:
    - `t` : A value between 0 and 1, where 0 equals 0 degrees, 0.5 equals 180 degrees and 1 equals 360 around the circle.
    - `point` : an existing point or returns a new point if point is not provided

  or

  ```
  Copyvar point = Phaser.Geom.Ellipse.CircumferencePoint(ellipse, angle); // angle in degrees
  // var point = Phaser.Geom.Ellipse.CircumferencePoint(ellipse, angle, point);  // modify point

  ```
* Get a random point inside shape

  ```
  Copyvar point = ellipse.getRandomPoint();
  // var point = ellipse.getRandomPoint(point);  // modify point

  ```
* Get points around shape's edge

  + Based on quantity:

  ```
  Copyvar points = ellipse.getPoints(quantity);
  // var points = ellipse.getPoints(quantity, null, pointsArray);  // If pointsArray not provided a new array will be created.

  ```

  + Based on stepRate:

  ```
  Copyvar points = ellipse.getPoints(false, stepRate);
  // var points = ellipse.getPoints(false, stepRate, pointsArray);  // If pointsArray not provided a new array will be created.

  ```

  + `pointsArray` : an existing array
  + `stepRate` : sets the quantity by getting the circumference of the ellipse divided by the stepRate
* Point is inside shape

  ```
  Copyvar isInside = ellipse.contains(x, y);

  ```

  or

  ```
  Copyvar isInside = Phaser.Geom.Ellipse.ContainsPoint(ellipse, point);

  ```
* Rectangle is inside shape

  ```
  Copyvar isInside = Phaser.Geom.Ellipse.ContainsRect(ellipse, rect); // rect : 4 points

  ```

### Empty

* Set empty

  ```
  Copyellipse.setEmpty(); // ellipse.width = 0, ellipse.height = 0

  ```
* Is empty

  ```
  Copyvar isEmpty = ellipse.isEmpty(); // ellipse.width <= 0 || ellipse.height <= 0

  ```

### Equal

```
Copyvar isEqual = Phaser.Geom.Ellipse.Equals(ellipse0, ellipse1);

```

Position and width, height are equal.

## Line

### Create line

```
Copyvar line = new Phaser.Geom.Line(x1, y1, x2, y2);

```

### Clone line

```
Copyvar line1 = Phaser.Geom.Line.Clone(line0);

```

### Draw on Graphics object

```
Copy// graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
graphics.strokeLineShape(line);

```

### Set properties

* All properties

  ```
  Copyline.setTo(x1, y1, x2, y2);

  ```

  or

  ```
  CopyPhaser.Geom.Line.CopyFrom(source, dest);

  ```
* Position

  ```
  Copyline.x1 = 0;
  line.y1 = 0;
  line.x2 = 0;
  line.y2 = 0;

  ```

  or

  ```
  Copyline.left = 0; // min(x1, x2)
  line.top = 0; // min(y1, y2)
  line.right = 0; // max(x1, x2)
  line.bottom = 0; // max(y1, y2)

  ```

  + Offset start, end

    ```
    Copyvar line = Phaser.Geom.Line.Offset(line, dx, dy);
    // line.x1 += dx, line.y1 += dy, line.x2 += dx, line.y2 += dy

    ```
  + Set center position

    ```
    Copyvar line = Phaser.Geom.Line.CenterOn(line, x, y);

    ```
* Start point, angle, length

  ```
  Copyvar line = Phaser.Geom.Line.SetToAngle(line, x, y, angle, length);

  ```

  + `line` : The line to set
  + `x` , `y` : start point
  + `angle` : The angle of the line in **radians**

    ```
    Copyvar rad = Phaser.Math.DegToRad(deg);

    ```
  + `length` :　 The length of the line
* Rotate

  + Rotate around **midpoint**

    ```
    Copyvar line = Phaser.Geom.Line.Rotate(line, angle);

    ```

    - `line` : The line to set
    - `angle` : The angle of the line in **radians**

      ```
      Copyvar rad = Phaser.Math.DegToRad(deg);

      ```
  + Rotate around point

    ```
    Copyvar line = Phaser.Geom.Line.RotateAroundPoint(line, point, angle);

    ```

    or

    ```
    Copyvar line = Phaser.Geom.Line.RotateAroundXY(line, x, y, angle);

    ```

    - `line` : The line to set
    - `angle` : The angle of the line in **radians**

      ```
      Copyvar rad = Phaser.Math.DegToRad(deg);

      ```
* Extend

  ```
  Copyvar line = Phaser.Geom.Line.Extend(line, left, right);

  ```

### Get properties

* Position

  ```
  Copyvar x1 = line.x1;
  var y1 = line.y1;
  var x2 = line.x2;
  var y2 = line.y2;
  var top = line.top; // min(x1, x2)
  var left = line.left; // min(y1, y2)
  var right = line.right; // max(x1, x2)
  var bottom = line.bottom; // max(y1, y2)

  ```

  + Start point

    ```
    Copyvar start = line.getPointA(); // start: {x, y}
    var start = line.getPointA(start); // push start

    ```
  + End point

    ```
    Copyvar end = line.getPointB(); // end: {x, y}
    var end = line.getPointB(end); // push end

    ```
  + Middle point

    ```
    Copyvar middle = Phaser.Geom.Line.GetMidPoint(line); // middle: {x, y}
    // var middle = Phaser.Geom.Line.GetMidPoint(line, middle);

    ```
* Length

  ```
  Copyvar length = Phaser.Geom.Line.Length(line);

  ```

  + Width : Abs(x1 - x2)

    ```
    Copyvar width = Phaser.Geom.Line.Width(line);

    ```
  + Height : Abs(y1 - y2)

    ```
    Copyvar width = Phaser.Geom.Line.Height(line);

    ```
* Slope

  + Slope : (y2 - y1) / (x2 - x1)

    ```
    Copyvar slope = Phaser.Geom.Line.Slope(line);

    ```
  + Perpendicular slope : -((x2 - x1) / (y2 - y1))

    ```
    Copyvar perpSlope = Phaser.Geom.Line.PerpSlope(line);

    ```
* Angle

  + Angle

    ```
    Copyvar angle = Phaser.Geom.Line.Angle(line);

    ```

    - `angle` : The angle of the line in **radians**

      ```
      Copyvar deg = Phaser.Math.RadToDeg(rad); // deg : -180 ~ 180

      ```
  + Normal angle (angle - 90 degrees)

    - Normal angle

      ```
      Copyvar normalAngle = Phaser.Geom.Line.NormalAngle(line);

      ```
    - Normal vector

      ```
      Copyvar normal = Phaser.Geom.Line.GetNormal(line); // normal: {x, y}
      // var normal = Phaser.Geom.Line.GetNormal(line, normal);  // push normal

      ```

      or

      ```
      Copyvar normalX = Phaser.Geom.Line.NormalX(line);
      var normalY = Phaser.Geom.Line.NormalY(line);

      ```
  + Reflect angle

    ```
    Copyvar reflectAngle = Phaser.Geom.Line.ReflectAngle(aimLine, reflectingLine);

    ```
* Type:

  ```
  Copyvar type = line.type; // GEOM_CONST.LINE or 2

  ```

### Point(s) & shape

* Get point at shape's edge

  ```
  Copyvar point = line.getPoint(t);
  // var point = line.getPoint(t, point);

  ```

  + Arguments:
    - `t` : A value between 0 and 1, where 0 is the start, 0.5 is the middle and 1 is the end point of the line.
    - `point` : an existing point or returns a new point if point is not provided
* Get a random point inside shape

  ```
  Copyvar point = line.getRandomPoint();
  // var point = line.getRandomPoint(point);  // modify point

  ```
* Get points around shape's edge

  + Based on quantity:

  ```
  Copyvar points = line.getPoints(quantity);
  // var points = line.getPoints(quantity, null, pointsArray);  // push points

  ```

  + Based on stepRate:

  ```
  Copyvar points = line.getPoints(false, stepRate);
  // var points = line.getPoints(false, stepRate, pointsArray);  // If pointsArray not provided a new array will be created.

  ```

  + `pointsArray` : an existing array
  + `stepRate` : distance between each point on the line
* Get points using *Bresenham*'s line algorithm

  ```
  Copyvar points = Phaser.Geom.Line.BresenhamPoints(line, step);
  // var points = Phaser.Geom.Line.BresenhamPoints(line, step, points);  // push points

  ```
* Get points using easing function

  ```
  Copyvar points = Phaser.Geom.Line.GetEasedPoints(line, ease, quantity);
  // var points = Phaser.Geom.Line.GetEasedPoints(line, ease, quantity, collinearThreshold, easeParams);

  ```

  + `ease` : String of [ease function](tweens.md), or a custom function (`function (t) { return value}`).
  + `quantity` : The number of points to return.
  + `collinearThreshold` : Each point is spaced out at least this distance apart. This helps reduce clustering in noisey eases.
  + `easeParams` : Array of ease parameters to go with the ease.
* Get the nearest point on a line perpendicular to the given point.

  ```
  Copyvar point = Phaser.Geom.Line.GetNearestPoint(line, pointIn);
  // var point = Phaser.Geom.Line.GetNearestPoint(line, pointIn, point);

  ```
* Get the shortest distance from a Line to the given Point.

  ```
  Copyvar distance = Phaser.Geom.Line.GetShortestDistance(line, point);

  ```

### Equal

```
Copyvar isEqual = Phaser.Geom.Line.Equals(line0, line1);

```

x1, y2, x2, y2 are equal.

### Intersection

#### Line to [circle](#circle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.LineToCircle(line, circle);
  // var result = Phaser.Geom.Intersects.LineToCircle(line, circle, nearest);

  ```

  + `nearest` : Nearest point on line.
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetLineToCircle(line, circle);
  // var out = Phaser.Geom.Intersects.GetLineToCircle(line, circle, out);

  ```

#### Line to [rectangle](#rectangle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.LineToRectangle(line, rect);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetLineToRectangle(line, rect);
  // var out = Phaser.Geom.Intersects.GetLineToRectangle(line, rect, out);

  ```

#### Line to [triangle](#triangle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.TriangleToLine(triangle, line);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetTriangleToLine(triangle, line);
  // var out = Phaser.Geom.Intersects.GetTriangleToLine(triangle, line, out);

  ```

#### Line to [line](#line)

* Is intersection

  ```
  Copyvar isIntersection = Phaser.Geom.Intersects.LineToLine(line1, line2);

  ```

  + `isIntersection` : Return `true` if line1 and line2 are intersectioned
* Get intersection point

  ```
  Copyvar isIntersection = Phaser.Geom.Intersects.LineToLine(line1, line2, out);

  ```

  + `isIntersection` : Return `true` if line1 and line2 are intersectioned
  + `out` : intersected point

## Point

### Create point

```
Copyvar point = new Phaser.Geom.Point(x, y);

```

### Clone point

```
Copyvar point1 = Phaser.Geom.Point.Clone(point0);

```

### Draw on Graphics object

```
Copy// graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
graphics.fillPointShape(point, size);

```

### Set properties

* All properties

  ```
  Copypoint.setTo(x, y);

  ```

  or

  ```
  CopyPhaser.Geom.Point.CopyFrom(source, dest);

  ```
* Position

  ```
  Copypoint.x = 0;
  point.y = 0;

  ```
* Round

  + Ceil : Apply `Math.ceil()` to each coordinate of the given Point

    ```
    Copyvar point = Phaser.Geom.Point.Ceil(point);

    ```
  + Floor : Apply `Math.floor()` to each coordinate of the given Point.

    ```
    Copyvar point = Phaser.Geom.Point.Floor(point);

    ```

### Symmetry

* Invert : x = y, y = x

  ```
  Copyvar point = Phaser.Geom.Point.Invert(point);

  ```
* Negative : x = -x, y = -y

  ```
  Copyvar out = Phaser.Geom.Point.Negative(point);
  // var out = Phaser.Geom.Point.Negative(point, out);  // modify out

  ```

### Get properties

* Position

  ```
  Copyvar x = point.x;
  var y = point.y;

  ```
* Type:

  ```
  Copyvar type = point.type; // GEOM_CONST.POINT or 3

  ```

### Equal

```
Copyvar isEqual = Phaser.Geom.Point.Equals(point0, point1);

```

x, y are equal.

### Points

* Centroid : center-point over some points

  ```
  Copyvar out = Phaser.Geom.Point.GetCentroid(points);
  // var out = Phaser.Geom.Point.GetCentroid(points, out);  // modify out

  ```
* Calculates the Axis Aligned Bounding Box (or aabb) from an array of points ([rectangle](#rectangle))

  ```
  Copyvar rect = Phaser.Geom.Point.GetRectangleFromPoints(points);
  // var rect = Phaser.Geom.Point.GetRectangleFromPoints(points, rect);  // modify rect

  ```
* Interpolate

  ```
  Copyvar out = Phaser.Geom.Point.Interpolate(pointA, pointB, t); // out : point
  // var out = Phaser.Geom.Point.Interpolate(pointA, pointB, t, out);  // modify out

  ```

### Intersection

* Point to [line](#line)

  ```
  Copyvar result = Phaser.Geom.Intersects.PointToLine(point, line);
  // var result = Phaser.Geom.Intersects.PointToLine(point, line, lineThickness);

  ```

  ```
  Copyvar result = Phaser.Geom.Intersects.PointToLineSegment(point, line);

  ```

### Point as Vector

Vector starting at (0,0)

* Magnitude : sqrt( (x \_ x) + (y \_ y) )

  ```
  Copyvar magnitude = Phaser.Geom.Point.GetMagnitude(point);

  ```

  or

  ```
  Copyvar magnitudeSq = Phaser.Geom.Point.GetMagnitudeSq(point);

  ```
* Project

  ```
  Copyvar out = Phaser.Geom.Point.Project(from, to);
  // var out = Phaser.Geom.Point.Project(from, to, out);  // modify out

  ```

  or

  ```
  Copyvar out = Phaser.Geom.Point.ProjectUnit(from, to); // vector `from` and `to` are unit vector (length = 1)
  // var out = Phaser.Geom.Point.ProjectUnit(from, to, out);  // modify out

  ```

## Polygon

### Create polygon

```
Copyvar polygon = new Phaser.Geom.Polygon(points);

```

* `points` :
  + An array of number : `[x0, y0, x1, y1, ...]`
  + An array of points : `[{x:x0, y:y0}, {x:x1, y:y1}, ...]`
  + A string : `'x0 y0 x1 y1 ...'`

### Clone polygon

```
Copyvar polygon1 = Phaser.Geom.Polygon.Clone(polygon0);

```

### Draw on Graphics object

* Fill shape

  ```
  Copy// graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
  graphics.fillPoints(polygon.points, true);

  ```
* Stroke shape

  ```
  Copy// graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
  graphics.strokePoints(polygon.points, true);

  ```

### Set properties

```
Copypolygon.setTo(points);
// points = [x0, y0, x1, y1, x2, y2, ...] , or [{x,y}, {x,y}, {x,y}, ...]

```

### Get properties

* Points

  ```
  Copyvar points = polygon.points; // array of points {x,y}

  ```
* Area

  ```
  Copyvar area = polygon.area;

  ```
* Number array

  ```
  Copyvar out = Phaser.Geom.Polygon.GetNumberArray(polygon);
  // var out = Phaser.Geom.Polygon.GetNumberArray(polygon, out);  // modify out

  ```

  + `arr` : [x0, y0, x1, y1, x2, y2, ...]
* AABB (A minimum rectangle to cover this polygon)

  ```
  Copyvar out = Phaser.Geom.Polygon.GetAABB(polygon);
  // var out = Phaser.Geom.Polygon.GetAABB(polygon, out);

  ```

  + `out` : A [rectangle](#rectangle)
* Type:

  ```
  Copyvar type = polygon.type; // GEOM_CONST.POLYGON or 4

  ```

### Point(s) & shape

* Point is inside shape

  ```
  Copyvar isInside = polygon.contains(x, y);

  ```

  or

  ```
  Copyvar isInside = Phaser.Geom.Polygon.ContainsPoint(polygon, point);

  ```
* Translate : Shift points.

  ```
  CopyPhaser.Geom.Polygon.Translate(polygon, x, y);

  ```
* Reverse the order of points.

  ```
  Copyvar polygon = Phaser.Geom.Polygon.Reverse(polygon);

  ```
* Smooth : Takes a Polygon object and applies Chaikin's smoothing algorithm on its points.

  ```
  CopyPhaser.Geom.Polygon.Smooth(polygon);

  ```
* Simplify : Simplifies the points by running them through a combination of
  Douglas-Peucker and Radial Distance algorithms. Simplification dramatically
  reduces the number of points in a polygon while retaining its shape, giving
  a huge performance boost when processing it and also reducing visual noise.

  ```
  Copyvar polygon = Phaser.Geom.Polygon.Simplify(polygon);
  // var polygon = Phaser.Geom.Polygon.Simplify(polygon, tolerance, highestQuality);

  ```
* Get points around the polygon's perimeter.

  + Based on quantity:

  ```
  Copyvar points = polygon.getPoints(quantity);
  // var points = polygon.getPoints(quantity, null, pointsArray);  // If pointsArray not provided a new array will be created.

  ```

  + Based on stepRate:

  ```
  Copyvar points = polygon.getPoints(false, stepRate);
  // var points = polygon.getPoints(false, stepRate, pointsArray);  // If pointsArray not provided a new array will be created.

  ```

  + `pointsArray` : an existing array
  + `stepRate` : sets the quantity by getting the perimeter of the Polygon divided it by the stepRate

### Vector to polygon

* Get closest point of intersection between a vector and an array of polygons

  ```
  Copyvar result = Phaser.Geom.Intersects.GetLineToPolygon(line, polygons);
  // var out = Phaser.Geom.Intersects.GetLineToPolygon(line, polygons, isRay, out);

  ```

  + `line` : Vector of [line](#line) object
  + `polygons` : A single polygon, or array of polygons
  + `isRay` : Is `line` a ray or a line segment?
  + `out` :
    - `out.x`, `out.y` : Intersection point
    - `out.z` : Closest intersection distance
    - `out.w` : Index of the polygon
* Projects rays out from the given point to each line segment of the polygons.

  ```
  Copyvar out = Phaser.Geom.Intersects.GetRaysFromPointToPolygon(x, y, polygons);

  ```

  + `x`, `y` : The point to project the rays from.
  + `polygons` : A single polygon, or array of polygons
  + `out` : An array containing all intersections
    - `out[i].x`, `out[i].y` : Intersection point
    - `out[i].z` : Angle of intersection
    - `out[i].w` : Index of the polygon

## Rectangle

### Create rectangle

```
Copyvar rect = new Phaser.Geom.Rectangle(x, y, width, height);

```

### Create rectangle from points

All of the given points are on or within its bounds.

```
Copyvar rect = Phaser.Geom.Rectangle.FromPoints(points);
// var rect = Phaser.Geom.Rectangle.FromPoints(points, rect);  // push rect

```

* `points` : an array with 4 points. `[x, y]`, or `{x:0, y:0}`

or

```
Copyvar rect = Phaser.Geom.Rectangle.FromXY(x1, y1, x2, y2);
// var rect = Phaser.Geom.Rectangle.FromXY(x1, y1, x2, y2, rect);  // push rect

```

### Clone rectangle

```
Copyvar rect1 = Phaser.Geom.Rectangle.Clone(rect0);

```

### Draw on Graphics object

* Fill shape

  ```
  Copy// graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
  graphics.fillRectShape(rect);

  ```
* Stroke shape

  ```
  Copy// graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
  graphics.strokeRectShape(rect);

  ```

!!! note
`x` with positive/negative width is left/right bound  
`y` with positive/negative height is top/bottom bound

### Set properties

* All properties

  ```
  Copyrect.setTo(x, y, width, height);

  ```

  or

  ```
  CopyPhaser.Geom.Rectangle.CopyFrom(source, dest);

  ```
* Position

  ```
  Copyrect.setPosition(x, y);

  ```

  or

  ```
  Copyrect.x = 0;
  rect.y = 0;

  ```

  or

  ```
  Copyrect.left = 0; // rect.x, rect.width
  rect.top = 0; // rect.y, rect.height
  // rect.right = 0;   // rect.x, rect.width
  // rect.bottom = 0;  // rect.y, rect.height
  rect.centerX = 0; // rect.x
  rect.centerY = 0; // rect.y

  ```

  or

  ```
  CopyPhaser.Geom.Rectangle.Offset(rect, dx, dy); // rect.x += dx, rect.y += dy

  ```

  or

  ```
  CopyPhaser.Geom.Rectangle.OffsetPoint(rect, point); // rect.x += point.x, rect.y += point.y

  ```

  or

  ```
  CopyPhaser.Geom.Rectangle.CenterOn(rect, x, y); // rect.x = x - (rect.width / 2), rect.y = y - (rect.height / 2)

  ```
* Size

  ```
  Copyrect.setSize(width, height);
  // rect.setSize(width);   // height = width

  ```

  or

  ```
  Copyrect.width = 0;
  rect.height = 0;

  ```

  + Scale

    ```
    CopyPhaser.Geom.Rectangle.Scale(rect, x, y); // rect.width *= x, rect.height *= y;
    // Phaser.Geom.Rectangle.Scale(rect, x);   // y = x

    ```
  + Extend size to include points

    ```
    CopyPhaser.Geom.Rectangle.MergePoints(rect, points);

    ```

    - `points` : an array of points. `[x, y]`, or `{x:0, y:0}`
  + Extend size to include another rectangle

    ```
    CopyPhaser.Geom.Rectangle.MergeRect(target, source);

    ```
* Inflate

  ```
  CopyPhaser.Geom.Rectangle.Inflate(rect, x, y);

  ```

  1. change size to `width += x*2, height += y*2`
  2. center on previous position
* Fits the target rectangle into the source rectangle

  ```
  CopyPhaser.Geom.Rectangle.FitInside(target, source);

  ```

  Preserves aspect ratio, scales and centers the target rectangle to the source rectangle
* Fits the target rectangle around the source rectangle

  ```
  CopyPhaser.Geom.Rectangle.FitOutside(target, source);

  ```

  Preserves aspect ratio, scales and centers the target rectangle to the source rectangle
* Ceil

  ```
  CopyPhaser.Geom.Rectangle.Ceil(rect); // ceil x, y

  ```

  ```
  CopyPhaser.Geom.Rectangle.CeilAll(rect); // ceil x, y, width, height

  ```
* Floor

  ```
  CopyPhaser.Geom.Rectangle.Floor(rect); // floor x, y

  ```

  ```
  CopyPhaser.Geom.Rectangle.FloorAll(rect); // floor x, y, width, height

  ```

### Get properties

* Position

  ```
  Copyvar x = rect.x;
  var y = rect.y;

  ```

  + Bound

    ```
    Copyvar top = rect.top;
    var left = rect.left;
    var right = rect.right;
    var bottom = rect.bottom;

    ```

    or

    ```
    Copyvar points = Phaser.Geom.Rectangle.Decompose(rect);
    // var points = Phaser.Geom.Rectangle.Decompose(rect, points); // push result points

    ```

    - `points` : top-left, top-right, bottom-right, bottom-left
  + Center

    ```
    Copyvar centerX = rect.centerX;
    var centerY = rect.centerY;

    ```

    or

    ```
    Copyvar point = Phaser.Geom.Rectangle.GetCenter(rect);
    // var point = Phaser.Geom.Rectangle.GetCenter(rect, point);

    ```
* Size

  ```
  Copyvar width = rect.width;
  var height = rect.height;

  ```

  or

  ```
  Copyvar point = Phaser.Geom.Rectangle.GetSize(rect); // {x: rect.width, y: rect.height}

  ```
* Area

  ```
  Copyvar area = Phaser.Geom.Rectangle.Area(rect);

  ```
* Perimeter

  ```
  Copyvar perimeter = Phaser.Geom.Rectangle.Perimeter(rect); // 2 * (rect.width + rect.height)

  ```
* Aspect ratio

  ```
  Copyvar aspectRatio = Phaser.Geom.Rectangle.GetAspectRatio(rect); // rect.width / rect.height

  ```
* Lines around rectangle

  ```
  Copyvar topLine = rect.getLineA(); // top line of this rectangle
  var rightLine = rect.getLineB(); // right line of this rectangle
  var bottomLine = rect.getLineC(); // bottom line of this rectangle
  var leftLine = rect.getLineD(); // left line of this rectangle
  // var out = rect.getLineA(out);  // top line of this rectangle

  ```
* Type:

  ```
  Copyvar type = rect.type; // GEOM_CONST.RECTANGLE or 5

  ```

### Point(s) & shape

* Get point at shape's edge

  ```
  Copyvar point = rect.getPoint(t); // t : 0 ~ 1 (0= top-left, 0.5= bottom-right, 1= top-left)
  // var point = rect.getPoint(t, point);

  ```

  + Arguments:
    - `t` : A value of 0 or 1 is at the top left corner, 0.5 is at the bottom right corner. Values 0 to 0.5 are on the top or the right side, values 0.5 to 1 are on the bottom or the left side.
    - `point` : an existing point or returns a new point if point is not provided

  or

  ```
  Copyvar point = Phaser.Geom.Rectangle.PerimeterPoint(rect, angle); // angle in degrees
  // var point = Phaser.Geom.Rectangle.PerimeterPoint(rect, angle, point);  // push point

  ```
* Get points around shape's edge

  + Based on quantity:

  ```
  Copyvar points = rect.getPoints(quantity);
  // var points = rect.getPoints(quantity, null, pointsArray);  // push points

  ```

  + Based on stepRate:

  ```
  Copyvar points = rect.getPoints(false, stepRate);
  // var points = rect.getPoints(false, stepRate, pointsArray);  // If pointsArray not provided a new array will be created.

  ```

  + `pointsArray` : an existing array
  + `stepRate` : if quantity is 0, determines the normalized distance between each returned point
* Point is inside shape

  ```
  Copyvar isInside = rect.contains(x, y);

  ```

  or

  ```
  Copyvar isInside = Phaser.Geom.Rectangle.ContainsPoint(rect, point);

  ```
* Get a random point inside shape

  ```
  Copyvar point = rect.getRandomPoint();
  // var point = rect.getRandomPoint(point);  // modify point

  ```
* Get a random point outside shape

  ```
  Copyvar point = Phaser.Geom.Rectangle.RandomOutside(outer, inner);
  // var point = Phaser.Geom.Rectangle.RandomOutside(outer, inner, point); // modify point

  ```
* Rectangle is inside shape

  ```
  Copyvar isInside = Phaser.Geom.Rectangle.ContainsRect(rectA, rectB); // rectB is inside rectA

  ```

### Multiple rectangles

* Is overlapping

  ```
  Copyvar isOverlapping = Phaser.Geom.Rectangle.Overlaps(rectA, rectB);

  ```
* Get intersection rectangle

  ```
  Copyvar rect = Phaser.Geom.Rectangle.Intersection(rectA, rectB);
  var rect = Phaser.Geom.Rectangle.Intersection(rectA, rectB, rect); // push rect

  ```
* Get union rectangle

  ```
  Copyvar rect = Phaser.Geom.Rectangle.Union(rectA, rectB);
  var rect = Phaser.Geom.Rectangle.Union(rectA, rectB, rect); // push rect

  ```

### Empty

* Set empty

  ```
  Copyrect.setEmpty(); // rect.x = 0, rect.y = 0, rect.width = 0, rect.height = 0

  ```
* Is empty

  ```
  Copyvar isEmpty = rect.isEmpty(); // rect.radius <= 0;

  ```

### Equal

* Position, width, and height are the same

  ```
  Copyvar isEqual = Phaser.Geom.Rectangle.Equals(rect0, rect1);

  ```
* Width and height are the same

  ```
  Copyvar isEqual = Phaser.Geom.Rectangle.SameDimensions(rect0, rect1);

  ```

### Intersection

#### Rectangle to [circle](#circle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.CircleToRectangle(circle, rect);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetCircleToRectangle(circle, rect);
  // var out = Phaser.Geom.Intersects.GetCircleToRectangle(circle, rect, out);

  ```

#### Rectangle to [rectangle](#rectangle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.RectangleToRectangle(rectA, rectB);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetRectangleToRectangle(rectA, rectB);
  // var out = Phaser.Geom.Intersects.GetRectangleToRectangle(rectA, rectB, out);

  ```

#### Rectangle to [triangle](#triangle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.RectangleToTriangle(rect, triangle);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetRectangleToTriangle(rect, triangle);
  // var out = Phaser.Geom.Intersects.GetRectangleToTriangle(rect, triangle, out);

  ```

#### Rectangle to [line](#line)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.LineToRectangle(line, rect);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetLineToRectangle(line, rect);
  // var out = Phaser.Geom.Intersects.GetLineToRectangle(line, rect, out);

  ```

## Triangle

### Create triangle

```
Copyvar triangle = new Phaser.Geom.Triangle(x1, y1, x2, y2, x3, y3);

```

### Clone triangle

```
Copyvar triangle1 = Phaser.Geom.Triangle.Clone(triangle0);

```

### Equilateral triangle

```
Copyvar triangle = Phaser.Geom.Triangle.BuildEquilateral(x1, y1, length);

```

### Right triangle

```
Copyvar triangle = Phaser.Geom.Triangle.BuildRight(x1, y1, width, height);

```

### [Polygon](#polygon) to triangles

```
Copyvar out = Phaser.Geom.Triangle.BuildFromPolygon(data);
// var out = Phaser.Geom.Triangle.BuildFromPolygon(data, holes, scaleX, scaleY);
// out = Phaser.Geom.Triangle.BuildFromPolygon(data, holes, scaleX, scaleY, out);

```

* `data` : A flat array of vertice coordinates like `[x0,y0, x1,y1, x2,y2, ...]`
* `out` : Array of triangles

### Draw on Graphics object

* Fill shape

  ```
  Copy// graphics.fillStyle(color, alpha);   // color: 0xRRGGBB
  graphics.fillTriangleShape(triangle);

  ```
* Stroke shape

  ```
  Copy// graphics.lineStyle(lineWidth, color, alpha);   // color: 0xRRGGBB
  graphics.strokeTriangleShape(triangle);

  ```

### Set properties

* All properties

  ```
  Copytriangle.setTo(x1, y1, x2, y2, x3, y3);

  ```

  or

  ```
  CopyPhaser.Geom.Triangle.CopyFrom(source, dest);

  ```
* Position

  ```
  Copytriangle.x1 = 0;
  triangle.y1 = 0;
  triangle.x2 = 0;
  triangle.y2 = 0;
  triangle.x3 = 0;
  triangle.y3 = 0;

  ```

  or

  ```
  Copytriangle.left = 0; // triangle.x1, triangle.x2, triangle.x3
  triangle.top = 0; // triangle.y1, triangle.y2, triangle.y3
  // triangle.right = 0;   // triangle.x1, triangle.x2, triangle.x3
  // triangle.bottom = 0;  // triangle.y1, triangle.y2, triangle.y3

  ```

  or

  ```
  CopyPhaser.Geom.Triangle.Offset(triangle, dx, dy); // triangle.x += dx, triangle.y += dy

  ```

  or

  ```
  CopyPhaser.Geom.Triangle.CenterOn(triangle, x, y);

  ```
* Rotate

  + Rotate around center (incenter)

    ```
    Copyvar triangle = Phaser.Geom.Triangle.Rotate(triangle, angle);

    ```

    - `angle` : Radian
  + Rotate around point

    ```
    Copyvar triangle = Phaser.Geom.Triangle.RotateAroundPoint(
      triangle,
      point,
      angle
    );

    ```

    - `point` : `{x, y}`
    - `angle` : Radian
  + Rotate around (x,y)

    ```
    Copyvar triangle = Phaser.Geom.Triangle.RotateAroundXY(triangle, x, y, angle);

    ```

    - `angle` : Radian

### Get properties

* Position

  ```
  Copyvar x1 = triangle.x1;
  var y1 = triangle.y1;
  var x2 = triangle.x2;
  var y2 = triangle.y2;
  var x3 = triangle.x3;
  var y3 = triangle.y3;
  var top = triangle.top;
  var left = triangle.left;
  var right = triangle.right;
  var bottom = triangle.bottom;

  ```

  or

  ```
  Copyvar out = Phaser.Geom.Triangle.Decompose(triangle); // out: [{x1,y1}, {x2,y2}, {x3,y3}]
  // var out = Phaser.Geom.Triangle.Decompose(triangle, out);

  ```
* Perimeter

  ```
  Copyvar perimeter = Phaser.Geom.Triangle.Perimeter(triangle);

  ```
* Area

  ```
  Copyvar area = Phaser.Geom.Triangle.Area(triangle);

  ```
* Lines around triangle

  ```
  Copyvar line12 = rect.getLineA(); // line from (x1, y1) to (x2, y2)
  var line23 = rect.getLineB(); // line from (x2, y2) to (x3, y3)
  var line31 = rect.getLineC(); // line from (x3, y3) to (x1, y1)

  ```
* Centroid

  ```
  Copyvar out = Phaser.Geom.Triangle.Centroid(triangle); // out: {x,y}

  ```
* Incenter

  ```
  Copyvar out = Phaser.Geom.Triangle.InCenter(triangle); // out: {x,y}
  // var out = Phaser.Geom.Triangle.InCenter(triangle, out);

  ```
* Circumcenter

  ```
  Copyvar out = Phaser.Geom.Triangle.CircumCenter(triangle); // out: {x,y}
  // var out = Phaser.Geom.Triangle.CircumCenter(triangle, out);

  ```
* Circumcircle

  ```
  Copyvar out = Phaser.Geom.Triangle.CircumCircle(triangle); // out: a circle object
  // var out = Phaser.Geom.Triangle.CircumCircle(triangle, out);

  ```
* Type:

  ```
  Copyvar type = triangle.type; // GEOM_CONST.TRIANGLE or 6

  ```

### Point(s) & shape

* Get point at shape's edge

  ```
  Copyvar point = triangle.getPoint(t);
  // var point = triangle.getPoint(t, point);

  ```

  + Arguments:
    - `t` : A value of 0 or 1 is the first point. Values 0 to 1 returns a point along the perimeter of the triangle.
    - `point` : an existing point or returns a new point if point is not provided
* Get a random point inside shape

  ```
  Copyvar point = triangle.getRandomPoint();
  // var point = triangle.getRandomPoint(point);  // modify point

  ```
* Get points around triangle's edge

  + Based on quantity:

  ```
  Copyvar points = triangle.getPoints(quantity);
  // var points = triangle.getPoints(quantity, null, points);  // push points

  ```

  + Based on stepRate:

  ```
  Copyvar points = triangle.getPoints(false, stepRate);
  // var points = triangle.getPoints(false, stepRate, points);  // If pointsArray not provided a new array will be created.

  ```

  + `pointsArray` : an existing array
  + `stepRate` : used only when quantity is falsey and is the distance between two points
* Point is inside shape

  ```
  Copyvar isInside = triangle.contains(x, y);

  ```

  or

  ```
  Copyvar isInside = Phaser.Geom.Triangle.ContainsPoint(triangle, point);

  ```

  + Points inside shape

    ```
    Copyvar out = Phaser.Geom.Triangle.ContainsArray(triangle, points, returnFirst);
    // var out = Phaser.Geom.Triangle.ContainsArray(triangle, points, returnFirst, out);

    ```

    - `out` : Points inside triangle
    - `returnFirst` : True to get fist matched point

### Equal

```
Copyvar isEqual = Phaser.Geom.Triangle.Equals(triangle0, triangle1);

```

Position and radius are equal.

### Intersection

#### Triangle to [circle](#circle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.TriangleToCircle(triangle, circle);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetTriangleToCircle(triangle, circle);
  // var out = Phaser.Geom.Intersects.GetTriangleToCircle(triangle, circle, out);

  ```

#### Triangle to [rectangle](#rectangle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.RectangleToTriangle(rect, triangle);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetRectangleToTriangle(rect, triangle);
  // var out = Phaser.Geom.Intersects.GetRectangleToTriangle(rect, triangle, out);

  ```

#### Triangle to [triangle](#triangle)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.TriangleToTriangle(triangleA, triangleB);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetTriangleToTriangle(
    triangleA,
    triangleB
  );
  // var out = Phaser.Geom.Intersects.GetTriangleToTriangle(triangleA, triangleB, out);

  ```

#### Triangle to [line](#line)

* Is intersection

  ```
  Copyvar result = Phaser.Geom.Intersects.TriangleToLine(triangle, line);

  ```
* Get intersection points

  ```
  Copyvar result = Phaser.Geom.Intersects.GetTriangleToLine(triangle, line);
  // var out = Phaser.Geom.Intersects.GetTriangleToLine(triangle, line, out);

  ```

## Author Credits

Content on this page includes work by:

* [RexRainbow](https://github.com/rexrainbow)

Updated on June 4, 2025, 1:16 PM UTC

---

[Video](gameobjects/video.md)

[Input](input.md)

On this page

* [Geometry](#geometry)

  + [Circle](#circle)

    - [Create circle](#create-circle)
    - [Clone circle](#clone-circle)
    - [Draw on Graphics object](#draw-on-graphics-object)
    - [Set circle properties](#set-circle-properties)
    - [Get properties](#get-properties)
    - [Point(s) & shape](#points--shape)
    - [Empty](#empty)
    - [Equal](#equal)
    - [Intersection](#intersection)
  + [Ellipse](#ellipse)

    - [Create ellipse](#create-ellipse)
    - [Clone ellipse](#clone-ellipse)
    - [Draw on Graphics object](#draw-on-graphics-object-1)
    - [Set properties](#set-properties)
    - [Get properties](#get-properties-1)
    - [Point(s) & shape](#points--shape-1)
    - [Empty](#empty-1)
    - [Equal](#equal-1)
  + [Line](#line)

    - [Create line](#create-line)
    - [Clone line](#clone-line)
    - [Draw on Graphics object](#draw-on-graphics-object-2)
    - [Set properties](#set-properties-1)
    - [Get properties](#get-properties-2)
    - [Point(s) & shape](#points--shape-2)
    - [Equal](#equal-2)
    - [Intersection](#intersection-1)
  + [Point](#point)

    - [Create point](#create-point)
    - [Clone point](#clone-point)
    - [Draw on Graphics object](#draw-on-graphics-object-3)
    - [Set properties](#set-properties-2)
    - [Symmetry](#symmetry)
    - [Get properties](#get-properties-3)
    - [Equal](#equal-3)
    - [Points](#points)
    - [Intersection](#intersection-2)
    - [Point as Vector](#point-as-vector)
  + [Polygon](#polygon)

    - [Create polygon](#create-polygon)
    - [Clone polygon](#clone-polygon)
    - [Draw on Graphics object](#draw-on-graphics-object-4)
    - [Set properties](#set-properties-3)
    - [Get properties](#get-properties-4)
    - [Point(s) & shape](#points--shape-3)
    - [Vector to polygon](#vector-to-polygon)
  + [Rectangle](#rectangle)

    - [Create rectangle](#create-rectangle)
    - [Create rectangle from points](#create-rectangle-from-points)
    - [Clone rectangle](#clone-rectangle)
    - [Draw on Graphics object](#draw-on-graphics-object-5)
    - [Set properties](#set-properties-4)
    - [Get properties](#get-properties-5)
    - [Point(s) & shape](#points--shape-4)
    - [Multiple rectangles](#multiple-rectangles)
    - [Empty](#empty-2)
    - [Equal](#equal-4)
    - [Intersection](#intersection-3)
  + [Triangle](#triangle)

    - [Create triangle](#create-triangle)
    - [Clone triangle](#clone-triangle)
    - [Equilateral triangle](#equilateral-triangle)
    - [Right triangle](#right-triangle)
    - [Polygon to triangles](#polygon-to-triangles)
    - [Draw on Graphics object](#draw-on-graphics-object-6)
    - [Set properties](#set-properties-5)
    - [Get properties](#get-properties-6)
    - [Point(s) & shape](#points--shape-5)
    - [Equal](#equal-5)
    - [Intersection](#intersection-4)
  + [Author Credits](#author-credits)

Back to top

©2025[Phaser](../../index.md)



Geometry