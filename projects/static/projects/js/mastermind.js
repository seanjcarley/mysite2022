$(document).ready(function () {
    dif = "easy";
    guess_count = 0;
    plyr_guess = [];
    seq = [];
    document.getElementById("easy-mm").addEventListener("click", function () {
      dif = "easy";
    });
    document.getElementById("med-mm").addEventListener("click", function () {
      dif = "med";
    });
    document.getElementById("hard-mm").addEventListener("click", function () {
      dif = "hard";
    });
    document.getElementById("easy-mob").addEventListener("click", function () {
      dif = "easy";
    });
    document.getElementById("med-mob").addEventListener("click", function () {
      dif = "med";
    });
    document.getElementById("hard-mob").addEventListener("click", function () {
      dif = "hard";
    });
    document.getElementById("start").addEventListener("click", function () {
      if(dif == "easy") {
        createGameArea("easy");
      } else if(dif == "med") {
        createGameArea("med");
      } else {
        createGameArea("hard");
      }
      createGuessMenues();
      generateCode(dif);
    });
    document.getElementById("reset").addEventListener("click", function () {
      reset();
    });
    document.getElementById("guess").addEventListener("click", function () {
      plyrGuess(dif, seq.length);
    });
    document.getElementById("start-mob").addEventListener("click", function () {
      if(dif == "easy") {
        createGameArea("easy");
      } else if(dif == "med") {
        createGameArea("med");
      } else {
        createGameArea("hard");
      }
      createGuessMenues();
      generateCode(dif);
    });
    document.getElementById("reset-mob").addEventListener("click", function () {
      reset();
    });
    document.getElementById("guess-mob").addEventListener("click", function () {
      plyrGuess(dif, seq.length);
    });
  
    function createGameArea(dif) {
      $(".game-area").html(`
        <div class="row empty-block mobile"></div>
        <divclass="row mobile">
          <div class="col-md-12">
            <h3>Reveal the Code!</h3>
          </div>
        </div>
        <div class="row">
          <div class="col-1 col-md-1"></div>
          <div id="target1" class="col-2 col-md-2 target">
            <i class="fas fa-question" aria-hidden="true"></i>
          </div>
          <div id="target2" class="col-2 col-md-2 target">
            <i class="fas fa-question" aria-hidden="true"></i>
          </div>
          <div id="target3" class="col-2 col-md-2 target">
            <i class="fas fa-question" aria-hidden="true"></i>
          </div>
          <div id="target4" class="col-2 col-md-2 target">
            <i class="fas fa-question" aria-hidden="true"></i>
          </div>
          <div id="target5" class="col-2 col-md-2 target">
            <i class="fas fa-question" aria-hidden="true"></i>
          </div>
          <div class="col-1 col-md-1"></div>
        </div>
        <div class="row empty-block mobile"></div>
        <divclass="row">
          <div class="col-md-12">
            <h3>Guess Here!</h3>
          </div>
        </div>
        <div class="row">
          <div class="col-1 col-md-1"></div>
          <div id="guess1" class="col-2 col-md-2 target"></div>
          <div id="guess2" class="col-2 col-md-2 target"></div>
          <div id="guess3" class="col-2 col-md-2 target"></div>
          <div id="guess4" class="col-2 col-md-2 target"></div>
          <div id="guess5" class="col-2 col-md-2 target"></div>
          <div class="col-1 col-md-1"></div>
        </div>
        <div class="row empty-block mobile"></div>
        <divclass="row">
          <div class="col-md-12">
            <h3>Previous Guess</h3>
          </div>
        </div>
        <div class="row">
          <div class="col-1 col-md-1"></div>
          <div id="pguess1" class="col-2 col-md-2 target"></div>
          <div id="pguess2" class="col-2 col-md-2 target"></div>
          <div id="pguess3" class="col-2 col-md-2 target"></div>
          <div id="pguess4" class="col-2 col-md-2 target"></div>
          <div id="pguess5" class="col-2 col-md-2 target"></div>
          <div class="col-1 col-md-1"></div>
        </div>
      `)
      if(dif == "easy") {
        $("#guess1, #guess2, #guess3, #guess4, #guess5").removeClass("hide");
        $("#pguess1, #pguess2, #pguess3, #pguess4, #pguess5").removeClass("hide");
        $("#target1, #target2, #target3, #target4, #target5").removeClass("hide");
        $("#guess4, #guess5").addClass("hide");
        $("#pguess4, #pguess5").addClass("hide");
        $("#target4, #target5").addClass("hide");
      } else if(dif == "med") {
        $("#guess1, #guess2, #guess3, #guess4, #guess5").removeClass("hide");
        $("#pguess1, #pguess2, #pguess3, #pguess4, #pguess5").removeClass("hide");
        $("#target1, #target2, #target3, #target4, #target5").removeClass("hide");
        $("#guess5").addClass("hide");
        $("#pguess5").addClass("hide");
        $("#target5").addClass("hide");
      } else {
        $("#guess1, #guess2, #guess3, #guess4, #guess5").removeClass("hide");
        $("#pguess1, #pguess2, #pguess3, #pguess4, #pguess5").removeClass("hide");
        $("#target1, #target2, #target3, #target4, #target5").removeClass("hide");
      }
    }
  
    function createGuessMenues() {
      $("#guess1").html(`
        <form>
          <select id="playerinput1" name="colors">
            <option value="select">Select</option>
            <option class="sored" value="0">Red</option>
            <option class="soorange" value="1">Orange</option>
            <option class="soyellow" value="2">Yellow</option>
            <option class="sogreen" value="3">Green</option>
            <option class="soblue" value="4">Blue</option>
          </select>
        </form>
      `);
      $("#guess2").html(`
        <form>
          <select id="playerinput2" name="colors">
            <option value="select">Select</option>
            <option class="sored" value="0">Red</option>
            <option class="soorange" value="1">Orange</option>
            <option class="soyellow" value="2">Yellow</option>
            <option class="sogreen" value="3">Green</option>
            <option class="soblue" value="4">Blue</option>
            </select>
        </form>
      `);
      $("#guess3").html(`
        <form>
          <select id="playerinput3" name="colors">
            <option value="select">Select</option>
            <option class="sored" value="0">Red</option>
            <option class="soorange" value="1">Orange</option>
            <option class="soyellow" value="2">Yellow</option>
            <option class="sogreen" value="3">Green</option>
            <option class="soblue" value="4">Blue</option>
          </select>
        </form>
      `);
      $("#guess4").html(`
        <form>
          <select id="playerinput4" name="colors">
            <option value="select">Select</option>
            <option class="sored" value="0">Red</option>
            <option class="soorange" value="1">Orange</option>
            <option class="soyellow" value="2">Yellow</option>
            <option class="sogreen" value="3">Green</option>
            <option class="soblue" value="4">Blue</option>
          </select>
        </form>
      `);
      $("#guess5").html(`
        <form>
          <select id="playerinput5" name="colors">
            <option value="select">Select</option>
            <option class="sored" value="0">Red</option>
            <option class="soorange" value="1">Orange</option>
            <option class="soyellow" value="2">Yellow</option>
            <option class="sogreen" value="3">Green</option>
            <option class="soblue" value="4">Blue</option>
            </select>
        </form>
      `);
    }
  
    function reset() {
      $(".game-area").html(``);
      dif = "easy";
    }
  
    function plyrGuess(dif, num) {
      count = 0;
      for(var i = 0; i < num; i++) {
        var slot = "playerinput" + (i + 1);
        var inpt = document.getElementById(slot).value;
        if(inpt == "select") {
          count++;
        } else {
          plyr_guess.push(Number(inpt));
        }
      }
      if(count > 0) {
        alert("Please Complete your Guess!")
      } else {
        checkGuess(seq, plyr_guess);
        populatePrevGuess(plyr_guess);
        plyr_guess = [];
      }
    }
  
    function populatePrevGuess(ary1) {
      for(var i = 0; i < ary1.length; i++) {
        var slot = "#pguess" + (i + 1);
        if(ary1[i] == 0) {
          col = "Red";
        } else if(ary1[i] == 1) {
          col = "Orange";
        } else if(ary1[i] == 2) {
          col = "Yellow";
        } else if(ary1[i] == 3) {
          col = "Green";
        } else {
          col = "Blue";
        }
        $(slot).html(`<h4>${col}</h4>`);
      }
    }
  
    function checkGuess(ary1, ary2) {
      for(i in ary1) {
        if(ary1[i] == ary2[i]) {
          if(ary1[i] == 0) {
            col = "red";
            col2 = "yellow"
          } else if(ary1[i] == 1) {
            col = "orange";
            col2 = "red"
          } else if(ary1[i] == 2) {
            col = "yellow";
            col2 = "blue"
          } else if(ary1[i] == 3) {
            col = "green";
            col2 = "orange"
          } else {
            col = "blue";
            col2 = "green"
          }
          var slot = "#target" + (Number(i) + 1);
          $(slot).css("background-color", col);
          $(slot).css("color", col2);
          $(slot).html(`<i class="far fa-check-square" aria-hidden="true"></i>`);
        }
      }
    }
  
    function generateCode(dif) {
      let seq_count = 0;
      if(dif == "easy") {
        while(seq_count < 3) {
          seq.push(Math.floor(Math.random() * 5));
          seq_count++;
        }
      } else if(dif == "med") {
        while(seq_count < 4) {
          seq.push(Math.floor(Math.random() * 5));
          seq_count++;
        }
      } else {
        while(seq_count < 5) {
          seq.push(Math.floor(Math.random() * 5));
          seq_count++;
        }
      }
    }
  })