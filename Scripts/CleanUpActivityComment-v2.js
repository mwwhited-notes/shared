/* https://myactivity.google.com/page?page=youtube_comment_likes */
(async function() {
    function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

    // Scroll to bottom to load all items
    async function scrollToBottom() {
        let lastHeight = document.body.scrollHeight;
        while (true) {
            window.scrollTo(0, document.body.scrollHeight);
            await sleep(2000); // Wait for new items to load
            let newHeight = document.body.scrollHeight;
            if (newHeight === lastHeight) break;
            lastHeight = newHeight;
        }
        console.log(`[${new Date().toLocaleTimeString()}] Finished scrolling. All items should be loaded.`);
    }

    // Delete activity items by prefix in aria-label
    async function deleteActivities(prefix) {
        let buttons = Array.from(document.querySelectorAll(`button[aria-label^="${prefix}"]`));
        console.log(`[${new Date().toLocaleTimeString()}] Found ${buttons.length} "${prefix}" delete buttons`);
        for (let i = 0; i < buttons.length; i++) {
            let btn = buttons[i];
            let label = btn.getAttribute('aria-label');
            console.log(`[${new Date().toLocaleTimeString()}] Deleting item ${i + 1}/${buttons.length}: "${label}"`);
            btn.click();
            await sleep(50); // Wait for confirmation dialog

            // Click confirm if it appears
            let confirmBtn = document.querySelector('button[name="ok"], button[jsname="LgbsSe"]');
            if (confirmBtn) {
                confirmBtn.click();
                console.log(`[${new Date().toLocaleTimeString()}] Confirmed deletion: "${label}"`);
                await sleep(50);
            }
        }
    }

    await scrollToBottom();
    await deleteActivities("Delete activity item I");  // For YouTube comments
    await deleteActivities("Delete activity item Liked");  // For YouTube comment likes

    console.log(`[${new Date().toLocaleTimeString()}] Finished attempting all deletions. Run again if new items loaded dynamically.`);
})();
