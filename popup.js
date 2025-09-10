document.getElementById("analyzeBtn").addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript(
    {
      target: { tabId: tab.id },
      func: () => document.body.innerText
    },
    async (injectionResults) => {
      let pageText = injectionResults[0].result;

      let response = await fetch("http://127.0.0.1:8080/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: pageText })
      });

      let data = await response.json();

      document.getElementById("score").innerText =
        "Credibility Score: " + data.credibility_score;
      document.getElementById("label").innerText = "Label: " + data.label;
      document.getElementById("explanation").innerText =
        "Why: " + data.explanation;
    }
  );
});


