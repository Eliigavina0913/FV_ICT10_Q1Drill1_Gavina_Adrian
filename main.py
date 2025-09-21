from js import document, console
from pyscript import when

@when("click", "#computeBtn")
def compute_result(event=None):
    console.log("✅ Button clicked!")  
    s1 = document.getElementById("score1").value
    s2 = document.getElementById("score2").value

    if s1 and s2:
        avg = (float(s1) + float(s2)) / 2
        document.getElementById("result").innerText = f"Average: {avg:.2f}"
    else:
        document.getElementById("result").innerText = "⚠️ Please enter both scores!"




#I used chatgpt and co pilot to fix the problems in my code