document.getElementById("submitDict").addEventListener("click", async () => {
  const dictInput = document.getElementById("xpathDictInput").value;

  let xpathDict;
  try {
    xpathDict = JSON.parse(dictInput); // Parse the JSON input
  } catch (error) {
    document.getElementById("resultBox").textContent = "Invalid JSON format. Please enter a valid JSON dictionary.";
    return;
  }

  if (typeof xpathDict !== 'object' || xpathDict === null) {
    document.getElementById("resultBox").textContent = "Please enter a valid JSON dictionary.";
    return;
  }

  // Get the active tab
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  // Execute the function in the active tab with the dictionary as an argument
  chrome.scripting.executeScript({
    target: { tabId: tab.id },
    func: getValuesByXPathDict,
    args: [xpathDict]
  }, (results) => {
    if (results && results[0] && results[0].result) {
      const resultData = results[0].result;
      document.getElementById("resultBox").textContent = JSON.stringify(resultData, null, 2);
    } else {
      document.getElementById("resultBox").textContent = "No data found or error occurred.";
    }
  });
});

// This function runs in the context of the webpage
function getValuesByXPathDict(xpathDict) {
  const resultDict = {};

  for (const [key, xpath] of Object.entries(xpathDict)) {
    try {
      const element = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
      resultDict[key] = element ? element.textContent || element.value || "No visible text or value" : "Element not found";
    } catch (error) {
      resultDict[key] = "Invalid XPath";
    }
  }

  return resultDict;
}
