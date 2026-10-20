# 🎤 Siri → Open Safari & Search

Make Siri open a Safari tab and search for anything you say.

## What this does

You say something like *"Hey Siri, search Safari for pizza near me"* and Siri will:
1. Ask you what to search for (or use your spoken phrase)
2. Open Safari
3. Open a new tab with your search

---

## Option 1: Shortcuts App (Recommended - No coding)

### On iPhone/iPad:
1. Open the **Shortcuts** app
2. Tap the **+** (plus) in the top-right to create a new shortcut
3. Tap **Add Action**
4. Search for and add: **Ask for Input**
   - Set prompt to: "What do you want to search for?"
5. Search for and add: **Open URL**
   - Set the URL to: `https://www.google.com/search?q=[Your Input]`
   - Tap the variable bubble (the little `x` in a circle) above the keyboard and select the "Ask for Input" result
6. Tap **…** (three dots) → **Add to Siri**
7. Record a phrase like: *"Search Safari for ___"* or *"Safari search ___"*
8. Tap **Done**

### On Mac:
1. Open the **Shortcuts** app
2. Click **+** to create a new shortcut
3. Add action: **Ask for Input** (prompt: "What do you want to search for?")
4. Add action: **Open URL** (use the input variable as the URL, e.g. `https://www.google.com/search?q=<input>`)
5. Click **Details** (the `i` icon) → check **Add to Siri**
6. Record your Siri phrase
7. Save

---

## Option 2: AppleScript (Mac only)

I've included `Siri_Safari_Search.applescript` in this folder.

### To use it with Siri:
1. Open the **Shortcuts** app on your Mac
2. Create a new shortcut
3. Add action: **Run AppleScript**
4. Paste the contents of `Siri_Safari_Search.applescript`
5. Add to Siri and record a phrase like *"Safari search"*

### To run it directly:
- Open **Script Editor** (in Applications > Utilities)
- Open `Siri_Safari_Search.applescript`
- Click the **Run** (▶) button

---

## Example Siri phrases (after setup)

- "Hey Siri, search Safari for weather tomorrow"
- "Hey Siri, Safari search best pizza near me"
- "Hey Siri, look up how to bake a cake"

---

## Files in this folder

| File | Purpose |
|------|---------|
| `Siri_Safari_Search.applescript` | AppleScript that prompts for a query and opens Safari with a Google search |

---

## Troubleshooting

- **Safari doesn't open**: Make sure Safari is installed and is your default browser.
- **Search doesn't work**: Check that you have an internet connection.
- **"Add to Siri" not available**: Make sure you're signed into iCloud and Siri is enabled in Settings.
