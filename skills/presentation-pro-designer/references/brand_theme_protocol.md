# Brand and Theme Protocol

## Brand Extraction

From brand guides, templates, logos, and sample decks, extract:
- primary, secondary, accent, neutral, surface, text, border colours
- heading and body fonts
- type scale
- logo variants and clear-space rules
- imagery style
- icon style
- voice and tone
- prohibited treatments

## Presentation Tokens

Represent design decisions as presentation tokens:

```yaml
presentation_tokens:
  colors:
    primary: "#2563EB"
    secondary: "#3B82F6"
    accent: "#F97316"
    background: "#F8FAFC"
    text_primary: "#0F172A"
  typography:
    heading_font: "Aptos Display"
    body_font: "Aptos"
  spacing:
    margin: 0.55
    gap: 0.25
  charts:
    label_size: 14
    gridlines: "minimal"
```

## Accessibility

- Normal text contrast should meet 4.5:1 where practical.
- Large text and chart elements should meet at least 3:1.
- Do not rely on colour alone.
- Keep projected text readable from the back of a room.
