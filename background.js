chrome.runtime.onInstalled.addListener(() => {
  console.log("✅ Credibility Checker Extension Installed");
});

// Listen for messages (optional debug)
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  console.log("📩 Message in background.js:", message);
  sendResponse({ status: "Background script alive" });
});
