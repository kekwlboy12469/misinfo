document.getElementById("analyzeBtn").addEventListener("click", async () => {
  let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

  chrome.scripting.executeScript(
    {
      target: { tabId: tab.id },
      func: () => {
        let caption = "";
        let imageUrl = "";

        // Only focus on post image, ignore comments
        let imgEl = document.querySelector("article img, img[srcset]"); 
        if (imgEl) imageUrl = imgEl.src;

        // Try caption (Instagram caption OR article headline)
        let captionEl = document.querySelector("h1, h2, meta[property='og:title']");
        if (captionEl) caption = captionEl.innerText || captionEl.content || "";

        return { caption, imageUrl };
      }
    },
    async (injectionResults) => {
      let { caption, imageUrl } = injectionResults[0].result;

      let response = await fetch("http://127.0.0.1:8080/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: caption, image: imageUrl }) // send both
      });

      let data = await response.json();

      document.getElementById("score").innerText =
  "Credibility Score: " + (data.credibility_score ?? "N/A") + "/100";

document.getElementById("textLabel").innerText =
  "Text Label: " + (data.text_label ?? "N/A");

document.getElementById("textWhy").innerText =
  "Text Why: " + (data.text_explanation ?? "N/A");

document.getElementById("imageLabel").innerText =
  "Image Label: " + (data.image_label ?? "N/A");

document.getElementById("imageWhy").innerText =
  "Image Why: " + (data.image_explanation ?? "N/A");

      document.getElementById("textLabel").innerText =
        "Text Label: " + (data.text_label ?? "N/A");
      document.getElementById("textWhy").innerText =
        "Text Why: " + (data.text_explanation ?? "N/A");
      document.getElementById("imageLabel").innerText =
        "Image Label: " + (data.image_label ?? "N/A");
      document.getElementById("imageWhy").innerText =
        "Image Why: " + (data.image_explanation ?? "N/A");
    }
  );
});


