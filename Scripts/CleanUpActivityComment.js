/* https://myactivity.google.com/page?page=youtube_comment_likes */
(async function() {
    function sleep(ms) { return new Promise(resolve => setTimeout(resolve, ms)); }

    async function scrollToBottom() {
        let lastHeight = document.body.scrollHeight;
        while (true) {
            window.scrollTo(0, document.body.scrollHeight);
            await sleep(200);
            let newHeight = document.body.scrollHeight;
            if (newHeight === lastHeight) break;
            lastHeight = newHeight;
        }
        console.log(`[${new Date().toLocaleTimeString()}] Finished scrolling. All items should be loaded.`);
    }

    async function deleteActivities(prefix) {
        let buttons = Array.from(document.querySelectorAll(`button[aria-label^="${prefix}"]`));
        while (buttons.length > 0) {
            for (let i = 0; i < buttons.length; i++) {
                let btn = buttons[i];
                let label = btn.getAttribute('aria-label');
                console.log(`[${new Date().toLocaleTimeString()}] Deleting item: "${label}"`);
                btn.click();
                await sleep(50);

                let confirmBtn = document.querySelector('button[name="ok"], button[jsname="LgbsSe"]');
                if (confirmBtn) {
                    confirmBtn.click();
                    console.log(`[${new Date().toLocaleTimeString()}] Confirmed deletion: "${label}"`);
                    await sleep(50);
                }
            }
            await scrollToBottom();
            buttons = Array.from(document.querySelectorAll(`button[aria-label^="${prefix}"]`));
        }
        console.log(`[${new Date().toLocaleTimeString()}] All "${prefix}" items deleted.`);
    }

    await scrollToBottom();
    await deleteActivities("Delete activity item I");        // YouTube comments
    await deleteActivities("Delete activity item Liked");    // YouTube comment likes

    console.log(`[${new Date().toLocaleTimeString()}] Finished all deletions. No items left.`);
})();
