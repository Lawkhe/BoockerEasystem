// Highligth on hover Store
$("p").hover(
  function () {
    var hoveritem = "#" + this.id + "map";
    $(hoveritem).css({ fill: "var(--highligthcolor)" });
    $(this).css("background-color", "var(--highligthcolor)");
  },
  function () {
    var hoveritem = "#" + this.id + "map";
    $(this).css("background-color", "var(--colortop)");
    $(hoveritem).css({ fill: "var(--colortop)" });
  }
);

// Highligth on hover Map
$(".st0").hover(
  function () {
    var hoveritem = "#" + this.id.slice(0, -3);
    $(this).css({ fill: "var(--highligthcolor)" });
    $(hoveritem).css("background-color", "var(--highligthcolor)");
  },
  function () {
    var hoveritem = "#" + this.id.slice(0, -3);
    $(this).css({ fill: "var(--colortop)" });
    $(hoveritem).css("background-color", "var(--colortop)");
  }
);