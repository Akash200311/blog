









var count=0;
var a=0;
var b=0;

function fire()
{  
    
    document.getElementById("s1").style.transition="0.9s";
document.getElementById("s2").style.transition="0.9s";
    document.getElementById("s1").style.translate="-100%";
    document.getElementById("s2").style.translate="110%";
   
    function wait()
    {
        document.getElementById("body").style.display="nbody";
        document.getElementById("three").style.display="nbody";
  
      
        document.getElementById("a").style.display="flex";
        document.getElementById("two").style.padding="3%";

        
        
    }
    setTimeout(wait,1100)

}


function state()
{
    if(count%2==0)
    {
    document.getElementById("s-c").src="/static/on-button.png";
    document.getElementById("body").style.backgroundColor="rgba(0,0,0,0.85)";
    document.getElementById("body").style.color="white";
}

    if(count%2!=0)
    { document.getElementById("s-c").src="/static/off-button.png";
    document.getElementById("body").style.backgroundColor="white";
    document.getElementById("body").style.color="black";

   
  
    }
    count=count+1;
}






function fire1()
{  


    document.getElementById("body").style.display="block";
    document.getElementById("three").style.display="block";
    document.getElementById("a").style.display="nbody";

    document.getElementById("s1").style.translate="-110%";
    document.getElementById("s2").style.translate="110%";
    
    function wait()
    { document.getElementById("s1").style.transition="0.9s";
    document.getElementById("s2").style.transition="0.9s";
        
        document.getElementById("three").style.display="block";
      
        document.getElementById("s1").style.translate="0%";
        document.getElementById("s2").style.translate="0%";
      
       
        document.getElementById("two").style.padding="7%";
      
     

        
        
    }
    setTimeout(wait,1100)

}


function state1()
{
    if(count%2==0)
    {
    document.getElementById("s-c1").src="/static/on-button.png";
    document.getElementById("body").style.backgroundColor="rgba(0,0,0,0.85)";
    
    document.getElementById("body").style.color="white";
   
    document.getElementById("body").style.color="white";
}

    if(count%2!=0)
    { document.getElementById("s-c1").src="/static/off-button.png";
    document.getElementById("body").style.backgroundColor="white";
    document.getElementById("body").style.color="black";


   
  
    }
    count=count+1;
}
var c=0;
function state2()
{
    if(c%2==0)
    {
    document.getElementById("s-c2").src="/static/on-button.png";
    document.getElementById("body").style.backgroundColor="rgba(0,0,0,0.85)";
    document.getElementById("body").style.color="white";
}

    if(c%2!=0)
    { document.getElementById("s-c2").src="/static/off-button.png";
    document.getElementById("body").style.backgroundColor="white";
    document.getElementById("body").style.color="black";
    

   
  
    }
    c=c+1;
 
}





















$('.slider').each(function() {
var $this = $(this);
var $group = $this.find('.slide_group');
var $slides = $this.find('.slide');
var bulletArray = [];
var currentIndex = 0;
var timeout;

function move(newIndex) {
var animateLeft, slideLeft;

advance();

if ($group.is(':animated') || currentIndex === newIndex) {
return;
}

bulletArray[currentIndex].removeClass('active');
bulletArray[newIndex].addClass('active');

if (newIndex > currentIndex) {
slideLeft = '100%';
animateLeft = '-100%';
} else {
slideLeft = '-100%';
animateLeft = '100%';
}

$slides.eq(newIndex).css({
display: 'block',
left: slideLeft
});
$group.animate({
left: animateLeft
}, function() {
$slides.eq(currentIndex).css({
display: 'none'
});
$slides.eq(newIndex).css({
left: 0
});
$group.css({
left: 0
});
currentIndex = newIndex;
});
}

function advance() {
clearTimeout(timeout);
timeout = setTimeout(function() {
if (currentIndex < ($slides.length - 1)) {
move(currentIndex + 1);
} else {
move(0);
}
}, 4000);
}

$('.next_btn').on('click', function() {
if (currentIndex < ($slides.length - 1)) {
move(currentIndex + 1);
} else {
move(0);
}
});

$('.previous_btn').on('click', function() {
if (currentIndex !== 0) {
move(currentIndex - 1);
} else {
move(3);
}
});

$.each($slides, function(index) {
var $button = $('<a class="slide_btn">&bull;</a>');

if (index === currentIndex) {
$button.addClass('active');
}
$button.on('click', function() {
move(index);
}).appendTo('.slide_buttons');
bulletArray.push($button);
});

advance();
});



const questionContainers = document.querySelectorAll('.question-container');
const answers = document.querySelectorAll('.answer');
let activeAnswer = answers[0];

// Adds the visible class to the first answer and rotate class to the first toggle button
questionContainers[0].querySelector('.toggle-btn p').classList.add('rotate');
activeAnswer.classList.add('visible');

questionContainers.forEach((container, index) => {
container.addEventListener('click', () => {
const answer = answers[index];
const toggleBtn = container.querySelector('.toggle-btn p');

if (activeAnswer !== null && activeAnswer !== answer) {
const activeToggleBtn = activeAnswer.previousElementSibling.querySelector('.toggle-btn p');
activeToggleBtn.classList.remove('rotate');
activeAnswer.classList.remove('visible');
}

toggleBtn.classList.toggle('rotate');

if (answer.classList.contains('visible')) {
answer.classList.remove('visible');
activeAnswer = null;
} else {
answers.forEach(a => {
a.classList.remove('visible');
});
answer.classList.add('visible');
activeAnswer = answer;
}
});
});
var c=0;


function answer()
{
if(c%2==0)
{
document.getElementById("answer1").style.display="block";
document.getElementById("block1").style.backgroundColor="rgba(0, 0, 0, 0.4)";
}
if(c%2!=0)
{document.getElementById("answer1").style.display="none";
document.getElementById("block1").style.backgroundColor="white";

}

c=c+1;
}
c=0;




function answer2()
{
if(a%2==0)
{
document.getElementById("answer2").style.display="block";
document.getElementById("block2").style.backgroundColor="rgba(0, 0, 0, 0.4)";


}
if(a%2!=0)
{document.getElementById("answer2").style.display="none";
document.getElementById("block2").style.backgroundColor="white";

}

a=a+1;
}
a=0

function answer3()
{
if(b%2==0)
{
document.getElementById("answer3").style.display="block";
document.getElementById("block3").style.backgroundColor="rgba(0, 0, 0, 0.4)";


}
if(b%2!=0)
{document.getElementById("answer3").style.display="none";
document.getElementById("block3").style.backgroundColor="white";

}

b=b+1;
}
b=0

















