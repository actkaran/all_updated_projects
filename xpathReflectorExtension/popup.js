document.getElementById("submitXpath").addEventListener("click", async () => {
  const xpath = document.getElementById("xpathInput").value;
  if (xpath) {
    // Get the active tab in the current window
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    // Execute the script in the context of the active tab
    chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: getElementValueByXPath,
      args: [xpath]
    }, (results) => {
      // Display the result if it's available
      if (results && results[0] && results[0].result !== null) {
        document.getElementById("result").textContent = results[0].result;
      } else {
        document.getElementById("result").textContent = "Element not found or invalid XPath.";
      }
    });
  } else {
    document.getElementById("result").textContent = "Please enter a valid XPath.";
  }
});

// This function will be executed on the current tab
function getElementValueByXPath(xpath) {
  try {
    const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    return element ? element.textContent || element.value || "Element found but has no visible text or value." : null;
  } catch (error) {
    return "Invalid XPath or error occurred.";
  }
}
