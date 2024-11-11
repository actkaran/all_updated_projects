document.getElementById("applyText").addEventListener("click", async () => {
    const text = document.getElementById("inputText").value;
    if (text) {
      const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
      chrome.scripting.executeScript({
        target: { tabId: tab.id },
        func: updateTextOnPage,
        args: [text]
      });
    }
  });
  
  function updateTextOnPage(text) {
    const textDisplay = document.createElement("div");
    textDisplay.innerText = text;
    textDisplay.style.position = "fixed";
    textDisplay.style.top = "10px";
    textDisplay.style.left = "10px";
    textDisplay.style.padding = "5px";
    textDisplay.style.backgroundColor = "yellow";
    textDisplay.style.zIndex = 10000;
    document.body.appendChild(textDisplay);
  }
  