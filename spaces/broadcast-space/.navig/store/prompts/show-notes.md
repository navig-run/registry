# Show Notes

## Purpose
Generate structured show notes from an episode transcript.

## Variables
- `{{EPISODE_TITLE}}` — Episode title
- `{{EPISODE_NUMBER}}` — Episode number
- `{{GUEST_NAME}}` — Guest name (if applicable)
- `{{TRANSCRIPT}}` — Full or partial transcript text
- `{{PUBLISH_DATE}}` — Publication date

## Prompt

Generate professional show notes for **Episode {{EPISODE_NUMBER}}: {{EPISODE_TITLE}}**.

**Guest**: {{GUEST_NAME}}
**Publish Date**: {{PUBLISH_DATE}}

Based on the transcript, create:

### 1. Episode Description
- 2-3 paragraph summary for podcast platforms
- Optimised for search (include key terms)
- Engaging hook in the first sentence

### 2. Key Timestamps
| Time | Topic |
|------|-------|

Mark every major topic transition with a timestamp.

### 3. Key Takeaways
- 5-7 bullet points of main insights
- Each takeaway should standalone as a social media post

### 4. Notable Quotes
- 3-5 quotable moments with exact timestamps
- Format: "Quote text" — Speaker (timestamp)

### 5. Resources Mentioned
| Resource | Type | Link |
|----------|------|------|

### 6. Guest Links
- Website, social media, books, projects mentioned

### 7. Episode Credits
- Host, guest, editor, producer
- Music credits
- Sponsor mentions (if applicable)

### 8. SEO Tags
- 10-15 relevant keywords for platform discoverability
