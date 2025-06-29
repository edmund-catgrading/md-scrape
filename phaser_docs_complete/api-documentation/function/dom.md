# Phaser.DOM

## AddToDOM

### <static> AddToDOM(element, [parent])

**Description:**

Adds the given element to the DOM. If a parent is provided the element is added as a child of the parent, providing it was able to access it.

If no parent was given it falls back to using `document.body`.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| element | HTMLElement | No | The element to be added to the DOM. Usually a Canvas object. |
| --- | --- | --- | --- |
| parent | string | HTMLElement | Yes | The parent in which to add the element. Can be a string which is passed to `getElementById` or an actual DOM object. |

**Returns:** HTMLElement - The element that was added to the DOM.

> Source: [src/dom/AddToDOM.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/AddToDOM.js#L7)  
> Since: 3.0.0

## DOMContentLoaded

### <static> DOMContentLoaded(callback)

**Description:**

Inspects the readyState of the document. If the document is already complete then it invokes the given callback.

If not complete it sets up several event listeners such as `deviceready`, and once those fire, it invokes the callback.

Called automatically by the Phaser.Game instance. Should not usually be accessed directly.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| callback | ContentLoadedCallback | No | The callback to be invoked when the device is ready and the DOM content is loaded. |
| --- | --- | --- | --- |

> Source: [src/dom/DOMContentLoaded.js#L13](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/DOMContentLoaded.js#L13)  
> Since: 3.0.0

## GetInnerHeight

### <static> GetInnerHeight(iOS)

**Description:**

Attempts to determine the document inner height across iOS and standard devices.

Based on code by @tylerjpeterson

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| iOS | boolean | No | Is this running on iOS? |
| --- | --- | --- | --- |

**Returns:** number - The inner height value.

> Source: [src/dom/GetInnerHeight.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/GetInnerHeight.js#L7)  
> Since: 3.16.0

## GetScreenOrientation

### <static> GetScreenOrientation(width, height)

**Description:**

Attempts to determine the screen orientation using the Orientation API.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| width | number | No | The width of the viewport. |
| --- | --- | --- | --- |
| height | number | No | The height of the viewport. |

**Returns:** string - The orientation.

> Source: [src/dom/GetScreenOrientation.js#L9](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/GetScreenOrientation.js#L9)  
> Since: 3.16.0

## GetTarget

### <static> GetTarget(element)

**Description:**

Attempts to get the target DOM element based on the given value, which can be either

a string, in which case it will be looked-up by ID, or an element node. If nothing

can be found it will return a reference to the document.body.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| element | HTMLElement | No | The DOM element to look-up. |
| --- | --- | --- | --- |

> Source: [src/dom/GetTarget.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/GetTarget.js#L7)  
> Since: 3.16.0

## ParseXML

### <static> ParseXML(data)

**Description:**

Takes the given data string and parses it as XML.

First tries to use the window.DOMParser and reverts to the Microsoft.XMLDOM if that fails.

The parsed XML object is returned, or `null` if there was an error while parsing the data.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| data | string | No | The XML source stored in a string. |
| --- | --- | --- | --- |

**Returns:** DOMParser, ActiveXObject - The parsed XML data, or `null` if the data could not be parsed.

> Source: [src/dom/ParseXML.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/ParseXML.js#L7)  
> Since: 3.0.0

## RemoveFromDOM

### <static> RemoveFromDOM(element)

**Description:**

Attempts to remove the element from its parentNode in the DOM.

**Parameters:**

| name | type | optional | description |
| --- | --- | --- | --- |
| element | HTMLElement | No | The DOM element to remove from its parent node. |
| --- | --- | --- | --- |

> Source: [src/dom/RemoveFromDOM.js#L7](https://github.com/phaserjs/phaser/blob/v3.87.0/src/dom/RemoveFromDOM.js#L7)  
> Since: 3.0.0

Updated on June 4, 2025, 1:16 PM UTC

---

[Phaser 3.87.0 API Documentation](../../index.md)

On this page

* [Phaser.DOM](#phaserdom)

  + [AddToDOM](#addtodom)

    - [<static> AddToDOM(element, [parent])](#static-addtodomelement-parent)
  + [DOMContentLoaded](#domcontentloaded)

    - [<static> DOMContentLoaded(callback)](#static-domcontentloadedcallback)
  + [GetInnerHeight](#getinnerheight)

    - [<static> GetInnerHeight(iOS)](#static-getinnerheightios)
  + [GetScreenOrientation](#getscreenorientation)

    - [<static> GetScreenOrientation(width, height)](#static-getscreenorientationwidth-height)
  + [GetTarget](#gettarget)

    - [<static> GetTarget(element)](#static-gettargetelement)
  + [ParseXML](#parsexml)

    - [<static> ParseXML(data)](#static-parsexmldata)
  + [RemoveFromDOM](#removefromdom)

    - [<static> RemoveFromDOM(element)](#static-removefromdomelement)

Back to top

©2025[Phaser](https://docs.phaser.io)