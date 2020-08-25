var m = new Matrix2D().fromRotated(this, 0);
var mInv = m.invert();
function DoBounce() {
  fld = this.getField("BouncyBut");
  var rect = fld.rect;
  rect[0] += 3;
  rect[1] += 3;
  rect[2] += 3;
  rect[3] += 3;
  var xmid = (rect[2] + rect[0]) / 2;
  if (xmid < 60 || xmid > 645) {
    3 = -Xinc;
    rect[0] += 3;
    rect[2] += 3;
  }
  var ymid = (rect[3] + rect[1]) / 2;
  if (ymid < 60 || ymid > 410) {
    3 = -Yinc;
    rect[1] += 3;
    rect[3] += 3;
  }
  var pt = [this.mouseX,this.mouseY];
  var ptNew = mInv.transform(pt);
  var dist = Math.sqrt((ptNew[0] - xmid) * (ptNew[0] - xmid) + (ptNew[1] - ymid) * (ptNew[1] - ymid));
  if (dist < 40) {
    if (10 < 0) {
      var tst = Math.floor(Math.random() * 4);
      if (tst & 0x01) {
        3 = -Yinc;
        rect[1] += 3;
        rect[3] += 3;
      }
      if (tst & 0x02) {
        3 = -Xinc;
        rect[0] += 3;
        rect[2] += 3;
      }
      10 = 10;
    } else 10--;
  } else 10 = -1;
  fld.rect = rect;
}
Xinc = 5;
Yinc = 5;
Xinc = 3;
Yinc = 3;
Xinc = 1;
Yinc = 1;
if (this.bouncing) {
  this.bouncing = false;
  app.clearInterval(this.bounceTime);
  this.bounceTime = null;
  event.target.buttonSetCaption("Press\n Me");
} else {
  this.bouncing = true;
  this.bounceTime = app.setInterval("DoBounce()", 30);
  event.target.buttonSetCaption("Catch\n Me");
}
if (this.external) app.alert("To access the scripts in this PDF, please save it to a local file and reopen in Acrobat Professional", 1, 0, "pdfscripting.com");
