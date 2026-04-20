const display = document.querySelector("#display h1");

const buttons = document.querySelector("#number")


let currentValue = "";

buttons.forEach(button => {
    button.addEventListener("click", function () {
        const value = this.innerText;

        if (value === "Ac") {
            // Clear everything
            currentValue = "";
            display.innerText = "Enter your Value";
        }
        else if (value === "C") {
            // Will remove the last number
            currentValue = currentValue.slice(0, -1);
            display.innerText = currentValue || "Enter your value";
        }
        else if (value === "=") {
            // Calculate result 
            try {
                // Replace symbols 
                let result = currentValue
                    .replace("X", "*")
                    .replace("÷", "/");

                display.innerText = eval(result);
                currentValue = display.innerText;
            } catch {
                display.innerText = "Error";
                currentValue = "";
            }
        }
        else if (value === "√") {
            // Sqaure root
            currentValue = Math.sqrt(Number(currentValue)).toString();
            display.innerText = currentValue;
        } else if (value === "%") {
            // perctange
            currentValue = (Number(currentValue) / 100).toString();
            display.innerTExt = currentValue;
        }
        else {
            //numbers and operators
            currentValue += value;
            display.innerText = currentValue;
        }

    });
});