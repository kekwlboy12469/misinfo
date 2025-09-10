chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "getPageSelection") {
    sendResponse({ selection: window.getSelection().toString() });
  }
});
