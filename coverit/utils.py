from django.http import HttpResponse

def dynamic_spinner_script(request):
    js_code = """
    (function() {
        const spinner = document.createElement("div");
        spinner.id = "fullpage-spinner";
        spinner.setAttribute("data-state", "off");

        const spinnerInner = document.createElement("div");
        spinnerInner.className = "spinner";

        // Apply styles using JavaScript
        Object.assign(spinner.style, {
            position: "fixed",
            top: "0",
            left: "0",
            width: "100%",
            height: "100%",
            background: "rgba(0, 0, 0, 0.5)",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            zIndex: "9999",
            visibility: "hidden",
            opacity: "0",
            transition: "opacity 0.3s ease-in-out"
        });

        Object.assign(spinnerInner.style, {
            width: "50px",
            height: "50px",
            border: "5px solid #f3f3f3",
            borderTop: "5px solid #3498db",
            borderRadius: "50%",
            animation: "spin 1s linear infinite"
        });

        // Append to the body
        spinner.appendChild(spinnerInner);
        document.body.appendChild(spinner);

        // Add keyframe animation
        const styleSheet = document.styleSheets[0] || document.createElement("style");
        styleSheet.insertRule(`
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        `, styleSheet.cssRules.length);

        // Function to toggle spinner
        window.toggleSpinner = function(state) {
            if (state === "on") {
                spinner.setAttribute("data-state", "on");
                spinner.style.visibility = "visible";
                spinner.style.opacity = "1";
            } else if (state === "off") {
                spinner.setAttribute("data-state", "off");
                spinner.style.visibility = "hidden";
                spinner.style.opacity = "0";
            } else {
                console.warn("Invalid state. Use 'on' or 'off'.");
            }
        };

        // Prevent removal from DevTools
        setInterval(() => {
            if (!document.body.contains(spinner)) {
                document.body.appendChild(spinner);
            }
        }, 1000);

        // Automatically turn on the spinner for testing
        //toggleSpinner("on");
    })();
    """
    return HttpResponse(js_code, content_type="application/javascript")
