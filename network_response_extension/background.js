let requestMap = new Map();

// Initialize debugger when extension starts
chrome.runtime.onInstalled.addListener(() => {
  initializeDebugger();
});

function initializeDebugger() {
  chrome.tabs.query({}, (tabs) => {
    tabs.forEach(tab => {
      if (tab.url && tab.url.startsWith('http')) {
        attachDebugger(tab.id);
      }
    });
  });
}

function attachDebugger(tabId) {
  chrome.debugger.attach({ tabId }, '1.0', () => {
    if (chrome.runtime.lastError) {
      console.log('Debugger attach error:', chrome.runtime.lastError);
      return;
    }
    chrome.debugger.sendCommand({ tabId }, 'Network.enable');
  });
}

// Attach debugger to new tabs
chrome.tabs.onCreated.addListener((tab) => {
  if (tab.url && tab.url.startsWith('http')) {
    attachDebugger(tab.id);
  }
});

// Listen for network response events
chrome.debugger.onEvent.addListener((source, method, params) => {
  if (method === 'Network.responseReceived') {
    const requestId = params.requestId;
    chrome.debugger.sendCommand(
      { tabId: source.tabId },
      'Network.getResponseBody',
      { requestId: requestId },
      (response) => {
        if (response) {
          const requestData = requestMap.get(requestId) || {};
          requestData.response = response.body;
          requestMap.set(requestId, requestData);
        }
      }
    );
  }
});

// Listen for network requests
chrome.webRequest.onBeforeRequest.addListener(
  (details) => {
    requestMap.set(details.requestId, {
      url: details.url,
      timestamp: Date.now(),
      response: null
    });
  },
  { urls: ['<all_urls>'] },
  ['requestBody']
);

// Clean up old requests every 5 minutes
setInterval(() => {
  const fiveMinutesAgo = Date.now() - 300000;
  for (let [requestId, requestData] of requestMap) {
    if (requestData.timestamp < fiveMinutesAgo) {
      requestMap.delete(requestId);
    }
  }
}, 300000);
