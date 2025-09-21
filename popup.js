document.getElementById("analyzeBtn").addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript(
    {
      target: { tabId: tab.id },
      func: () => {
        let caption = "";
        let host = window.location.hostname;

        
        if (host.includes("instagram.com")) {
          let captionEl =
            document.querySelector("article h1") ||
            document.querySelector("article span") ||
            document.querySelector("meta[property='og:title']");
          if (captionEl) caption = captionEl.innerText || captionEl.content || "";
        }

        
        else if (document.querySelector("article") || document.querySelector("h1")) {
          let headline =
            document.querySelector("h1") ||
            document.querySelector("meta[property='og:title']") ||
            document.querySelector("title");
          if (headline) caption = headline.innerText || headline.content || headline.textContent;
        }

        return caption?.trim() || null;
      }
    },
    async (injectionResults) => {
      let caption = injectionResults[0].result;
      const resultsDiv = document.getElementById("results");
      resultsDiv.innerHTML = "";

      if (!caption) {
        resultsDiv.innerHTML = `<p class="error">❌ No text found on this page.</p>`;
        return;
      }

      try {
      
        const response = await fetch("http://127.0.0.1:8080/analyze", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({ text: caption })
        });

        if (!response.ok) throw new Error(`Server error: ${response.status}`);
        const data = await response.json();

        
        let labelClass = "neutral";
        if (data.text_label?.toLowerCase().includes("real")) labelClass = "real";
        else if (data.text_label?.toLowerCase().includes("fake")) labelClass = "fake";
        else if (data.text_label?.toLowerCase().includes("misleading")) labelClass = "misleading";

      
        let explanationItems = [];
        if (data.text_explanation) {
          explanationItems = data.text_explanation
            .split(/\n|-/) 
            .map(line => line.trim())
            .filter(line => line.length > 3); 
        }

        resultsDiv.innerHTML = `
          <div class="result-card">
            <h3>🔍 Analysis Result</h3>
            <p><strong>Credibility Score:</strong> 
              <span class="score">${data.credibility_score ?? "N/A"}/100</span>
            </p>
            <p><strong>Text Label:</strong> 
              <span class="label ${labelClass}">${data.text_label ?? "N/A"}</span>
            </p>
            <p><strong>Reasoning:</strong></p>
            <ul class="explanation">
              ${explanationItems.map(e => `<li>${e}</li>`).join("")}
            </ul>
          </div>
        `;
      } catch (err) {
        console.error(err);
        resultsDiv.innerHTML = `<p class="error">❌ Error: ${err.message}</p>`;
      }
    }
  );
});

