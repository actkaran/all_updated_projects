let currentResponse = null;
let searchInterval = null;

document.addEventListener('DOMContentLoaded', function() {
  const urlInput = document.getElementById('urlInput');
  const submitBtn = document.getElementById('submitBtn');
  const downloadBtn = document.getElementById('downloadBtn');
  const responseContainer = document.getElementById('responseContainer');
  const statusText = document.getElementById('statusText');

  // Restore previous search if exists
  chrome.storage.local.get(['lastSearch', 'lastResponse'], (data) => {
    if (data.lastSearch) {
      urlInput.value = data.lastSearch;
      if (data.lastResponse) {
        displayResponse(data.lastResponse);
      }
    }
  });

  function displayResponse(response) {
    currentResponse = response;
    downloadBtn.disabled = false;

    try {
      // Try to parse as JSON
      const jsonData = JSON.parse(response);
      responseContainer.innerHTML = `<pre class="json-response">${JSON.stringify(jsonData, null, 2)}</pre>`;
    } catch {
      // If not JSON, display as text/html
      responseContainer.innerHTML = `<div class="json-response">${response}</div>`;
    }
  }

  function startSearch(searchPattern) {
    if (searchInterval) {
      clearInterval(searchInterval);
    }

    let attempts = 0;
    const maxAttempts = 10; // Maximum number of refresh attempts

    async function searchAndRefresh() {
      const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
      
      statusText.textContent = `Searching... Attempt ${attempts + 1}/${maxAttempts}`;
      
      chrome.runtime.sendMessage(
        { 
          action: 'findResponse', 
          pattern: searchPattern, 
          tabId: tab.id 
        },
        async (response) => {
          if (response.error) {
            attempts++;
            if (attempts >= maxAttempts) {
              clearInterval(searchInterval);
              statusText.textContent = 'Max attempts reached. No matching response found.';
              return;
            }
            // Refresh the page and continue searching
            chrome.tabs.reload(tab.id);
          } else {
            clearInterval(searchInterval);
            statusText.textContent = 'Response found!';
            displayResponse(response.data);
            
            // Save the search and response
            chrome.storage.local.set({
              lastSearch: searchPattern,
              lastResponse: response.data
            });
          }
        }
      );
    }

    // Start immediate search
    searchAndRefresh();
    // Continue searching every 3 seconds
    searchInterval = setInterval(searchAndRefresh, 3000);
  }

  submitBtn.addEventListener('click', () => {
    const searchPattern = urlInput.value.trim();
    if (!searchPattern) {
      statusText.textContent = 'Please enter a URL pattern';
      return;
    }
    responseContainer.innerHTML = '';
    downloadBtn.disabled = true;
    startSearch(searchPattern);
  });

  downloadBtn.addEventListener('click', () => {
    if (!currentResponse) return;

    const blob = new Blob([currentResponse], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
    
    chrome.downloads.download({
      url: url,
      filename: `response-${timestamp}.html`,
      saveAs: true
    });
  });
});
