-- Siri Safari Search AppleScript
-- This script asks you what to search for, then opens Safari with that search.
-- You can trigger this via Siri using the Shortcuts app.

on run
    -- Ask Siri / Shortcuts for the search query
    set searchQuery to text returned of (display dialog "What do you want me to search for?" default answer "" buttons {"Cancel", "Search"} default button "Search" with title "Siri Safari Search")

    if searchQuery is "" then
        display notification "No search query provided." with title "Siri Safari Search"
        return
    end if

    -- URL-encode the search query (replace spaces with + for Safari/Google)
    set encodedQuery to my urlEncode(searchQuery)

    -- Build the Safari search URL (Google search)
    set searchURL to "https://www.google.com/search?q=" & encodedQuery

    -- Tell Safari to open the search in a new tab
    tell application "Safari"
        activate
        -- Open a new document (tab) with the search URL
        open location searchURL
    end tell

    display notification "Searching Safari for: " & searchQuery with title "Siri Safari Search"
end run

-- Helper: encode spaces and special characters for a URL
on urlEncode(theText)
    set encodedText to ""
    repeat with i from 1 to length of theText
        set theChar to character i of theText
        if theChar is " " then
            set encodedText to encodedText & "+"
        else if theChar is "&" then
            set encodedText to encodedText & "%26"
        else if theChar is "=" then
            set encodedText to encodedText & "%3D"
        else if theChar is "#" then
            set encodedText to encodedText & "%23"
        else if theChar is "?" then
            set encodedText to encodedText & "%3F"
        else
            set encodedText to encodedText & theChar
        end if
    end repeat
    return encodedText
end urlEncode
